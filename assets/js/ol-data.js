/* ol-data.js — the original-language data layer (P21 Phase 1).
 *
 * Extracted verbatim from workshop.js per docs/plans/OL-DESK-PLAN.md: every reference
 * cache and its lazy loader, so the coming /ol/word/ and /ol/verse/ desk
 * pages share one data layer with the (interim) workshop shell. Caches are
 * exported live bindings — loaders reassign them here and importers see the
 * update; importers must never assign to them directly.
 */
'use strict';

import { _resolve, parseRef } from './core.js';

// INTENT: Grammar data cache for SW-B particle highlighting in passage tiles and
//   the Grammar Significance dossier section. Loaded lazily on first passage study.
// CHANGE? If particle file paths change, update _loadParticles() URL template.
//   If morphology-significance files are added for new languages, extend the loader.
// VERIFY: Study John 1 — tiles with γάρ/οὖν/ἀλλά get colored left-border + badge.
//   Click γάρ tile → dossier Grammar section shows "Ground / Reason" function card.
export let _particlesCache = {};         // lang ('greek'|'hebrew') → {code: particle entry}
export let _morphSigCache  = {};         // lang → morphology significance data
// INTENT: Grammar debates cache for SW-C — lazy-loaded array of debate objects.
//   Checked in _renderDossier() to surface Contested Interpretation cards when
//   the clicked word's code matches a debate and the current passage is a trigger passage.
// CHANGE? If grammar-debates.json schema changes (strongs_keys, trigger_passages fields),
//   update _renderDebateSection() and the index built in _loadDebates().
// VERIFY: Study Gal 2:16, click G4102 (πίστεως) → Contested Interpretation card appears
//   showing both sides of the πίστις Χριστοῦ debate with proponents named.
export let _debatesCache   = null;       // array of debate objects (null = not yet loaded)
export let _debatesByCode  = {};         // inverted index: strongs_code → [debate, ...]

// INTENT: Idiom database cache for SW-E — loaded lazily on first passage study.
//   _idiomsIndex maps Strong's code → [idiom ids] for O(1) lookup per tile click.
//   _idiomsData maps idiom id → full idiom entry for rendering.
// CHANGE? If data/idioms.json or data/idioms-index.json paths change, update _loadIdioms().
// VERIFY: Study John 1 → click G5207 (υἱός) → "Idiom Alert" section shows son-of-x
//   and son-of-man entries. Study John 1:1-18 passage → "Idioms in This Passage" panel
//   appears above tiles listing all idioms triggered by tokens in the pericope.
export let _idiomsData  = null;   // id → full idiom entry (null = not loaded)
export let _idiomsIndex = null;   // strongs_code → [idiom id, ...] (null = not loaded)

// INTENT: Cognate family data for SW-H — shows root→descendants so the user sees
//   semantic weight from root meaning (e.g. כבד "heavy" → כָּבוֹד "glory", the weight of God).
//   Two caches: one per language (Hebrew/Greek) for families array, one for the inverted index.
// CHANGE? If cognate-families-*.json or cognate-index-*.json paths change, update _loadCognates().
// VERIFY: Click H3519 (כָּבוֹד) → "Word Family" section shows root H3513 כָּבַד "heavy/honor"
//   with chips for כָּבֵד (heavy), כָּבֵד (liver), כְּבֵדֻת (heavily), כָּבוֹד (glory).
export let _cognatesFamilies = { H: null, G: null };  // lang prefix → families array (null = not loaded)
export let _cognatesIndex    = { H: null, G: null };  // lang prefix → code→root map

// INTENT: Author frequency data for SW-J — shows which NT/OT author uses a word most
//   intensively (normalized per 1000 tokens). Enables detecting Johannine, Pauline, or
//   Lukan characteristic vocabulary at a glance.
// CHANGE? If author groups in build-author-frequencies.py change, update the author label
//   mapping in _renderAuthorFreqSection().
// VERIFY: Click G26 (ἀγάπη) → Author Frequency shows Paul as peak; John close behind.
export let _authorFreqCache = { greek: null, hebrew: null };  // lang → { code: { rates, peak } }

