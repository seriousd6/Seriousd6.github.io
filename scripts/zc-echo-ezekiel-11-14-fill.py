"""
Echo Commentary — Ezekiel chapters 11–14 (fill script; ch 11 already complete)
Run: python3 scripts/zc-echo-ezekiel-11-14-fill.py

Key echo nodes:
- 12:2 "eyes but do not see, ears but do not hear" → Isa 6:9-10; Mark 4:12; Matt 13:14-15 (Jesus quotes this)
- 12:11 "I am your sign" → Luke 11:29-30; John 2:18-22
- 12:14 "scatter to every wind" → Zech 13:7; Matt 26:31 (strike shepherd, sheep scatter)
- 12:22-25 vision-delay proverb answered → 2 Pet 3:3-4; Matt 24:35
- 13:10-14 "peace when there is no peace; whitewashed wall falls" → Eph 2:14; Matt 23:27; Matt 7:26-27
- 13:17-22 prophetesses who trap souls → Rev 2:20; Matt 7:15-23
- 14:6 "repent and turn from idols" → Acts 3:19; 1 Thess 1:9
- 14:14/20 Noah, Daniel, Job deliver only themselves → Rom 5:17-19 (Christ's righteousness covers many)
- 14:22 remnant brought out → Isa 10:20-21; Rom 9:27
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
"12": {
    "2": [
        {"type": "fulfillment", "target": "Mark 4:12", "note": "Jesus quotes the eyes-that-see-not / ears-that-hear-not tradition (Isa 6:9-10) to explain why parables both reveal and conceal; Ezek 12:2's 'rebellious house with eyes that do not see' is the same diagnosis of covenant blindness that Jesus applies to his generation."},
        {"type": "allusion",    "target": "Matt 13:14", "note": "Matthew's formula 'in them is fulfilled the prophecy of Isaiah' cites the same blindness-tradition; Ezekiel's sign-act ministry in Babylon parallels Jesus's parabolic ministry in Israel — both address communities whose ears have closed."}
    ],
    "11": [
        {"type": "allusion", "target": "Luke 11:29", "note": "Ezekiel declares 'I am your sign' — the prophet's body enacting the coming exile. Jesus says 'no sign will be given except the sign of Jonah'; both prophets are themselves the sign, not merely sign-bearers. The pattern of the prophet-as-embodied-sign runs from Ezekiel through Jonah to the sign of Christ's death and resurrection."},
        {"type": "allusion", "target": "John 2:19", "note": "When pressed for a sign, Jesus points to the destruction and rebuilding of the temple — his own body. The sign-act prophet of Ezek 12:11 ('as I have done, so shall it be done to them') prefigures the sign Jesus gives: enacted judgment absorbed by his own body."}
    ],
    "14": [
        {"type": "fulfillment", "target": "Matt 26:31", "note": "YHWH scatters Zedekiah's troops to every wind; Jesus quotes Zech 13:7 at Gethsemane — 'strike the shepherd and the sheep will be scattered' — and all the disciples desert him (Mark 14:50). The divine scattering of Ezek 12:14 finds its NT application in the passion-night abandonment of the Shepherd."}
    ],
    "16": [
        {"type": "theme", "target": "Rom 9:27", "note": "YHWH spares a small number so they may confess their abominations among the nations — the preserved remnant becomes a witness. Isaiah's remnant-theology (Isa 10:22) and Paul's argument in Romans 9 that 'a remnant will be saved' both draw on this pattern: judgment refines rather than annihilates, leaving a witness-bearing remnant."}
    ],
    "22": [
        {"type": "allusion", "target": "2 Pet 3:3", "note": "The proverb 'the days drag on and every vision comes to nothing' is the exact skepticism Peter warns about — 'scoffers who say: where is this coming he promised?' Both Ezekiel and Peter face audiences that use apparent delay to dismiss prophetic truth; both insist the word will not be delayed indefinitely."}
    ],
    "25": [
        {"type": "allusion", "target": "Matt 24:35", "note": "YHWH declares 'I will speak, and what I speak will happen — it will not be delayed any further.' Jesus echoes this with the same absolute divine authority: 'heaven and earth will pass away, but my words will never pass away.' Both assert the unbreakable reliability of the divine word against a generation inclined toward delay-skepticism."}
    ],
    "28": [
        {"type": "allusion", "target": "Rev 22:20", "note": "'None of my words will be delayed any longer' is the divine urgency behind Revelation's repeated 'I am coming soon.' The prophetic word that the exiles tried to postpone indefinitely arrives with Christ's imminent return — the same urgency Ezekiel asserts against the 'distant future' dismissal."}
    ]
},
"13": {
    "3": [
        {"type": "allusion", "target": "Matt 7:15", "note": "Ezekiel's 'foolish prophets who follow their own spirit and have seen nothing' is the OT counterpart to Jesus's warning against false prophets in sheep's clothing. Both describe the same structural failure: prophetic authority claimed without divine commission, producing ruin for those who trust them."}
    ],
    "9": [
        {"type": "allusion", "target": "Matt 7:23", "note": "The false prophets will not be 'in the council of my people' or enrolled in the register of Israel — the divine exclusion. Jesus's 'I never knew you; depart from me, you evildoers' is the NT form of the same exclusion from the divine assembly that belongs to those who prophesy without being sent."}
    ],
    "10": [
        {"type": "allusion", "target": "Eph 2:14", "note": "The false prophets say 'peace' when there is no peace — the comfortable lie vs. the true peace. Paul identifies Christ himself as 'our peace' who broke down the dividing wall; the shalom Christ makes (Eph 2:14-17; Col 1:20 — 'making peace through his blood') is the costly opposite of the false prophets' costless 'peace, peace.'"},
        {"type": "allusion", "target": "Matt 23:27", "note": "The whitewashed wall that conceals rotten foundations directly parallels Jesus's 'whitewashed tombs' — beautiful on the outside but full of dead bones inside. Ezekiel's image of the collapsing whitewashed wall is the architectual form of the same diagnosis Jesus applies to the scribes and Pharisees."}
    ],
    "11": [
        {"type": "allusion", "target": "Matt 7:27", "note": "The flooding rain, hailstones, and stormy wind that tear down the whitewashed wall are the exact elements of Jesus's parable of the house built on sand: 'the rain came down, the streams rose, and the winds blew and beat against that house, and it fell with a great crash.' Both texts use the storm as the divine test of foundations."}
    ],
    "17": [
        {"type": "allusion", "target": "Rev 2:20", "note": "The prophetesses of Ezek 13:17-22 who lead people astray with magic bands and veils, hunting souls like birds, anticipate the Jezebel-figure in Thyatira (Rev 2:20) who 'calls herself a prophet and by her teaching misleads my servants.' The female false prophet who traps and kills is a recurring biblical type that the letter to Thyatira addresses directly."}
    ],
    "19": [
        {"type": "allusion", "target": "Acts 3:14", "note": "The false prophets kill those who should not die and preserve those who should not live — the inversion of just judgment. Peter's accusation that the crowd 'killed the author of life' (Acts 3:14-15) applies this same inversion to the crucifixion: the one who had done nothing deserving death was killed while a murderer (Barabbas) was released."}
    ],
    "22": [
        {"type": "allusion", "target": "Isa 42:3", "note": "The false prophets 'discourage the righteous' — making the true believer faint. Isaiah 42:3, applied to Jesus in Matt 12:20 — 'a bruised reed he will not break and a smoldering wick he will not snuff out' — describes Christ's ministry as the exact opposite of the discouraging false prophet: he strengthens the faint, not weakens them."}
    ]
},
"14": {
    "3": [
        {"type": "allusion", "target": "Col 3:5", "note": "The idols set up 'in their hearts' are the interior idolatry that Ezekiel uniquely diagnoses — not merely physical idols but heart-devotion. Paul's 'greed, which is idolatry' (Col 3:5) and his call to 'put to death' the inner idolatrous desires is the direct NT development of Ezekiel's heart-idol diagnosis."},
        {"type": "allusion", "target": "1 Cor 8:9", "note": "The 'stumbling block of iniquity before their faces' anticipates Paul's concern about the stumbling block of idolatrous food (1 Cor 8:9 — 'be careful that this liberty does not become a stumbling block to the weak'). The Ezekielian heart-idol and the Pauline stumbling block occupy the same theological space: the internal attachment that trips the believer."}
    ],
    "6": [
        {"type": "fulfillment", "target": "Acts 3:19", "note": "YHWH's call 'repent and turn away from your idols; turn your faces from all your abominations' is the template for the apostolic repentance-call. Peter's Pentecost sermon and Solomon's portico sermon (Acts 3:19 — 'repent and turn to God') both use the <em>shûb</em>-from-idols structure of Ezek 14:6."},
        {"type": "allusion",    "target": "1 Thess 1:9", "note": "Paul's summary of the Thessalonians' conversion — 'you turned to God from idols to serve the living and true God' — uses the exact Ezekielian structure: turning from idols to YHWH. The missionary proclamation that produces this turning is the fulfillment of the divine call Ezekiel articulates."}
    ],
    "9": [
        {"type": "theme", "target": "Rom 1:24", "note": "The mysterious verse that YHWH 'deceives' the deceived prophet and then judges him points toward the divine hardening theology: God gives the persistently self-deceiving over to their deception (Rom 1:24 — 'God gave them over'; 2 Thess 2:11 — 'God sends a powerful delusion'). Ezek 14:9 establishes that divine hardening/deception is not arbitrary but judicial — it follows persistent idol-hearted pursuit of false prophets."}
    ],
    "11": [
        {"type": "allusion", "target": "John 10:28", "note": "The goal of YHWH's judgment and restoration is 'that the house of Israel may no longer wander away from me' — the permanent non-wandering of the redeemed people. Jesus's promise 'no one will snatch them out of my hand; they shall never perish' (John 10:28) is the fulfillment of this purpose: the good shepherd ensures the definitive non-wandering that Ezek 14:11 anticipates."}
    ],
    "14": [
        {"type": "allusion", "target": "Rom 5:19", "note": "Even Noah, Daniel, and Job — the three supreme OT examples of righteousness that delivers — could save only themselves, not others. Paul's argument in Romans 5:17-19 is the positive fulfillment: 'through the obedience of the one man the many will be made righteous.' What the three righteous men of Ezek 14:14 could not accomplish (deliver others by their righteousness), Christ accomplishes by being the one whose righteousness constitutively covers many."},
        {"type": "theme",    "target": "Heb 7:25", "note": "The limitation of Noah, Daniel, and Job — their righteousness cannot transfer to their children — highlights the unique nature of Christ's intercession: 'he always lives to intercede for them' (Heb 7:25). Where the three greatest OT saints have no intercessory reach beyond their own lives, Christ's priestly intercession is perpetual and effective for all who come to God through him."}
    ],
    "20": [
        {"type": "allusion", "target": "Isa 53:11", "note": "Noah, Daniel, and Job would deliver neither son nor daughter — individual righteousness is not transferable. Isaiah 53:11's Servant 'will justify many by his knowledge' through his vicarious suffering — the one whose righteousness *is* transferable because it is substitutionary, not merely exemplary. Ezek 14:20's limitation of personal righteousness is the negative shadow of the Servant's positively transferable righteousness."}
    ],
    "22": [
        {"type": "allusion", "target": "Rom 9:27", "note": "A remnant will be brought out from Jerusalem, coming to the exiles in Babylon — the surviving remnant whose presence vindicates YHWH's justice. Isaiah's remnant theology ('only a remnant will return') quoted by Paul in Romans 9:27 is the sustained interpretation of this Ezekielian remnant: the preserved few vindicate God's ways and serve as the nucleus of the restored people."},
        {"type": "theme",    "target": "Rev 15:3", "note": "The remnant's presence 'comforts' the exiles and validates YHWH's justice ('you will know that I have not acted without cause') — the final theodicy. Revelation 15:3-4 places the same vindication-of-divine-justice at the conclusion of judgment: 'just and true are your ways, King of the nations.' Both texts affirm that the divine judgments, fully carried out, vindicate YHWH/Christ rather than indicting him."}
    ],
    "23": [
        {"type": "theme", "target": "Rev 19:2", "note": "'You will know that I have not acted without cause in all that I have done to it' — the theodicy conclusion. Revelation 19:2 — 'true and just are his judgments; he has condemned the great prostitute' — is the same assertion at the end of history: the divine judgments are validated, not arbitrary. Ezekiel 14:23 and Revelation 19:2 are the bookends of the biblical theodicy: God's actions are always justified, not requiring the observer's approval."}
    ]
}
}

def main():
    existing = load_echo('ezekiel')
    merge_echo(existing, EZEKIEL_ECHOES)
    save_echo('ezekiel', existing)
    print('Ezekiel 11-14 echoes written.')

if __name__ == '__main__':
    main()
