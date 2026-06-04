#!/usr/bin/env python3
"""
fetch-more-commentaries.py — Download additional public-domain SWORD commentaries.

Commentaries fetched:
  Barnes' Notes on the Bible         → data/commentary/barnes/{bookId}.json
  Jamieson-Fausset-Brown             → data/commentary/jfb/{bookId}.json
  Adam Clarke's Commentary           → data/commentary/clarke/{bookId}.json
  Calvin's Collected Commentaries    → data/commentary/calvin/{bookId}.json
  Robertson's Word Pictures (NT)     → data/commentary/rwp/{bookId}.json
  Wesley's Notes                     → data/commentary/wesley/{bookId}.json

All modules are from the CrossWire SWORD Project (public domain).
Data shape: {"chapter": {"startVerse": "<p>HTML text</p>", ...}}
            Same as existing Matthew Henry data.

Usage:
  python3 scripts/fetch-more-commentaries.py [--force] [--only barnes,jfb]
"""

import argparse, io, json, os, re, struct, sys, urllib.request, zipfile

REPO_ROOT  = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BOOKS_JSON = os.path.join(REPO_ROOT, 'data', 'bible', 'books.json')
BIBLE_DIR  = os.path.join(REPO_ROOT, 'data', 'bible', 'KJV')
COMM_ROOT  = os.path.join(REPO_ROOT, 'data', 'commentary')

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

# Module definitions — CrossWire FTP primary + fallback mirror
MODULES = [
    {
        'id': 'barnes',
        'label': "Barnes' Notes on the Bible",
        'nt_only': True,           # CrossWire module only has NT
        'czv_ext': True,           # uses .czv/.czs/.czz instead of .bzv/.bzs/.bzz
        'urls': [
            'https://www.crosswire.org/ftpmirror/pub/sword/packages/rawzip/Barnes.zip',
            'http://ftp.crosswire.org/pub/sword/packages/rawzip/Barnes.zip',
        ],
    },
    {
        'id': 'jfb',
        'label': 'Jamieson-Fausset-Brown Commentary',
        'urls': [
            'https://www.crosswire.org/ftpmirror/pub/sword/packages/rawzip/JFB.zip',
            'http://ftp.crosswire.org/pub/sword/packages/rawzip/JFB.zip',
        ],
    },
    {
        'id': 'clarke',
        'label': "Adam Clarke's Commentary",
        'urls': [
            'https://www.crosswire.org/ftpmirror/pub/sword/packages/rawzip/Clarke.zip',
            'http://ftp.crosswire.org/pub/sword/packages/rawzip/Clarke.zip',
        ],
    },
    {
        'id': 'calvin',
        'label': "Calvin's Collected Commentaries",
        'urls': [
            'https://www.crosswire.org/ftpmirror/pub/sword/packages/rawzip/CalvinCommentaries.zip',
            'http://ftp.crosswire.org/pub/sword/packages/rawzip/CalvinCommentaries.zip',
        ],
    },
    {
        'id': 'rwp',
        'label': "Robertson's Word Pictures",
        'nt_only': True,
        'urls': [
            'https://www.crosswire.org/ftpmirror/pub/sword/packages/rawzip/RWP.zip',
            'http://ftp.crosswire.org/pub/sword/packages/rawzip/RWP.zip',
        ],
    },
    {
        'id': 'wesley',
        'label': "Wesley's Notes",
        'urls': [
            'https://www.crosswire.org/ftpmirror/pub/sword/packages/rawzip/Wesley.zip',
            'http://ftp.crosswire.org/pub/sword/packages/rawzip/Wesley.zip',
        ],
    },
    {
        'id': 'gill',
        'label': "Gill's Exposition of the Entire Bible",
        'urls': [
            'https://www.crosswire.org/ftpmirror/pub/sword/packages/rawzip/Gill.zip',
            'http://ftp.crosswire.org/pub/sword/packages/rawzip/Gill.zip',
        ],
    },
]


# ── Verse-count helpers ────────────────────────────────────────────────────────

