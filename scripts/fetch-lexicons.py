#!/usr/bin/env python3
"""
fetch-lexicons.py — Download enhanced Hebrew and Greek lexicon data.

Sources:
  Hebrew : openscriptures/HebrewLexicon HebrewStrong.xml — keyed by H-number
  Greek  : CrossWire StrongsGreek.zip (zLD, Thayer content) — keyed by G-number

Output:
  data/strongs/bdb.json    — {H1: {lemma, translit, short_def, long_def}, …}
  data/strongs/thayer.json — {G1: {lemma, translit, pronounce, short_def, long_def}, …}

Usage:
  python3 scripts/fetch-lexicons.py
  python3 scripts/fetch-lexicons.py --force
"""

import io, json, re, struct, urllib.request, zipfile, zlib, argparse
from pathlib import Path
import xml.etree.ElementTree as ET

REPO_ROOT  = Path(__file__).parent.parent
OUT_DIR    = REPO_ROOT / 'data' / 'strongs'

BDB_URL    = 'https://raw.githubusercontent.com/openscriptures/HebrewLexicon/master/HebrewStrong.xml'
GREEK_URL  = 'https://www.crosswire.org/ftpmirror/pub/sword/packages/rawzip/StrongsGreek.zip'

TAG_RE = re.compile(r'<[^>]+>')


def fetch_bytes(url, timeout=90):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'bsw-fetch/1.0'})
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.read()
    except Exception as e:
        print(f'  ERROR fetching {url}: {e}')
        return None


def strip_xml(text):
    return re.sub(r'\s+', ' ', TAG_RE.sub('', text)).strip()


# ── BDB Hebrew (HebrewStrong.xml) ─────────────────────────────────────────────
#
# Format per entry:
#   <entry id="H1">
#     <w pos="n-m" pron="awb" xlit="ʼâb" xml:lang="heb">אָב</w>
#     <source>a primitive word;</source>
#     <meaning><def>father</def>, in a literal and remote application</meaning>
#     <usage>chief, (fore-) father(-less)...</usage>
#   </entry>

def parse_bdb_xml(xml_bytes):
    """Parse HebrewStrong.xml → {H1: {lemma, translit, short_def, long_def}}"""
    out = {}

    text = xml_bytes.decode('utf-8', errors='replace')
    # Strip namespace declarations and any xsi: attributes so ET can parse bare tag names
    text = re.sub(r'\s+xmlns(?::[^=]+)?="[^"]+"', '', text)
    text = re.sub(r'\s+xsi:\w+="[^"]*"', '', text)

    try:
        root = ET.fromstring(text)
    except ET.ParseError as e:
        print(f'  ERROR parsing BDB XML: {e}')
        return out

    for entry in root.findall('entry'):
        eid = entry.get('id', '')
        if not eid.startswith('H'):
            continue
        # Normalize: H001 → H1
        key = 'H' + (eid[1:].lstrip('0') or '0')

        # <w> element carries lemma (text) and translit (xlit attr)
        w_el = entry.find('w')
        lemma    = (w_el.text or '').strip() if w_el is not None else ''
        translit = (w_el.get('xlit') or w_el.get('pron') or '').strip() if w_el is not None else ''

        # <meaning> — may contain nested <def> tags
        meaning_el = entry.find('meaning')
        long_def   = ''
        short_def  = ''
        if meaning_el is not None:
            # Extract the <def> text as the bold/primary gloss
            def_el = meaning_el.find('def')
            if def_el is not None:
                short_def = (def_el.text or '').strip()
            # Full meaning text (all text inside <meaning>)
            long_def = ''.join(meaning_el.itertext()).strip()

        # <usage> — KJV usage / translation equivalents
        usage_el = entry.find('usage')
        usage = ''
        if usage_el is not None:
            usage = ''.join(usage_el.itertext()).strip()

        # <source> — etymology / derivation
        src_el = entry.find('source')
        source = ''
        if src_el is not None:
            source = ''.join(src_el.itertext()).strip()

        if not short_def and long_def:
            short_def = long_def[:180].rsplit(' ', 1)[0] + ('…' if len(long_def) > 180 else '')

        full = '; '.join(x for x in [long_def, usage] if x)
        if not full:
            full = source

        out[key] = {
            'lemma':     lemma,
            'translit':  translit,
            'short_def': short_def,
            'long_def':  full,
        }

    return out


# ── Thayer Greek (CrossWire StrongsGreek zLD) ─────────────────────────────────
#
# Keys: zero-padded 5-digit strings ('00001', '00025', etc.) → G1, G25
# Entry XML:
#   <entryFree n="1">
#     <orth>ἄλφα</orth>                           ← Greek lemma
#     <orth type="writing">a[lfa</orth>            ← beta-code
#     <orth rend="bold" type="trans">a</orth>      ← transliteration
#     <pron rend="italic">{al'-fah}</pron>         ← pronunciation
#     <def>...definition text...</def>
#   </entryFree>

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


