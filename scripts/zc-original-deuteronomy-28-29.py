"""
Combined OT Phase 2 script: Deuteronomy, Jeremiah, Ezekiel, Daniel — all four layers.
These four books have the highest NT echo density of all remaining OT books.
"""

import json, pathlib

ROOT = pathlib.Path(__file__).parent.parent

def load_echo(book):
    p = ROOT / 'data' / 'echoes' / f'{book}.json'
    return json.loads(p.read_text()) if p.exists() else {}

def save_echo(book, data):
    p = ROOT / 'data' / 'echoes' / f'{book}.json'
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=None))
    print(f'  wrote {p.relative_to(ROOT)}')

def load_comm(layer, book):
    p = ROOT / 'data' / 'commentary' / layer / f'{book}.json'
    return json.loads(p.read_text()) if p.exists() else {}

def save_comm(layer, book, data):
    p = ROOT / 'data' / 'commentary' / layer / f'{book}.json'
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=None))
    print(f'  wrote {p.relative_to(ROOT)}')

def merge_echo(existing, new_data):
    for ch, verses in new_data.items():
        if ch not in existing:
            existing[ch] = {}
        for v, entries in verses.items():
            if v not in existing[ch]:
                existing[ch][v] = entries
            else:
                seen = {(e['type'], e['target']) for e in existing[ch][v]}
                for e in entries:
                    if (e['type'], e['target']) not in seen:
                        existing[ch][v].append(e)
                        seen.add((e['type'], e['target']))

def merge_comm(existing, new_data):
    for ch, verses in new_data.items():
        if ch not in existing:
            existing[ch] = {}
        for v, html in verses.items():
            if v not in existing[ch]:
                existing[ch][v] = html

# ============================================================
# DEUTERONOMY
# ============================================================

DEUT_ECHO = {
  "6": {
    "4": [
      {"type": "allusion", "target": "Mark 12:29", "note": "Hear O Israel the LORD our God the LORD is one — Jesus cites the Shema (Deut 6:4-5) as the first and greatest commandment; the Shema frames the entire law in the context of YHWH's singular Lordship over Israel"},
      {"type": "allusion", "target": "1 Cor 8:6", "note": "One God the Father from whom are all things and one Lord Jesus Christ through whom are all things — Paul's expansion of the Shema incorporates Jesus into the divine identity: the 'one Lord' of the Shema is now differentiated into Father and Son"}
    ]
  },
  "18": {
    "15": [
      {"type": "fulfillment", "target": "Acts 3:22", "note": "A prophet like me will the LORD your God raise up for you — Peter cites Deut 18:15 as fulfilled in Jesus; the eschatological prophet-like-Moses was the figure Israel expected, and Peter declares Jesus to be that prophet"},
      {"type": "fulfillment", "target": "Acts 7:37", "note": "God will raise up for you a prophet like me from your brothers — Stephen's speech identifies the prophet-like-Moses promise as the Christological center of Moses's ministry; Israel's rejection of Moses typifies their rejection of Jesus"}
    ]
  },
  "21": {
    "23": [
      {"type": "fulfillment", "target": "Gal 3:13", "note": "Cursed is everyone who hangs on a tree — Paul cites Deut 21:23 as fulfilled in the crucifixion: Christ redeemed us from the curse of the law by becoming a curse for us, for cursed is everyone who hangs on a tree; the cross is the site of curse-absorption"}
    ]
  },
  "30": {
    "12": [
      {"type": "allusion", "target": "Rom 10:6-8", "note": "Do not say in your heart who will go up to heaven — Paul adapts Deut 30:12-14 Christologically: the word that is near you, in your heart and mouth, is the word of faith we proclaim; what Deuteronomy said of the Torah-command is now said of Christ and his gospel"}
    ]
  },
  "32": {
    "21": [
      {"type": "fulfillment", "target": "Rom 10:19", "note": "I will make you jealous of those who are not a nation — Paul cites the Song of Moses (Deut 32:21) as the OT basis for the Gentile mission provoking Israel to jealousy; the unexpected reversal of Gentile blessing is Moses's own warning"}
    ],
    "43": [
      {"type": "fulfillment", "target": "Rom 15:10", "note": "Rejoice O Gentiles with his people — Paul cites Deut 32:43 LXX as one of four OT texts (Rom 15:9-12) proving that Gentile inclusion in the worship of God was always the divine plan from Moses through the Psalms and Isaiah"}
    ]
  }
}

