/* entries/workshop.js — Translation workshop entry (translation/workshop/).
 *
 * Private tool; does not use the shared boot (no Bible-metadata dependency,
 * no sidebar modal). Mirrors the inline module script the page used to carry,
 * including its loading-error surface. Having a real entry (instead of inline
 * imports) lets the Vite build bundle workshop.js and its terms.js/library.js
 * chain like every other page module.
 */
import { initTheme } from '../core.js';
import { initWorkshopPage } from '../workshop.js';

initTheme();
initWorkshopPage().catch(function (err) {
  var el = document.getElementById('ws-loading-text');
  if (el) el.textContent = 'Error loading: ' + err.message;
  console.error('[Workshop]', err);
});
