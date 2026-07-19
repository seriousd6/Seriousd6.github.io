/* entries/study-panel.js — /study/passage/: the reader's Passage Study
 * drawer as a standalone, linkable desk panel (P26, docs/plans/OL-DESK-PLAN.md §2b).
 * Shared boot gives it the verse modal, ref wiring, terms, and — in frames —
 * the desk protocol (goto follow, word emits).
 */
import { boot } from '../core-boot.js';
import { initStudyPanelPage } from '../study-desk.js';

boot(function () {
  initStudyPanelPage();
});
