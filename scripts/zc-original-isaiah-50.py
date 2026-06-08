"""
MKT Original Commentary — Isaiah chapter 50
Run: python3 scripts/zc-original-isaiah-50.py

Isaiah 50 contains the Third Servant Song (vv.4-9), the most explicitly
passion-oriented of the four songs. The chapter also includes a divorce-nullification
oracle (vv.1-3) and a wisdom call (vv.10-11).

Key translation decisions:
- 50:1 sēfer kĕrîtût: "certificate of divorce" — a technical legal document; the
  absence of one proves YHWH did not divorce Israel.
- 50:4 limmudîm: "taught/disciples" — the tongue of the taught ones (limmudîm);
  the related noun talmîd is the later Hebrew for "disciple." The Servant has the
  speech of one who has been divinely instructed.
- 50:6 gēwî / lĕḥāyay / pānay: back, cheeks, face — the three anatomical references
  cover the full Passion narrative. The NT passion accounts (Matt 26:67; Mark 14:65;
  Luke 22:63-64; John 19:1) each fulfill one or more of these.
- 50:7 kĕḥallāmîš: "like flint" — the hardest stone available in the ancient
  Levant; the phrase "set my face like flint" indicates inflexible resolution.
  Luke 9:51 ("he set his face to go to Jerusalem") echoes this language.
- 50:8-9 maṣdîqî / yaʿăzor lî: "he who vindicates/my helper" — the forensic
  challenge. Paul builds on this in Rom 8:33-34 (no one can condemn those whom
  God justifies), applying the Servant's vindication claim to all who are in Christ.
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
    """Merge new_data into existing without overwriting present entries."""
    for ch, verses in new_data.items():
        if ch not in existing:
            existing[ch] = {}
        for v, html in verses.items():
            if v not in existing[ch]:
                existing[ch][v] = html

ISAIAH = {
  "50": {
    "1": '<p><strong>ʾê zeh sēfer kĕrîtût ʾimkĕkem</strong> — "where is the certificate of divorce of your mother?" — the rhetorical question assumes no such document exists. <em>sēfer kĕrîtût</em> (H3748) is the technical legal term for a writ of divorce (cf. Deut 24:1,3; Jer 3:8). YHWH challenges Israel to produce evidence of formal divorce — and cannot be produced. Parallel question: <strong>ûmî minnōšay ʾăšer mākartî etkem lô</strong> — "to which of my creditors did I sell you?" — the second legal scenario (debt-slavery) is also dismissed. <strong>hēn baʿăwōnōtêkem nimkartem</strong> — "for your iniquities you were sold" — the exile was self-caused through sin, not divine abandonment.</p>',
    "2": '<p><strong>maddûaʿ bāʾtî wĕʾên ʾîš</strong> — "why was there no one when I came?" — the lament that YHWH\'s arrival for rescue met no response. <strong>qārāʾtî wĕʾên ʿōneh</strong> — "I called and there was no one who answered" — the failure of responsiveness mirrors the earlier covenant accusation (cf. 65:12; 66:4). Then the counter-challenge: <strong>hăqāṣōr qāṣĕrâ yādî mippĕdût</strong> — "is my hand too short to ransom?" (<em>pĕdût</em>, H6304, redemption/ransom). The rhetorical question expects "no" — power to save exists; the problem is Israel\'s unresponsiveness.</p>',
    "3": '<p><strong>ʾalbîš šāmayim qadrût wĕśaq ʾāśîm kĕsûtām</strong> — "I clothe the heavens in blackness and make sackcloth their covering" — YHWH can reverse creation\'s light. The cosmic darkness imagery inverts the creation of light (Gen 1:3) and anticipates the darkness at the crucifixion (Matt 27:45). The <em>śaq</em> (sackcloth) of the heavens mirrors the human mourning garment — heaven mourns with the same clothing worn at funerals. YHWH\'s demonstration of power establishes that the failure of salvation is not YHWH\'s incapacity but human refusal.</p>',
    "4": '<p><strong>ʾădōnāy Yhwh nātan lî lĕšôn limmudîm</strong> — "the Lord YHWH has given me the tongue of those who are taught/disciples" (<em>limmudîm</em>, H3929, the taught ones — plural of <em>limmûd</em>, from <em>lāmaḏ</em>, to teach/learn). The Servant is specifically characterized as a learner who speaks from instruction received, not from innate authority. <strong>lāḏaʿat lāʿût ʾet-yaʿēp dābār</strong> — "to know how to sustain with a word him who is weary" — the purpose of the instructed tongue is pastoral: to support the exhausted with speech. <strong>yaʿîr lî ʾōzen babbōqer babbōqer</strong> — "he wakens my ear morning by morning" — the daily spiritual formation; the repetition of <em>babbōqer</em> (morning) emphasizes the continuity of divine instruction.</p>',
    "5": '<p><strong>ʾădōnāy Yhwh pātaḥ lî ʾōzen wĕʾānōkî lōʾ mārîtî</strong> — "the Lord YHWH opened my ear, and I was not rebellious" (<em>mārar</em>, H4784, to be rebellious). The opening of the ear by YHWH is the prerequisite for obedience — divine action precedes human response. The Servant\'s obedience is explicitly contrasted with Israel\'s rebellion in chs 1-39. <strong>ʾāḥôr lōʾ nasûgtî</strong> — "I did not turn backward" — the refusal to retreat under pressure. The steadfast obedience is a character description, not merely a single act.</p>',
    "6": '<p><strong>gēwî nātattî lammakkîm ûlĕḥāyay lĕmōrĕṭîm</strong> — "I gave my back to those who strike (<em>nākâ</em>), and my cheeks to those who pluck out the beard." The beard-plucking (<em>māraṭ</em>, H4803, to pluck/pull smooth) was a profound degradation in ANE culture — it was done to captive enemies and was considered deeply shameful. <strong>pānay lōʾ hissatirtî mikelimmôt wārōq</strong> — "I did not hide my face from disgrace and spitting" (<em>rōq</em>, H7536, spittle). The three anatomical elements — back, cheeks, face — span the full range of body-oriented humiliation. Matt 26:67; Mark 14:65; John 19:1 each fulfill one or more of these Servant-song elements at the Passion.</p>',
    "7": '<p><strong>wĕʾădōnāy Yhwh yaʿăzor lî ʿal-kēn lōʾ niklāmtî</strong> — "but the Lord YHWH helps me; therefore I was not disgraced" — the divine assistance transforms the suffering from defeat into endurance. <strong>ʿal-kēn śamtî pānay kĕḥallāmîš</strong> — "therefore I set my face like flint" (<em>ḥallāmîš</em>, H2496, flint — the hardest stone, used for cutting tools). The flint-face is a metaphor for absolute determination in the face of opposition. Luke 9:51 — "he set his face to go to Jerusalem" (<em>estēriksen to prosōpon autou</em>) — echoes this Servant posture in Jesus\'s commitment to the Passion journey. <strong>wĕʾēdaʿ kî-lōʾ ʾēbôš</strong> — "and I know I will not be put to shame."</p>',
    "8": '<p><strong>qārôb maṣdîqî</strong> — "near is the one who vindicates me" (<em>ṣādaq</em> in the hiphil, to declare righteous/acquit). The Servant shifts into forensic (courtroom) language — YHWH is his vindicator against accusers. <strong>mî yārîḇ ʾittî naʿămdâ yāḥad</strong> — "who will contend with me? let us stand up together." The legal challenge is issued to any would-be accuser. <strong>mî-baʿal mišpāṭî yiggaš ʾēlay</strong> — "who is the master of my lawsuit? let him approach me." Paul uses this forensic logic in Rom 8:33-34: "Who shall bring any charge against God\'s elect? It is God who justifies. Who is to condemn?" — the Servant\'s vindication-by-YHWH becomes the basis for the believer\'s freedom from condemnation in Christ.</p>',
    "9": '<p><strong>hēn ʾădōnāy Yhwh yaʿăzor lî mî hûʾ yarširʿēnî</strong> — "behold, the Lord YHWH helps me; who will declare me guilty?" — the divine vindication makes human condemnation futile. <strong>hēn kullām kabbegaḏ yiblû</strong> — "behold, all of them will wear out like a garment" — the accusers/opponents will decay while the Servant endures. <strong>ʿāš yōʾklēm</strong> — "the moth will eat them" — the same moth-eaten garment imagery as 51:8 (where YHWH\'s righteousness endures while the nations rot like moth-eaten wool). The language anticipates Heb 1:11 (the heavens wearing out like a garment) contrasted with Christ\'s permanence.</p>',
    "10": '<p><strong>mî bākem yĕrēʾ Yhwh šōmēaʿ bĕqôl ʿabdô</strong> — "who among you fears YHWH and obeys the voice of his servant?" — the Servant\'s instruction is now mediated to the community. The one who walks in darkness (<em>ʾăšer hālak ḥăšēkîm wĕʾên nōgah lô</em>, "who walks in darkness and has no light") is called to trust (<em>yiḇṭaḥ</em>) in YHWH\'s name and rely (<em>yiššāʿēn</em>) on his God. The model of trust-in-darkness echoes Hab 2:4 ("the righteous will live by his faithfulness") and anticipates the NT call to walk by faith, not by sight (2 Cor 5:7).</p>',
    "11": '<p><strong>hēn kullĕkem qōdĕḥê ʾēš mĕʾazzĕrê zîqôt</strong> — "behold, all of you who kindle fire and equip yourselves with burning torches" — those who manufacture their own light as a substitute for trusting in YHWH. <strong>lĕkû bĕʾûr ʾeškĕkem</strong> — "walk in the light of your fire" — the ironic permission to continue in self-made illumination. <strong>miyyādî hāyĕtâ-zōʾt lākem lĕmaʿăṣēbâ tišhābûn</strong> — "this you have from my hand: you will lie down in torment" (<em>maʿăṣēbâ</em>, H4620, pain/torment). The self-made fire — human wisdom, political maneuvering, idolatry — becomes the source of final torment. The chapter closes with the judgment oracle against self-reliance as the anti-type to the Servant\'s trust in YHWH (vv.4-9).</p>',
  },
}

def main():
    existing = load_comm('mkt-original', 'isaiah')
    merge_comm(existing, ISAIAH)
    save_comm('mkt-original', 'isaiah', existing)
    # INTENT: Verify all 11 Isaiah 50 mkt-original verses present against interlinear
    # CHANGE? If interlinear/isaiah.json ch 50 verse count changes, update expected total
    # VERIFY: Console shows OK with 11 verses; no MISSING output
    il = json.loads((ROOT / 'data' / 'interlinear' / 'isaiah.json').read_text())
    out = json.loads((ROOT / 'data' / 'commentary' / 'mkt-original' / 'isaiah.json').read_text())
    missing = [v for v in il.get('50', {}) if v not in out.get('50', {})]
    if missing:
        print(f'  MISSING: {missing}')
    else:
        print(f'  OK: all Isaiah 50 mkt-original verses present ({len(il.get("50", {}))} verses)')

if __name__ == '__main__':
    main()
