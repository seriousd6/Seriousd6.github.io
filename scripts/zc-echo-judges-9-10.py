import json, pathlib

ROOT = pathlib.Path(__file__).parent.parent

def load_echo(book):
    p = ROOT / 'data' / 'echoes' / f'{book}.json'
    if p.exists():
        return json.loads(p.read_text())
    return {}

def save_echo(book, data):
    p = ROOT / 'data' / 'echoes' / f'{book}.json'
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

JUDGES_ECHOES = {
    "9": {
        "2": [
            {
                "type": "allusion",
                "target": "Matt 26:15",
                "note": "Abimelech is hired for seventy pieces of silver from the temple of Baal-berith (Judg 9:4) to kill his seventy brothers. The silver-for-death motif echoes at the betrayal of Christ: Judas receives thirty pieces of silver to betray Jesus (Matt 26:15). Both are blood-money transactions — silver paid to accomplish the murder of the rightful heir(s) and install a false ruler."
            }
        ],
        "4": [
            {
                "type": "allusion",
                "target": "Acts 1:18",
                "note": "The 'seventy pieces of silver' paid from the temple treasury to fund Abimelech's fratricide prefigures the 'thirty pieces of silver' Judas received from the chief priests and subsequently flung back into the temple (Matt 27:5). Both involve sacred treasury money used to purchase the death of the rightful leader. Both end in the judgment of the betrayer."
            }
        ],
        "5": [
            {
                "type": "allusion",
                "target": "Matt 2:16",
                "note": "Abimelech killed seventy brothers 'on one stone' to secure his kingship. Herod's massacre of the Bethlehem infants (Matt 2:16) follows the same anti-messianic logic: the false king eliminates all rival claimants through mass killing. In both cases, the only survivor is the one who escapes the slaughter — Jotham at Shechem, Jesus in Egypt. The one survivor becomes the voice of divine judgment against the false king."
            }
        ],
        "7": [
            {
                "type": "type",
                "target": "Luke 19:41",
                "note": "Jotham's proclamation from Mount Gerizim — the mountain of blessing — over Shechem types every prophetic cry of judgment over a city that has rejected the true king. As Jesus wept over Jerusalem ('If you had known on this day what would bring you peace... now it is hidden from your eyes,' Luke 19:41-44), Jotham weeps over Shechem's fatal choice of Abimelech. Both are prophetic laments pronounced from a height over a city that chose the false king over YHWH's anointed."
            }
        ],
        "8": [
            {
                "type": "type",
                "target": "John 15:1",
                "note": "Jotham's parable of the trees seeking a king (vv.8-15) is the OT's most sustained political parable. The olive tree refuses kingship because it produces oil that honors God and man (v.9); the fig tree refuses because it produces good fruit (v.11); the vine refuses because it produces wine that cheers God and man (v.13). The three productive trees are types of true service — the calling to bear fruit rather than rule. Jesus as the true vine (John 15:1) is the anti-Abimelech: the one who chooses to bear fruit and give life rather than grasp kingship, even when offered it (John 6:15)."
            }
        ],
        "11": [
            {
                "type": "allusion",
                "target": "Luke 13:19",
                "note": "The fig tree's refusal — 'Shall I leave my sweetness and my good fruit and go hold sway over the trees?' (v.11) — contrasts with the thornbush's eager acceptance. The productive fig provides nourishment and shade; the thornbush provides only thorns and fire. Christ's parable of the mustard seed (Luke 13:18-19) inverts Jotham's parable: where Jotham shows trees refusing to shelter, the mustard seed grows into a tree where birds nest — the true King who genuinely shelters. The kingdom of God is not the thornbush-kingdom Jotham warned about but the sheltering-tree-kingdom Jesus announces."
            }
        ],
        "13": [
            {
                "type": "allusion",
                "target": "John 15:1",
                "note": "The vine's refusal — 'Shall I leave my wine that cheers God and men and go hold sway over the trees?' — is an anti-type of Christ the true vine (John 15:1). The vine of Jotham's parable refuses false kingship to remain in its calling of joy-giving. Christ the true vine gives not mere wine but himself: 'I am the vine; you are the branches. Whoever abides in me and I in him, he it is that bears much fruit' (John 15:5). The vine that cheers God and man in Jotham's parable anticipates the vine that gives his blood for the life of the world."
            }
        ],
        "14": [
            {
                "type": "type",
                "target": "Matt 27:29",
                "note": "The bramble-king's acceptance speech — 'Come and take refuge in my shadow; but if not, let fire come out of the bramble and devour the cedars of Lebanon' (v.15) — is the definitive OT portrait of the false king. The bramble (thornbush) offers shade it cannot provide and threatens destruction it will bring on itself. The crown of thorns placed on Jesus's head (Matt 27:29) inverts Jotham's bramble-king: Jesus, the true King, takes the thornbush's identity on himself — crowned with thorns, he absorbs the curse the false king represented (Gal 3:13: 'cursed is everyone who is hanged on a tree')."
            }
        ],
        "15": [
            {
                "type": "allusion",
                "target": "Gal 3:13",
                "note": "The thornbush-king's threat of fire that comes from the bramble and devours the cedars (v.15) types the curse of the law that destroys even the greatest through its condemnation. Paul's 'Christ redeemed us from the curse of the law by becoming a curse for us — for it is written, \"Cursed is everyone who is hanged on a tree\"' (Gal 3:13) shows Christ taking the thornbush curse on himself. The bramble's fire was a curse on the trees; the cross's curse was absorbed by Christ, extinguishing the fire before it could devour the inheritance."
            }
        ],
        "16": [
            {
                "type": "allusion",
                "target": "Luke 23:28",
                "note": "Jotham's pronouncement of judgment on Shechem for choosing Abimelech — 'if in good faith you made Abimelech king... then rejoice in Abimelech and let him also rejoice in you' (v.19-20) — is the conditional curse that plays out in the chapter. Jesus pronounces a parallel judgment on Jerusalem on the way to the cross: 'Daughters of Jerusalem, do not weep for me, but weep for yourselves and for your children' (Luke 23:28). Both are prophetic pronouncements of deserved judgment on a city that chose the wrong king."
            }
        ],
        "20": [
            {
                "type": "allusion",
                "target": "Rev 17:16",
                "note": "The mutual destruction Jotham predicted — fire from Abimelech devouring the citizens of Shechem, and fire from the citizens of Shechem devouring Abimelech — is fulfilled in vv.45-49,57. This self-destructive dynamic of evil devouring evil echoes Revelation's portrayal of the beast turning against the harlot city: 'The ten horns that you saw, they and the beast will hate the prostitute and make her desolate and naked, and devour her flesh and burn her up with fire' (Rev 17:16). The bramble-king and the city that chose him destroy each other — as every false messianic system ultimately self-destructs."
            }
        ],
        "23": [
            {
                "type": "allusion",
                "target": "2 Thess 2:11",
                "note": "YHWH sent an evil spirit between Abimelech and the men of Shechem (v.23) as divine judicial hardening — the consequences of their sin returned upon them through divine orchestration. Paul's 'God sends them a strong delusion, so that they may believe what is false, in order that all may be condemned who did not believe the truth but had pleasure in unrighteousness' (2 Thess 2:11) operates on the same logic: YHWH allows and directs the destructive consequences of choosing false authority. The judicial abandonment to self-chosen delusion is YHWH's judgment, not mere fate."
            }
        ],
        "45": [
            {
                "type": "allusion",
                "target": "Luke 19:44",
                "note": "Abimelech razed Shechem and sowed it with salt (v.45) — the ancient curse of total destruction. Jesus's judgment on Jerusalem anticipates the same total destruction: 'They will not leave one stone upon another in you, because you did not know the time of your visitation' (Luke 19:44). The city that chose the false king (Abimelech/the Zealot leaders) and rejected the true king (YHWH/Jesus) faced the same salted-ruins judgment. Abimelech's sowing salt prefigures the Roman plowing of Jerusalem after 70 CE."
            }
        ],
        "53": [
            {
                "type": "type",
                "target": "Gen 3:15",
                "note": "A woman threw an upper millstone on Abimelech's head and crushed his skull (v.53). The woman who crushes the head of the false king is an inversion of the Gen 3:15 promise — not the seed of the woman crushing the serpent's head, but a woman crushing the head of the false king. This anticipates Jael's killing of Sisera (Judg 4-5) in the same pattern: YHWH's victory over the enemy accomplished through an unexpected woman. Both point forward to the ultimate crushing — Christ crushing the serpent's head (Gen 3:15; Rom 16:20) — and both hint that the victory will come through unexpected human agency."
            }
        ],
        "54": [
            {
                "type": "allusion",
                "target": "Matt 21:44",
                "note": "Abimelech, felled by a millstone, asks his armor-bearer to kill him 'lest they say about me, \"A woman killed him\"' (v.54). The millstone of judgment is a recurring image in the NT: 'Whoever causes one of these little ones who believe in me to sin, it would be better for him to have a great millstone fastened around his neck and to be drowned in the depth of the sea' (Matt 18:6). Jesus's warning about the stone of judgment also echoes Abimelech's fall: 'The one who falls on this stone will be broken to pieces; and when it falls on anyone, it will crush him' (Matt 21:44). The crushing millstone of Judges 9 is an image of divine judgment on those who seize power against YHWH's anointed."
            }
        ],
        "57": [
            {
                "type": "allusion",
                "target": "Gal 6:7",
                "note": "'God also made all the evil of the men of Shechem return on their heads, and on them came the curse of Jotham the son of Jerubbaal' (v.57). The return of evil on the heads of evildoers is the lex talionis at the cosmic level — 'Do not be deceived: God is not mocked, for whatever one sows, that will he also reap' (Gal 6:7). The Shechem-Abimelech mutual destruction is the OT's clearest example of this principle: those who choose the bramble-king reap the bramble's thorns and fire. The same principle operates in the cross-event: the powers that killed Jesus had their own violence returned on them through his resurrection (Col 2:15)."
            }
        ],
    },
    "10": {
        "1": [
            {
                "type": "allusion",
                "target": "Heb 11:32",
                "note": "Tola the son of Puah saved Israel and judged it for twenty-three years. Hebrews 11:32 includes 'judges' in its roll call of faith, though the text does not name each individual judge. Tola's quiet faithfulness — a single verse summary of two decades of service — types the unrecorded faithful of every generation. The hall of faith includes many unnamed Tolas alongside the Samsons and Gideons: those whose faithful governance bore fruit not spectacular enough for narrative expansion but real enough for the divine record."
            }
        ],
        "3": [
            {
                "type": "allusion",
                "target": "Luke 15:11",
                "note": "Jair the Gileadite judged Israel for twenty-two years and had thirty sons who rode on thirty donkeys and had thirty cities — a picture of settled prosperity in the land. The thirty-son inheritance types the multiplication of the covenant family: as YHWH promised Abraham descendants as numerous as the stars, the proliferation of Jair's sons riding on donkeys (the mount of royalty, Gen 49:11; Zech 9:9) hints at the royal family's expansion. The thirty donkeys echo the thirty pieces of silver that betray the true king — the same number framing abundance and loss."
            }
        ],
        "6": [
            {
                "type": "allusion",
                "target": "Luke 15:13",
                "note": "Israel again did evil, serving the Baals and Ashtaroth and the gods of the surrounding nations — the most extended list of apostasy in Judges (Syria, Sidon, Moab, Ammon, Philistines). The cycle of forgetting YHWH after deliverance and returning to the gods of the surrounding cultures is the Judges-spiral that anticipates the prodigal son's leaving his father's house for a far country: 'He squandered his property in reckless living' (Luke 15:13). Israel's going after seven foreign deities is the collective prodigal departure — trading the Father's house for the gods of the surrounding nations."
            }
        ],
        "10": [
            {
                "type": "allusion",
                "target": "Luke 15:21",
                "note": "Israel's cry — 'We have sinned against you, because we have forsaken our God and have served the Baals' (v.10) — is the OT template for the prodigal son's confession: 'Father, I have sinned against heaven and before you. I am no longer worthy to be called your son' (Luke 15:21). Both confessions follow a period of spiritual departure followed by oppression. The Hebrew prayer structure — sin acknowledged, cause identified, mercy sought — is the same pattern Jesus builds into the model prayer: 'Forgive us our debts' (Matt 6:12)."
            }
        ],
        "14": [
            {
                "type": "allusion",
                "target": "Ps 22:1",
                "note": "YHWH's remarkable answer to Israel's cry — 'Go and cry out to the gods whom you have chosen; let them save you in the time of your distress' (v.14) — is the divine ultimatum before relenting. The temporary withdrawal of YHWH's saving response mirrors the cross-cry: 'My God, my God, why have you forsaken me?' (Ps 22:1; Matt 27:46). As YHWH told Israel 'I will save you no more' before ultimately relenting (v.16), the Father's turning away at the cross was the deepest expression of the pattern — the only time the ultimatum was fully actualized, born by the Son in Israel's place, so that the Father could relent toward his people permanently."
            }
        ],
        "15": [
            {
                "type": "allusion",
                "target": "Luke 15:18",
                "note": "Israel's responsive confession — 'We have sinned; do to us whatever seems good to you. Only please deliver us this day' (v.15) — moves from formal acknowledgment (v.10) to complete surrender to divine judgment. 'Do to us whatever seems good to you' is the prodigal son's resolution: 'I will arise and go to my father... I am no longer worthy to be called your son. Treat me as one of your hired servants' (Luke 15:18-19). Both confessions reach the same place of abandoning all claims and casting themselves on the Father's judgment. This is repentance reaching its fullest form: not bargaining with YHWH but submitting to whatever he decides."
            }
        ],
        "16": [
            {
                "type": "type",
                "target": "John 11:35",
                "note": "Israel put away the foreign gods and served YHWH, and 'he could bear Israel's misery no longer' (v.16, lit. 'his soul was shortened/grieved over the toil of Israel'). This is one of the OT's most anthropopathic descriptions of YHWH — the divine grief over human suffering that precedes divine action. Jesus weeping at Lazarus's tomb (John 11:35 — the shortest verse in the NT) is the incarnation of this Judges 10:16 pattern: the divine distress over human suffering made visibly present in the tears of the Son. YHWH who 'could not bear to see Israel's misery' became human specifically in order to weep at the tomb."
            }
        ],
        "17": [
            {
                "type": "allusion",
                "target": "Heb 11:32",
                "note": "The Ammonites assembled against Israel at Gilead, and Israel gathered at Mizpah — the military crisis that sets the stage for Jephthah's rise in ch11. The pattern of oppression following apostasy following deliverance is the Judges rhythm that Heb 11:32 summarizes in a phrase ('Jephthah'). The gathering at Mizpah (the watchtower) in distress types the church's gathering in moments of crisis: the community that scatters under prosperity reassembles at the watchtower under threat. The 'who will begin the fight?' question (v.18) anticipates Jephthah's unexpected answer."
            }
        ],
        "18": [
            {
                "type": "allusion",
                "target": "John 1:46",
                "note": "The leaders of Gilead ask 'Who is the man who will begin to fight against the Ammonites? He shall be head over all the inhabitants of Gilead' — an offer of leadership to the one willing to fight. The leader Israel needs is unexpected: the illegitimate Jephthah (11:1), the son of a prostitute rejected by his brothers. This anticipates the pattern of Christ's origin: 'Can anything good come out of Nazareth?' (John 1:46). The question 'who will lead us?' has an answer that surprises everyone — the rejected son becomes the deliverer and head."
            }
        ],
    },
}

def main():
    existing = load_echo('judges')
    merge_echo(existing, JUDGES_ECHOES)
    save_echo('judges', existing)
    count_9 = len(existing.get('9', {}))
    count_10 = len(existing.get('10', {}))
    print(f'ch9: {count_9} verses with echoes; ch10: {count_10} verses with echoes')
    print('Judges 9-10 echo written.')

if __name__ == '__main__':
    main()
