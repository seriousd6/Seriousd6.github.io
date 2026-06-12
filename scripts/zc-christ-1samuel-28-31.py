"""
mkt-christ | 1 Samuel 28-31
Run: python3 scripts/zc-christ-1samuel-28-31.py

Christological framework:
- Ch28: Divine silence that Christ fills — Saul's necromancy exposes the bankruptcy of reaching the dead
  prophet; Christ is the living Mediator who never goes silent (Heb 7:25)
- Ch29: Achish's triple acquittal pattern — "I find no fault" echoes Pilate, but David is sent away
  alive; the inversion reveals what the True Innocent endured
- Ch30: Total recovery / none missing (v19) anticipates John 17:12; ḥāzaq in YHWH (v6) is the
  proto-Gethsemane pattern of strength drawn from the Father when everything else is gone
- Ch31: Saul's suicide vs Christ's submission — the king who refused Gentile humiliation vs the King
  who accepted it all; Saul's death is defeat, Christ's death is victory
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
    "28": {
        "1": "<p>The Philistine mobilization forces David into an impossible position — fighting Israel or exposing himself as a traitor to Achish. Providence will resolve this dilemma through pagan commanders' suspicion (ch 29), but here the crisis is real. God's anointed navigates between two kingdoms, a pattern the True Anointed knows from the inside: the Son of David would also be caught between competing loyalties — family, nation, God — and resolve them not by political maneuvering but by the cross.</p>",

        "2": "<p>David's deliberately ambiguous reply ('You will see what your servant can do') commits him to nothing while keeping Achish satisfied. He is appointed 'permanent bodyguard' — sar-rosh (head-guardian) — an irony: the future king of Israel serving as a Philistine officer's personal protection. Christ similarly entered the domain of his enemies not as conqueror but as servant, operating under structures of authority he would ultimately overturn (Phil 2:6-8).</p>",

        "3": "<p>The narrator interrupts with two backstory facts: Samuel is dead (already established in 25:1) and Saul expelled the mediums. Both facts are necessary for the coming scene. Samuel's absence is a kind of absence-of-mediator; the medium-ban is Saul's formal compliance with Torah (Deut 18:9-12) now about to be violated in desperation. Christ's absence from the disciples after the crucifixion will prompt a similar crisis of 'where do we turn now?' — the answer being the resurrection rather than a séance.</p>",

        "4": "<p>Geography of impending doom: Philistines at Shunem (north of Jezreel Valley), Israel at Gilboa (south). The battle lines that will end Saul's dynasty are drawn. The narrator's camera is cold and factual, like a war correspondent's dispatch. The location Gilboa will become synonymous with catastrophe in David's elegy (2 Sam 1:21). In the shadow of the cross, God's chosen also gathered in Gethsemane — a named place that would mark the pivot between old order and new.</p>",

        "5": "<p>Saul's terror is visceral: rā'âh (saw) the Philistines and wayyirā' (feared) — the same root for seeing and fearing, his heart trembling. The man anointed precisely to lead Israel against enemies is paralyzed. He has become everything the people feared when Samuel warned them about godless kings (8:11-17) — a ruler who extracts but cannot protect. Christ, facing Gethsemane, was also troubled to the soul (Mark 14:34 'perilypos hē psychē mou'), yet moved through fear rather than being consumed by it.</p>",

        "6": "<p>Divine silence on three fronts: dreams, Urim, prophets. This is the complete communications closure — every channel YHWH used to speak to Israel has gone dark. For Saul specifically it is the silence of judgment: YHWH stopped speaking to Saul the moment the Spirit departed (16:14). The silence itself is the answer. Christ on the cross cried 'My God, my God, why have you forsaken me?' (Ps 22:1, Matt 27:46) — the only moment the Father's face was turned away. But Christ's silence was temporary and atoning; Saul's silence is permanent and condemning.</p>",

        "7": "<p>Saul's request — 'find me a bā'ălat-ʾôḇ' (mistress of the ob, a spirit-pit) — is the desperate king seeking what the legitimate prophet once provided. He has driven out the mediums by royal decree and now seeks one in secret at night, a self-contradiction that reveals total moral collapse. The instruction to consult the dead rather than the living (Isa 8:19-20) is exactly the diagnostic Isaiah will make. Christ is the answer to this prohibition: not a medium but the Living Word (John 1:1), the one who has the words of eternal life (John 6:68), who holds the keys of death and Hades (Rev 1:18).</p>",

        "8": "<p>Saul disguises himself (wayyiṯḥappe') and travels by night with two men — a king incognito, hiding from his own decree. The night setting is more than tactical; moral and spiritual darkness attend the visit. Compare Nicodemus who also came to Jesus 'at night' (John 3:2), and Judas who went out 'and it was night' (John 13:30). Darkness marks the boundary between legitimate and illegitimate seeking. Saul's request to 'bring up' (ʿālāh Hiphil) whom he names is the reverse of prayer — summoning upward from below rather than petitioning downward from above.</p>",

        "9": "<p>The woman's fear is legitimate — she references Saul's own edict, not knowing who she is speaking to. Her resistance is an accidental sermon on the law Saul himself enacted and is now violating. The law he applied to others now indicts himself. This mirrors the judgment dynamic Jesus describes in John 5:45: 'Moses, on whom your hopes are set, is the one who will accuse you.' The law that should protect Israel becomes the instrument of Saul's self-condemnation.</p>",

        "10": "<p>Saul swears 'by the LORD' (YHWH) that no punishment will come to her — an oath that invokes the very God whose silence drove him here, and whose Torah prohibits what he is requesting. The oath on YHWH's name to facilitate necromancy is perhaps the deepest irony of the passage. Christ's High Priestly intercession (Heb 7:25) stands in total contrast: he appeals to the Father's character in full alignment with the Father's will, not in contradiction to it.</p>",

        "11": "<p>Saul names Samuel. The specificity matters — he doesn't want a general consultation with the dead but with the prophet who anointed him, who spoke God's word to him, who is now unavailable through any legitimate channel. Samuel was the last legitimate mediator between YHWH and Saul. Christ is the one new Mediator (1 Tim 2:5) who permanently fills the role Samuel held provisionally, available not through death-consulting but through his own death-conquering resurrection.</p>",

        "12": "<p>When the woman sees Samuel, she screams and recognizes Saul — suggesting the apparition's reality shocked even her and that Samuel's appearance was somehow distinctive to her craft. The text takes the apparition seriously without endorsing necromancy as valid spiritual practice. Christ's resurrection appearances similarly startled those who encountered them (Mary in the garden, the disciples on the road to Emmaus) — not because the dead had been invoked but because death had been defeated.</p>",

        "13": "<p>'An ʾĕlōhîm rising from the earth' — the word ʾĕlōhîm (divine beings) is deliberately ambiguous. The woman sees a supernatural figure. Christ descended into the lower regions of the earth (Eph 4:9) and rose — but rising from death through conquest, not from Sheol through summoning. The resurrection ascent is the anti-type of this necromantic 'bringing up': where the medium forces a soul upward, the Father raises the Son by power (Rom 1:4).</p>",

        "14": "<p>Saul identifies Samuel by description: an old man in a robe (mĕʿîl — the prophet's mantle, last mentioned when Samuel's robe was torn at Gilgal in 15:27-28 as a sign of the kingdom's tearing). Even in death Samuel is wearing the garment associated with his prophetic authority and with Saul's rejection. Saul bows his face to the ground before the dead prophet he once obeyed but ultimately defied. The posture of submission that should have been lifelong worship is now a gesture of terror.</p>",

        "15": "<p>Samuel's first word is a rebuke: 'Why did you disturb me?' (rāgaz, agitate). The dead prophet is annoyed to be summoned. Saul's desperate speech summarizes his crisis: God has turned away (sār), Philistines war, no prophets — so he called Samuel. He has replaced prayer with necromancy, the living God with the dead prophet. Christ is the one who answered the disciples' 'master, we're perishing!' (Mark 4:38) and does not sleep, does not need to be awakened from death: 'I am the resurrection and the life' (John 11:25).</p>",

        "16": "<p>'YHWH has become your adversary (ṣar)' — the word ṣar means both enemy and tight-straits (the root of 'distress'). God has become what Israel's enemies should be. This is covenant curse language: Deut 28:63 describes God opposing disobedient Israel as he once blessed them. The stunning reversal — the God you thought was on your side has become the opposing force — finds its NT counterpart not in judgment but in the cross: God makes Christ to be sin (2 Cor 5:21), as if treating his own Son as adversary, to absorb the curse.</p>",

        "17": "<p>Samuel recites the sentence from 15:28 — the kingdom torn from Saul and given to David. What was spoken at Gilgal is now being confirmed in a cave at night through an illicit séance. The word of God has a way of returning regardless of the manner of its delivery. Christ's resurrection was similarly foretold and confirmed through multiple voices across multiple contexts; the resurrection appearances were in part a confirmation of what the Scriptures had promised (Luke 24:44-46).</p>",

        "18": "<p>The hinge cause: 'because you did not obey the voice of the LORD and did not carry out his fierce anger against Amalek.' The sentence traces directly back to the Agag incident in ch 15. Partial obedience — killing almost everyone, sparing the best livestock, keeping the king — brought total consequences. The NT counterpart is sobering: half-hearted discipleship is still disobedience. Christ's obedience was total, 'unto death, even death on a cross' (Phil 2:8), precisely filling the void that Saul's partial obedience created.</p>",

        "19": "<p>'Tomorrow you and your sons will be with me.' This is the death sentence. It will be fulfilled in ch 31. 'With me' — with Samuel in Sheol — is the underside of the NT phrase 'with Christ' (Phil 1:23; Luke 23:43 'with me in paradise'). The same preposition, the same post-death location, but opposite valences: Saul will join the dead in defeat; the thief on the cross will join Christ in paradise. Death sentences spoken from beyond the grave point to the One who has authority over what lies on both sides of death (Rev 1:17-18).</p>",

        "20": "<p>Saul falls full-length on the ground — the complete physical collapse of a man whose spirit has been broken by the word of judgment. He has not eaten all day. The contrast with ch 7 where Samuel proclaimed a fast that preceded victory (7:6) is sharp: here the fast precedes defeat. David's later fast for his dying child (2 Sam 12:16) and Christ's forty-day fast before the temptation (Matt 4:2) are fasts that move toward God rather than fasts imposed by God-forsakenness.</p>",

        "21": "<p>The medium approaches Saul with concern — a pagan woman showing more practical compassion than Saul's own servants have shown him for years. She 'saw that he was greatly terrified' (nib'al mĕ'ōd). The outsider as caregiver recurs in the Gospels: the Samaritan who helps the beaten man, the Syrophoenician woman who presses Jesus for her daughter's healing. Often those marginalized by the religious establishment model the care the establishment fails to provide.</p>",

        "22": "<p>Her insistence that he eat echoes Elijah's story (1 Kgs 19:5-8) in which an angel woke the prophet twice to eat 'because the journey is too great for you.' Here it is a medium rather than an angel, and the journey leads to death rather than Horeb, but the structural parallel — exhausted man, urgent feeding before a decisive journey — underscores how far Saul has fallen from the prophetic pattern. Christ, unlike Elijah, did not need angels to feed him after the cross; he prepared breakfast for his disciples on the shore (John 21:9).</p>",

        "23": "<p>Saul initially refuses — then relents under pressure. The man who refused to refuse Agag's pleading (15:24) now refuses food until his own servants press him. The reversal is complete: Saul who should have been immovable in obedience has become movable only by social pressure. Christ's resistance to compromise was consistent: he refused the tempter's bread in the wilderness (Matt 4:3-4), refused the crowd's desire to make him king by force (John 6:15), refused Pilate's implicit offer of release through accommodation.</p>",

        "24": "<p>The woman slaughters the fattened calf (ēgel-marbēq) — a detail that echoes the prodigal son's homecoming feast (Luke 15:23 'the fatted calf'). Here the feast precedes not restoration but death; the fattened animal is consumed in the shadow of judgment. The NT takes this image and inverts it: the feast at the end of the journey is not the last meal before annihilation but the eschatological banquet of the kingdom (Luke 14:15-24; Rev 19:9).</p>",

        "25": "<p>They ate and left 'that same night.' The chapter closes as it opened: under cover of darkness, moving in secret. The last image of Saul alive in this episode is a king eating at a medium's table at night before walking toward his death. The Last Supper also takes place at night, the bread and cup also shared in the shadow of imminent death — but Christ's meal institutes a covenant, distributes life, and anticipates reunion; Saul's meal is only refueling for a fatal march.</p>",
    },

    "29": {
        "1": "<p>The scene shifts back to before ch 28's night episode (the narrator has been using flashback structure since ch 27). The Philistine assembly at Aphek — the same place where the Ark was captured in ch 4 — is notable. This time David is on the Philistine side. The geography of Israel's humiliations has become the geography of David's military curriculum. Christ similarly operates in enemy-occupied territory — the whole world is under the evil one (1 John 5:19) — and his victory comes from within that territory, not by avoiding it.</p>",

        "2": "<p>David and his men march in review at the rear with Achish — the most awkward military formation in Israel's history. The future king of Israel is formally aligned with Israel's chief enemy. Yet Providence is threading the needle: this alignment will be providentially broken before the battle. God's purposes often appear to require compromising positions that he then resolves without his servant having to commit the act that would compromise them permanently.</p>",

        "3": "<p>The Philistine commanders' suspicion is the instrument of Providence. Their question — 'What are these Hebrews (ʿiḇrîm) doing here?' — uses the ethnic term associated with Israel's outsider status. Achish's defense invokes both David's service record and the time elapsed ('a year or two') — he has become completely trustworthy in Achish's eyes. The irony that a Philistine king better perceives David's integrity than Saul did is sharp. Achish's threefold defense ('is this not David … has he not been with me … I have found no fault in him') will echo Pilate's threefold declaration about Jesus (John 18:38; 19:4, 6).</p>",

        "4": "<p>The commanders' veto is providential rescue. They fear David will turn mid-battle — 'he could turn against us in the fight and become an adversary (śāṭān)' — using the word that means both military opponent and the accusing adversary. Their political calculation unwittingly enacts God's protection of David. The Commander of heaven's armies (Josh 5:14) arranges the removal of his servant from an impossible situation through the strategic self-interest of his enemies. What the commanders intend as insult is actually deliverance.</p>",

        "5": "<p>They cite the battle-hymn — 'Saul has struck his thousands, David his ten thousands.' This song has haunted Saul since 18:7, driven his jealousy, and now reaches across enemy lines to protect David by making Achish's allies distrust him. The very song of David's honor becomes the mechanism of his exemption from fratricide. God's reputation, once established, works on its own — even among those who use it against him. Christ's reputation ('who is this man?') similarly preceded him and shaped how people responded.</p>",

        "6": "<p>Achish's famous declaration — 'As YHWH lives, you are upright and your going out and coming in with me in the camp is good in my eyes, for I have found no evil in you' — invokes YHWH's name while acquitting a Hebrew. This is the third acquittal formula (vv. 3, 6, 9). A pagan king swears by Israel's God to declare Israel's future king innocent. The NT parallel is Pilate's 'I find no guilt in this man' (Luke 23:4; John 18:38) — also a pagan authority, also triple acquittal, but followed not by dismissal but by crucifixion. David escapes what Jesus bore.</p>",

        "7": "<p>'Go back in peace (šālôm)' — the peace-blessing from a Philistine. Saul had tried to kill David; pagan commanders have tried to dismiss him; now he is dismissed in peace. Shalom from an enemy is grace. The disciples received the same greeting from the risen Christ: 'Peace be with you' (John 20:19) — the word of the Risen One to men who had abandoned him, a peace born through the cross that no enemy could prevent.</p>",

        "8": "<p>David's protest — 'What have I done? What fault have you found in me?' — is either genuine frustration at being dismissed or diplomatic theater covering his relief. Either way the words echo innocent-sufferer language from the Psalms (Ps 7:3-5) and will be echoed by Christ's silence before Pilate (Matt 27:12-14) and his question to the arresting soldiers, 'If I am the one you are looking for, let these men go' (John 18:8). The righteous man protests his innocence even when — especially when — surrounded by hostile forces.</p>",

        "9": "<p>'You are good in my eyes as a messenger of God (mal'ak ʾĕlōhîm)' — Achish's highest compliment is to call David an angel. The irony runs deep: the man whom Saul has been hunting as a traitor is regarded by the Philistine king as an angel of God. Christ was called demon-possessed by some and acknowledged as Son of God by others; the contrast reveals how radically the same person can be perceived based on one's spiritual orientation. Even Achish, limited as he is, sees more clearly than Saul in these final chapters.</p>",

        "10": "<p>Achish's final instruction — rise early, return to Ziklag — will lead David directly to the crisis of ch 30. The providential detour through Philistine service has had a purpose: positioning David at Ziklag during Israel's defeat at Gilboa, so that he is not implicated in Saul's death and is therefore available to receive the crown cleanly (2 Sam 2:4). The long circuitous path of the fugitive years now resolves into the direct path to the throne.</p>",

        "11": "<p>David's departure for 'the land of the Philistines' and the Philistines' march to Jezreel — two armies moving in opposite directions, one toward catastrophe and one away from it. The separation is Providence in action. Christ also 'withdrew' (anachōreō) at strategic moments — not from cowardice but from timing: 'his hour had not yet come' (John 7:30; 8:20). When the hour came, he did not withdraw but went deliberately to meet it (John 18:4 'knowing everything that was coming to him').</p>",
    },

    "30": {
        "1": "<p>David returns from Philistia to find Ziklag burned. The Amalekites — the same enemy Saul failed to destroy in ch 15 — have struck. Incomplete obedience has created an enemy who now strikes at the heart of David's household. The theological logic is present but unsentimental: Saul's failure to execute YHWH's judgment has left a wound in Israel's side that bleeds on David's doorstep. Christ's atonement is exhaustive precisely because any incomplete work would leave a remaining source of harm (Heb 10:14 'by one offering he has perfected for all time those who are being sanctified').</p>",

        "2": "<p>The Amalekites took captives but killed none — their calculation was commercial (slaves and ransom) rather than genocidal. This will be significant: the captives can be recovered. The NT counterpart is Satan's 'captivity' of humanity (Eph 4:8; Col 2:15) — taking prisoners but not destroying them, which creates the possibility of Christ's liberation. The Exodus pattern (captivity → rescue) underlies both the Ziklag episode and the cross-event.</p>",

        "3": "<p>The city burned, wives and children taken — David comes home to ash and absence. The triple arrival clause ('David and his men came to the city, and behold, burned with fire, and their wives and sons and daughters taken captive') piles up loss in three strokes. The vocabulary of ruin here (śōrĕpâ bā-'ēš) echoes lament psalms and prophetic judgment oracles. David as the man who returns to ruins will also characterize Christ: 'the foxes have holes, the birds of the air have nests, but the Son of Man has nowhere to lay his head' (Matt 8:20) — always returning to a world that has nothing to offer him but rejection.</p>",

        "4": "<p>'They wept until they had no more strength to weep (ʾad ʾăšer ʾên-bāhem kōaḥ libkôt)' — exhaustion of grief. This is one of the most human moments in the narrative. David's men are not heroes here; they are fathers and husbands broken by loss. Christ 'wept' (John 11:35) at Lazarus's tomb — the God of the universe grieving alongside those who grieve, entering the experience of devastation from the inside. The incarnation means Christ has sat where David's men sat, crying without strength to continue crying.</p>",

        "5": "<p>David's two wives — Ahinoam and Abigail — are among the captives. The personal dimension of the crisis is pressed home: this is not abstract political adversity but David's own household gone. The names connect back to earlier narrative threads: Ahinoam from Jezreel (25:43), Abigail the widow of Nabal (ch 25). These women who came to David through distinct providential paths are now at risk together. Christ's 'household' — those the Father gave him — are likewise at risk (John 17:11 'protect them in your name').</p>",

        "6": "<p>'David strengthened himself in the LORD his God (wayyitḥazzēq dāwīḏ ba-YHWH ʾĕlōhāyw)' — the fulcrum verse of chapter 30. His men speak of stoning him; every external support is gone; he has no military resource, no political cover, no family. In this stripping down to nothing he turns not to strategy but to God. This is the proto-Gethsemane pattern: when everything else is unavailable, the anointed man draws strength from the Father alone. Christ in Gethsemane — sweat like drops of blood, disciples asleep — was strengthened by an angel (Luke 22:43). The pattern is consistent: the nadir of human support is the place where divine strengthening is most clearly operative.</p>",

        "7": "<p>The ephod inquiry — through Abiathar, the priest who fled to David when Saul killed the priests at Nob (22:20). Abiathar is himself a refugee carrying Israel's legitimate cultic apparatus. David's access to the ephod at his lowest moment contrasts with Saul's complete communicative isolation in ch 28. David can inquire; Saul cannot. The reason is not moral superiority but covenant standing: YHWH speaks to his anointed. Christ has permanent access to the Father (John 11:41-42 'I knew that you always hear me') — not earned through spotless performance but through the relational reality of the Son.</p>",

        "8": "<p>The divine answer is a double infinite absolute construction: rādōp tirdōp (pursue, you will certainly pursue) and haṣṣēl taṣṣîl (you will certainly recover). The grammar of certainty — God not merely permitting but guaranteeing — stands in total contrast to Saul's triple silence. When God speaks, it is with the kind of certainty Christ's 'truly, truly I say to you' (amēn amēn) echoes: not possibility but declaration. 'I will build my church and the gates of hell will not prevail against it' (Matt 16:18) is the same grammatical confidence in eschatological terms.</p>",

        "9": "<p>Six hundred men begin the pursuit — the number that has characterized David's band since the Adullam days (22:2). The brook Besor becomes the threshold of endurance: some cannot cross. The mission continues without the exhausted, but they will not be forgotten (v 21-25). Christ's disciples similarly scattered at the arrest — 'they all forsook him and fled' (Mark 14:50) — yet he promised he would go ahead of them to Galilee (Mark 14:28), as if already planning the reunion across the threshold.</p>",

        "10": "<p>Four hundred press on; two hundred remain. The gap at the Besor creates the later justice problem (vv 22-25) that David resolves with grace. The division between those who complete the mission and those who cannot is not treated as moral failure but as physical limit. Christ's parable of the workers (Matt 20:1-16) makes an analogous point: the latecomers receive the same wage, generating protest from the early workers — the same protest David's 'wicked and worthless men' will make in v 22. Grace is always being resisted by merit-logic.</p>",

        "11": "<p>An Egyptian slave is found in the field — abandoned by his Amalekite master when he fell ill. He is fed and restored (v 12) before being asked anything. The provision precedes the petition, modeling the grace-before-demand order that characterizes YHWH's relationship with Israel (Exod 19:4 'I bore you on eagles' wings and brought you to myself' comes before the ten commands). Christ healed and fed before he called; the Sermon on the Mount beatitudes (blessings) precede the commands.</p>",

        "12": "<p>Fig cake and raisins — emergency rations. 'His spirit returned to him' after three days without food or water: a three-day recovery that prefigures resurrection rhythm (Hosea 6:2; Matt 12:40). The Egyptian revives and becomes the guide to the enemy camp. The one who was abandoned and left for dead leads the living to victory. This is the pattern of Christ: abandoned, left in a tomb, raised on the third day — and then becoming the guide ('I am the way') through whom all else is recovered.</p>",

        "13": "<p>The Egyptian's identification — slave of an Amalekite, abandoned when sick — makes him a double marginal figure: a slave (outsider by status) and a castoff (outsider even within that low status). David does not interrogate before feeding; he feeds and then asks. The reversal of normal interrogation protocol is grace logic. The centurion's servant (Matt 8:5-13), the Syrophoenician's daughter (Mark 7:24-30), the Samaritan leper (Luke 17:16) — Christ similarly engages the marginalized before they can establish any claim.</p>",

        "14": "<p>The Egyptian's intelligence report: they raided Negeb Cherethites, Negeb Judah, Negeb Caleb, and Ziklag. The Cherethites are the Philistine elite guard David will later employ (2 Sam 8:18) — a reminder that the geopolitical web is complex. For now the report is what matters: the Egyptian knows where the plunderers are. The guide from outside the covenant community providing insider intelligence is a pattern of grace: Rahab in Jericho, the Gibeonites who tricked Israel into treaty, the Roman centurion who builds the synagogue (Luke 7:5).</p>",

        "15": "<p>The Egyptian's condition for service: 'Swear to me by God (ʾĕlōhîm)' that you won't kill me or return me to my master. He is bargaining from a position of no power with the one resource he has: information. David swears and the covenant is made. The former slave becomes an ally. Christ's inclusion of the marginalized into his covenant community operates on the same principle — not demanding performance first, but receiving the person and then sending them into service (Zacchaeus, Luke 19:5-9).</p>",

        "16": "<p>The Amalekites found spread across the landscape, celebrating their plunder, totally off-guard. The imagery of a victory feast that is actually the prelude to defeat is eschatologically resonant: 'as in the days of Noah … eating and drinking … until the flood came and swept them all away' (Matt 24:38-39). The party that does not know it is the last party. The booty celebration of the enemy is routinely interrupted by divine judgment; Belshazzar's feast (Dan 5) is the paradigmatic OT version.</p>",

        "17": "<p>David attacks 'from the twilight (nešep) until the evening of the next day' — a full night and day of battle, an extraordinary military exertion. 'Not one of them escaped except four hundred young men who fled on camels.' The completeness of the victory inverts the incompleteness of Saul's Amalek campaign (15:9 'the best of … the best of'). What Saul failed to execute completely, David essentially does — though not by YHWH's direct ḥērem command but by necessity of recovery. The Church's warfare against the principalities (Eph 6:12) is similarly meant to be comprehensive, not partial.</p>",

        "18": "<p>'David recovered everything the Amalekites had taken, including his two wives.' The recovery is complete, beginning with the personal — his wives named first. What was lost is found, what was taken is returned. The parable of the lost sheep ends: 'I have found my sheep that was lost' (Luke 15:6); the father of the prodigal says 'this son of mine was dead and is alive again, was lost and is found' (Luke 15:24). Recovery of the lost is the essential movement of the gospel narrative, and David's total recovery at Ziklag is one of its OT forms.</p>",

        "19": "<p>'Nothing was missing (lō' neʿdar)' — not young or old, sons or daughters, any spoil, anything taken. The inventory-completeness formula is theologically significant. Christ's high priestly prayer in John 17:12: 'While I was with them, I kept them in your name … I guarded them, and not one of them was lost.' The shepherd who recovers all that was entrusted to him is the pattern David enacts and Jesus fulfills. In both cases the loss was real, the danger was real, and the recovery was total.</p>",

        "20": "<p>The spoil beyond the recovered goods — the Amalekite flocks and herds driven ahead. The men declare 'this is David's spoil' (šĕlal dāwīḏ), acknowledging him as king in all but name. The military victory generates the redistribution of wealth that will characterize David's later kingdom and that Christ's eschatological kingdom will accomplish in ultimate form: the meek inheriting the earth (Matt 5:5), the hungry filled with good things (Luke 1:53).</p>",

        "21": "<p>David returns to the two hundred exhausted men at the Besor. They come out to 'meet' (liqqrā'ṯ) him — the same verb used for the royal reception procession. Even the men who couldn't keep up greet the returning victor. Christ's return (parousia) is described similarly: the 'meeting' (apantēsis, 1 Thess 4:17) of those who wait for the returning Lord, some of whom have been too 'exhausted' (dead) to participate in the active campaign but are raised to share in the victory.</p>",

        "22": "<p>'Wicked and worthless men' (benê-beliyyaʿal, sons of Belial) — the same phrase used for Eli's sons (2:12) and Nabal (25:17, 25). They want to exclude the two hundred from the spoil: merit logic, compensation-for-service, the economy of deserve. This logic is structurally opposed to grace. The merit-economy objectors appear throughout the gospel narratives: the elder brother of the prodigal, the workers who resent the latecomers' equal pay, the disciples arguing about greatness. Every outbreak of merit-logic in the NT has its OT precedent in exactly this kind of scene.</p>",

        "23": "<p>'My brothers (ʾaḥay), you must not act this way with what the LORD has given us.' David reframes the spoil as divine gift rather than earned wages — a theological move that redefines the entire redistribution question. If the victory came from YHWH, the spoil is YHWH's to distribute through his anointed, not the combatants' to allocate by merit. Christ's parable of the workers (Matt 20:15) makes exactly this argument: 'Am I not allowed to do what I choose with what belongs to me?'</p>",

        "24": "<p>'The share of the one who goes down to battle shall be the same as the share of the one who stays with the equipment (kî kĕḥēleq hayyōrēd ba-mĕlḥāmāh ûkĕḥēleq hayyōšēḇ ʿal-hakkēlîm yĕḥālōqû yāḥdāw).' David's ruling becomes Israel's rule (v 25). Equal share regardless of contribution is the logic of grace: those who could not fight receive the same as those who did — because the victory was YHWH's, not theirs. Paul applies the same principle to resurrection: those who have 'fallen asleep' receive the same inheritance as those who are alive at the coming (1 Thess 4:15).</p>",

        "25": "<p>'David made it a fixed rule (ḥōq ûmišpāṭ) for Israel to this day.' A grace-principle becomes institutionalized law. The gospel pattern — grace as the rule, merit as the exception — is encoded into Israel's military customs through this moment. The institutionalization of grace in law is what the Torah itself is at its core: YHWH's redemption of slaves codified into ongoing covenant obligations. Christ does not abolish this institutionalized grace but fulfills and deepens it (Matt 5:17).</p>",

        "26": "<p>David distributes gifts to the elders of Judah from the spoil. He calls them 'my friends (rēʿay)' and frames the gift as from 'the LORD's enemies.' He is already governing — not yet crowned, but acting in the role. The distribution to Judah's cities is proto-kingly: surveying his future domain, building the network of loyalty that will coalesce into his coronation at Hebron (2 Sam 2:4). Christ's pre-resurrection ministry similarly built networks of relationship across Galilee and Judea that became the infrastructure of the early church.</p>",

        "27": "<p>Bethel, Ramoth-negeb, Jattir — the first of a list of southern cities. These are towns of the Negeb, the semi-arid southern zone that is David's operational theater. The systematic distribution of gifts anticipates the systematic distribution of the kingdom — the king establishing presence across territory before formal coronation. The pattern of the Kingdom of God is similar: sown widely before the harvest, present before acknowledged (Luke 17:20-21 'the kingdom of God is in your midst').</p>",

        "28": "<p>Aroer, Siphmoth, Eshtemoa — continuing the distribution list. The geographical specificity serves as a kind of pre-census of David's future domain. Each town named is a future subject community receiving advance grace from the coming king. The eschatological feast of the kingdom similarly draws from all directions (Luke 13:29 'they will come from east and west, north and south').</p>",

        "29": "<p>Racal, the Jerahmeelite towns, the Kenite towns — the list extends to include non-Israelite communities absorbed into David's network (Jerahmeelites and Kenites are affiliated but distinct peoples). The coming Davidic kingdom has from its pre-coronation phase included outsiders. This prefigures the Gentile inclusion in the Messianic kingdom that the prophets would later announce and the NT would enact (Eph 2:11-13 'you who once were far off have been brought near by the blood of Christ').</p>",

        "30": "<p>Hormah, Bor-ashan, Athach — towns of the extreme south. The list is nearly comprehensive in covering the Negeb region. Hormah (ḥormāh) is particularly resonant: its name is related to ḥērem (devoted-destruction), and it was the site of Israel's first major defeat under Moses (Num 14:45) and later a victory (Num 21:3). David is redeeming the geography of past failure, distributing grace in the very places where Israel had once been routed. Christ similarly goes to Galilee (dismissed by the establishment: 'no prophet comes from Galilee', John 7:52) and makes it the region of his primary ministry and resurrection appearances.</p>",

        "31": "<p>Hebron — the last city in the list, and the most significant. Hebron is where Abraham settled (Gen 13:18) and where the patriarchs are buried (Gen 23). Sending gifts to Hebron's elders is an act of Abrahamic-covenantal significance: David is positioning himself in the land of promise, in the city of the patriarchal covenant. It is at Hebron that he will be anointed king of Judah (2 Sam 2:4) and later all Israel (2 Sam 5:3). The last word of chapter 30 is Hebron — pointing forward to the kingship about to come, just as the last chapters of the OT point forward to the King yet to come.</p>",
    },

    "31": {
        "1": "<p>The final battle. The Philistines press Israel at Gilboa; Israel flees; the slain fall on the mountain. The same mountain that will become a curse in David's elegy (2 Sam 1:21 'let there be no dew or rain on you, O mountains of Gilboa') is now the killing field of Saul's dynasty. The defeat of God's anointed king by pagan forces echoes the exile-judgment of later history and anticipates the cross: the One sent by God, rejected, handed to the Gentiles, executed on a hillside. But the cross is Golgotha, not Gilboa — and unlike Gilboa, Golgotha is followed by resurrection.</p>",

        "2": "<p>Jonathan, Abinadab, Malchishua — Saul's three sons fall with him. Jonathan's death is the grief-center of the chapter and of David's lament (2 Sam 1:26). The son who had recognized YHWH's hand on David (23:17) dies in his father's failed battle. The innocent die alongside the guilty; the faithful friend shares the fate of the unfaithful king. Christ's disciples were similarly endangered by association with him ('if they have kept my word, they will keep yours also', John 15:20) — but the pattern reverses at the resurrection: the disciples survive precisely because Christ dies.</p>",

        "3": "<p>The battle 'presses hard' (tibkad, heavy) against Saul. He is wounded by archers. The word kābēd (heavy) echoes the 'heavy' glory (kāḇôḏ) that departed in ch 4 and that should have rested on the king — but Saul has been operating without YHWH's protective weight since the Spirit left him (16:14). Now the physical weight of arrows replaces the metaphysical weight of divine presence. Christ's carrying of the cross — the literal weight of the instrument of execution — is the weight of all human rejection of divine presence, compressed into one body.</p>",

        "4": "<p>Saul's request to his armor-bearer — 'Pierce me with your sword so these uncircumcised men cannot mock me' — is the defining statement of his kingship. He fears contempt more than death. He has been afraid of public humiliation throughout (15:30 'honor me before the elders'), and that fear has governed his disobedience and his end. Christ suffered everything Saul fled from: stripped of his garments (John 19:23-24), mocked with a crown of thorns (John 19:2), taunted on the cross (Matt 27:40-44), crucified among thieves. The total submission to contempt that Saul refused was the path of the true King.</p>",

        "5": "<p>The armor-bearer sees Saul is dead and falls on his own sword. Loyal to the end in a terrible way — following his master into death by his own hand. The contrast with Abishai and Joab who would die protecting David is implicit. But the greater contrast is with the disciples: they fled rather than dying with Jesus. And the resurrection makes their survival retrospectively significant — they are needed as witnesses. Saul's armor-bearer has no resurrection to await; his death is simply the final clause of a sentence that has been ending since ch 13.</p>",

        "6": "<p>'Saul died, and his three sons, and his armor-bearer, and all his men on that day.' The summarizing verse is stark. The dynasty that began with the people's demand in ch 8 ends in a single sentence. All-on-one-day is the narrator's way of marking the decisive end. The contrast with Christ's death is structural: Christ dies alone among his companions — not because he fails but because he must. His death is not the dynasty's end but the dynasty's fulfillment: 'this is the heir, come, let us kill him and the inheritance will be ours' (Luke 20:14) — a plan that backfires into resurrection.</p>",

        "7": "<p>Israel abandons its cities when news of the defeat spreads; Philistines occupy them. The collapse of a kingdom when its king falls mirrors the cosmic dimension of the spiritual battle: if the king falls, the people scatter. The disciples' scattering at the arrest of Jesus (Matt 26:31, quoting Zech 13:7 'strike the shepherd and the sheep will scatter') follows this exact pattern. But the resurrection reverses it: the scattered sheep are gathered again around the Risen Shepherd (John 10:16 'I have other sheep … they will hear my voice, and there will be one flock').</p>",

        "8": "<p>The Philistines find Saul and his sons fallen on Gilboa the next day, while coming to strip the slain. Stripping the dead of armor and valuables was standard ANE practice — weapons in temples, bodies as trophies. The soldiers gambling for Jesus's garments (John 19:23-24) are the NT echo of this stripping. In both cases the victors take the defeated man's clothing. But the Resurrection produces an empty tomb and a folded burial cloth (John 20:6-7) — the stripping reversed, the absence announcing presence.</p>",

        "9": "<p>They cut off his head (karṯû ʾeṯ-rōšô), strip his armor, and send bĕśōrāh (victory-news) through Philistia. The same word bĕśōrāh/bāśar that runs through Isaiah's servant songs (Isa 40:9; 52:7) and that becomes euangelion (gospel) in the NT is used here for pagan triumphalism over Israel's fallen king. The Philistines have their gospel: the enemy is dead. The NT gospel is the anti-type: the true King who appeared dead is alive, and the gospel is that the enemies of God have been defeated by the death they thought was their victory.</p>",

        "10": "<p>Saul's armor placed in the temple of Ashtaroth; his body pinned to the wall of Beth-shan. Both actions are acts of cultic trophy — victory announced to the goddess and the walls of a strategic city simultaneously. Saul's body becomes propaganda for Philistine religion. Christ's body on the cross was similarly displayed as propaganda — the Romans' demonstration of what happens to would-be kings (the titulus 'KING OF THE JEWS'). But crucifixion as propaganda becomes resurrection as proclamation: 'what you meant for a trophy, God displayed as triumph' (1 Cor 1:18-25).</p>",

        "11": "<p>'When the inhabitants of Jabesh-gilead heard what the Philistines did to Saul' — the news travels south to the city that owes its existence to Saul's first victory (ch 11). Their response in vv 12-13 is the last act of covenant loyalty toward a fallen king. The city Saul rescued now risks itself to rescue Saul's body. Covenant fidelity persists beyond the covenant partner's failure. The church's care for its martyred dead — burying them honorably against the empire's practice of leaving them exposed — continues this pattern of post-mortem covenant loyalty.</p>",

        "12": "<p>All the warriors of Jabesh-gilead travel all night, take the bodies from Beth-shan's wall, return and burn them — an unusual practice for Israelites (normally burial without burning), perhaps to prevent further desecration at distance, or reflecting Transjordanian custom. They then bury the bones under the tamarisk at Jabesh. The all-night journey of the warriors echoes the women who came to the tomb at dawn (Mark 16:2) and the disciples who ran to the tomb at the news of resurrection (John 20:3-4). In both cases, urgent nighttime action to recover what was lost to enemies. But the disciples found an empty tomb; Jabesh-gilead found bodies that stayed dead.</p>",

        "13": "<p>They bury Saul's bones under the tamarisk (ēšel) at Jabesh and fast seven days. The tamarisk tree is where Saul had his command post (14:2; 22:6) — his 'headquarters tree.' He is buried under his own tree, a final irony of a king who sat under the tamarisk giving orders and ends under it without breath. The seven-day fast is the mourning period for the dead king — a death that, unlike the deaths in 2 Samuel 12 or the NT, has no resurrection to interrupt it. First Samuel ends not with resurrection but with honest death — the kings and prophets of the old covenant pointing forward to the One whose death would be the last word on death itself (1 Cor 15:54-55).</p>",
    }
}


def main():
    import json as _json
    existing = load_comm('mkt-christ', '1samuel')
    merge_comm(existing, SAMUEL)
    save_comm('mkt-christ', '1samuel', existing)

    # Verify completeness
    il = _json.loads((ROOT / 'data/interlinear/1samuel.json').read_text())
    all_ok = True
    for ch in range(28, 32):
        ck = str(ch)
        missing = set(il.get(ck, {}).keys()) - set(existing.get(ck, {}).keys())
        if missing:
            print(f'ch {ch} STILL MISSING: {sorted(missing, key=int)}')
            all_ok = False
        else:
            print(f'ch {ch}: complete ({len(existing.get(ck, {}))} verses)')
    if all_ok:
        print('All verses present ✓')
    total = sum(len(existing.get(str(c), {})) for c in range(28, 32))
    print(f'Total chapters in file: {len(existing)}')


if __name__ == '__main__':
    main()