// INTENT: Semantic field data for SW-I — PMI co-occurrence neighbors showing which words
//   travel together in the corpus. Reveals conceptual clusters invisible in dictionary definitions.
// CHANGE? If semantic-fields-*.json schema changes (fields renamed), update _renderSemanticSection().
// VERIFY: Click H2617 (חֶסֶד hesed) → Semantic Neighborhood shows אֱמֶת, אֱמוּנָה, רַחֲמִים.
export let _semanticCache = { greek: null, hebrew: null };  // lang → { code: [{ code, pmi, co_count }] }

// INTENT: Second Temple context data for SW-L — surfaces relevant Jewish background
//   documents when a word in the dossier has matching strongs_keys or when the current
//   passage matches a trigger reference in data/second-temple/context.json.
// CHANGE? If strongs_keys or trigger_passages schema changes, update _renderSTContext().
// VERIFY: Study John 1:1, click G3056 (λόγος) → "Second Temple Context" section appears
//   with Philo Logos entry showing source, date, context, and representative quote.
export let _stContextCache = null;  // array of context entries (null = not loaded)

// INTENT: OT-in-NT quotation data for SW-K — shows the MT/LXX/NT three-column comparison
//   panel whenever a dossier word appears in a NT quotation of the OT.
//   _otInNtCache is keyed by nt_ref (e.g. "Matt 1:23") and also indexed by ot_ref for OT-side lookup.
// CHANGE? If data/ot-in-nt/quotations.json schema changes, update _renderOTinNTSection().
// VERIFY: Study Matt 1:23 → click G3933 (παρθένος) → "OT Source" section shows Isa 7:14
//   in three columns with עַלְמָה vs παρθένος difference highlighted and interpretation note.
export let _otInNtCache    = null;   // array of quotation entries (null = not loaded)
export let _otInNtByRef    = {};     // nt_ref string → [quotation, ...] (built on load)

// INTENT: Per-book synthesis data for SW-M — each book's pericope entries are loaded
//   lazily on first Synthesis tab click and cached. Each entry is { key, ref, data }
//   where key is the raw ref string (e.g. "Rom 1:16-17") and ref is the parseRef result.
//   undefined = not yet attempted, null = fetch in progress, [] = loaded but no data.
// CHANGE? If data/synthesis/ filename convention changes, update _loadSynthesis() path.
// VERIFY: Study Romans 1:16 → click Synthesis tab → "The Thesis of Romans" pericope loads.
export let _synthesisCache = {};   // bookId → [{ key, ref, data }] | null (undefined = not loaded)

// INTENT: Switches column 2 from the vocabulary queue to the interlinear tile view
//   for the requested passage. Tile click → _openWord() → shows lexical dossier.
// CHANGE? If the tile popover from interlinear.js is ported here, remove the
//   inline dossier call in _renderPassageTiles and defer to the popover logic.
// VERIFY: Type "John 1:1-5", click Study → sw-passage-view shows John 1:1 through
//   1:5 as rows of tiles. Click a G-code tile → dossier loads for that word.
// INTENT: Lazily fetch the particle discourse-marker JSON for a language.
//   Returns cached result on subsequent calls so the file is fetched at most once.
// CHANGE? If data/grammar/{lang}-particles.json is renamed or moved, update the URL.
// VERIFY: Open DevTools Network tab, study John 1 → one request to greek-particles.json,
//   then study Romans 8 → no second request (cache hit).
export async function _loadParticles(lang) {
  if (_particlesCache[lang]) return _particlesCache[lang];
  try {
    const url = _resolve('../../data/grammar/' + lang + '-particles.json');
    _particlesCache[lang] = await fetch(url).then(function(r) { return r.ok ? r.json() : {}; });
  } catch (e) {
    _particlesCache[lang] = {};
  }
  return _particlesCache[lang];
}

// INTENT: Lazily fetch the morphology significance JSON for a language.
//   Used in the dossier Grammar section to show per-POS form significance notes.
// CHANGE? If data/grammar/{lang}-morphology-significance.json is renamed, update URL.
// VERIFY: Click a Greek verb in any passage → dossier Grammar section shows at least
//   the aspect significance rows (aorist, perfect, imperfect, present).
export async function _loadMorphSig(lang) {
  if (_morphSigCache[lang]) return _morphSigCache[lang];
  try {
    const url = _resolve('../../data/grammar/' + lang + '-morphology-significance.json');
    _morphSigCache[lang] = await fetch(url).then(function(r) { return r.ok ? r.json() : {}; });
  } catch (e) {
    _morphSigCache[lang] = {};
  }
  return _morphSigCache[lang];
}

