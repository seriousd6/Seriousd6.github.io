"""
MKT Original Commentary — 2 Kings chapters 1–3
Run: python3 scripts/zc-original-2kings-1-3.py

Ch1: baʿal zᵉḇûḇ — 'lord of the flies' as scribal mockery of baʿal zᵉḇûl ('Baal the Prince');
     Elijah's description — 'hairy man / leather belt' = the Elijah-figure (Matt 3:4; Mark 1:6)
Ch2: ʾayyēh YHWH ʾelōhê ʾēliyyāhû — 'where is the God of Elijah?' at the Jordan
Ch3: wayhî kᵉnaggen hammᵉnaggen — music as the medium of prophetic Spirit-reception

Key Hebrew terms:
- baʿal zᵉḇûḇ (1:2): deliberate scribal alteration of zᵉḇûl ('prince') to zᵉḇûḇ ('flies')
- ʾîš baʿal śēʿār (1:8): 'the hairy man' = Elijah's identifying description
- ʾayyēh YHWH ʾelōhê ʾēliyyāhû (2:14): Where is the God of Elijah? — prophetic inheritance
- kᵉnaggen hammᵉnaggen (3:15): 'as the minstrel played' — Spirit/music connection
"""

import json, pathlib

ROOT = pathlib.Path(__file__).parent.parent

def load_comm(layer, book):
    p = ROOT / 'data' / 'commentary' / layer / f'{book}.json'
    return json.loads(p.read_text()) if p.exists() else {}

def save_comm(layer, book, data):
    p = ROOT / 'data' / 'commentary' / layer / f'{book}.json'
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

