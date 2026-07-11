/* entries/search.js — Explore/search page entry (search/).
 *
 * The only page that loads the full search engine. Other pages get just the
 * sidebar Search button + hotkeys from core-boot's buildSearchNav.
 */
import { boot } from '../core-boot.js';
import { initSearchPage } from '../search.js';

boot(function () {
  var input = document.getElementById('bsw-search-input');
  if (input) initSearchPage(input);
});
