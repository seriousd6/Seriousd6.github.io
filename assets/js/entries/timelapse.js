/* entries/timelapse.js — Biblical history time-lapse map entry (maps/timelapse/).
 * Keeps the ?v=2 cache-buster the app.js import carried. */
import { boot } from '../core-boot.js';
import { initTimelapsePage } from '../timelapse-map.js?v=2';

boot(function () {
  initTimelapsePage();
});