ORTH_RE       = re.compile(r'<orth([^>]*)>(.*?)</orth>', re.DOTALL)
PRON_RE       = re.compile(r'<pron[^>]*>\{?([^}<{]+?)\}?</pron>', re.DOTALL)
DEF_INNER_RE  = re.compile(r'<def[^>]*>(.*?)</def>', re.DOTALL | re.IGNORECASE)


def parse_thayer_entries(raw_entries):
    """Convert CrossWire StrongsGreek zLD entries to {G1: {...}}."""
    out = {}
    for key, xml in raw_entries:
        # Key is like '00001' → G1
        num_str = key.lstrip('0') or '0'
        try:
            int(num_str)
        except ValueError:
            continue
        gkey = 'G' + num_str

        lemma, translit, pronounce = '', '', ''
        for m in ORTH_RE.finditer(xml):
            attrs = m.group(1)
            text  = strip_xml(m.group(2)).strip()
            if not attrs.strip():
                # First bare <orth> = Greek lemma
                if not lemma:
                    lemma = text
            elif 'type="trans"' in attrs and 'bold' in attrs:
                translit = text
            # Skip type="writing" (beta-code)

        pm = PRON_RE.search(xml)
        if pm:
            pronounce = pm.group(1).strip().strip('{}')

        dm = DEF_INNER_RE.search(xml)
        full_def = strip_xml(dm.group(1)).strip() if dm else strip_xml(xml)

        short_def = full_def[:200].rsplit(' ', 1)[0] + ('…' if len(full_def) > 200 else '')

        if gkey and (lemma or full_def):
            out[gkey] = {
                'lemma':     lemma,
                'translit':  translit,
                'pronounce': pronounce,
                'short_def': short_def,
                'long_def':  full_def,
            }

    return out


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--force', action='store_true')
    args = parser.parse_args()

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    # ── BDB Hebrew ────────────────────────────────────────────────────────────
    bdb_out = OUT_DIR / 'bdb.json'
    if bdb_out.exists() and not args.force:
        print(f'{bdb_out} exists — use --force to regenerate.')
    else:
        print(f'Downloading HebrewStrong.xml from openscriptures …')
        xml_bytes = fetch_bytes(BDB_URL)
        if xml_bytes:
            print(f'  Downloaded {len(xml_bytes):,} bytes')
            bdb = parse_bdb_xml(xml_bytes)
            if bdb:
                bdb_out.write_text(
                    json.dumps(bdb, ensure_ascii=False, separators=(',', ':')), 'utf-8'
                )
                print(f'  Wrote {len(bdb)} Hebrew entries → {bdb_out} ({bdb_out.stat().st_size:,} bytes)')
            else:
                print('  ERROR: No entries parsed from HebrewStrong.xml')
        else:
            print('  ERROR: Could not download HebrewStrong.xml')

    # ── Thayer's Greek ────────────────────────────────────────────────────────
    thayer_out = OUT_DIR / 'thayer.json'
    if thayer_out.exists() and not args.force:
        print(f'{thayer_out} exists — use --force to regenerate.')
    else:
        print(f'Downloading StrongsGreek.zip from CrossWire …')
        zip_bytes = fetch_bytes(GREEK_URL)
        if zip_bytes:
            print(f'  Downloaded {len(zip_bytes):,} bytes')
            try:
                with zipfile.ZipFile(io.BytesIO(zip_bytes)) as z:
                    print('  Files:', z.namelist()[:8])
                    base, is_zld = detect_module(z)
                    print(f'  base={base}  is_zld={is_zld}')
                    if base is None:
                        print('  ERROR: cannot detect module structure')
                    else:
                        raw = parse_zld(z, base) if is_zld else []
                        print(f'  Parsed {len(raw)} raw entries')
                        thayer = parse_thayer_entries(raw)
                        print(f'  Resolved {len(thayer)} G-number entries')
                        if thayer:
                            thayer_out.write_text(
                                json.dumps(thayer, ensure_ascii=False, separators=(',', ':')), 'utf-8'
                            )
                            print(f'  Wrote {len(thayer)} Thayer entries → {thayer_out} ({thayer_out.stat().st_size:,} bytes)')
                        else:
                            print('  ERROR: No Thayer entries resolved')
            except Exception as e:
                print(f'  ERROR processing StrongsGreek.zip: {e}')
        else:
            print('  ERROR: Could not download StrongsGreek.zip')

    print('Done.')


if __name__ == '__main__':
    main()
