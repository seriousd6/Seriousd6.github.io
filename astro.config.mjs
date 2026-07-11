// @ts-check
import { defineConfig } from 'astro/config';
import rootStatics from './tools/root-statics.mjs';

// Phase-1 structural migration config.
// The legacy runtime tree (assets/, data/, sw.js, …) stays at the repo root so
// the branch-served live site and the hourly data auto-sync keep working
// untouched; rootStatics() serves those root paths during `astro dev`, and the
// deploy workflow copies them into dist/ after `astro build`.
export default defineConfig({
  site: 'https://kingdombiblestudy.com',
  // Ship page markup un-minified so dist output stays diffable against the
  // legacy hand-authored HTML (Phase-1 acceptance is a clean DOM diff).
  compressHTML: false,
  build: {
    // Mirror the source tree exactly: src/pages/foo/index.astro -> /foo/index.html,
    // src/pages/topics/prayer/deep-dive.astro -> /topics/prayer/deep-dive.html.
    format: 'preserve',
  },
  integrations: [rootStatics()],
});
