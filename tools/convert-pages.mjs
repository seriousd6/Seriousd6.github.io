// convert-pages.mjs — Phase-1 converter: legacy root HTML pages → src/pages/*.astro
//
// For each page: parse with parse5, recognize the universal boilerplate
// (charset/viewport/favicon/title/description, theme bootstrap script, base
// stylesheets, standard footer, main.js/app.js pair) and turn it into
// Base.astro props; pass every other head/body node through VERBATIM into the
// matching layout slot. Any page whose structure deviates from the expected
// shape is reported, not silently mangled.
//
// Escaping notes:
//  - Astro treats {…} in template text/attrs as expressions → escape braces in
//    text nodes and attribute values (but NOT inside <script>/<style>, whose
//    raw text Astro never interpolates).
//  - Every passthrough <script>/<style> gets is:inline so Astro leaves it
//    untouched (no bundling, hoisting, or style scoping).
import { parse, parseFragment, serialize } from 'parse5';
import { readFileSync, writeFileSync, mkdirSync, readdirSync, statSync } from 'node:fs';
import { join, relative, dirname, resolve, sep } from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = resolve(fileURLToPath(new URL('..', import.meta.url)));
const OUT = join(ROOT, 'src', 'pages');

const SKIP_DIRS = new Set(['data', 'node_modules', 'dist', 'src', 'tools', '.git', '.github', '.astro']);
// Astro ignores _-prefixed routes; these authoring scaffolds ship verbatim via
// the deploy workflow's copy list instead (see deploy.yml / root-statics.mjs).
const SKIP_UNDERSCORE = true;
// Redirect/retirement stubs deliberately lack the standard boilerplate
// (theme script, base CSS). They ship verbatim via the same copy list rather
// than gaining chrome they never had. Keep in sync with root-statics.mjs.
const VERBATIM_PAGES = new Set([
  'devotionals/index.html',
  'journal/index.html',
  'memorize/index.html',
  'plans/index.html',
  'reflections/index.html',
  'worship/index.html',
  'word/index.html',
  'verse-study/index.html',
  'topics/index.html',
]);

const THEME_SNIPPET = "try{var t=localStorage.getItem('bsw_theme')";
const STD_FOOTER_TEXT = 'Personal Bible study notes & references.';

// ── tiny parse5 helpers ─────────────────────────────────────────────────────
const isEl = (n) => !!n.tagName;
const attr = (n, name) => n.attrs?.find((a) => a.name === name)?.value;
const text = (n) => {
  let out = '';
  (function walk(x) {
    if (x.nodeName === '#text') out += x.value;
    x.childNodes?.forEach(walk);
  })(n);
  return out;
};
const findEl = (n, pred) => {
  if (isEl(n) && pred(n)) return n;
  for (const c of n.childNodes || []) {
    const hit = findEl(c, pred);
    if (hit) return hit;
  }
  return null;
};

// Escape {, } in text nodes and attribute values so Astro doesn't read them as
// expressions — except inside script/style, where content must stay raw.
// Placeholders survive parse5 serialization (which would escape a literal &).
const OPEN = '', CLOSE = '';
function protectBraces(node, inRaw = false) {
  if (node.nodeName === '#text' && !inRaw) {
    node.value = node.value.replaceAll('{', OPEN).replaceAll('}', CLOSE);
  }
  if (isEl(node)) {
    for (const a of node.attrs || []) {
      a.value = a.value.replaceAll('{', OPEN).replaceAll('}', CLOSE);
    }
  }
  const raw = inRaw || (isEl(node) && ['script', 'style'].includes(node.tagName));
  node.childNodes?.forEach((c) => protectBraces(c, raw));
}

function markInline(node) {
  if (isEl(node) && ['script', 'style'].includes(node.tagName)) {
    if (!node.attrs.some((a) => a.name === 'is:inline')) {
      node.attrs.push({ name: 'is:inline', value: '' });
    }
  }
  node.childNodes?.forEach(markInline);
}

// Serialize a list of nodes verbatim (via a synthetic fragment).
function serializeNodes(nodes) {
  if (!nodes.length) return '';
  const frag = parseFragment('');
  frag.childNodes = nodes;
  return serialize(frag)
    .replaceAll(OPEN, '&#123;')
    .replaceAll(CLOSE, '&#125;');
}

const isBlank = (n) => n.nodeName === '#text' && !n.value.trim();

