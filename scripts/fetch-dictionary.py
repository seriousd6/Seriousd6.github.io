#!/usr/bin/env python3
"""
fetch-dictionary.py — Download Easton's Bible Dictionary from CrossWire SWORD module.

Source: https://www.crosswire.org/ftpmirror/pub/sword/packages/rawzip/Easton.zip
Format: zLD (compressed Lexical Dictionary), entryFree XML content
Year:   1897 (public domain)

Output:
  data/dictionary/index.json      — all entries [{id, term, brief}]
  data/dictionary/{slug}.json     — full entry per term {id, term, html, refs, source}

Usage:
  python3 scripts/fetch-dictionary.py
  python3 scripts/fetch-dictionary.py --force   # re-generate even if index exists
"""

import io, json, re, struct, urllib.request, zipfile, zlib, argparse
from pathlib import Path

REPO_ROOT  = Path(__file__).parent.parent
BOOKS_JSON = REPO_ROOT / 'data' / 'bible' / 'books.json'
OUT_DIR    = REPO_ROOT / 'data' / 'dictionary'
EASTON_URL = 'https://www.crosswire.org/ftpmirror/pub/sword/packages/rawzip/Easton.zip'
SOURCE     = "Easton's Bible Dictionary (M.G. Easton, 1897)"

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
    return s or None


def osis_to_ref(osis_str, book_names):
    """'Bible:Rev.1.8' → 'Revelation 1:8';  'Gen.15' → 'Genesis 15'."""
    s = osis_str.strip()
    if s.startswith('Bible:'):
        s = s[6:]
    s = s.split('-')[0]   # ranges like Gen.1.27-Gen.2.5 → use start only
    parts = s.split('.')
    book_id = OSIS_BOOKS.get(parts[0])
    if not book_id:
        return None
    name = book_names.get(book_id, book_id)
    if len(parts) == 1:
        return name
    ch = parts[1]
    if len(parts) == 2:
        return f'{name} {ch}'
    v = parts[2]
    return f'{name} {ch}:{v}'


REF_RE     = re.compile(r'<ref\s+osisRef="([^"]*)"[^>]*>(.*?)</ref>', re.DOTALL)
FOREIGN_RE = re.compile(r'<foreign[^>]*>(.*?)</foreign>', re.DOTALL)
NOTE_RE    = re.compile(r'<note[^>]*>.*?</note>', re.DOTALL)
TAG_RE     = re.compile(r'<[^>]+>')
KEEP_TAGS  = re.compile(r'^</?(?:p|em|b|i|a|blockquote|ul|ol|li|br)[\s/>]')


def xml_to_html(xml, book_names):
    """Convert entryFree XML to clean HTML with .ref anchor links."""
    xml = re.sub(r'<entryFree[^>]*>|</entryFree>', '', xml)
    xml = re.sub(r'<title[^>]*>.*?</title>', '', xml, flags=re.DOTALL)
    xml = NOTE_RE.sub('', xml)
    xml = FOREIGN_RE.sub(r'<em>\1</em>', xml)

    def replace_ref(m):
        osis_ref = m.group(1).split()[0]   # take first if space-separated
        text     = TAG_RE.sub('', m.group(2)).strip()
        canonical = osis_to_ref(osis_ref, book_names)
        if canonical:
            return f'<a class="ref" data-ref="{canonical}">{text}</a>'
        return text

    xml = REF_RE.sub(replace_ref, xml)

    def keep_or_strip(m):
        return m.group(0) if KEEP_TAGS.match(m.group(0)) else ''

    xml = re.sub(r'<[^>]+>', keep_or_strip, xml)
    xml = re.sub(r'\n{3,}', '\n\n', xml).strip()
    return xml


def xml_to_brief(xml):
    """Extract plain-text summary (~160 chars)."""
    text = TAG_RE.sub('', xml)
    text = re.sub(r'\s+', ' ', text).strip()
    if len(text) > 160:
        text = text[:160].rsplit(' ', 1)[0] + '…'
    return text


