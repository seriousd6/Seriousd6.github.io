#!/usr/bin/env python3
"""
fetch-nave.py — Download Nave's Topical Bible from CrossWire SWORD module.

Source: https://www.crosswire.org/ftpmirror/pub/sword/packages/rawzip/Nave.zip
Format: zLD (compressed Lexical Dictionary), TEI XML content

Output:
  data/topical/nave.json                  — all topics [{slug, title, verses}]
  data/topical/verse-index/{bookId}.json  — reverse index {"ch:v": ["slug",...]}

Usage:
  python3 scripts/fetch-nave.py
  python3 scripts/fetch-nave.py --force   # re-generate even if up to date
"""

import io, json, re, struct, sys, urllib.request, zipfile, zlib, argparse
from pathlib import Path

REPO_ROOT    = Path(__file__).parent.parent
BOOKS_JSON   = REPO_ROOT / 'data' / 'bible' / 'books.json'
OUT_DIR      = REPO_ROOT / 'data' / 'topical'
VIDX_DIR     = OUT_DIR / 'verse-index'
NAVE_ZIP_URL = 'https://www.crosswire.org/ftpmirror/pub/sword/packages/rawzip/Nave.zip'

# ── OSIS book abbreviation → (bookId, displayName) ───────────────────────────
OSIS_BOOKS = {
    'Gen':'genesis','Exod':'exodus','Lev':'leviticus','Num':'numbers',
    'Deut':'deuteronomy','Josh':'joshua','Judg':'judges','Ruth':'ruth',
    '1Sam':'1samuel','2Sam':'2samuel','1Kgs':'1kings','2Kgs':'2kings',
    '1Chr':'1chronicles','2Chr':'2chronicles','Ezra':'ezra','Neh':'nehemiah',
    'Esth':'esther','Job':'job','Ps':'psalms','Prov':'proverbs',
    'Eccl':'ecclesiastes','Song':'songofsolomon','Isa':'isaiah','Jer':'jeremiah',
    'Lam':'lamentations','Ezek':'ezekiel','Dan':'daniel','Hos':'hosea',
    'Joel':'joel','Amos':'amos','Obad':'obadiah','Jonah':'jonah',
    'Mic':'micah','Nah':'nahum','Hab':'habakkuk','Zeph':'zephaniah',
    'Hag':'haggai','Zech':'zechariah','Mal':'malachi',
    'Matt':'matthew','Mark':'mark','Luke':'luke','John':'john','Acts':'acts',
    'Rom':'romans','1Cor':'1corinthians','2Cor':'2corinthians','Gal':'galatians',
    'Eph':'ephesians','Phil':'philippians','Col':'colossians',
    '1Thess':'1thessalonians','2Thess':'2thessalonians','1Tim':'1timothy',
    '2Tim':'2timothy','Titus':'titus','Phlm':'philemon','Heb':'hebrews',
    'Jas':'james','1Pet':'1peter','2Pet':'2peter','1John':'1john',
    '2John':'2john','3John':'3john','Jude':'jude','Rev':'revelation',
}

def load_book_names():
    with open(BOOKS_JSON) as f:
        books = json.load(f)
    return {b['id']: b['name'] for b in books}

def slugify(title):
    s = title.lower()
    s = re.sub(r"[^\w\s-]", '', s)
    s = re.sub(r'[\s_]+', '-', s).strip('-')
    return s

def parse_osis_ref(osis_ref):
    """Parse an osisRef like 'Exod.6.16' or '1Kgs.18.24-1Kgs.18.39'.
    Returns list of canonical refs like ['Exodus 6:16'] or ['1 Kings 18:24-39'].
    """
    # Strip any extra whitespace
    osis_ref = osis_ref.strip()
    # Handle ranges: "Book.Ch.V-Book.Ch.V" or "Book.Ch.V-Book.Ch.V2"
    parts = osis_ref.split('-')
    if not parts:
        return []

    # Parse start
    start = parts[0].split('.')
    if len(start) < 2:
        return []
    osis_book = start[0]
    book_id = OSIS_BOOKS.get(osis_book)
    if not book_id:
        return []
    ch = start[1] if len(start) > 1 else '1'
    v  = start[2] if len(start) > 2 else None

    if len(parts) == 1:
        # Single ref
        if v:
            return [(book_id, ch, v, v)]
        else:
            return [(book_id, ch, None, None)]

    # Range: determine end
    end = parts[1].split('.')
    # End might be same book (just ch.v) or different book
    if len(end) == 3:
        end_osis_book = end[0]
        end_book_id = OSIS_BOOKS.get(end_osis_book, book_id)
        end_ch = end[1]
        end_v  = end[2]
    elif len(end) == 2:
        end_book_id = book_id
        end_ch = end[0]
        end_v  = end[1]
    elif len(end) == 1:
        end_book_id = book_id
        end_ch = ch
        end_v  = end[0]
    else:
        end_book_id = book_id
        end_ch = ch
        end_v  = v

    if v and (book_id == end_book_id) and (ch == end_ch):
        return [(book_id, ch, v, end_v)]
    else:
        # Cross-chapter or cross-book range — just use start verse
        if v:
            return [(book_id, ch, v, v)]
        else:
            return [(book_id, ch, None, None)]

def format_ref(book_id, ch, v, end_v, book_names):
    name = book_names.get(book_id, book_id)
    if v is None:
        return f'{name} {ch}'
    if end_v and end_v != v:
        return f'{name} {ch}:{v}-{end_v}'
    return f'{name} {ch}:{v}'

