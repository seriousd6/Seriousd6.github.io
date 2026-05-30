#!/usr/bin/env python3
"""
fetch-torrey.py — Download Torrey's New Topical Textbook from CrossWire SWORD module.

Source: https://www.crosswire.org/ftpmirror/pub/sword/packages/rawzip/Torrey.zip
Format: zLD (compressed Lexical Dictionary), TEI XML with verse refs
Year:   1897 (public domain)

Output:
  data/torrey/torrey.json                  — [{slug, title, verses}]
  data/torrey/verse-index/{bookId}.json    — {"ch:v": ["slug",...]}

Usage:
  python3 scripts/fetch-torrey.py
  python3 scripts/fetch-torrey.py --force
"""

import io, json, re, struct, urllib.request, zipfile, zlib, argparse
from pathlib import Path

REPO_ROOT    = Path(__file__).parent.parent
BOOKS_JSON   = REPO_ROOT / 'data' / 'bible' / 'books.json'
OUT_DIR      = REPO_ROOT / 'data' / 'torrey'
VIDX_DIR     = OUT_DIR / 'verse-index'
TORREY_URL   = 'https://www.crosswire.org/ftpmirror/pub/sword/packages/rawzip/Torrey.zip'

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

# Torrey rawld uses its own abbreviation scheme inside <scripRef> tags
TORREY_ABBREVS = {
    'Ge':'genesis','Ex':'exodus','Le':'leviticus','Nu':'numbers',
    'De':'deuteronomy','Jos':'joshua','Jud':'judges','Ru':'ruth',
    '1Sa':'1samuel','2Sa':'2samuel','1Ki':'1kings','2Ki':'2kings',
    '1Ch':'1chronicles','2Ch':'2chronicles','Ezr':'ezra','Ne':'nehemiah',
    'Es':'esther','Job':'job','Ps':'psalms','Pr':'proverbs',
    'Ec':'ecclesiastes','So':'songofsolomon','Is':'isaiah','Jer':'jeremiah',
    'La':'lamentations','Eze':'ezekiel','Da':'daniel','Ho':'hosea',
    'Joe':'joel','Am':'amos','Ob':'obadiah','Jon':'jonah',
    'Mic':'micah','Na':'nahum','Hab':'habakkuk','Zep':'zephaniah',
    'Hag':'haggai','Zec':'zechariah','Mal':'malachi',
    'Mt':'matthew','Mr':'mark','Lu':'luke','Joh':'john','Ac':'acts',
    'Ro':'romans','1Co':'1corinthians','2Co':'2corinthians','Ga':'galatians',
    'Eph':'ephesians','Php':'philippians','Col':'colossians',
    '1Th':'1thessalonians','2Th':'2thessalonians','1Ti':'1timothy',
    '2Ti':'2timothy','Tit':'titus','Phm':'philemon','Heb':'hebrews',
    'Jas':'james','1Pe':'1peter','2Pe':'2peter','1Jo':'1john',
    '2Jo':'2john','3Jo':'3john','Jude':'jude','Re':'revelation',
}


def load_book_names():
    with open(BOOKS_JSON) as f:
        return {b['id']: b['name'] for b in json.load(f)}


def slugify(title):
    s = re.sub(r"[^\w\s-]", '', title.lower())
    return re.sub(r'[\s_]+', '-', s).strip('-') or None


def parse_osis_ref(osis_ref, book_names):
    """Return list of (book_id, ch, v_start, v_end) tuples."""
    osis_ref = osis_ref.strip()
    parts = osis_ref.split('-')
    start = parts[0].split('.')
    if len(start) < 2: return []
    book_id = OSIS_BOOKS.get(start[0])
    if not book_id: return []
    ch = start[1]
    v  = start[2] if len(start) > 2 else None

    if len(parts) == 1:
        return [(book_id, ch, v, v)] if v else [(book_id, ch, None, None)]

    end = parts[1].split('.')
    if len(end) == 3:
        end_book_id = OSIS_BOOKS.get(end[0], book_id)
        end_ch, end_v = end[1], end[2]
    elif len(end) == 2:
        end_book_id, end_ch, end_v = book_id, end[0], end[1]
    elif len(end) == 1:
        end_book_id, end_ch, end_v = book_id, ch, end[0]
    else:
        return [(book_id, ch, v, v)] if v else []

    if v and book_id == end_book_id and ch == end_ch:
        return [(book_id, ch, v, end_v)]
    return [(book_id, ch, v, v)] if v else [(book_id, ch, None, None)]


