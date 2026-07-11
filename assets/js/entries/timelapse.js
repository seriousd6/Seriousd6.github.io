/* entries/timelapse.js — Biblical history time-lapse map entry (maps/timelapse/).
 * (The old ?v=2 cache-buster was dropped in Phase 3 — content hashing owns busting.) */
import { boot } from '../core-boot.js';
import { initTimelapsePage } from '../timelapse-map.js';

boot(function () {
  initTimelapsePage();
});
