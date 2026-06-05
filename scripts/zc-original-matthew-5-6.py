"""
MKT Original — Matthew chapters 5–6 (Sermon on the Mount part 1)
Output: data/commentary/mkt-original/matthew.json (adds ch5-6)

Key terms: makarios, teleios, antithesis formula, phos tou kosmou, thelema,
ostentation vocabulary (synagogues/street vs. inner room), mammonas.
"""

import json, pathlib

ROOT = pathlib.Path(__file__).parent.parent

def load_comm(source, book):
    p = ROOT / 'data' / 'commentary' / source / f'{book}.json'
    if p.exists():
        return json.loads(p.read_text())
    return {}

def save_comm(source, book, data):
    p = ROOT / 'data' / 'commentary' / source / f'{book}.json'
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=None))
    print(f'  wrote {p.relative_to(ROOT)}')

def merge_comm(existing, new_data):
    for ch, verses in new_data.items():
        if ch not in existing:
            existing[ch] = {}
        for v, html in verses.items():
            if v not in existing[ch]:
                existing[ch][v] = html

DATA = {
  "5": {
    "3": '<p><strong>makarioi</strong> (<em>makarios</em>) — blessed, happy, fortunate — in Hellenistic usage the word described the blissful state of the gods or those who lived like gods; in Jewish usage (Hebrew <em>ashre</em>) it described the one who is in a right relationship with YHWH and experiences his favor. The plural (blesseds) is a Hebraism. <strong>hoi ptochoi to pneumati</strong> — the poor in spirit — <em>ptochos</em> is the beggar-poor (from <em>ptosso</em>, to crouch) rather than the merely hard-pressed <em>penes</em>; in spirit (dative) specifies the domain: those who know their total spiritual bankruptcy before God.</p>',
    "17": '<p><strong>katalyo</strong> — to abolish, dissolve, tear down — used for dismantling buildings and nullifying covenants; Jesus uses the strongest possible abolition-verb to deny that his intention is abolition. <strong>pleroō</strong> — to fill full, complete, fulfill — the same verb as the formula citations (hina plerothe). Jesus comes not to add to the law but to bring it to its intended fullness and goal; his life, death, and resurrection are what the Torah was pointing toward. <strong>iota hen e mia keraia</strong> — one iota or one tittle — the smallest letter of the Greek alphabet (iota = yod in Hebrew) and a serif-mark on a letter; not the smallest detail will pass unfulfilled.</p>',
    "21": '<p><strong>ercousin</strong> is the formula <em>ekouste hoti errethe</em> — you have heard that it was said — the passive <em>errethe</em> (it was said) leaves the speaker unnamed, placing the authority on the received tradition. <strong>ego de lego hymin</strong> — but I say to you — the <em>ego</em> is emphatic by position; the antithesis is not Moses vs. Jesus but tradition-understood vs. authoritatively-interpreted. Jesus speaks with <em>exousia</em> (authority from the one who has the right to speak), not like the scribes who derived authority by citation.</p>',
    "48": '<p><strong>esesthe oun hymeis teleioi</strong> — you therefore shall be perfect/complete/mature — <em>teleios</em> (from <em>telos</em>, end/goal) means having reached one\'s full end or purpose; it is not the impossible Platonic ideal of moral perfection but the wholeness/undividedness of character that mirrors God\'s wholeness. The parallel in Luke 6:36 reads <em>oiktirmon</em> (merciful), suggesting <em>teleios</em> here means wholeness-in-love, the same indiscriminate love that God shows to all. <strong>hos ho pater hymon ho ouranios teleios estin</strong> — as your heavenly Father is perfect — the standard is not an abstract ideal but the character of the Father.</p>'
  },
  "6": {
    "9": '<p><strong>Pater hemon ho en tois ouranois</strong> — Our Father who is in the heavens — the address combines intimacy (<em>Pater</em> = Father, probably translating Aramaic <em>Abba</em>) with transcendence (<em>en tois ouranois</em> = in the heavens, indicating divine majesty). <strong>hagiastheto to onoma sou</strong> — hallowed be your name — the passive imperative (<em>hagiastheto</em>) is a divine passive: may God himself act to hallow his name (sanctify it before the world). This is not a prayer that we will reverence the name but that God will act eschatologically to vindicate his own name (Ezek 36:23).</p>',
    "12": '<p><strong>aphes hemin ta opheilemata hemon</strong> — forgive us our debts — <em>opheilema</em> (debt) is the commercial-legal term for what is owed; sin as moral debt to God is a Semitic conceptual framework (Aramaic <em>hoba</em> = debt = sin). The aorist <em>aphes</em> (forgive, once) vs. the perfect in <em>aphekamen</em> (we have forgiven, already done) — the community\'s forgiveness of others is presented as the completed precondition, not a parallel request.</p>',
    "24": '<p><strong>mammonas</strong> (<em>mammonas</em>) — Mammon — an Aramaic loanword (<em>mammon</em>), wealth or possessions as a personified power; Jesus personifies wealth as a rival lord (<em>kyrios</em>). <strong>ou dynasthe theo douleuein kai mammona</strong> — you cannot serve God and Mammon — the impossibility is structural: a slave belongs entirely to one master; divided service is definitionally impossible in the slave-master relationship. The two masters are presented as mutually exclusive rivals for ultimate loyalty.</p>'
  }
}

def main():
    existing = load_comm('mkt-original', 'matthew')
    merge_comm(existing, DATA)
    save_comm('mkt-original', 'matthew', existing)
    total = sum(len(v) for v in existing.values())
    print(f'Matthew mkt-original: {len(existing)} chapters, {total} verses written.')

if __name__ == '__main__':
    main()