// ── head/body classification ────────────────────────────────────────────────
function classifyHeadNode(n) {
  if (!isEl(n)) return n.nodeName === '#comment' ? 'other' : 'skip'; // whitespace
  if (n.tagName === 'meta' && attr(n, 'charset')) return 'charset';
  if (n.tagName === 'meta' && attr(n, 'name') === 'viewport') return 'viewport';
  if (n.tagName === 'link' && attr(n, 'rel') === 'icon' && (attr(n, 'href') || '').endsWith('favicon.svg')) return 'icon';
  if (n.tagName === 'meta' && attr(n, 'name') === 'description' && !attr(n, 'id')) return 'description';
  if (n.tagName === 'title') return 'title';
  if (n.tagName === 'script' && text(n).startsWith(THEME_SNIPPET)) return 'theme';
  if (n.tagName === 'link' && attr(n, 'rel') === 'stylesheet') {
    const href = attr(n, 'href') || '';
    if (href.endsWith('assets/css/style.css')) return 'style-css';
    if (href.endsWith('assets/css/bible-ui.css')) return 'bible-ui';
  }
  return 'other';
}

function convertPage(absPath, relPath, report) {
  const html = readFileSync(absPath, 'utf8');
  const doc = parse(html);
  const flags = [];

  const htmlEl = findEl(doc, (n) => n.tagName === 'html');
  if (attr(htmlEl, 'lang') !== 'en') flags.push(`html lang="${attr(htmlEl, 'lang')}"`);
  const head = findEl(htmlEl, (n) => n.tagName === 'head');
  const body = findEl(htmlEl, (n) => n.tagName === 'body');

  // ── head ──
  let title = '';
  let description;
  let bibleUi = false;
  let sawTheme = false;
  let sawStyleCss = false;
  let prevKind = null;    // previous non-blank head node's kind
  const headSlot = [];    // between <title> and theme script
  const headPreCss = [];  // between theme script and style.css (e.g. Leaflet CDN CSS)
  const headEndSlot = []; // after style.css (page CSS — cascade order preserved)
  const seen = [];

  for (const n of head.childNodes) {
    const kind = classifyHeadNode(n);
    if (kind === 'skip' || isBlank(n)) continue;
    seen.push(kind);
    switch (kind) {
      case 'charset': case 'icon': break; // layout-owned
      case 'viewport':
        // Layout hardcodes the standard viewport; flag pages that differed so
        // the normalization is a conscious one.
        if (attr(n, 'content') !== 'width=device-width, initial-scale=1.0, viewport-fit=cover') {
          flags.push(`nonstandard viewport normalized ("${attr(n, 'content')}")`);
        }
        break;
      case 'description': description = attr(n, 'content'); break;
      case 'title': title = text(n); break;
      case 'theme': sawTheme = true; break;
      case 'style-css': sawStyleCss = true; break;
      case 'bible-ui':
        // Layout-owned ONLY in the canonical position (immediately after
        // style.css); anywhere else it passes through verbatim so the CSS
        // cascade order is preserved exactly (topic pages load it last).
        if (prevKind === 'style-css') {
          bibleUi = true;
        } else {
          flags.push('bible-ui.css in noncanonical position (passed through)');
          headEndSlot.push(n);
        }
        break;
      default:
        (sawStyleCss ? headEndSlot : sawTheme ? headPreCss : headSlot).push(n);
    }
    prevKind = kind;
  }
  // Sanity: universal items must appear in layout order, "other" metas must not
  // precede <title> (layout renders the slot after the title).
  const order = ['charset', 'viewport', 'icon', 'description', 'title', 'theme', 'style-css', 'bible-ui'];
  const positions = order.map((k) => seen.indexOf(k)).filter((i) => i !== -1);
  if (positions.some((p, i) => i > 0 && p < positions[i - 1])) flags.push('head order deviates');
  if (!sawTheme) flags.push('no theme bootstrap script');
  if (!sawStyleCss) flags.push('no style.css link');
  if (!title) flags.push('no <title>');
  const firstOther = seen.indexOf('other');
  const titleIdx = seen.indexOf('title');
  if (firstOther !== -1 && titleIdx !== -1 && firstOther < titleIdx) flags.push('head extras before <title>');

  // ── body ──
  const bodyAttrs = {};
  for (const a of body.attrs || []) bodyAttrs[a.name] = a.value;
  let footer = false;
  let mainJs = false;
  let appJs = false;
  const content = [];
  const afterScripts = [];
  let zone = 'content'; // content → scripts (after standard footer or main/app script)

  for (const n of body.childNodes) {
    if (isBlank(n)) continue;
    const src = isEl(n) && n.tagName === 'script' ? attr(n, 'src') || '' : '';
    const isMainJs = src.endsWith('assets/js/main.js');
    const isAppJs = src.endsWith('assets/js/app.js') && attr(n, 'type') === 'module';
    const isStdFooter =
      isEl(n) && n.tagName === 'footer' && (attr(n, 'class') || '').includes('site-footer') &&
      text(n).trim() === STD_FOOTER_TEXT;

    if (isStdFooter) {
      if (footer) flags.push('duplicate footer');
      footer = true;
      zone = 'scripts';
    } else if (isMainJs) {
      mainJs = true;
      zone = 'scripts';
      if (appJs) flags.push('main.js after app.js');
    } else if (isAppJs) {
      appJs = true;
      zone = 'scripts';
    } else if (isEl(n) && n.tagName === 'footer') {
      flags.push('nonstandard footer (passed through)');
      content.push(n); // keep in place; layout footer disabled below
    } else {
      (zone === 'content' ? content : afterScripts).push(n);
    }
  }
  const hasNonStdFooter = flags.includes('nonstandard footer (passed through)');

  // Icon href must resolve to the root favicon; flag pages whose (broken)
  // relative path resolved elsewhere — the layout normalizes them.
  const iconEl = head.childNodes.find((n) => classifyHeadNode(n) === 'icon');
  if (iconEl) {
    const depthUp = '../'.repeat(relPath.split('/').length - 1);
    const href = attr(iconEl, 'href');
    if (href !== `${depthUp}favicon.svg` && href !== '/favicon.svg') {
      flags.push(`icon href "${href}" resolved off-root (normalized)`);
    }
  }

  // ── emit .astro ──
  [...headSlot, ...headPreCss, ...headEndSlot, ...content, ...afterScripts].forEach((n) => {
    protectBraces(n);
    markInline(n);
  });

  const depth = relPath.split('/').length - 1;
  const layoutPath = '../'.repeat(depth + 1) + 'layouts/Base.astro';
  const props = [`title={${JSON.stringify(title)}}`];
  if (description !== undefined) props.push(`description={${JSON.stringify(description)}}`);
  if (Object.keys(bodyAttrs).length) props.push(`bodyAttrs={${JSON.stringify(bodyAttrs)}}`);
  if (!bibleUi) props.push('bibleUi={false}');
  if (!mainJs) props.push('mainJs={false}');
  if (!appJs) props.push('appJs={false}');
  if (!footer || hasNonStdFooter) props.push('footer={false}');

  const parts = [`---\nimport Base from '${layoutPath}';\n---\n`];
  parts.push(`<Base ${props.join(' ')}>`);
  if (headSlot.length) parts.push(`<Fragment slot="head">\n${serializeNodes(headSlot)}\n</Fragment>`);
  if (headPreCss.length) parts.push(`<Fragment slot="head-pre-css">\n${serializeNodes(headPreCss)}\n</Fragment>`);
  if (headEndSlot.length) parts.push(`<Fragment slot="head-end">\n${serializeNodes(headEndSlot)}\n</Fragment>`);
  parts.push(serializeNodes(content));
  if (afterScripts.length) parts.push(`<Fragment slot="after-scripts">\n${serializeNodes(afterScripts)}\n</Fragment>`);
  parts.push('</Base>\n');

  const outPath = join(OUT, relPath.replace(/\.html$/, '.astro'));
  mkdirSync(dirname(outPath), { recursive: true });
  writeFileSync(outPath, parts.join('\n'), 'utf8');
  report.push({ page: relPath, flags });
}

// ── walk the repo for legacy pages ──────────────────────────────────────────
function* htmlFiles(dir, rel = '') {
  for (const name of readdirSync(dir)) {
    if (rel === '' && SKIP_DIRS.has(name)) continue;
    if (SKIP_UNDERSCORE && name.startsWith('_')) continue;
    const abs = join(dir, name);
    if (statSync(abs).isDirectory()) yield* htmlFiles(abs, rel ? `${rel}/${name}` : name);
    else if (name.endsWith('.html')) yield [abs, rel ? `${rel}/${name}` : name];
  }
}

const report = [];
let count = 0;
let skipped = 0;
for (const [abs, rel] of htmlFiles(ROOT)) {
  if (VERBATIM_PAGES.has(rel)) {
    skipped++;
    continue;
  }
  convertPage(abs, rel, report);
  count++;
}
console.log(`Skipped ${skipped} verbatim-copy stubs.`);

console.log(`Converted ${count} pages → src/pages/`);
const flagged = report.filter((r) => r.flags.length);
if (flagged.length) {
  console.log(`\n${flagged.length} pages with deviations:`);
  for (const r of flagged) console.log(`  ${r.page}: ${r.flags.join('; ')}`);
} else {
  console.log('No structural deviations.');
}
