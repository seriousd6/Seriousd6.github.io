"""
MKT Context — 1 John chapter 5
Output: data/commentary/mkt-context/1john.json (adds ch5)
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
    "6": '<p>The "water and blood" of v.6 has generated multiple interpretive traditions, each reflecting a different cultural-theological context: (1) Baptism + Eucharist: the sacramental reading (Tertullian, Cyprian) that grounds both Christian rites in the incarnate Christ\'s own water-and-blood coming; (2) Jordan-baptism + Golgotha-blood: the anti-Docetic reading that insists the same Jesus who was baptized died on the cross (targeting Cerinthus, who taught the divine Christ departed before the crucifixion); (3) Johannine eyewitness: connecting to John 19:34 (water and blood from the pierced side), with the added witness of the Spirit (John 19:35). The first-century audience would have heard all three registers, since baptism, the Lord\'s Supper, and the crucifixion narrative were all central to community life.</p>',
    "14": '<p>Prayer with <em>parresia</em> (boldness/confidence) was a known Stoic ideal (the sage speaking frankly to anyone, even kings) but here receives a thoroughly Johannine-covenantal content. The <em>parresia</em> of prayer is not the Stoic autonomous sage\'s self-confidence but the covenant child\'s access-confidence before the Father — grounded not in moral achievement but in union with the Son who always prays and is always heard (John 11:41-42). This is the theological resolution of the Jewish problem of how a sinful community can approach a holy God: through the advocacy of the Son.</p>',
    "16": '<p>The "sin unto death" discussion has parallels in several traditions: (1) The Qumran community distinguished between sins correctable through community discipline and sins requiring expulsion (1QS 8:20-9:2, 7:1-25); (2) Rabbinic law distinguished between transgressions for which sacrifices atoned and those for which only death atoned (Mishnah Yoma 8:8); (3) Numbers 15:30-31 identified high-handed deliberate sin as beyond sacrificial remedy. John does not define the sin-unto-death precisely, which suggests his community understood the category from shared tradition — likely apostasy combined with active opposition to Christ, the unforgivable sin of rejecting the Spirit\'s witness to the Son (Mark 3:29, Matt 12:31-32).</p>',
    "20": '<p>The claim "this is the true God and eternal life" (v.20) at the letter\'s close echoes the Shema theology (Deut 6:4) while identifying Jesus as the content of what the Shema affirms. In a city like Ephesus — home to the Temple of Artemis (one of the Seven Wonders), multiple imperial cult temples, and a dense religious marketplace — the claim to know "the true God" (<em>ton alethinos</em>) was a sharp competitive assertion. The Artemis cult offered <em>soteria</em> (salvation, protection); the imperial cult offered security under the divine emperor. John\'s final verse declares that the community in Christ possesses the reality that all these cult offerings approximated: the true God who is eternal life himself.</p>',
    "21": '<p>The closing "keep yourselves from idols" was not an abstract warning in Ephesus, where Artemis worship permeated the city\'s economic, social, and civic life. Acts 19:23-41 records the riot of the silversmiths who made shrines to Artemis — the economic infrastructure of idol-worship was vast. Participation in civic festivals (including temple meals with idol-offerings, 1 Cor 8-10), guild dinners, and household shrines were all forms of the idol-contact the community was to avoid. The letter that begins with the tangible, physical reality of the incarnation ends with the equally tangible, social reality of idolatry — both the false spiritual (Docetism) and the false material (idols) are rejected in favor of the true God incarnate in Jesus Christ.'
  }
}

def main():
    existing = load_comm('mkt-context', '1john')
    merge_comm(existing, DATA)
    save_comm('mkt-context', '1john', existing)
    total = sum(len(v) for v in existing.values())
    print(f'1 John mkt-context: {len(existing)} chapters, {total} verses written.')

if __name__ == '__main__':
    main()
