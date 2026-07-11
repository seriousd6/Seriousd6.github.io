/* entries/apocrypha.js — Apocrypha reader entry (apocrypha/). */
import { boot } from '../core-boot.js';
import { initApocryphaReader } from '../apocrypha-reader.js';

boot(function () {
  initApocryphaReader();
});