DEUT_ORIGINAL = {
  "28": {
    "1": "<p><strong>shamoa tishma</strong> (<em>šāmōaʿ tišmaʿ</em>): the emphatic infinitive absolute + imperfect construction intensifies the condition — 'if you truly, fully, obedient-hearing hear.' This is not cursory compliance but complete covenantal attention. The promised result: YHWH will set you <em>elyon</em> (highest, uppermost) over all nations. The blessing section (vv1-14) frames obedience as the precondition for the blessings that YHWH then actively sends. Passivity on Israel's part (hearing, following) generates divine action (setting high, sending blessings).</p>",
    "2": "<p><strong>hissigucha</strong> (<em>wĕhissîgûkā</em>): 'will overtake you' — the blessings are not merely available but pursuing; they hunt down the obedient like an enemy pursues a retreating army. The same verb (<em>nasag</em>) is used of enemies overtaking Israel in the curse section (v15). Whether you are overtaken by blessings or curses depends entirely on covenantal orientation. The reversal of the verb in v15 makes the structural symmetry explicit: blessings and curses are not different categories but the same covenantal mechanism applied in two directions.</p>",
    "3": "<p><strong>baruch atta ba'ir uvaruch atta basadeh</strong>: 'blessed in the city and blessed in the field' — the spatial blessing covers both domains of Israelite life: the urban (city, commerce, assembly) and the rural (field, agriculture, livestock). No place of Israelite existence falls outside the blessing sphere. The city-field pair is a merism: the whole of life. Verse 16 mirrors this exactly with the curse.</p>",
    "4": "<p>The three domains of fruitful production: <em>peri bitnecha</em> (fruit of your womb/body — children), <em>peri adamatecha</em> (fruit of your ground — crops), <em>peri behemtecha</em> (fruit of your livestock — herds and flocks). The threefold fruitfulness mirrors the creation mandate (be fruitful, multiply, fill the earth) and the Abrahamic promises. Blessing is never abstract but always bodied — in children, harvests, and animals.</p>",
    "5": "<p><strong>tene</strong> (<em>ṭenĕʾ</em>) and <strong>misharetech</strong> (<em>mišʾarteṯ</em>): 'basket' and 'kneading bowl' — the two vessels of food processing: the basket that carries grain to market and the bowl that processes it into bread. The blessing reaches into the most domestic and practical points of daily life. No part of the food cycle escapes covenantal significance.</p>",
    "6": "<p><strong>bevo'acha uvetzetecha</strong> (<em>bĕbōʾĕkā ûbĕṣēʾṯĕkā</em>): 'in your coming in and your going out' — the temporal merism completing the spatial one in v3: all activities, all movements, all moments of daily life enclosed within the blessing. This formula appears in the Aaronic blessing structure; it expresses comprehensive coverage rather than specific circumstances.</p>",
    "7": "<p><strong>negifu lifneicha</strong> (<em>nĕgûpîm lipnêkā</em>): 'defeated/struck before you' — the military blessing; YHWH is the primary combatant. The coming-from-one-direction/fleeing-in-seven pattern inverts exactly in v25 for the curse: the seven-to-one ratio in battle describes either overwhelming military dominance or complete military collapse. The number seven marks totality.</p>",
    "8": "<p><strong>yetzav YHWH ittecha et-habrakha ba'asameicha</strong>: 'the LORD will command the blessing to be with you in your storehouses' — blessing is not an impersonal force but a divine command; YHWH orders it to attach to specific locations of human labor and storage. The blessing is <em>commanded</em> (from <em>tzavah</em>), not merely granted or released — a word of royal authority dispatching the blessing to its assigned destination.</p>",
    "9": "<p><strong>yequimecha YHWH lo le'am qadosh</strong> (<em>yĕqîmĕkā Yhwh lô lĕʿam qādôš</em>): 'the LORD will establish you as his holy people' — <em>qadosh</em> (holy, set apart) is not primarily a moral category but a relational one: belonging to YHWH, separated for his purposes. The establishment (<em>qum</em> hiphil) is covenant-constituting action; YHWH makes Israel what they are called to be through the covenant itself. The condition (<em>im tishmor...</em>) grounds holiness in obedience, not in natural or ethnic identity.</p>",
    "10": "<p><strong>ki shem YHWH nikra alecha</strong> (<em>kî šem Yhwh niqrāʾ ʿālêkā</em>): 'because the name of YHWH is called over you' — the name-bearing formula; to have YHWH's name called over you is to belong to him, to bear his identification. The Aaronic blessing ends by YHWH putting his name on Israel (Num 6:27). The result: the nations stand in awe (<em>yare'u</em>). The covenant community's holiness functions as a witness to YHWH's reality among the nations.</p>",
    "11": "<p><strong>hoterekha YHWH letovah</strong> (<em>wĕhôṯirĕkā Yhwh lĕṭôbāh</em>): 'the LORD will make you overflow with good things' — <em>hotir</em> means to leave a surplus, to make abundant; the land gives more than enough. The threefold abundance (body, livestock, ground) repeats the pattern of v4; the Abrahamic promise of multiplication finds agricultural and demographic expression in the land.</p>",
    "12": "<p><strong>et-otzaro hatov et-hashamayim latet matar artzecha be'ito</strong>: 'his good storehouse — the heavens — to give rain to your land in its season' — the heavenly storehouse (<em>otzer</em>): YHWH controls the water supply through a treasury in the sky; rain is not a natural phenomenon but a covenantal allocation. The lend/borrow inversion (you will lend to many, borrow from none) transforms the Exodus refugee into a creditor-nation: abundance that can share its surplus.</p>",
    "13": "<p><strong>rosh velo zanav</strong> (<em>rōʾš wĕlōʾ zānāb</em>): 'head and not tail' — the head-tail image for social and political leadership versus dependency/subjection. The exact reversal in v44 (the foreigner as head, Israel as tail) makes clear what is at stake: covenantal obedience determines whether Israel leads or follows. Isaiah's polemic against Egypt uses the same image (Isa 9:14-15).</p>",
    "14": "<p>The negative conditional frames the blessing: <em>im lo tasur... yamin usmol</em> ('if you do not turn aside to the right or to the left'). The spatial metaphors of deviation — turning right or left from the covenant path — appear throughout Deuteronomy as the image of apostasy. The specific form of apostasy here: going after other gods to serve them. Covenant faithfulness is monotheistic fidelity in embodied practice.</p>",
    "15": "<p><strong>im-lo tishma beqol YHWH</strong> (<em>ʾim-lōʾ tišmaʿ bĕqôl Yhwh</em>): 'if you do not listen to the voice of YHWH' — the curse-section opens with the precise inversion of the blessing-condition: where v1 says <em>shamoa tishma</em> (if you truly hear), v15 says <em>im-lo tishma</em> (if you do not hear). The structural parallel is deliberate; the same covenant mechanism operates in reverse. The curses will <em>come upon you and overtake you</em> (<em>uvisigucha</em>) — the same overtaking-verb as the blessings (v2), now carrying curses.</p>",
    "16": "<p>The curse-mirror of v3: <em>arur atta ba'ir ve'arur atta basadeh</em> ('cursed in the city and cursed in the field'). The identical spatial merism now bears the covenant curse. The symmetry is perfect: the same verse structure, the same coverage of all space, the same comprehensive claim — reversed in valence. The curse is not a different covenant but the same covenant's opposite pole.</p>",
    "17": "<p>The curse-mirror of v5: basket and kneading bowl cursed. Where the blessing reaches into the vessels of food production, the curse contaminates those same vessels. The domestic and practical is never neutral in Deuteronomy; it is always covenantally charged.</p>",
    "18": "<p>The curse-mirror of v4: womb, ground, herds, flocks — all three domains of fruitfulness now under the curse. Miscarriage, drought, livestock death — the Deuteronomic curses will be fulfilled in Israel's historical experience. The agricultural failures of the prophetic era read as the specific actualization of this verse.</p>",
    "19": "<p>The curse-mirror of v6: cursed coming in and cursed going out. The temporal merism of all activity now under the curse. No movement, no undertaking, no moment of daily life escapes the curse's reach — exactly as no moment escaped the blessing's reach. The totality is symmetrical.</p>",
    "20": "<p><strong>meera</strong> (<em>mĕʾērāh</em>): 'disaster/curse' — not the standard <em>arar</em> (curse) but the noun <em>meera</em>, the curse-substance itself; <strong>mehumah</strong> (<em>mĕhûmāh</em>): 'confusion, panic'; <strong>migeeret</strong> (<em>migĕreʿeṯ</em>): 'rebuke, frustration' — three negative forces YHWH dispatches against the apostate. The root cause: <em>asher azavtani</em> ('because you abandoned me') — the curse is named as the consequence of relational abandonment, not mere rule-violation.</p>",
    "21": "<p><strong>yadvek YHWH becha et-hadaver</strong> (<em>yadbiqqĕkā Yhwh bāddāber</em>): 'the LORD will cling to you with plague/pestilence' — the irony of <em>davaq</em> here: the same verb used for the covenant-love of cleaving (Deut 10:20, 11:22) now applied to plague clinging to the covenant-breaker. What should have been covenant-adhesion (cleaving to YHWH) becomes plague-adhesion (pestilence cleaving to Israel).</p>",
    "22": "<p>The catalog of natural afflictions — <em>shachefet</em> (tuberculosis/wasting disease), <em>qaddachat</em> (fever), <em>dalleket</em> (inflammation), <em>charcharah</em> (scorching heat), <em>cherev</em> (drought/sword), <em>shiddafon</em> (blight), <em>yerakon</em> (mildew/jaundice). The seven afflictions form a complete curse-catalog; the natural world itself becomes YHWH's instrument of covenant enforcement.</p>",
    "23": "<p><strong>venehyu shameicha asher al-roshecha nechoshet veha'aretz asher tachteicha barzel</strong>: 'the sky above you will be bronze and the ground beneath you iron' — two of the most prized metals (used for weapons and tools) become images of impenetrability: the sky seals shut against rain, the ground hardens against cultivation. The productivity of v7-12 (from YHWH's treasure-storehouse to the earth's abundance) is reversed: both sky and ground become barriers rather than channels of provision.</p>",
    "24": "<p><strong>yeiten YHWH et-matar artzecha avaq ve'afar</strong>: 'the LORD will turn the rain of your land into dust and powder' — the inversion of the agricultural covenant; instead of water from the heavenly storehouse, dust falls. The dust-rain is both literal (drought causing topsoil loss) and covenantally symbolic: the land given to Abraham's seed returns to the pre-creation condition of formlessness (<em>tohu</em>).</p>",
    "25": "<p>The military inversion of v7: <em>yittencha YHWH niguph lifnei oyeveika</em> ('the LORD will cause you to be struck/routed before your enemies'). Where v7 says enemies flee in seven directions, here Israel flees in seven directions from enemies. <em>Vezayat lizivaah</em> ('you will become a thing of horror'): <em>za'avah</em> is a trembling/shaking caused by terror; Israel becomes the object that causes nations to shudder in horror — not from awe but from revulsion at their fate.</p>",
    "26": "<p><strong>vehayta nivlatecha lema'achal le'of hashamayim ulivhemot ha'aretz</strong>: 'your bodies will become food for birds of the sky and animals of the earth' — burial was a fundamental covenant marker; the unburied corpse was the ultimate disgrace and the sign of covenant abandonment. The prophets use this image repeatedly for Jerusalem's judgment (Jer 7:33, 8:1-2; Ezek 29:5). The absence of a burier (<em>ein macharid</em>) marks total social collapse.</p>",
    "27": "<p><strong>yakkecha YHWHbishchin Mitzraim</strong>: 'the LORD will strike you with the boils of Egypt' — Egypt's diseases returning to the people YHWH brought out of Egypt; the covenant reversal takes the form of a return to the condition of pre-redemption. The diseases YHWH inflicted on Egypt for refusing to release Israel now fall on Israel for refusing covenant fidelity.</p>",
    "28": "<p><strong>shigga'on</strong> (<em>šiggāʿôn</em>): 'madness'; <strong>ivaron</strong> (<em>ʿiwwārôn</em>): 'blindness'; <strong>timhon levav</strong> (<em>timmāhôn lēbāb</em>): 'confusion/bewilderment of heart/mind' — the cognitive and psychological curses; not only external disaster but internal disintegration. The mind that refused covenant wisdom now loses coherent reality-apprehension. Isaiah 59:10 echoes this verse directly.</p>",
    "29": "<p><strong>umishshesh batzohorayim ka'asher yemashesh ha'iver ba'afelah</strong>: 'at midday you will grope like a blind man in the dark' — the paradox of midday blindness: the one who should have covenant clarity (standing in full light of YHWH's revelation) gropes in darkness. The three verbs of failure: <em>lo tatliach</em> (you will not succeed), <em>ashak ve'gazul</em> (you will be oppressed and robbed), <em>ein moshia</em> (no one to save). The absence of a savior (<em>moshia</em>) is the covenant curse's most pointed dimension: the one who is not saved is the one who abandoned the Savior.</p>",
    "30": "<p>The dispossession triad: wife taken by another man, house built but not inhabited, vineyard planted but fruit not enjoyed. <strong>Techallelnah</strong> (<em>tĕḥallelennāh</em>): 'will violate/defile her' — sexual violation is the first in the list, the most intimate sphere of life. Then shelter (house), then sustenance (vineyard). The progressive loss moves from the most personal to the material; the covenant-breaker becomes an alien in his own construction.</p>",
    "31": "<p>Agricultural dispossession continues: ox slaughtered before your eyes but you eat none, donkey seized and not returned, sheep surrendered to enemies with no rescuer. The animals that worked the land are taken; the livestock that marked prosperity are stripped. The seeing-without-receiving pattern recurs — <em>lefaneicha</em> (before your eyes) — making the loss a witnessed experience, not a hidden one.</p>",
    "32": "<p><strong>baneicha u-venoteicha nettunim le'am acher</strong>: 'your sons and daughters given to another people' — the generational horror of the exile; children given to foreigners while parents watch helplessly (<em>ve'eineicha ro'ot vekalot aleihem kol-hayom</em>, 'your eyes looking and longing for them all day long'). <em>Ve'ein le'el yadecha</em> ('and there is nothing your hand can do') — the covenant curse strips power precisely from those who used power autonomously rather than dependently. The Babylonian exile is the historical fulfillment.</p>",
    "33": "<p><strong>peri adamatecha vekhol-yegiecha tokhal am asher lo-yadatah</strong>: 'a people you did not know will eat the fruit of your ground and all your labor' — the productivity that YHWH blessed in vv1-14 is consumed by an unknown foreign nation. The fruit of the land and the labor of hands — the two components of prosperity — become provision for enemies. Deuteronomy's economic theology: what is received as gift can be taken as judgment.</p>",
    "34": "<p><strong>vehayita meshugga</strong> (<em>wĕhāyîṯā mĕšuggāʿ</em>): 'you will be driven mad by what you see' — <em>meshugga</em> is the state of madness from sustained horror; the seeing-without-rescue pattern (begun in vv30-33) generates madness. The covenant curse works through psychological devastation as much as material loss: the mind breaks under the accumulation of witnessed helplessness.</p>",
    "35": "<p>The boil-curse becomes comprehensive: <em>mishoch raglecha ve'ad kodkodecha</em> ('from the sole of your foot to the crown of your head') — the full-body coverage; no inch of the physical person escapes. Job's condition (Job 2:7) is an individual parallel; the Deuteronomic curse applies this body-devastation nationally. The incurability is emphasized: <em>lo tukhal lehirapha</em> ('you will not be able to be healed').</p>",
    "36": "<p><strong>yolikha YHWH ve'et-malkecha asher taqim alecha</strong>: 'the LORD will drive you and the king you set over you' — the king is specifically included; covenant curse falls on the entire institutional structure, including the monarchy. <em>El-goy asher lo-yadatah atah va'avoteicha</em> ('to a nation unknown to you or your fathers') — the exile destination is described by its foreignness; Babylon exceeds all Israel's prior experience. There they will serve wood-and-stone gods — the ultimate covenant inversion: the people of the living God worshipping inert material.</p>",
    "37": "<p><strong>mashal ushinah vetanah</strong>: 'a byword, a mocking taunt, and a proverb' — three words for mockery; Israel-in-exile becomes the reference point for disaster, the go-to illustration of catastrophe among nations. This is the inverse of v10 (nations in awe of Israel bearing YHWH's name): rather than inspiring fear-reverence, Israel now inspires ridicule. The covenant's public witness function works in both directions.</p>",
    "38": "<p>The agricultural curses begin — sowing much, harvesting little (<em>zera rav totzi hasadeh ume'at ta'asof ki yachselen haarbe</em>): the locust-curse. Every agricultural investment returns diminished; the land that was to give abundantly becomes a ground of futility. Haggai 1:6 echoes this precise pattern as the condition of the post-exilic community still under covenant judgment.</p>",
    "39": "<p>The vine-curse: planting vineyards but drinking no wine, gathering no grapes, because worms eat them. The <em>shamir</em> (worm/grub) consumes from within what external enemies could not reach. Internal corruption mirrors internal covenantal failure; the covenant-breaker's crop is eaten from the inside.</p>",
    "40": "<p>The olive-curse: olive trees throughout the land but no oil to use, because olives fall prematurely. Oil was fuel, cosmetic, and medicinal; the olive curse strikes health, light, and festivity simultaneously. The <em>yishol</em> (shall shed/drop off) is the term for premature falling — the fruit never matures.</p>",
    "41": "<p>The generational curse returns: sons and daughters, but not kept — <em>ki yelchu bashvi</em> ('because they go into captivity'). The most fundamental expression of covenant blessing — children to carry forward the name and the land — becomes the most pointed curse: children taken into captivity. The Babylonian exile is precisely this: the generation born in the land taken to the empire.</p>",
    "42": "<p>The locust-comprehensive curse: <em>kol-etzecha u-feri admatecha</em> ('all your trees and the fruit of your ground') — total agricultural devastation. Verses 38-42 form a systematic elimination of the seven-species abundance promised in ch 8: every productive category of the land stripped. Joel 1 describes the locust-plague as covenant curse in its full force.</p>",
    "43": "<p><strong>hager asher beqirbecha ya'aleh alecha ma'la ma'la</strong>: 'the foreigner living among you will rise higher and higher' — the exact social inversion of the covenant blessing. Verse 12 promised Israel would lend to nations, borrow from none; v43-44 reverses this: the resident foreigner (<em>ger</em>) becomes the creditor, Israel the debtor. <em>Atah tashkeh shafal shafal</em> ('you will sink lower and lower') — the superlative doubled: absolute social descent.</p>",
    "44": "<p>The head-tail reversal completing v13: the <em>ger</em> (foreigner) as head, Israel as tail. The social order ordained in the covenant (Israel leading, nations following) inverts completely under the curse. This is not merely economic reversal but covenantal testimony: the watching nations see Israel under a curse more severe than any they bear.</p>",
    "45": "<p><strong>uba'u alecha kol-haqelalot ha'eleh</strong>: 'all these curses will come upon you and pursue and overtake you' — the summary verse; the same overtaking-language as the blessing-summary (v2). The curses pursue with the same relentless energy as the blessings would have; there is no escape, only the question of which set of covenantal consequences pursues you. <em>Ad hishamedeha</em> ('until you are destroyed') — the terminal point of the curse-sequence is extinction from the land.</p>",
    "46": "<p><strong>vehayu vecha le'ot ulemo'fat</strong> (<em>wĕhāyû bĕkā lĕʾôṯ ûlĕmôpēṯ</em>): 'they will be a sign and a wonder in you' — the covenant curses become <em>otot umoftim</em>, signs and wonders, in/on Israel. These are the same terms for the Exodus miracles (Exod 7:3; Deut 4:34): YHWH's signs and wonders brought Israel out of Egypt; the curses become counter-signs and counter-wonders that testify to covenant-judgment as clearly as the Exodus testified to covenant-salvation. The watching nations read Israel's devastation as divine text.</p>",
    "47": "<p><strong>tachat asher lo avadeta et-YHWH Eloheicha besimcha uvtuv levav</strong>: 'because you did not serve the LORD your God with joy and gladness of heart' — this is the most theologically penetrating verse in the curse section: the root of all the curses is not spectacular apostasy but joyless religion. The covenant life is meant to be served (<em>aved</em>) with <em>simcha ve-tuv levav</em> (joy and goodness of heart); when prosperity becomes grounds for obligation without gratitude, the spiral begins. Paul's <em>godliness with contentment is great gain</em> (1 Tim 6:6) is the NT reformulation of this principle.</p>",
    "48": "<p><strong>ol barzel</strong> (<em>ʿōl barzel</em>): 'an iron yoke' — the military subjugation described in material terms; the iron yoke (versus the wooden yoke of lighter vassalage) represents permanent and unbreakable servitude. The four conditions of the enemy's service — hunger, thirst, nakedness, and want (<em>bera'av uvattzama uveirummah uvechesar kol</em>) — are the precise inversion of the abundance promised in vv1-14 (eating to full, clothed, no want). Babylon as iron yoke is Jeremiah's primary metaphor (Jer 28:13-14).</p>",
    "49": "<p><strong>yissa YHWH alecha goy merachok</strong>: 'the LORD will bring against you a nation from far away' — the eagle-nation (<em>ka'asher yide'ah nesher</em>, 'swooping like an eagle'). Babylon is consistently described as an eagle in the prophets (Jer 48:40; Ezek 17:3); the Babylonian standards bore eagle imagery. <em>Asher lo-tishma leshono</em> ('whose language you will not understand') — linguistic alienation as a dimension of the covenant curse; Isa 28:11 and 33:19 use incomprehensible speech as a sign of judgment.</p>",
    "50": "<p><strong>goy az panim</strong> (<em>gôy ʿaz pānîm</em>): 'a fierce/brazen-faced nation' — shameless, unrestrained in cruelty. <em>Asher lo-yissa panim lezaqen ve'naar lo yachanun</em> ('who shows no respect to the old or mercy to the young') — the complete violation of natural social order; both the elderly (deserving respect) and the young (deserving protection) are equally unprotected. Babylon's siege warfare fulfilled this precisely.</p>",
    "51": "<p>The comprehensive agricultural stripping: grain (<em>dagan</em>), new wine (<em>tirosh</em>), olive oil (<em>yitzhar</em>), livestock calves and lambs — every category of the seven-species abundance systematically taken. The list of what the enemy will take is the exact reverse of what YHWH's abundance provided. Deuteronomy's agricultural theology is concrete: the specific bounties that obedience unlocks are the specific provisions that disobedience removes.</p>",
    "52": "<p>The siege of the fortified cities — the <em>chomot gebohot u-vetzu'ot</em> ('high, fortified walls') in which Israel trusted prove inadequate. The trust-in-walls is itself a form of covenant displacement: trusting the city's defenses rather than YHWH's protection. Jeremiah's temple-sermon (Jer 7:4, 'these are deceptive words: the temple of YHWH') applies the same logic to the temple as a false-security object.</p>",
    "53": "<p><strong>ve'akhalta pri bitnecha</strong>: 'you will eat the fruit of your womb' — the most horrific curse in Deuteronomy: cannibalism of one's own children in the siege's final extremity. <em>Peri bitna</em> (fruit of her womb) is used in v4 for the supreme blessing; here the same phrase describes the ultimate curse. The historical fulfillment occurred at the fall of Jerusalem (Lam 4:10; 2 Kgs 6:28-29). The covenant's comprehensive claim on human existence means that its most extreme curses reach into the most intimate biological relationships.</p>",
    "54": "<p>The siege-stinginess (<em>ra ayin</em>, 'evil/grudging eye') of the most refined man — the <em>rak ve-anugah</em> ('tender and delicate') who in normal life is generous now refuses to share even with his beloved wife and children. The curses strip social and familial bonds: prosperity enables generosity; the extremity of the curse makes even the most civilized man a hoarder of horror.</p>",
    "55": "<p>The inversion of covenant sharing: the tender man refuses to share the flesh he is eating — his own child's flesh — because <em>ein lo kol</em> ('he has nothing left'). The scarcity generated by the siege reverses every impulse of familial affection. Lamentations 4:3-10 describes precisely this horror as the fulfillment of these curses in 586 BCE.</p>",
    "56": "<p>The <em>raka veha'anugah</em> ('delicate and sensitive woman') — the one so refined she never placed her sole on the ground — counterpart to v54's man. The covenant curse reaches the most sheltered and protected member of society; no social insulation prevents the curse's penetration.</p>",
    "57": "<p>The woman's extremity: eating the afterbirth (<em>shiltah</em>) and the children she bears (<em>biladeiha asher teled</em>) in secret, because of the siege's absolute need. The secrecy — <em>beseter</em> — indicates that even in the horror she knows the act is abominable; the curse has not removed moral awareness but has overwhelmed moral capacity. This is the absolute nadir of the curse-sequence: the covenant community that was to eat the covenant meal in joy has been reduced to consuming its own progeny in secrecy.</p>",
    "58": "<p><strong>et-hashem hanichbad ve-hanora hazeh et-YHWH Eloheicha</strong>: 'this glorious and awesome name — the LORD your God' — the pivot verse; the basis of the curse is explicit: failure to fear <em>this name</em>. The <em>nora</em> (awesome, feared) name is the one that the covenant community should have feared; instead they feared other gods. Isaiah 57:11 uses the same vocabulary: 'whom have you so feared and dreaded that you have not been faithful to me?' The awesome name demands a corresponding awe-response; its absence generates all that precedes in this chapter.</p>",
    "59": "<p><strong>peliot</strong> (<em>pĕliʾōṯ</em>): 'extraordinary, wondrous/severe' — the curses become exceptional in their intensity and duration (<em>makot gedolot ve'ne'emanot vecholayim ra'im ve'ne'emanim</em>: 'great and persistent plagues and terrible and persistent diseases'). The word <em>ne'eman</em> (faithful, persistent) normally describes YHWH's faithfulness to the covenant; here it describes the faithful persistence of judgment. The same divine reliability that sustains blessing sustains curse.</p>",
    "60": "<p><strong>veheshiv becha et kol madveh Mitzraim</strong>: 'he will bring back to you all the diseases of Egypt' — the return of Egypt's plagues on Israel. The exodus was from Egypt's diseases (<em>madveh</em>); covenant apostasy reverses the direction: the diseases return with the people. The feared diseases of Egypt (<em>asher yagortah</em>, 'which you dreaded') were Israel's pre-covenant experience; they become post-apostasy reality. The restoration of pre-exodus conditions is the covenant curse's historical logic.</p>",
    "61": "<p><strong>gam kol-choli ve'kol-makkah asher lo katub besefer ha-Torah hazeh</strong>: 'every sickness and plague not recorded in this Book of the Law' — the curse is not limited to the specific items enumerated; YHWH reserves the right to execute covenant justice beyond the enumerated list. The <em>sefer ha-Torah</em> (Book of the Law) is here mentioned as the covenant document; the written text is the basis of covenant accountability. Deuteronomy's self-awareness as a written document is explicit.</p>",
    "62": "<p><strong>venishaartem bimtei me'at tachat asher heyitem kekochvei hashamayim larov</strong>: 'you who were as numerous as the stars will be left few in number' — the Abrahamic promise reversed. Genesis 15:5 promised Abraham's descendants as numerous as the stars; Deuteronomy 28:62 describes the same stellar analogy now marking the before-state of a people reduced to remnant by covenant curse. The population arithmetic of divine faithfulness (multiplication in blessing, reduction in judgment) is one of the most concrete ways the OT speaks about theological realities.</p>",
    "63": "<p><strong>ka'asher sas YHWH aleichem leheitiv etkhem uleharboth etkhem ken yasis YHWH aleichem le'havid etkhem velehashmiid etkhem</strong>: 'just as the LORD delighted in making you prosperous and multiplying you, so he will delight in bringing you to ruin and destruction' — the startling covenant symmetry: YHWH's delight (<em>sus</em>) operates in both directions. The same divine pleasure that drove the blessing program drives the curse program; YHWH is not reluctantly cursing but covenantally delighted in covenant-consistency. This is the theological paradox that the prophets wrestle with: YHWH's wrath is not his reluctant default but his active, covenant-consistent will.</p>",
    "64": "<p><strong>vehefiztecha YHWH bekhol-ha'ammim miqtzeh ha'aretz ve'ad qetzeh ha'aretz</strong>: 'the LORD will scatter you among all peoples from one end of the earth to the other' — the Diaspora as divine decree. The scattering (<em>hefitz</em>) is YHWH's action, not merely a political accident. The wood-and-stone gods of v36 recur here: in exile, Israel will serve the gods they chose over YHWH — the covenant curse is that YHWH gives them what they wanted. Romans 1:24-28 applies this same logic to idolatry.</p>",
    "65": "<p><strong>lo-tashqot velo-yihyeh manoach lechaf raglecha</strong>: 'you will find no rest and no resting place for the sole of your foot' — the anti-Sabbath; where the covenant promised rest (<em>menucha</em>, Deut 3:20, 12:9-10), the curse denies rest entirely. The psychological dimensions: <em>lev ragaz</em> (trembling/anxious heart), <em>kilyon einayim</em> (failing eyes), <em>deva'on nefesh</em> (anguish/pining of soul) — the whole inner person disintegrated.</p>",
    "66": "<p><strong>vechayu chayeicha taluyim lecha mineged</strong>: 'your life will hang before you in the balance' — the constant uncertainty of physical survival under oppression; the covenant community that had assured inheritance now has no certainty of tomorrow. <em>Ufachdata laylah veyomam velo ta'amin bechayeicha</em> ('you will dread night and day and have no assurance of your life') — the existential anxiety that replaces covenant security.</p>",
    "67": "<p>The morning-evening wish-reversal: <em>baboker tomar mi-yitein erev</em> ('in the morning you will say: if only it were evening') and <em>ba'erev tomar mi-yitein boker</em> ('in the evening you will say: if only it were morning') — the complete temporal desolation. No part of the day brings relief; each time-horizon holds terror. This is the exact opposite of Psalm 30:5's <em>weeping may endure for a night, but joy comes in the morning</em> — under the curse, neither morning nor evening brings joy.</p>",
    "68": "<p><strong>ve'etichem YHWH Mitzraimah ba'oniyot</strong>: 'the LORD will send you back to Egypt in ships' — the definitive covenant reversal: the Exodus undone. Going back to Egypt by ships intensifies the reversal; the Exodus was a land journey, miraculously through the sea; the return is a maritime deportation, a slave cargo. <em>Ve-hitnmakhartem sham le'oyeveichem la'avadim ule'shifchot ve'ein qoneh</em> ('you will offer yourselves for sale as slaves, but no one will buy you') — the ultimate degradation: not even worth the price of a slave.</p>"
  },
  "29": {
    "1": "<p><strong>eleh divrei ha-berit asher tzivvah YHWH et-Mosheh liwrot im-benei Yisrael be'eretz Mo'av</strong>: 'these are the words of the covenant the LORD commanded Moses to make with the Israelites in the land of Moab' — the Moab covenant is explicitly identified as <em>levad ha-berit asher karat itam be-Chorev</em> ('in addition to the covenant made with them at Horeb'). Not a replacement but a supplement; the covenantal structure grows but the Sinai foundation remains. The treaty-renewal form is attested in ancient Near Eastern treaty practice: covenants could be renewed or extended without canceling the original.</p>",
    "2": "<p><strong>atem re'item</strong> (<em>ʾattem rĕʾîtem</em>): 'you have seen with your own eyes' — eyewitness testimony as the basis for covenant accountability; what Israel has <em>seen</em> constitutes their epistemic obligation. The appeal to <em>ra'ah</em> (to see, to witness) recurs throughout Deuteronomy as the covenant's evidentiary foundation. Moses summarizes the entire Egypt-to-Moab experience as what they have seen: they cannot claim ignorance.</p>",
    "3": "<p><strong>ha-massot ha-gedolot ha'otot ve-ha-mofiim ha-gedolim ha-hem</strong>: 'the great trials, the signs and wonders' — the standard Exodus vocabulary: <em>massot</em> (tests/trials, from the same root as Massah — testing-place), <em>otot</em> (signs), <em>mofiim</em> (wonders). The covenant is founded on demonstrated divine power; the signs and wonders are not incidental accompaniments but constitutive covenant-establishing events. They cannot be unknown; they were <em>asher ra'u eineicha</em> ('which your eyes have seen').</p>",
    "4": "<p><strong>velo-natan YHWH lachem lev lada'at ve'einayim lir'ot ve'oznaim lishmo'a ad hayom hazeh</strong>: 'yet the LORD has not given you a heart to understand or eyes to see or ears to hear, to this very day' — the most anthropologically striking verse in Deuteronomy 29. Despite seeing the Exodus miracles (vv2-3), Israel lacks the divinely given perceptual apparatus to understand what they witnessed. Paul quotes this verse in Romans 11:8 (citing a combination of Deut 29:4 and Isa 29:10) to explain Israel's partial hardening. The <em>natan</em> (given) makes YHWH the agent of both revelation and non-understanding; the capacity to receive revelation is itself a divine gift.</p>",
    "5": "<p>The wilderness provision repeated in summary: forty years, clothing that did not wear out, sandals that did not wear out (<em>na'alechem lo valu me'al ragleikem</em>). The miracle of preservation is the covenant's educational program (<em>lema'an tede'u ki Ani YHWH Eloheichem</em>, 'so that you would know that I am the LORD your God'). The purpose of miracle is <em>da'at YHWH</em> — knowing YHWH — not abstract information but relational covenant knowledge.</p>",
    "6": "<p><strong>lechem lo akhally veyayin ve-shechar lo shtitem</strong>: 'you ate no bread and drank no wine or strong drink' — the wilderness diet defined by what it lacked; Israel's food was manna, water from the rock, not normal agricultural produce. The absence of normal food and drink is itself a theological statement: Israel lived on divine provision alone, not on their own agricultural labor. This is the preparatory education for the land's abundance: dependence before possession.</p>",
    "7": "<p>The military history condensed: Sihon of Heshbon and Og of Bashan came out to fight and were defeated. The covenant-victories over Transjordanian kings are the concrete evidence of YHWH's covenant-fighting on Israel's behalf; they are cited here as the recent historical foundation of covenant confidence.</p>",
    "8": "<p>The distribution of Transjordanian territory: Reuben, Gad, and half-Manasseh. The giving of the land (<em>veniten et-artzam lenachalah</em>) as a covenant inheritance is already partially fulfilled east of the Jordan; it grounds the expectation of what lies ahead. Covenant promise becomes covenant history in stages.</p>",
    "9": "<p><strong>u-shmartem et-divrei ha-berit hazot va'asitem otam lema'an taskilu et kol asher ta'asun</strong>: 'observe this covenant and do it so that you may be successful in everything you do' — <em>taskilU</em> from <em>sakal</em> (to be wise, to prosper): covenant observance produces <em>sekhel</em> (wisdom, prudent success). This echoes the promise of Joshua 1:8 (if the Book of the Law does not depart from your mouth, you will make your way prosperous and be successful). Covenant observance and practical wisdom are not separable categories.</p>",
    "10": "<p><strong>atem nitzavim hayom kulkhem lifnei YHWH Eloheichem</strong>: 'you are all standing today before the LORD your God' — the covenant assembly; the full text of what 'all' means follows: leaders, elders, officials, all the men of Israel (v10-11). The spatial standing before YHWH (<em>lifnei YHWH</em>) is the covenant ceremony; the whole community becomes a legal party to the covenant.</p>",
    "11": "<p><strong>tapkhem nesheichem ve-gercha asher bekerev machaneicha</strong>: 'your children, your wives, and the foreigners in your camp' — the covenant assembly extends to the marginalized: women, children, and the <em>ger</em> (resident alien). Even the wood-choppers and water-carriers (<em>chotech etzeicha shov meimicha</em>) are included; no functional level of Israelite society is excluded from covenant membership. This broad covenant-inclusion anticipates the new covenant's gathering of all peoples (Gal 3:28).</p>",
    "12": "<p><strong>le'avrekha beveirit YHWH Eloheicha u've'alato</strong>: 'to enter into the covenant of the LORD your God and into his oath' — the ceremony is an entry-into (<em>avar</em> + berit), literally 'to cross over into' the covenant. The covenant ceremony involved physically crossing between divided animal pieces (Gen 15:17); the spatial crossing enacts the covenant-bond. <em>Alah</em> (oath): covenant oaths were self-curse formulas — may these curses come on me if I break the covenant.</p>",
    "13": "<p><strong>lema'an hakim otcha hayom lo le'am vehu yihyeh lecha le'Elohim</strong>: 'to confirm you today as his people that he may be your God' — the covenant declaration formula: you are my people, I am your God (cf. Exod 6:7; Lev 26:12; Jer 31:33). The mutual possession stated symmetrically: Israel confirmed as YHWH's people, YHWH established as Israel's God. This formula is the covenant's relational core; everything else (law, land, blessing, curse) flows from this bilateral identification.</p>",
    "14": "<p><strong>lo ittechem levadchem anochi koret et-ha-berit hazot ve'et-ha-alah hazot</strong>: 'not with you alone am I making this covenant and this oath' — the temporal extension of the covenant beyond the present generation. The covenant is not a bilateral agreement between Moses-and-YHWH on one side and the standing assembly on the other; it encompasses those not present (<em>va'et asher einennu po imanu hayom</em>, v15).</p>",
    "15": "<p><strong>ki et-asher yeshno po imanu omed hayom lifnei YHWH Eloheinu ve'et asher einennu po imanu hayom</strong>: 'both with those standing here today before the LORD and with those who are not here with us today' — the covenant's generational extension; every subsequent generation of Israelites is a party to the Mosaic covenant. This is the basis for the prophets' covenant-lawsuit against later generations (they violated a covenant their ancestors made on their behalf); it is also the basis for Paul's inclusion of Gentile believers in the Abrahamic covenant (Gal 3:29: if you are Christ's, you are Abraham's seed).</p>",
    "16": "<p>The reminder of Egyptian experience and the wilderness journey through foreign nations. <em>Ra'item et-shiqqutzehem ve'et gilulehem</em> ('you saw their detestable things and their idols') — the witnessing of idolatry makes Israel responsible to resist it; what they saw but should not have desired now becomes the temptation to guard against.</p>",
    "17": "<p><strong>etz ve'even kesef ve'zahav asher immahem</strong>: 'wood, stone, silver, and gold idols that are with them' — the idol-materials listed in ascending economic value (wood, stone, base metals to precious metals) but descending ontological value: the more expensive the idol, the more obviously it is a manufactured object rather than a living being. The idol's materials are its indictment.</p>",
    "18": "<p><strong>shoresh poreh rosh ve-la'anah</strong> (<em>šōreš pōreh rōʾš wĕlaʿănāh</em>): 'a root producing bitter poison/gall and wormwood' — the image of apostasy as a root that corrupts the whole plant; individual covenant apostasy contaminates the community. <em>Rosh</em> (gall/head) and <em>la'anah</em> (wormwood) are bitter plants associated with poison and misery (Jer 9:15; Amos 6:12; Lam 3:15,19). Hebrews 12:15 quotes this verse directly as a warning against bitterness in the congregation.</p>",
    "19": "<p><strong>hitbarech bilevavo lemor shalom yihyeh li ki bishrerut libi elech</strong>: 'he reassures himself thinking: I will be safe, even though I walk in the stubbornness of my heart' — the antinomian self-assurance; taking comfort in the covenant blessing while violating covenant conditions. <em>Bishrirut libi</em> (in the stubbornness/determination of my heart): the heart that has decided its own course regardless of the covenant's demands. <em>Lemaan sefer ha-ravah et-hatzmea</em> ('to sweep away the well-watered with the thirsty') — one person's self-assurance contaminates the whole community, making the well-watered apostate drag the thirsty community into judgment.</p>",
    "20": "<p><strong>lo-yoveh YHWH salach lo</strong> (<em>lōʾ-yōʾbeh Yhwh sĕlōaḥ-lô</em>): 'the LORD will never be willing to forgive him' — the specific refusal of pardon for the self-assured apostate. <em>Ki-az ye'shan af YHWH ve-qin'ato be'ish hahu</em> ('then the anger and jealousy of the LORD will smoke against that man') — <em>qin'ah</em> (jealousy/zeal) is the covenant-possession emotion; the self-assured apostate excites precisely YHWH's covenant-ownership response. <em>Emcha et-shemo mitachat hashamayim</em> ('I will blot out his name from under heaven') — name-obliteration as the ultimate covenant judgment (cf. Deut 9:14).</p>",
    "21": "<p>The covenant instrument of judgment: <em>hivdilo YHWH lera'ah mikkol shivtei Yisrael</em> ('the LORD will single him out for disaster from all the tribes of Israel') — the individual who sought anonymity in the corporate covenant blessing is publicly identified and separated for individual judgment. The Book of the Law functions as the covenant lawsuit against him; the curses <em>written in this book</em> are the specific charges.</p>",
    "22": "<p>The future generation's observation — <em>hador ha'acharon baneikem asher yaqumu me'achareichem</em> ('the next generation, your children who come after you') alongside foreigners from distant lands will see the devastation and ask why. The covenant curses are pedagogical for multiple generations and multiple peoples; the question prompted by the devastation is the entry point for the covenant's theological explanation.</p>",
    "23": "<p><strong>gofrit ve'melach serephah kol-artzah lo tizara velo tatzmiyach</strong>: 'burning sulfur and salt, all the land scorched, nothing planted, nothing sprouting' — the Sodom-and-Gomorrah landscape as the covenant curse's terminal image. The salt-and-sulfur desolation is total sterility: the land becomes un-creatable, un-farmable, un-livable. <em>Ka-mahpecat Sedom ve-Amorah Admah ve-Tzevoyim asher hafach YHWH be'appo u-vachamato</em> — the five cities of the plain as the reference point for total covenantal annihilation.</p>",
    "24": "<p><strong>lamma asah YHWH kakha la'aretz hazot</strong>: 'why has the LORD done this to this land?' — the nations' question; the theological puzzle of a land that was once described as the LORD's gift now devastated by the LORD's judgment. The question assumes that the land's condition reflects YHWH's disposition — the nations have learned to read history theologically from Israel's own covenant theology. This is the apologetic witness that covenant observance or violation generates among the nations.</p>",
    "25": "<p><strong>al asher azvu et-berit YHWH Elohei avotam asher karat itam betzioto otam me'eretz Mitzraim</strong>: 'because they abandoned the covenant of the LORD, the God of their fathers, which he made with them when he brought them out of Egypt' — the answer to the nations' question: covenant abandonment. The covenant is identified by its Exodus-origin; it is the relationship YHWH established precisely in the act of redemption. To abandon the covenant is to abandon the Redeemer.</p>",
    "26": "<p>The specific covenant violation: going and serving other gods (<em>vayelku vaya'avdu elohim acherim</em>) and bowing down to them — <em>elohim asher lo yeda'um velo chalak lahem</em> ('gods that they had not known and that he had not allotted to them'). The phrase 'not allotted to them' is significant: the nations have their allotted gods (the heavenly beings of Deut 4:19, 32:8 MT), but Israel's allotment is YHWH himself (32:9). Serving the nations' gods is a double covenant violation: abandoning YHWH and taking what belongs to other peoples.</p>",
    "27": "<p><strong>vayyichar af YHWH ba-aretz hahi</strong>: 'the LORD's anger burned against that land' — the land as the recipient of YHWH's anger because the land is the covenant theater; what happened in the land happened in YHWH's presence and under his covenant governance. The curses written in this book are now executed: the written covenant-sanctions become historical events.</p>",
    "28": "<p><strong>vayyiteshem YHWH me'al admatam be'af u-vecheima u-veqetzef gadol</strong>: 'the LORD uprooted them from their land in anger and wrath and great fury' — the three anger-nouns (<em>af, cheima, qetzef</em>) accumulate to express total covenant-wrath; no moderation, no partial execution. The uprooting from the land (<em>nashal me'al adamatam</em>) is the covenant curse's central punishment: losing the land YHWH gave. The exile to another land completes the covenant inversion: from the land of YHWH's gift to the land of YHWH's judgment.</p>",
    "29": "<p><strong>hannistarot laYHWH Eloheinu vehanniglot lanu ule-vaneinu ad-olam la'asot et-kol divrei ha-Torah hazot</strong>: 'the secret things belong to the LORD our God, but the revealed things belong to us and to our children forever, to do all the words of this Torah' — the canonical principle of Deuteronomy 29:29. The <em>nistarot</em> (hidden/secret things) are YHWH's sovereign domain: why some are hardened and some are softened, why covenant executes as it does in history, the timing of eschatological events. The <em>niglot</em> (revealed things) are Israel's domain: the written Torah, the covenant commands. Human responsibility is bounded by revelation; speculation about divine secrets is not the covenant's demand. The demand is: do what has been revealed. Paul's similar principle in Romans 11:33-36 (the unsearchable judgments of God) follows from the same Deuteronomic logic.</p>"
  },
  "6": {
    "4": "<p><strong>shema yisrael YHWH eloheinu YHWH echad</strong> (<em>šĕmaʿ yiśrāʾēl Yhwh ʾĕlōhênû Yhwh ʾeḥād</em>): 'Hear O Israel: YHWH our God, YHWH is one.' The Shema is the foundational confession of Jewish faith, recited morning and evening by observant Jews. <em>Echad</em> (one) is the standard Hebrew numeral one — it allows for internal distinction (as in <em>yom echad</em>, one day, composed of evening and morning; Gen 2:24, <em>basar echad</em>, one flesh, composed of two persons) but asserts the unity of the divine being against all polytheism. Paul's expansion in 1 Cor 8:6 ('one God the Father ... and one Lord Jesus Christ') is not an abandonment of monotheism but a Christological reconfiguration: the Shema's single divine identity now encompasses both Father and Son.</p>"
  },
  "18": {
    "15": "<p><strong>navi mikirbecha meacheicha kamoni yaqim lecha YHWH eloheicha elav tishmaun</strong> (<em>nābîʾ miqqirbĕkā mēʾahêkā kāmōnî yāqîm lĕkā Yhwh ʾĕlōhêkā ʾēlāw tišmāʿûn</em>): 'A prophet like me will YHWH your God raise up for you from among your brothers; to him you shall listen.' The singular prophet (<em>navi</em>) can be read as: (1) a category or series of prophets who will continue Moses's role; (2) an individual eschatological figure. The Qumran community awaited a specific prophetic figure alongside the Messiah and the Aaronic priest (1QS 9:11). Peter and Stephen in Acts 3 and 7 take reading (2): the specific individual is Jesus, whose coming makes the definitive Torah-interpretation that Moses could only anticipate.</p>"
  },
  "30": {
    "15": "<p><strong>reeh natati lefanecha hayom et-hahayyim veet-hatov veet-hamot veet-hara</strong> (<em>rĕʾēh nātattî lĕpānêkā hayyôm ʾet-hahayyîm wĕʾet-haṭṭôb wĕʾet-hammāwet wĕʾet-hārāʿ</em>): 'See I have set before you today life and good, and death and evil.' The covenant's binary choice — life or death, blessing or curse — is Israel's definitive moral situation. Paul's Christological reading of Deut 30 in Romans 10:6-8 is one of his most daring hermeneutical moves: the Torah's own accessibility-language ('not up in heaven, not across the sea, but very near you') is applied to the word of Christ — the gospel is the <em>Torah's own principle</em> of accessibility now embodied in the proclaimed word of faith.</p>"
  }
}

