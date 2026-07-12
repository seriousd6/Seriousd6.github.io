/* entries/reader.js — Bible reader entry (read/ and settings/read/).
 *
 * The heaviest page family: chapter rendering, compare, study desk, audio,
 * interlinear, parallels, and the full toggle set. Uses boot()'s `early`
 * option so reader init runs BEFORE autoTagRefs/wireInlineVerses — the same
 * order the app.js dispatch used.
 */
import { boot } from '../core-boot.js';
import {
  initReaderPage, initCompareToggle,
  initViewToggle, initStudyToolsToggle, initFontSizeControls,
  initSidebarToggle, initXrefNotesToggle, initCommModeToggle,
  initColumnsToggle, initReaderModeToggle, initNotesPanelToggle,
  initParaViewToggle
} from '../reader.js';
import { initReaderAudio } from '../reader-audio.js';
import { initStudyDesk } from '../study-desk.js';
import { initInterlinearToggle, initBookInfoToggle } from '../interlinear.js';
import { initEchoToggle } from '../parallels.js';
import { initParallelsToggle } from '../synoptic.js';
import { _injectShortcutsBtn } from '../modal.js';
import { initReaderRail } from '../reader-rail.js';
import { initWordTap } from '../reader-wordtap.js';

boot(function () {
  initReaderPage();
  initCompareToggle();
  // Build the two popovers first so their member toggles route into them:
  // ⚙ View (layout) and 📖 Study Tools (study/reading features). The six study
  // toggles below look up #reader-studytools-popover, so it must exist first.
  initViewToggle();
  initStudyToolsToggle();
  initInterlinearToggle();
  initBookInfoToggle();
  initCommModeToggle();
  initNotesPanelToggle();
  initSidebarToggle();
  initFontSizeControls();
  initXrefNotesToggle();
  initEchoToggle();
  initParallelsToggle();
  initColumnsToggle();
  initReaderModeToggle();
  initParaViewToggle();
  initReaderAudio();
  initStudyDesk();
  _injectShortcutsBtn();
  initReaderRail();
  initWordTap();
}, { early: true });