// INTENT: Lazily fetch literary genre.json and structures.json for the SW-D literary panel.
//   Both are loaded together since they are small and always used together.
// CHANGE? If literary file paths change, update both URLs below.
// VERIFY: Study John 1:1-18 → click "Literary Structure" tab → genre badge shows "gospel"
//   with sub-genres; the John prologue chiasm renders with element labels.
export let _literaryCache = { genre: null, structures: null, devices: null };
// INTENT: Fetch all three literary data files in parallel; guard so repeated calls are no-ops.
//   devices-glossary.json (DATA-15) is now fetched here and rendered as a collapsible
//   reference at the bottom of the Literary tab.
// CHANGE? If any data/literary/*.json file is moved, update its URL below.
// VERIFY: Open DevTools → Network, study any passage, click Literary tab → three requests
//   fire: genre.json, structures.json, devices-glossary.json. Second click: zero requests.
export async function _loadLiterary() {
  if (_literaryCache.genre && _literaryCache.structures && _literaryCache.devices) return _literaryCache;
  const [genre, structures, devices] = await Promise.all([
    _literaryCache.genre      ? Promise.resolve(_literaryCache.genre)
      : fetch(_resolve('../../data/literary/genre.json')).then(function(r) { return r.ok ? r.json() : {}; }).catch(function() { return {}; }),
    _literaryCache.structures ? Promise.resolve(_literaryCache.structures)
      : fetch(_resolve('../../data/literary/structures.json')).then(function(r) { return r.ok ? r.json() : []; }).catch(function() { return []; }),
    _literaryCache.devices    ? Promise.resolve(_literaryCache.devices)
      : fetch(_resolve('../../data/literary/devices-glossary.json')).then(function(r) { return r.ok ? r.json() : []; }).catch(function() { return []; }),
  ]);
  _literaryCache.genre      = genre;
  _literaryCache.structures = structures;
  _literaryCache.devices    = devices;
  return _literaryCache;
}

// INTENT: Lazily fetch grammar-debates.json and build the _debatesByCode inverted index
//   so that _renderDebateSection() can look up debates by Strong's code in O(1).
// CHANGE? If grammar-debates.json is moved from data/grammar/, update the URL here.
// VERIFY: After studying any passage, open DevTools → Network: one request to
//   grammar-debates.json, then subsequent tile clicks reuse the cached array.
export async function _loadDebates() {
  if (_debatesCache !== null) return _debatesCache;
  try {
    const url = _resolve('../../data/grammar/grammar-debates.json');
    _debatesCache = await fetch(url).then(function(r) { return r.ok ? r.json() : []; });
  } catch (e) {
    _debatesCache = [];
  }
  // Build inverted index: code → [debate, ...]
  _debatesByCode = {};
  (_debatesCache || []).forEach(function(debate) {
    (debate.strongs_keys || []).forEach(function(code) {
      if (!_debatesByCode[code]) _debatesByCode[code] = [];
      _debatesByCode[code].push(debate);
    });
  });
  return _debatesCache;
}

// INTENT: Lazily fetch all three cultural background files in parallel and cache them.
//   Provides frameworks primer, book-context notes, and symbol lookup for SW-F tab.
// CHANGE? If cultural/ file paths change, update the three _resolve() URLs below.
//   If new cultural files are added (e.g., geography.json), add a fourth fetch here
//   and expose it in _literaryCulturalCache.
// VERIFY: Study any passage, click "Cultural Context" tab → framework primers appear
//   for the book. DevTools Network shows one set of requests to data/cultural/*.json
//   and no repeat requests on subsequent tab clicks.
export let _culturalCache = { frameworks: null, bookContext: null, symbols: null };
export async function _loadCultural() {
  if (_culturalCache.frameworks && _culturalCache.bookContext && _culturalCache.symbols) return _culturalCache;
  try {
    const [frameworks, bookContext, symbols] = await Promise.all([
      _culturalCache.frameworks  ? Promise.resolve(_culturalCache.frameworks)
        : fetch(_resolve('../../data/cultural/frameworks.json')).then(function(r) { return r.ok ? r.json() : []; }),
      _culturalCache.bookContext ? Promise.resolve(_culturalCache.bookContext)
        : fetch(_resolve('../../data/cultural/book-context.json')).then(function(r) { return r.ok ? r.json() : {}; }),
      _culturalCache.symbols     ? Promise.resolve(_culturalCache.symbols)
        : fetch(_resolve('../../data/cultural/symbols.json')).then(function(r) { return r.ok ? r.json() : {}; }),
    ]);
    _culturalCache.frameworks  = frameworks  || [];
    _culturalCache.bookContext = bookContext || {};
    _culturalCache.symbols     = symbols    || {};
  } catch(e) {
    _culturalCache.frameworks  = [];
    _culturalCache.bookContext = {};
    _culturalCache.symbols     = {};
  }
  return _culturalCache;
}