DEUT_CONTEXT = {
  "1": {
    "1": "<p>Deuteronomy is the fifth book of the Torah and claims to be Moses's farewell addresses on the plains of Moab before Israel enters Canaan (Deut 1:1-5). Its genre is that of a suzerainty treaty — a literary form well-attested in Hittite treaties of the second millennium BCE (Meredith Kline's groundbreaking work showed the structural parallels): preamble (1:1-5), historical prologue (1:6-4:49), stipulations (5-26), sanctions/blessings-curses (27-30), succession arrangements (31-34). The treaty-form supports an early date for Deuteronomy's core. The 'Deuteronomistic History' (Joshua through Kings) shares Deuteronomy's theological vocabulary and framework — its editors used Deuteronomy as the lens for evaluating Israel's kings.</p>"
  },
  "18": {
    "20": "<p>The test for a true prophet (18:21-22: if the word does not come to pass, it is not from YHWH) is applied in the NT to Jesus in a reversed form: his words came to pass, validating his prophetic authority. The false-prophet warning (18:20: the prophet who presumes to speak in YHWH's name a word I have not commanded him — that prophet shall die) is the background for Paul's 'if anyone preaches a gospel contrary to the one you received, let him be accursed' (Gal 1:8-9) — the apostolic test of false teaching applies Deuteronomic prophet-testing logic.</p>"
  },
  "34": {
    "10": "<p>'There has not arisen a prophet since in Israel like Moses, whom YHWH knew face to face' (34:10) is Deuteronomy's own closing judgment — the book ends by declaring Moses's prophetic incomparable greatness, which simultaneously points forward to the one greater prophet who is still awaited (18:15). The ending creates an anticipation: Moses is the greatest so far; the prophet-like-Moses is still coming. Hebrews 3:3 completes the comparison: Jesus has been counted worthy of more glory than Moses, as the builder of a house has more honor than the house.</p>"
  }
}

