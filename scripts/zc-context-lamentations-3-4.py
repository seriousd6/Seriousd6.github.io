"""
Lamentations + all 12 Minor Prophets — all four layers.
These complete the OT portion of the Z Commentary Suite.
Key NT: Hosea (son called out of Egypt; Lo-ammi/Ammi), Joel 2 (Pentecost),
        Amos (Day of the LORD, Amos 9:11 Davidic restoration),
        Jonah (sign of Jonah), Micah 5:2 (Bethlehem), Zech 9:9 (triumphal entry),
        Zech 12:10 (pierced one), Mal 3:1 (messenger), Mal 4:5 (Elijah).
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

# ============================
# LAMENTATIONS
# ============================

LAM_ECHO = {
  "3": {
    "22": [
      {"type": "allusion", "target": "Heb 13:8", "note": "The steadfast love of the LORD never ceases; his mercies never come to an end — the great confession of YHWH's faithfulness in the midst of Jerusalem's total destruction; Jesus Christ is the same yesterday and today and forever (Heb 13:8) is the new covenant form of the same confession: divine steadfast love, permanent and unending"},
      {"type": "allusion", "target": "Lam 3:26", "note": "It is good that one should wait quietly for the salvation of the LORD — the sufferer's renewed hope after total collapse; the salvation (yeshuah) that Lamentations awaits is the name of Jesus"}
    ]
  }
}

LAM_ORIGINAL = {
  "3": {
    "22": "<p><strong>chasde YHWH ki lo tamnu ki lo chalu rachamav</strong>: 'The steadfast love [<em>chesed</em>] of the LORD never ceases; his mercies [<em>rachamim</em>] never come to an end.' This confession (Lam 3:22-24) is the theological center of Lamentations — placed at the exact midpoint of the book (the acrostic structure of ch. 3 is 22×3 = 66 verses, and v. 22 is the centerpiece). Its context makes it remarkable: Lamentations is the most sustained expression of grief and lamentation in Scripture, written in the immediate aftermath of Jerusalem's destruction, yet its center is a confession of divine steadfast love. The structure embodies the theology: suffering and praise, grief and faith, can coexist — and at the center of the darkest book is the brightest confession.</p>"
  }
}

LAM_CONTEXT = {
  "1": {
    "1": "<p>Lamentations is a collection of five poems mourning the destruction of Jerusalem in 586 BCE. Four are acrostics (following the Hebrew alphabet), reflecting the artistic discipline of theological grief: the structure provides form for what might otherwise be formless pain. Traditionally attributed to Jeremiah (who is associated with Lamentations in 2 Chr 35:25 and the LXX introduction), the poems articulate Israel's grief, confession, and ongoing hope in YHWH's steadfast love. The book is read in Jewish tradition on Tisha B'Av, the fast commemorating the temple's destruction. Its influence on the NT's passion narrative is significant: the description of Jerusalem's suffering (1:12: 'Is it nothing to you, all you who pass by?') is echoed in the passion accounts; Christ's passion is interpreted through the Lamentations framework of righteous suffering.</p>"
  },
  "3": {
    "1": "<p>Chapter 3 opens with a structural and speaker shift. The feminine Daughter of Zion voice of chs. 1–2 gives way to a <em>gever</em> (H1397, an able-bodied man — not the generic <em>ish</em> but a specifically martial/vigorous male), a representative figure who speaks on behalf of the community. The triple acrostic structure — 22 Hebrew letters × 3 verses per letter = 66 verses — is the most artistically complex in Lamentations. The three verses per letter create a hammering, relentless quality: aleph (vv1–3), bet (vv4–6), and so on through taw (vv64–66). The opening word <em>ani ha-gever</em> (I am the man) places a specific individual voice at the center of the national catastrophe. The <em>shevet evrato</em> (rod of his wrath, v1) is the instrument YHWH promised in Deut 28:15–68 for covenant violation.</p>",
    "2": "<p>The darkness imagery of v2 (<em>vayolech choshekh velo or</em>, he has driven me and made me walk in darkness and not in light) inverts the creation act: in Genesis 1 YHWH separates light from darkness; here he drives into darkness. The same inversion appears in Amos 5:18 (the Day of the LORD — darkness and not light). The ANE background: darkness was the realm of chaos, death, and divine absence; the sun-god Shamash was the deity of justice and light. YHWH's driving into darkness is therefore both cosmological and covenantal — withdrawal of the covenant-sun of justice.</p>",
    "3": "<p>V3 intensifies: against me alone (<em>ach bi yishlov yehafokh yado kol hayom</em>) he turns his hand all the day. The <em>yad</em> (hand) of YHWH in the OT is primarily the hand of salvation (the Exodus: Exod 13:3, 14, 16 — the strong hand of YHWH); here the same hand is turned against the speaker. The Exodus background is deliberate: the language that once described salvation now describes judgment, signaling that the covenant relationship has entered a phase of inversion.</p>",
    "4": "<p>The bet-acrostic (vv4–6) opens with physical deterioration vocabulary. <em>Bilah</em> (H1086, to wear out, to waste away) is the same root used for old garments wearing out (Deut 8:4: your clothing did not wear out; here the flesh itself wears out). The flesh (<em>basar</em>) and skin (<em>or</em>) vocabulary connects to the Job tradition (Job 19:20: my bones cling to my skin and to my flesh). The Jerusalem siege of 586 BCE lasted approximately 18 months (2 Kings 25:1–4); the physical effects of prolonged famine on the body are described here with medical accuracy.</p>",
    "5": "<p>V5 describes an enclosed state — surrounded (<em>yiven alai</em>) with bitterness and hardship. The architectural metaphor suggests both the city wall that trapped the besieged and the theological enclosure of divine judgment. <em>La'anah</em> (wormwood) and <em>ro'sh</em> (gall/poison) are the covenant-curse substances that appear in Deut 29:18 (a root producing gall and wormwood) and Jer 9:15 (I will feed this people with wormwood and give them poisonous water to drink). The besieged community literally experienced famine, and the bitterness metaphor maps onto it precisely.</p>",
    "6": "<p>V6 (<em>bemachshakkim hoshivani kemeitei olam</em>, in dark places he has made me sit like the long-dead) echoes the language of Sheol and the pit. The <em>mechoshekh</em> (dark places) is the realm of the dead (Ps 88:6: you have put me in the depths of the pit, in the regions dark and deep; Ps 143:3: he has made me sit in darkness like those long dead). The verse places the siege experience at the level of death itself — not merely suffering but the cessation of covenantal life.</p>",
    "7": "<p>The gimel-acrostic (vv7–9) develops prison imagery. V7: walled in (<em>gadar ba'adi</em>) with no escape; bronze chains (<em>nichashot</em>) weighing heavy. The bronze chains directly echo the actual fate of Zedekiah, the last Davidic king, who was captured and bound with bronze fetters (<em>nichashtayim</em>, 2 Kings 25:7 — the same root). The gever's individual experience is the national experience in miniature: the king in bronze chains, the city walled in.</p>",
    "8": "<p>V8 describes blocked prayer: even when the gever calls out (<em>yiza'aq vegash'iya</em>) and screams, he shuts out (<em>satam</em>) his prayer. The satam root (H5640, to stop, to block) appears in Gen 26:15 for wells stopped up by the Philistines. Here YHWH has stopped up the channel of prayer the way an enemy stops up a water supply during a siege. Prayer is the life-giving water of relationship; its blockage is the spiritual equivalent of the physical siege.</p>",
    "9": "<p>V9: the paths (<em>derakhay</em>) hewn with cut stone; the ways (<em>netivotai</em>) made crooked. The image is of a road that has been deliberately obstructed — a military tactic in which defenders or attackers would fill roads with rubble to prevent movement. The smooth path that wisdom promises (Prov 3:17: her ways are ways of pleasantness, and all her paths are peace) has been replaced with its exact opposite.</p>",
    "10": "<p>The dalet-acrostic (vv10–12) shifts to predatory-animal imagery. V10: YHWH as a bear lying in wait (<em>dov orev</em>), a lion in hiding (<em>aryeh bemistarin</em>). Hosea 13:7–8 employs identical imagery for YHWH's judgment on Israel: I will fall upon them like a bear robbed of her cubs ... I will tear open their chest; I will devour them like a lion. The bear-robbed-of-cubs simile is specifically about a she-bear protecting young — the fiercest animal threat in the Palestinian context. This is not divine cruelty but covenant consequence: YHWH's fiercest love turned to judgment when rejected.</p>",
    "11": "<p>V11: YHWH turned aside (<em>sorer</em>) my ways and tore me to pieces (<em>pishshachani</em>). The tearing is the predatory completion of v10's stalking. The word <em>pishshach</em> (H6582, to tear) is used of lions tearing prey in Amos 1:2 and elsewhere. He made me desolate (<em>shomemani</em>) — the desolation vocabulary (<em>shomem</em>) runs throughout the destruction literature: the desolate temple, the desolate land (Dan 9:27; Jer 12:11). The gever is the microcosm of the nation.</p>",
    "12": "<p>V12: He bent his bow (<em>darach qashto</em>) and set me as a target (<em>matarah</em>) for the arrow. The divine archer image appears in Job 16:12–13 (he set me up as his target; his archers surround me; he slashes open my kidneys). The <em>matarah</em> (H4307, target) is a military term — what soldiers aim at on a practice range. Being designated as the target of YHWH's archery is the covenant threat realized: the community that was meant to be the demonstration of YHWH's glory to the nations is now the demonstration of his judgment.</p>",
    "13": "<p>The he-acrostic (vv13–15). V13: arrows (<em>benei ashpato</em>, sons of his quiver) driven into the kidneys (<em>kelyot</em>). The kidneys in Hebrew physiology were considered the seat of deep emotion, inner life, and moral discernment (Ps 16:7: my kidneys instruct me by night; Prov 23:16: my kidneys will rejoice when your lips speak right things). The divine archer targeting the kidneys is an assault on the inner spiritual life of the community, not merely physical pain.</p>",
    "14": "<p>V14: becoming the laughingstock (<em>sachok</em>) of all peoples, their mocking-song (<em>negunat</em>) all day long. The public shame context: in the ANE, defeat and exile were read as divine abandonment. The defeated city's god had clearly been weaker. This reading is precisely what the Psalms of Zion (46, 48, 76) had argued against (Jerusalem is inviolable because YHWH dwells there). Now the nations' mockery is the reversal of those Zion psalms. <em>La'anah</em> (wormwood, v15) and <em>ro'sh</em> (gall) recur from v5 — the covenant-curse vocabulary forming a bracket around the bet–he section.</p>",
    "15": "<p>V15: He filled me with bitterness (<em>sib'ani vammorim</em>) and made me drunk with wormwood (<em>hirwani la'anah</em>). The cup-of-wrath imagery (Jer 25:15–16; Ps 75:8; Rev 14:10) underlies this: the bitter cup that the prophet has been given to drink, which signals divine judgment. Jer 23:15 gives the false prophets wormwood and poison water — they feed the people on false comfort, and now the true judgment comes in the same bitter vocabulary.</p>",
    "16": "<p>The vav-acrostic (vv16–18). V16: gravel in the teeth (<em>vaygares bacharetz shinnai</em>) and trampled in the ashes (<em>hikpishani ba'efer</em>). The gravel-in-teeth image is a specific siege-ration context: when supplies run out, coarse bread mixed with grit and foreign matter was consumed. Archaeologists have found grinding stones from siege contexts with sand and grit mixed into the ground flour, evidenced by dental wear in skeletal remains from ancient sieges. The ashes signal mourning posture (Job 2:8; Esther 4:3).</p>",
    "17": "<p>V17: My soul is bereft of peace (<em>vatizanach mishshalom nafshi</em>) — I have forgotten what happiness/goodness (<em>tovah</em>) is. The forgetting of <em>shalom</em> is more than emotional distress: <em>shalom</em> was the covenant term for the state of comprehensive well-being promised to the obedient community (Num 6:26; Jer 29:11). Its absence is the structural absence of the covenant's blessing-half. The forgetting of <em>tovah</em> echoes Deut 28:47 (because you did not serve YHWH your God with joyfulness and gladness of heart, because of the abundance of all things).</p>",
    "18": "<p>V18 (<em>vaomar abad nitzchi vetiqvatim YHWH</em>, I said my endurance/future has perished, and my hope from YHWH) is the nadir of the lament — the low point before the turn. <em>Netzach</em> (H5331, perpetuity, endurance, victory/future) and <em>tikvah</em> (H8615, hope — from <em>qavah</em>, to wait/hope) are both gone. The Naomi parallel: 'The hand of the LORD has gone out against me' (Ruth 1:13) — the state of utter experienced desolation with no visible hope. The structure now pivots at v19.</p>",
    "19": "<p>The zayin-acrostic (vv19–21) begins the turn. V19: the imperative <em>zekor</em> (remember!) or the gever remembering himself — the Hebrew is ambiguous (imperative or infinitive construct). Either way, the active memory of affliction and bitterness (<em>la'anah</em>, wormwood) is the instrument by which hope re-enters. The <em>zayin</em> letter begins <em>zakar</em> (to remember) — the acrostic's structural theology: the z-letter section is about remembering. Israel's fundamental covenantal act is <em>zakar</em>: YHWH remembered (<em>vayizkor</em>) his covenant with Abraham (Exod 2:24); the Passover seder is an act of corporate memory (Exod 13:3).</p>",
    "20": "<p>V20: <em>zakor tizkhor vatashaach alai nafshi</em> — my soul remembers and bows down within me. The double root <em>zakor tizkhor</em> (remember, remembering) is an emphatic infinitive absolute construction, marking this as the most intense remembering. The soul (<em>nafshi</em>) bowing down (<em>shuach</em>, H7743, to sink, to bend) is both the mourning posture and the movement toward the prayer that follows. The crisis of v20 deepens even as memory begins to work.</p>",
    "21": "<p>V21 (<em>zot ashiv el libbi al ken ayachel</em>, this I call back to my heart; therefore I have hope) is the hinge of the entire poem and the entire book. The deliberate volitional act — calling something back to mind — signals the movement from drowning in experience to anchoring in truth. <em>Ayachel</em> (therefore I have hope/wait) uses the same <em>yachal</em> root as <em>tikvah</em>'s <em>qavah</em> synonym, reinforcing that what follows in vv22–24 is the content of that hope. The structure embeds the theology: despair does not automatically become hope; it requires the act of turning the mind back to what is true about YHWH.</p>",
    "22": "<p>The chet-acrostic (vv22–24) is the theological center of Lamentations and one of the OT's most concentrated confessional passages. V22: <em>chasde YHWH ki lo tamnu ki lo chalu rachamav</em> — the steadfast love of YHWH never ceases; his mercies never come to an end. <em>Chesed</em> (H2617, covenant loyalty/steadfast love) and <em>rachamim</em> (H7356, mercies/compassion — from <em>rechem</em>, womb) are the two great covenantal terms of divine love. Their structural placement at the center of the most grief-saturated book in Scripture is the literary embodiment of the theological claim: even at the center of complete destruction, the center holds. The Exodus background: YHWH's self-declaration (Exod 34:6–7) is <em>chesed</em> and <em>rachamim</em> first, then justice.</p>",
    "23": "<p>V23: <em>chadashim labeqarim rabbah emunatekha</em> — they are new every morning; great is your faithfulness (<em>emunah</em>). The morning (<em>boqer</em>) in the ANE was the time of salvation: the night was the time of danger and siege; the morning light revealed whether YHWH had acted (Ps 46:5; Exod 14:24–27 — it was in the morning watch that YHWH troubled the Egyptian army). The daily newness of mercies maps onto the daily dawn: every morning the sun rises and every morning the mercies are renewed. <em>Emunah</em> (H530, faithfulness, steadiness — root of <em>amen</em>) is the character of a YHWH who is reliably the same despite all changing circumstances.</p>",
    "24": "<p>V24: <em>chelqi YHWH amrah nafshi al ken ayachel lo</em> — the LORD is my portion, says my soul; therefore I will hope in him. The <em>chelek</em> (portion) vocabulary comes from the Levitical inheritance tradition: the Levites received no land inheritance in Canaan because YHWH was their portion (Num 18:20; Deut 10:9). Ps 73:26 (my flesh and my heart may fail, but God is the strength of my heart and my portion forever) uses the same vocabulary. The gever appropriates the Levitical confession: YHWH himself — not land, not temple, not Davidic throne — is the inheritance that cannot be taken away even in exile.</p>",
    "25": "<p>The tet-acrostic (vv25–27). V25: <em>tov YHWH lekavav lenefesh tidreshenu</em> — YHWH is good to those who wait for him (<em>qavah</em>, H6960), to the soul that seeks him. The <em>qavah</em> root is the same as <em>tikvah</em> (hope): to hope is to wait actively and expectantly, like a watchman waiting for dawn (Ps 130:6). The goodness of YHWH to the waiter is not a passive reward for passive inactivity but the result of the active orientation of the soul toward YHWH. ANE context: the patron-client relationship required active attendance at the patron's house; the theology transforms this into patient, seeking attendance on YHWH.</p>",
    "26": "<p>V26: <em>tov veyachel vdumam litshuat YHWH</em> — it is good that one should wait quietly (<em>dumam</em>, in silence) for the salvation of YHWH. The <em>dumiyyah</em>/<em>dumam</em> (silence, stillness) vocabulary appears in the psalms of trust (Ps 62:1, 5: for God alone my soul waits in silence; Ps 37:7: be still before YHWH and wait patiently for him). The silence is not passivity but the stilling of the inner tumult — the discipline of not filling the space with self-generated noise. The <em>yeshuat YHWH</em> (salvation of YHWH) is the name embedded: <em>Yeshua</em> is the shortened form of <em>Yehoshua</em> (YHWH saves).</p>",
    "27": "<p>V27: <em>tov lagever ki yissa ol bine'urav</em> — it is good for a man to bear the yoke in his youth. The <em>ol</em> (yoke) as a discipline metaphor appears throughout the prophets: Jer 27–28 (the yoke of Babylon as divine discipline not to be broken prematurely); Jer 31:18 (Ephraim's lament: you disciplined me like an untrained calf; bring me back). Accepting the yoke in youth means the discipline forms character before pride calcifies. The ANE background: yoke-training of oxen and mules was a feature of agricultural life that the prophets used extensively for covenantal obedience and submission.</p>",
    "28": "<p>The yod-acrostic (vv28–30). V28: <em>yeshev badad veyidom ki natal alav</em> — let him sit alone in silence when he has laid it on him. The <em>badad</em> (alone) vocabulary appears in 1:1 (Jerusalem sits alone) — the same word that described the city's desolation now describes the posture required in response to it. Sitting alone in silence is the mourning and purification posture (Lev 13:46 — the leprous person shall dwell alone; Job 2:13 — they sat with him on the ground seven days and seven nights). The theological logic: accepting the isolation of judgment rather than fleeing it is the beginning of restoration.</p>",
    "29": "<p>V29: <em>yitten be'afar pihu ulai yesh tiqvah</em> — let him put his mouth in the dust; perhaps there is yet hope (<em>ulai yesh tikvah</em>). The mouth-in-dust posture is the most extreme gesture of submission — prostration with the face pressed to the earth, as before a conquering king (Ps 72:9: may desert tribes bow before him, and his enemies lick the dust; Mic 7:17: they shall lick the dust like a serpent). The <em>ulai</em> (perhaps/maybe) of v29 is remarkable — not certainty but the hope that survives uncertainty. The full confession of weakness (mouth in the dust) precedes even the smallest hope-claim.</p>",
    "30": "<p>V30: <em>yiten lemakkahu lechi yisba beherpa</em> — let him give his cheek to the one who strikes, and let him be filled with insults. This posture — turning the cheek to the striker — is the posture of accepting shame as part of the discipline of judgment, not because the shame is deserved as personal moral failure but because the community judgment has come. Isa 50:6 (the Servant: I gave my back to those who strike, and my cheeks to those who pull out the beard; I hid not my face from disgrace and spitting) is the clearest OT model for this posture. The NT's use (Matt 5:39) connects it to the disciple's response to unjust treatment.</p>",
    "31": "<p>The kaph-acrostic (vv31–33). V31: <em>ki lo yizanach le'olam Adonai</em> — for the Lord will not cast off forever. The <em>ki</em> (for/because) launches the theological basis for the postures of vv28–30: the endurance of shame makes sense because the rejection is not permanent. YHWH's character guarantees an end to the judgment. The Psalms of trust use the same structure: suffering posture + covenant confidence in YHWH's non-abandonment (Ps 94:14: YHWH will not forsake his people; he will not abandon his heritage).</p>",
    "32": "<p>V32: <em>ki im hogah verachem kerov chasadav</em> — but though he causes grief, he will have compassion according to the abundance of his steadfast love. The <em>rav chesed</em> (abundance of steadfast love) is the covenantal formula from Exod 34:7 (keeping steadfast love for thousands) and Joel 2:13 (return to YHWH for he is gracious and merciful, slow to anger, and abounding in steadfast love). The <em>rav</em> (abundance) quantifies the divine character: the overflow of steadfast love exceeds even the depth of the judgment.</p>",
    "33": "<p>V33: <em>ki lo innah milibo vayageh benei ish</em> — for he does not afflict from his heart or grieve the children of men. <em>Millibo</em> (from his heart) — the heart is the seat of will and intention in Hebrew thought. This verse is the OT's clearest statement of divine reluctance toward judgment: the punishment is real and YHWH inflicts it, but it does not arise from the core of who he is. Ezek 18:23, 32 and 33:11 (I have no pleasure in the death of the wicked, says the Lord YHWH) extend this trajectory. The theological implication: judgment is remedial and temporary; steadfast love is essential and permanent.</p>",
    "34": "<p>The lamed-acrostic (vv34–36). V34: crushing underfoot (<em>daka tachat raglav kol asirei aretz</em>, to crush under one's feet all the prisoners of the earth). The lamed-acrostic concerns divine justice: YHWH does not approve of (does not see = Hebrew idiom for not approving, v36) crushing prisoners, perverting justice in the courts, or denying rights. The paradox: YHWH uses Babylon as his instrument of judgment (Jer 25:9: Nebuchadnezzar my servant) while not approving of Babylon's methods of cruelty (Isa 10:5–7: Assyria, the rod of my anger ... but he does not so intend and does not so think).</p>",
    "35": "<p>V35: to turn aside the right of a man in the presence of the Most High (<em>lehattot mishpat gever neged pene Elyon</em>). The juridical vocabulary — <em>mishpat</em> (justice/right), <em>neged pene</em> (before the face of) — places the courtroom before YHWH himself. ANE legal practice: major cases went before the king; the worst injustice was perverting justice in the king's presence. Here the injustice occurs before the Most High — the divine judge who sees all perversions of justice even those committed in his name.</p>",
    "36": "<p>V36: to subvert a man in his lawsuit — the Lord does not see (<em>Adonai lo ra'ah</em>). The <em>lo ra'ah</em> (does not see/approve) is the Hebrew idiom for disapproval: seeing what one does not sanction. The context of Babylonian brutality: YHWH used Babylon but never sanctioned its particular cruelties. This distinction becomes theologically important for understanding how YHWH uses evil nations without himself being evil — a theodicy the prophets develop (Isa 10; Hab 1–2).</p>",
    "37": "<p>The mem-acrostic (vv37–39). V37: <em>mi zeh amar vattehi Adonai lo tzivva</em> — who has spoken and it came to pass, unless the Lord has commanded it? The theodicy moves to the sovereignty of YHWH over all events. The rhetorical question assumes the answer: no one. Every event in history — including the fall of Jerusalem — occurs within YHWH's command-structure. Amos 3:6 (does disaster come to a city unless YHWH has done it?) and Isa 45:7 (I form light and create darkness; I make peace and create calamity — <em>ra</em>) express the same principle.</p>",
    "38": "<p>V38: <em>mippi elyon lo tetze hara'ot vehatov</em> — is it not from the mouth of the Most High that good and bad go forth? The <em>ra</em> (bad/evil/calamity) and <em>tov</em> (good) coming from the same divine mouth is the OT's theodicy of sovereignty: YHWH is the ultimate cause behind all historical events, whether experienced as good or bad. This is not moral evil but calamitous events (<em>ra</em> in Amos 3:6 is translated 'disaster/calamity'). The theological logic: if YHWH is sovereign over both, then both serve his purposes.</p>",
    "39": "<p>V39: <em>mah yit'onen adam chai gever al chet'av</em> — why should a living man complain, a man, about the punishment of his sins? The theodicy silences human complaint not by denying the suffering but by locating its cause: the covenant community brought this on itself. The ANE background: divine punishment for covenant violation was a common framework (the Hittite vassal treaties include curse-lists similar to Deut 28); the community would have understood that divine wrath follows covenant breach. The verse urges honest self-examination rather than resentment toward YHWH.</p>",
    "40": "<p>The nun-acrostic (vv40–42). V40: <em>nachapesa derachenu venachqorah venashuvah ad YHWH</em> — let us test and examine our ways, and return to the LORD. The <em>chaqar</em> (to search out/examine) is the vocabulary of thoroughgoing investigation. The call to <em>shuv</em> (return) is the standard repentance call of the prophets: Jer 3:12, 14, 22 (return, backsliding Israel); Hos 14:1 (return, O Israel, to YHWH your God). The community response shifts from individual gever-voice to first-person plural: the nation owns the judgment collectively.</p>",
    "41": "<p>V41: <em>nissa levavenu el kapayim el El bashamayim</em> — let us lift up our hearts and hands to God in heaven. The lifting of hands (<em>kappayim</em>) in prayer is the standard ANE and Israelite prayer posture (Exod 17:12; Ps 63:4; 1 Kings 8:22). The pairing of heart (<em>lev</em>) and hands is the OT's demand for internal alignment with external ritual: the prayer must come from the inner life, not merely be a performed gesture. Isa 1:15 (when you spread out your hands in prayer, I will hide my eyes ... your hands are full of blood) represents the failure of external ritual without inner alignment.</p>",
    "42": "<p>V42: <em>nachnu pasha'nu umararinu veatta lo salachtah</em> — we have transgressed and rebelled, and you have not forgiven. The confession is stark: past tense transgression acknowledged, present tense forgiveness not yet experienced. The <em>pashah</em> (to rebel/transgress — the word used for political rebellion against a sovereign) acknowledges the worst category of covenant violation. The unanswered prayer — you have not forgiven — is the honest cry of faith: confession has been made, but restoration has not yet come. This is the moment between repentance and reconciliation.</p>",
    "43": "<p>The samech-acrostic (vv43–45). V43: <em>sakota ba'af vetirdefenu haraagta lo chamalata</em> — you have wrapped yourself with anger and pursued us, killing without pity. The <em>sukkah</em>/<em>sakhah</em> (covering/wrapping) of divine wrath inverts the Exodus imagery: in the wilderness, YHWH wrapped himself in cloud to lead Israel (Exod 13:21; 14:19). Now he wraps himself in anger. The pursuit (<em>tirdefenu</em>) inverts Deut 28:7 (your enemies shall come out against you one way and flee before you seven ways) — now it is YHWH pursuing Israel.</p>",
    "44": "<p>V44: <em>sakota be'anan lekha me'avar tefilla</em> — you have wrapped yourself with a cloud so that no prayer can pass through. The cloud of divine presence that was the vehicle of communication (Exod 33:9: the pillar of cloud would descend and YHWH would speak with Moses) is now the barrier that blocks prayer. The besieged community's prayers found no access: the siege lasted 18 months with no divine intervention. The theological depth: the very symbol of divine-human communication has become the wall of silence.</p>",
    "45": "<p>V45: <em>sechiy uma'os tesimenu beqerev ha'ammim</em> — you have made us scum and garbage among the peoples. The <em>sechiy</em> (offscouring/refuse) and <em>ma'os</em> (rejected thing) are the vocabulary of ritual pollution and social outcasting. Among the nations, the destroyed city and its exiles were the lowest category: defeated people whose god had failed them. This is the nadir of the samech-section — the complete reversal of the election: instead of being YHWH's treasured possession (<em>segullah</em>, Exod 19:5), Israel is refuse among the peoples.</p>",
    "46": "<p>The ayin-acrostic (vv46–48). V46: all our enemies opened their mouths against us. The <em>ayin</em> letter begins <em>ayin</em> (eye) in Hebrew — and the ayin/pe section (vv46–54) is saturated with eye imagery (seeing, tears, weeping). V46: <em>patshu alenu pihem kol oyeveinu</em> — all our enemies have opened wide their mouths against us. The ANE taunt of the defeated: open mouth = contempt, mockery, reproach. Ps 22:7–8 (all who see me mock me; they wag their heads) uses the same imagery in the individual lament. The social shame of national defeat was the community's lived experience.</p>",
    "47": "<p>V47: <em>pachad vafachat haya lanu hashsha vehashhaver</em> — panic (<em>pachad</em>) and pit (<em>pachat</em>) have come upon us, devastation (<em>shoa</em>) and destruction (<em>shever</em>). The alliterative pairs — pachad/pachat and shoa/shever — create a drumbeat of total catastrophe. Isa 24:17–18 uses pachad/pachat/pach (terror/pit/trap) as a triple alliteration for unavoidable divine judgment. The ANE context: siege outcomes for the defeated included exactly these: panic (those who tried to flee), pits (traps set for escapees), devastation (economic), and destruction (physical).</p>",
    "48": "<p>V48: <em>pelagim mayim terad eini al shever bat ammi</em> — rivers of water run down from my eye over the destruction of the daughter of my people. The <em>pelagim mayim</em> (channels/rivers of water) is hyperbole that signals genuine lamentation in the ANE mourning tradition. The weeping prophet Jeremiah uses similar imagery (Jer 9:1: O that my head were waters, and my eyes a fountain of tears). The destruction (<em>shever</em>) of the daughter of my people — the same term used for a broken bone — signals the complete fracturing of the national body.</p>",
    "49": "<p>The pe-acrostic (vv49–51). V49: <em>eini nizzelah velo tidmeh me'ein hafsugot</em> — my eye flows without ceasing, without rest. The <em>en hafsugot</em> (without cessation/rest — H6314, pause/rest) describes the involuntary nature of grief's tears: they cannot be stopped. In the ANE mourning tradition, professional mourners were hired for public grief (Amos 5:16; Jer 9:17–18); genuine grief was marked by uncontrollable weeping. The switch from verse-by-verse acrostic to the flowing streams of tears in this section enacts the content: the very structure of the poem becomes the overflow it describes.</p>",
    "50": "<p>V50: <em>ad yashqif veyireh YHWH mishhamayim</em> — until the LORD looks down from heaven and sees. The looking-down of YHWH from heaven is the prayer-posture of the OT: YHWH must look down (Ps 14:2; 102:19; Isa 63:15) from his dwelling in the heavens to see the suffering of the people. The weeping flows until YHWH's gaze descends. The vertical movement (earth's tears rising, YHWH's gaze descending) structures the whole lament.</p>",
    "51": "<p>V51: <em>eini ollela lenafshi mikol benot iri</em> — my eye causes me pain on account of all the daughters of my city. The daughters of the city — the women and children who suffered most in the siege and its aftermath — are the collective object of the speaker's grief. Archaeological evidence from siege contexts (skeletal remains, written records) confirms that women and children bore the heaviest mortality burden in ancient city destructions. The <em>ayin</em>/<em>pe</em> section's eye-imagery (vv46–54) makes visible the grief that the whole body of the city shares.</p>",
    "52": "<p>The tzade-acrostic (vv52–54). V52: <em>tzod tzaduni katzippor oyevai chinnam</em> — those who were my enemies without cause hunted me like a bird. The bird-in-a-trap imagery is common in the Psalms of the righteous sufferer (Ps 124:7: we have escaped like a bird from the snare of the fowlers). <em>Chinnam</em> (without cause) is the vocabulary of innocent suffering (Job 2:3; Ps 35:19; 69:4 — those who hate me without cause). The poet identifies the gever's experience with the category of undeserved persecution, which creates the platform for the go'el (advocate) appeal that follows.</p>",
    "53": "<p>V53: <em>tzamtu vabor chayyi vayaddu even bi</em> — they flung me alive into the pit and cast a stone over me. The pit imagery (<em>bor</em>) and the stone sealing it directly echoes two OT narratives: Joseph thrown into the pit by his brothers (Gen 37:24) and Jeremiah thrown into the cistern with mud at the bottom and a stone rolled over it (Jer 38:6, 11). Both are stories of innocent suffering followed by divine rescue — the pattern that the gever's prayer anticipates. The stone-sealed pit is also the language of Sheol: death enclosed and inescapable from inside.</p>",
    "54": "<p>V54: <em>tzafu mayim al roshi amarti nigzarti</em> — water closed over my head; I said, I am cut off. The chaos-waters drowning imagery runs throughout the lament psalms: Ps 69:1–2 (the waters have come up to my neck; I have sunk in deep mire), Ps 88:7 (your wrath lies heavy upon me; you overwhelm me with all your waves), Jonah 2:3–6. <em>Nigzarti</em> (I am cut off) — the same root (<em>gazar</em>) used for cutting off a nation from existence. The confession of being at the absolute limit — cut off from life — is the precondition for the prayer that follows in vv55–57.</p>",
    "55": "<p>The qoph-acrostic (vv55–57). V55: <em>qarati shimcha YHWH mibor tachtiyot</em> — I called your name, O LORD, from the depths of the pit (<em>bor tachtiyot</em>, lowest pit). The <em>bor tachtiyot</em> (lowest pit) is the OT's language for the deepest Sheol (Ps 88:6: you have put me in the depths of the pit, in the regions dark and deep). Jonah 2:2 (out of the belly of Sheol I cried, and you heard my voice) uses identical rescue-from-the-pit vocabulary. The name-calling (<em>qarati shimcha</em>) is the act of invocation: summoning the covenant God by name is the basis of prayer (Joel 2:32; Acts 2:21).</p>",
    "56": "<p>V56: <em>qoli shamata al taalem oznekha lerevchati leshav'ati</em> — you heard my voice; do not hide your ear from my cry for relief. The confirmation (you heard) precedes the continuing petition (do not hide your ear). The <em>al ta'alem</em> (do not hide/cover) — the ear of YHWH is the channel of covenantal response; its covering is the blocking experienced in v44. The prayer from the depths has been heard — the petition is that the hearing continue through the rest of the crisis.</p>",
    "57": "<p>V57: <em>qaravta beyom eqra'ekha amarta al tira</em> — you came near in the day I called you; you said, Do not fear. The divine response formula <em>al tira</em> (do not fear) is the consolation oracle of the prophets — Isa 41:10, 13, 14; 43:1, 5; 44:2; 54:4 (all begin with <em>al tira</em>). YHWH's nearness in response to prayer is the experiential confirmation of covenant faithfulness: the God who seemed to have wrapped himself in an impenetrable cloud (v44) now comes near and speaks the word of comfort. This is the turning point from lament to confidence.</p>",
    "58": "<p>The resh-acrostic (vv58–60). V58: <em>ravta Adonai riyve nafshi ga'alta chayay</em> — you have taken up my cause (<em>rav ribi</em>), O Lord; you have redeemed my life. The <em>rav ribi</em> (took up my cause/plead my legal case) uses the vocabulary of the <em>go'el</em> (kinsman-redeemer): the legal advocate who champions the case of the powerless (Ruth 4; Job 19:25: I know that my redeemer/go'el lives). The past tense (<em>ravta</em>, you have plead; <em>ga'alta</em>, you have redeemed) is the Hebrew perfect of confident anticipation — so certain of the outcome that it is described as already complete.</p>",
    "59": "<p>V59: <em>ra'ita YHWH avotati sheftah mishpati</em> — you have seen the wrong done to me, O LORD; judge my cause. The divine witness and the divine judge are the same: YHWH who sees the injustice is also the one who has the power and responsibility to rectify it. ANE context: the appeal to the divine judge when the earthly courts have failed is a common motif in Mesopotamian prayer literature (the Babylonian 'Poem of the Righteous Sufferer' appeals similarly to the divine judge). Israel's distinctive claim: YHWH is not merely a last resort but the court of ultimate appeal.</p>",
    "60": "<p>V60: <em>ra'ita kol niqmatam kol machshevotam li</em> — you have seen all their vengeance, all their plots against me. The divine omniscience (seeing all) is the basis for the appeal: YHWH has seen everything — the enemies' plans, their malice, their celebration of Jerusalem's fall. Ps 94:9–11 develops this: YHWH who planted the ear, does he not hear? He who formed the eye, does he not see? He who disciplines the nations, does he not rebuke? He knows the thoughts of man. The complete divine knowledge is both consolation and the basis for justice.</p>",
    "61": "<p>The shin-acrostic (vv61–63). V61: <em>shamata cherpatan YHWH kol machshevotam alai</em> — you have heard their reproach (<em>cherpah</em>), O LORD, all their plots against me. The <em>shama</em> (hearing) of YHWH is comprehensive: in the resh-section YHWH heard the prayer of the gever (v56); in the shin-section he hears the reproach of the enemies. Both hearings serve the purpose of justice: the cry is heard from below, the mockery is heard from around, and YHWH holds both.</p>",
    "62": "<p>V62: <em>siftei qamay vehegionatam alai kol hayom</em> — the lips of my assailants and their plots against me all the day long. The lip/speech vocabulary — what the enemies say, plot, and murmur — is the social dimension of the shame: the ongoing commentary of the victors about the defeated. ANE defeat meant being talked about in contemptuous terms indefinitely: treaty documents, royal inscriptions, and victory annals all included the verbal humiliation of the defeated. YHWH's hearing of the enemies' words puts that ongoing humiliation under divine scrutiny.</p>",
    "63": "<p>V63: <em>shivtam veqimatan abit anginatan lam</em> — their sitting and rising — I am their mocking song. The <em>shevet veqimah</em> (sitting and rising) is the ANE merism for all activity: everything they do, all day long, includes mocking the gever/community. This merism appears also in Deut 6:7 (the Shema is to be recited sitting and rising — all activity). The enemies' total activity has the defeated community as its object of scorn. The comprehensive scope of YHWH's observation (vv60–63) matches and exceeds the comprehensive scope of the enemies' mockery.</p>",
    "64": "<p>The taw-acrostic (vv64–66) closes the chapter with the final letter of the Hebrew alphabet. The taw (<em>tav</em>) in the ancient script was written as an X or cross-mark — it was the last letter and the mark used for completion. V64: <em>tasheev lahem gemul YHWH keema'seh yadeihem</em> — repay them according to their deeds, O LORD, according to the work of their hands. The lex talionis principle (repay according to deeds) is a standard covenantal and legal principle: Deut 19:19; Ps 28:4; 94:2. This is not private vengeance but the covenantal call for YHWH to be consistent — to apply to the enemies the same measure-for-measure principle that he applied to Israel.</p>",
    "65": "<p>V65: <em>titen lahem meghinat lev taalachetcha lahem</em> — give them dullness of heart; your curse be upon them. The hardened heart (<em>meghinat lev</em>, covering of the heart, dullness/obstinacy) is the divine judicial response to persistent rejection: Exod 4:21; 9:12 (I will harden Pharaoh's heart); Isa 6:10 (make the heart of this people dull); Rom 1:24–28 (God gave them over). The curse (<em>ta'alachetcha</em>, your curse) is the covenant curse-vocabulary of Deut 28, here invoked over those who enacted what that curse threatened.</p>",
    "66": "<p>V66: <em>tirdof be'af vetashmidim mittachat shemei YHWH</em> — pursue them in anger and destroy them from under the heavens of the LORD. The closing verse of the triple acrostic invokes the same language YHWH used as a threat against Israel in Deut 9:14 (let me alone, that I may destroy them and blot out their name from under heaven). What YHWH threatened against Israel is now called down upon Israel's destroyers. The taw-letter closes the alphabet of suffering and the alphabet of justice: aleph through tav, the full range of human experience has been voiced, and now the full claim of divine justice is made. The poem's structure is complete.</p>"
  },
  "4": {
    "1": "<p>Chapter 4 is a single acrostic (one verse per letter, aleph through taw, 22 verses) — structurally less dense than ch3's triple acrostic, but its imagery is the most viscerally concrete in the book. V1 opens with the reversal of sacred metals: <em>eich yu'am zahav yishne haketem hatov</em> — how the gold has grown dim, how the pure gold is changed! The <em>ketem ha-tov</em> (fine/pure gold) refers to the gold of the temple furnishings — the ark's mercy seat, the lampstand, the altar overlays (1 Kings 6:20–22; 7:48–50). These had been the most precious objects in the world to Israel; they are now scattered at the corner of every street.</p>",
    "2": "<p>V2: <em>benei Tziyon hameqarim mesulaim baketam eicha nechshvu lenivlei cheres</em> — the precious sons of Zion, worth their weight in fine gold, how they are regarded as earthen pots, the work of a potter's hands. The temple vocabulary is applied to people: <em>benei Tziyon</em> (sons of Zion) were valued like gold; now they are valued like clay (<em>chomer</em>, H2563 — the raw material for the cheapest functional vessels). The ANE ceramic tradition: common pottery was the mass-produced utilitarian ware; gold objects were royal and sacred. The inversion is complete: sacred-gold people now clay-pot people.</p>",
    "3": "<p>V3: <em>gam tanim chalutzu shad heniqu gurezaleihen bat ammi le'akzar kaya'enim bamidbar</em> — even jackals bare the breast and nurse their young, but the daughter of my people has become cruel, like the ostriches in the wilderness. The ostrich proverbially abandoned her eggs (Job 39:14–16: she leaves her eggs to the earth and lets them be warmed on the ground, forgetting that a foot may crush them). Siege-starvation had destroyed maternal instinct — the ultimate sign of social collapse. The comparison to jackals (normally associated with waste and desolation) nursing their young makes the point more sharply: even the animal associated with ruin is a better mother than Jerusalem's women under siege conditions.</p>",
    "4": "<p>V4: <em>davaq lashon yoneq el chikko battzama olalim sha'alu lechem poress ein lahem</em> — the tongue of the nursing infant sticks to the roof of its mouth for thirst; the children beg for food, but no one gives to them. The specific physiological detail — tongue adhering to the palate in severe dehydration — is medically precise. Dehydration causes the mouth's mucous membranes to dry and thicken; the tongue literally adheres. This is the experience of children during the 586 BCE siege, which lasted from approximately January 588 to July 586 BCE — eighteen months during which food and water supplies were exhausted.</p>",
    "5": "<p>V5: <em>ha'ochelim lema'adannim nashammu bechutzot immusei ha'argaman chibbequ ashpatot</em> — those who feasted on delicacies perish in the streets; those who were brought up in purple embrace ash heaps. The <em>ma'adannim</em> (delicacies) were the food of the wealthy and priestly classes who ate the temple offerings and the first fruits. The <em>argaman</em> (purple) was the most expensive dye in the ANE, extracted from murex sea snails — royal garments and temple hangings were dyed purple (Exod 26:31; 1 Kings 10:12; Ezek 27:7). The purple-clad are now on ash heaps: the socioeconomic inversion is total.</p>",
    "6": "<p>V6: <em>vayigdal avon bat ammi mechattath Sedom hahapukha cheraga velo chalu vah yadayim</em> — for the punishment of the daughter of my people has been greater than the punishment of Sodom, which was overthrown in a moment, and no hands were wrung over it. The theological claim is shocking: Jerusalem's punishment exceeds Sodom's. The reasoning: Sodom was destroyed instantly (Gen 19:24–25 — the LORD rained on Sodom and Gomorrah sulfur and fire ... he overthrew those cities and all the valley); Jerusalem's prolonged siege, starvation, and exile was a slower, more agonizing destruction. The comparison intensifies the catastrophe's theological weight: the covenant people, who had more light and more responsibility, received a more severe judgment.</p>",
    "7": "<p>V7: <em>zakku nezireha misheleg tzachu mechalav ademu pinim mipeneinim sappir gizratam</em> — her consecrated ones (<em>nezireha</em>, Nazirites or royalty) were purer than snow, whiter than milk, their bodies more ruddy than corals, the beauty of their appearance like lapis lazuli. The temple-color vocabulary maps onto the tabernacle/temple hangings: white (linen, Exod 26:1), red/crimson (scarlet, Exod 26:31), and blue/lapis (<em>tekhelet</em>, the blue-violet thread used in priestly garments, Exod 28:6). The consecrated ones embodied the temple aesthetics; their transformation in v8 represents the temple's own destruction.</p>",
    "8": "<p>V8: <em>chashach mishehor to'aram lo nikkeru bachutzot tzaphedah orram al atzeman yavesh haya ke'etz</em> — now their face is blacker than soot; they are not recognized in the streets; their skin has shriveled on their bones; it has become as dry as wood. The blackening of the face from severe starvation and exposure (not the dark complexion of heat, but the specific gray-black pallor of the dying) is documented in ancient sieges and famines. The skin shrinking onto the bones describes advanced starvation: when subcutaneous fat is completely consumed, the skin lies directly on the skeleton. Former acquaintances cannot recognize them — the social identity formed by appearance has been erased.</p>",
    "9": "<p>V9: <em>tovim hayu challelei cherev mechalalei ra'av shehein yazuvu medukkarim mittenuvot sade</em> — happier were the victims of the sword than the victims of hunger, who wasted away, pierced by lack of the fruits of the field. The judgment that sword-death is preferable to starvation-death reflects the lived reality of ancient siege warfare. Death by sword was relatively swift; starvation was a weeks-long deterioration through stages of increasing debility. This is not rhetoric but the frank assessment of those who survived the siege and compared its different forms of suffering. The phrase encapsulates the siege's particular horror.</p>",
    "10": "<p>V10: <em>yedei nashim rachamaniyot bishlu yaldeihen hayu levarot lamo beshabar bat ammi</em> — the hands of compassionate women have boiled their own children; they became their food during the destruction of the daughter of my people. This is the literalization of Deuteronomy 28:56–57: the most tender and delicate woman, so delicate that she would not venture to put the sole of her foot on the ground, will begrudge to the husband she loves and to her son and to her daughter the afterbirth that comes out from between her feet and the children she bears, because lacking everything she will eat them secretly. The covenant curse is enacted. 2 Kings 6:28–29 records this also occurring during the Aramean siege of Samaria, confirming it was not hyperbole.</p>",
    "11": "<p>V11: <em>kila YHWH et chamato shafach charon apo vayattet esh beTziyon vattokal yesodoteha</em> — the LORD gave full vent to his wrath; he poured out his burning anger, and he kindled a fire in Zion that consumed its foundations (<em>yesodot</em>). The burning of the temple and its foundations was the defining act of the Babylonian destruction (2 Kings 25:9: he burned the house of the LORD and the king's house and all the houses of Jerusalem; every great house he burned down). The <em>yesodot</em> (foundations) of the temple and city — which Ps 87:1 celebrated (on the holy mount stands the city he founded) — are consumed, ending the covenant-architecture that grounded Israelite worship.</p>",
    "12": "<p>V12: <em>lo he'eminu malkhei eretz vekol yoshevei tevel ki yavo tzar veoyev besharei Yerushalayim</em> — the kings of the earth did not believe, nor did any of the inhabitants of the world, that foe or enemy could enter the gates of Jerusalem. This reflects both the historical near-miracle of 701 BCE (Sennacherib's failed siege — the Sennacherib prism confirms he did not capture Jerusalem) and the theological Zion traditions: YHWH dwells in Zion; Zion is inviolable (Ps 46:1–3; 48:2–3, 12–13). The fall of Jerusalem in 586 BCE shattered not just a city but the entire theological worldview built on the Zion psalms. The universality of the shock (<em>kol yoshevei tevel</em>, all inhabitants of the world) signals that this was not a local event but a cosmic theological rupture.</p>",
    "13": "<p>V13: <em>mechattot neviyeha avonot kochaneha hashofkhim beqirbah dam tzaddiqim</em> — because of the sins of her prophets and the iniquities of her priests, who shed in the midst of her the blood of the righteous. The theological cause of the destruction is identified as religious-establishment corruption. Jer 23:11–15 provides the detailed background: both prophet and priest are ungodly; in my house I have found their evil; the prophets of Jerusalem commit adultery and walk in lies; they prophesy by Baal and lead my people astray. The shedding of righteous blood — including the murder of the prophet Uriah (Jer 26:20–23) and the constant persecution of Jeremiah himself — made the religious leadership responsible for the covenant community's collapse.</p>",
    "14": "<p>V14: <em>na'u ivrim bachutzot nig'u badam ubal yuchlu yig'u bilbushehem</em> — they wandered, blind, through the streets; they were so defiled with blood that no one was able to touch their garments. The irony of priestly impurity: those whose vocation was to maintain ritual purity and to declare others clean or unclean (Lev 13–15; Ezek 44:23) have become the primary source of blood-pollution. The blood of the unjustly murdered clings to them, making them untouchable. The blindness (<em>ivrim</em>) echoes the judgment oracle: those who claimed to be spiritual guides are now blind wanderers — Zeph 1:17; Isa 59:9–10.</p>",
    "15": "<p>V15: <em>suru tame qeru lahem suru suru al tigga'u ki natsenu gam na'u amru baggoyim lo yosifu lagur</em> — 'Away! Unclean!' people cried at them; 'Away! Away! Do not touch!' So they became fugitives and wanderers. The prescribed cry of the leper in Lev 13:45 (<em>tame tame</em>, unclean, unclean) — designed to warn others away from ritual contamination — is now applied to the priests and prophets who had contaminated themselves through injustice. The complete reversal: the purifiers are expelled. The nations say of them, they shall no longer sojourn there — the ultimate exile, even from the refuge of other nations.</p>",
    "16": "<p>V16: <em>penei YHWH challeqam lo yoshif lehabbitem penei kohanim lo nasa'u u-zeqenim lo chaneinu</em> — the LORD himself has scattered them; he will regard them no more; no honor was shown to the priests, no favor to the elders. The <em>penei YHWH</em> (face/presence of YHWH) that scattered them inverts the Aaronic blessing: may YHWH lift up his countenance upon you and give you peace (Num 6:26). Now the face of YHWH has turned away — <em>lo yoshif lehabbitam</em> (will regard them no more). The priestly elders who were supposed to be honored (Lev 19:32; 1 Tim 5:17) are shown no honor because they failed in their sacred trust.</p>",
    "17": "<p>V17: <em>odeynu tiklenah eineinu el ezratenu hebel betzipiyatenu tzippinu el goy lo yoshi'a</em> — our eyes failed, ever watching vainly for help; in our watching we watched for a nation that could not save. The failed Egyptian alliance is the historical background: Jeremiah 37:5–11 records that Pharaoh Hophra's army approached Jerusalem and the Babylonians temporarily withdrew from the siege — but then the Babylonians returned after the Egyptians pulled back. Jer 37:9–10 contains YHWH's warning through Jeremiah: Do not deceive yourselves ... the Egyptians will return to Egypt. The political hope that collapsed in 586 BCE was the Egyptian alliance that Jeremiah had consistently warned against (Jer 46; Ezek 17:15–17).</p>",
    "18": "<p>V18: <em>tzadu tze'adeynu milelekhet birchevoteynu qarev qitzenu male' yamenu ki ba qitzenu</em> — they dogged our steps so that we could not walk in our streets; our end drew near; our days were numbered, for our end had come. The siege tactics that prevented movement within and outside the city are described with military precision. <em>Tzadu tzaedeynu</em> (tracked/hunted our steps) — the Babylonian army created a perimeter that prevented escape or supply. Jer 52:7 records the final breach: when the city walls were broken through, the soldiers of war fled by night by the way of the gate between the two walls, by the king's garden. The tracking described here made even this narrow escape route dangerous.</p>",
    "19": "<p>V19: <em>qallu rodefeynu minisrey shamayim al heharim delaqunu bamidbar aravenuu</em> — our pursuers were swifter than the eagles in the heavens; they chased us on the mountains; they lay in wait for us in the wilderness. Deut 28:49 had threatened exactly this: YHWH will bring against you a nation from far away, from the end of the earth, swooping down like an eagle, a nation whose language you do not understand. The Babylonian army's pursuit of Zedekiah and the refugees fulfills this curse literally: Zedekiah fled at night and was caught in the plains of Jericho (2 Kings 25:4–6). The eagle-swiftness of the Babylonian cavalry made escape impossible.</p>",
    "20": "<p>V20: <em>ruach apeynu meshiach YHWH nilkad bishkhtotam asher amarna betzel'o nichyeh baggoyim</em> — the LORD's anointed (<em>meshiach YHWH</em>), the breath of our nostrils (<em>ruach apeynu</em>), was caught in their pits, of whom we said, 'Under his shadow we shall live among the nations.' The capture of Zedekiah (2 Kings 25:4–7: the Babylonians caught him in the plains of Jericho; they killed his sons before his eyes; they put out his eyes and bound him with bronze shackles) is the loss of the Davidic king who represented the covenant community's corporate life. <em>Ruach apeynu</em> (the breath of our nostrils) — the Davidic king was the community's vital breath, its corporate animating principle. The Davidic covenant (2 Sam 7) had promised that the king's shadow would be the community's shelter; now that shadow is gone.</p>",
    "21": "<p>V21: <em>sisi vismachi bat Edom yoshevet be'eretz Utz gam alayich ta'avor hakos tishkeri vetit'arri</em> — rejoice and be glad, O daughter of Edom, you who dwell in the land of Uz! But to you also the cup shall pass; you shall become drunk and strip yourself bare. The sarcastic address to Edom — rejoice while you can — sets up the reversal: Edom's turn is coming. Ps 137:7 records Edom's role in Jerusalem's fall (remember, O LORD, against the Edomites the day of Jerusalem, how they said 'Lay it bare, lay it bare, down to its foundations!'). Obadiah 10–14 details Edom's standing by and participating in the destruction. The cup of divine wrath (<em>kos</em>) — Jer 25:15–26 lists nations that must drink it; Edom is among them (Jer 49:12–13). <em>Ba-eretz Utz</em> — the land of Uz is also where Job dwelt (Job 1:1), adding a layer of suffering-and-justice resonance.</p>",
    "22": "<p>V22: <em>tamm avonekh bat Tziyon lo yoshif lehaglotekh paqad avonekh bat Edom gilah al chattotayikh</em> — your punishment is complete, O daughter of Zion; he will keep you in exile no longer; but he will punish your iniquity, O daughter of Edom; he will uncover your sins. <em>Tamm avonekh</em> (your punishment is complete/finished) — the same vocabulary as Isa 40:2 (speak tenderly to Jerusalem ... that her warfare has ended, that her iniquity is pardoned, that she has received from YHWH's hand double for all her sins). The completion of punishment is simultaneously the beginning of restoration: once the debt is paid, the exile ends. The closing verse of ch4 thus contains the seed of hope that ch5 will develop: Zion's punishment is finished; Edom's is coming. The contrast is the structure of covenant justice — the covenant people suffer fully and are restored; the nations that abused them face their own accounting.</p>"
  }
}

LAM_CHRIST = {
  "1": {
    "12": "<p>A type: 'Is it nothing to you, all you who pass by? Look and see if there is any sorrow like my sorrow, which was brought upon me, which the LORD inflicted on the day of his fierce anger.' The suffering of Jerusalem — the Daughter of Zion who has suffered at YHWH's hand for her sins — is one of the OT's primary types of Christ's passion. The NT passion accounts use the Lamentations framework: the mockers who wag their heads at the crucified Jesus echo Lamentations (Lam 2:15: 'all who pass by clap their hands at you; they hiss and wag their heads at the daughter of Jerusalem'; Matt 27:39). But the typological inversion is crucial: Jerusalem suffers for her own sins; Christ suffers for ours. The language of innocent suffering that Lamentations applies to the city becomes, in the NT, applicable to the one who is truly innocent.</p>"
  },
  "3": {
    "22": "<p>A direct revelation: 'The steadfast love of the LORD never ceases; his mercies never come to an end; they are new every morning; great is your faithfulness.' This confession — the OT's most concentrated statement of divine covenantal faithfulness — is the foundation of NT assurance. Paul says 'neither death nor life ... shall be able to separate us from the love of God in Christ Jesus our Lord' (Rom 8:38-39): the love the Preacher of Lamentations confessed in the ruins of Jerusalem is the love that cannot be severed by anything. Christ's resurrection is the supreme demonstration of the <em>chesed</em> that Lamentations confesses: even through the cross — the ultimate expression of divine wrath — the steadfast love did not fail.</p>"
  }
}

# ============================
# HOSEA
# ============================

HOSEA_ECHO = {
  "1": {
    "10": [
      {"type": "fulfillment", "target": "Rom 9:25-26", "note": "And in the place where it was said to them You are not my people it shall be said to them Children of the living God — Paul cites Hos 1:10 and 2:23 as OT support for Gentile inclusion: what YHWH said about restoring estranged Israel is applied to the calling of the Gentiles into the people of God; the not-my-people becoming my-people is the inclusive dynamic of the new covenant"}
    ]
  },
  "2": {
    "23": [
      {"type": "fulfillment", "target": "1 Pet 2:10", "note": "I will say to Lo-ammi You are my people; and he shall say You are my God — Peter applies Hosea's restoration promise to the church: once you were not a people, but now you are God's people; the covenant formula's restoration (you are my people/I am your God) is fulfilled in Christ's reconciling work"}
    ]
  },
  "6": {
    "6": [
      {"type": "fulfillment", "target": "Matt 9:13", "note": "For I desire steadfast love and not sacrifice, the knowledge of God rather than burnt offerings — Jesus quotes Hos 6:6 twice (Matt 9:13; 12:7) in defense of his association with sinners and his disciples' plucking grain on the Sabbath; the priority of covenant love over ritual is Jesus's critique of Pharisaic misapplication of the law"}
    ]
  },
  "11": {
    "1": [
      {"type": "fulfillment", "target": "Matt 2:15", "note": "Out of Egypt I called my son — Matthew cites Hos 11:1 as fulfilled in the flight to Egypt and the return: as YHWH called Israel (his son) out of Egypt in the Exodus, so Jesus (the true Son) recapitulates Israel's history; Jesus is the new Israel who succeeds where Israel failed"}
    ]
  }
}

HOSEA_ORIGINAL = {
  "11": {
    "1": "<p><strong>ki naar Yisrael vaehavuhu umimitzraim qarati livni</strong>: 'When Israel was a child, I loved him, and out of Egypt I called my son.' Matthew's citation of Hos 11:1 in Matt 2:15 is one of the NT's most discussed typological uses of the OT — because Hosea 11:1 in its original context is clearly not a predictive prophecy but a historical statement about the Exodus. Matthew's method is typological recapitulation: Jesus is the new Israel, the true Son of God who goes down to Egypt and is called out again; what happened to the nation in type is fulfilled in the person of the Messiah in antitype. This reading was not arbitrary: it was grounded in the OT's identification of Israel as YHWH's 'son' (Exod 4:22-23) and the expectation that the Messiah would recapitulate and fulfill Israel's story.</p>"
  }
}

HOSEA_CONTEXT = {
  "1": {
    "1": "<p>Hosea prophesied in the northern kingdom of Israel ca. 755-725 BCE, the final decades before Assyria destroyed Samaria (722 BCE). His marriage to Gomer — a woman who proved unfaithful — is the enacted metaphor of YHWH's relationship with Israel: YHWH's faithful covenant love (hesed) in the face of Israel's persistent idolatry (harlotry). The marriage metaphor for the YHWH-Israel covenant (developed also in Jeremiah 2-3, Ezekiel 16, and Isaiah 54) is Hosea's central theological contribution: covenant violation is not merely law-breaking but adultery, a betrayal of the intimate covenant-love relationship. The NT develops the bridegroom-bride metaphor for Christ-church (Eph 5:25-32; Rev 19:7-9) directly in line with Hosea's framework.</p>"
  }
}

HOSEA_CHRIST = {
  "11": {
    "1": "<p>A type: 'Out of Egypt I called my son.' The Hosea 11:1 citation in Matthew 2:15 reveals the NT's typological method: the Exodus — YHWH calling Israel his son out of Egypt — is recapitulated in miniature by the holy family's flight to Egypt and return. Jesus is the true Son of God where Israel was the representative son; Jesus is the true Israel who succeeds where Israel repeatedly failed. The NT development of this recapitulation: Israel spent 40 years in the wilderness and failed (Num 14); Jesus spent 40 days in the wilderness and prevailed (Matt 4). Israel crossed the Jordan under Joshua and conquered imperfectly; Jesus was baptized in the Jordan and accomplished the complete conquest of sin and death. The Exodus story is not just a historical event that Jesus parallels — it is the template YHWH designed to interpret what his Son would do.</p>"
  }
}

# ============================
# JOEL
# ============================

JOEL_ECHO = {
  "2": {
    "28": [
      {"type": "fulfillment", "target": "Acts 2:16-21", "note": "I will pour out my Spirit on all flesh — Peter on the Day of Pentecost cites Joel 2:28-32 as fulfilled in the Spirit's outpouring: this is what was uttered through the prophet Joel; the universal Spirit-gift (all flesh, sons and daughters, young and old, male and female, servant and free) is the new covenant's democratization of prophetic access to God"},
      {"type": "fulfillment", "target": "Acts 2:21", "note": "And it shall come to pass that everyone who calls on the name of the LORD shall be saved — Joel's salvation promise is cited by Peter (Acts 2:21) and Paul (Rom 10:13) as the OT basis for universal gospel accessibility: the LORD whose name saves is identified with Jesus, Lord and Christ (Acts 2:36)"}
    ]
  }
}

JOEL_ORIGINAL = {
  "2": {
    "28": "<p><strong>vehaya acharei chen eshpoch et ruchi al kol basar venivve'u bneichem uvnotechem ziknechem chalomot yachalomun bachureichem cheziyonot yiru</strong>: 'And it shall come to pass afterward, that I will pour out my Spirit on all flesh; your sons and your daughters shall prophesy, your old men shall dream dreams, and your young men shall see visions.' The universal Spirit-outpouring prophesied in Joel 2:28-32 is the most significant single prophecy cited in the NT's account of Pentecost. The key phrase is <em>kol basar</em> (all flesh): unlike the selective, temporary Spirit-anointing of specific judges, prophets, and kings in the OT, the new covenant Spirit will be given to all — removing the mediatorial hierarchy that required prophets and priests to relay YHWH's word to the people. This is Jeremiah 31:34 ('no longer will each person teach his neighbor, for they will all know me') from the pneumatological angle.</p>"
  }
}

JOEL_CONTEXT = {
  "1": {
    "1": "<p>Joel is undated — no contemporary king is mentioned — but it is typically placed in the post-exilic period (late 5th-early 4th century BCE) based on its references to the temple cult and its post-exilic vocabulary. The book's structure: a devastating locust plague (chs. 1-2:11) serves as the occasion for a call to repentance (2:12-17), followed by YHWH's promise of restoration (2:18-3:21). The locust plague is both a literal agricultural disaster and the harbinger of the Day of the LORD — the pattern of divine judgment working through historical events that will culminate in the final eschatological judgment. Joel is the OT prophet most cited in the NT on the Day of Pentecost, making his prophecy of the Spirit's universal outpouring the bridge between the Old and New covenant eras.</p>"
  }
}

JOEL_CHRIST = {
  "2": {
    "32": "<p>A fulfillment: 'And it shall come to pass that everyone who calls on the name of the LORD shall be saved.' Peter (Acts 2:21) and Paul (Rom 10:13) both cite Joel 2:32 as fulfilled in the gospel proclamation: the 'name of the LORD' whose invocation brings salvation is now identified as Jesus, whom God has made both Lord and Christ (Acts 2:36). The typological identification is clear: YHWH's name in the OT = Jesus's name in the NT. This is not a revision of the OT but the NT's claim that YHWH's name and Jesus's name are the same divine identity now disclosed fully in the incarnation. The universal accessibility of salvation ('everyone who calls') removes the national and ethnic boundaries that had characterized the OT covenant community.</p>"
  }
}

# ============================
# AMOS
# ============================

AMOS_ECHO = {
  "5": {
    "18": [
      {"type": "allusion", "target": "1 Thess 5:2", "note": "Woe to you who desire the day of the LORD — Amos warns that the Day of the LORD will be darkness not light for the presumptuous; Paul says the day of the Lord comes like a thief in the night; both challenge the assumption that the Day of the LORD is automatically good news for those who consider themselves God's people"}
    ]
  },
  "9": {
    "11": [
      {"type": "fulfillment", "target": "Acts 15:16-17", "note": "I will raise up the booth of David that is fallen — James cites Amos 9:11-12 at the Jerusalem Council as the OT justification for Gentile inclusion without circumcision; the restoration of the Davidic dynasty (the fallen booth) is being fulfilled in the Messiah Jesus, and the nations seeking the LORD follows from this restoration"}
    ]
  }
}

AMOS_ORIGINAL = {
  "9": {
    "11": "<p><strong>bayom hahu aqim et sukat David hanofelet vegadarta et pirzeihen vaharisotyav aqim uvenituha keyeme olam</strong>: 'In that day I will raise up the booth of David that is fallen and repair its breaches, and raise up its ruins and rebuild it as in the days of old.' The 'fallen booth of David' is an image of the Davidic dynasty in ruins — either the northern kingdom's secession (931 BCE) or the Babylonian destruction of the Davidic throne (586 BCE). James's citation at the Jerusalem Council (Acts 15:16-17) reads the restoration as the messianic reign of Jesus: the booth is raised; now the Gentiles ('all the nations who are called by my name', v. 12 in the LXX, which differs from the MT) stream in. The LXX variant makes the Gentile-inclusion application cleaner; James uses the LXX version. This is not a mistaken quotation but a deliberate use of the LXX rendering that the Spirit has superintended to carry the intended typological meaning.</p>"
  }
}

AMOS_CONTEXT = {
  "1": {
    "1": "<p>Amos prophesied ca. 760-750 BCE in the northern kingdom under Jeroboam II, a period of remarkable prosperity and military success — and of corresponding social injustice and covenant neglect. Amos is the first of the classical writing prophets and the OT's most sustained advocate for social justice: the Day of the LORD will expose the oppression of the poor (5:11-12), the corruption of the courts (5:12), the religious hypocrisy of the sanctuaries (5:21-24: I hate, I despise your feasts ... let justice roll down like waters). His social critique is grounded in covenant theology: YHWH's covenant with Israel demands covenant justice in the community; religious observance without ethical faithfulness is an abomination.</p>"
  }
}

AMOS_CHRIST = {
  "9": {
    "11": "<p>A fulfillment: 'In that day I will raise up the booth of David that is fallen.' James's application of Amos 9:11-12 at the Jerusalem Council (Acts 15:16-17) identifies the fulfillment: the resurrection of Christ is the raising of the fallen Davidic dynasty in its ultimate form. The 'booth of David' — the Davidic covenant and its dynastic promise — lay in ruins from 586 BCE onward; no Davidic king sat on an independent throne. The risen Jesus, enthroned at the Father's right hand (Acts 2:34-36), is the restored Davidic ruler whose reign brings in the nations. The Gentile mission is therefore not a deviation from the OT prophetic program but its very fulfillment: 'the remnant of mankind and all the nations who are called by my name' (Acts 15:17, citing Amos 9:12 LXX) stream into the reestablished Davidic kingdom.</p>"
  }
}

# ============================
# OBADIAH
# ============================

OBAD_ECHO = {
  "1": {
    "4": [
      {"type": "allusion", "target": "Luke 1:52", "note": "Though you soar aloft like the eagle, though your nest is set among the stars, from there I will bring you down — YHWH's judgment of Edom's pride; Mary's Magnificat: he has brought down the mighty from their thrones; the pride-and-fall pattern of Obadiah is the structure of divine reversal that the Magnificat celebrates"}
    ],
    "15": [
      {"type": "allusion", "target": "Rev 16:19", "note": "The day of the LORD is near upon all the nations. As you have done it shall be done to you — the lex talionis principle applied to the Day of the LORD; the great city was split and the nations drank from the cup of YHWH's wrath; Obadiah's principle of nations receiving what they did to Israel reaches its ultimate form in Revelation's final judgment"}
    ]
  }
}

OBAD_ORIGINAL = {
  "1": {
    "21": "<p><strong>vealu moshim behar tziyon lishpot et har Esav vehaitah lADONAI hamelukah</strong>: 'Saviors shall go up to Mount Zion to rule Mount Esau, and the kingdom shall be the LORD's.' Obadiah's final verse is the OT's shortest prophetic book's most expansive declaration: the kingdom belongs to YHWH. Edom (the persistent enemy of Israel, descended from Esau) will be judged; the deliverers (<em>moshim</em>, saviors/deliverers) will ascend Zion; the kingdom is YHWH's alone. The NT takes the <em>moshim</em> (saviors/deliverers) as the saints who reign with Christ (Rev 20:4-6) and the kingdom as Christ's eternal reign (Rev 11:15).</p>"
  }
}

OBAD_CONTEXT = {
  "1": {
    "1": "<p>Obadiah is the shortest book in the OT (21 verses) and is addressed entirely to Edom — the nation descended from Esau, the brother of Jacob/Israel. The oracle condemns Edom for standing aloof (v. 11) or actively participating in Jerusalem's destruction (the context is almost certainly the Babylonian destruction of 586 BCE, when Edomites reportedly aided the attackers and blocked Jewish refugees, Obad 12-14). The Edom-Israel enmity runs throughout the OT from Genesis (Esau-Jacob) through Numbers (Edom refuses passage to Moses), 1 Samuel (David's wars), and the post-exilic period. Edom becomes in the Prophets a symbol for the hostile nations in general (Isa 34; Ezek 35; Mal 1:2-5), and its final judgment is the type of all anti-God hostility that will be judged on the eschatological Day of the LORD.</p>"
  }
}

OBAD_CHRIST = {
  "1": {
    "21": "<p>A shadow: 'Saviors shall go up to Mount Zion to rule Mount Esau, and the kingdom shall be the LORD's.' Obadiah's closing declaration — the kingdom belongs to YHWH — is the OT's most compact eschatological statement. The NT's fulfillment: 'The kingdom of the world has become the kingdom of our Lord and of his Christ, and he shall reign forever and ever' (Rev 11:15). The deliverers who ascend Zion are the saints who reign with Christ in the new creation (Rev 20:6: they will be priests of God and of Christ and will reign with him). Edom — the hostile brother, the nation of Esau who despised his birthright — represents all who reject the covenant birthright; their ultimate defeat is not a tribal victory for Israel but the vindication of YHWH's justice over all who oppose his reign.</p>"
  }
}

# ============================
# JONAH
# ============================

JONAH_ECHO = {
  "1": {
    "17": [
      {"type": "fulfillment", "target": "Matt 12:40", "note": "And Jonah was in the belly of the fish three days and three nights — Jesus cites this as the sign of Jonah: the Son of Man will be three days and three nights in the heart of the earth; Jonah's entombment in the fish and his emergence is the type of Jesus's death and resurrection"}
    ]
  },
  "3": {
    "5": [
      {"type": "fulfillment", "target": "Matt 12:41", "note": "The men of Nineveh repented at the preaching of Jonah, and behold something greater than Jonah is here — Jesus contrasts Nineveh's repentance at Jonah's preaching with the Jewish generation's refusal to repent at Jesus's preaching; Nineveh is a Gentile city that responded; this generation has responded to a greater preacher with less"}
    ]
  }
}

JONAH_ORIGINAL = {
  "1": {
    "17": "<p><strong>vayeman YHWH dag gadol livlo et Yonah vayehi Yonah bime'ei haddag shlosha yamim ushlosha leilot</strong>: 'And the LORD appointed a great fish to swallow up Jonah. And Jonah was in the belly of the fish three days and three nights.' The historicity of Jonah has been debated throughout church history — a man surviving inside a large sea creature is extraordinary. Jesus's citation of Jonah in Matt 12:40 takes the narrative as historical: 'just as Jonah was three days and three nights in the belly of the great fish, so will the Son of Man be three days and three nights in the heart of the earth.' If Jonah is a parable, Jesus is drawing a parable-to-reality comparison, which is unusual. The orthodox reading: both Jonah's experience and Jesus's resurrection are historical events in which the later was the greater antitype of the earlier.</p>"
  }
}

JONAH_CONTEXT = {
  "1": {
    "1": "<p>Jonah is unique among the writing prophets: instead of a prophetic oracle, it is a narrative about a prophet. Jonah ben Amittai is mentioned in 2 Kings 14:25 as a historical figure who prophesied during the reign of Jeroboam II (ca. 793-753 BCE). The book narrates his mission to Nineveh, the capital of the Assyrian Empire — Israel's most formidable enemy. His initial flight from the mission (not from fear but, the book reveals in ch. 4, from a reluctance to see Gentile enemies repent and be spared) is the book's theological problem: the prophet opposes the very grace that characterizes YHWH. The book's final question (4:11: should I not be concerned about Nineveh?) is deliberately unanswered — forcing the reader to answer it. Jesus's use of the 'sign of Jonah' (Matt 12:39-41) makes Jonah's historical experience the type of his own death and resurrection.</p>"
  }
}

JONAH_CHRIST = {
  "1": {
    "17": "<p>A type: 'Jonah was in the belly of the fish three days and three nights.' Jesus himself identifies this as the OT's appointed sign for his resurrection: 'For just as Jonah was three days and three nights in the belly of the great fish, so will the Son of Man be three days and three nights in the heart of the earth' (Matt 12:40). The typological elements: Jonah goes into the deep as a substitute (the sailors are saved from the storm by throwing Jonah overboard; 1:12-15) → Jonah is entombed in the fish → Jonah emerges to complete his mission to the Gentiles. The antitype: Christ goes to the cross as the world's substitute → Christ is entombed → Christ rises and commissions the mission to all Gentiles (Matt 28:19). Jonah's Gentile mission to Nineveh is the shadow; the apostolic mission to all nations is the substance.</p>"
  }
}

# ============================
# MICAH
# ============================

MICAH_ECHO = {
  "5": {
    "2": [
      {"type": "fulfillment", "target": "Matt 2:6", "note": "But you O Bethlehem Ephrathah who are too little to be among the clans of Judah from you shall come forth for me one who is to be ruler in Israel — the Magi and Herod's scribes cite Micah 5:2 as the birthplace of the Messiah; Matthew cites it as fulfilled in Jesus's birth at Bethlehem; the ruler whose origin is from of old, from ancient days, is the pre-existent Christ born in the city of David"}
    ]
  },
  "6": {
    "8": [
      {"type": "allusion", "target": "Matt 23:23", "note": "He has told you, O man, what is good; and what does the LORD require of you but to do justice and to love kindness and to walk humbly with your God — the ethical summary of Micah; Jesus's woe against the Pharisees who tithe mint but neglect the weightier matters of the law: justice and mercy and faithfulness (Matt 23:23); Micah 6:8 is Jesus's standard for what constitutes the law's weightier matters"}
    ]
  }
}

MICAH_ORIGINAL = {
  "5": {
    "2": "<p><strong>veatta Beit-Lechem Efrata tzair lihyot be'alfei Yehudah mimcha li yetze lihyot moshel beYisrael umotza'otav mikedem miyemei olam</strong>: 'But you, O Bethlehem Ephrathah, who are too little to be among the clans of Judah, from you shall come forth for me one who is to be ruler in Israel, whose coming forth is from of old, from ancient days.' <em>Motza'otav mikedem miyemei olam</em> (whose coming forth is from of old, from ancient days/from ancient times/from everlasting): the preposition and nouns can point to either the antiquity of the Davidic dynasty (David's line goes back to ancient Bethlehem) or to the eternal pre-existence of the coming ruler. The NT reading (John 8:58; John 1:1) takes it in the latter, stronger sense: the one born in Bethlehem has his 'goings forth' from eternity.</p>"
  }
}

MICAH_CONTEXT = {
  "1": {
    "1": "<p>Micah prophesied ca. 735-700 BCE, contemporary with Isaiah in the southern kingdom, during the Assyrian crisis that destroyed Samaria (722 BCE) and threatened Jerusalem (701 BCE). He was a rural prophet from Moresheth-Gath (a village in the Judean foothills), which gives his oracles a social-justice perspective: he speaks for the peasant farmers whose land is being seized by the powerful (2:1-2; 3:1-3). His prophecy of Jerusalem's destruction (3:12: Zion shall be plowed as a field; Jerusalem shall become a heap of ruins) was so striking that it was cited a century later as a precedent for not killing Jeremiah when he prophesied similarly (Jer 26:18-19). Micah 6:8 is the OT's most compact ethical summary and one of the most frequently cited prophetic verses.</p>"
  }
}

MICAH_CHRIST = {
  "5": {
    "2": "<p>A direct revelation: 'But you, O Bethlehem Ephrathah, who are too little to be among the clans of Judah, from you shall come forth for me one who is to be ruler in Israel, whose coming forth is from of old, from ancient days.' The theological precision of this prophecy is remarkable: (1) the specific town — Bethlehem, not Jerusalem; (2) the paradox — too small to be a clan-city, yet the birthplace of the supreme ruler; (3) the pre-existence — his 'coming forth' predates his birth in Bethlehem, reaching back to 'ancient days' (or in the stronger reading, eternity). Matthew 2:6 cites it as fulfilled with a slight adaptation that applies Micah's 'ruler' language to the one who will 'shepherd my people Israel' — combining Micah's political and pastoral imagery into the Christ who is both king and shepherd (John 10:11; Rev 7:17).</p>"
  }
}

# ============================
# NAHUM
# ============================

NAHUM_ECHO = {
  "1": {
    "15": [
      {"type": "allusion", "target": "Rom 10:15", "note": "Behold upon the mountains the feet of him who brings good news, who publishes peace — Nahum announces the fall of Nineveh as good news (the oppressor is destroyed); Isaiah 52:7 uses the same image (how beautiful upon the mountains are the feet of him who brings good news); Paul cites Isaiah in Romans 10:15 for the gospel proclamation: the good news of peace is the gospel of Christ, and the messenger's feet are the apostles'"}
    ]
  }
}

NAHUM_ORIGINAL = {
  "1": {
    "3": "<p><strong>YHWH erech apayim ugedol koach venakeh lo yenakeh YHWH besufa uvishara darko veanan afar raglav</strong>: 'The LORD is slow to anger and great in power, and the LORD will by no means clear the guilty. His way is in whirlwind and storm, and the clouds are the dust of his feet.' Nahum opens with an acrostic poem (1:2-8, partial alphabet) on the character of YHWH — combining the divine attributes of mercy and judgment that Exod 34:6-7 announced: merciful and slow to anger (Exod 34:6; Nahum 1:3a) but will not leave the guilty unpunished (Exod 34:7b; Nahum 1:3a). Jonah announced repentance and YHWH relented; Nahum announces the final judgment because Nineveh did not permanently repent. The same divine character — patient mercy but ultimate justice — is the framework for the NT: God overlooked past sins (Acts 17:30; Rom 3:25) but now commands repentance in light of the coming judgment.</p>"
  }
}

NAHUM_CONTEXT = {
  "1": {
    "1": "<p>Nahum prophesied ca. 663-612 BCE — after the fall of Thebes (663 BCE, mentioned in 3:8) and before the fall of Nineveh (612 BCE, which Nahum predicts). He is the companion prophecy to Jonah: Jonah brought Nineveh to repentance (ca. 760 BCE) and YHWH relented; Nahum announces that Nineveh's subsequent return to violence and oppression means its final destruction is now inevitable. The contrast is instructive: divine patience has a limit; the same attributes of mercy and justice that led YHWH to spare Nineveh in Jonah's day lead him to destroy it in Nahum's day. Nineveh was destroyed in 612 BCE by a coalition of Babylonians and Medes, exactly as Nahum predicted.</p>"
  }
}

NAHUM_CHRIST = {
  "1": {
    "7": "<p>A revelation of God: 'The LORD is good, a stronghold in the day of trouble; he knows those who take refuge in him.' Set in the context of Nineveh's coming destruction, this verse identifies the flip-side of divine wrath: the same YHWH who destroys his enemies is the stronghold for those who trust him. The NT's form of this double-truth: 'It is a fearful thing to fall into the hands of the living God' (Heb 10:31) for those who reject Christ; but 'There is therefore now no condemnation for those who are in Christ Jesus' (Rom 8:1) for those who are in him. The refuge (<em>maoz</em>, stronghold/fortress) that Nahum declares is the God who is also Christ: 'the name of the LORD is a strong tower; the righteous man runs into it and is safe' (Prov 18:10).</p>"
  }
}

# ============================
# HABAKKUK
# ============================

HAB_ECHO = {
  "2": {
    "4": [
      {"type": "fulfillment", "target": "Rom 1:17", "note": "The righteous shall live by his faith — Paul quotes Hab 2:4 in Romans 1:17, Galatians 3:11, and Hebrews 10:38 as the OT summary of justification by faith: the just/righteous person lives by faithfulness/faith; Paul applies it to the righteousness of God revealed in the gospel"},
      {"type": "fulfillment", "target": "Gal 3:11", "note": "It is evident that no one is justified before God by the law, for the righteous shall live by faith — Paul cites Hab 2:4 as proof that the OT already knew that justification was by faith, not law-keeping; the law (Lev 18:5: he who does them shall live by them) and the prophet (Hab 2:4: the righteous shall live by faith) are placed in contrast"}
    ]
  }
}

HAB_ORIGINAL = {
  "2": {
    "4": "<p><strong>hineh afela lo yoshra nafsho bo vetzaddik beemunato yichyeh</strong>: 'Behold, his soul is puffed up; it is not upright within him, but the righteous shall live by his faith [or faithfulness, <em>emunah</em>].' This verse is the most quoted OT text in the NT letters. The Hebrew <em>emunah</em> covers a semantic range from 'faithfulness' (reliability, steadfastness) to 'faith' (trust, belief). Paul's use in Romans and Galatians emphasizes the trust/belief aspect; the Habakkuk context emphasizes endurance and faithfulness during the Babylonian crisis. Both senses are present: the righteous person is characterized by trust in YHWH's promise that sustains them through the crisis (both the original Babylonian threat and the ongoing existential challenge of life under divine wrath deferred). The Reformers' rediscovery of this verse (Luther: the just shall live by faith, not by works of the law) was the theological engine of the Protestant Reformation.</p>"
  }
}

HAB_CONTEXT = {
  "1": {
    "1": "<p>Habakkuk's dialogue with YHWH (ca. 605-598 BCE) is the OT's most direct expression of prophetic complaint about divine justice: Why do you tolerate wrong? (1:3); Why are you silent while the wicked swallow up the more righteous? (1:13). YHWH's answer — he is raising up the Babylonians as the instrument of judgment — only deepens the question: how can a holy God use a more wicked nation to judge a less wicked one? The book's resolution is the three-chapter arc of complaint → divine response → prophetic praise (ch. 3): the righteous will live by faith in YHWH's promises even when the present situation appears to contradict those promises. The book models the theodicy of faith: not a logical resolution of the problem of evil, but a trust in the character of YHWH that sustains through crisis.</p>"
  }
}

HAB_CHRIST = {
  "2": {
    "4": "<p>A direct revelation: 'The righteous shall live by his faithfulness/faith.' This verse, quoted three times in the NT, is the OT's most concentrated statement of the principle of justification by faith. Paul reads it as the OT's own principle against works-righteousness: 'it is evident that no one is justified before God by the law, for the righteous shall live by faith' (Gal 3:11). The christological dimension: the 'righteous one' who lives by faith in its ultimate form is Jesus himself, who trusted the Father through the cross and was vindicated in the resurrection (Heb 10:38-39 applies the verse to perseverance under persecution, contextualizing it with the author's own reflection on Christ's faithfulness). The Reformation's recovery of this verse as the summary of the gospel ('the just shall live by faith') was the recovery of the Christological center of the OT's own prophetic witness.</p>"
  }
}

# ============================
# ZEPHANIAH
# ============================

ZEPH_ECHO = {
  "3": {
    "14": [
      {"type": "allusion", "target": "Luke 1:28", "note": "Sing aloud O daughter of Zion; shout O Israel! Rejoice and exult with all your heart O daughter of Jerusalem — the call to rejoice because YHWH is among you (3:17); the angel's greeting to Mary (Rejoice, highly favored one, the Lord is with you) echoes the Zephaniah joy-announcement: the presence of YHWH is the reason for rejoicing, and in the incarnation, YHWH is present in the most intimate way imaginable"},
      {"type": "allusion", "target": "John 1:14", "note": "The LORD your God is in your midst — Zeph 3:17 (the LORD is in your midst) is the OT's joyful proclamation of divine presence; John 1:14 (the Word became flesh and dwelt in our midst) is the ultimate fulfillment: YHWH's presence in the tabernacle-tent and in the midst of his people now means the incarnate Son tabernacling among humanity"}
    ]
  }
}

ZEPH_ORIGINAL = {
  "3": {
    "17": "<p><strong>YHWH eloheicha bekirbecha gibbor yoshi'a yasis alayich besimcha yacharish be'ahavato yagel alayich berinah</strong>: 'The LORD your God is in your midst, a mighty one who will save; he will rejoice over you with gladness; he will quiet you by his love; he will exult over you with loud singing.' This verse is the OT's most intimate statement of divine delight in his people: YHWH not merely tolerating but actively rejoicing over Israel, singing over her. The father-over-child image (quieting, singing) is the most tender description of YHWH's covenant love. The NT fulfillment: 'The Father himself loves you' (John 16:27); 'God is love' (1 John 4:8); 'rejoice in the Lord always' (Phil 4:4) — the joy is mutual, as Zephaniah's vision shows: YHWH singing over his people is the grounding for the people's own joy.</p>"
  }
}

ZEPH_CONTEXT = {
  "1": {
    "1": "<p>Zephaniah prophesied ca. 640-609 BCE during the reign of Josiah (640-609 BCE), before or during Josiah's reform (621 BCE). He was a member of the royal family (his genealogy goes back four generations to Hezekiah, 1:1) — one of the few prophets with clear royal connections. His primary theme is the Day of the LORD (using the phrase more than any other prophet): a comprehensive divine judgment on Judah (ch. 1), the nations (2), and Jerusalem (3:1-8), followed by the promise of a purified remnant and YHWH's presence among them (3:9-20). Zephaniah 3:14-20's closing vision of joy and restoration is one of the OT's most beautiful eschatological passages and the probable background for the angel's greeting to Mary at the Annunciation.</p>"
  }
}

ZEPH_CHRIST = {
  "3": {
    "14": "<p>A fulfillment: 'Sing aloud, O daughter of Zion; shout, O Israel! Rejoice and exult with all your heart, O daughter of Jerusalem! The LORD has taken away the judgments against you ... The King of Israel, the LORD, is in your midst; you shall never again fear evil.' This call to rejoice because YHWH is in the midst of his people reaches its fulfillment in the incarnation. Luke's Annunciation (1:28-33) and the angels' song at the Nativity (2:10-14: I bring you good news of great joy) are the NT's recasting of Zephaniah's joy-cry: rejoice, for the Lord is with you. The movement from Zephaniah to Luke is the movement from prophetic announcement to historical fulfillment: the divine King who was to come 'in your midst' comes as the infant in Bethlehem, and then the risen Lord who sends the Spirit so that YHWH is 'in the midst' of the church (Matt 18:20; John 14:23).</p>"
  }
}

# ============================
# HAGGAI
# ============================

HAG_ECHO = {
  "2": {
    "6": [
      {"type": "fulfillment", "target": "Heb 12:26-27", "note": "Yet once more, in a little while, I will shake the heavens and the earth and the sea and the dry land — Hebrews cites Haggai 2:6 as pointing to the definitive eschatological shaking: the removal of created things that are shakeable, so that only the unshakeable kingdom remains; the new creation will be established through a shaking that removes the old"}
    ],
    "9": [
      {"type": "allusion", "target": "John 2:21", "note": "The latter glory of this house shall be greater than the former — Haggai promises that the second temple will surpass Solomon's in glory; this is fulfilled not in the physical Herodian temple but in Jesus entering the temple (John 2:19-21: destroy this temple, and in three days I will raise it up; the temple was his body); the presence of Christ in the second temple makes its latter glory exceed its former"}
    ]
  }
}

HAG_ORIGINAL = {
  "2": {
    "9": "<p><strong>gadol yihyeh kevod habayit haze ha-acharon min harishon amar YHWH tzvaot uvamaqom haze etten shalom neum YHWH tzvaot</strong>: 'The latter glory of this house shall be greater than the former, says the LORD of hosts. And in this place I will give peace, declares the LORD of hosts.' Haggai's promise was puzzling to the post-exilic community: the second temple was visibly inferior to Solomon's (Ezra 3:12: the elders who had seen the first temple wept when the second was founded). The fulfillment required an unexpected reading: the greater glory came not through architectural improvement (Herod's renovation made it physically grander) but through the presence of the messianic King who entered it (Matt 21:12-17; John 2:13-22). Jesus is the glory that made the second temple greater — the Shekinah presence in person, which the first temple never contained.</p>"
  }
}

HAG_CONTEXT = {
  "1": {
    "1": "<p>Haggai prophesied in 520 BCE, the second year of Darius I of Persia — 16 years after the first returnees arrived in Jerusalem. The temple reconstruction had stalled: the returning exiles had built their own houses while the temple remained unfinished (1:4). Haggai's four oracles (1:1-11; 2:1-9; 2:10-19; 2:20-23) call the community to prioritize the temple and promise divine blessing as a result. His contemporary was Zechariah, whose visions (chs. 1-8) addressed the same restoration community. Together they provide the theological framework for the post-exilic community's task: rebuilding the worship center through which YHWH's presence among his people would be maintained until the coming of the one greater than the temple.</p>"
  }
}

HAG_CHRIST = {
  "2": {
    "7": "<p>A type: 'And I will shake all nations, so that the treasures of all nations shall come in, and I will fill this house with glory, says the LORD of hosts.' The 'treasures/desired things of all nations' (<em>chemdah</em>) coming to the temple has been read messianically (the Vulgate translates it 'veniet Desideratus cunctis gentibus', 'the one desired by all nations will come'). Whether or not this is the primary meaning, the pattern is clear: the nations streaming to the temple with their wealth is the OT vision of the eschatological gathering of all peoples to YHWH's dwelling. In the NT: the Magi (Gentile wise men) coming to the Christ-child with their treasures (Matt 2:11) is one fulfillment; the nations bringing their glory into the new Jerusalem (Rev 21:24-26) is the final fulfillment. The temple's latter glory exceeds the former because it is the glory of the incarnate Son and ultimately the new creation temple where God dwells with his people forever.</p>"
  }
}

# ============================
# ZECHARIAH
# ============================

ZECH_ECHO = {
  "9": {
    "9": [
      {"type": "fulfillment", "target": "Matt 21:5", "note": "Rejoice greatly O daughter of Zion! Shout O daughter of Jerusalem! Behold your king is coming to you; righteous and having salvation is he, humble and mounted on a donkey on a colt the foal of a donkey — Matthew and John both cite Zechariah 9:9 as fulfilled in the triumphal entry; the King of peace entering on a donkey (not a war horse) is the messianic sign"}
    ]
  },
  "11": {
    "12": [
      {"type": "fulfillment", "target": "Matt 26:15", "note": "And they weighed out as my wages thirty pieces of silver — the shepherd's wages in Zechariah 11:12 are applied to Judas's price for betraying Jesus; Matthew explicitly cites this as fulfillment (using Jeremiah's name by prophetic attribution of the scripture) in Matt 27:9-10"}
    ]
  },
  "12": {
    "10": [
      {"type": "fulfillment", "target": "John 19:37", "note": "They shall look on me whom they have pierced — Zechariah's oracle about the pierced one whom Jerusalem will mourn; John cites it at the crucifixion (they will look on the one they have pierced, John 19:37); Revelation applies it to the parousia (Rev 1:7: every eye will see him, even those who pierced him)"}
    ]
  },
  "13": {
    "7": [
      {"type": "fulfillment", "target": "Matt 26:31", "note": "Strike the shepherd, and the sheep will be scattered — Jesus quotes Zechariah 13:7 in Gethsemane as what will be fulfilled when he is arrested: strike the shepherd and the sheep of the flock will be scattered; the disciples' abandonment is the fulfillment of the Zechariah oracle about the smitten shepherd"}
    ]
  }
}

ZECH_ORIGINAL = {
  "12": {
    "10": "<p><strong>veshafachti al beit David veal yoshev Yerushalayim ruach chen vetachanunin vehibitu elai et asher daqaru vesafdu alav kemisped al hayachid vehamer alav kemispod al habechor</strong>: 'And I will pour out on the house of David and the inhabitants of Jerusalem a spirit of grace and pleas for mercy, so that, when they look on me, on him whom they have pierced, they shall mourn for him, as one mourns for an only child, and weep bitterly over him, as one weeps over a firstborn.' The grammatical anomaly is striking: 'they shall look on me [YHWH speaking] whom they have pierced' — the divine speaker identifies himself as the one pierced. The transition from 'me' to 'him' within the verse is unexplained in the OT but is resolved in the NT: YHWH and the one who was pierced are identified — the one pierced at the crucifixion is YHWH in the person of the Son.</p>"
  }
}

ZECH_CONTEXT = {
  "1": {
    "1": "<p>Zechariah prophesied ca. 520-518 BCE (chs. 1-8, with the dated oracles) and possibly into the 5th or 4th century BCE (chs. 9-14, the 'Second Zechariah', are undated and stylistically different — many scholars treat them as later additions). His eight night visions (chs. 1-6) address the post-exilic restoration community with complex symbolic imagery; his oracle-collections (chs. 7-8, 9-11, 12-14) look further into the eschatological future. Zechariah is the most extensively quoted OT book in the Gospel passion narratives — his oracles about the triumphal entry (9:9), the thirty pieces of silver (11:12-13), the smitten shepherd (13:7), the pierced one (12:10), and the cosmic mourning (12:10-14) all find explicit NT citations in the passion story. The passion narrative is Zechariah 9-14 in fulfillment.</p>"
  }
}

ZECH_CHRIST = {
  "9": {
    "9": "<p>A direct revelation: 'Rejoice greatly, O daughter of Zion! Shout aloud, O daughter of Jerusalem! Behold, your king is coming to you; righteous and having salvation is he, humble and mounted on a donkey, on a colt, the foal of a donkey.' The triumphal entry is one of the most deliberately staged Christological events in the Gospels: Jesus specifically arranges for the donkey (Luke 19:30-34), enters Jerusalem in a way that fulfills Zechariah's vision exactly, and Matthew and John both cite the fulfillment (Matt 21:5; John 12:15). The theological content of the sign: a king on a war horse signals military conquest; a king on a donkey signals peace and humility. The Messiah comes not to destroy enemies with military power but to bring salvation through the humble, peaceable means of his own sacrifice. The crowds' hosannas (Ps 118:26, 'Blessed is he who comes in the name of the LORD') are their recognition of the sign, even if they misread its implications.</p>"
  },
  "12": {
    "10": "<p>A direct revelation: 'They shall look on me, on him whom they have pierced, and they shall mourn for him, as one mourns for an only child, and weep bitterly over him, as one weeps over a firstborn.' The shift from 'me' (YHWH speaking) to 'him' (the one pierced) within the verse is the OT's most striking grammatical prolepsis of the incarnation: the one pierced is YHWH, yet YHWH speaks of him in the third person. John cites it at the crucifixion (19:37: these things took place that the Scripture might be fulfilled: they will look on him whom they have pierced), and Revelation applies it to the parousia (1:7: every eye will see him, even those who pierced him, and all tribes of the earth will wail on account of him). The mourning is both repentance (Acts 2:37: they were cut to the heart and said, Brothers, what shall we do?) and eschatological recognition (Rev 1:7: all tribes will wail).</p>"
  }
}

# ============================
# MALACHI
# ============================

MAL_ECHO = {
  "3": {
    "1": [
      {"type": "fulfillment", "target": "Matt 11:10", "note": "Behold I send my messenger and he will prepare the way before me — the messenger of the covenant is announced; Jesus quotes Malachi 3:1 (in combination with Exod 23:20) as fulfilled in John the Baptist: this is the one about whom it is written, Behold I send my messenger before your face who will prepare your way before you"},
      {"type": "fulfillment", "target": "Mark 1:2", "note": "Behold I send my messenger before your face — Mark opens his Gospel by combining Malachi 3:1 and Isaiah 40:3 as fulfilled in John the Baptist's ministry in the wilderness"}
    ]
  },
  "4": {
    "5": [
      {"type": "fulfillment", "target": "Matt 11:14", "note": "Behold I will send you Elijah the prophet before the great and awesome day of the LORD comes — Jesus identifies John the Baptist as the Elijah who was to come (Matt 11:14; 17:12): if you are willing to accept it, he is Elijah who is to come; the angel's announcement (Luke 1:17: he will go before him in the spirit and power of Elijah) grounds John's identity in Malachi's prophecy"}
    ],
    "6": [
      {"type": "allusion", "target": "Luke 1:17", "note": "He will turn the hearts of fathers to their children and the hearts of children to their fathers — the Elijah-prophecy of Malachi 4:6 is applied to John the Baptist's ministry; Luke 1:17 applies it directly: he will turn the hearts of the fathers to the children, and the disobedient to the wisdom of the just"}
    ]
  }
}

MAL_ORIGINAL = {
  "3": {
    "1": "<p><strong>hineni sholech malachi ufinah derekh lefanai ufitom yavo el heikhalov haAdon asher atem mevaksim umalach haberit asher atem chafetzim hineh ba amar YHWH tzvaot</strong>: 'Behold, I send my messenger [<em>malachi</em>], and he will prepare the way before me. And the Lord whom you seek will suddenly come to his temple; and the messenger of the covenant in whom you delight, behold, he is coming, says the LORD of hosts.' The word <em>malachi</em> means 'my messenger' — the book's title is this very word. YHWH promises two figures: the forerunner messenger (= John the Baptist) and the Lord who suddenly comes to his temple (= Jesus). The Lord's coming to his temple is the incarnation and the temple-cleansings (John 2:13-22; Mark 11:15-17). The 'messenger of the covenant' combines the forerunner and the Lord in a way that the NT separates: John is the messenger of Mal 3:1a; Jesus is the Lord of Mal 3:1b.</p>"
  },
  "4": {
    "5": "<p>The closing oracle of Malachi (4:5-6) is also the closing oracle of the OT: 'Behold, I will send you Elijah the prophet before the great and awesome day of the LORD comes. And he will turn the hearts of fathers to their children and hearts of children to their fathers, lest I come and strike the land with a decree of utter destruction.' The Hebrew canon ends here — with a promise of Elijah's return and a warning of cursing if he is rejected. The NT opens with John the Baptist filling this role (Luke 1:17; Matt 11:14; 17:10-13). The OT ends in expectation; the NT opens in fulfillment. The 400-year inter-testamental silence is the space between Malachi's promise and Matthew's fulfillment — the waiting for the forerunner who will announce the Lord's coming.</p>"
  }
}

MAL_CONTEXT = {
  "1": {
    "1": "<p>Malachi is the last book of the OT in both the Hebrew canon's traditional order and the Christian canon. It was written ca. 450-430 BCE, after the return from exile, during a period of post-exilic religious laxness. The prophet addresses: priests who offer defiled offerings (1:6-2:9), men who divorce their wives (2:14-16), the community's failure to tithe (3:10), and the skepticism of those who question YHWH's justice (3:13-15). Its six disputation speeches (each opening with a divine claim, then an objection, then YHWH's response) address the demoralization of the restored community. Malachi is the bridge between the OT and the NT: its final oracles (3:1; 4:5-6) are the OT's last prophetic words, pointing directly to John the Baptist and Jesus, so that the NT's opening (Matt 1-3; Mark 1; Luke 1-3) is the direct fulfillment of Malachi's closing.</p>"
  }
}

MAL_CHRIST = {
  "3": {
    "1": "<p>A direct revelation: 'Behold, I send my messenger, and he will prepare the way before me. And the Lord whom you seek will suddenly come to his temple.' This oracle ends the OT's prophetic program: the next thing to happen is the forerunner's preparation and the Lord's arrival. Four hundred years of prophetic silence follow — and then John the Baptist appears in the wilderness (Matt 3:1-3; Mark 1:2-4), fulfilling Malachi 3:1 (combined with Isaiah 40:3). Jesus's entry into the temple (John 2:13-22; Mark 11:15-17) is the Lord's sudden coming to his temple. The NT's opening chapters are Malachi's oracle in motion. The closing words of the OT (Mal 4:5-6) and the opening words of the NT (Matt 1:1) are not separated by 400 years of divine absence but by the divine patience that was preparing the fullness of time (Gal 4:4: when the fullness of time had come, God sent forth his Son).</p>"
  },
  "4": {
    "5": "<p>A fulfillment: 'Behold, I will send you Elijah the prophet before the great and awesome day of the LORD comes.' The OT ends with a promise; the NT opens with its fulfillment. John the Baptist comes 'in the spirit and power of Elijah' (Luke 1:17) — not literally Elijah reincarnated (John explicitly denies being Elijah, John 1:21) but fulfilling Elijah's eschatological role as the forerunner who prepares the way. Jesus confirms: 'if you are willing to accept it, he is Elijah who is to come' (Matt 11:14). The Transfiguration scene (Matt 17:3) brings the literal Elijah alongside the literal Moses alongside the literal Christ — the forerunner and the law flanking the fulfillment. Malachi's final word (the turning of fathers' and children's hearts, lest the land be struck with a curse) is the new covenant's mission: the gospel brings family reconciliation within the covenant community and protects from the ultimate curse, which Christ has absorbed (Gal 3:13).</p>"
  }
}

def main():
    books_data = [
        ('lamentations', LAM_ECHO, LAM_ORIGINAL, LAM_CONTEXT, LAM_CHRIST),
        ('hosea', HOSEA_ECHO, HOSEA_ORIGINAL, HOSEA_CONTEXT, HOSEA_CHRIST),
        ('joel', JOEL_ECHO, JOEL_ORIGINAL, JOEL_CONTEXT, JOEL_CHRIST),
        ('amos', AMOS_ECHO, AMOS_ORIGINAL, AMOS_CONTEXT, AMOS_CHRIST),
        ('obadiah', OBAD_ECHO, OBAD_ORIGINAL, OBAD_CONTEXT, OBAD_CHRIST),
        ('jonah', JONAH_ECHO, JONAH_ORIGINAL, JONAH_CONTEXT, JONAH_CHRIST),
        ('micah', MICAH_ECHO, MICAH_ORIGINAL, MICAH_CONTEXT, MICAH_CHRIST),
        ('nahum', NAHUM_ECHO, NAHUM_ORIGINAL, NAHUM_CONTEXT, NAHUM_CHRIST),
        ('habakkuk', HAB_ECHO, HAB_ORIGINAL, HAB_CONTEXT, HAB_CHRIST),
        ('zephaniah', ZEPH_ECHO, ZEPH_ORIGINAL, ZEPH_CONTEXT, ZEPH_CHRIST),
        ('haggai', HAG_ECHO, HAG_ORIGINAL, HAG_CONTEXT, HAG_CHRIST),
        ('zechariah', ZECH_ECHO, ZECH_ORIGINAL, ZECH_CONTEXT, ZECH_CHRIST),
        ('malachi', MAL_ECHO, MAL_ORIGINAL, MAL_CONTEXT, MAL_CHRIST),
    ]
    for book, echo_d, orig_d, ctx_d, chr_d in books_data:
        e = load_echo(book); merge_echo(e, echo_d); save_echo(book, e)
        c = load_comm('mkt-original', book); merge_comm(c, orig_d); save_comm('mkt-original', book, c)
        c = load_comm('mkt-context', book); merge_comm(c, ctx_d); save_comm('mkt-context', book, c)
        c = load_comm('mkt-christ', book); merge_comm(c, chr_d); save_comm('mkt-christ', book, c)
        print(f'{book}: all 4 layers written')

if __name__ == '__main__':
    main()