# ── SWORD zLD parser ──────────────────────────────────────────────────────────
def parse_sword_zld(z):
    """Return list of (key, content_xml) for all entries in the zLD module."""
    idx_data = z.read('modules/lexdict/zld/nave/dict.idx')
    dat_data = z.read('modules/lexdict/zld/nave/dict.dat')
    zdx_data = z.read('modules/lexdict/zld/nave/dict.zdx')
    zdt_data = z.read('modules/lexdict/zld/nave/dict.zdt')

    # Parse block table from zdx
    blocks = []
    for i in range(0, len(zdx_data), 8):
        off, sz = struct.unpack_from('<II', zdx_data, i)
        blocks.append((off, sz))

    # Decompress all blocks
    decompressed = {}
    for bn, (off, sz) in enumerate(blocks):
        try:
            raw = zlib.decompress(zdt_data[off:off+sz])
            numE = struct.unpack_from('<I', raw, 0)[0]
            entries = []
            for ei in range(numE):
                eOff, eSz = struct.unpack_from('<II', raw, 4 + ei*8)
                entries.append(raw[eOff:eOff+eSz].decode('utf-8', 'replace'))
            decompressed[bn] = entries
        except Exception:
            decompressed[bn] = []

    # Parse dat (key → block lookup)
    results = []
    for i in range(0, len(idx_data), 8):
        off, sz = struct.unpack_from('<II', idx_data, i)
        chunk = dat_data[off:off+sz]
        nl = chunk.find(b'\r\n')
        if nl < 0:
            continue
        key = chunk[:nl].decode('utf-8', 'replace').strip()
        if len(chunk) < nl + 10:
            continue
        block_num   = struct.unpack_from('<I', chunk, nl+2)[0]
        entry_in_block = struct.unpack_from('<I', chunk, nl+6)[0]
        block_entries = decompressed.get(block_num, [])
        if entry_in_block < len(block_entries):
            content = block_entries[entry_in_block]
            results.append((key, content))

    return results

# ── Extract verse refs from TEI XML content ───────────────────────────────────
OSIS_REF_RE = re.compile(r'osisRef="([^"]+)"')

def extract_refs(xml_content, book_names):
    """Return list of canonical ref strings extracted from osisRef attributes."""
    refs = []
    seen = set()
    for m in OSIS_REF_RE.finditer(xml_content):
        osis_str = m.group(1)
        # May be space-separated multi-ref
        for part in osis_str.split():
            parsed = parse_osis_ref(part)
            for p in parsed:
                r = format_ref(p[0], p[1], p[2], p[3], book_names)
                if r not in seen:
                    seen.add(r)
                    refs.append(r)
    return refs

# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--force', action='store_true')
    args = parser.parse_args()

    nave_out = OUT_DIR / 'nave.json'
    if nave_out.exists() and not args.force:
        print(f'{nave_out} already exists — use --force to regenerate.')
        return

    book_names = load_book_names()
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    VIDX_DIR.mkdir(parents=True, exist_ok=True)

    print(f'Downloading {NAVE_ZIP_URL} …')
    with urllib.request.urlopen(NAVE_ZIP_URL) as resp:
        data = resp.read()
    print(f'  Downloaded {len(data):,} bytes')

    with zipfile.ZipFile(io.BytesIO(data)) as z:
        raw_entries = parse_sword_zld(z)

    print(f'  Parsed {len(raw_entries)} topics')

    topics = []
    # verse-index: bookId → {"ch:v": [slugs]}
    verse_index = {}

    for title, xml in raw_entries:
        slug  = slugify(title)
        if not slug:
            continue
        refs  = extract_refs(xml, book_names)
        # Deduplicate while preserving order
        seen_refs = set()
        unique_refs = []
        for r in refs:
            if r not in seen_refs:
                seen_refs.add(r)
                unique_refs.append(r)

        topics.append({'slug': slug, 'title': title, 'verses': unique_refs})

        # Build verse-index
        for ref_str in unique_refs:
            # Parse ref_str back to bookId + ch:v
            # Format: "Book Ch:V" or "Book Ch:V-V2" or "Book Ch"
            m = re.match(r'^(.+?)\s+(\d+)(?::(\d+))?', ref_str)
            if not m:
                continue
            book_name_str = m.group(1).strip()
            ch = m.group(2)
            v  = m.group(3)
            if not v:
                continue  # skip chapter-only refs in verse-index
            # Find bookId from name
            book_id = next((bid for bid, n in book_names.items() if n == book_name_str), None)
            if not book_id:
                continue
            key = f'{ch}:{v.split("-")[0]}'  # normalize "3:16-20" → "3:16"
            if book_id not in verse_index:
                verse_index[book_id] = {}
            if key not in verse_index[book_id]:
                verse_index[book_id][key] = []
            if slug not in verse_index[book_id][key]:
                verse_index[book_id][key].append(slug)

    # Write main nave.json
    with open(nave_out, 'w') as f:
        json.dump(topics, f, separators=(',', ':'))
    print(f'  Wrote {nave_out} ({nave_out.stat().st_size:,} bytes, {len(topics)} topics)')

    # Write per-book verse-index files
    for book_id, chv_map in verse_index.items():
        out_path = VIDX_DIR / f'{book_id}.json'
        with open(out_path, 'w') as f:
            json.dump(chv_map, f, separators=(',', ':'))

    print(f'  Wrote {len(verse_index)} verse-index files to {VIDX_DIR}/')
    print('Done.')

if __name__ == '__main__':
    main()
