// diff-pages.mjs — Phase-1 acceptance gate.
// Parses each legacy root HTML page and its Astro-built dist counterpart,
// normalizes both DOMs, and reports every remaining difference. The goal is
// ZERO functional diffs; the only tolerated deltas are:
//   - URL attributes that resolve to the same absolute target for that page
//   - Astro's <meta name="generator"> tag
//   - whitespace / attribute order / void-tag syntax
import { parse } from 'parse5';
import { readFileSync, existsSync } from 'node:fs';
import { join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = resolve(fileURLToPath(new URL('..', import.meta.url)));
const DIST = join(ROOT, 'dist');
const SITE = 'https://seriousd6.github.io';

// Same enumeration rules as convert-pages.mjs.
import { readdirSync, statSync } from 'node:fs';
const SKIP_DIRS = new Set(['data', 'node_modules', 'dist', 'src', 'tools', '.git', '.github', '.astro']);
const VERBATIM = new Set([
  'devotionals/index.html', 'journal/index.html', 'memorize/index.html',
  'plans/index.html', 'reflections/index.html', 'worship/index.html',
  'word/index.html', 'verse-study/index.html', 'topics/index.html',
]);
function* htmlFiles(dir, rel = '') {
  for (const name of readdirSync(dir)) {
    if (rel === '' && SKIP_DIRS.has(name)) continue;
    if (name.startsWith('_')) continue;
    const abs = join(dir, name);
    if (statSync(abs).isDirectory()) yield* htmlFiles(abs, rel ? `${rel}/${name}` : name);
    else if (name.endsWith('.html')) yield rel ? `${rel}/${name}` : name;
  }
}

const URL_ATTRS = new Set(['href', 'src', 'action', 'data-src', 'poster']);
const isEl = (n) => !!n.tagName;

// Normalize a parse5 tree into a comparable structure.
function normalize(node, out = []) {
  for (const c of node.childNodes || []) {
    if (c.nodeName === '#text') {
      const t = c.value.replace(/\s+/g, ' ');
      if (t.trim()) out.push({ kind: 'text', value: t.trim() });
    } else if (c.nodeName === '#comment') {
      // Astro strips HTML comments from rendered output (the .astro sources
      // keep them); they are not part of the functional DOM — skip.
      continue;
    } else if (isEl(c)) {
      if (c.tagName === 'meta' && c.attrs.some((a) => a.name === 'name' && a.value === 'generator')) continue;
      const attrs = {};
      for (const a of c.attrs) attrs[a.name] = a.value;
      const el = { kind: 'el', tag: c.tagName, attrs, children: [] };
      if (c.tagName === 'script' || c.tagName === 'style') {
        // Raw text must match exactly (modulo outer indentation trim).
        el.raw = (c.childNodes?.map((x) => x.value ?? '').join('') || '').trim();
      } else {
        normalize(c, el.children);
      }
      out.push(el);
    }
  }
  return out;
}

function urlEquivalent(a, b, pageUrl) {
  try {
    return new URL(a, pageUrl).href === new URL(b, pageUrl).href;
  } catch {
    return false;
  }
}

// Conscious, documented normalizations — reported separately, not as failures.
const STD_VIEWPORT = 'width=device-width, initial-scale=1.0, viewport-fit=cover';
const VIEWPORT_VARIANTS = new Set([
  'width=device-width, initial-scale=1.0',
  'width=device-width, initial-scale=1, viewport-fit=cover',
]);
function acceptedNormalization(rel, tag, attrName, va, vb) {
  // 1) Slightly-off viewports (3 legacy pages) standardize to the site-wide one.
  if (tag === 'meta' && attrName === 'content' && VIEWPORT_VARIANTS.has(va) && vb === STD_VIEWPORT) {
    return 'viewport standardized';
  }
  // 2) settings/read/ had depth-broken relative URLs (../assets/… resolved to
  //    the nonexistent /settings/assets/…); root-absolute paths repair them.
  if (rel === 'settings/read/index.html' && (attrName === 'href' || attrName === 'src')) {
    const tail = (va || '').replace(/^(\.\.\/)+/, '');
    if (vb === '/' + tail) return 'broken relative path repaired';
  }
  return null;
}

function diffNodes(a, b, pageUrl, path, diffs, rel, accepted) {
  const max = Math.max(a.length, b.length);
  for (let i = 0; i < max; i++) {
    const x = a[i], y = b[i];
    const here = `${path}[${i}]`;
    if (!x || !y) {
      diffs.push(`${here}: ${x ? 'missing in dist' : 'extra in dist'}: ${describe(x || y)}`);
      continue;
    }
    if (x.kind !== y.kind || (x.kind === 'el' && x.tag !== y.tag)) {
      diffs.push(`${here}: ${describe(x)} vs ${describe(y)}`);
      continue;
    }
    if (x.kind !== 'el') {
      if (x.value !== y.value) diffs.push(`${here} ${x.kind}: "${trunc(x.value)}" vs "${trunc(y.value)}"`);
      continue;
    }
    const keys = new Set([...Object.keys(x.attrs), ...Object.keys(y.attrs)]);
    for (const k of keys) {
      const va = x.attrs[k], vb = y.attrs[k];
      if (va === vb) continue;
      if (URL_ATTRS.has(k) && va != null && vb != null && urlEquivalent(va, vb, pageUrl)) continue;
      if (k === 'charset' && (va || '').toLowerCase() === (vb || '').toLowerCase()) continue;
      const norm = acceptedNormalization(rel, x.tag, k, va, vb);
      if (norm) {
        accepted.push(`${rel}: ${norm} (<${x.tag} ${k}>)`);
        continue;
      }
      diffs.push(`${here} <${x.tag} ${k}>: "${trunc(va)}" vs "${trunc(vb)}"`);
    }
    if (x.raw !== undefined || y.raw !== undefined) {
      if ((x.raw || '') !== (y.raw || '')) diffs.push(`${here} <${x.tag}> raw content differs (${(x.raw || '').length} vs ${(y.raw || '').length} chars)`);
      continue;
    }
    diffNodes(x.children, y.children, pageUrl, `${here}/${x.tag}`, diffs, rel, accepted);
  }
}

const describe = (n) => !n ? '(none)' : n.kind === 'el' ? `<${n.tag}>` : `${n.kind} "${trunc(n.value)}"`;
const trunc = (s) => (s ?? '(absent)').length > 80 ? s.slice(0, 77) + '…' : (s ?? '(absent)');

let pages = 0, clean = 0, missing = 0;
const problems = [];
const accepted = [];
for (const rel of htmlFiles(ROOT)) {
  if (VERBATIM.has(rel)) continue;
  pages++;
  const distFile = join(DIST, rel);
  if (!existsSync(distFile)) {
    missing++;
    problems.push({ rel, diffs: ['MISSING from dist'] });
    continue;
  }
  const pageUrl = `${SITE}/${rel.replace(/index\.html$/, '')}`;
  const orig = normalize(parse(readFileSync(join(ROOT, rel), 'utf8')));
  const built = normalize(parse(readFileSync(distFile, 'utf8')));
  const diffs = [];
  diffNodes(orig, built, pageUrl, '', diffs, rel, accepted);
  if (diffs.length) problems.push({ rel, diffs });
  else clean++;
}

console.log(`Compared ${pages} pages: ${clean} identical, ${problems.length} with diffs, ${missing} missing.`);
if (accepted.length) {
  console.log(`\nAccepted normalizations (${accepted.length}):`);
  accepted.forEach((a) => console.log('  ' + a));
}
for (const p of problems) {
  console.log(`\n── ${p.rel} (${p.diffs.length}) ──`);
  p.diffs.slice(0, 12).forEach((d) => console.log('  ' + d));
  if (p.diffs.length > 12) console.log(`  … +${p.diffs.length - 12} more`);
}