DEUT_CHRIST = {
  "18": {
    "15": "<p>A fulfillment: 'YHWH your God will raise up for you a prophet like me from among you, from your brothers — it is to him you shall listen.' Moses is the OT's supreme mediator — prophet (spoke YHWH's word), priest (offered sacrifice), and king (led the nation). The prophet-like-Moses is therefore the one who fulfills and exceeds all three mediatorial roles. Jesus is explicitly this prophet (Acts 3:22; 7:37), and exceeds him: as the Sermon on the Mount places Jesus's authority above Moses's ('you have heard it said ... but I say to you'), so Hebrews (3:3-6) places Christ's glory above Moses's as Son above servant. The Mosaic mediation was provisional; the Christological mediation is final and complete.</p>"
  },
  "21": {
    "23": "<p>A fulfillment: 'A hanged man is cursed by God.' Paul's citation of Deut 21:23 in Galatians 3:13 is one of his most audacious Christological moves: the cross is the cursed man's tree, and Christ became the curse for us by hanging on it. The law's curse-category — designed for criminals — is the very location where Christ absorbs all covenant-curses. The cross is not a circumvention of Torah-logic but its fulfillment: the law had always required a curse-bearer for the covenant community's sin, and Christ is that bearer. The Deuteronomic law that seemed to disqualify Jesus (a hanged criminal is cursed by God) becomes, in Paul's reading, the very mechanism of redemption.</p>"
  },
  "30": {
    "15": "<p>A direct revelation: 'See I have set before you today life and good, and death and evil.' Deuteronomy's covenant-choice reaches its eschatological fullness in Jesus: 'I am the way, and the truth, and the life' (John 14:6); 'I came that they may have life and have it abundantly' (John 10:10). The choice Moses set before Israel — life or death — is now embodied in a person. To choose Christ is to choose life in the covenant's deepest sense; to reject him is to choose the death that Moses warned of. The binary structure of Deut 30 (life vs. death, blessing vs. curse) is not dissolved in the NT but given its ultimate personal form in Christ.</p>"
  }
}

