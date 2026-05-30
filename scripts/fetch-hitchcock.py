#!/usr/bin/env python3
"""
fetch-hitchcock.py — Download Hitchcock's Bible Names Dictionary from CrossWire.

Source: https://www.crosswire.org/ftpmirror/pub/sword/packages/rawzip/HitchBD.zip
Format: zLD or rawld, simple key → meaning entries
Year:   1874 (public domain)

Output:
  data/hitchcock/index.json  — [{id, term, meaning}]  (all ~2,500 names in one file)

Usage:
  python3 scripts/fetch-hitchcock.py
  python3 scripts/fetch-hitchcock.py --force
"""

import io, json, re, struct, urllib.request, zipfile, zlib, argparse
from pathlib import Path

REPO_ROOT  = Path(__file__).parent.parent
OUT_FILE   = REPO_ROOT / 'data' / 'hitchcock' / 'index.json'
HITCH_URL  = 'https://www.crosswire.org/ftpmirror/pub/sword/packages/rawzip/Hitchcock.zip'
SOURCE     = "Hitchcock's Bible Names (Roswell Hitchcock, 1874)"

TAG_RE = re.compile(r'<[^>]+>')


def slugify(title):
    s = re.sub(r"[^\w\s-]", '', title.lower())
    return re.sub(r'[\s_]+', '-', s).strip('-') or None


def strip_xml(text):
    return re.sub(r'\s+', ' ', TAG_RE.sub('', text)).replace('\x00', '').strip()


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
    if not idx_files:
        return None, None
    base = idx_files[0][:-4]
    zdx  = base + '.zdx'
    is_zld = (zdx in names) if not moddrv else (moddrv.lower() == 'zld')
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


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--force', action='store_true')
    args = parser.parse_args()

    if OUT_FILE.exists() and not args.force:
        print(f'{OUT_FILE} exists — use --force to regenerate.')
        return

    OUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    print(f'Downloading {HITCH_URL} …')
    with urllib.request.urlopen(HITCH_URL) as resp:
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

    print(f'  Parsed {len(raw_entries)} entries')

    index = []
    for key, content in raw_entries:
        # Hitchcock entries are just plain text: "From Hebrew; [meaning]"
        # Strip any XML tags
        tm = re.search(r'<title[^>]*>(.*?)</title>', content, re.DOTALL)
        term = tm.group(1).strip() if tm else key

        # The meaning is the plain-text body (strip XML)
        meaning = strip_xml(content)
        # Remove title duplication
        if meaning.lower().startswith(term.lower()):
            meaning = meaning[len(term):].lstrip(' ,;—-').strip()

        slug = slugify(term)
        if not slug or not meaning:
            continue

        index.append({'id': slug, 'term': term, 'meaning': meaning})

    index.sort(key=lambda x: x['term'].lower())
    OUT_FILE.write_text(json.dumps(index, ensure_ascii=False, separators=(',', ':')), 'utf-8')
    print(f'  Wrote {len(index)} names → {OUT_FILE}  ({OUT_FILE.stat().st_size:,} bytes)')
    print('Done.')


if __name__ == '__main__':
    main()
