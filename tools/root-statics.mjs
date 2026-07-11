// Dev-server bridge for the Phase-1 overlay layout: the legacy static tree
// (assets/, data/, sw.js, …) lives at the repo root — NOT in public/ — so the
// branch-served production site and the hourly data auto-sync stay untouched.
// This integration makes `astro dev` serve those root paths like public/ would.
// Production builds don't use this; .github/workflows/deploy.yml copies the
// same list into dist/ after `astro build`.
import { createReadStream, existsSync, statSync } from 'node:fs';
import { join, normalize, resolve, sep } from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = resolve(fileURLToPath(new URL('..', import.meta.url)));

// Root directories and files that ship verbatim. Keep in sync with deploy.yml
// and the VERBATIM_PAGES list in convert-pages.mjs.
const STATIC_DIRS = ['assets', 'data', 'topics/_template', 'topics/_template-book', 'study-guides/_template'];
const STATIC_FILES = [
  'sw.js', 'manifest.json', 'favicon.ico', 'favicon.svg', 'offline.html',
  // Redirect/retirement stubs excluded from Astro conversion:
  'devotionals/index.html', 'journal/index.html', 'memorize/index.html',
  'plans/index.html', 'reflections/index.html', 'worship/index.html',
  'word/index.html', 'verse-study/index.html', 'topics/index.html',
];

const MIME = {
  '.html': 'text/html; charset=utf-8',
  '.js': 'text/javascript; charset=utf-8',
  '.mjs': 'text/javascript; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.json': 'application/json; charset=utf-8',
  '.svg': 'image/svg+xml',
  '.ico': 'image/x-icon',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.webp': 'image/webp',
  '.woff2': 'font/woff2',
  '.woff': 'font/woff',
  '.txt': 'text/plain; charset=utf-8',
  '.xml': 'application/xml; charset=utf-8',
};

function resolveRootPath(urlPath) {
  let p;
  try {
    p = decodeURIComponent(urlPath.split('?')[0]);
  } catch {
    return null;
  }
  if (!p.startsWith('/')) return null;
  const rel = p.slice(1);
  const isStatic =
    STATIC_FILES.includes(rel) ||
    STATIC_DIRS.some((d) => rel === d || rel.startsWith(d + '/'));
  if (!isStatic) return null;
  let file = normalize(join(ROOT, rel));
  if (!file.startsWith(ROOT + sep)) return null; // path traversal guard
  if (existsSync(file) && statSync(file).isDirectory()) file = join(file, 'index.html');
  return existsSync(file) && statSync(file).isFile() ? file : null;
}

export default function rootStatics() {
  return {
    name: 'root-statics',
    hooks: {
      'astro:server:setup': ({ server }) => {
        server.middlewares.use((req, res, next) => {
          const file = resolveRootPath(req.url || '');
          if (!file) return next();
          const ext = file.slice(file.lastIndexOf('.')).toLowerCase();
          res.setHeader('Content-Type', MIME[ext] || 'application/octet-stream');
          createReadStream(file).pipe(res);
        });
      },
    },
  };
}