# ============================================================
# JEREMIAH
# ============================================================

JER_ECHO = {
  "1": {
    "5": [
      {"type": "allusion", "target": "Gal 1:15", "note": "Before I formed you in the womb I knew you, before you were born I consecrated you — Paul describes his own apostolic call with the same language: he was set apart before his birth; the prophetic-call pattern of Jeremiah's consecration becomes the pattern for Paul's apostolic election"}
    ]
  },
  "7": {
    "11": [
      {"type": "fulfillment", "target": "Matt 21:13", "note": "Has this house become a den of robbers in your eyes? — Jesus quotes Jer 7:11 in the temple-cleansing: my house shall be called a house of prayer, but you have made it a den of robbers; the Jeremianic temple-sermon's judgment of Israel's false security in the temple is Jesus's own indictment of the Herodian temple system"}
    ]
  },
  "31": {
    "15": [
      {"type": "fulfillment", "target": "Matt 2:18", "note": "A voice was heard in Ramah, weeping and loud lamentation, Rachel weeping for her children — Matthew cites Jer 31:15 as fulfilled in Herod's massacre of the infants of Bethlehem; Rachel weeping for her exiled children (the Babylonian deportation) is now Rachel weeping for the slaughtered children of Bethlehem"},
      {"type": "allusion", "target": "Luke 23:28", "note": "Jesus's warning to the daughters of Jerusalem to weep not for him but for themselves and their children echoes the Jeremianic pattern of future lamentation over Jerusalem (Jer 9:1; 14:17; 31:15); the weeping-for-Israel motif runs from Jeremiah through Luke's passion narrative"}
    ],
    "31": [
      {"type": "fulfillment", "target": "Heb 8:8-12", "note": "Behold the days are coming when I will make a new covenant with the house of Israel — Hebrews cites Jer 31:31-34 in full (the longest OT quotation in the NT) as the scriptural demonstration that the Mosaic covenant was designed to be superseded; the new covenant's promise (law on hearts, universal knowledge of YHWH, permanent forgiveness) is fulfilled in Christ"},
      {"type": "fulfillment", "target": "Luke 22:20", "note": "This cup is the new covenant in my blood — Jesus at the Last Supper identifies the cup with Jer 31:31-34's new covenant; the blood of Christ is the blood of the covenant Jeremiah announced, making the Lord's Supper the enacted new covenant seal"}
    ]
  }
}