def format_ref(book_id, ch, v, end_v, book_names):
    name = book_names.get(book_id, book_id)
    if v is None: return f'{name} {ch}'
    if end_v and end_v != v: return f'{name} {ch}:{v}-{end_v}'
    return f'{name} {ch}:{v}'


def detect_module(z):
    names = z.namelist()
    conf_files = [n for n in names if n.lower().endswith('.conf')]
    moddrv = ''
    if conf_files:
        try:
            conf = z.read(conf_files[0]).decode('utf-8', errors='replace')
            m = re.search(r'ModDrv\s*=\s*(\w+)', conf, re.IGNORECASE)
            if m: moddrv = m.group(1).strip()
        except Exception:
            pass
    idx_files = [n for n in names if n.endswith('.idx')]
    if not idx_files: return None, None
    base = idx_files[0][:-4]
    is_zld = (base + '.zdx' in names) if not moddrv else (moddrv.lower() == 'zld')
    return base, is_zld


def parse_zld(z, base):
    idx_data = z.read(base + '.idx')
    dat_data = z.read(base + '.dat')
    zdx_data = z.read(base + '.zdx')
    zdt_data = z.read(base + '.zdt')

    blocks = []
    for i in range(0, len(zdx_data), 8):
        off, sz = struct.unpack_from('<II', zdx_data, i)
        blocks.append((off, sz))

    decompressed = {}
    for bn, (off, sz) in enumerate(blocks):
        try:
            raw  = zlib.decompress(zdt_data[off:off+sz])
            numE = struct.unpack_from('<I', raw, 0)[0]
            entries = []
            for ei in range(numE):
                eOff, eSz = struct.unpack_from('<II', raw, 4 + ei*8)
                entries.append(raw[eOff:eOff+eSz].decode('utf-8', 'replace'))
            decompressed[bn] = entries
        except Exception:
            decompressed[bn] = []

    results = []
    for i in range(0, len(idx_data), 8):
        off, sz = struct.unpack_from('<II', idx_data, i)
        chunk = dat_data[off:off+sz]
        nl = chunk.find(b'\r\n')
        if nl < 0: continue
        key = chunk[:nl].decode('utf-8', 'replace').strip()
        if len(chunk) < nl+10: continue
        block_num      = struct.unpack_from('<I', chunk, nl+2)[0]
        entry_in_block = struct.unpack_from('<I', chunk, nl+6)[0]
        block_entries  = decompressed.get(block_num, [])
        if entry_in_block < len(block_entries):
            results.append((key, block_entries[entry_in_block]))
    return results


def parse_rawld(z, base):
    idx_data = z.read(base + '.idx')
    dat_data = z.read(base + '.dat')
    entry_size = 8 if (len(idx_data) % 8 == 0 and len(idx_data) % 6 != 0) else 6
    results = []
    for i in range(0, len(idx_data), entry_size):
        if entry_size == 8:
            off, sz = struct.unpack_from('<II', idx_data, i)
        else:
            off = struct.unpack_from('<I', idx_data, i)[0]
            sz  = struct.unpack_from('<H', idx_data, i+4)[0]
        chunk = dat_data[off:off+sz]
        nl = chunk.find(b'\n')
        if nl < 0: continue
        key     = chunk[:nl].decode('utf-8', 'replace').strip()
        content = chunk[nl+1:].decode('utf-8', 'replace').strip()
        if key and content:
            results.append((key, content))
    return results


OSIS_REF_RE  = re.compile(r'osisRef="([^"]+)"')
SCRIP_REF_RE = re.compile(r'<scripRef>(.*?)</scripRef>', re.DOTALL)

# Match a leading book abbreviation (1–3 chars, optionally preceded by digit)
_BOOK_PREFIX_RE = re.compile(r'^(\d?[A-Z][a-z]{0,2})\s+')


