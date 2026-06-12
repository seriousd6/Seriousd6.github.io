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
  }
}

LAM_CHRIST = {
  "1": {
    "1": "<p>A shadow: 'How deserted she sits, the city once full of people! She has become like a widow.' The desolate, widowed city is the image of the church without its Lord — or more precisely, the image of a humanity exiled from God's presence. Christ's answer to this desolation is his promised return: 'I will not leave you as orphans; I will come to you' (John 14:18). The 'widow' image also sets up its reversal in the new creation, where the city whose husband seemed absent is reunited with him: 'the holy city, new Jerusalem, coming down out of heaven from God, prepared as a bride adorned for her husband' (Rev 21:2).</p>",
    "2": "<p>A theme: 'She weeps bitterly in the night ... among all her lovers there is none to comfort her.' The repeated absence of a comforter runs through Lamentations like a refrain (1:2, 9, 16, 17, 21; 2:13). Christ's answer is direct and explicit: 'I will ask the Father, and he will give you another Helper [<em>Parakletos</em>]' (John 14:16). The word <em>Parakletos</em> (Comforter, Advocate, Helper) is the NT's answer to Lamentations' lament. The Spirit is given precisely because Zion's repeated cry — 'there is no comforter' — demands fulfillment. The weeping in the night anticipates the disciples' grief on the night of the crucifixion; the resurrection morning transforms night-weeping into morning joy (Ps 30:5; John 20:11-16).</p>",
    "3": "<p>A shadow: 'Judah has gone into exile because of affliction and hard servitude.' The exile of God's people is the condition of all humanity in sin — alienated from God's presence and under hard servitude. Christ enters that exile to bring the exiles home: 'while we were still sinners, Christ died for us' (Rom 5:8); 'once you were alienated and enemies... he has now reconciled' (Col 1:21-22). The parable of the prodigal son (Luke 15:11-24) is exile-and-return told from the Father's perspective; Christ is the agent who makes the return possible.</p>",
    "4": "<p>A shadow: 'The roads to Zion mourn because no one comes to her appointed feasts. All her gates are desolate.' The roads to Zion — the pilgrimage routes that brought worshippers to the temple at Passover, Pentecost, and Tabernacles — are empty. Christ is the new way to the Father: 'I am the way, and the truth, and the life. No one comes to the Father except through me' (John 14:6). The blocked roads of Lamentations are reopened by Christ; the pilgrimage that Lamentations mourns as impossible is restored when Christ opens the new and living way through his flesh (Heb 10:20).</p>",
    "5": "<p>A type: 'Her adversaries have become her masters; her enemies prosper, because the LORD afflicted her for the multitude of her transgressions.' YHWH's own hand in Zion's affliction is the key theological claim: the enemies prevailed only because YHWH allowed it for Israel's sin. This is the shadow of the cross: 'He who did not spare his own Son but gave him up for us all' (Rom 8:32). The Father's active role in the Son's suffering — not merely permitting but delivering him up (<em>paredōken</em>, Rom 4:25; Acts 2:23) — is the NT form of Lamentations' claim that YHWH afflicted his own city. The difference: Jerusalem suffered for her own transgressions; Christ suffered for ours.</p>",
    "6": "<p>A shadow: 'From the daughter of Zion all her majesty has departed.' The departure of Zion's glory (<em>hadar</em>) is the final stage of what began when Ezekiel saw the glory (<em>kabod</em>) departing from the temple (Ezek 10:18; 11:23). The glory that Lamentations mourns returns in Christ, who is 'the radiance of the glory of God and the exact imprint of his nature' (Heb 1:3). The Word who was with God and was God 'became flesh and dwelt among us, and we have seen his glory' (John 1:14) — the departed <em>kabod</em> reappears in the incarnate Son.</p>",
    "7": "<p>A theme: 'Jerusalem recalled in the days of her affliction and exile all the precious things she once possessed.' The memory of former blessing intensifies present grief. The NT answers the memory of loss with the Lord's Supper: 'Do this in remembrance of me' (Luke 22:19). The act of remembering is transformed — not a memory of lost blessings that deepens grief, but a remembrance of the sacrifice that secures eternal blessing. The one who is remembered is also the one who 'always lives to make intercession' and has never left his people (Heb 7:25).</p>",
    "8": "<p>A type: 'Jerusalem sinned gravely; therefore she has become unclean. All who once honored her now despise her, for they have seen her nakedness.' The uncleanness of sin that strips away honor and leaves a person exposed — spiritually naked before God and socially shamed before people — is the condition Christ takes on at the cross. He who 'knew no sin' was 'made sin for us' (2 Cor 5:21), becoming publicly unclean and despised so that we might be made the righteousness of God. His 'nakedness' on the cross (the soldiers divided his garments, John 19:23-24) is the typological fulfillment of Zion's exposed nakedness.</p>",
    "9": "<p>A type: 'Her uncleanness clung to her skirts; she did not consider her future. Her fall was appalling, with no one to comfort her.' The ritual uncleanness (<em>niddah</em>) that clings to Zion is the type Christ resolves in healing the woman with the discharge of blood (Mark 5:25-34): she who suffered from uncleanness touched Christ and was made clean rather than making him unclean. He absorbed her uncleanness and gave her cleanness — the mechanics of substitutionary cleansing in miniature. The one who 'did not consider her future' is met by Christ who secures her future: 'I know the plans I have for you' (Jer 29:11 → fulfillment in Christ's resurrection which guarantees our future).</p>",
    "10": "<p>A type: 'The enemy stretched out his hand over all her treasures. She watched the nations enter her sanctuary, which you had forbidden to enter your assembly.' The desecration of the sanctuary — the nations entering what was forbidden — is the crisis of temple theology that Jesus addresses: 'Destroy this temple, and in three days I will raise it up' (John 2:19). The temple that enemies defiled was always a shadow; Christ is the true temple (John 2:21: 'he was speaking about the temple of his body'). The temple's defilement is the occasion for the revelation that the entire sacrificial system was a pointer to the one whose body is the real dwelling place of God.</p>",
    "11": "<p>A shadow: 'All her people groan as they search for bread. They traded their treasures for food to keep themselves alive.' Selling precious things for physical sustenance is the condition of spiritual famine — the trading away of lasting value for immediate survival. Christ addresses this condition directly: 'I am the bread of life; whoever comes to me shall not hunger, and whoever believes in me shall never thirst' (John 6:35). The prodigal son who 'traded his treasures' (his inheritance) for food in the far country (Luke 15:14-16) is the archetypal form of this exchange; Christ is the Father who restores the lost son to the feast.</p>",
    "12": "<p>A type: 'Is it nothing to you, all you who pass by? Look and see if there is any sorrow like my sorrow, which was brought upon me, which the LORD inflicted on the day of his fierce anger.' The suffering of Jerusalem — the Daughter of Zion who has suffered at YHWH's hand for her sins — is one of the OT's primary types of Christ's passion. The NT passion accounts use the Lamentations framework: the mockers who wag their heads at the crucified Jesus echo Lamentations (Lam 2:15: 'all who pass by clap their hands at you; they hiss and wag their heads at the daughter of Jerusalem'; Matt 27:39). But the typological inversion is crucial: Jerusalem suffers for her own sins; Christ suffers for ours. The language of innocent suffering that Lamentations applies to the city becomes, in the NT, applicable to the one who is truly innocent.</p>",
    "13": "<p>A type: 'From on high he sent fire into my bones. He spread a net for my feet and turned me back. He has left me desolate and faint all day long.' The divine affliction — fire, net, desolation — describes what the Servant of Isaiah experiences: 'it was the will of the LORD to crush him; he has put him to grief' (Isa 53:10). Jesus in Gethsemane takes on Zion's experience of divine assault: 'Father, if you are willing, remove this cup from me. Nevertheless, not my will, but yours, be done' (Luke 22:42). He accepts the fire from on high and the net for his feet so that those who are caught in the net of sin may go free.</p>",
    "14": "<p>A type: 'The yoke of my transgressions was tightly bound; braided together by his hand and placed on my neck. He has sapped my strength.' The yoke of transgression placed on the neck is what Christ explicitly comes to remove and replace: 'Take my yoke upon you, and learn from me, for I am gentle and lowly in heart, and you will find rest for your souls. For my yoke is easy, and my burden is light' (Matt 11:29-30). The heavy yoke of sin and judgment that Lamentations describes is the yoke Christ carries to the cross; he removes it from our necks and gives us the easy yoke of union with him instead.</p>",
    "15": "<p>A type: 'He has trodden as in a winepress the virgin daughter of Judah.' The winepress of divine judgment that YHWH treads against his own people in Lamentations 1:15 is the image reversed and fulfilled in Revelation 19:15: 'He will tread the winepress of the fury of the wrath of God the Almighty.' In Lamentations YHWH treads his own city in judgment; in Revelation, Christ treads his enemies in the final judgment. Christ stood in the winepress of judgment (Isa 63:3: 'I have trodden the winepress alone') — absorbing divine wrath in his passion — so that the final winepress is for enemies, not for those who are in him.</p>",
    "16": "<p>A theme: 'For these things I weep; my eyes stream with tears because no comforter is near who could revive my spirit.' The repeated absence of a comforter in Lamentations is the cry that Christ fills in person. Jesus weeps over Jerusalem (Luke 19:41) — he is the comforter who is near, even if the people do not recognize him. After his resurrection he gives the Paraclete (John 14:26; 15:26; 16:7), so that no follower of Christ can ever again say 'there is no comforter.' The Spirit's presence in the church is the permanent answer to Lamentations' lament.</p>",
    "17": "<p>A type: 'Zion stretches out her hands, but there is no one to comfort her.' The outstretched hands of the desolate city = the posture of the crucified: Christ on the cross stretches out his hands in the ultimate posture of abandonment. But Zion's outstretched hands find no response; Christ's outstretched hands are the active embrace of the world he came to save (John 3:16). The cross that looks like Zion's desolation is actually the posture by which he draws all people to himself (John 12:32).</p>",
    "18": "<p>A revelation of God: 'The LORD is in the right, for I rebelled against his command.' The community's confession that YHWH's judgment is just — even against themselves — is the OT foundation for Paul's declaration that God is 'just and the justifier of the one who has faith in Jesus' (Rom 3:26). God's righteousness in judging sin (demonstrated fully at the cross) and his mercy in justifying sinners (also demonstrated at the cross) meet in Christ. Lamentations says YHWH is in the right; Paul says the cross proves it while also making the guilty righteous.</p>",
    "19": "<p>A shadow: 'I called to my allies, but they deceived me. My priests and my elders perished in the city.' The human allies and leaders who fail Zion are the shadow that throws Christ into relief. Where earthly priests and elders perish in their attempts to help, Christ is the high priest 'who always lives to make intercession' (Heb 7:25) and the advocate who does not deceive. When all human helpers fail — when the allies become deceivers and the priests perish seeking bread — the only sufficient intercessor is the one who passed through the heavens (Heb 4:14) and appears before the Father on our behalf (1 John 2:1).</p>",
    "20": "<p>A type: 'See, O LORD, how distressed I am! My insides churn; my heart writhes within me, for I have sinned deeply.' Zion's prayer-cry of inner anguish prefigures Christ's Gethsemane: 'My soul is very sorrowful, even to death' (Matt 26:38); 'being in agony he prayed more earnestly; and his sweat became like great drops of blood falling down to the ground' (Luke 22:44). Christ enters Zion's anguish — the anguish of one who must face divine wrath — and makes it his own. The difference: Zion's anguish was over her own sin; Christ's anguish was over ours, which he had taken as his own.</p>",
    "21": "<p>A shadow: 'They heard my sighing; there is no one to comfort me. All my enemies heard of my misery and are glad.' The gloating of enemies over Zion's fall is the condition Christ reverses at the resurrection. The enemies who were glad over the crucified Jesus (Ps 22:6-8; Matt 27:41-43) face the reversal on Easter: the one they destroyed is Lord. Christ's resurrection is the divine vindication against all who are glad over God's apparent defeat — and the permanent comfort of those who weep with Zion.</p>",
    "22": "<p>A theme: 'Let all their wickedness come before you, and deal with them as you have dealt with me for all my transgressions.' The imprecatory petition of Lamentations — that YHWH apply the same judgment to enemies that he applied to Jerusalem — points to the final judgment, which Christ executes (Acts 17:31: 'he has fixed a day on which he will judge the world in righteousness by a man whom he has appointed'). But Christ is also the one who absorbs judgment for those who trust him, so that 1 Thess 5:9 can say 'God has not destined us for wrath, but to obtain salvation through our Lord Jesus Christ.' The same day of wrath that Lamentations invokes against enemies is deflected from believers by the cross.</p>"
  },
  "2": {
    "1": "<p>A shadow: 'How the Lord shrouded the daughter of Zion in his anger! He hurled the splendor of Israel down from heaven to earth.' The cloud of divine wrath covering Zion anticipates the darkness at the crucifixion: 'From the sixth hour there was darkness over all the land until the ninth hour' (Matt 27:45). The wrath that shrouded Zion fell on Christ; the darkness at noon is the physical sign that the Son was absorbing the full weight of God's anger against sin. The splendor 'hurled down' = the humiliation of the incarnate Son, who 'though he was in the form of God, did not count equality with God a thing to be grasped, but emptied himself' (Phil 2:6-7).</p>",
    "2": "<p>A revelation of God: 'The Lord swallowed up all Jacob's dwellings without pity; in his wrath he broke down the strongholds of the daughter of Judah.' YHWH's wrath enacted without restraint — 'without pity' — shows the full weight of what sin costs. This same 'without pity' is the measure of the cost of redemption: 'He who did not spare his own Son but gave him up for us all' (Rom 8:32). The Greek <em>ouk epheisato</em> (did not spare) echoes exactly the Hebrew <em>lo chamal</em> (without pity/without sparing) — the same absence of restraint that fell on Jerusalem fell on the Son of God at the cross, so that it need not fall on those who are in him.</p>",
    "3": "<p>A type: 'In fierce anger he cut off every horn of Israel. He withdrew his right hand in the face of the enemy.' The withdrawal of YHWH's 'right hand' — his power and protective presence — from Israel is the experience of divine abandonment under covenant curse. Christ on the cross cries exactly this: 'My God, my God, why have you forsaken me?' (Matt 27:46 = Ps 22:1). The Son of God experiences the ultimate withdrawal of the divine right hand — the abandonment that Israel feared and experienced — so that those who are in Christ can hear: 'I will never leave you nor forsake you' (Heb 13:5).</p>",
    "4": "<p>A shadow: 'He bent his bow like an enemy; he stood firm as an adversary and cut down all who were pleasing to the eye.' YHWH acting as Israel's enemy is the most disturbing of Lamentations' images of divine judgment. At the cross this reaches its ultimate form: God made Christ 'to be sin who knew no sin' (2 Cor 5:21), treating the sinless Son as if he were the guilty party. God stood 'as an adversary' against his own Son so that he would not need to stand as adversary against those who shelter in the Son. The bow bent like an enemy is discharged at the cross so it is not discharged at us.</p>",
    "5": "<p>A type: 'The Lord has acted like an enemy; he has swallowed up Israel, swallowed all her palaces.' YHWH as enemy against his own people is the typological shadow of the cross, where the Father 'did not spare his own Son' (Rom 8:32) — directing against the Son the judgment that was ours to face. Christ stands where Israel stands in Lamentations: under the divine wrath as covenant people who have taken on the guilt of others. The difference is the direction of guilt: Israel bore her own; Christ bore ours. Resurrection is the proof that the Father's 'enmity' was temporary and redemptive, not the final word.</p>",
    "6": "<p>A type: 'He broke down his tabernacle like a garden shelter and ruined his assembly place. The LORD made the appointed feast and Sabbath to be forgotten in Zion.' The destroyed tabernacle/assembly place is the type Jesus claims in John 2:19-21: 'Destroy this temple, and in three days I will raise it up.' Jesus's body is the true tabernacle (John 1:14: <em>eskēnōsen</em>, 'tabernacled') whose destruction and resurrection is the definitive fulfillment of what Lamentations mourns. The feasts and Sabbaths forgotten in Zion are fulfilled and surpassed in Christ: Passover fulfilled in his sacrifice, Sabbath rest fulfilled in his person (Matt 11:28-29; Heb 4:9-10).</p>",
    "7": "<p>A type: 'The Lord rejected his altar and disowned his sanctuary.' The abandoned altar points to the supersession of the sacrificial system by Christ's once-for-all offering. The old altar — site of the Levitical sacrifices that covered sin temporarily — is 'rejected' (its shadow function ended) so the true altar, the cross, can be revealed. 'He has no need, like those high priests, to offer sacrifices daily... He did this once for all when he offered up himself' (Heb 7:27). The temple's rejection in Lamentations is the occasion for revealing that the system it housed always pointed beyond itself.</p>",
    "8": "<p>A revelation of God: 'The LORD planned the destruction of Zion's wall. He stretched out the measuring line and would not pull his hand back from destroying.' The measured, deliberate nature of divine judgment — YHWH planning and executing Zion's destruction methodically — is the theological background for Acts 2:23: Christ 'delivered up according to the definite plan and foreknowledge of God.' The cross was not a historical accident or a failure of divine protection but the most planned event in history, as deliberately executed as YHWH's judgment on Jerusalem. Both are the outworking of divine sovereignty over history for redemptive purposes.</p>",
    "9": "<p>A shadow: 'Her gates have sunk into the ground; he shattered and broke their bars. Her king and princes are among the nations; the instruction is no more.' The king exiled among the nations is the shadow of Christ crucified among the Gentiles (executed by Roman, not Jewish, law) and then exalted among the nations as their Lord. The Psalms anticipate this: 'I will give the nations as your heritage, and the ends of the earth as your possession' (Ps 2:8). The king driven into exile becomes the king to whom every knee bows 'in heaven and on earth and under the earth' (Phil 2:10).</p>",
    "10": "<p>A theme: 'The elders of Zion's daughter sit on the ground in silence. They have thrown dust on their heads and put on sackcloth.' The profound silence and grief of Zion's leadership = the silence of the disciples on Holy Saturday — between cross and resurrection, between desolation and hope. The community sits in silence 'not knowing' what has happened or what comes next. The resurrection breaks the silence and restores the community to speech and mission (Acts 2:4; Matt 28:19-20).</p>",
    "11": "<p>A type: 'My eyes are spent with weeping; my insides churn; my bile spills on the ground over the destruction of my people.' The prophet's visceral weeping over Jerusalem = Christ weeping over Jerusalem: 'When he drew near and saw the city, he wept over it, saying, &ldquo;Would that you, even you, had known on this day the things that make for peace!&rdquo;' (Luke 19:41-42). Jesus is the prophet-mourner who enters into Lamentations' grief in person. He weeps the tears that Lamentations writes; his tears are the human embodiment of the divine grief that the book expresses.</p>",
    "12": "<p>A shadow: 'They cry to their mothers, &ldquo;Where is grain and wine?&rdquo; as they collapse like the mortally wounded in the streets of the city, as their life is poured out on their mothers' bosoms.' The children's cry for bread in the streets of the starved city = the condition of those without Christ, the bread of life. 'Your fathers ate the manna in the wilderness, and they died. This is the bread that comes down from heaven, so that one may eat of it and not die' (John 6:49-50). Christ comes to feed where Jerusalem's famine left children dying; he is the grain and wine they cry for.</p>",
    "13": "<p>A shadow: 'What can I say to you? To what can I compare you, daughter of Jerusalem? Your ruin is as vast as the sea; who can heal you?' The incomparability of Zion's suffering — too great to describe, too vast to heal by human means — points to the incomparability of the answer. Paul says, 'God shows his love for us in that while we were still sinners, Christ died for us' (Rom 5:8). The healing that is 'too vast' for human diagnosis and medicine is accomplished by the one for whom no wound is too great: 'by his wounds we are healed' (Isa 53:5; 1 Pet 2:24).</p>",
    "14": "<p>A type: 'Your prophets gave you empty and deceptive visions. They did not expose your sin to restore you.' The false prophets who failed Zion — who comforted with lies rather than confronting sin — are the contrast that makes Christ the true prophet plain. Jesus is the prophet who tells the truth precisely to restore: 'you will know the truth, and the truth will set you free' (John 8:32). He exposes sin not to condemn but to heal (John 3:17). The false prophets' failure — they neither exposed sin nor restored the people — is the foil that shows what a true prophet must do, and what Christ does.</p>",
    "15": "<p>A direct anticipation: 'All who pass by clap their hands at you; they hiss and wag their heads at Jerusalem's daughter: &ldquo;Is this the city that was called the perfection of beauty, the joy of all the earth?&rdquo;' Matthew 27:39 fulfills this exactly: 'those who passed by derided him, wagging their heads.' The passers-by at Zion's ruins and the passers-by at Golgotha are placed in direct correspondence. But the irony is reversed: what looks like the cross being called 'is this what was called beautiful?' is actually the moment when true beauty — the self-giving love of God — is revealed. 'For the joy that was set before him he endured the cross' (Heb 12:2).</p>",
    "16": "<p>A type: 'All your enemies open wide their mouths against you; they hiss and gnash their teeth. They say, &ldquo;We have swallowed her up!&rdquo;' The gloating enemies who claim to have 'swallowed up' Jerusalem find their claim undone by resurrection. Paul applies the same language: 'Death is swallowed up in victory. O death, where is your victory? O death, where is your sting?' (1 Cor 15:54-55). The enemies who swallow — death, Babylon, Rome — are themselves swallowed up by the resurrection. What Lamentations describes as completed defeat becomes, in the light of Easter, the moment before the reversal.</p>",
    "17": "<p>A revelation of God: 'The LORD has done what he planned; he fulfilled the word he decreed in days of old. He overthrew without pity.' YHWH's sovereign execution of his plan in Jerusalem's destruction is the OT form of Acts 2:23: Christ 'delivered up according to the definite plan and foreknowledge of God.' In both cases, historical catastrophe is not the failure of divine sovereignty but its execution. The cross is not God caught off guard but God acting 'in the fullness of time' (Gal 4:4) exactly as planned 'before the foundation of the world' (1 Pet 1:20; Rev 13:8). Lamentations teaches us to read catastrophe through the lens of divine purpose; the NT applies this hermeneutic to the cross.</p>",
    "18": "<p>A shadow: 'Their heart cried out to the Lord. O wall of Zion's daughter, let tears flow like a river day and night. Give yourself no rest, let your eyes have no relief.' The call to unceasing prayer before YHWH in the midst of catastrophe = the posture Christ inhabits in Gethsemane: 'He offered up prayers and supplications, with loud cries and tears, to him who was able to save him from death, and he was heard because of his reverence' (Heb 5:7). Christ prays with the tears Lamentations calls for; he is the suffering intercessor whose prayer is answered not by being spared suffering but by being raised through it.</p>",
    "19": "<p>A type: 'Arise, cry out in the night! At the start of the night watches pour out your heart like water before the Lord. Lift your hands to him for the lives of your children.' The priestly intercession called for here — pouring out the heart, lifting hands, praying for the children — is what Christ does as the eternal high priest: 'He always lives to make intercession for them' (Heb 7:25). He 'poured out his soul to death' (Isa 53:12) and lifts his pierced hands in eternal intercession. The night-watches prayer of Lamentations is the OT picture of the unceasing intercession that Christ now offers from the right hand of the Father.</p>",
    "20": "<p>A shadow: 'Look, O LORD, and take heed! To whom have you done this? Should women eat the fruit of their own wombs, the children they have cradled?' The extreme horror of the siege — mothers eating their own children — shocks the very conscience of creation; it is the kind of suffering that demands a commensurate divine response. The resurrection is that response: when human suffering has reached its absolute nadir (the Son of God crucified; 'cursed is everyone who is hanged on a tree,' Gal 3:13), God's answer is not continued silence but resurrection and new creation. The horror of Lamentations 2:20 cries for exactly the kind of answer that only a resurrection can give.</p>",
    "21": "<p>A type: 'Young and old lie on the ground in the streets. You have slain them in the day of your anger; you have slaughtered without pity.' YHWH 'slaughtering without pity' his own people is the most severe language in Lamentations for divine wrath. The NT equivalent: 'He who did not spare his own Son but gave him up for us all' (Rom 8:32) — the same absence of sparing that fell on Jerusalem fell on Christ. He was 'slaughtered' (Rev 5:6: 'a Lamb standing, as though it had been slain') under divine wrath so that the same wrath would not fall on those who are in him. The young and old slain in the streets of Jerusalem are the shadow of the 'one man' who died for the many (John 11:50; Rom 5:15).</p>",
    "22": "<p>A type: 'You called my terrors from every side as though summoning people to a feast day.' The ironic inversion — a day of terror called as if it were a feast — is reversed at the cross: what looks like terror (crucifixion) is actually the greatest feast-provision in history. 'Christ, our Passover lamb, has been sacrificed. Let us therefore celebrate the festival' (1 Cor 5:7-8). The Lord's Supper is the feast that comes from the terror of the cross; the new Passover is instituted at the moment of greatest apparent defeat. Lamentations' ironic 'feast-of-terror' is the shadow of the real reversal where the terror of Good Friday becomes the feast of Easter.</p>"
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
