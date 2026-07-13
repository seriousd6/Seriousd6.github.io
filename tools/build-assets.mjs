/* tools/build-assets.mjs — Phase-3 asset pipeline (runs after `astro build`).
 *
 * Produces the deployable static-asset tree inside dist/:
 *
 *   1. Vite-bundles the 17 page entries (assets/js/entries/*.js):
 *        - entry URLs stay STABLE (entries/<name>.js) so Base.astro and the
 *          verbatim HTML (templates, topics/index.html, word/index.html) never
 *          need to know about hashes;
 *        - shared code goes into content-HASHED, minified chunks
 *          (assets/js/chunks/*-<hash>.js);
 *        - dynamic imports (terms/places/ol-companion/apocrypha-reader) become
 *          hashed lazy chunks automatically.
 *   2. Externalizes core.js and tracker.js to their stable root-absolute URLs.
 *      Both are ALSO imported by inline <script type=module> blocks in page
 *      HTML (home/discipline/tracker pages); bundling a copy would create two
 *      module instances and break their shared subscriber state. They ship as
 *      minified stable files instead, imported by the bundles at runtime.
 *   3. Ships minified stable copies of the classic scripts (main.js,
 *      settings.js) and the inline-only leaf modules (store.js, sg-progress.js).
 *   4. Minifies every assets/css file in place (same URLs) and copies fonts,
 *      icons, share-scenes verbatim.
 *   5. Rewrites sw.js: the precache list between the BUILD:ASSETS markers is
 *      regenerated from what was actually emitted, and APP_CACHE_V is stamped
 *      with a digest of the emitted bytes — no more manual version bumps for
 *      JS/CSS changes.
 *   6. Copies the root PWA statics (manifest.json, favicons, offline.html).
 *
 * `astro dev` is untouched: tools/root-statics.mjs keeps serving the raw
 * source tree, which works as native unbundled ESM.
 */
import { build } from 'vite';
import { transform } from 'esbuild';
import { createHash } from 'node:crypto';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const DIST = path.join(ROOT, 'dist');
const SRC_JS = path.join(ROOT, 'assets', 'js');

// Modules that must keep their stable URL because inline page scripts import
// them directly. Bundles reference them as externals at these exact URLs.
const EXTERNAL_STABLE = ['core.js', 'tracker.js'];
// Stable files never reachable from bundles: classic scripts + inline-only leaves.
const COPY_STABLE = ['main.js', 'settings.js', 'store.js', 'sg-progress.js'];

if (!fs.existsSync(DIST)) {
  console.error('dist/ not found — run `astro build` first.');
  process.exit(1);
}

// ── 1+2. Bundle the entries ────────────────────────────────────────────────
const entryDir = path.join(SRC_JS, 'entries');
const entries = Object.fromEntries(
  fs.readdirSync(entryDir).filter(f => f.endsWith('.js'))
    .map(f => [f.replace(/\.js$/, ''), path.join(entryDir, f)])
);

await build({
  root: ROOT,
  logLevel: 'warn',
  configFile: false,
  build: {
    outDir: path.join(DIST, 'assets', 'js'),
    emptyOutDir: false,
    target: 'es2020',
    minify: 'esbuild',
    modulePreload: false, // GitHub Pages, no preload polyfill needed for stable graph
    rollupOptions: {
      input: entries,
      preserveEntrySignatures: 'allow-extension',
      output: {
        format: 'es',
        entryFileNames: 'entries/[name].js',
        // Chunks land at /assets/js/ depth (not a subdir): the source modules
        // were rewritten to resolve data URLs via core.js _resolve (stable
        // external), but keeping chunk depth == source depth is cheap defense
        // against any future import.meta.url-relative path sneaking in.
        chunkFileNames: '[name]-[hash].js',
      },
      external: (id) => EXTERNAL_STABLE.some(f => id === `/assets/js/${f}`),
    },
  },
  plugins: [{
    // Map any relative import that resolves to an EXTERNAL_STABLE file onto
    // its root-absolute URL and mark it external, so bundled code does
    // `import ... from '/assets/js/core.js'` at runtime — the same URL the
    // inline page scripts use → one module instance.
    name: 'stable-externals',
    resolveId(source, importer) {
      if (!importer || !source.startsWith('.')) return null;
      const resolved = path.resolve(path.dirname(importer), source.split('?')[0]);
      const base = path.basename(resolved);
      if (path.dirname(resolved) === SRC_JS && EXTERNAL_STABLE.includes(base)) {
        return { id: `/assets/js/${base}`, external: true };
      }
      return null;
    },
  }],
});

