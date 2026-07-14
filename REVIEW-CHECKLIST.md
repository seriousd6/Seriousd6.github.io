# Owner Review Checklist — three arcs (updated 2026-07-14)

Hard-refresh once first (the service worker updates behind one stale load).
Three sets of major changes since your last hands-on pass. Anything that
does not match its expectation is a bug report.

---

## Arc 1 · The fix/feature batches (P14–P20)

1. **Search is ONE tool now** — /search/ has a single Search tab (plus the
   four browse hubs). Any query renders: answers panel → ranked verses →
   "Across the library" omni sections, all on one page. No Verse/Omni
   split anywhere.
2. **Relevance** — search "anxiety": raw results lead 1 Peter 5:7, Psalms
   94:19, Philippians 4:6 with KEY VERSE badges and a colored edge. Try
   "forgiveness", "money", "fear" — pastor-grade openers? A non-topic
   phrase ("green pastures") behaves classically, no badges.
3. **Maps on the phone** (was "completely unusable") — dropdown selector,
   tall full-width map, Overview/Sites/Refs stacked below. Root causes
   were a CDN single-point-of-failure (Leaflet is now self-hosted) and a
   mobile stylesheet that had never actually applied.
4. **Linked-reader scroll sync** — two Bible panels, same chapter, 🔗
   both; scroll either one, the other tracks by verse. Different text
   sizes/versions still align on content.
5. **Desk text size** — A− / A+ in the desk toolbar resizes every panel,
   persists, and applies to newly opened panels.
6. **Era auto-snap** — Bible + Maps linked: Genesis 12 → Journeys of the
   Patriarchs; John 3 → Palestine in the Time of Jesus; Acts 16 → Paul's
   Journeys. (This was silently broken when first shipped — re-verified
   against non-default eras after the fix.)
7. **2 Versions word-tap** — popover (lexeme + highlight row) works in
   both columns; select-a-word + W too.
8. **Small stuff** — timeline era rows "Era · count · c. YYYY–YYYY BC"
   stack cleanly in short panels; light-mode sidebar is paper-toned;
   Aa/Study Tools popovers are mutually exclusive; divider click + arrow
   keys resizes; no "Passage Study" debris anywhere; /history/ never
   nests itself.

## Arc 2 · The Original Languages decomposition (workshop → desk panels)

9. **The three-panel study rig** — Desk → Bible + OL Verse + Word
   Dossier, 🔗 all three. Navigate chapters: OL Verse follows with its
   interlinear tiles and insight tabs. Tap words in the reader (or click
   tiles in OL Verse): the Word Dossier follows every tap. This is the
   flagship flow — live in it for a real study session.
10. **Entry points** — reader Strong's banner "Dossier →", interlinear
    popover "Word Dossier →" (beside "All occurrences →"), study-drawer
    word blade "Word Dossier →": all open /ol/word/?s=CODE — inside the
    Desk, as a panel.
11. **Flashcards** — the 🄯 button lives in the word tab's header now;
    /ol/word/?fc=1 boots straight into review. Disciplines → Memory →
    Original Language shows the same deck and links "🄯 Flashcards →".
    Star a word in any dossier → it appears in both places.
12. **Retired per your decisions** — no ⚙ advanced panel, no translation
    mode, no dashboard, no review queue anywhere. Sidebar "Original
    Language Study" opens the Word Dossier directly.
13. **Which dossier sections do you actually use?** (grammar, tiers,
    attested uses, LXX bridge, cognates, author frequency, semantic
    fields…) — your answer drives what the module purge keeps
    first-class.

## Arc 3 · The study-blade decomposition (P26)

14. **Passage Study as a desk panel** — Desk chooser → "Passage Study"
    (or /study/passage/?ref=John+3 directly). The full drawer surface —
    outline, speakers, key words, places, context, cross-refs, echoes,
    and every blade — with no reader required on the page.
15. **Verse lock** — 🔗 a Bible panel and a Passage Study panel; navigate
    chapters — the study panel re-renders each chapter (verified through
    Romans 8).
16. **Blade → dossier chain** — in the Passage Study panel, open a key
    word ("Open word study (G4151) →") with a linked Word Dossier panel
    present: the dossier follows the word. Blades opening inside the
    panel (synthesis, biblepedia, place & time, book) should all work as
    they did in the drawer.
17. **The drawer is untouched** — on /read/, Study Tools → Study still
    opens the in-reader drawer exactly as before (this is the phone/
    single-window path).
18. **The four-panel rig** — Bible + Passage Study + Original Language +
    Word Dossier, all linked: navigate and tap. If this feels right, the
    decomposition thesis is proven.
19. **Deduped chooser (P27)** — the + Panel chooser is grouped
    (Read / Study / Explore / Daily), 13 entries: "Original Languages"
    and "Topical Answers" are gone (superseded by the Study panels and
    Search). The Original Language panel shows six tabs — Cross-refs and
    Commentary were removed there because the reader and Passage Study
    own those jobs. Does every remaining tab feel like its own concept?
