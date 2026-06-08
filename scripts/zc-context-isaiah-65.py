"""
MKT Context Commentary — Isaiah chapter 65
Run: python3 scripts/zc-context-isaiah-65.py

Isaiah 65 is YHWH's answer to the community prayer of 63:7-64:12, which ended with
"Will you keep silent and punish us very severely?" (64:12). The answer distinguishes
between the rebellious and the faithful remnant, then opens into the great new creation
vision (vv.17-25).

The chapter's structural function:
- vv.1-7: Response to the prayer — YHWH has been present, but Israel refused him
- vv.8-16: The distinction speech — the faithful servants and the rebels receive
  opposite outcomes from the same history
- vv.17-25: The new creation — the eschatological horizon that reframes all prior
  judgment and promise

Key reception:
- vv.1-2: Rom 10:20-21 (Paul applies the "found by those who did not seek me"
  to the gentile mission and the "rebellious people" to Israel)
- v.17: Rev 21:1 ("then I saw a new heaven and a new earth")
- v.21-22: The reversal of Deut 28:30 covenant curses
- v.25: Echoes Isaiah 11:6-9 (the peaceable kingdom)
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
  "65": {
    "1": '<p>YHWH\'s response to the community lament (63:7–64:12) opens by reversing the complaint: it was not YHWH who was absent but Israel who was unreachable. The image of YHWH extending his hands and saying "Here I am! Here I am!" (<em>hinnênî hinnênî</em>) to a nation that did not ask is a reversal of the intercessory prayer posture — usually the petitioner cries "Here am I" to the divine call; here YHWH calls and Israel ignores. Paul reads vv.1-2 in Rom 10:20-21 as a textual warrant for the gentile mission — those who "did not ask" are the nations, and Israel is the "disobedient and contrary people." This is a typological inversion that Paul applies to his own experience of gentile receptivity versus Jewish resistance.</p>',
    "2": '<p>The image of YHWH stretching out his hands (<em>pēraśtî yādāy</em>) throughout the day (<em>kol-hayyôm</em>) to a "rebellious people" (<em>ʿam sôrēr</em>) is drawn from the parental posture of patient outstretched welcome. Deut 21:18-21 uses <em>sôrēr</em> for the rebellious son who is to be brought before the elders; YHWH is the parent whose child has become the "rebellious son." The people "walk in the way that is not good" (<em>hahōlĕkîm hadderek lōʾ-ṭôḇ</em>) — the "two ways" tradition of Psalm 1 and Deut 30:15-20 frames the contrast.</p>',
    "3": '<p>The specific indictments of vv.3-5 describe practices of popular religion that competed with orthodox Yahwism in the late exilic and early post-exilic period. "Sacrificing in gardens" (<em>haššōḥăṭîm baggannôt</em>) refers to outdoor shrines associated with fertility cults, possibly connected to Asherah worship. "Burning incense on bricks" (<em>ûmĕqaṭṭĕrîm ʿal-halĕbēnîm</em>) — the specific mention of bricks (a Babylonian building material) may allude to practices borrowed during the exile. The practices represent the syncretism that post-exilic prophets like Malachi and Zechariah also confronted.</p>',
    "4": '<p>"Sitting in tombs" (<em>hayyōšĕḇîm baqqĕḇārîm</em>) and spending nights in hidden places (<em>ûḇannĕṣûrîm yālînû</em>) are necromantic practices — consulting the dead by sleeping at their graves to receive revelatory dreams. The same practice is condemned in 8:19-20 ("should not a people consult their God? Should they consult the dead on behalf of the living?"). "Eating pig\'s flesh" (<em>ʾōkĕlê bĕśar haḥăzîr</em>) violates Lev 11:7-8; Deut 14:8 — a marker of gentile practice adopted by some Israelites. "Broth of unclean things in their vessels" (<em>ûmĕraq piggulîm kĕlêhem</em>) — <em>piggûl</em> is a technical term for sacrificial meat that has been kept past its lawful time (Lev 7:18; 19:7).</p>',
    "5": '<p>"Keep to yourself, do not come near me, for I am holy to you" (<em>qĕḏaštîkā</em>) — this is a parody of the Holiness Code\'s language. In Lev 19:2 and Num 16:5 YHWH declares his own holiness or the holiness of those he chooses; here the idolaters appropriate the holiness-language to exclude others from their rituals, as if their forbidden practices had made them more sacred. The irony is pointed: those who defile themselves most thoroughly claim the greatest purity. The phrase echoes the false prophets condemned in Mic 3:5 and Jer 6:13-14 who cry "peace" when there is no peace.</p>',
    "6": '<p>The divine record-keeping: "behold, it is written before me" (<em>hinnēh kĕtûḇâ lĕpānāy</em>) — the image of a heavenly register where sins are documented awaiting judgment. The phrase "I will not keep silent but I will repay" (<em>kî ʾim-šillmtî wĕlōʾ ʾeḥĕšeh</em>) is particularly significant as it answers the community\'s complaint in 64:12: "Will you keep silent?" YHWH was not silent; he was recording. The repayment will be "into their bosom" (<em>el-ḥêqām</em>) — the breast/bosom was the place where one gathered grain or carried provisions; paying into the bosom means settling the account in full.</p>',
    "7": '<p>The intergenerational accounting: "your iniquities and your fathers\' iniquities together" (<em>ʿăwōnōtêkem wĕʿăwōnōt ʾăḇôtêkem yaḥdāw</em>). The burning incense "on the mountains" (<em>ʿal-hehārîm</em>) and "reviling me on the hills" (<em>ḥērĕpûnî ʿal-haggĕḇāʿôt</em>) describes the high place worship condemned in Hosea 4:13; 2 Kings 17:9-11. The ancestral sin framework does not eliminate individual responsibility but situates it within a generational pattern — the post-exilic community is not starting fresh but continuing a history that must be acknowledged and discontinued.</p>',
    "8": '<p>The grape-cluster parable: "as new wine is found in a cluster" (<em>kaʾăšer yimmāṣēʾ hatîrôš bĕʾeškôl</em>) — the good wine discovered within an otherwise spoiled cluster. The instruction "do not destroy it, for there is a blessing in it" (<em>ʾal tašḥitēhû kî bĕrākâ bô</em>) parallels the decision to spare the remnant from within a largely corrupt community. The grape-cluster image connects to the vineyard parable of ch. 5 (where the vineyard failed to produce good grapes) — now within the failed cluster, YHWH finds the faithful remnant worth preserving.</p>',
    "9": '<p>"I will bring out from Jacob a seed/offspring" (<em>wĕhôṣĕʾtî miyyaʿăqōb zeraʿ</em>) — the remnant as seed (cf. 1:9 "unless YHWH of hosts had left us a very small remnant, we should have been like Sodom"; 6:13 "the holy seed is its stump"). The promise of possessing the mountain (<em>wĕyārĕšâ ʿam hārî</em>) echoes the original conquest language — the return from exile as a new entering-the-land. "My chosen ones shall inhabit it" (<em>ûbĕḥîray yišĕkĕnû-šām</em>) — the election category (<em>bāḥar</em>) that defines the Servant (42:1) now extends to the remnant community.</p>',
    "10": '<p>The specific geography of restoration — Sharon (<em>haššārôn</em>), the coastal plain of central Israel, and the Valley of Achor (<em>ʿēmeq ʿākôr</em>) — provides historical concreteness to the eschatological promises. The Valley of Achor was the place of Achan\'s sin and execution (Josh 7:24-26) — a place of cursed memory. Hosea 2:15 had already promised that the Valley of Achor would become "a door of hope" for the restored remnant. Isaiah here echoes and deepens that promise: the most cursed geography becomes pastoral land for YHWH\'s seeking people.</p>',
    "11": '<p>The fate-deity worship condemned here identifies the specific religious competition in the post-exilic community. "Gad" (<em>gāḏ</em>, H1408) is a deity of fortune or fate known from personal names in the ancient Near East; "Meni" (<em>mĕnî</em>, H4507) is the deity of destiny (possibly related to the word for "portion" or "allotment"). Setting a table for these deities and filling cups of drink-offering for them represents the practice of honoring the deities who control fate — a temptation especially acute in a community of returnees whose survival felt contingent on cosmic powers. YHWH responds: those who chose Fate will receive judgment as their portion.</p>',
    "12": '<p>The wordplay on "Destiny" (<em>mĕnî</em>) and "I will destine/appoint" (<em>mānîtî</em>): you chose the deity of Destiny, so YHWH himself will appoint your destiny — to the sword. The logic reverses the promise: those who worshipped the god of fate receive YHWH\'s direct assignment of their fate. "You did not answer when I called, you did not listen when I spoke" (<em>yaʿan qārāʾtî wĕlōʾ ʿănittem dibbarti wĕlōʾ šĕmaʿtem</em>) — the accusation of non-response echoes 50:2 and 66:4, framing the entire end of Isaiah around the theme of YHWH\'s call and Israel\'s refusal.</p>',
    "13": '<p>The double-destiny discourse of vv.13-16 is structured as a series of antitheses: "my servants shall eat, but you shall be hungry; my servants shall drink, but you shall be thirsty; my servants shall rejoice, but you shall be ashamed." The same history (exile, return, restoration) produces opposite outcomes for those who trusted YHWH and those who did not. This structure anticipates the judgment parables of Jesus in which the same master, the same banquet, the same wedding produces inclusion for some and exclusion for others (Matt 25:1-13; Luke 14:15-24).</p>',
    "14": '<p>"My servants shall sing for joy of heart" (<em>yārōnnû miṭṭûḇ-lēḇ</em>) contrasted with "you shall cry out for pain of heart" (<em>tizʿăqû mimmakʾôḇ-lēḇ</em>). The heart (<em>lēḇ</em>) is the center of the antithesis — the same organ that rejoices or grieves. "From anguish of spirit you shall wail" (<em>ûmišĕḇer rûaḥ tiylîlû</em>) — the <em>šĕḇer</em> (brokenness) of the spirit echoes the "broken spirit" that YHWH does not despise in Ps 51:17; here the spirit\'s brokenness is the consequence of rebellion rather than its cure.</p>',
    "15": '<p>"Your name shall be left for my chosen ones as a curse" (<em>ûhinnãḥtem šĕmĕkem libḥîray lišĕḇûʿâ</em>) — the proper name of the rebellious community becomes the formula of cursing ("YHWH make you like those"), in contrast to the Abrahamic promise in Gen 12:2 ("I will make your name great" as a formula of blessing). "But his servants he will call by another name" — the new name promises covenant renewal; cf. 56:5 (the eunuch\'s everlasting name) and 62:2 (a new name for Jerusalem).</p>',
    "16": '<p>The double formula "whoever blesses himself in the land shall bless himself by the God of truth (<em>ʾĕlōhê ʾāmēn</em>)" — the Hebrew <em>ʾāmēn</em> used as a divine title ("God of Amen/Truth") is unique. This becomes a significant motif in the NT where Jesus begins statements with "Amen, amen I say to you" — the Amen is a divine truth-claim. "The former troubles are forgotten and hidden from my eyes" (<em>kî niškĕḥû haṣṣārôt hārîʾšōnôt wĕkî nistarrû mēʿênāy</em>) — the forgetting of former distress provides the theological basis for the new creation oracle that follows.</p>',
    "17": '<p>"For behold, I create new heavens and a new earth" (<em>hinnî-ḇōrēʾ šāmayim ḥăḏāšîm wĕʾāreṣ ḥăḏāšâ</em>) — the verb <em>bārāʾ</em> (to create) is used exclusively of divine creation in the Hebrew Bible and is the same verb as Gen 1:1. The new creation is not renovation but a creative act of the same order as the original. "The former things shall not be remembered or come to mind" (<em>wĕlōʾ tizzākarenâ hārîʾšōnôt wĕlōʾ taʿălênâ ʿal-lēḇ</em>) — the forgetting of the former world is not amnesia but the eclipse of the old by the overwhelming goodness of the new. Revelation 21:1 ("then I saw a new heaven and a new earth, for the first heaven and the first earth had passed away") and 2 Pet 3:13 ("we are waiting for new heavens and a new earth in which righteousness dwells") both draw on this verse.</p>',
    "18": '<p>"But be glad and rejoice forever in what I create" (<em>kî ʾim-śîśû wĕgîlû ʿăḏê-ʿaḏ ʾăšer ʾănî bôrēʾ</em>) — the new creation is designed for perpetual celebration. "Behold, I create Jerusalem to be a joy and her people to be a gladness" — the recreated Jerusalem is defined by what it produces: joy and gladness. The city is not rebuilt but recreated (<em>bôrēʾ</em>), which means its fundamental character is changed, not merely its condition improved. The specific naming of Jerusalem within the cosmic new creation anchors the universal promise in a particular covenantal location.</p>',
    "19": '<p>"I will rejoice in Jerusalem and be glad in my people" (<em>wĕgaltî bîrûšālaim wĕśaśtî bĕʿammî</em>) — the divine joy complements the human joy of v.18. The mutual joy — YHWH in his people and people in YHWH — is the relational content of the new creation. "The sound of weeping shall be heard no more in it, nor the cry of distress" — the absence of the sounds of mourning defines the new creation negatively. This verse is the immediate background for Rev 21:4 ("he will wipe away every tear from their eyes, and death shall be no more, neither shall there be mourning, nor crying, nor pain").</p>',
    "20": '<p>The new creation\'s altered relationship to death is not the full abolition of death (that appears in 25:8 and Rev 21:4) but a radical extension of life: a person dying at a hundred years old will be considered a youth, and a hundred-year-old sinner will be accounted as one cut off. This intermediate vision — greatly extended life rather than immortality — represents a stage in the eschatological imagination that is developed further in Rev 20:4-6 (the thousand-year reign) before the fully deathless new creation of Rev 21.</p>',
    "21": '<p>"They shall build houses and inhabit them; they shall plant vineyards and eat their fruit" — the exact reversal of the Deuteronomy 28:30 covenant curse: "You shall build a house, but you shall not dwell in it. You shall plant a vineyard, but you shall not enjoy its fruit." The new creation is characterized structurally by the removal of the covenant curses. The Holiness Code\'s blessings (Lev 26:3-13) and curses (26:14-39) have established the framework; the new creation represents the permanent installation of the blessing structure and the permanent elimination of the curse structure.</p>',
    "22": '<p>"They shall not build and another inhabit; they shall not plant and another eat" — the covenant security is expressed through the stable connection between labor and fruit. The simile "for like the days of a tree shall the days of my people be" (<em>kî kimê haʿēṣ yĕmê ʿammî</em>) — the longevity of the great trees (cedar, oak) is the measure of the new creation\'s lifespan. "My chosen ones shall long enjoy the work of their hands" (<em>ûmiḇḥîray yĕballû maʿăśēh yĕḏêhem</em>) — the election theme that framed the remnant theology (vv.9,15) culminates here in the enjoyment of one\'s own labor as the specific content of election\'s blessing.</p>',
    "23": '<p>"They shall not labor in vain or bear children for calamity" (<em>lōʾ yîgĕʿû lāreiq wĕlōʾ yēlĕdû labĕhālâ</em>) — another reversal of the covenant curses (Deut 28:41: "you shall father sons and daughters, but they shall not be yours"). The promise extends to intergenerational blessing: "they and their offspring with them" (<em>hēmmâ wĕzarʿām ʾittām</em>). The "blessed of YHWH" (<em>zereʿ bĕrûkê Yhwh</em>) identity is inheritable — the new covenant blessing flows through generations as the original Abrahamic blessing was designed to do.</p>',
    "24": '<p>"Before they call I will answer; while they are yet speaking I will hear" (<em>wĕhāyâ ṭerem-yiqrĕʾû wĕʾănî ʾeʿĕneh ʿôd hēm mĕḏabbĕrîm wĕʾănî ʾešmaʿ</em>) — the new creation\'s relational register: no more of the silence complaint (63:15; 64:12) or the "I was present and they did not answer" (65:12). The proactive divine responsiveness — answering before the request is complete — represents the fullness of covenantal intimacy. John 16:23-24 ("ask and you will receive") and 1 John 5:14-15 (confidence that God hears) develop this promise further.</p>',
    "25": '<p>The return of Eden\'s harmony between creatures: "the wolf and the lamb shall graze together, the lion shall eat straw like the ox" (<em>zĕʾēḇ wĕṭāleh yirʿû yāḥaḏ wĕʾaryēh kattābên yōʾkal</em>) — identical motifs to 11:6-9 (the peaceable kingdom), where the wolf lies with the lamb and the lion eats straw. The repetition confirms that the new creation and the messianic kingdom are facets of the same eschatological reality in Isaiah\'s vision. "And dust shall be the serpent\'s food" (<em>wĕnāḥāš ʿāpār laḥmô</em>) — the serpent\'s curse from Gen 3:14 ("on your belly you shall go, and dust you shall eat") persists into the new creation. The serpent\'s curse is not reversed but acknowledged — it remains as the permanent memorial of the judgment that was escaped, the one element from the old order that marks the new.</p>',
  },
}

def main():
    existing = load_comm('mkt-context', 'isaiah')
    merge_comm(existing, ISAIAH)
    save_comm('mkt-context', 'isaiah', existing)
    # INTENT: Verify all 25 Isaiah 65 mkt-context verses present against interlinear
    # CHANGE? If interlinear/isaiah.json ch 65 verse count changes, update expected total
    # VERIFY: Console shows OK with 25 verses; no MISSING output
    il = json.loads((ROOT / 'data' / 'interlinear' / 'isaiah.json').read_text())
    out = json.loads((ROOT / 'data' / 'commentary' / 'mkt-context' / 'isaiah.json').read_text())
    missing = [v for v in il.get('65', {}) if v not in out.get('65', {})]
    if missing:
        print(f'  MISSING: {missing}')
    else:
        print(f'  OK: all Isaiah 65 mkt-context verses present ({len(il.get("65", {}))} verses)')

if __name__ == '__main__':
    main()
