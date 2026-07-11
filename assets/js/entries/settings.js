/* entries/settings.js — Settings entry (settings/) — Sync & Backup section. */
import { boot } from '../core-boot.js';
import { initSyncSection } from '../sync.js';

boot(function () {
  initSyncSection();
});
