"""
MKT Original — Matthew chapters 1–4 (Greek philology layer)
Output: data/commentary/mkt-original/matthew.json

Key terms: biblos geneseos, huios Dauid, parthenos, Emmanuel, ek pneumatos hagiou,
magoi, to paidion, kata to rhēthen, baptisma metanoias, ho agapetos, peirazo.
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
  "1": {
    "1": '<p><strong>biblos geneseos</strong> (<em>biblos geneseos</em>) — book of the origin/genealogy — the same phrase as LXX Gen 5:1 (<em>haute he biblos geneseos anthropon</em>). Matthew deliberately opens with the creation-formula, presenting Jesus as inaugurating a new genesis. <strong>Iesou Christou</strong> — Jesus Christ — the name first, immediately followed by both titles: <em>huiou Dauid</em> (son of David, the royal Messianic line) and <em>huiou Abraam</em> (son of Abraham, the covenant promise-bearer). The reverse order (David before Abraham) emphasizes the Messianic dimension; then the founding covenant is named.</p>',
    "18": '<p><strong>mnesteutheises</strong> (<em>mnesteuo</em>) — betrothed, engaged — the Jewish betrothal (<em>erusin</em>) was a legally binding covenant, not merely a modern engagement; breaking it required a divorce (v.19 apolyein = to release/divorce). <strong>ek pneumatos hagiou</strong> — of/from the Holy Spirit — the preposition <em>ek</em> denotes origin: the conception is sourced from the Holy Spirit, not from human generation. <strong>ephanerothe</strong> — was revealed, appeared — Matthew uses a passive suggesting divine disclosure; the pregnancy was not hidden but theologically explained by the angel as divine action.</p>',
    "21": '<p><strong>Iesous</strong> — Jesus, the Greek form of Hebrew <em>Yeshua</em> (Joshua), which means YHWH saves or YHWH is salvation. The angel\'s explanation (<em>autos gar sosei</em> = for he himself will save) plays on the name\'s etymology: the one named YHWH-saves will in fact save (<em>sosei</em>). <strong>ton laon autou</strong> — his people — the possessive is striking; even before the birth, the angel calls Israel his people. <strong>apo ton hamartion auton</strong> — from their sins — not merely from enemies or oppressors (the expected Davidic deliverance) but from sins; the scope of salvation is transformed.</p>',
    "23": '<p><strong>parthenos</strong> (<em>parthenos</em>) — virgin — Matthew uses the LXX reading of Isa 7:14, which translates Hebrew <em>almah</em> (young woman of marriageable age) with the Greek term specifically denoting virginity. Matthew stakes the fulfillment on this reading. <strong>Emmanuel</strong> — Hebrew <em>Immanu El</em> = God with us — not merely a descriptive title but a theological claim: the presence of God (the Shekinah) is now embodied in the person of Jesus. Matthew frames the entire Gospel between Immanuel (1:23) and the presence-promise of 28:20.</p>'
  },
  "2": {
    "1": '<p><strong>magoi</strong> (<em>magi</em>, plural of <em>magos</em>) — originally a priestly caste of Persian Zoroastrians skilled in astronomy, interpretation of signs, and dream interpretation. By the 1st century the term had broadened to include wise men, court astrologers, and interpreters of omens throughout the eastern Mediterranean. Matthew does not specify three or kings — the church tradition of three kings derives from the three gifts (v.11). <strong>apo anatolon</strong> — from the east — the same direction from which the Babylonian exile came; now wise men from the nations seek the Jewish King.</p>',
    "11": '<p><strong>prosekynesan auto</strong> — they worshiped/did obeisance to him — <em>proskyneo</em> (fall before in worship or homage) is used throughout Matthew for worship of Jesus (4:10, 8:2, 9:18, 14:33, 15:25, 28:9,17) and specifically for worship of God (4:10 quoting Deut 6:13). The Magi perform before the infant what the disciples perform before the risen Lord. <strong>edoran auto dora</strong> — they offered him gifts — the noun <em>dora</em> (gifts, offerings) carries cultic overtones; these are tribute-offerings appropriate to a king and priest.</p>'
  },
  "3": {
    "2": '<p><strong>metanoeite</strong> (<em>metanoeo</em>) — repent, change one\'s mind and direction — the verb combines <em>meta</em> (after, change) + <em>noeo</em> (to think, perceive). True repentance is not mere remorse (<em>metamelomai</em>) but a reorientation of the whole person\'s direction. <strong>hengiken gar he basileia ton ouranon</strong> — for the kingdom of the heavens has drawn near — <em>engiken</em> is perfect tense (has come near and stands near), indicating the kingdom\'s arrival is not merely future but has approached to proximity. <em>Basileia ton ouranon</em> is Matthew\'s distinctive phrase (vs. Mark/Luke\'s <em>basileia tou theou</em>); the <em>ouranon</em> (heavens plural) is the reverential Jewish circumlocution for God.</p>',
    "11": '<p><strong>baptizo</strong> (<em>baptizo</em>) — to immerse, dip, plunge — used for dyeing cloth, sinking ships, and ritual washings; in Jewish contexts (<em>mikveh</em>) it denoted purification immersion. John\'s baptism is <strong>eis metanoian</strong> (unto/for repentance) — the preposition <em>eis</em> indicates purpose or result. He contrasts it with Jesus\'s baptism <strong>en pneumati hagio kai pyri</strong> — in/with the Holy Spirit and fire — the preposition <em>en</em> is instrumental: the Spirit and fire are the medium, not the destination.</p>',
    "17": '<p><strong>houtos estin ho huios mou ho agapetos</strong> — this is my beloved Son — the demonstrative <em>houtos</em> identifies the specific individual; <em>agapetos</em> (beloved, uniquely loved) appears in the LXX at Gen 22:2 for Isaac (the only son, <em>yahid</em>); the term carries the Aqedah resonance of the uniquely beloved son offered. <strong>en ho eudokesa</strong> — in whom I am well pleased — the aorist <em>eudokesa</em> (to be well pleased, to take delight in) combines the royal Ps 2:7 investiture with the Servant Isa 42:1 anointing; king and servant in one declaration.</p>'
  },
  "4": {
    "1": '<p><strong>anechthe</strong> (<em>anago</em>) — led up — the passive (was led up) makes the Spirit the agent of the wilderness-leading, just as YHWH led Israel in the wilderness (Deut 8:2, the immediate context of Jesus\'s first temptation response). <strong>peirasthēnai</strong> — to be tested/tempted — <em>peirazo</em> carries both meanings: external testing (to prove quality) and internal temptation (to induce sin). The wilderness testing recapitulates Israel\'s 40 years (Jesus\'s 40 days) with the key difference that Jesus passes where Israel failed.</p>',
    "17": '<p><strong>apo tote erxato</strong> — from that time he began — <em>apo tote</em> is a Matthean structural marker used at key transitions (also 16:21 for the passion-announcements). <strong>kerusso</strong> — to herald, proclaim — the verb of public announcement rather than private teaching; Jesus speaks as one with royal authority proclaiming the King\'s news. The message is identical to John\'s (3:2): <strong>metanoeite, engiken gar he basileia ton ouranon</strong> — but Jesus proclaims it as the one in whom the kingdom is present, not merely approaching.</p>'
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