// INTENT: Lazily fetch idioms.json and idioms-index.json, storing the full entries in
//   _idiomsData (keyed by id) and the inverted index in _idiomsIndex (code → [id,...]).
//   Both files are fetched in parallel on first call; subsequent calls return immediately.
// CHANGE? If the idioms JSON schema changes (id field renamed, strongs_trigger_* renamed),
//   update _renderIdiomAlertSection() and _renderPassageIdioms(). If files are moved from
//   data/, update the _resolve() paths below.
// VERIFY: After studying any passage, DevTools → Network shows one request each to
//   idioms.json and idioms-index.json. Subsequent passage studies make no new requests.
export async function _loadIdioms() {
  if (_idiomsData !== null && _idiomsIndex !== null) return;
  try {
    const [rawArr, rawIdx] = await Promise.all([
      fetch(_resolve('../../data/idioms.json')).then(function(r) { return r.ok ? r.json() : []; }),
      fetch(_resolve('../../data/idioms-index.json')).then(function(r) { return r.ok ? r.json() : {}; }),
    ]);
    // Convert array → id-keyed map
    _idiomsData = {};
    (rawArr || []).forEach(function(entry) { if (entry.id) _idiomsData[entry.id] = entry; });
    _idiomsIndex = rawIdx || {};
  } catch(e) {
    _idiomsData  = {};
    _idiomsIndex = {};
  }
}

// INTENT: Load cognate family data for the given language (H or G). Uses separate JSON
//   files per language to avoid loading Hebrew data when studying Greek and vice versa.
//   Pre-warms both families array and the O(1) code→root index.
// CHANGE? If cognate-families or cognate-index file paths change, update both fetch URLs.
//   If a third language is added (Aramaic), extend _cognatesFamilies and _cognatesIndex.
// VERIFY: After studying a Hebrew passage, DevTools → Network shows one request to
//   cognate-families-hebrew.json and one to cognate-index-hebrew.json. No re-fetch on
//   subsequent passages in the same language.
export async function _loadCognates(lang) {
  var prefix = lang === 'greek' ? 'G' : 'H';
  if (_cognatesFamilies[prefix] !== null && _cognatesIndex[prefix] !== null) return;
  var langSlug = lang === 'greek' ? 'greek' : 'hebrew';
  try {
    var [famArr, idxObj] = await Promise.all([
      fetch(_resolve('../../data/grammar/cognate-families-' + langSlug + '.json')).then(function(r) { return r.ok ? r.json() : []; }),
      fetch(_resolve('../../data/grammar/cognate-index-' + langSlug + '.json')).then(function(r) { return r.ok ? r.json() : {}; }),
    ]);
    _cognatesFamilies[prefix] = famArr  || [];
    _cognatesIndex[prefix]    = idxObj  || {};
  } catch(e) {
    _cognatesFamilies[prefix] = [];
    _cognatesIndex[prefix]    = {};
  }
}

// INTENT: Lazy-load OT-in-NT quotations data. Builds two indexes on first load:
//   _otInNtByRef keys each quotation by the NT reference string for passage-based lookup.
//   Also builds _otInNtByOTRef for when the user is studying an OT passage and wants to
//   see how that OT text was quoted in the NT.
// CHANGE? If the nt_ref or ot_ref format in quotations.json changes, update the split logic here.
//   If the path moves, update the fetch URL.
// VERIFY: After studying Matt 1:23, DevTools → Network shows one request to quotations.json.
//   Click G3933 (παρθένος) in passage → "OT Source" section appears with three-column compare.
export async function _loadOTinNT() {
  if (_otInNtCache !== null) return;
  try {
    var arr = await fetch(_resolve('../../data/ot-in-nt/quotations.json')).then(function(r) { return r.ok ? r.json() : []; });
    _otInNtCache = arr || [];
    _otInNtByRef = {};
    _otInNtCache.forEach(function(q) {
      // Index by NT reference (e.g. "Matt 1:23")
      var ntKey = (q.nt_ref || '').trim();
      if (!_otInNtByRef[ntKey]) _otInNtByRef[ntKey] = [];
      _otInNtByRef[ntKey].push(q);
    });
  } catch(e) {
    _otInNtCache = [];
    _otInNtByRef = {};
  }
}

