/* entries/home.js — Home page (/) entry.
 *
 * The home page hosts the daily reading plan (#daily-plan-select) and shows
 * first-visit onboarding. (The old #home-plans-widget / initPlansHomeWidget
 * branch is gone — the full daily plan lives on the home page now.)
 */
import { boot } from '../core-boot.js';
import { initDailyPage } from '../daily.js';
import { _initOnboarding } from '../pwa.js';

boot(function () {
  initDailyPage();
  // Onboarding is shown to first-time visitors on the daily plan page.
  _initOnboarding();
});
