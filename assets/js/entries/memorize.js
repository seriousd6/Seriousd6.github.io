/* entries/memorize.js — Memorisation entry (discipline/ hosts #mem-list). */
import { boot } from '../core-boot.js';
import { initMemorizePage } from '../daily.js';

boot(function () {
  initMemorizePage();
});
