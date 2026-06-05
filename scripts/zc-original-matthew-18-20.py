"""
MKT Original — Matthew chapters 15–20
Output: data/commentary/mkt-original/matthew.json (adds ch15-20)
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
  "15": {
    "8": '<p><strong>ho laos houtos tois cheilesin me tima, he de kardia auton porro apechei ap emou</strong> — this people honors me with the lips but their heart is far from me — Matthew cites Isa 29:13 LXX as the proof-text for the Pharisees\' tradition-over-Torah priority. <em>Kardia</em> (heart) in the Jewish anthropology is the seat of will, understanding, and intention — not merely emotion; far-heartedness is not coldness of feeling but absence of genuine covenantal alignment. <strong>matēn de sebontai me</strong> — in vain do they worship me — <em>maten</em> (vainly, to no purpose) makes the worship not merely imperfect but empty, producing nothing that constitutes true worship.</p>'
  },
  "16": {
    "16": '<p><strong>su ei ho Christos ho huios tou theou tou zontos</strong> — you are the Christ the Son of the living God — Peter\'s confession stacks three titles: <em>Christos</em> (the anointed one = the Messiah), <em>huios tou theou</em> (Son of God = the one in a unique filial relationship to the Father), and <em>tou zontos</em> (of the living God = the God who is distinctively, characteristically alive, contrasted with dead idols). The full Christological confession combines royal Messianism, divine sonship, and the living covenant-God.</p>',
    "18": '<p><strong>su ei Petros kai epi taute te petra oikodomeso mou ten ekklesian</strong> — you are Peter (Petros) and on this rock (petra) I will build my church — the wordplay is clearer in Aramaic where both are <em>kepha</em> (Cephas). The referent of <em>petra</em> is debated: Peter himself as the founding confessor, Peter\'s confession of Christ, or Christ himself as the foundational rock (1 Cor 10:4). Matthew\'s context suggests Peter-as-confessor: the one who receives the revelation (v.17) is the one on whom the community is built. <strong>ekklesia</strong> — assembly, congregation — Matthew is the only Gospel to use the word; it translates Hebrew <em>qahal</em> (the covenant assembly of Israel).</p>'
  },
  "17": {
    "5": '<p><strong>nephele photeinen</strong> — a bright/luminous cloud — the cloud of divine presence (<em>shekinah</em>) throughout the OT (Exod 13:21, 40:34-38, 1 Kgs 8:10-11); the Transfiguration cloud is the visible form of the divine glory-presence investing itself in the scene. <strong>akouete autou</strong> — listen to him — the addition to the baptism-declaration (3:17) echoes Deut 18:15 (him you shall listen to = the prophet like Moses); the Transfiguration completes the Moses/Elijah pattern by declaring that the one who surpasses them is the one to be heard.</p>'
  },
  "18": {
    "18": '<p><strong>hosa ean desete epi tes ges estai dedomena en ourano</strong> — whatever you bind on earth will have been bound in heaven — the exact same binding/loosing language as 16:19 (the authority given to Peter) is now given to the community as a whole in the context of church discipline. <em>Deo/luo</em> (bind/loose) were standard rabbinic terms for declaring something forbidden or permitted (halakic ruling); here applied to the community\'s disciplinary decisions and intercessions. The perfects (<em>dedemenon/lelymeron</em>) indicate that the heavenly ratification precedes and grounds the earthly decision.</p>'
  },
  "19": {
    "4": '<p><strong>ho ktisas ap arches arsen kai thely epoiesen autous</strong> — the one who created from the beginning made them male and female — Jesus grounds the marriage argument in the <em>arche</em> (beginning = creation order), which has theological priority over Mosaic legislation. The creation-given (<em>ktisas</em>, aorist passive) is the theological bedrock from which human institutional arrangements derive; Moses\'s concession accommodated fallen humanity but did not abrogate the creation norm. The two-become-one-flesh (Gen 2:24) is not a Mosaic law but a creational institution that precedes law.</p>'
  },
  "20": {
    "28": '<p><strong>dounai ten psychen autou lytron anti pollon</strong> — to give his soul as a ransom in exchange for many — <em>lytron</em> (ransom price) is the price paid to release a slave or captive; the LXX uses it for the redemption-payment. <em>Anti</em> (in exchange for, instead of) is a substitutionary preposition: the soul of Jesus stands in the place of the many. <em>Psyche</em> here means life/person-as-a-whole; Jesus gives himself entirely as the exchange-price. The Isaianic Servant background (Isa 53:10-12) provides the theological content: the Servant makes his soul an offering for sin and thereby justifies many.</p>'
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