JER_ORIGINAL = {
  "31": {
    "31": "<p><strong>hinei yamim baim neum YHWH vekharati et-beit Yisrael veet-beit Yehudah berit hadasha</strong> (<em>hinnēh yāmîm bāʾîm nĕʾum Yhwh wĕkārattî ʾet-bêt yiśrāʾēl wĕʾet-bêt yĕhûdāh bĕrît ḥădāšāh</em>): 'Behold the days are coming, declares YHWH, when I will make a new covenant with the house of Israel and the house of Judah.' <em>Berit hadasha</em> (new covenant): the only occurrence of this exact phrase in the OT. <em>Hadash</em> (new) can mean 'renewed' (as in the new moon, <em>hodesh</em>) or 'qualitatively different.' Jeremiah's contrast makes it the latter: 'not like the covenant I made with their fathers ... which they broke' (v. 32). The new covenant is distinguished by three characteristics: (1) internalized law (v. 33: on the heart, not stone); (2) universal direct knowledge of YHWH (v. 34: no longer 'know the LORD'); (3) permanent forgiveness (v. 34: I will remember their sin no more).</p>"
  }
}

JER_CONTEXT = {
  "1": {
    "1": "<p>Jeremiah prophesied ca. 627-586 BCE (from the 13th year of Josiah through the fall of Jerusalem and beyond), the most turbulent period in Judah's history. He witnessed Josiah's reform (621 BCE, 2 Kings 22-23) and its collapse, the defeats at Megiddo (609 BCE) and Carchemish (605 BCE), Nebuchadnezzar's three deportations (605, 597, 586 BCE), the destruction of Jerusalem and the temple (586 BCE), and the assassination of Gedaliah. His call at the outset of his ministry and his suffering throughout (the 'Confessions', Jer 11-20) make him the most personal of the prophets — his inner life is more visible in Scripture than any other OT figure. The 'new covenant' oracle (31:31-34) is addressed to a people in the ruins of the Babylonian exile.</p>"
  },
  "31": {
    "34": "<p>The three promises of Jer 31:33-34 in their historical context: (1) the Torah internalized on hearts rather than carved on tablets solves the problem that generated the exile — Israel kept the external law while their hearts were far from YHWH; (2) the universal knowledge of YHWH solves the class-stratification of covenantal knowledge (prophets, priests, sages knew; the people often did not); (3) the permanent forgiveness ('I will remember their sin no more') solves the accumulated sin-debt that the Mosaic sacrificial system could cover but not finally remove (Heb 10:1-4: the law has a shadow ... sacrifices cannot make perfect those who draw near). The new covenant addresses precisely the structural deficiencies of the Mosaic covenant.</p>"
  }
}