def _parse_scripref_content(content, book_names):
    """Parse Torrey rawld scripRef text → list of formatted ref strings."""
    refs, seen = [], set()
    current_book_id = None

    for segment in re.split(r'[;]', content):
        segment = segment.strip()
        if not segment:
            continue

        # Check if this segment starts with a book abbreviation
        bm = _BOOK_PREFIX_RE.match(segment)
        if bm:
            abbrev = bm.group(1)
            book_id = TORREY_ABBREVS.get(abbrev)
            if book_id:
                current_book_id = book_id
                segment = segment[bm.end():]  # strip the book prefix

        if not current_book_id:
            continue

        book_name = book_names.get(current_book_id, current_book_id)

        # Remaining segment: may be "ch:v1,v2" or "ch:v" or "ch" or "v1,v2"
        # Split by comma to handle multiple verses in same chapter
        # First try to get a chapter from segment (contains colon)
        if ':' in segment:
            ch_str, rest = segment.split(':', 1)
            ch_str = ch_str.strip()
            # rest may be "7,25" or "7"
            for v_str in rest.split(','):
                v_str = v_str.strip()
                if not v_str or not v_str[0].isdigit():
                    continue
                # Handle verse ranges like "7-10" — take start verse
                v_clean = re.split(r'[-–]', v_str)[0].strip()
                if ch_str.isdigit() and v_clean.isdigit():
                    ref = f'{book_name} {ch_str}:{v_clean}'
                    if ref not in seen:
                        seen.add(ref)
                        refs.append(ref)
        else:
            # No colon: it's chapter only — skip (no verse to index)
            pass

    return refs


def extract_refs(xml, book_names):
    refs, seen = [], set()

    # Try OSIS osisRef= attributes first (zLD format)
    for m in OSIS_REF_RE.finditer(xml):
        for part in m.group(1).split():
            for tup in parse_osis_ref(part, book_names):
                r = format_ref(*tup, book_names)
                if r not in seen:
                    seen.add(r)
                    refs.append(r)

    # Try <scripRef> tags (rawld format used by Torrey)
    for m in SCRIP_REF_RE.finditer(xml):
        for r in _parse_scripref_content(m.group(1), book_names):
            if r not in seen:
                seen.add(r)
                refs.append(r)

    return refs


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--force', action='store_true')
    args = parser.parse_args()

    out_file = OUT_DIR / 'torrey.json'
    if out_file.exists() and not args.force:
        print(f'{out_file} exists — use --force to regenerate.')
        return

    book_names = load_book_names()
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    VIDX_DIR.mkdir(parents=True, exist_ok=True)

    print(f'Downloading {TORREY_URL} …')
    with urllib.request.urlopen(TORREY_URL) as resp:
        raw_zip = resp.read()
    print(f'  Downloaded {len(raw_zip):,} bytes')

    with zipfile.ZipFile(io.BytesIO(raw_zip)) as z:
        print('  Files:', z.namelist()[:12])
        base, is_zld = detect_module(z)
        print(f'  base={base}  is_zld={is_zld}')
        if base is None:
            print('ERROR: cannot detect module structure')
            return
        raw_entries = parse_zld(z, base) if is_zld else parse_rawld(z, base)

    print(f'  Parsed {len(raw_entries)} raw entries')

    topics, verse_index = [], {}
    for title, xml in raw_entries:
        # Title might be inside <title> tag or just the key
        tm = re.search(r'<title[^>]*>(.*?)</title>', xml, re.DOTALL)
        if tm:
            title = tm.group(1).strip()
        slug = slugify(title)
        if not slug: continue

        refs = extract_refs(xml, book_names)
        # Deduplicate
        seen, unique = set(), []
        for r in refs:
            if r not in seen:
                seen.add(r)
                unique.append(r)

        topics.append({'slug': slug, 'title': title, 'verses': unique})

        # Build verse-index
        for ref_str in unique:
            m = re.match(r'^(.+?)\s+(\d+)(?::(\d+))?', ref_str)
            if not m: continue
            book_name_str = m.group(1).strip()
            ch = m.group(2)
            v  = m.group(3)
            if not v: continue
            book_id = next((bid for bid, n in book_names.items() if n == book_name_str), None)
            if not book_id: continue
            key = f'{ch}:{v.split("-")[0]}'
            verse_index.setdefault(book_id, {}).setdefault(key, [])
            if slug not in verse_index[book_id][key]:
                verse_index[book_id][key].append(slug)

    with open(out_file, 'w') as f:
        json.dump(topics, f, separators=(',', ':'))
    print(f'  Wrote {out_file} ({out_file.stat().st_size:,} bytes, {len(topics)} topics)')

    for book_id, chv_map in verse_index.items():
        out_path = VIDX_DIR / f'{book_id}.json'
        with open(out_path, 'w') as f:
            json.dump(chv_map, f, separators=(',', ':'))
    print(f'  Wrote {len(verse_index)} verse-index files to {VIDX_DIR}/')
    print('Done.')


if __name__ == '__main__':
    main()
