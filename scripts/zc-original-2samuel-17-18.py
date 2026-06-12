"""
mkt-original | 2 Samuel 17-18
Run: python3 scripts/zc-original-2samuel-17-18.py

Key lexical/syntactic items:
- 17:14: hēpēr YHWH 'et-'ēṣat 'Ăḥîṯōp̄el — YHWH "frustrated" the good counsel; theological hinge
- 17:23: wayyēḥānaq — Ahithophel "hanged himself"; same semantic field as Judas (Matt 27:5)
- 18:5: liʾaṭ — "gently/quietly"; David's tender command re: Absalom
- 18:9: tālûy — Absalom "hanging" from oak; Deut 21:22-23 curse-language
- 18:18: yad (lit. "hand") Absalom = the memorial pillar vs. the stone heap of v17
- 18:33: ûmî yittēn mūṯî ʾanî taḥteykā — "would that I had died in your place";
         substitutionary longing, the father's love as prefigurement of the Father's giving the Son
"""

import json
import pathlib

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


SAMUEL = {
    "17": {
        "1": "<p>Ahithophel's counsel opens with crisp military logic: twelve thousand men (ʾĕlep, a military unit), immediate night pursuit (halaylâ), swift strike against the weary king. The precision marks him as a brilliant strategist. The noun <em>ʿēṣâ</em> (counsel, advice) is key throughout chs 16-17 — it becomes the contested commodity of the narrative. Proverbs 20:18 notes that war is won by guidance (<em>ʿēṣôṯ</em>); the battle of ch 17 is a battle of counsels before it is a battle of swords.</p>",

        "2": "<p><em>waʾāḇôʾ ʿālāyw</em> — 'I will come upon him' — Ahithophel positions himself as the attacker of a prey: David 'weary and weak-handed' (yĕgîaʿ ûrĕpeh yādayim). The phrase <em>rĕpeh yādayim</em> (slack of hands) echoes Isa 35:3 ('strengthen the weak hands') and Heb 12:12 ('lift your drooping hands'). David's exhaustion at the Jordan is the inverse of his vigor at earlier battles. The vulnerability of the anointed king at his lowest point is the moment of maximum danger.</p>",

        "3": "<p>Ahithophel's goal is stated cleanly: bring back all the people as a bride returns to her husband (<em>kĕ-šûḇ hakallâ ʾel-ʾîšāh</em>, lit. 'like the return of the bride to her husband'). One man's death resolves everything. The cold elegance of 'you seek only one man' reveals Ahithophel's calculating mind — he reduces the civil war to an assassination problem. The contrast with YHWH's logic in the NT is sharp: God also seeks the one lost sheep (Luke 15:4), but not to destroy it — to restore it.</p>",

        "4": "<p>The counsel was <em>yāšar</em> (right, straight, good) in Absalom's eyes and in all the elders' eyes. The word <em>yāšar</em> typically connotes moral uprightness in Proverbs; here it simply means strategically sound. Human wisdom that is technically <em>yāšar</em> can still be overturned by divine purpose — the same principle Paul invokes when he says 'the wisdom of this world is folly before God' (1 Cor 3:19).</p>",

        "5": "<p>Absalom's decision to consult Hushai as well introduces the providential counter-move. His calling Hushai shows insecurity — a truly confident leader accepts his best counselor's advice. The double-consultation dynamic mirrors Balak calling Balaam repeatedly: even when the divine plan is fixed, the human actors keep testing alternative options.</p>",

        "6": "<p>Absalom presents Ahithophel's plan to Hushai for evaluation — an unusual procedural move that will prove fatal. The very act of committee-checking exceptional military advice gives Hushai the opening he needs. Proverbs warns that 'in an abundance of counselors there is victory' (Prov 11:14), but the proverb assumes the counselors are seeking the same goal. When one counselor is a double agent, the abundance of counsel becomes the instrument of defeat.</p>",

        "7": "<p>'The advice Ahithophel has given is not good this time (<em>bappe'am hazzōʾṯ</em>).' Hushai's opening gambit is precisely calibrated: he does not attack Ahithophel's character or past record, but limits his objection to this specific situation. The phrase <em>bappe'am hazzōʾṯ</em> (at this time) is a masterpiece of targeted critique — it acknowledges Ahithophel's general brilliance while creating doubt about this particular plan.</p>",

        "8": "<p>Hushai's counter-argument begins with David's reputation: he and his men are <em>gibbōrê ḥayil</em> (mighty warriors) and they are <em>mārê nepeš</em> (bitter of soul, furious). The <em>dōḇ šakkûl bassādeh</em> (bear robbed of cubs in the field) is a powerful ANE battle simile — a bereaved bear was proverbially the most dangerous of animals (Prov 17:12; Hos 13:8). Hushai is appealing to Absalom's fear of David's reputation.</p>",

        "9": "<p>'He is hiding in some cave (<em>ʾaḥad happa-haṯîm</em>)' — Hushai is deliberately vague and cautious. The word <em>paḥaṯ</em> (pit, cave) will appear again in 18:17 for Absalom's own burial-pit — a grim verbal echo. Hushai's rhetorical strategy is to amplify uncertainty and potential disaster, countering Ahithophel's confidence with worst-case scenarios.</p>",

        "10": "<p>'Even the brave man with the heart of a lion (<em>lēḇ hā-ʾaryēh</em>) will lose his nerve.' The double reversal — brave lion-heart becomes water — is hyperbole, but effective. <em>māsōs yimmās</em> (will melt away) uses the niphal of māsas (melt, dissolve), the same verb used for the Canaanites' terror in Josh 2:11 ('our hearts melted') and for fear at divine presence in Ps 68:2. Hushai is feeding Absalom's fear while appearing to bolster his strategy.</p>",

        "11": "<p>Hushai's alternate plan: assemble all Israel 'from Dan to Beersheba, as the sand of the sea.' The pan-Israel mobilization formula (<em>mîdān ʿad-bĕʾēr šāḇaʿ</em>) is the rhetoric of overwhelming force. He recommends Absalom himself lead the charge — <em>ûp̄ānêkā hōlĕḵîm baqeraḇ</em> (your face going in the battle). This flatters the prince while actually delaying the pursuit long enough for David to escape.</p>",

        "12": "<p>'We will come upon him like dew (kĕ-ašer yippe'l haṭṭal) settling on the ground.' The dew simile inverts Ahithophel's precision-strike imagery: instead of twelve thousand men moving silently and fast, Hushai envisions an overwhelming blanket of force leaving nothing alive. The imagery is vivid but the plan is strategically inferior precisely because it requires time to assemble.</p>",

        "13": "<p>The hyperbole reaches its peak: if David enters a city, all Israel will drag it into the valley with ropes. The exaggeration reveals Hushai's rhetorical goal — he is not making a serious tactical proposal but dazzling Absalom with the spectacle of total victory. Absalom, who erected a monument to himself (18:18), responds to grandiosity.</p>",

        "14": "<p><strong>waYHWH ṣiwwâ lĕhāpēr ʾeṯ-ʿăṣaṯ ʾĂḥîṯōp̄el</strong> — 'And YHWH had commanded/decreed to frustrate the good counsel of Ahithophel.' The narrative's theological interpretation: the choice of Hushai's worse plan over Ahithophel's better plan was YHWH's doing. The verb <em>hēpēr</em> (Hiphil of pārar, H6565) means to break, annul, frustrate — used elsewhere for breaking covenants (Lev 26:44) and invalidating vows (Num 30:8). YHWH breaks Ahithophel's counsel the way he breaks an enemy's plans (Ps 33:10: 'YHWH frustrates the plans of the nations'). This verse is the theological center of the Absalom narrative: Providence works through the persuasiveness of flawed advice.</p>",

        "15": "<p>Hushai immediately reports both plans to the priests Zadok and Abiathar — operating as David's spy exactly as planned (15:34-36). His message is detailed and urgent: 'Thus and so Ahithophel counseled … thus and so I counseled.' The intelligence network David established before fleeing Jerusalem (the priests, the Levites, Jonathan and Ahimaaz) is now activated. Foresight at the moment of crisis is the theme: David's preparation for exile made this rescue possible.</p>",

        "16": "<p>'Do not spend the night at the wilderness crossings' (<em>ʾal-tālîn bĕ-ʿarĕḇôṯ hammiḏbār</em>) — the urgency is specific to the crossing fords. <em>ʿarĕḇôṯ</em> are the plain/steppes flanking the Jordan — predictable crossing locations. Hushai's intelligence about Ahithophel's plan makes the specific warning actionable. Military intelligence translates into specific geographical instruction: cross the Jordan now.</p>",

        "17": "<p>Jonathan and Ahimaaz were stationed at En-rogel — a spring just southeast of Jerusalem, a natural rendezvous point outside the city. A servant girl (<em>šipḥâ</em>) served as their courier, moving freely because of her low social status and gender — invisible to Absalom's surveillance. The use of a female servant as intelligence courier anticipates Rahab's use as a spy-protector in Josh 2 and reverses the gender conventions: the 'weak' become the instruments of salvation.</p>",

        "18": "<p>They were discovered and fled to Bahurim, where a man hid them in a well (<em>bôr</em>). The well/pit image recurs: Joseph in the pit, Absalom's burial pit (18:17), Jeremiah in the cistern (Jer 38:6). The well is the threshold between life and death; being lowered in or hidden within it marks a critical survival moment. The domestic space — a well in someone's courtyard — becomes the hinge of the narrative.</p>",

        "19": "<p>The woman spread a covering (<em>hammaḥăpěšeṯ</em>) over the well's mouth and scattered ground grain (<em>hāriṯōṯ</em>) on it to disguise it. Her quick thinking and deception parallel Rahab's concealment of the spies (Josh 2:4-6). The woman of Bahurim, unnamed like Rahab initially, takes decisive action to protect YHWH's anointed king's messengers.</p>",

        "20": "<p>When Absalom's servants ask 'Where are Ahimaaz and Jonathan?' she says 'They crossed over the brook.' <em>ʿāḇĕrû miḵĕlat hamayim</em> — 'they crossed the brook of water.' A half-truth: she doesn't say they're not in the well. The morality of protective deception here echoes the treatment of Rahab's lie — the narrative does not editorially condemn her action, and her protection of David's messengers places her among those who serve divine purposes at personal risk.</p>",

        "21": "<p>After the soldiers leave, the men emerge and go to David with the intelligence: 'Arise, cross the Jordan quickly.' The imperative sequence — qûm, ʿăḇōr — matches the urgency. The information relay from Hushai → priests → Jonathan/Ahimaaz → the woman of Bahurim → David covers six degrees of separation, each link dependent on faithfulness under pressure. The intelligence chain is the instrument of salvation.</p>",

        "22": "<p>David and all his household crossed before dawn with no one remaining on the near side. The narrator emphasizes total evacuation: <em>lōʾ-neʿdar ʾăšer lōʾ-ʿāḇar</em> — 'not one was missing who had not crossed.' The phrase echoes the Passover evacuation: Exod 12:37 'the Israelites journeyed from Rameses to Succoth.' David's flight across the Jordan is a mini-Exodus, the king taking his people through the river to safety in the wilderness.</p>",

        "23": "<p><strong>wayyaḥăbōš ʾeṯ-ḥămōrô wayyāqom wayyēlek ʾel-bêṯô</strong> — 'he saddled his donkey and arose and went to his own city.' Then: <em>wayĕṣaw ʾeṯ-bêṯô</em> (he set his house in order), and <em>wayyēḥānaq wayyāmōṯ</em> (he strangled himself and died). The suicide of Ahithophel is clinically reported in four verbs. The verb <em>ḥānaq</em> (H2614, to strangle/hang) is rare in Hebrew — the only other clear use is in Nah 2:12 for a lion. Ahithophel's organized exit — setting his house in order before death — is the act of a man who recognizes the political consequences of his failed bet. The NT parallel is explicit: Judas Iscariot, the betrayer of a later anointed king who ate at his table (Ps 41:9), also 'went and hanged himself' (apēnxato, Matt 27:5 — same action, different word). Both betray a Davidic figure; both die by suicide; both are figures of the consequential cost of betrayal.</p>",

        "24": "<p>David arrives at Mahanaim — the city where Saul's son Ish-bosheth had his rival capital (2:8). The geography is charged: David is in the very territory associated with the previous contested succession. Absalom crosses the Jordan with 'all the men of Israel' — the rebel army's crossing mirrors David's escape crossing.</p>",

        "25": "<p>Absalom appoints Amasa as commander in place of Joab. Amasa is identified as 'son of a man named Ithra the Israelite' (<em>hayyiśrĕʾēlî</em>) — the LXX reads 'Jezreelite,' and the parallel in 1 Chr 2:17 says 'Jether the Ishmaelite.' The textual uncertainty around Amasa's lineage may reflect the scribal hesitation about a non-pure-Israelite commanding Israel's army. He was 'son of Abigail daughter of Nahash, sister of Zeruiah' — making Amasa David's nephew and Joab's cousin. A family civil war within a civil war.</p>",

        "26": "<p>Simple geography: Israel and Absalom camped in Gilead. The battle lines are forming across the Jordan east bank. Gilead was territory associated with military standoffs (Gideon crossed here against Midian; Jephthah rose from Gilead). The region has a history as a launching pad for decisive battles against established power.</p>",

        "27": "<p>At Mahanaim, three men bring supplies to David: Shobi son of Nahash from Rabbah of the Ammonites (perhaps a pro-Israelite Ammonite prince), Machir son of Ammiel from Lo-debar (who had sheltered Mephibosheth, 9:4-5), and Barzillai the Gileadite from Rogelim. The diversity of supporters — Ammonite, Manassite, Gileadite — echoes the diverse circle around David in the wilderness years. The exiled king attracts loyal outsiders.</p>",

        "28": "<p>The supply list is materially specific: <em>miškāḇ</em> (beds/couches), <em>sappōṯ</em> (basins), <em>kĕlê yōṣēr</em> (clay vessels), wheat, barley, flour, roasted grain, beans, lentils, honey, curd (<em>ḥemʾâ</em>), sheep, and cheese (<em>šĕp̄ôṯ bāqār</em>). The detailed inventory communicates genuine provision — not symbolic gifts but substantive hospitality. The materials for survival in the desert: bedding, cooking equipment, protein, carbohydrates, preserved foods.</p>",

        "29": "<p>'The people are hungry and weary and thirsty in the wilderness.' The assessment shows the donors understood the urgency. <em>hāʿām rāʿēḇ wĕʿāyēp̄ wĕṣāmēʾ bammiḏbār</em> — three participles building the picture. Three men from outside Israel's political mainstream sustained the king in exile. The NT pattern of 'those who ministered to him out of their own means' (Luke 8:3) has this OT precedent: the exiled king is fed by unlikely supporters while his official kingdom turns against him.</p>",
    },

    "18": {
        "1": "<p>David reorganizes his forces at Mahanaim: he musters (<em>wayyipqōḏ</em>, from pāqaḏ, to appoint/muster/number) and sets over them commanders of thousands and commanders of hundreds — the standard military hierarchy. The muster is a quiet act of reasserting authority: the scattered exile king is reorganizing his forces for battle.</p>",

        "2": "<p>The army is divided into three divisions under Joab, Abishai, and Ittai the Gittite. Ittai — the Philistine from Gath who pledged loyalty in 15:21 — commands a third of David's forces. A foreigner who pledged covenantal loyalty now leads in battle alongside the king's own nephews. The inner circle of the Davidic military demonstrates the pattern of Gentile inclusion that will expand in the Messianic kingdom.</p>",

        "3": "<p>The troops refuse to let David go into battle: 'You must not go out' (<em>lōʾ ṯēṣēʾ</em>). Their argument: if David dies, everything is lost; they are worth nothing compared to him. 'You are worth ten thousand of us' (<em>ki ʿattâ ʿāmĕkā ʿāśārâ rĕḇāḇôṯ</em>). The king's survival is the army's survival. The theological parallel is inverted in Christ: the Shepherd's death is what saves the flock (John 10:11); here the shepherd's survival is what the flock requires. David's preservation is strategic; Christ's sacrifice is salvific.</p>",

        "4": "<p>David defers to the troops' judgment — a rare moment of the king following rather than leading. He 'stood at the side of the gate' (<em>wayyaʿămōḏ hammelek bĕyaḏ-haššaʿar</em>) while all the troops passed out before him. The king at the gate watching his army deploy is a tableau of both authority and impotence: he commands but cannot accompany.</p>",

        "5": "<p><strong>liʾaṭ-lî lannāʿar lĕʾaḇšālôm</strong> — 'deal gently for me with the young man Absalom.' <em>Laʾaṭ</em> (H3909) means quietly, softly, gently — used of a gentle wind (1 Kgs 19:12 'a still small voice,' <em>qôl dĕmāmâ daqqâ</em>, but the same gentleness is implied). David the king and father asks for mercy on the son who tried to kill him. The instruction is heard by all the troops — v5 says 'all the troops heard.' Yet Joab will execute Absalom anyway.</p>",

        "6": "<p>The battle in the forest of Ephraim. Location uncertain — probably east of the Jordan in Gilead, not in the tribal territory of Ephraim to the west. The forest as battlefield setting is unusual in Israelite warfare; the terrain will prove to be Absalom's fatal enemy (v8).</p>",

        "7": "<p>Israel is defeated before David's servants — a massive slaughter of twenty thousand men (<em>ʿeśrîm ʾelep̄</em>). The battle reversal is decisive. The rebel army, which had the advantage of numbers (17:11), is routed. Divine sovereignty is at work: YHWH frustrated Ahithophel's counsel (17:14) and now grants the victory. The large number (20,000) emphasizes the completeness of the defeat.</p>",

        "8": "<p>'The forest (<em>hayyaʿar</em>) devoured more people that day than the sword.' The terrain became the weapon — pitfalls, entanglements, disorientation. <em>wayyereb hayyaʿar lĕʾăkōl bāʿām</em> — 'and the forest multiplied/increased to devour among the people.' The forest is personified as a predator. The creation itself fights on behalf of David's cause — echoing the hailstones in Joshua 10:11 and the stars fighting for Israel in Judges 5:20.</p>",

        "9": "<p>Absalom's fatal moment: his mule passes under branches of a great oak (<em>ʾēlâ gĕḏōlâ</em>), and his head (or hair — the Hebrew says <em>rōʾšô</em>, head, but the Josephus tradition says his hair) is caught in the tree. <em>wayyiṯlāʾ rōʾšô bā-ʾēlâ wayyûṯar bên haššāmayim ûḇên hāʾāreṣ</em> — 'his head was caught in the oak and he was suspended between heaven and earth.' The image is cosmologically charged: the rebel son hangs between heaven (which has rejected him) and earth (which will receive him). The verb <em>tālâ</em> (H8518, to hang) connects directly to Deut 21:22-23: the man executed and hung on a tree is 'under God's curse.' Absalom, who tried to seize the kingdom by killing his father, ends hanging on a tree — cursed.</p>",

        "10": "<p>A soldier reports to Joab: 'I just saw Absalom hanging in an oak.' The bystander who witnesses the suspended rebel understands the military significance but hesitates — he knows the king's command of v5. His report to Joab rather than his own initiative reveals the conflict between military logic and the king's explicit instruction.</p>",

        "11": "<p>Joab's response reveals his priorities: 'Why didn't you strike him? I would have given you ten pieces of silver and a belt (<em>ḥăgôrâ</em>).' The financial offer — ten silver pieces plus military honor — stands against David's explicit command of v5. Joab is operating on military pragmatism: the rebellion ends when Absalom dies. His calculus is correct politically but wrong relationally and ethically in terms of the king's instruction.</p>",

        "12": "<p>The man's response is principled: 'Even if a thousand pieces of silver were weighed out, I would not raise my hand against the king's son.' He invokes the king's explicit command heard by all the troops (v5). The soldier is the novel figure here: the common fighter who obeys the spirit of the king's instruction when the commander is prepared to violate it. His ten-thousand-fold increase of the offered price makes the point by hyperbole.</p>",

        "13": "<p>'And if I had acted treacherously against his life — and nothing is hidden from the king — you yourself would have stood at a distance.' The soldier perceives correctly: Joab would not have protected him from the king's anger. His risk-assessment is precise. The phrase <em>wĕʾattâ hiṯnaṣṣāltā minneged</em> — 'and you would have distanced yourself' — accurately predicts Joab's political survival instinct.</p>",

        "14": "<p><strong>wayyiṯqaʿ šĕlōšâ šĕḇāṭîm bĕleḇ ʾaḇšālôm ʿôḏennû ḥay</strong> — 'He drove three javelins into the heart of Absalom while he was still alive.' <em>wayyiṯqaʿ</em> is the verb used for driving tent pegs (Judges 4:21, Jael killing Sisera) — it denotes violent thrusting. Joab disobeys the king's direct command. The three javelins recall the three javelins Saul threw at David (1 Sam 18:11; 20:33): the pattern of royal violence against a beloved one is now enacted by the king's own commander against the king's son. Joab's action ends the rebellion but inaugurates David's grief.</p>",

        "15": "<p>Ten armor-bearers then finish the execution. The group killing after Joab's wounding ensures Absalom is dead and distributes the political accountability. No single man can be blamed for the act Joab ordered.</p>",

        "16": "<p>The trumpet signals the halt — <em>wayyiṯqaʿ yôʾāḇ baššôp̄ār</em> — Joab blew the horn. With Absalom dead, the military purpose is accomplished; further pursuit and slaughter of Israelites (who were following Absalom) would be counterproductive. Joab's decision to stop the killing is strategically sound: David will need these Israelites to submit peacefully.</p>",

        "17": "<p>Absalom's burial: thrown into a great pit (<em>pāḥaṯ gāḏôl</em>) in the forest, covered with a great heap of stones (<em>gal-ʾăḇānîm gāḏôl mĕʾōḏ</em>). The burial of shame: no tomb, no anointing, no mourning ritual — thrown into a pit and covered with stones, the standard dishonor-burial for criminals (Josh 7:26, Achan; Josh 8:29, king of Ai). The 'great heap' contrasts bitterly with the pillar in the next verse.</p>",

        "18": "<p><em>ûʾaḇšālôm lāqaḥ wayyaṣṣeḇ-lô ḇĕḥayyāyw ʾeṯ-maṣṣeḇeṯ</em> — 'Absalom in his lifetime had taken and set up for himself the pillar.' <em>maṣṣeḇeṯ</em> (H4676) typically refers to sacred standing stones — this is the only use for a memorial to a person. He named it <em>yaḏ ʾaḇšālôm</em> — 'the hand/monument of Absalom.' The reason: 'for he said, I have no son to preserve my name.' The irony is complete — he erected the monument because his name would otherwise die; instead, the monument in the King's Valley (Kidron) is remembered as the site of the man who died hanging on a tree, not honored by it.</p>",

        "19": "<p>Ahimaaz son of Zadok asks to run with the news (<em>ʾărûṣâ nā' ûʾăḇassĕrâ</em>) — 'let me run and bring the bĕśōrâ.' <em>Bĕśōrâ</em> (H1309, news/tidings/good news) is the root that gives us <em>bāśar</em> (to proclaim good news, H1319 — gospel root). Whether news of a victory is 'good news' depends entirely on the receiver. For the troops, Absalom's death is victory-news; for David, it is devastating news. The same word will carry opposite meanings in the next few verses.</p>",

        "20": "<p>Joab refuses Ahimaaz's request: 'You are not to carry bĕśōrâ today — another day you may carry bĕśōrâ, but today you shall not.' The reason is unstated but implied: today's news will not be received as good news by the king. Joab assigns the Cushite (v21) instead — perhaps calculating that a foreign messenger will be less affected by David's grief, or less likely to be blamed for the news.</p>",

        "21": "<p>The Cushite messenger is sent. <em>Kûšî</em> indicates a sub-Saharan African — his ethnicity marks him as an outsider, possibly a slave or military servant. That the death of the king's son is announced by a Cushite foreigner is one of the narrative's many ironies: the outsider brings the hardest domestic news. The NT has its own Cushite in Acts 8 — an Ethiopian official on whom the Spirit falls through Philip, a foreigner becoming the first African bearer of good news.</p>",

        "22": "<p>Ahimaaz persists — 'come what may, let me run.' His persistence after Joab's refusal is the behavior of someone who genuinely wants to bring news and cannot understand why it should be withheld. The verbal exchange emphasizes the repetition of his request and Joab's reluctant grant: 'Then run.' The doubleness of the messengers sets up the dramatic scene of David at the gate.</p>",

        "23": "<p>Ahimaaz outruns the Cushite by taking the plain route (<em>derek hakikkar</em>) — a longer but more direct path than the mountain route. His faster arrival means he reaches David first with incomplete intelligence. His speed will not help him deliver good news.</p>",

        "24": "<p>David is sitting between the two gates (<em>bên šĕnê haššĕʿārîm</em>) — a distinctive post, the inner space between double-gate structures typical of Bronze Age cities. The watchman's visual line of sight, the report relayed upward from gate to roof, the king waiting — the scene is a masterpiece of suspense pacing. The question David is waiting to have answered is the one the narrative has withheld since chapter 15: what happened to Absalom?</p>",

        "25": "<p>'If he is alone, there is good news in his mouth (<em>bĕśōrâ bĕp̄îw</em>).' David's reading of military messaging protocols: a single runner brings news, not emergency retreat. The king's hope is contained in this tactical reading — good news. But the news David hopes for (safety? return? surrender?) and the good news the runner brings (military victory, Absalom dead) are not the same news.</p>",

        "26": "<p>The second runner — the Cushite — is spotted. 'Another man running alone.' The watchman's double-runner report increases the tension: two messengers, two possible messages, the king waiting between the gates.</p>",

        "27": "<p>'The running of the first one is like the running of Ahimaaz son of Zadok.' David's response: 'He is a good man and comes with good news.' David's identification of Ahimaaz with good news is his own projection. He trusts the priest's son. The gap between David's expectation and the approaching reality is the narrative's sharpest irony.</p>",

        "28": "<p>Ahimaaz reports the military victory and credits YHWH: 'Blessed be YHWH your God, who has delivered up the men who raised their hand against my lord the king.' He prostrates himself. Then David asks the one question: 'Is the young man Absalom safe?' (<em>hăšālôm lannāʿar lĕʾaḇšālôm</em>). He uses the word <em>šālôm</em> — the question is not just 'is he alive?' but 'is he at peace, whole, well?'</p>",

        "29": "<p>Ahimaaz's evasion: 'When Joab sent me, I saw a great commotion but I did not know what it was.' He cannot bring himself to say what he knows. His non-answer condemns David to another agonizing wait while the Cushite arrives. The moral complexity of Ahimaaz's position — he knows the truth but withholds it — mirrors the messenger's dilemma throughout Scripture: how do you tell a father his son is dead?</p>",

        "30": "<p>'Stand aside' — the king dismisses the incomplete messenger with minimal ceremony. The king's attention is entirely on the incoming Cushite, who will complete the picture Ahimaaz could not finish.</p>",

        "31": "<p>The Cushite: 'Good tidings for my lord the king! YHWH has given you justice today against all who rose up against you.' <em>Hiṯbōšĕšû</em> — 'let them be confounded.' Again David asks the only question that matters: 'Is the young man Absalom safe?'</p>",

        "32": "<p>The Cushite's answer is indirect but unmistakable: 'May the enemies of my lord the king and all who rise against you for evil be as that young man is.' The diplomatic circumlocution is clear: Absalom is dead. The Cushite does not say 'he is dead' — he frames it as an imprecation against enemies. But the identification of Absalom with the category 'enemies' is its own kind of judgment on the rebel prince.</p>",

        "33": "<p><strong>wayyirgaz hammelek wayyaʿal ʿal-ʿăliȳaṯ haššaʿar wayyēḇek</strong> — 'The king was deeply shaken and went up to the chamber above the gate and wept.' <em>Rāgaz</em> (H7264) — to tremble, be shaken — is the word used for the Philistines' terror of the Ark (1 Sam 4:13); here it marks David's complete internal collapse. The lament that follows is the OT's most anguished parental cry: <em>bĕnî ʾaḇšālôm bĕnî bĕnî ʾaḇšālôm mî yitten mûṯî ʾanî taḥteykā</em> — 'O my son Absalom, my son, my son Absalom! Would that I had died in your place, I, in your place!' The phrase <em>mî yitten mûṯî ʾanî taḥteykā</em> uses the <em>mî yitten</em> construction (H5414, 'who will give' = 'would that') + the infinitive construct <em>mûṯî</em> (my dying) + <em>taḥteykā</em> (in your place, under you). It is the OT's clearest expression of substitutionary love: the father who wishes he could die in the son's place. The NT's fulfillment is not a wish but a fact: in Christ, the Father does not merely wish the Son could die in our place — he sends the Son to die (Rom 8:32: 'he who did not spare his own Son but gave him up for us all'). David's grief is the fractured image; the cross is the completion.</p>",
    }
}


def main():
    existing = load_comm('mkt-original', '2samuel')
    merge_comm(existing, SAMUEL)
    save_comm('mkt-original', '2samuel', existing)

    import json as _json
    il = _json.loads((ROOT / 'data/interlinear/2samuel.json').read_text())
    all_ok = True
    for ch in range(17, 19):
        ck = str(ch)
        missing = set(il.get(ck, {}).keys()) - set(existing.get(ck, {}).keys())
        if missing:
            print(f'ch {ch} STILL MISSING: {sorted(missing, key=int)}')
            all_ok = False
        else:
            print(f'ch {ch}: complete ({len(existing.get(ck, {}))} verses)')
    if all_ok:
        print('All verses present ✓')
    print(f'Total chapters in file: {len(existing)}')


if __name__ == '__main__':
    main()
