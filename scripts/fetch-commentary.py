#!/usr/bin/env python3
"""
fetch-commentary.py — Download and install Matthew Henry Concise Commentary.

Source: CrossWire SWORD Project MHCom module (public domain)
Run from repo root:
  python3 scripts/fetch-commentary.py

Output: data/commentary/{bookId}.json
Format: {"chapter": {"startVerse": "<p>HTML text</p>", ...}}

Lookup note: MHC sections span ranges (e.g., "verses 14-21"). Each section
is stored under its *first* verse. In JS, search backwards from the target
verse to find the enclosing section.

Options:
  --force   Re-generate files even if they already exist
"""

import json, os, sys, io, struct, zlib, zipfile, urllib.request, argparse, re

REPO_ROOT  = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BOOKS_JSON = os.path.join(REPO_ROOT, 'data', 'bible', 'books.json')
BIBLE_DIR  = os.path.join(REPO_ROOT, 'data', 'bible', 'KJV')
OUT_DIR    = os.path.join(REPO_ROOT, 'data', 'commentary')

SOURCE_URLS = [
    'https://www.crosswire.org/ftpmirror/pub/sword/packages/rawzip/MHCC.zip',
    'http://ftp.crosswire.org/pub/sword/packages/rawzip/MHCC.zip',
]

# SWORD canonical book order — must match bookNumber in books.json (1-66)
OT_BOOK_IDS = [
    'genesis','exodus','leviticus','numbers','deuteronomy','joshua','judges',
    'ruth','1samuel','2samuel','1kings','2kings','1chronicles','2chronicles',
    'ezra','nehemiah','esther','job','psalms','proverbs','ecclesiastes',
    'songofsolomon','isaiah','jeremiah','lamentations','ezekiel','daniel',
    'hosea','joel','amos','obadiah','jonah','micah','nahum','habakkuk',
    'zephaniah','haggai','zechariah','malachi',
]
NT_BOOK_IDS = [
    'matthew','mark','luke','john','acts','romans','1corinthians',
    '2corinthians','galatians','ephesians','philippians','colossians',
    '1thessalonians','2thessalonians','1timothy','2timothy','titus',
    'philemon','hebrews','james','1peter','2peter','1john','2john',
    '3john','jude','revelation',
]


# ── Verse-count helpers ───────────────────────────────────────────────────────

def get_verse_counts(book_ids):
    """Return [[ch1_vcount, ch2_vcount, ...], ...] in book_ids order from KJV data."""
    result = []
    for bid in book_ids:
        path = os.path.join(BIBLE_DIR, bid + '.json')
        if not os.path.exists(path):
            result.append([1])
            continue
        with open(path) as f:
            data = json.load(f)
        chs = data.get('chapters', {})
        num_chs = max((int(k) for k in chs.keys()), default=1)
        counts = []
        for ch in range(1, num_chs + 1):
            ch_data = chs.get(str(ch), {})
            counts.append(max(len(ch_data), 1))
        result.append(counts)
    return result


def build_verse_list(book_ids, verse_counts):
    """
    Build [(book_idx, ch, v), ...] matching SWORD's bzv entry order exactly.
    Each testament file starts with 2 header entries, then for each book:
      (b, 0, 0) = book intro, then for each chapter:
        (b, ch, 0) = chapter intro, then (b, ch, 1)..(b, ch, N) = verses.
    v=0 and b_idx=-1 entries are skipped during populate.
    """
    entries = []
    entries.append((-1, 0, 0))   # module header (empty slot)
    entries.append((-1, 0, 1))   # importer metadata
    for b_idx, counts in enumerate(verse_counts):
        entries.append((b_idx, 0, 0))    # book intro
        for ch_idx, vc in enumerate(counts):
            entries.append((b_idx, ch_idx + 1, 0))  # chapter intro
            for v in range(1, vc + 1):
                entries.append((b_idx, ch_idx + 1, v))
    return entries


# ── SWORD zCom binary parser ──────────────────────────────────────────────────

