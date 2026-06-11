"""
Echo Commentary — Ezekiel 21–22
Run: python3 scripts/zc-echo-ezekiel-21-22-fill.py

Key echo nodes:
- 21:6  the sighing prophet → Isa 53:3; Mark 7:34; John 11:33
- 21:9  sword sharpened → Heb 4:12; Rev 1:16; Rev 19:15
- 21:17 YHWH satisfies his fury → Rom 3:25 (propitiation)
- 21:27 "until he comes to whom it belongs" → Gen 49:10 (direct allusion); Luke 1:32; Rev 11:15
- 22:2  verdict on the city of bloodshed → Matt 27:25; Luke 11:49-51
- 22:18-22 dross in furnace → Mal 3:2-3; 1 Cor 3:13; 1 Pet 1:7
- 22:28 whitewashing prophets → Matt 23:27
- 22:30 no one to stand in the breach → Heb 7:25; Ps 106:23 (Moses type → Christ antitype)
- 22:31 wrath poured out → 1 John 2:2; Rom 5:9
"""

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
    """Merge echo entries; deduplicate by (type, target) within each verse."""
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

EZEKIEL_ECHOES = {
"21": {
    "6": [
        {"type": "allusion", "target": "Isa 53:3",  "note": "Ezekiel is commanded to sigh openly, with bitterness and a broken heart, as a visible enactment of the grief to come. The man of sorrows in Isaiah 53:3 — 'acquainted with grief' — is the deepest fulfillment of this prophetic embodiment of anguish; what Ezekiel performs as sign-act, Christ inhabits as identity."},
        {"type": "allusion", "target": "Mark 7:34", "note": "Jesus sighs deeply (ἐστέναξεν) before healing the deaf-mute — the same involuntary groaning under the weight of a broken world that Ezekiel is commanded to display. John 11:33 and 38 show Jesus 'deeply moved in spirit' and troubled before Lazarus's tomb — the incarnate God carrying the grief Ezekiel was asked only to enact."}
    ],
    "9": [
        {"type": "allusion", "target": "Heb 4:12", "note": "The sword described as 'sharpened and polished' to flash like lightning is the OT register that Hebrews draws on: 'the word of God is alive and active, sharper than any double-edged sword.' The divine word that comes as judgment-sword in Ezekiel becomes in Hebrews the word that judges the thoughts and attitudes of the heart."},
        {"type": "allusion", "target": "Rev 1:16",  "note": "The risen Christ has a sharp double-edged sword coming from his mouth (Rev 1:16; 2:12; 19:15) — the same sword-as-divine-word that Ezekiel's polished-for-lightning blade anticipates. Christ wields the sword not against Israel but against the enemies of the redeemed, and it is his spoken word, not a material weapon."}
    ],
    "17": [
        {"type": "allusion", "target": "Rom 3:25", "note": "YHWH says 'I will clap my hands together and satisfy my fury' — the divine wrath brought to its completion. Paul's argument in Romans 3:25-26 that God 'presented Christ as a propitiation (ἱλαστήριον)... to demonstrate his justice' is the NT answer to this passage: the fury is satisfied not by annihilating Israel but by Christ absorbing the blow. The 'satisfaction' of YHWH's wrath in Ezekiel 21:17 is christologically enacted at the cross."}
    ],
    "25": [
        {"type": "allusion", "target": "Luke 1:32", "note": "The 'profaned and wicked prince of Israel whose day has come, the time when iniquity reaches its end' — the Davidic dynasty at its lowest point — sets the stage for the reversal of 21:26-27. The angel's promise to Mary in Luke 1:32 that 'the Lord God will give him the throne of his father David' is the restoration of what the profaned prince forfeited: the throne stripped and awaiting its rightful claimant."}
    ],
    "27": [
        {"type": "fulfillment", "target": "Gen 49:10", "note": "The triple 'I will overturn, overturn, overturn — and it will be no more until he comes to whom it belongs (עַד-בֹּא אֲשֶׁר-לוֹ הַמִּשְׁפָּט)' directly echoes Genesis 49:10 — the scepter will not depart from Judah 'until he comes to whom it belongs' (עַד כִּי-יָבֹא שִׁילֹה). Ezekiel's formula is the prophetic reiteration of Jacob's dying oracle: the crown is removed and held in suspension until the Davidic Messiah whose right it is claims it."},
        {"type": "allusion",    "target": "Rev 11:15", "note": "Revelation 11:15 is the fulfillment of Ezek 21:27's suspended throne: 'the kingdom of the world has become the kingdom of our Lord and of his Messiah, and he will reign for ever and ever.' The crown overturned and removed in Ezekiel's oracle is given to the one to whom judgment belongs — the Christ of Revelation who receives the kingdoms."}
    ]
},
"22": {
    "2": [
        {"type": "allusion", "target": "Matt 27:25", "note": "Ezekiel is commanded to pronounce verdict on 'the city of bloodshed' — the charge of innocent blood. Matthew 27:25 shows the Jerusalem crowd accepting responsibility with 'let his blood be on us and on our children' — they identify themselves as the city of bloodshed Ezekiel diagnosed, and the blood they invoke is Christ's."},
        {"type": "allusion", "target": "Luke 11:50", "note": "Jesus's pronouncement that 'this generation will be held responsible for the blood of all the prophets that has been shed since the creation of the world' applies Ezekiel's city-of-bloodshed verdict (22:2-4) directly to his contemporaries. The accumulation of shed prophetic blood that Ezekiel charges to Jerusalem reaches its culminating indictment in Luke 11:49-51."}
    ],
    "7": [
        {"type": "allusion", "target": "Matt 25:43", "note": "Jerusalem's specific failures — dishonoring parents, oppressing the resident foreigner, wronging the orphan and widow (22:7) — are the exact categories Jesus uses in the sheep-and-goats judgment: 'I was a stranger and you did not invite me in.' Ezekiel's social-justice indictment of the city is the OT template that Christ applies to final judgment."},
        {"type": "allusion", "target": "Jas 1:27",  "note": "James's definition of pure religion — 'to care for orphans and widows in their distress' — is the positive formulation of Ezekiel's negative indictment: Jerusalem failed to do precisely what James says is the mark of authentic faith. Both texts make the care of the vulnerable the litmus test of genuine covenant relationship."}
    ],
    "12": [
        {"type": "allusion", "target": "Matt 26:15", "note": "Jerusalem's acceptance of bribes to shed blood (22:12) finds its sharpest NT parallel in the thirty pieces of silver Judas receives for betraying Jesus — the price negotiated for innocent blood (Matt 26:14-16; 27:4). The city charged with bribe-for-blood in Ezekiel enacts that charge at the precise moment it pays for the Son of God's death."}
    ],
    "18": [
        {"type": "allusion", "target": "Mal 3:2",  "note": "Ezekiel's furnace image — Israel as dross that YHWH will gather and smelt — is taken up in Malachi 3:2-3: 'who can stand when he appears? For he is like a refiner's fire... he will sit as a refiner and purifier of silver.' What Ezekiel presents as judgment (the furnace consuming dross) Malachi transforms into sanctification — the same fire, but now refining those who are Christ's."},
        {"type": "allusion", "target": "1 Cor 3:13", "note": "Paul's 'the fire will test the quality of each person's work' draws on this furnace tradition: both Ezekiel and Paul describe a divine fire that reveals what is dross and what is genuine. The eschatological refining in 1 Corinthians 3:13-15 is the NT form of the furnace Ezekiel describes — judgment that destroys what is worthless but saves what is real."},
        {"type": "allusion", "target": "1 Pet 1:7",  "note": "Peter's 'your faith — of greater worth than gold, which perishes even though refined by fire — may be proved genuine' transforms Ezekiel's dross-furnace into the positive refining image: believers are not the dross that burns away but the gold that emerges purified. Christ's own suffering is the furnace that both judges sin and refines faith."}
    ],
    "26": [
        {"type": "allusion", "target": "Heb 7:26", "note": "Ezekiel charges Jerusalem's priests with making no distinction between holy and common, failing to teach the difference between clean and unclean, and profaning the sabbaths. Hebrews 7:26 describes Christ as 'holy, blameless, pure, set apart from sinners, exalted above the heavens' — the high priest who upholds every distinction the Jerusalem priests violated. He is the anti-type of the boundary-erasing priests Ezekiel indicts."},
        {"type": "allusion", "target": "Matt 23:23", "note": "Jesus's 'woe' to teachers who neglect the weightier matters of the law — justice, mercy, faithfulness — while fastidiously tithing spices is the NT form of Ezekiel's indictment against priests who distinguish between the minor and ignore the major. Both texts charge religious leaders with inverted priorities that nullify the law's purpose."}
    ],
    "28": [
        {"type": "allusion", "target": "Matt 23:27", "note": "Ezekiel's prophets 'whitewash' (טָח תָּפֵל) the city's deeds with flimsy plaster — the same image Jesus uses for the scribes and Pharisees as 'whitewashed tombs... full of dead men's bones.' Ezekiel 13:10-12 and 22:28 together supply the whitewash-over-rotten-foundation image that Jesus concentrates into his 'woe' against the religious establishment."}
    ],
    "30": [
        {"type": "type",    "target": "Ps 106:23", "note": "Moses is the OT type of the intercessor who stands in the breach: Psalm 106:23 — 'he would have destroyed them had not Moses, his chosen one, stood in the breach before him to keep his wrath from destroying them.' Ezekiel 22:30's search for an intercessor and its failure ('I found no one') establishes the insufficiency of every human candidate for the role Moses prefigured."},
        {"type": "fulfillment", "target": "Heb 7:25", "note": "The failed search of Ezek 22:30 — YHWH finding no one to stand in the breach — is fulfilled in Christ: Hebrews 7:25 — 'he always lives to intercede for them.' Christ is the intercessor the divine search could not find among human candidates; his intercession is not temporary (Moses's prayer ended) but perpetual, grounded in his resurrection life and priestly office."},
        {"type": "allusion",    "target": "Isa 59:16", "note": "Isaiah 59:16 parallels Ezekiel's failed search: 'he saw that there was no one, he was appalled that there was no one to intervene; so his own arm achieved salvation for him, and his own righteousness sustained him.' The divine arm that achieves salvation when no human intercessor is found is the arm of YHWH that Isaiah 53:1 asks 'to whom has it been revealed?' — ultimately Christ himself."}
    ],
    "31": [
        {"type": "allusion", "target": "1 John 2:2", "note": "YHWH pours out his indignation and consumes them with the fire of his wrath (22:31). John identifies Christ as the propitiation (ἱλασμός) for sin — 1 John 2:2 — not only for our sins but also for the whole world. The wrath that falls on Jerusalem in Ezekiel's oracle is the same wrath that falls on Christ at Calvary; those in him are no longer the objects of the consuming fire."},
        {"type": "allusion", "target": "Rom 5:9",   "note": "'I have repaid them for their conduct' — the divine recompense poured out as wrath. Paul's 'since we have been justified by his blood, how much more shall we be saved from God's wrath through him' (Rom 5:9) is the answer to Ezekiel 22:31: the wrath repaid on the basis of conduct is now repaid on the basis of Christ's blood for those who are in him."}
    ]
}
}

def main():
    existing = load_echo('ezekiel')
    merge_echo(existing, EZEKIEL_ECHOES)
    save_echo('ezekiel', existing)
    print('Ezekiel 21-22 echoes written.')

if __name__ == '__main__':
    main()
