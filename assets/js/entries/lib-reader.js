/* entries/lib-reader.js — Library document reader entry (library/read/). */
import { boot } from '../core-boot.js';
import { initLibReaderPage } from '../lib-reader.js';

boot(function () {
  initLibReaderPage();
});
