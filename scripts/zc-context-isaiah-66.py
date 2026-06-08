"""
MKT Context Commentary — Isaiah chapter 66
Run: python3 scripts/zc-context-isaiah-66.py

Source data used:
- data/interlinear/isaiah.json
- data/translation/draft/mediating/isaiah.json

Key decisions in this range:
- v. 1: Temple critique in context of ANE divine-dwelling debates; Stephen quotes this
- v. 3: Syncretism catalog — pairing of licit and illicit sacrifices; post-exilic situation
- v. 5: 'harēdîm' — the trembling remnant as a distinct community within Israel
- v. 17: Forbidden foods (pig, mouse) as Lev 11 violations; garden cult sites
- v. 21: Taking Gentiles as priests/Levites — eschatological break from hereditary rule
- v. 24: Worm and fire — Gehenna allusion; Jesus quotes this in Mark 9:44-48
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
    # INTENT: Non-destructive merge — existing entries are never overwritten, safe to re-run
    for ch, verses in new_data.items():
        if ch not in existing: existing[ch] = {}
        for v, html in verses.items():
            if v not in existing[ch]: existing[ch][v] = html

ISAIAH = {
"66": {
"1": "<p>The claim that heaven is YHWH's throne and earth his footstool (<em>hašāmayim kissî wĕhā'āreṣ hădom raglāy</em>) directly challenges the ideology of temple-as-divine-dwelling. Solomon acknowledged this tension at the temple's dedication (1 Kgs 8:27: <em>will God indeed dwell on the earth?</em>). The ANE background assumed temples housed deities — Israel's view was always more complex, holding divine transcendence alongside cultic presence. Stephen quotes v. 1-2 in Acts 7:49-50 to argue that the Jerusalem temple does not contain God.</p>",
"2": "<p>YHWH made all things (<em>yādî 'āśāt kol-'ēlleh</em>) — creator transcendence is the ground for temple critique. The one YHWH regards is the <em>'ānî ûnĕkēh-rûaḥ ûḥārēd 'al-dĕb̠ārî</em> — the afflicted and contrite of spirit who trembles at his word. In Second Temple Judaism, the <em>ḥărēdîm</em> (trembling ones, cf. v. 5) became a recognized category of the faithful remnant who maintained strict covenantal seriousness. This concept is proto-typical of the pietist streams within post-exilic Judaism.</p>",
"3": "<p>The verse pairs legitimate sacrifices with abhorrent acts in a catalog of syncretism: slaughtering an ox AND killing a man (human sacrifice); offering a lamb AND breaking a dog's neck (ritually unclean animal); grain offering AND pig's blood; frankincense AND worshipping idols. This is not either/or but both/and — the practices are simultaneous. The post-exilic context included continued pressure to assimilate to surrounding cult practices. Ezekiel 8:16-18 describes similar syncretistic abominations practiced within the temple precincts.</p>",
"4": "<p>YHWH will choose their delusions (<em>tĕ'alûlêhem</em> — capricious things/terrors; the term appears only here and in Ps 119:37) as a form of judicial irony: those who chose their own ways will receive those ways fully enacted upon them. This is the theological principle of divine abandonment to the consequences of one's choices (cf. Rom 1:24,26,28 where Paul uses the same logic of YHWH <em>giving over</em> those who suppress truth).</p>",
"5": "<p>The <em>ḥărēdîm</em> — those who tremble at YHWH's word — are a distinct community within Israel, addressed separately from the apostates. Their opponents speak mockingly of YHWH's glory (<em>yikabed YHWH</em>) — whether this is genuine religious claim or sarcasm aimed at the trembling ones is debated. The situation reflects internal communal conflict in post-exilic Judah between strict Torah-observers (the returnees' party) and those who had accommodated to Babylonian or Persian religious culture. The same conflict surfaces in Ezra 9-10, Neh 13, and Mal 2-3.</p>",
"6": "<p>The sudden divine voice from the city and temple (<em>qôl šā'ôn mē'îr qôl mēhêkāl qôl YHWH mĕšallēm gĕmûl</em>) is in the tradition of the divine warrior theophany — a battle roar announcing judgment. Compare Amos 1:2 (YHWH roars from Zion) and Joel 3:16 (YHWH roars from Jerusalem). The temple is here the launching point of divine judgment rather than a refuge from it — reversal of the popular Zion theology that treated the temple's presence as automatic protection.</p>",
"7": "<p>The birth-before-labor imagery (<em>b̠eṭerem tāḥîl yāl ĕdāh bĕṭerem yāb̠ô' ḥēbel lāh</em>) reverses the normal sequence: the baby arrives before the birth pangs begin. ANE mythology and royal ideology frequently used birth metaphors to describe the creation of cities, nations, and dynasties — the maternity of cities and their divine patrons was a common image in Mesopotamian literature. Israel used birth language for the exodus (the birth of the nation) and here for the eschatological restoration.</p>",
"8": "<p>The rhetorical question — <em>mî-šāma' k̠āzō't</em> (who has heard such a thing?) — acknowledges that what YHWH is about to do is unprecedented. The birth of a nation in a day (<em>hăyûkāl 'èreṣ bĕyôm 'eḥād</em>) recalls the speed of the exodus: Israel moved from slavery to nation-status virtually overnight. The post-exilic audience would have read this against the backdrop of their slow, difficult return — YHWH promises a different kind of restoration: sudden, complete, and undeniable.</p>",
"9": "<p>The midwifery metaphor: <em>hă'ănî 'aśbîr wĕlō' 'ôlîd</em> — shall I open the womb and not cause birth? In ANE thought, the goddess Nintu (or Ishtar in Babylonian tradition) served as divine midwife at births of importance. YHWH here takes the role of the divine midwife — he who opens the womb (cf. Gen 30:22; 1 Sam 1:5) will not abandon what he has begun. The theological principle: divine initiation guarantees divine completion.</p>",
"10": "<p>The call to rejoice with Jerusalem (<em>śimĕḥû 'et-yĕrûšālaim</em>) presupposes a congregation gathered around the city — the <em>'ōhăb̠êhā</em> (those who love her) are pilgrims and worshippers whose identity is bound to Zion. Psalm 122 uses exactly this language: <em>pray for the peace of Jerusalem; may those who love you prosper</em>. The Zion psalms (46, 48, 76, 84, 87, 122) form the liturgical background for this call — community identity organized around the holy city.</p>",
"11": "<p>The maternal imagery of Zion nursing her children with abundance (<em>mišad tanḥumêhā</em> — from the breast of her consolations) draws on the ancient Near Eastern goddess traditions of the nurturing city-mother. In Mesopotamian lament literature, the destruction of a city was depicted as a mother losing her children; the restoration was depicted as the mother receiving them back. Lamentations uses similar imagery (1:2: all her friends betrayed her; cf. 66:13 where YHWH himself takes the mother's role).</p>",
"12": "<p>The river of peace (<em>nāhār šālôm</em>) and overflowing torrent of national wealth (<em>naḥal šōṭēp̄</em> — a rushing wadi in flood) draw on the ANE cosmic river traditions. Babylon was built on rivers (Ps 137:1); Egypt was sustained by the Nile. The eschatological river flowing to Jerusalem (Ezek 47; Zech 14:8) represents the reversal of desert-barrenness: the cosmic life-giving river redirected to Zion. Revelation 22:1-2 presents the river of life flowing from the throne of God and the Lamb.</p>",
"13": "<p>The explicit maternal simile for YHWH (<em>kĕ'îš 'ăšer 'immô tĕnaḥămennû</em> — as a man whose mother comforts him) is one of the most striking feminine divine images in the Hebrew Bible. Isa 49:15 uses the same comparison (can a nursing mother forget her child?). This does not feminize YHWH but uses the most universally recognized image of intimate consoling love — the mother-child bond — to communicate the intensity of divine comfort. The divine name used here is YHWH, the covenantal name, grounding the maternal metaphor in covenant faithfulness.</p>",
"14": "<p>The flourishing of bones like grass (<em>wĕ'aṣmôtêk̠em k̠addeše' tipraḥnāh</em>) echoes Ezek 37 (dry bones restored to life) and the restoration of physical vitality. The recognition formula: <em>wĕnôda' yad YHWH 'et-'ăb̠ādāyw</em> — the hand of YHWH will be made known to his servants, and his indignation to his enemies. The contrast between the fate of servants and enemies is a recurring structure in the closing chapters of Isaiah (cf. 65:8-16).</p>",
"15": "<p>The fiery theophany (<em>kî-hinnēh YHWH b̠ā'ēš yāb̠ô'</em>) draws on the tradition of YHWH's appearances in fire: the burning bush (Exod 3:2), Sinai (Exod 19:18), the pillar of fire (Exod 13:21), and the theophanic fire in 1 Kings 18 (Elijah on Carmel). Chariots (<em>markāb̠ôt</em>) are the standard equipment of the divine warrior; in Canaanite mythology, Baal rides the clouds in his chariot. YHWH's chariots here are instruments of judgment rather than storm-force.</p>",
"16": "<p>The cosmic judgment by fire and sword echoes the divine-warrior oracle tradition: YHWH executes judgment (<em>nišpāṭ</em>, Niphal — judgment is done to the earth) against all flesh simultaneously. The <em>ḥallĕlê YHWH</em> (the slain of YHWH) recalls the aftermath of holy war in texts like Jer 25:33. This is judgment of universal scope — not limited to one nation but directed at all who rebel.</p>",
"17": "<p>The garden cult sites (<em>miqqaddĕšîm ûmittaharîm 'el-haggannôt</em> — those who sanctify and purify themselves for the gardens) recall Isa 65:3 and the Canaanite garden-sanctuary practices. The forbidden foods — pig (<em>hazzîr</em>), mouse (<em>hā'ak̠b̠ār</em>), and detestable things (<em>haššèqeṣ</em>) — are specifically enumerated in the Levitical purity code (Lev 11:7, 11:29). Consuming them as part of a sacrificial ritual represents a complete inversion of covenantal identity: the boundary markers that define Israel as YHWH's people are destroyed.</p>",
"18": "<p>YHWH's omniscience over deeds and thoughts (<em>yāda'tî ma'ăśêhem wĕmaḥšĕb̠ōtêhem</em>) grounds the gathering of all nations and tongues for the revelation of his glory. The phrase <em>wĕrā'û 'et-kĕb̠ôdî</em> — they shall see my glory — echoes the theophanic disclosure of YHWH's <em>k̠āb̠ôd</em> (weighty presence) at Sinai (Exod 24:16-17), in Isaiah's vision (ch. 6), and Ezekiel's chariot-vision. The eschatological gathering is a universal Sinai event.</p>",
"19": "<p>The survivors (<em>pĕlêṭîm</em> — those who escape) are sent as missionaries to distant nations: Tarshish (western Mediterranean, possibly Spain), Pul and Lud (Africa — possibly Punt and Libya), Tubal (Black Sea region, Asia Minor), and Javan (יָוָן — Greece, specifically the Ionian Greeks). From Israel's perspective these represented the geographical edges of the known world. The mission: <em>wĕhiggîdû 'et-kĕb̠ôdî baggôyim</em> — to declare my glory among the nations. This is the first explicit universal mission mandate in the Hebrew Bible, anticipating the Apostolic mission of Acts.</p>",
"20": "<p>The nations function as carriers of diaspora Jews back to Jerusalem — on horses, chariots, litters (<em>ṣāb̠îm</em> — covered carriages), mules, and swift camels. This reverses the exile imagery: as Israel was taken into captivity by foreign powers, so the foreign powers now bring Israel home. The diaspora Jews are brought as a <em>minḥāh</em> (grain offering) to YHWH — priestly cultic language applied to a human gathering, framing the return as an act of worship.</p>",
"21": "<p>The most radical eschatological claim of the chapter: <em>wĕgam-mēhem 'eqqaḥ lakkōhănîm lallĕwiyyim</em> — from the Gentile nations, YHWH will take some as priests and Levites. The Levitical priesthood was strictly hereditary — only sons of Aaron could serve as priests (Num 18:1-7). This verse breaks the hereditary principle entirely for the eschatological age. Second Temple Judaism debated whether Gentiles could be incorporated into the covenant community; the NT letters of Paul engage precisely this question (Gal 3:28; Eph 2:11-22).</p>",
"22": "<p>The new heavens and new earth (<em>hašāmayim haḥădāšîm wĕhā'āreṣ haḥădāšāh</em>, cf. Isa 65:17) provide the measure of permanence for Zion's seed and name: as permanent as the new cosmic order. The phrase appears in Isa 65:17; 66:22; and is taken up in 2 Pet 3:13 and Rev 21:1. In Jewish eschatology, the current age (<em>'ôlām hazzeh</em>) will give way to the coming age (<em>'ôlām hab̠bā'</em>); the new creation is the coming age's cosmic framework.</p>",
"23": "<p>The new-moon and Sabbath calendar (<em>mîddē-ḥōdèš bĕḥoḏšô ûmiddē-šabbāt bĕšabbattô</em>) frames universal worship within Israel's existing liturgical calendar — the eschatological worship is not a break from Israel's cult but its universal extension. <em>kol-b̠āśār</em> — all flesh — will come to worship, the same phrase used in v. 16 for those subject to divine judgment. The same humanity that faced divine fire now participates in perpetual worship. The calendar is democratized and universalized.</p>",
"24": "<p>The final verse is deliberately jarring: those who go out from universal worship will see the corpses of rebels against YHWH (<em>bĕpigrê hā'ănāšîm happ̄ōšĕ'îm b̠î</em>). The worm and fire that do not cease (<em>tolĕ'ātām lō' tāmût wĕ'iššām lō' tik̠beh</em>) describe the aftermath of conquest — bodies left unburied. The Valley of Hinnom (Hebrew: <em>gê hinnōm</em>, the source of the Greek <em>Geenna</em>/Gehenna) outside Jerusalem served in the Second Temple period as a burning garbage dump — the perpetually-smoldering site associated with judgment. Jesus quotes this verse three times in Mark 9:44, 46, 48 to describe the fate of the unrighteous. The book of Isaiah closes not with universal triumph alone but with the permanent visibility of judgment — a warning inseparable from the promise.</p>"
}
}

def main():
    existing = load_comm('mkt-context', 'isaiah')
    merge_comm(existing, ISAIAH)
    save_comm('mkt-context', 'isaiah', existing)
    v = sum(len(vs) for vs in ISAIAH.values())
    print(f'Isaiah 66 mkt-context: {v} verses written.')

if __name__ == '__main__':
    main()