JER_CHRIST = {
  "31": {
    "31": "<p>A direct revelation: 'Behold the days are coming when I will make a new covenant with the house of Israel and the house of Judah.' The new covenant is the Christological center of the OT's prophetic program: Jesus at the Last Supper explicitly claims to enact this covenant (Luke 22:20: 'This cup that is poured out for you is the new covenant in my blood'), and Hebrews quotes all of Jer 31:31-34 (8:8-12) as the scriptural proof that the old covenant's priesthood and sacrificial system were provisional and superseded. The three elements of the new covenant are fulfilled in Christ: (1) law on hearts → the Spirit writes Christ's character in the believer; (2) universal knowledge of YHWH → all who come to Christ know the Father (John 17:3); (3) permanent forgiveness → the once-for-all sacrifice of Christ (Heb 9:26-28; 10:14).</p>"
  }
}

# ============================================================
# EZEKIEL
# ============================================================

EZEK_ECHO = {
  "11": {
    "19": [
      {"type": "fulfillment", "target": "2 Cor 3:3", "note": "I will remove the heart of stone and give them a heart of flesh — the new heart/new spirit promise of Ezek 11:19 and 36:26 is fulfilled in the Spirit's ministry that Paul describes: written not on stone tablets but on tablets of human hearts"}
    ]
  },
  "34": {
    "11": [
      {"type": "fulfillment", "target": "John 10:11", "note": "I myself will search for my sheep and seek them out — YHWH's own shepherding (Ezek 34:11-16) is enacted by Jesus as the Good Shepherd; what YHWH promised to do for his abandoned sheep (I myself will shepherd them) is what Jesus claims to be doing: I am the good shepherd"}
    ]
  },
  "36": {
    "25": [
      {"type": "fulfillment", "target": "John 3:5", "note": "I will sprinkle clean water on you and you shall be clean; I will give you a new spirit — the new birth of water and Spirit in John 3:5 is the fulfillment of Ezek 36:25-27; what Ezekiel prophesied as the new covenant's cleansing and Spirit-filling is what Jesus announces as the necessary birth for entering the kingdom"}
    ]
  },
  "37": {
    "1": [
      {"type": "allusion", "target": "John 11:43-44", "note": "The valley of dry bones that come to life at YHWH's breath-word — Jesus's command 'Lazarus, come out' is the personal enactment of the eschatological resurrection vision of Ezek 37; the Spirit's breath (John 20:22) that animates the church repeats the pattern of Ezek 37:9-10"}
    ]
  },
  "47": {
    "1": [
      {"type": "fulfillment", "target": "Rev 22:1", "note": "The river of water flowing from the temple — Ezekiel's visionary river (increasingly deep, bringing life to everything it touches) is fulfilled in Revelation's river of life flowing from the throne of God and the Lamb; Jesus is himself the source of living water (John 7:38-39)"}
    ]
  }
}

EZEK_ORIGINAL = {
  "1": {
    "28": "<p><strong>ke-mareh haqeshet asher yihyeh beanav beyom hagashem ken mareh hanog saviv hu mareh demut kevod YHWH</strong>: 'Like the appearance of the bow that is in the cloud on the day of rain, so was the appearance of the brightness all around. Such was the appearance of the likeness of the glory of YHWH.' Ezekiel's theophany of the divine chariot-throne (<em>merkabah</em>) is the foundation of Jewish mystical speculation. His careful qualification of language — 'likeness of the glory of YHWH' rather than 'glory of YHWH' — maintains divine transcendence even in the vision. John of Revelation reuses Ezekiel's visionary vocabulary (the four living creatures of Ezek 1 reappear in Rev 4:6-8; the rainbow around the throne in Rev 4:3 echoes Ezek 1:28), grounding the Christological throne-vision in the Ezekielian framework.</p>"
  },
  "36": {
    "26": "<p><strong>venathati lachem lev hadash veruach hadasha etten bekirbechem vahashirothi et-lev haeben mivsarchem venatati lachem lev basar</strong>: 'And I will give you a new heart and a new spirit I will put within you. And I will remove the heart of stone from your flesh and give you a heart of flesh.' The new heart-new spirit promise is the Ezekielian new covenant (parallel to Jer 31:31-34). <em>Lev hadash</em> (new heart): the decision-making center (<em>lev</em>) of human personhood is replaced — not repaired, not improved, but new. <em>Ruach hadasha</em> (new spirit): YHWH's own Spirit placed within (v. 27: 'I will put my Spirit within you and cause you to walk in my statutes'). This is Pentecost prophesied — the Spirit's indwelling that replaces external Torah-motivation with internal Spirit-empowered desire and ability to obey.</p>"
  }
}

EZEK_CONTEXT = {
  "1": {
    "1": "<p>Ezekiel was a priest who was deported to Babylon in the first deportation (597 BCE) and received his call-vision in 593 BCE by the Chebar canal in Babylonia ('the thirtieth year', 1:1 — possibly his own thirtieth year, the age for priestly service). He prophesied to the exilic community ca. 593-571 BCE. His priestly background shapes his theology: the book is preoccupied with divine glory (<em>kavod</em>), the departure of the Shekinah from the temple (chs. 8-11), and its eschatological return (chs. 40-48). The merkabah vision (ch. 1) was the most influential single vision in subsequent Jewish mysticism — the Hekhalot literature built an entire tradition of heavenly ascent around it. The four living creatures (lion, ox, eagle, human) reappear in Irenaeus's identification of the four Gospel symbols.</p>"
  },
  "37": {
    "1": "<p>The valley of dry bones vision (37:1-14) is addressed to the exilic community that had concluded 'our bones are dried up, our hope is lost, we are indeed cut off' (v. 11). The corporate resurrection metaphor — national restoration envisioned as bodily resurrection — uses the imagery of physical resurrection for Israel's return from exile. This is not a straightforward prophecy of individual eschatological resurrection (though the same imagery is applied there in Isa 26:19; Dan 12:2), but a bold use of resurrection as the metaphor for what only divine creative power could accomplish for the exiled nation. The NT develops the resurrection-from-exile typology: Christ's resurrection is both personal and the beginning of the great return-from-death that Ezekiel envisioned.</p>"
  }
}

EZEK_CHRIST = {
  "34": {
    "11": "<p>A direct revelation: 'For thus says the Lord GOD: Behold I, I myself will search for my sheep and seek them out ... I will rescue them from all places where they have been scattered ... I will seek the lost and I will bring back the strayed and I will bind up the injured and I will strengthen the weak.' Jesus's 'I am the good shepherd' (John 10:11) and the parable of the lost sheep (Luke 15:4-6) are the incarnational enactment of Ezek 34's promise. What YHWH said he himself would do (in contrast to the failed shepherds of Israel's leaders) is what Jesus does: the divine shepherd-promise is fulfilled by the Son who is YHWH present in person, doing what YHWH promised he personally would do for the scattered flock.</p>"
  },
  "36": {
    "27": "<p>A direct revelation: 'And I will put my Spirit within you and cause you to walk in my statutes and be careful to obey my rules.' Pentecost is Ezekiel 36:27 enacted. The Spirit's indwelling is not merely motivational but causally efficacious: 'I will cause you to walk' — the Hebrew Hiphil form makes YHWH the enabling cause of the obedience that follows. This is the new covenant's answer to the old covenant's demand without the enabling Spirit: the same Torah-standard now fulfilled because the Spirit from within enables what the law from without could only command. Paul's 'the righteous requirement of the law might be fulfilled in us who walk not according to the flesh but according to the Spirit' (Rom 8:4) is the Christological-pneumatological fulfillment of Ezek 36:27.</p>"
  },
  "47": {
    "9": "<p>A type: 'And wherever the river goes, every living creature that swarms will live, and there will be very many fish. For this water goes there, that the waters of the sea may become fresh; so everything will live where the river goes.' The eschatological temple-river of Ezekiel's vision (ch. 47), increasingly deep and life-giving, is the OT type for the water that flows from Christ. Jesus at Tabernacles (John 7:38-39) applies the Spirit-water promise to himself: 'rivers of living water will flow from within him' — and John explains this is the Spirit. Revelation's new creation river (22:1) flowing from the throne of God and the Lamb completes the Ezekiel type: the new temple's river is Christ himself, and all who drink from him live.</p>"
  }
}

