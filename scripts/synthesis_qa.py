#!/usr/bin/env python3
"""
synthesis_qa.py — shared QA contract for Commentary A.

Imported by validate-synthesis.py (shape enforcement), by
audit-synthesis-quality.py (grading), and by backfill-synthesis-qa.py.
Keeping it in one place means the standard version, the check ids, and the
grounding logic cannot drift between the three.

THE PER-VERSE QA BLOCK lives on the verse's TAGS entry:

    "qa": {
      "v": 1,                                  # schema version of this block
      "standard": "cow-prose-rules-2026-08-09",# which writing standard applied
      "generated": "2026-08-09",               # when the prose was written
      "grade": "A",                            # lint grade AT THAT TIME
      "checks": ["length", "refs-linked", ...],# what was actually verified
      "lint": "audit-synthesis-quality/1"      # tool + version that graded it
    }

Why record the grade rather than recompute it: the next wave of repairs needs to
know what standard a verse was written to and what it scored *then*, so it can
tell "already repaired" from "not yet looked at" without re-reading the corpus.
A recomputed grade tells you the state; the recorded one tells you the history.
"""
import json, os, re, glob

QA_SCHEMA_VERSION = 1

# Standards, newest first. A verse records which one it was written to.
STANDARDS = {
    'cow-prose-rules-2026-08-09':
        'Six prose rules + thin exemption + lint gate (post-quality-audit).',
    'legacy-unversioned':
        'Written before any recorded standard; length/refs/tags only.',
}
CURRENT_STANDARD = 'cow-prose-rules-2026-08-09'
LEGACY_STANDARD = 'legacy-unversioned'

# Verses carrying LEGACY_STANDARD are the known debt from the 2026-07-22 batch:
# the CI gate exempts them so it can be switched on before the repair lands.
# This baseline is the ratchet — the exempt set may SHRINK as chapters are
# repaired, never grow. Raising it is how the exemption would quietly become a
# loophole, so the gate fails if the legacy count exceeds it.
LEGACY_BASELINE = 21682

# Check ids. A verse lists the ones actually performed on it.
CHECKS = {
    'length':         'word count inside the window (or a justified thin exemption)',
    'refs-linked':    'every scripture reference is an <a class="ref"> link',
    'tags-match':     'prose and tags verse keys correspond 1:1',
    'schools-valid':  'school slugs and prevalence come from the enums',
    'voices-sourced': 'every tagged voice is groundable in a source corpus',
    'no-meta':        'does not narrate the source\'s thinness to the reader',
    'no-noise':       'does not narrate that a fragment was skipped',
    'no-slot':        'no degenerate "; the <clause> (<gloss>)" slot-lists',
    'no-carriers':    'no banned stock carrier phrase used as filler',
    'quotes-capped':  'quoted scripture within budget, no fragment quoted twice',
    'fidelity-self-graded':
                      'the writer re-read each verse against its source and '
                      'graded whether the prose says only what the witnesses say',
}
GRADES = ('A', 'B', 'C', 'D')

# ── fidelity ────────────────────────────────────────────────────────────────
# The lint can measure repetition and whether a NAMED voice exists in the
# source. It cannot judge whether a 430-word paraphrase of 90 words of Gill
# still says what Gill said — that is a reading task, so it is graded by the
# writer and recorded, not inferred.
#
#   A  every claim traces to the source; expansion is framing, not new content
#   B  faithful, but stretched — the prose leans further than the witness does
#   C  contains a claim the source does not support (do not ship; rewrite)
#
# A note is required for anything below A, so "B" cannot become a shrug.
FIDELITY_GRADES = ('A', 'B', 'C')
# Expansion beyond this is not wrong, but it is where invention would live:
# 7% of the corpus is above it, and a 400-word verse built on 15 words of
# catena deserves a second look before it ships.
STRETCH_RATIO = 6.0

def expansion_ratio(prose_words, source_words):
    if not source_words:
        return None
    return round(prose_words / source_words, 2)

def fidelity_problems(f, required):
    if f is None:
        return ['fidelity is required for the current standard — the writer '
                'must re-read each verse against its source and grade it'] if required else []
    if not isinstance(f, dict):
        return ['fidelity must be an object']
    p = []
    if f.get('grade') not in FIDELITY_GRADES:
        p.append(f'fidelity.grade must be one of {FIDELITY_GRADES}')
    if f.get('grade') == 'C':
        p.append('fidelity.grade C means an unsupported claim is present — '
                 'rewrite the verse rather than recording it')
    if f.get('grade') in ('B', 'C') and not str(f.get('note') or '').strip():
        p.append('fidelity.note is required when the grade is not A')
    if 'expansion' in f and not isinstance(f['expansion'], (int, float, type(None))):
        p.append('fidelity.expansion must be a number')
    if not str(f.get('checked_by') or '').strip():
        p.append('fidelity.checked_by must say who graded it')
    return p

