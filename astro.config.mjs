// @ts-check
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';
import rootStatics from './tools/root-statics.mjs';

// The runtime data tree (data/, fonts, icons) stays at the repo root so the
// hourly data auto-sync keeps working untouched; rootStatics() serves those
// root paths during `astro dev`. Production assets are built by
// tools/build-assets.mjs after `astro build` (see `npm run build`), and
// .github/workflows/deploy.yml copies data/ + verbatim HTML into dist/.
export default defineConfig({
  site: 'https://kingdombiblestudy.com',
  // Phase 5: whitespace-compressed markup. (compressHTML:false existed only
  // for the Phase-1 acceptance of DOM-diffing dist/ against the legacy
  // hand-authored HTML, which is long retired.)
  compressHTML: true,
  build: {
    // Mirror the source tree exactly: src/pages/foo/index.astro -> /foo/index.html,
    // src/pages/topics/prayer/deep-dive.astro -> /topics/prayer/deep-dive.html.
    format: 'preserve',
  },
  integrations: [
    rootStatics(),
    // ~4.6k static pages (biblepedia articles, library docs) are worth
    // surfacing to crawlers; robots.txt at the repo root points here.
    sitemap(),
  ],
});