// INTENT: Check whether a debate's trigger_passages overlap with the current study passage.
//   Returns the matching trigger refs as strings (for display), or all triggers if no passage active.
// INTENT: Load author frequency data for the given language lazily. One file per language
//   to avoid loading OT author data when studying NT passages.
// CHANGE? If author-freq-*.json path or schema changes, update _renderAuthorFreqSection().
// VERIFY: Click G26 (ἀγάπη) in passage view → Author Frequency section appears at Student depth.
export async function _loadAuthorFreq(lang) {
  var key = lang === 'greek' ? 'greek' : 'hebrew';
  if (_authorFreqCache[key] !== null) return;
  try {
    var data = await fetch(_resolve('../../data/grammar/author-freq-' + key + '.json')).then(function(r) { return r.ok ? r.json() : {}; });
    _authorFreqCache[key] = data || {};
  } catch(e) {
    _authorFreqCache[key] = {};
  }
}

// INTENT: Load semantic field (PMI co-occurrence) data for the given language.
// CHANGE? If semantic-fields-*.json schema changes, update _renderSemanticSection().
// VERIFY: Click H2617 (חֶסֶד) → Semantic Neighborhood shows אֱמֶת and אֱמוּנָה chips.
export async function _loadSemanticFields(lang) {
  var key = lang === 'greek' ? 'greek' : 'hebrew';
  if (_semanticCache[key] !== null) return;
  try {
    var data = await fetch(_resolve('../../data/grammar/semantic-fields-' + key + '.json')).then(function(r) { return r.ok ? r.json() : {}; });
    _semanticCache[key] = data || {};
  } catch(e) {
    _semanticCache[key] = {};
  }
}

// INTENT: Load Second Temple context data lazily on first passage study or dossier open.
// CHANGE? If second-temple/context.json schema changes (strongs_keys or trigger_passages),
//   update _renderSTContext() accordingly.
// VERIFY: After studying any passage, DevTools → Network shows one request to context.json.
export async function _loadSTContext() {
  if (_stContextCache !== null) return;
  try {
    var arr = await fetch(_resolve('../../data/second-temple/context.json')).then(function(r) { return r.ok ? r.json() : []; });
    _stContextCache = arr || [];
  } catch(e) {
    _stContextCache = [];
  }
}

// INTENT: Lazily loads the synthesis JSON for a given book (SW-M). Each key in the file
//   is a pericope ref string (e.g. "Rom 1:16-17"); we parse it with parseRef and store
//   the structured entry so _renderSynthesisTab can do overlap matching against the
//   current passage. One file per book; only fetched when the Synthesis tab is clicked.
// CHANGE? If synthesis files move from data/synthesis/{bookId}.json, update path below.
//   If the key format changes, update the parseRef call and overlap logic in _renderSynthesisTab.
// VERIFY: Study Romans 1:16 → Synthesis tab → pericope card renders without 404 error.
//   Study Acts (no synthesis file) → tab shows "no synthesis notes" gracefully.
export async function _loadSynthesis(bookId) {
  if (_synthesisCache[bookId] !== undefined) return;
  _synthesisCache[bookId] = null;  // sentinel while fetching
  try {
    var data = await fetch(_resolve('../../data/synthesis/' + bookId + '.json'))
      .then(function(r) { return r.ok ? r.json() : null; });
    if (!data) { _synthesisCache[bookId] = []; return; }
    var entries = [];
    Object.keys(data).forEach(function(key) {
      var ref = parseRef(key);
      if (ref) entries.push({ key: key, ref: ref, data: data[key] });
    });
    _synthesisCache[bookId] = entries;
  } catch(e) {
    _synthesisCache[bookId] = [];
  }
}