def get_verse_counts(book_ids):
    result = []
    for bid in book_ids:
        path = os.path.join(BIBLE_DIR, bid + '.json')
        if not os.path.exists(path):
            result.append([1]); continue
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
    entries = [(-1, 0, 0), (-1, 0, 1)]
    for b_idx, counts in enumerate(verse_counts):
        entries.append((b_idx, 0, 0))
        for ch_idx, vc in enumerate(counts):
            entries.append((b_idx, ch_idx + 1, 0))
            for v in range(1, vc + 1):
                entries.append((b_idx, ch_idx + 1, v))
    return entries


# ── SWORD binary parsers ───────────────────────────────────────────────────────

def decompress_block(data):
    import zlib
    try:
        return zlib.decompress(data)
    except zlib.error:
        try:
            return zlib.decompress(data, -15)
        except zlib.error:
            return b''


def read_zcom(bzv_data, bzs_data, bzz_data):
    num_verses = len(bzv_data) // 10
    block_cache = {}
    result = []
    for i in range(num_verses):
        off = i * 10
        if off + 10 > len(bzv_data):
            result.append(''); continue
        block_num, block_start, entry_size = struct.unpack_from('<IIH', bzv_data, off)
        if entry_size == 0:
            result.append(''); continue
        if block_num not in block_cache:
            bs_off = block_num * 12
            if bs_off + 12 > len(bzs_data):
                result.append(''); continue
            blk_offset, blk_comp, _ = struct.unpack_from('<III', bzs_data, bs_off)
            block_cache[block_num] = decompress_block(bzz_data[blk_offset:blk_offset + blk_comp])
        block = block_cache[block_num]
        end = block_start + entry_size
        if end > len(block):
            result.append(''); continue
        raw = block[block_start:end]
        try:
            result.append(raw.decode('utf-8'))
        except UnicodeDecodeError:
            result.append(raw.decode('latin-1', errors='replace'))
    return result


def read_rawcom(dat_data, idx_data, entry_size=6):
    fmt, sz = ('<IH', 6) if entry_size == 6 else ('<QH', 10)
    num_verses = len(idx_data) // sz
    result = []
    for i in range(num_verses):
        off = i * sz
        if off + sz > len(idx_data):
            result.append(''); continue
        start, length = struct.unpack_from(fmt, idx_data, off)
        if length == 0:
            result.append(''); continue
        raw = dat_data[start:start + length]
        try:
            result.append(raw.decode('utf-8'))
        except UnicodeDecodeError:
            result.append(raw.decode('latin-1', errors='replace'))
    return result


# ── OSIS → HTML ───────────────────────────────────────────────────────────────

