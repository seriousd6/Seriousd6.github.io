/* entries/generic.js — Default page entry (Phase 2 per-page JS split).
 *
 * For every page with no page-specific feature module: home cards, topics,
 * study guides, search, library documents, about, etc. Runs the shared boot
 * only — theme, PWA, Bible metadata, tooltip/modal/ref wiring, version
 * picker, sidebar Search button. See core-boot.js for the full sequence.
 */
import { boot } from '../core-boot.js';

boot();