// ── 3. Stable minified JS files ────────────────────────────────────────────
async function minifyTo(rel, destRel) {
  const src = fs.readFileSync(path.join(ROOT, rel), 'utf8');
  const isCss = rel.endsWith('.css');
  const out = await transform(src, isCss ? { loader: 'css', minify: true }
                                         : { loader: 'js', minify: true });
  const dest = path.join(DIST, destRel);
  fs.mkdirSync(path.dirname(dest), { recursive: true });
  fs.writeFileSync(dest, out.code);
}
for (const f of [...EXTERNAL_STABLE, ...COPY_STABLE]) {
  await minifyTo(`assets/js/${f}`, `assets/js/${f}`);
}

// ── 4. CSS (minified, same URLs) + verbatim asset dirs ─────────────────────
for (const f of fs.readdirSync(path.join(ROOT, 'assets', 'css')).filter(f => f.endsWith('.css'))) {
  await minifyTo(`assets/css/${f}`, `assets/css/${f}`);
}
for (const dir of ['fonts', 'share-scenes']) {
  const from = path.join(ROOT, 'assets', dir);
  if (fs.existsSync(from)) fs.cpSync(from, path.join(DIST, 'assets', dir), { recursive: true });
}
for (const f of fs.readdirSync(path.join(ROOT, 'assets'))) {
  const from = path.join(ROOT, 'assets', f);
  if (fs.statSync(from).isFile()) fs.copyFileSync(from, path.join(DIST, 'assets', f));
}

// ── 5. sw.js: regenerate precache list + stamp APP_CACHE_V ────────────────
function walk(dir, out = []) {
  for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
    const p = path.join(dir, e.name);
    e.isDirectory() ? walk(p, out) : out.push(p);
  }
  return out;
}
const emitted = walk(path.join(DIST, 'assets'))
  .map(p => './' + path.relative(DIST, p).split(path.sep).join('/'))
  .filter(p => p.endsWith('.js') || p.endsWith('.css') || p.endsWith('.woff2'))
  .sort();

const digest = createHash('sha256');
for (const p of emitted) digest.update(fs.readFileSync(path.join(DIST, p)));
const hash = digest.digest('hex').slice(0, 12);

let sw = fs.readFileSync(path.join(ROOT, 'sw.js'), 'utf8');
sw = sw.replace(
  /(\/\/ ── BUILD:ASSETS-START ─+\n)[\s\S]*?(  \/\/ ── BUILD:ASSETS-END ─+\n)/,
  `$1  // (generated by tools/build-assets.mjs — bundled entries, hashed chunks,\n` +
  `  //  stable externals, minified CSS)\n` +
  emitted.map(p => `  '${p}',`).join('\n') + '\n$2'
);
sw = sw.replace(
  /var APP_CACHE_V {2}= 'bsw-app-[^']+';/,
  `var APP_CACHE_V  = 'bsw-app-${hash}';`
);
fs.writeFileSync(path.join(DIST, 'sw.js'), sw);

// ── 6. Root PWA statics ────────────────────────────────────────────────────
for (const f of ['manifest.json', 'favicon.ico', 'favicon.svg', 'offline.html', 'robots.txt']) {
  fs.copyFileSync(path.join(ROOT, f), path.join(DIST, f));
}

console.log(`[build-assets] ${emitted.length} JS/CSS assets emitted; APP_CACHE_V=bsw-app-${hash}`);