def clean_osis(text):
    if not text or not text.strip():
        return ''

    # Remove tables (chapter outlines), title elements
    text = re.sub(r'<table\b[^>]*>.*?</table>', ' ', text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r'<title\b[^>]*>.*?</title>', ' ', text, flags=re.DOTALL | re.IGNORECASE)

    # Extract bold heading
    heading = ''
    m = re.search(r'<hi\b[^>]*type=["\']bold["\'][^>]*>(.*?)</hi>', text, re.DOTALL | re.IGNORECASE)
    if not m:
        m = re.search(r'<hi\b[^>]*>(.*?)</hi>', text, re.DOTALL | re.IGNORECASE)
    if m:
        heading = re.sub(r'<[^>]+>', ' ', m.group(1)).strip()

    # Strip OSIS markup
    text = re.sub(r'<hi\b[^>]*>.*?</hi>', '', text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r'<[a-z][^>]*/>', ' ', text, flags=re.IGNORECASE)  # self-closing
    text = re.sub(r'<[^>]+>', ' ', text)
    text = re.sub(r'&amp;', '&', text)
    text = re.sub(r'&lt;', '<', text)
    text = re.sub(r'&gt;', '>', text)
    text = re.sub(r'&nbsp;', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()

    if not text and not heading:
        return ''

    html = ''
    if heading:
        html += '<p class="comm-heading"><strong>' + heading + '</strong></p>'
    if text:
        # Split on sentence endings to create readable paragraphs
        parts = re.split(r'(?<=[.!?])\s{2,}', text)
        if len(parts) == 1:
            html += '<p>' + text + '</p>'
        else:
            html += ''.join('<p>' + p.strip() + '</p>' for p in parts if p.strip())
    return html


# ── Zip helpers ───────────────────────────────────────────────────────────────

def find_in_zip(zf, *suffixes):
    names = zf.namelist()
    for suffix in suffixes:
        sl = suffix.lower()
        for n in names:
            if n.lower().endswith(sl):
                return n
    return None


# ── Module parsers ────────────────────────────────────────────────────────────

def populate(result, texts, verse_list, book_ids):
    prev_raw = None
    for idx, (b_idx, ch, v) in enumerate(verse_list):
        if idx >= len(texts):
            break
        if b_idx < 0 or ch == 0 or v == 0:
            continue
        raw = texts[idx]
        if not raw or not raw.strip():
            prev_raw = None; continue
        if not re.search(r'[A-Za-z]{8}', raw):
            continue
        if raw == prev_raw:
            continue
        prev_raw = raw
        book_id = book_ids[b_idx]
        html = clean_osis(raw)
        if not html:
            continue
        result.setdefault(book_id, {}).setdefault(str(ch), {})[str(v)] = html


def parse_zcom_module(zf, data_path, ot_vlist, nt_vlist, nt_only=False, czv_ext=False):
    result = {}
    scope = [('nt', NT_BOOK_IDS, nt_vlist)] if nt_only else [
        ('ot', OT_BOOK_IDS, ot_vlist), ('nt', NT_BOOK_IDS, nt_vlist)
    ]
    # Some modules use .czv/.czs/.czz; others use .bzv/.bzs/.bzz
    ext_pairs = [('.czv', '.czs', '.czz'), ('.bzv', '.bzs', '.bzz')] if czv_ext else \
                [('.bzv', '.bzs', '.bzz'), ('.czv', '.czs', '.czz')]
    for prefix, book_ids, verse_list in scope:
        base = data_path + prefix
        bzv = bzs = bzz = None
        for ve, se, ze in ext_pairs:
            bzv = find_in_zip(zf, base + ve, prefix + ve)
            bzs = find_in_zip(zf, base + se, prefix + se)
            bzz = find_in_zip(zf, base + ze, prefix + ze)
            if all([bzv, bzs, bzz]):
                break
        if not all([bzv, bzs, bzz]):
            print(f'  WARNING: {prefix.upper()} index files not found — skipping')
            continue
        print(f'  Parsing {prefix.upper()} files…')
        texts = read_zcom(zf.read(bzv), zf.read(bzs), zf.read(bzz))
        populate(result, texts, verse_list, book_ids)
    return result


def parse_rawcom_module(zf, data_path, ot_vlist, nt_vlist, nt_only=False):
    result = {}
    scope = NT_BOOK_IDS if nt_only else (OT_BOOK_IDS + NT_BOOK_IDS)
    scope_vlist = nt_vlist if nt_only else (ot_vlist + nt_vlist)
    names_lower = {n.lower(): n for n in zf.namelist()}
    dp_lower = data_path.lower()

    for bid in scope:
        for abbrev in (bid, bid[:3], bid.replace('1', 'i').replace('2', 'ii').replace('3', 'iii')):
            dat_key = dp_lower + abbrev + '.dat'
            idx_key = dp_lower + abbrev + '.idx'
            if dat_key in names_lower and idx_key in names_lower:
                dat = zf.read(names_lower[dat_key])
                idx = zf.read(names_lower[idx_key])
                texts = read_rawcom(dat, idx)
                book_idx = scope.index(bid)
                b_verses = [(0, ch, v) for (bi, ch, v) in scope_vlist if bi == book_idx]
                populate(result, texts, b_verses, [bid])
                break
    return result


# ── Download helper ───────────────────────────────────────────────────────────

def download(urls, label):
    for url in urls:
        try:
            print(f'  Trying {url}')
            req = urllib.request.Request(url, headers={'User-Agent': 'bsw-fetch/1.0'})
            with urllib.request.urlopen(req, timeout=120) as r:
                data = r.read()
            print(f'  Downloaded {len(data):,} bytes')
            return data
        except Exception as e:
            print(f'  Failed: {e}')
    return None


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description='Fetch additional public-domain SWORD commentaries.')
    parser.add_argument('--force', action='store_true', help='Re-generate existing files')
    parser.add_argument('--only', help='Comma-separated list of module IDs to fetch (e.g. barnes,jfb)')
    args = parser.parse_args()

    only = set(x.strip() for x in args.only.split(',')) if args.only else None

    with open(BOOKS_JSON) as f:
        books_meta = json.load(f)

    ot_counts = get_verse_counts(OT_BOOK_IDS)
    nt_counts = get_verse_counts(NT_BOOK_IDS)
    ot_vlist  = build_verse_list(OT_BOOK_IDS, ot_counts)
    nt_vlist  = build_verse_list(NT_BOOK_IDS, nt_counts)

    for mod in MODULES:
        mid = mod['id']
        if only and mid not in only:
            continue

        print(f'\n══ {mod["label"]} ({mid}) ══')

        out_dir = os.path.join(COMM_ROOT, mid)

        # Check if already done (unless --force)
        if not args.force:
            done = sum(1 for bk in books_meta
                       if os.path.exists(os.path.join(out_dir, bk['id'] + '.json')))
            if done >= 60:
                print(f'  {done} book files exist — skipping (--force to re-fetch)')
                continue

        zip_bytes = download(mod['urls'], mod['label'])
        if not zip_bytes:
            print(f'  ERROR: Could not download {mid}')
            continue

        print('  Parsing SWORD module…')
        with zipfile.ZipFile(io.BytesIO(zip_bytes)) as zf:
            conf_name = find_in_zip(zf, mod['id'] + '.conf', '.conf')
            if not conf_name:
                print('  ERROR: No .conf file in zip')
                continue

            conf = zf.read(conf_name).decode('utf-8', errors='replace')
            mod_drv = data_path = ''
            for line in conf.splitlines():
                if '=' in line:
                    k, _, v = line.partition('=')
                    kl = k.strip().lower()
                    if kl == 'moddrv':
                        mod_drv = v.strip()
                    elif kl == 'datapath':
                        data_path = v.strip().lstrip('./').replace('\\', '/')
                        if not data_path.endswith('/'):
                            data_path += '/'

            print(f'  ModDrv={mod_drv}  DataPath={data_path}')
            nt_only  = mod.get('nt_only', False)
            czv_ext  = mod.get('czv_ext', False)
            drv_lower = mod_drv.lower()
            # zCom, zCom2, zCom3, zCom4 all use the same binary format
            if re.match(r'^zcom\d*$', drv_lower):
                commentary = parse_zcom_module(zf, data_path, ot_vlist, nt_vlist, nt_only, czv_ext)
            elif re.match(r'^rawcom\d*$', drv_lower):
                commentary = parse_rawcom_module(zf, data_path, ot_vlist, nt_vlist, nt_only)
            else:
                print(f'  ERROR: Unknown ModDrv "{mod_drv}"')
                continue

        total = sum(len(vs) for bk in commentary.values() for vs in bk.values())
        print(f'  Extracted {total:,} sections across {len(commentary)} books')

        os.makedirs(out_dir, exist_ok=True)
        written = skipped = 0

        for meta in books_meta:
            bid = meta['id']
            out_file = os.path.join(out_dir, bid + '.json')

            if os.path.exists(out_file) and not args.force:
                skipped += 1; continue

            bk_data = commentary.get(bid, {})
            sorted_data = {}
            for ch in sorted(bk_data.keys(), key=lambda x: int(x)):
                sorted_data[ch] = {}
                for v in sorted(bk_data[ch].keys(), key=lambda x: int(x)):
                    sorted_data[ch][v] = bk_data[ch][v]

            with open(out_file, 'w', encoding='utf-8') as f:
                json.dump(sorted_data, f, ensure_ascii=False, separators=(',', ':'))

            n = sum(len(vs) for vs in sorted_data.values())
            if n:
                print(f'    {meta["name"]}: {n} sections')
            written += 1

        print(f'  Done. Written: {written}  Skipped: {skipped}  → {out_dir}')

    print('\nAll done.')


if __name__ == '__main__':
    main()