def parse_sword_zld(z, module_name):
    """Read a SWORD zLD module from an open ZipFile. Returns [(key, xml_content)]."""
    base = f'modules/lexdict/zld/{module_name}/'
    idx_data = z.read(base + f'{module_name}.idx')
    dat_data = z.read(base + f'{module_name}.dat')
    zdx_data = z.read(base + f'{module_name}.zdx')
    zdt_data = z.read(base + f'{module_name}.zdt')

    blocks = []
    for i in range(0, len(zdx_data), 8):
        off, sz = struct.unpack_from('<II', zdx_data, i)
        blocks.append((off, sz))

    decompressed = {}
    for bn, (off, sz) in enumerate(blocks):
        try:
            raw  = zlib.decompress(zdt_data[off:off + sz])
            numE = struct.unpack_from('<I', raw, 0)[0]
            entries = []
            for ei in range(numE):
                eOff, eSz = struct.unpack_from('<II', raw, 4 + ei * 8)
                entries.append(raw[eOff:eOff + eSz].decode('utf-8', 'replace'))
            decompressed[bn] = entries
        except Exception:
            decompressed[bn] = []

    results = []
    for i in range(0, len(idx_data), 8):
        off, sz = struct.unpack_from('<II', idx_data, i)
        chunk = dat_data[off:off + sz]
        nl = chunk.find(b'\r\n')
        if nl < 0:
            continue
        key = chunk[:nl].decode('utf-8', 'replace').strip()
        if len(chunk) < nl + 10:
            continue
        block_num      = struct.unpack_from('<I', chunk, nl + 2)[0]
        entry_in_block = struct.unpack_from('<I', chunk, nl + 6)[0]
        block_entries  = decompressed.get(block_num, [])
        if entry_in_block < len(block_entries):
            results.append((key, block_entries[entry_in_block]))
    return results


def extract_refs(xml, book_names):
    refs, seen = [], set()
    for m in re.finditer(r'osisRef="([^"]+)"', xml):
        for part in m.group(1).split():
            r = osis_to_ref(part, book_names)
            if r and r not in seen:
                seen.add(r)
                refs.append(r)
    return refs


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--force', action='store_true',
                        help='Re-generate even if index.json already exists')
    args = parser.parse_args()

    idx_path = OUT_DIR / 'index.json'
    if idx_path.exists() and not args.force:
        print(f'{idx_path} already exists — use --force to regenerate.')
        return

    book_names = load_book_names()
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    print(f'Downloading {EASTON_URL} …')
    with urllib.request.urlopen(EASTON_URL) as resp:
        raw_zip = resp.read()
    print(f'  Downloaded {len(raw_zip):,} bytes')

    with zipfile.ZipFile(io.BytesIO(raw_zip)) as z:
        raw_entries = parse_sword_zld(z, 'easton')
    print(f'  Parsed {len(raw_entries)} raw entries')

    index   = []
    written = 0
    skipped = 0

    for key, xml in raw_entries:
        tm   = re.search(r'<title[^>]*>(.*?)</title>', xml, re.DOTALL)
        term = tm.group(1).strip() if tm else key.title()
        slug = slugify(term)
        if not slug:
            skipped += 1
            continue

        html  = xml_to_html(xml, book_names)
        brief = xml_to_brief(xml)
        refs  = extract_refs(xml, book_names)

        entry = {
            'id':     slug,
            'term':   term,
            'source': SOURCE,
            'html':   html,
            'refs':   refs,
        }
        (OUT_DIR / f'{slug}.json').write_text(
            json.dumps(entry, ensure_ascii=False, separators=(',', ':')), 'utf-8'
        )
        written += 1
        index.append({'id': slug, 'term': term, 'brief': brief})

    index.sort(key=lambda x: x['term'].lower())
    idx_path.write_text(
        json.dumps(index, ensure_ascii=False, separators=(',', ':')), 'utf-8'
    )

    print(f'  Written:  {written} entry files  ({skipped} skipped)')
    idx_size = idx_path.stat().st_size
    print(f'  index.json: {idx_size:,} bytes  ({len(index)} entries)')
    print('Done.')


if __name__ == '__main__':
    main()
