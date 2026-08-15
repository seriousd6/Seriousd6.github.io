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


# ── source residue and the thin exemption ───────────────────────────────────
# The prose rules require the writer to ignore scrape residue — a witness block
# that plainly belongs to another passage — and to omit it silently. But the
# thin exemption measures the RAW catena blob. Where a verse is mostly residue
# the two rules leave no legal output: over 200 raw words refuses the
# exemption, and the handful of usable words cannot honestly reach the 350-word
# floor. That is padding by contract, which is the defect the whole repair
# effort exists to remove. (Found on numbers 7; a corpus scan put the shape at
# 575 verses across 387 chapters.)
#
# The fix is to measure the source the way the writer is required to READ it.
# What is deliberately NOT done here is automatic residue detection: a rule that
# guessed wrong would silently license a short verse on a rich source, and no
# cheap textual test separates "JFB on the Day of Atonement, filed under Numbers
# 7" from "JFB on Numbers 7". So the exclusion is DECLARED on the tags entry and
# VERIFIED here — the same division of labour as the fidelity self-grade:
#
#     "excluded_voices": ["Jamieson, Fausset and Brown"]
#
# A declared voice must actually appear in the blob, so the field cannot be
# decorated with names to buy a thin pass, and every use of it is auditable
# per verse. Excluding a voice only ever LOWERS the measured source, and the
# only check that reads it is an upper bound (sw <= 200), so this can never
# turn a passing verse into a failing one.

# Display labels as they appear at the head of a segment in the merged catena.
VOICE_LABELS = [
    'Jamieson, Fausset and Brown', 'Keil and Delitzsch', 'Matthew Henry',
    'Adam Clarke', 'John Calvin', 'John Wesley', 'John Gill', 'Albert Barnes',
    'Charles Ellicott', 'Robertson', 'Charles Spurgeon', 'Martin Luther',
    'Augustine', 'Chrysostom', 'Origen', 'Basil', 'Bede', 'Tertullian',
    'Theodoret', 'Victorinus', 'Cyril', 'Gregory', 'Leo', 'Lightfoot',
]
_LABEL_RE = re.compile('(' + '|'.join(re.escape(v) for v in VOICE_LABELS) + r')\s*:')


def split_voices(blob):
    """Merged catena -> [(voice_label_or_None, segment_text)] in order."""
    text = visible(blob)
    parts, last, name = [], 0, None
    for m in _LABEL_RE.finditer(text):
        if m.start() > last:
            parts.append((name, text[last:m.start()].strip()))
        name = m.group(1)
        last = m.end()
    parts.append((name, text[last:].strip()))
    return [(n, s) for n, s in parts if s]


def usable_source_words(blob, excluded_voices=None):
    """Visible words of a catena minus the voice blocks declared as residue."""
    ex = {str(v).strip().lower() for v in (excluded_voices or []) if str(v).strip()}
    if not ex:
        return len(visible(blob).split())
    return sum(len(seg.split()) for name, seg in split_voices(blob)
               if not (name and name.lower() in ex))


def undeclarable_voices(blob, excluded_voices):
    """Declared exclusions that do not actually occur in this verse's blob."""
    present = {n.lower() for n, _ in split_voices(blob) if n}
    return [v for v in (excluded_voices or [])
            if str(v).strip().lower() not in present]


# ── pericopes: one entry covering a span of verses ──────────────────────────
# Some passages say the same thing many times over. Numbers 7 runs the identical
# tribal offering twelve times; a register chapter lists towns. Writing one entry
# per verse there produces twelve near-identical write-ups, which reads as
# template however carefully each is worded — and templating is the defect the
# audit found.
#
# A tags entry may therefore cover a SPAN instead of a single verse:
#
#     "12": { "range": "12-17", "pericope_label": "Nahshon of Judah offers", ... }
#
# The prose file carries ONE entry, keyed at the range start. "pericope" is the
# vocabulary Commentary B already uses (pericope_label + range), so the two
# commentaries name the same idea the same way.
#
# The reader needs no new data to render this: every render path already
# resolves a verse by walking back to the nearest key, so a span is found by the
# verses inside it, and the grid already gives one commentary cell spanning the
# section's rows. What the display could not do before was state the span
# HONESTLY — it inferred the end from the next key, which is only true if the
# keys have no gaps. Enforcing exact coverage here is what makes that inference
# sound, and is why the rule below is coverage rather than "keys must exist".
_RANGE_RE = re.compile(r'^\s*(\d+)\s*(?:[-–]\s*(\d+))?\s*$')


def parse_range(key, rng):
    """('12', '12-17') -> (12, 17). A missing/blank range is the single verse."""
    if rng is None or str(rng).strip() == '':
        n = int(key)
        return (n, n)
    m = _RANGE_RE.match(str(rng))
    if not m:
        raise ValueError(f'unparseable range {rng!r}')
    lo = int(m.group(1))
    hi = int(m.group(2)) if m.group(2) else lo
    return (lo, hi)


def span_keys(key, rng):
    """The source keys an entry covers, as strings. Unparseable ranges degrade
    to the single verse rather than raising — the range's SHAPE is the
    validator's business, and a measurement tool must not die on bad data."""
    try:
        lo, hi = parse_range(key, rng)
    except ValueError:
        lo = hi = int(key)
    return [str(v) for v in range(lo, hi + 1)]


def span_source_text(source, key, rng=None):
    """The catena an entry actually stands on, joined across its span.

    A pericope covers a range of verses, so its source is the UNION of the
    verses it covers — not the blob filed under its start key. Measuring only
    the start key makes every ranged entry look like an invention: the Numbers
    32 "18-19" entry read as 9.6x expansion against the 43 words under key 18,
    where the real figure is 1.09x against the 380 words of the span. The thin
    exemption in validate-synthesis.py has always summed the span; the expansion
    ratio did not, and the two must agree or the writer is graded against a
    denominator no rule uses.
    """
    return ' '.join(str(source.get(k) or '') for k in span_keys(key, rng))


def span_source_words(source, key, rng=None, excluded_voices=None):
    """Usable words of the span's catena, after any declared residue."""
    return sum(usable_source_words(source.get(k) or '', excluded_voices)
               for k in span_keys(key, rng))


def coverage_problems(source_keys, entries):
    """Check that the declared spans tile the chapter exactly.

    `entries` is {prose_key: range_string_or_None}. Returns a list of human
    problems: a span whose key is not its own start, a verse covered twice, a
    verse covered not at all, or a span reaching outside the chapter.
    """
    problems, seen = [], {}
    want = {int(k) for k in source_keys}
    for key in sorted(entries, key=lambda k: int(k)):
        try:
            lo, hi = parse_range(key, entries[key])
        except ValueError as e:
            problems.append(f'{key}: {e}')
            continue
        if lo != int(key):
            problems.append(f'{key}: range starts at {lo}, so it must be keyed "{lo}"')
        if hi < lo:
            problems.append(f'{key}: range ends ({hi}) before it starts ({lo})')
            continue
        for v in range(lo, hi + 1):
            if v in seen:
                problems.append(f'verse {v} is covered twice (by {seen[v]} and {key})')
            seen[v] = key
    missing = sorted(want - set(seen))
    if missing:
        problems.append(f'verses covered by no entry: {missing[:12]}'
                        + ('…' if len(missing) > 12 else ''))
    extra = sorted(set(seen) - want)
    if extra:
        problems.append(f'entries cover verses absent from the source: {extra[:12]}'
                        + ('…' if len(extra) > 12 else ''))
    return problems


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