def decompress_block(data):
    """Try zlib decompress; fall back to raw deflate."""
    try:
        return zlib.decompress(data)
    except zlib.error:
        try:
            return zlib.decompress(data, -15)
        except zlib.error:
            return b''


def read_zcom(bzv_data, bzs_data, bzz_data):
    """
    Parse SWORD zCom binary files.
    .bzv: 10 bytes/verse = [block_num(4LE), block_start(4LE), entry_size(2LE)]
    .bzs: 12 bytes/block = [offset_in_bzz(4LE), comp_size(4LE), uncomp_size(4LE)]
    .bzz: concatenated zlib-compressed blocks
    Returns list of str, one per verse in canonical order.
    """
    num_verses = len(bzv_data) // 10
    block_cache = {}
    result = []

    for i in range(num_verses):
        off = i * 10
        if off + 10 > len(bzv_data):
            result.append('')
            continue
        block_num, block_start, entry_size = struct.unpack_from('<IIH', bzv_data, off)

        if entry_size == 0:
            result.append('')
            continue

        if block_num not in block_cache:
            bs_off = block_num * 12
            if bs_off + 12 > len(bzs_data):
                result.append('')
                continue
            blk_offset, blk_comp, blk_uncomp = struct.unpack_from('<III', bzs_data, bs_off)
            compressed = bzz_data[blk_offset:blk_offset + blk_comp]
            block_cache[block_num] = decompress_block(compressed)

        block = block_cache[block_num]
        end = block_start + entry_size
        if end > len(block):
            result.append('')
            continue

        raw = block[block_start:end]
        try:
            result.append(raw.decode('utf-8'))
        except UnicodeDecodeError:
            result.append(raw.decode('latin-1', errors='replace'))

    return result


def read_rawcom(dat_data, idx_data, entry_size=6):
    """
    Parse SWORD rawCom binary files.
    .idx: entry_size bytes/verse = [start(4LE), length(2LE)] or [start(8LE), length(2LE)]
    .dat: concatenated verse text
    """
    if entry_size == 6:
        fmt, sz = '<IH', 6
    else:
        fmt, sz = '<QH', 10

    num_verses = len(idx_data) // sz
    result = []
    for i in range(num_verses):
        off = i * sz
        if off + sz > len(idx_data):
            result.append('')
            continue
        unpacked = struct.unpack_from(fmt, idx_data, off)
        start, length = unpacked
        if length == 0:
            result.append('')
            continue
        raw = dat_data[start:start + length]
        try:
            result.append(raw.decode('utf-8'))
        except UnicodeDecodeError:
            result.append(raw.decode('latin-1', errors='replace'))
    return result


# ── OSIS markup → clean HTML ─────────────────────────────────────────────────

def clean_osis(text):
    """
    Convert OSIS XML to simple display HTML.
    Extracts the <hi type="bold"> heading and prose text; strips structural
    markup (tables, chapter outlines, milestones).
    """
    if not text:
        return ''

    # Remove table elements entirely (chapter outlines like "Verses 1-21 / ...")
    text = re.sub(r'<table\b[^>]*>.*?</table>', ' ', text,
                  flags=re.DOTALL | re.IGNORECASE)
    # Remove title elements (e.g. <title type="x-s2">Chapter 3</title>)
    text = re.sub(r'<title\b[^>]*>.*?</title>', ' ', text,
                  flags=re.DOTALL | re.IGNORECASE)

    # Extract section heading from <hi type="bold">...</hi>
    heading = ''
    m = re.search(r'<hi\b[^>]*>(.*?)</hi>', text, re.DOTALL | re.IGNORECASE)
    if m:
        heading = m.group(1).strip()

    # Remove <hi> tag (already extracted)
    text = re.sub(r'<hi\b[^>]*>.*?</hi>', '', text,
                  flags=re.DOTALL | re.IGNORECASE)
    # Strip self-closing tags (milestones, chapter markers, etc.)
    text = re.sub(r'<[a-z][^>]*/>', ' ', text, flags=re.IGNORECASE)
    # Strip remaining tags
    text = re.sub(r'<[^>]+>', ' ', text)
    # Collapse whitespace
    text = re.sub(r'\s+', ' ', text).strip()

    if not text:
        return ''

    # Split into natural paragraphs on ". " boundaries to improve readability
    # (OSIS prose has no paragraph markers after tag removal)
    html = ''
    if heading:
        html += '<p class="mhcc-heading"><strong>' + heading + '</strong></p>'
    if text:
        html += '<p>' + text + '</p>'
    return html


