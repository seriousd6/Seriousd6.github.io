#!/usr/bin/env python3
"""
SW-H: Build cognate word families using directed derivation graph from `deriv` field.

Strategy:
  - Parse parent Strong's codes from each entry's `deriv` field
  - Build directed graph: child → parent(s)
  - Find roots (primitive roots: no in-lexicon parent)
  - BFS from each root to collect descendants (max depth 3, max family 20 members)
  - Output families with 2+ meaningful members

Output:
  data/grammar/cognate-families-hebrew.json
  data/grammar/cognate-families-greek.json
  data/grammar/cognate-index-hebrew.json   (code → root)
  data/grammar/cognate-index-greek.json

Schema per family:
  { root, root_lemma, root_translit, root_meaning, lang,
    members: [{ code, lemma, translit, gloss, is_root }] }
"""

import json, re, os

def load_json(path):
    with open(path, encoding='utf-8') as f:
        return json.load(f)

def code_num(code):
    m = re.search(r'\d+', code)
    return int(m.group()) if m else 0

def extract_parents(deriv_str, prefix):
    """Extract Strong's parent codes from deriv field (e.g. 'from H3513 (כָּבַד);')."""
    return re.findall(prefix + r'\d+', deriv_str)

def is_proper_noun(entry):
    """Heuristic: gloss is a proper name if it's title-case with no lowercase interior."""
    g = entry.get('gloss', '').split(',')[0].strip()
    words = g.split()
    if not words:
        return False
    # If first word is title-case and very short with no known verbs/nouns indicators
    return (len(words) <= 2
            and words[0][0].isupper()
            and all(ch.isupper() or not ch.isalpha() for ch in words[0][1:3])
            and len(words[0]) > 3)

def build_families(strongs_dict, prefix, max_family=20, max_depth=3):
    # Build parent map: code → [parent_codes in lexicon]
    parent_map = {}
    child_map  = {}  # root→[children]
    for code, entry in strongs_dict.items():
        parents = [p for p in extract_parents(entry.get('deriv', ''), prefix) if p in strongs_dict]
        parent_map[code] = parents
        for p in parents:
            child_map.setdefault(p, []).append(code)

    # Roots: codes with no in-lexicon parent
    roots = [c for c in strongs_dict if not parent_map[c]]

    families = []
    for root in sorted(roots, key=code_num):
        # BFS from root up to max_depth, collecting descendants
        visited = {root}
        queue   = [(root, 0)]
        members = [root]
        while queue and len(members) < max_family:
            node, depth = queue.pop(0)
            if depth >= max_depth:
                continue
            for child in child_map.get(node, []):
                if child not in visited and len(members) < max_family:
                    visited.add(child)
                    queue.append((child, depth + 1))
                    members.append(child)

        if len(members) < 2:
            continue

        # Skip mostly-proper-noun families
        proper = sum(1 for c in members if is_proper_noun(strongs_dict[c]))
        if proper / len(members) > 0.6:
            continue

        root_entry = strongs_dict[root]
        root_gloss = root_entry.get('gloss', '')
        root_meaning = root_gloss.split('.')[0].split(',')[0].strip()
        if len(root_meaning) > 60:
            root_meaning = root_meaning[:57] + '…'

        member_list = []
        for code in sorted(members, key=code_num):
            e = strongs_dict[code]
            g = e.get('gloss', '')
            if len(g) > 80:
                g = g[:77].rsplit(',', 1)[0] + '…'
            member_list.append({
                'code':     code,
                'lemma':    e.get('lemma', ''),
                'translit': e.get('translit', ''),
                'gloss':    g,
                'is_root':  code == root,
            })

        families.append({
            'root':         root,
            'root_lemma':   root_entry.get('lemma', ''),
            'root_translit':root_entry.get('translit', ''),
            'root_meaning': root_meaning,
            'lang':         prefix,
            'members':      member_list,
        })

    return families

def main():
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    for lang, fname, prefix in [
        ('Hebrew', 'hebrew.json', 'H'),
        ('Greek',  'greek.json',  'G'),
    ]:
        print(f'Processing {lang}…')
        strongs = load_json(os.path.join(base, 'data', 'strongs', fname))
        families = build_families(strongs, prefix)
        print(f'  {len(families)} families found')

        # Sort by root code number
        families.sort(key=lambda f: code_num(f['root']))

        out_dir  = os.path.join(base, 'data', 'grammar')
        out_path = os.path.join(out_dir, f'cognate-families-{lang.lower()}.json')
        with open(out_path, 'w', encoding='utf-8') as f:
            json.dump(families, f, ensure_ascii=False, indent=2)
        print(f'  → {out_path}')

        # Inverted index: code → root
        index = {}
        for fam in families:
            for m in fam['members']:
                index[m['code']] = fam['root']
        idx_path = os.path.join(out_dir, f'cognate-index-{lang.lower()}.json')
        with open(idx_path, 'w', encoding='utf-8') as f:
            json.dump(index, f, ensure_ascii=False)
        print(f'  → {idx_path} ({len(index)} entries)')

if __name__ == '__main__':
    main()
