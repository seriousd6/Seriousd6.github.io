/* entries/desk.js — the Desk work surface (/desk/). */
import { boot } from '../core-boot.js';
import { initDesk } from '../desk.js';
import { _initOnboarding } from '../pwa.js';

boot(function () {
  initDesk();
  // Desktop first-runs land HERE (desk-as-home) — the welcome card and its
  // tour link must greet them on the surface, not only on the daily page.
  _initOnboarding();
});