TAG = re.compile(r'<[^>]+>')
def visible(html):
    return re.sub(r'\s+', ' ', TAG.sub(' ', str(html or ''))).strip()


# ── voice grounding ─────────────────────────────────────────────────────────
# A voice is grounded if any distinctive token of its name appears in the
# merged catena OR any per-commentator corpus for that book+chapter.
#
# Three ways this check has been got wrong, all fixed here:
#   * matching on the LAST name token flags every "X of Y" patristic name,
#     because Pelusium / Hippo / Nyssa are places, not surnames;
#   * a >=4-character token filter silently drops "Leo";
#   * checking only cow/ misses everything drawn from cow-sources/.
_STOP_NAME = {'of', 'the', 'and', 'de', 'von', 'saint'}

def name_keys(voice):
    return [t.lower() for t in re.findall(r"[A-Za-z']+", str(voice))
            if len(t) >= 3 and t.lower() not in _STOP_NAME]

def _hit(keys, pool):
    for k in keys:
        if k in pool or (len(k) > 5 and k[:5] in pool):
            return True
    return False

class SourceIndex:
    """Lazily pools every source text available for a book+chapter."""
    def __init__(self, root):
        self.root = root
        self._cache = {}
        self._dirs = [d for d in glob.glob(os.path.join(root, 'data/commentary/cow-sources/*'))
                      if os.path.isdir(d)]

    def pool(self, book, ch):
        key = (book, ch)
        if key in self._cache:
            return self._cache[key]
        parts = []
        merged = os.path.join(self.root, 'data/commentary/cow', book, f'{ch}.json')
        if os.path.exists(merged):
            try:
                parts.append(visible(' '.join(json.load(open(merged, encoding='utf-8')).values())))
            except Exception:
                pass
        for d in self._dirs:
            by_book = os.path.join(d, f'{book}.json')
            if os.path.exists(by_book):
                try:
                    dd = json.load(open(by_book, encoding='utf-8'))
                    c = (dd.get('chapters') or dd).get(ch)
                    if c is not None:
                        parts.append(visible(c))
                except Exception:
                    pass
            by_ch = os.path.join(d, book, f'{ch}.json')
            if os.path.exists(by_ch):
                try:
                    parts.append(visible(json.load(open(by_ch, encoding='utf-8'))))
                except Exception:
                    pass
        self._cache[key] = ' '.join(parts).lower()
        return self._cache[key]

    def ungrounded_voices(self, book, ch, voices):
        """Voices with no comment on this chapter in ANY source corpus."""
        p = self.pool(book, ch)
        if not p:
            return []          # no sources on disk: cannot judge, do not accuse
        return [v for v in (voices or []) if not _hit(name_keys(v), p)]


# ── qa block validation ─────────────────────────────────────────────────────
def qa_problems(qa):
    """Return a list of human-readable problems with a qa block ([] if fine)."""
    if not isinstance(qa, dict):
        return ['qa must be an object']
    p = []
    if qa.get('v') != QA_SCHEMA_VERSION:
        p.append(f'qa.v must be {QA_SCHEMA_VERSION}')
    if qa.get('standard') not in STANDARDS:
        p.append(f'qa.standard unknown: {qa.get("standard")!r}')
    if qa.get('grade') not in GRADES:
        p.append(f'qa.grade must be one of {GRADES}')
    if not re.fullmatch(r'\d{4}-\d{2}-\d{2}', str(qa.get('generated', ''))):
        p.append('qa.generated must be YYYY-MM-DD')
    ch = qa.get('checks')
    if not isinstance(ch, list) or not ch:
        p.append('qa.checks must be a non-empty list')
    else:
        unknown = [c for c in ch if c not in CHECKS]
        if unknown:
            p.append(f'qa.checks has unknown ids: {unknown}')
    if not isinstance(qa.get('lint'), str) or not qa.get('lint'):
        p.append('qa.lint must name the tool that graded it')
    # Fidelity is mandatory for work written to the current standard, and absent
    # from the legacy debt (nobody read those against their sources).
    p += fidelity_problems(qa.get('fidelity'),
                           required=qa.get('standard') == CURRENT_STANDARD)
    return p