# ── Module zip parser ─────────────────────────────────────────────────────────

def find_in_zip(zf, *suffixes):
    """Case-insensitive search for a file ending with any of the given suffixes."""
    names = zf.namelist()
    for suffix in suffixes:
        sl = suffix.lower()
        for n in names:
            if n.lower().endswith(sl):
                return n
    return None


def parse_zcom_module(zf, data_path, ot_vlist, nt_vlist):
    result = {}  # bookId -> {ch -> {v -> html}}

    for prefix, book_ids, verse_list in [
        ('ot', OT_BOOK_IDS, ot_vlist),
        ('nt', NT_BOOK_IDS, nt_vlist),
    ]:
        base = data_path + prefix
        bzv_name = find_in_zip(zf, base + '.bzv', prefix + '.bzv')
        bzs_name = find_in_zip(zf, base + '.bzs', prefix + '.bzs')
        bzz_name = find_in_zip(zf, base + '.bzz', prefix + '.bzz')

        if not all([bzv_name, bzs_name, bzz_name]):
            print(f'  WARNING: {prefix.upper()} index files not found — skipping')
            continue

        print(f'  Parsing {prefix.upper()} files…')
        bzv = zf.read(bzv_name)
        bzs = zf.read(bzs_name)
        bzz = zf.read(bzz_name)
        texts = read_zcom(bzv, bzs, bzz)

        _populate(result, texts, verse_list, book_ids)

    return result


def parse_rawcom_module(zf, data_path, ot_vlist, nt_vlist):
    result = {}
    all_book_ids = OT_BOOK_IDS + NT_BOOK_IDS
    all_vlists   = ot_vlist + nt_vlist  # concatenate for simplicity

    # rawCom stores one .dat/.idx per book; file names vary by module
    names_lower = {n.lower(): n for n in zf.namelist()}
    dp_lower    = data_path.lower()

    for bid in all_book_ids:
        # Try common abbreviations
        for abbrev in (bid, bid[:3], bid.replace('1', 'i').replace('2', 'ii')):
            dat_key = dp_lower + abbrev + '.dat'
            idx_key = dp_lower + abbrev + '.idx'
            if dat_key in names_lower and idx_key in names_lower:
                dat = zf.read(names_lower[dat_key])
                idx = zf.read(names_lower[idx_key])
                texts = read_rawcom(dat, idx)
                # For rawCom the texts are already per-book
                book_idx = (OT_BOOK_IDS + NT_BOOK_IDS).index(bid)
                all_vlist = ot_vlist + nt_vlist
                b_verse_list = [(0, ch, v) for (bi, ch, v) in all_vlist if bi == book_idx]
                _populate(result, texts, [(0, ch, v) for (_, ch, v) in b_verse_list], [bid])
                break

    return result