# ============================================================
# DANIEL
# ============================================================

DAN_ECHO = {
  "2": {
    "44": [
      {"type": "fulfillment", "target": "Luke 1:33", "note": "The God of heaven will set up a kingdom that shall never be destroyed — the stone that becomes a great mountain filling the whole earth (Dan 2:35, 44) is fulfilled in the kingdom announced by the angel: his kingdom will have no end"},
      {"type": "fulfillment", "target": "Rev 11:15", "note": "The kingdom of the world has become the kingdom of our Lord and of his Christ — the seventh trumpet's announcement is the explicit fulfillment of Dan 2:44's never-to-be-destroyed kingdom of heaven"}
    ]
  },
  "7": {
    "13": [
      {"type": "fulfillment", "target": "Matt 26:64", "note": "You will see the Son of Man seated at the right hand of Power and coming on the clouds of heaven — Jesus applies Dan 7:13 to himself before the Sanhedrin; the coming on the clouds of heaven is the exaltation of the Son of Man to the divine throne, which the high priest recognizes as blasphemy"},
      {"type": "fulfillment", "target": "Acts 1:9", "note": "A cloud took him out of their sight — the ascension cloud echoes the Son of Man coming with the clouds of Dan 7:13; the ascension is the enthronement, not a departure to a distant location"},
      {"type": "fulfillment", "target": "Rev 1:7", "note": "Behold he is coming with the clouds — Revelation combines Dan 7:13 with Zech 12:10 to describe the parousia as the final manifestation of the Son of Man's cloud-coming that began at the ascension"}
    ]
  },
  "9": {
    "24": [
      {"type": "allusion", "target": "Luke 4:18", "note": "To anoint a most holy place — the seventy weeks leading to the anointing of the most holy one (or most holy place) has been interpreted as pointing to Christ's anointing at baptism; the messianic anointing is the fulfillment of Daniel's eschatological program"},
      {"type": "allusion", "target": "Heb 9:26", "note": "To finish transgression, put an end to sin, and atone for iniquity — the six goals of Daniel's seventy weeks (9:24) are summarized in Hebrews: he has appeared once for all at the end of the ages to put away sin by the sacrifice of himself"}
    ]
  },
  "12": {
    "2": [
      {"type": "fulfillment", "target": "John 5:28-29", "note": "Many who sleep in the dust of the earth shall awake, some to everlasting life and some to shame and everlasting contempt — Jesus's promise of a resurrection of all the dead, some to life and some to judgment, applies Dan 12:2's general resurrection language to himself as the one who gives life and judges"}
    ]
  }
}

DAN_ORIGINAL = {
  "7": {
    "13": "<p><strong>hazeh haveit bechezwe leylaya vaara im-anane shemayya kebar enash ateh vead attiq yomaya matah uqdamoy haytivuhi</strong> (Aramaic): 'I saw in the night visions, and behold, with the clouds of heaven there came one like a son of man, and he came to the Ancient of Days and was presented before him.' The 'one like a son of man' (<em>kebar enash</em>, Aramaic for 'like a human being') in Daniel 7 contrasts with the four beasts (lions, bears, leopards, a terrible beast) that rise from the sea — representing successive human empires. The human figure comes from heaven, not the sea, and receives the dominion the beasts claimed. The NT application (Jesus's self-designation as 'Son of Man' in all four Gospels) is the consistent claim that Jesus is this figure who receives eternal dominion from the Ancient of Days — a claim recognized as divine by the Sanhedrin (Mark 14:62-64).</p>"
  },
  "9": {
    "24": "<p><strong>shivim shavuim nechetach al-amecha vehal ir qadshecha lekale happesha ulehatem chataut velchapper avon ulehavi tsdeq olamim velachtom chazot venavia velimshoach qodesh qodashim</strong>: 'Seventy weeks are decreed about your people and your holy city, to finish the transgression, to put an end to sin, to atone for iniquity, to bring in everlasting righteousness, to seal both vision and prophet, and to anoint a most holy place.' The six infinitives of Dan 9:24 have generated centuries of calculation and debate. The <em>shavuim</em> (weeks/sevens) are most naturally weeks of years (seven-year units), giving 490 years from the decree to rebuild Jerusalem. The six goals — which are systematically soteriological and eschatological — align most naturally with Christ's work: atonement (to finish transgression, atone for iniquity), righteousness (bring in everlasting righteousness), and the end of the prophetic age (seal vision and prophet).</p>"
  }
}

DAN_CONTEXT = {
  "1": {
    "1": "<p>The book of Daniel is set in the Babylonian exile (605-538 BCE) and narrates the experiences of four young Jewish men under Nebuchadnezzar, Belshazzar, Darius the Mede, and Cyrus of Persia. The historical reliability of Daniel's court settings has been debated (Darius the Mede is unattested by name in Babylonian records; some details seemed anachronistic). The primary critical alternative: Daniel was composed ca. 167-164 BCE during the Maccabean revolt, as <em>vaticinium ex eventu</em> (prophecy after the fact) using the fictional setting of the sixth century. Conservative scholars argue for a sixth century date and understand the Darius question as a secondary title for Cyrus or an otherwise unrecorded official. The book's affinities with the Aramaic of the fifth-fourth centuries and the absence of Greek loanwords that would be expected in a second century BCE composition support an early composition.</p>"
  },
  "7": {
    "1": "<p>Daniel 7-12 contains four major apocalyptic visions. The genre of apocalypse (from Greek <em>apokalypsis</em>, unveiling) is characterized by: symbolic or heavenly visions mediated by an angel, disclosure of the heavenly perspective on historical events, periodization of history into fixed sequences, and imminent divine intervention. Daniel is the OT's primary apocalyptic text; its imagery (beasts from the sea, the Ancient of Days, the Son of Man, the four kingdoms) was enormously influential on Jewish and Christian apocalyptic (1 Enoch, 4 Ezra, 2 Baruch, and the NT's Revelation). Jesus's eschatological discourse (Mark 13 and parallels) draws extensively from Daniel, particularly the abomination of desolation (Dan 11:31; 12:11 → Mark 13:14) and the coming of the Son of Man (Dan 7:13 → Mark 13:26).</p>"
  }
}

DAN_CHRIST = {
  "7": {
    "13": "<p>A direct revelation: 'One like a son of man came with the clouds of heaven and came to the Ancient of Days and was presented before him. And to him was given dominion and glory and a kingdom, that all peoples, nations, and languages should serve him; his dominion is an everlasting dominion, which shall not pass away, and his kingdom one that shall not be destroyed.' Jesus's consistent self-identification as 'the Son of Man' throughout the Gospels is a deliberate claim to be this figure — the one who receives from the Ancient of Days the universal, eternal dominion. The ascension is the receiving of this dominion; Pentecost is the beginning of its exercise; the parousia is its final manifestation. The 'Son of Man' claim is Jesus's most characteristic and most Christologically loaded self-designation.</p>"
  },
  "9": {
    "26": "<p>A fulfillment: 'After sixty-two weeks, an anointed one shall be cut off and shall have nothing.' The phrase 'cut off' (<em>yikaret</em>) is the judicial-death vocabulary of Torah (used for capital offenses). The anointed one is cut off not for his own sins (the grammar allows 'and there is nothing to him' or 'but not for himself') — the same pattern as Isa 53:8 ('cut off out of the land of the living ... for the transgression of my people'). Regardless of the precise calculation of the seventy weeks, the Christological core is the same: the anointed one (the Messiah) dies, is cut off, apparently without inheriting anything — and yet this death is the very mechanism by which the six goals of v. 24 are accomplished. The cross is Daniel's predicted event.</p>"
  },
  "12": {
    "2": "<p>A direct revelation: 'And many of those who sleep in the dust of the earth shall awake, some to everlasting life and some to shame and everlasting contempt.' Daniel 12:2 is the OT's clearest statement of a general resurrection with differentiated outcomes — resurrection to life and resurrection to judgment. Jesus applies this directly to himself: 'The hour is coming when all who are in the tombs will hear his voice and come out, those who have done good to the resurrection of life and those who have done evil to the resurrection of judgment' (John 5:28-29). Christ is the voice that summons from the tombs — the executor of Daniel's two-outcome resurrection — and his own resurrection is the first fruits of what Dan 12:2 prophesied for the final eschatological hour.</p>"
  }
}

def main():
    books_data = [
        ('deuteronomy', DEUT_ECHO, DEUT_ORIGINAL, DEUT_CONTEXT, DEUT_CHRIST),
        ('jeremiah', JER_ECHO, JER_ORIGINAL, JER_CONTEXT, JER_CHRIST),
        ('ezekiel', EZEK_ECHO, EZEK_ORIGINAL, EZEK_CONTEXT, EZEK_CHRIST),
        ('daniel', DAN_ECHO, DAN_ORIGINAL, DAN_CONTEXT, DAN_CHRIST),
    ]
    for book, echo_d, orig_d, ctx_d, chr_d in books_data:
        e = load_echo(book)
        merge_echo(e, echo_d)
        save_echo('', e) if False else save_echo(book, e)

        c = load_comm('mkt-original', book)
        merge_comm(c, orig_d)
        save_comm('mkt-original', book, c)

        c = load_comm('mkt-context', book)
        merge_comm(c, ctx_d)
        save_comm('mkt-context', book, c)

        c = load_comm('mkt-christ', book)
        merge_comm(c, chr_d)
        save_comm('mkt-christ', book, c)
        print(f'{book}: all 4 layers written')

if __name__ == '__main__':
    main()