ORIGINAL = {
  "1": {
    "2": "<p>Ahaziah&rsquo;s inquiry of &lsquo;<em>baʿal zᵉḇûḇ</em> ʾelōhê ʿeqrôn&rsquo; — &lsquo;Baal-zebub god of Ekron&rsquo; — almost certainly preserves a scribal alteration of the deity&rsquo;s actual name. The Ugaritic texts and comparative Semitic evidence suggest the actual divine name was <em>baʿal zᵉḇûl</em> (&lsquo;Baal the Prince&rsquo; or &lsquo;Exalted Baal&rsquo;; <em>zbl</em> = prince, exalted one, cf. Ugaritic <em>zbl</em> as a divine epithet). The MT&rsquo;s <em>zᵉḇûḇ</em> (flies) instead of <em>zᵉḇûl</em> (prince) is the pattern of deliberate scribal degradation applied to Canaanite divine names in the Hebrew text tradition — the same tradition that vocalized <em>Baal</em> with the vowels of <em>bōšet</em> (shame) in personal names (cf. Ishbosheth / Ish-baal; Mephibosheth / Mephibaal). The NT picks up the <em>zᵉḇûl</em> form: Matthew 10:25 and 12:24 use <em>Beelzeboul</em> (Beelzebul), identifying the Philistine Baal with the prince of demons. The name-play is sustained across both testaments: the scribes mock the Baal with <em>zᵉḇûḇ</em> (flies); the NT identifies the same deity under <em>zᵉḇûl</em> (prince) as the archon of the demonic realm, against whom Jesus casts out demons as evidence of the arrival of YHWH&rsquo;s kingdom.</p>",
    "8": "<p>The description that identifies Elijah to Ahaziah&rsquo;s officers — <em>ʾîš baʿal śēʿār wᵉʾēzôr ʿôr ʾāzûr bᵉmotnāyw</em>, &lsquo;a hairy man with a leather belt around his waist&rsquo; — is the prophet&rsquo;s identifying uniform. The phrase <em>baʿal śēʿār</em> (literally &lsquo;lord/owner of hair&rsquo;) means either that Elijah wore a garment of animal hair (the traditional prophetic mantle, <em>ʾadderet</em>, cf. 1 Kgs 19:13, 19; Zech 13:4: &lsquo;a hairy robe&rsquo; as the false prophet&rsquo;s disguise) or had an unshaven, wild appearance. The leather belt (<em>ʾēzôr ʿôr</em>) is the practical wilderness garment. Matt 3:4 deliberately applies this description to John the Baptist: <em>autos de ho Iōannēs eichen to endyma autou apo trichōn kamēlou kai zōnēn dermatinēn peri tēn osphyn autou</em> — &lsquo;now John wore a garment of camel&rsquo;s hair and a leather belt around his waist.&rsquo; The verbal echo is intentional: the narrator identifies John as the Elijah-figure by clothing him in Elijah&rsquo;s recognizable garments. Luke 1:17 makes the typological claim explicit: John comes &lsquo;in the spirit and power of Elijah&rsquo; (<em>en pneumati kai dynamei Ēliou</em>). The leather-belt description in 2 Kgs 1:8 is the OT datum that the Synoptic tradition applies to identify John as Elijah returned.</p>"
  },
  "2": {
    "14": "<p>Elisha&rsquo;s cry at the Jordan before striking the water with Elijah&rsquo;s mantle — <em>ʾayyēh YHWH ʾelōhê ʾēliyyāhû</em>, &lsquo;where is YHWH the God of Elijah?&rsquo; — is the prophet&rsquo;s demand for theophanic demonstration before the act of succession. The question is rhetorical: it is a cry that calls for an answer in action. The waters divide; the prophetic inheritance is confirmed. The same structure — calling on YHWH before a public miracle to demonstrate divine presence and prophetic authorization — appears in Elijah&rsquo;s Carmel prayer (1 Kgs 18:36: <em>ʿăṡeh yadûʿ hayyôm kî ʾattāh ʾelōhîm bᵉyiśrāʾēl</em>, &lsquo;let it be known today that you are God in Israel&rsquo;) and in Jesus&rsquo;s prayer before raising Lazarus (John 11:41-42: <em>Pater, eucharistō soi hoti ēkousas mou... hina pisteusōsin hoti sy me apesteilas</em> — &lsquo;Father, I thank you that you have heard me... so that they may believe that you sent me&rsquo;). In each case the public prayer functions not to inform YHWH but to demonstrate to the watching crowd that the miracle comes from YHWH through his authorized agent. Elisha&rsquo;s Jordan-strike with the mantle is also the proof-fulfillment of the double-portion request (v9): the same Spirit that worked through Elijah now works through Elisha, demonstrated by the same Jordan sign.</p>"
  },
  "3": {
    "15": "<p>Elisha&rsquo;s request for a musician before prophesying — <em>wᵉʿattāh qᵉḥû lî mᵉnaggen wayhî kᵉnaggen hammᵉnaggen watᵉhî ʿālāyw yaḏ YHWH</em>, &lsquo;bring me a minstrel; and when the minstrel played, the hand of YHWH came upon him&rsquo; — is one of the OT&rsquo;s clearest connections between music and prophetic inspiration. The <em>yaḏ YHWH</em> (hand of YHWH) is the standard term for prophetic Spirit-reception in Ezekiel (1:3; 3:14, 22; 8:1; 37:1) and here marks the moment the Spirit descends. The practical use of music to prepare the prophet for reception echoes 1 Sam 10:5-6 (the band of prophets with harp, tambourine, flute, and lyre preceding Saul&rsquo;s Spirit-reception) and 1 Sam 16:16, 23 (David&rsquo;s harp-playing causing the evil spirit to depart from Saul — music as a counter-spiritual force). The Chronicler&rsquo;s integration of music into the Levitical liturgy (1 Chr 25: Asaph, Heman, and Jeduthun appointed to prophesy with lyres, harps, and cymbals) formalizes what the Elisha episode makes narrative: music is the embodied preparation for the Spirit&rsquo;s movement, not its cause but its occasion. The NT&rsquo;s Eph 5:18-19 (&lsquo;be filled with the Spirit, addressing one another in psalms and hymns and spiritual songs&rsquo;) sustains the connection between Spirit-reception and corporate sung worship.</p>"
  }
}

def main():
    c = load_comm('mkt-original', '2kings')
    merge_comm(c, ORIGINAL)
    save_comm('mkt-original', '2kings', c)
    count = sum(len(v) for v in ORIGINAL.values())
    print(f'2kings mkt-original: wrote {count} verses across ch 1-3')

if __name__ == '__main__':
    main()