// ── 6.4 Lite biblepedia index ───────────────────────────────────────────────
// The hover-tooltip / word-tap layer needs only a subset of the 1.8 MB
// biblepedia index; assets/js/bp-lite.js fetches this instead.
{
  const full = JSON.parse(fs.readFileSync(path.join(ROOT, 'data/biblepedia/index.json'), 'utf8'));
  const lite = full.map(e => {
    const o = { id: e.id, term: e.term, category: e.category };
    if (e.brief) o.brief = e.brief;
    if (e.hitchcock_meaning) o.hitchcock_meaning = e.hitchcock_meaning;
    if (e.has_article !== undefined) o.has_article = e.has_article;
    if (e.redirect) o.redirect = e.redirect;
    if (e.aliases && e.aliases.length) o.aliases = e.aliases;
    return o;
  });
  const json = JSON.stringify(lite);
  fs.writeFileSync(path.join(DIST, 'assets', 'bp-lite.json'), json);
  console.log(`[build-assets] bp-lite.json: ${lite.length} entries, ${(json.length / 1024).toFixed(0)} KB (full: ${(fs.statSync(path.join(ROOT, 'data/biblepedia/index.json')).size / 1024).toFixed(0)} KB)`);

  // bp-tag.json (P11): the tagging layer needs term/id/link fields on nearly
  // every content page but briefs only on an actual hover/tap — dropping
  // brief + hitchcock_meaning cuts the on-load fetch to ~a third.
  const tag = lite.map(({ brief, hitchcock_meaning, ...rest }) => rest);
  const tagJson = JSON.stringify(tag);
  fs.writeFileSync(path.join(DIST, 'assets', 'bp-tag.json'), tagJson);
  console.log(`[build-assets] bp-tag.json: ${(tagJson.length / 1024).toFixed(0)} KB`);
}

// ── 6.5 Answers-page manifest ───────────────────────────────────────────────
// The slug list of built /answers/ pages, so the verse search can offer a
// topic's answer page without risking a 404 (fetched lazily by search.js).
{
  const ansDir = path.join(DIST, 'answers');
  const slugs = fs.existsSync(ansDir)
    ? fs.readdirSync(ansDir, { withFileTypes: true }).filter(e => e.isDirectory()).map(e => e.name).sort()
    : [];
  fs.writeFileSync(path.join(DIST, 'assets', 'answers-index.json'), JSON.stringify(slugs));
  console.log(`[build-assets] answers-index.json: ${slugs.length} topic pages`);
}

// ── 6.6 Topics-lite ─────────────────────────────────────────────────────────
// The Omni/Topics chip renderers need slug+title+count, not the 1.4 MB
// nave.json. Covers Nave heads with verses plus the generated answer topics
// (title reconstructed from the slug; no count).
{
  const nave = JSON.parse(fs.readFileSync(path.join(ROOT, 'data/topical/nave.json'), 'utf8'));
  const lite = nave.filter(e => (e.verses || []).length > 0)
    .map(e => ({ s: e.slug, t: e.title, n: e.verses.length }));
  const have = new Set(lite.map(e => e.s));
  const ansDir = path.join(DIST, 'answers');
  if (fs.existsSync(ansDir)) {
    for (const slug of fs.readdirSync(ansDir)) {
      if (have.has(slug) || !fs.statSync(path.join(ansDir, slug)).isDirectory()) continue;
      lite.push({ s: slug, t: slug.replace(/-/g, ' ').toUpperCase() });
    }
  }
  const json = JSON.stringify(lite);
  fs.writeFileSync(path.join(DIST, 'assets', 'topics-lite.json'), json);
  console.log(`[build-assets] topics-lite.json: ${lite.length} topics, ${(json.length / 1024).toFixed(0)} KB (nave.json: ${(fs.statSync(path.join(ROOT, 'data/topical/nave.json')).size / 1024).toFixed(0)} KB)`);
}

// ── 7. Verse search index (H5) ─────────────────────────────────────────────
// Runs after the sw precache walk on purpose: the index JSON is fetched at
// runtime (and cached by the data strategy), never precached.
await import('./build-search-index.mjs');
