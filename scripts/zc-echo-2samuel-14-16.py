"""
MKT Echo — 2 Samuel chapters 14–16
Run: python3 scripts/zc-echo-2samuel-14-16.py

Ch14: Wise woman of Tekoa; Absalom's return; estranged from David (33 verses)
Ch15: Absalom's conspiracy; David's flight; crossing the Kidron; Mount of Olives (37 verses)
Ch16: Ziba; Shimei's cursing; Hushai's deception; Ahithophel's counsel (23 verses)

Key echo types:
- "God devises ways so the banished may not remain banished" (14:14) → 2 Cor 5:19 (reconciliation)
- The angel of God metaphor (14:17,20) → Mal 3:1; Heb 1:4
- Absalom stealing hearts at the gate → the anti-messiah usurping allegiance
- David crossing the Kidron (15:23) → John 18:1 (Jesus crosses the Kidron to Gethsemane)
- David ascending Mount of Olives weeping (15:30) → Luke 19:37-41 (Jesus weeps over Jerusalem)
- David's submission to YHWH's will (15:25-26) → Luke 22:42 (Gethsemane)
- Ahithophel: David's trusted counselor who betrays him → John 13:18 (Judas; Ps 41:9)
- Shimei cursing the fleeing king (16:5-13) → 1 Pet 2:23 (Christ did not retaliate)
- David: "Perhaps YHWH will see my suffering" (16:12) → Heb 5:7; 12:2
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

SAMUEL2_ECHO = {
  "14": {
    "14": [
      {"type": "allusion", "target": "2 Cor 5:19", "note": "The wise woman declares: 'We must all die; we are like water poured out on the ground that cannot be gathered back. But God devises ways so that a banished person may not remain banished' — this is one of the OT's most theologically precise statements of divine reconciliation; 'God does not take away life, but devises ways so the banished person may not remain banished from him.' Paul's summary of the gospel: 'God was reconciling the world to himself in Christ, not counting people's sins against them' (2 Cor 5:19) — the divine contrivance of a way for the banished to return is the pattern that the incarnation and atonement fulfill."},
      {"type": "allusion", "target": "Luke 15:20", "note": "The woman's argument to David — that God devises means for the banished not to remain banished — is the theological ground of the father's running to receive the prodigal son (Luke 15:20: 'while he was still a long way off, his father saw him and was filled with compassion; he ran to his son'). The father who does not wait for the son to complete the journey of return but runs to meet him is YHWH 'devising means' — actively working to ensure the exile does not remain exiled. The Tekoa woman's insight becomes the Lukan parable's plot."}
    ],
    "17": [
      {"type": "allusion", "target": "Mal 3:1", "note": "The woman compares David to 'the angel of God' who 'knows all things that are on earth' — a statement of the king's near-divine discernment. The messianic promise 'the Lord whom you seek will suddenly come to his temple, and the angel of the covenant whom you delight in' (Mal 3:1) applies the same 'angel of God' identification to the coming Messiah. The comparison of YHWH's anointed to the divine messenger/angel anticipates the NT identification of Christ as YHWH's ultimate messenger-representative."}
    ],
    "20": [
      {"type": "allusion", "target": "Col 2:3", "note": "Joab's flattery — 'my lord is as wise as the wisdom of the angel of God, to know all that happens on earth' — identifies the ideal king with transcendent wisdom that encompasses all earthly knowledge. Paul attributes this wisdom to Christ: 'in whom are hidden all the treasures of wisdom and knowledge' (Col 2:3). The royal wisdom ideal — knowing all that happens, discerning between good and evil — finds its only adequate fulfillment in the Son in whom the fullness of deity dwells bodily."}
    ]
  },
  "15": {
    "2": [
      {"type": "allusion", "target": "John 10:10", "note": "Absalom stations himself at the gate, intercepts those seeking the king's justice, and steals their hearts by promising better justice under himself — a systematic campaign to redirect covenant loyalty from the true king to himself. The thief who 'comes only to steal and kill and destroy' (John 10:10) describes the pattern of the one who comes to usurp the shepherd's role and divert the sheep's loyalty. Absalom's gate-campaign is the OT pattern of the false shepherd who undermines the true king's covenant relationship with his people."}
    ],
    "6": [
      {"type": "allusion", "target": "Rev 13:14", "note": "Absalom 'stole the hearts of the men of Israel' through systematic deception — personal flattery combined with false promises of justice. The false messiah deceives 'those who dwell on earth' through signs and wonders (Rev 13:14). Both Absalom and the Antichrist achieve apparent legitimacy through deception rather than covenant right: neither is the true king, both claim kingship by manipulating the loyalty of those who belong to another. The pattern of stolen allegiance redirected from the true anointed to the pretender runs from Absalom to the eschatological counterfeit."}
    ],
    "23": [
      {"type": "allusion", "target": "John 18:1", "note": "David and all the people crossed the Wadi Kidron (nahal qidron) and went up toward the wilderness — the legitimate king departing Jerusalem in humiliation, crossing the Kidron valley. Jesus crossed the same Kidron valley with his disciples on the night of his betrayal: 'When he had finished praying, Jesus left with his disciples and crossed the Kidron Valley' (John 18:1). Both crossings occur at night, both are moments of the anointed king's vulnerability before his enemies, and in both cases the crossing initiates the final confrontation with those who seek to overthrow him."},
      {"type": "allusion", "target": "Heb 13:12", "note": "David's crossing of the Kidron to go 'outside the city' in rejection by his own people is the typological pattern of Christ suffering 'outside the gate': 'Jesus also suffered outside the gate in order to sanctify the people through his own blood... let us go to him outside the camp and bear the reproach he endured' (Heb 13:12-13). The rejected king departing through weeping crowds, crossing the valley, going into the wilderness — the king rejected by those he came to rule — is fulfilled in Christ's passion."}
    ],
    "25": [
      {"type": "allusion", "target": "John 6:40", "note": "David sends the ark back to the city: 'If I find favor in YHWH's eyes, he will bring me back and let me see it and his dwelling.' David's conditional hope — 'if I find favor' — expresses his dependence on YHWH's will for his restoration. Christ's assurance to his disciples is the unconditional fulfillment of this conditional hope: 'everyone who looks to the Son and believes in him shall have eternal life, and I will raise them up at the last day' (John 6:40). What David hoped might happen, Christ guarantees will happen."}
    ],
    "26": [
      {"type": "allusion", "target": "Luke 22:42", "note": "David: 'But if he says, \"I take no pleasure in you\" — then here I am. Let him do with me whatever seems good to him.' The total submission of the anointed king to YHWH's sovereign will — even if that will is rejection and death — is the OT pattern fulfilled in Gethsemane: 'Father, if you are willing, take this cup from me; yet not my will, but yours be done' (Luke 22:42). Both David and Jesus arrive at the same absolute surrender: whatever YHWH determines is accepted without reservation. David's surrender is conditional on YHWH's judgment; Christ's is the voluntary self-giving of the Son to the Father's redemptive purpose."}
    ],
    "30": [
      {"type": "allusion", "target": "Luke 19:41", "note": "David went up the ascent of the Mount of Olives, weeping as he went, his head covered and his feet bare — the rejected king ascending the mountain in grief, barefoot in mourning. Jesus descended the Mount of Olives in the triumphal entry and wept over Jerusalem (Luke 19:41-44: 'As he approached Jerusalem and saw the city, he wept over it'). Both David and Jesus weep at the same mountain over the rejection and coming destruction of Jerusalem; in both cases the king's tears are for the city that refused him. The barefoot, covered-head mourning of David is the low-point of his reign; Christ's tears at the Mount of Olives are the announcement of Jerusalem's coming desolation."},
      {"type": "allusion", "target": "Acts 1:12", "note": "The Mount of Olives is the site of both David's ascent in flight from Absalom and Christ's ascension from earth to the Father: 'they returned to Jerusalem from the hill called the Mount of Olives' (Acts 1:12). The mountain that witnesses David's humiliation and departure from Jerusalem witnesses Christ's exaltation and departure to heaven. The same geography: the anointed king leaving Jerusalem via the Mount of Olives — once in flight, once in glory. The Ascension redeems the geography of David's exile."}
    ],
    "31": [
      {"type": "allusion", "target": "John 17:15", "note": "David prays against Ahithophel's counsel: 'O YHWH, please turn Ahithophel's counsel into foolishness.' David's prayer against the influence of the counselor who has joined the conspiracy against him echoes Christ's high priestly prayer: 'My prayer is not that you take them out of the world but that you protect them from the evil one' (John 17:15). Both prayers ask YHWH to defeat the counsel of the adversary — Ahithophel (whose counsel, if followed, would have killed David) and the evil one (whose counsel, if followed, would destroy the disciples). Prayer is the anointed's weapon against strategic adversarial counsel."}
    ],
    "34": [
      {"type": "allusion", "target": "John 13:18", "note": "Ahithophel — David's trusted counselor who defected to Absalom — is the type that Psalm 41:9 identifies and that Jesus applies to Judas: 'He who ate my bread has lifted his heel against me. I am telling you this now, before it takes place, that when it does take place you may believe that I am he' (John 13:18-19). The intimate counselor who ate at the king's table and then betrayed him is the pattern; Hushai's counterintelligence against Ahithophel's betrayal mirrors the Holy Spirit's role in preserving the church from the adversary's strategic counsel."}
    ]
  },
  "16": {
    "7": [
      {"type": "allusion", "target": "Matt 27:39", "note": "Shimei curses the fleeing king: 'Get out! Get out! You man of blood! You worthless wretch!' — the public cursing of the rejected anointed king by one of his own people as he passes by in humiliation. The mockers at the cross: 'Those who passed by hurled insults at him, shaking their heads and saying... &#8220;Come down from the cross, if you are the Son of God!&#8221;&#8217; (Matt 27:39-40). Both scenarios: the anointed in his hour of greatest humiliation, passing by while opponents shout abuse. In both cases the king does not retaliate."}
    ],
    "10": [
      {"type": "allusion", "target": "1 Pet 2:23", "note": "David's response to Shimei's cursing: 'If the LORD has told him to curse David, who can ask why he does so?' — David's acceptance of the cursing as YHWH's sovereign permission rather than retaliating against the curser. Peter applies this pattern directly to Christ: 'When they hurled their insults at him, he did not retaliate; when he suffered, he made no threats. Instead, he entrusted himself to him who judges justly' (1 Pet 2:23). David's refusal to silence Shimei is the OT model of non-retaliation that Christ perfectly embodies at the cross: entrusting the outcome to YHWH's judgment rather than self-defense."}
    ],
    "12": [
      {"type": "allusion", "target": "Heb 5:7", "note": "David: 'Perhaps YHWH will see my affliction and repay me with good for the cursing I receive today.' The suffering king hoping that YHWH will see his distress and respond in covenant faithfulness is the OT prayer-pattern that Heb 5:7 applies to Christ: 'In the days of his flesh, Jesus offered up prayers and supplications, with loud crying and tears, to him who was able to save him from death, and he was heard because of his reverent submission.' Both the afflicted David and the crucified Christ appeal to YHWH's covenant faithfulness as the only ground of hope in extremity."},
      {"type": "allusion", "target": "Rom 12:21", "note": "David's hope that YHWH will turn the cursing into good ('repay me with good for the cursing I receive') is the OT ground for Paul's ethic: 'Do not be overcome by evil, but overcome evil with good' (Rom 12:21). The pattern running from David through Christ to the church: the response to unjust suffering is neither retaliation nor passive resignation but active entrusting to YHWH who can transform affliction into covenant blessing. The cursing received without retaliation becomes, in YHWH's redemptive economy, the occasion of future blessing."}
    ],
    "21": [
      {"type": "allusion", "target": "2 Sam 12:11", "note": "Ahithophel counsels Absalom to go in to David's concubines publicly — the fulfillment of Nathan's prophecy: 'I will take your wives and give them to one who is close to you, and he will sleep with your wives in broad daylight' (2 Sam 12:11). The public desecration of the abandoned royal household is the covenant judgment on David's hidden sin — YHWH's word through Nathan is being precisely fulfilled. Prophetic announcement (12:11) to historical execution (16:21-22): the same pattern as the prophetic announcement of Christ's betrayal (Ps 41:9; Zech 11:12) and its precise fulfillment (John 13:18-19; Matt 26:15)."},
      {"type": "allusion", "target": "Matt 10:26", "note": "What David did in secret (2 Sam 11-12) is now publicly exposed through Absalom's action on the rooftop — Nathan's 'you did it secretly, but I will do this before all Israel and before the sun' (12:12) is fulfilled. Jesus: 'There is nothing hidden that will not be disclosed, and nothing concealed that will not be known or brought out into the open' (Luke 12:2; Matt 10:26). The covenant principle that hidden sin will be brought to light is executed in David's story and proclaimed by Christ as the universal principle governing all human action."}
    ],
    "23": [
      {"type": "allusion", "target": "Isa 9:6", "note": "Ahithophel's counsel was valued 'as if one had sought the oracle of God' (<em>kidbar ha-elohim</em>) — the human counselor treated as a divine oracle. The messianic title 'Wonderful Counselor' (Isa 9:6, <em>yoeitz pele</em>) designates the coming king as the one whose counsel truly is divine — the one in whom all the treasures of wisdom are hidden (Col 2:3). Ahithophel represents the pretension to divine counsel; the Wonderful Counselor of Isaiah fulfills what Ahithophel only approximated. The false divine counselor who serves the usurper is the anti-type of the true divine Counselor who serves the Father's redemptive purpose."}
    ]
  }
}

def main():
    e = load_echo('2samuel')
    merge_echo(e, SAMUEL2_ECHO)
    save_echo('2samuel', e)
    count = sum(len(v) for v in SAMUEL2_ECHO.values())
    print(f'2samuel echo: wrote {count} chapters (14-16)')

if __name__ == '__main__':
    main()