def _populate(result, texts, verse_list, book_ids):
    """
    Map text entries onto the result dict.
    Skips: header entries (b_idx=-1), intro entries (v=0 or ch=0).
    Deduplicates: MHCC stores the same section text for every verse in the range,
    so we only store it at the first verse of each section.
    """
    prev_raw = None
    for idx, (b_idx, ch, v) in enumerate(verse_list):
        if idx >= len(texts):
            break
        # Skip module header, book intro, chapter intro entries
        if b_idx < 0 or ch == 0 or v == 0:
            continue
        raw = texts[idx]
        if not raw or not raw.strip():
            prev_raw = None
            continue
        # Skip pure structural OSIS entries (no real commentary text)
        if not re.search(r'[A-Za-z]{10}', raw):
            continue
        # Deduplicate: skip if same text as previous non-empty entry
        if raw == prev_raw:
            continue
        prev_raw = raw
        book_id = book_ids[b_idx]
        html = clean_osis(raw)
        if not html:
            continue
        result.setdefault(book_id, {}).setdefault(str(ch), {})[str(v)] = html


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description='Fetch Matthew Henry Concise Commentary.')
    parser.add_argument('--force', action='store_true',
                        help='Re-generate files even if they exist')
    args = parser.parse_args()

    with open(BOOKS_JSON) as f:
        books_meta = json.load(f)

    # Build canonical verse lists from our KJV data
    ot_counts = get_verse_counts(OT_BOOK_IDS)
    nt_counts = get_verse_counts(NT_BOOK_IDS)
    ot_vlist  = build_verse_list(OT_BOOK_IDS, ot_counts)
    nt_vlist  = build_verse_list(NT_BOOK_IDS, nt_counts)

    print(f'Fetching MHCom SWORD module…')
    zip_bytes = None
    for url in SOURCE_URLS:
        try:
            print(f'  Trying {url}')
            with urllib.request.urlopen(url, timeout=90) as r:
                zip_bytes = r.read()
            print(f'  Downloaded {len(zip_bytes):,} bytes')
            break
        except Exception as e:
            print(f'  Failed: {e}')

    if not zip_bytes:
        print('ERROR: Could not download MHCom module from any source.')
        sys.exit(1)

    print('Parsing SWORD module…')
    with zipfile.ZipFile(io.BytesIO(zip_bytes)) as zf:
        # Read the conf file
        conf_name = find_in_zip(zf, 'mhcom.conf', '.conf')
        if not conf_name:
            print('ERROR: No .conf file in zip')
            sys.exit(1)
        conf_text = zf.read(conf_name).decode('utf-8', errors='replace')

        mod_drv   = ''
        data_path = ''
        for line in conf_text.splitlines():
            if '=' in line:
                k, _, v = line.partition('=')
                kl = k.strip().lower()
                if kl == 'moddrv':
                    mod_drv = v.strip()
                elif kl == 'datapath':
                    data_path = v.strip().lstrip('./').replace('\\', '/')
                    if not data_path.endswith('/'):
                        data_path += '/'

        print(f'  ModDrv   = {mod_drv}')
        print(f'  DataPath = {data_path}')

        drv_lower = mod_drv.lower()
        if drv_lower in ('zcom', 'zcom2'):
            commentary = parse_zcom_module(zf, data_path, ot_vlist, nt_vlist)
        elif drv_lower in ('rawcom', 'rawcom2'):
            commentary = parse_rawcom_module(zf, data_path, ot_vlist, nt_vlist)
        else:
            print(f'ERROR: Unknown ModDrv "{mod_drv}" — cannot parse.')
            sys.exit(1)

    total_entries = sum(
        len(vs) for bk in commentary.values() for vs in bk.values()
    )
    print(f'  Extracted {total_entries:,} commentary sections across '
          f'{len(commentary)} books')

    os.makedirs(OUT_DIR, exist_ok=True)
    written = skipped = 0

    for meta in books_meta:
        bid      = meta['id']
        out_file = os.path.join(OUT_DIR, bid + '.json')

        if os.path.exists(out_file) and not args.force:
            skipped += 1
            continue

        bk_data = commentary.get(bid, {})
        # Sort chapters and verses numerically
        sorted_data = {}
        for ch in sorted(bk_data.keys(), key=lambda x: int(x)):
            sorted_data[ch] = {}
            for v in sorted(bk_data[ch].keys(), key=lambda x: int(x)):
                sorted_data[ch][v] = bk_data[ch][v]

        with open(out_file, 'w', encoding='utf-8') as f:
            json.dump(sorted_data, f, ensure_ascii=False, separators=(',', ':'))

        n = sum(len(vs) for vs in sorted_data.values())
        if n:
            print(f'  {meta["name"]}: {n} sections')
        written += 1

    print(f'\nDone. Written: {written}  Skipped (exists): {skipped}')
    print(f'Output dir: {OUT_DIR}')


if __name__ == '__main__':
    main()
