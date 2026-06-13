#!/usr/bin/env python3
"""
Fix encoding artifacts in commentary JSON files.

Three artifact types found:
1. â + C1 control chars (UTF-8 smart-quotes decoded as Latin-1) — fixed by re-encoding
2. Î/Ï + Latin-1/C1 sequences (UTF-8 Greek text decoded as Latin-1) — fixed by re-encoding
3. Standalone C1 control chars from CP850 origin (degree, pound, umlauts, etc.)
"""
import re, os, glob

COMMENTARY_DIR = os.path.join(os.path.dirname(__file__), '..', 'data', 'commentary')

# CP850 byte → Unicode for the 0x80–0x9F range
CP850_MAP = {
    '\x80': 'Ç', '\x81': 'ü', '\x82': 'é', '\x83': 'â',
    '\x84': 'ä', '\x85': 'à', '\x86': 'å', '\x87': 'ç',
    '\x88': 'ê', '\x89': 'ë', '\x8a': 'è', '\x8b': 'ï',
    '\x8c': 'î', '\x8d': 'ì', '\x8e': 'Ä', '\x8f': 'Å',
    '\x90': 'É', '\x91': 'æ', '\x92': 'Æ', '\x93': 'ô',
    '\x94': 'ö', '\x95': 'ò', '\x96': 'û', '\x97': 'ù',
    '\x98': 'ÿ', '\x99': 'Ö', '\x9a': 'Ü', '\x9b': 'ø',
    '\x9c': '£', '\x9d': 'Ø', '\x9e': '×', '\x9f': 'ƒ',
}

# Match runs that look like Latin-1-decoded UTF-8 (lead bytes Â–Ï followed by
# continuation bytes U+0080–U+00BF, or Î/Ï followed by any single Latin-1 char).
# Captures:
#   • 3-byte sequences: â/ã/ä…ï (U+00E2–U+00EF) + two bytes in 0x80–0xBF
#   • 2-byte sequences: À–ß (U+00C0–U+00DF) + one byte in 0x80–0xBF
MOJIBAKE_3 = re.compile(r'[\xe2-\xef][\x80-\xbf][\x80-\xbf]')
MOJIBAKE_2 = re.compile(r'[\xc0-\xdf][\x80-\xbf]')


def fix_mojibake_sequence(m):
    seq = m.group(0)
    try:
        decoded = seq.encode('latin-1').decode('utf-8')
        # Only accept if it decodes to printable / plausible Unicode
        # (excludes C0/C1 controls produced by accident)
        if all(ord(c) > 0x1F and ord(c) != 0x7F for c in decoded):
            return decoded
    except (UnicodeEncodeError, UnicodeDecodeError):
        pass
    return seq


def fix_text(text):
    # Pass 1: fix 3-byte mojibake (smart quotes, em-dashes, Greek 3-byte chars)
    text = MOJIBAKE_3.sub(fix_mojibake_sequence, text)
    # Pass 2: fix 2-byte mojibake (Greek letters, accented Latin from Latin-1 source)
    text = MOJIBAKE_2.sub(fix_mojibake_sequence, text)
    # Pass 3: replace any remaining standalone C1 control chars via CP850 map
    text = ''.join(CP850_MAP.get(c, c) for c in text)
    return text


def process_file(fp):
    with open(fp, encoding='utf-8') as f:
        original = f.read()
    fixed = fix_text(original)
    if fixed != original:
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(fixed)
        return True
    return False


def main():
    files = sorted(glob.glob(os.path.join(COMMENTARY_DIR, '**', '*.json'), recursive=True))
    changed = []
    for fp in files:
        rel = os.path.relpath(fp, COMMENTARY_DIR)
        if process_file(fp):
            changed.append(rel)

    print(f"Fixed {len(changed)}/{len(files)} files:")
    for f in changed:
        print(f"  ✓  {f}")
    if not changed:
        print("  No changes needed.")

if __name__ == '__main__':
    main()
