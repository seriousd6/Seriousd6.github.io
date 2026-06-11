"""
MKT Original Commentary — Daniel chapter 12
Run: python3 scripts/zc-original-daniel-12-fill.py

Source data used:
- data/interlinear/daniel.json
- data/translation/draft/mediating/daniel.json (MKT text)

Key decisions in this range:
- Ch 12 returns to Hebrew (from Aramaic ch 2-7); noted at context level.
- 'diraon' (v.2, contempt) appears only here and Isa 66:24 — this rare term signals
  conscious intertextual echo of Isaiah's final verse.
- 'maskilim' (v.3, 10) carries both 'wise' and 'cause-to-shine' resonances; both are
  preserved in commentary.
- The 'goral' (v.13, lot/allotment) is the land-portion vocabulary of Joshua —
  Daniel's personal resurrection promise is framed as covenant land-inheritance.
- 'time, times, half a time' (v.7) recurs from ch 7:25; cross-reference maintained.
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

DANIEL = {
  "12": {
    "1": '<p><strong>Michael</strong> (<em>Mikha\'el</em>, H4317, "who is like God?") — the name is a rhetorical question asserting divine incomparability; in Daniel Michael functions as <em>sar</em> (H8269, prince/guardian) specifically over Israel (10:21). His "arising" (<em>ya\'amod</em>, H5975) echoes the same verb used for Daniel\'s own promised resurrection in v.13 — the angelic champion stands, and so will Daniel. <strong>Time of distress</strong> (<em>et tsarah</em>, H6256 + H6869) — the temporal phrase uses <em>tsarah gedolah</em> (great trouble/tribulation), an intensification of the exodus vocabulary (Deut 4:30, <em>ba-tsarah lekha</em>). "Such as never was since there was a nation" — the incomparable-distress formula echoes Joel 2:2 and anticipates its NT application (Matt 24:21). <strong>Book</strong> (<em>sefer</em>, H5612) — the book of the living, in which Israel\'s rescued are enrolled; cf. Exod 32:32-33, Ps 69:28, Mal 3:16.</p>',
    "2": '<p><strong>Many who sleep in the dust</strong> — <em>rabbim miyshene admat-afar</em>: <em>rabbim</em> (H7227, many) is the same word used in Isa 53:11 (the Servant justifying <em>rabbim</em>); <em>yashen</em> (H3463, sleep) as a euphemism for death; <em>afar</em> (H6083, dust) — the ground into which Adam was returned (Gen 3:19). This verse directly reverses the death sentence of Genesis 3. <strong>Everlasting life</strong> (<em>chayyei olam</em>, H2416 + H5769) — the phrase appears here for the first time in the OT in this exact form; Jesus takes it directly into Greek as <em>zōē aiōnios</em> (John 3:16; 5:24). <strong>Contempt</strong> (<em>dera\'on</em>, H1860) — this rare noun appears only here and Isa 66:24 ("the worm does not die"), making the book of Daniel close on a conscious echo of Isaiah\'s closing vision of final judgment. The two destinations — <em>chayyei olam</em> and <em>dera\'on</em> — are the sharpest OT formulation of eternal division.</p>',
    "3": '<p><strong>The wise will shine</strong> (<em>maskilim yaz\'hiru</em>) — <em>maskil</em> (H7919, wise/instructed) is also the hiphil participle of H2094 <em>zahar</em>, meaning "to cause to shine/warn/teach"; the verbal range is deliberate: those who have been enlightened <em>and</em> enlighten others shine with reflected glory. <strong>Brightness of the firmament</strong> (<em>zohar ha-raqia\'</em>) — <em>zohar</em> (H2096, brightness) + <em>raqia\'</em> (H7549, the firmament of Gen 1:6-8): the vocabulary of creation\'s luminaries is applied to the resurrection glory of the faithful. <strong>Like the stars forever</strong> (<em>kochavim le-olam va-ed</em>) — Paul draws on this tradition in 1 Cor 15:41-44 (the resurrection body compared to different degrees of stellar glory). The stars language echoes Abraham\'s descendants (Gen 15:5; 22:17) and Daniel\'s own vision of the holy ones as heavenly host.</p>',
    "4": '<p><strong>Shut up and seal the words</strong> (<em>setom vachatom ha-devarim</em>) — two near-synonyms: <em>satam</em> (H5640, to stop up/close) and <em>chatam</em> (H2856, to seal with a signet). Sealing a scroll preserves its contents for the appointed time; this is not suppression but eschatological safekeeping (cf. Rev 5:1 where the sealed scroll awaits the Lamb). <strong>Until the time of the end</strong> (<em>le-et qetz</em>, H6256 + H7093) — <em>qetz</em> appears in Daniel as the decisive technical term for the eschatological terminus; it first entered Daniel\'s vocabulary at 8:17 and now closes the book. <strong>Knowledge will increase</strong> (<em>tarbeh ha-da\'at</em>, H7235 + H1847) — <em>da\'at</em> is relational/covenantal knowledge, not merely information; the increase corresponds to the unsealing of the scroll, not technological progress.</p>',
    "5": '<p>Two angelic figures on the river banks — the scene echoes the theophany of ch 10 (the "man clothed in linen" over the river, H2975 <em>ye\'or</em>). The doubling of witnesses (<em>shenayim acherim</em>, two others) recalls the legal requirement of two witnesses (Deut 19:15); the revelation of the final things is confirmed by heavenly testimony. The river (<em>ye\'or</em>, the Nile/great river) grounds the vision in the liminal space between the earthly and heavenly.</p>',
    "6": '<p><strong>How long?</strong> — <em>ad-matai</em> (H4970), the prophetic question asked also in Pss 13, 74, 79, 89, and Hab 1:2. The question is addressed to "the man clothed in linen above the waters" (<em>levush ha-badim</em>, H906 <em>bad</em> — fine linen, the priestly material; cf. Lev 16:4, Ezek 9:2-3). The figure\'s position <em>above</em> the waters inverts the standing position of the two figures on the banks — elevation signals authority.</p>',
    "7": '<p><strong>Swore by him who lives forever</strong> (<em>vayishava be-chai ha-olam</em>) — the oath by "the living forever one" (H2416 + H5769) is the strongest possible guarantee; in the OT only God swears by himself (Gen 22:16; Isa 45:23). <strong>Time, times, and half a time</strong> (<em>le-moed moedim va-chatsi</em>, H4150 + H5732 + H2677) — the three-and-a-half period recurs from 7:25; using <em>moed</em> (appointed time, festival-time) rather than the Aramaic <em>idan</em>, the Hebrew text loads the interval with covenantal calendar resonance. <strong>Shattering the power of the holy people</strong> (<em>kenaphets yad am-qadosh</em>) — <em>naphets</em> (H5310, shatter/scatter); <em>yad</em> (H3027, hand/power) — when the power of God\'s people has been utterly broken, then (<em>ve-khallenah</em>, H3615, then it will be finished) all these things will be completed.</p>',
    "8": '<p>Daniel\'s admission: <em>shama\'ti ve-lo avin</em> — "I heard but I did not understand." <em>Shama\'</em> (H8085) normally implies comprehension; the qualification "but did not understand" (<em>bin</em>, H995) creates an instructive gap: the revelation is genuine and recorded, but its full significance remains sealed. The prophet can be a faithful transmitter without being a complete interpreter. <em>Acharit ella</em> (H319, the outcome/end of these things) — Daniel asks for closure; he receives instead a command to proceed without it.</p>',
    "9": '<p><strong>Go your way</strong> (<em>lekh Daniel</em>) — a gentle dismissal of the question. The words are <em>setumim ve-chatumin</em> (shut up and sealed, from the same roots as v.4) — the doubling is intentional: the sealing is confirmed even after Daniel\'s question. <strong>Until the time of the end</strong> recurs; the structure of non-understanding is constitutive for the reader also — the book closes on intentional opacity that models the eschatological posture of waiting trust.</p>',
    "10": '<p><strong>Purified, made white, refined</strong> — three metallurgical/laundry terms: <em>yitbararu</em> (H1305, barar — to cleanse/purify, used for sifting grain and refining metal), <em>yitlabenu</em> (H3835, laban — to make white, used for bleaching linen), and <em>yitsarafu</em> (H6884, tsaraph — to smelt/refine precious metal). The triple refinement language is used for Mal 3:2-3 (the refiner\'s fire) and Zech 13:9. <strong>The wicked will continue to act wickedly</strong> (<em>hirshi\'u resha\'im</em>, H7561 + H7563) — the hardening effect of tribulation: the same period purifies the wise and hardens the wicked. <strong>Maskilim will understand</strong> — the verb <em>yavinu</em> (H995) is the same as Daniel\'s own non-understanding in v.8; but in the time of the end the maskilim will have the understanding Daniel was denied.</p>',
    "11": '<p><strong>Daily sacrifice abolished</strong> (<em>hussar ha-tamid</em>, H8548 + H5493) — <em>tamid</em> (the perpetual/daily offering; Num 28:3-8) has been the measure of regular covenant worship; its removal marks the beginning of the crisis period. <strong>Abomination of desolation</strong> (<em>shiqquts meshomem</em>, H8251 + H8074) — <em>shiqquts</em> (detestable/abominable thing) is the Hebrew term for idols (cf. 1 Kgs 11:5, 7); <em>shomem</em> means desolating/laying waste. This phrase is picked up explicitly by Jesus (Matt 24:15, "the abomination of desolation spoken of by Daniel"). <strong>1,290 days</strong> — 30 days longer than the 1,260 days (42 months) of 7:25; the relationship between the time intervals is interpretively open.</p>',
    "12": '<p><strong>Blessed is the one who waits</strong> (<em>ashrei ha-mechakkeh</em>, H835 + H2442) — the beatitude form (<em>ashrei</em> from Ps 1:1) appears here for the one who patiently endures to the end. <em>Chikah</em> (H2442, to wait/tarry) is the active posture of faith under pressure; the same verb used in Isa 8:17 ("I will wait for YHWH") and Hab 2:3 ("wait for it; it will certainly come"). <strong>1,335 days</strong> — 45 days beyond the 1,290; the arithmetic difference points to an additional period of blessing beyond the crisis\'s end, but the text does not specify its content.</p>',
    "13": '<p><strong>Go your way till the end</strong> (<em>ve-atah lekh le-qetz</em>) — the final command given twice (cf. v.9). Daniel is to live out his remaining days in faithful service without requiring further explanation. <strong>You will rest</strong> (<em>tanuach</em>, H5117) — <em>nuach</em> is the root of Noah\'s name and the Sabbath rest; Daniel\'s death is framed as covenant Sabbath-rest. <strong>Stand in your lot at the end of days</strong> (<em>ta\'amod le-goralekha le-qetz ha-yamim</em>) — <em>amad</em> (H5975, to stand) is the resurrection verb from v.1 (Michael "stood"); <em>goral</em> (H1486, lot/allotment) is the Joshua land-portion vocabulary (Josh 14:2; 15:1) — the inheritance of the Land is now the eschatological frame for individual resurrection. Daniel will receive his allotted portion in the covenant inheritance. The book closes not on a cosmic calendar but on a personal resurrection promise.</p>'
  }
}

def main():
    existing = load_comm('mkt-original', 'daniel')
    merge_comm(existing, DANIEL)
    save_comm('mkt-original', 'daniel', existing)
    print('Daniel 12 mkt-original commentary written.')

if __name__ == '__main__':
    main()
