# Owner Review Checklist — 2026-07-13 session (P14–P20)

Hard-refresh once first (the service worker updates behind one stale load).
Ordered newest-first. Anything that doesn't match its expectation is a bug
report.

## P19 desk mechanics

1. **Scroll sync** — Desk → two Bible panels, same chapter (Psalm 119),
   🔗 on both. Scroll either; the other tracks by VERSE, whichever you
   scroll leads. Different text sizes/versions per panel should still
   align on the same verse, not drift.
2. **Desk text size** — toolbar A− / A+: all panels resize together, %
   label appears, size survives a desk reload, and a newly opened panel
   arrives already at that size.
3. **Workshop verse-lock** — Bible + Original Languages panels, 🔗 both,
   navigate the reader through 2–3 chapters — the workshop re-studies each
   passage. Note whether the per-navigation load feels heavy.

## P20 relevance

4. **Search "anxiety"** — leads 1 Peter 5:7, Psalms 94:19, Philippians
   4:6 with KEY VERSE badges + colored left edge. Also try "forgiveness",
   "money", "fear" — do the openers feel pastor-grade?
5. **Non-topic phrase** ("green pastures") — behaves as before, no badges.
6. **Sort: Bible order** — badges remain, order becomes canonical; flip
   back.

## P16–P18 fixes

7. **Maps on the phone** (was "completely unusable") — dropdown selector,
   full-width tall map, Overview/Sites/Refs below. A skinny desktop desk
   maps panel gets the same treatment.
8. **Era auto-snap** — Bible + Maps linked: John 3 → "Palestine in the
   Time of Jesus"; Genesis 12 → Patriarchal Journeys; Acts 16 → Paul's
   Journeys.
9. **2 Versions word-tap** — popover (lexeme + highlight row) works in
   BOTH columns; select-a-word + W works there too.
10. **Timeline in a desk panel** — rows read "Era · count · c. YYYY–YYYY
    BC" and stack without overlap in a short panel.
11. **Light-mode sidebar** — paper-toned, readable everywhere (hovers,
    section labels, active item); dark still ink.

## Regression sweep

12. No "Passage Study" debris at the bottom of any reader, under
    parallels, or in desk reader panels.
13. /history/ — no "← History" inside tabs; no nested tab bars.
14. Aa and Study Tools popovers can't be open at once.
15. Hover a term then immediately click next-chapter — no orphaned tooltip
    top-left.
16. Click a desk divider, then arrow keys — panels resize.
17. Parallels header bands readable in dark mode; /about/ lead readable on
    phone.

## Feeds the OL decomposition (OL-DESK-PLAN.md)

18. Use the linked workshop panel for one real study pass and note which
    two or three sections you actually consult (tiles? Grammar? Word
    dossier? Literary/Cultural?). That decides what Phase 2 extracts
    first; everything untouched is on the retirement list.
