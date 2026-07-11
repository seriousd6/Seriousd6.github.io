/* entries/lib-browser.js — Library browser entry (library/). */
import { boot } from '../core-boot.js';
import { initLibBrowserPage } from '../lib-browser.js';

boot(function () {
  initLibBrowserPage();
});
