"""
MKT Echo — 1 Kings chapter 22
Run: python3 scripts/zc-echo-1kings-22-22.py

Ch22: Micaiah's prophecy; the heavenly court; the lying spirit; Ahab's death by random arrow (53 verses)

Note: the interlinear does not extend to 1 Kings 22; echo entries use standard verse numbers.
Echo type is selective — entries are written for theologically significant verses only.

Key echo types:
- The heavenly court scene (22:19-22) → Dan 7:9-10; Rev 4:2; Isa 6:1
- The lying/deceptive spirit permitted by YHWH (22:22-23) → 2 Thess 2:11; John 8:44
- Zedekiah strikes Micaiah (22:24) → John 18:22 (Jesus struck at trial); Acts 23:2-3
- Imprisoning the true prophet until the king &#8220;returns safely&#8221; (22:27) → Rev 2:10; Matt 10:17-22
- Micaiah&#8217;s confidence in his prophetic word (22:28) → Deut 18:22; Jer 28:9
- Ahab disguised but the random arrow finds him (22:29-35) → Heb 4:13; Prov 21:30
- Dogs lick Ahab&#8217;s blood fulfilling Elijah&#8217;s word (22:38) → Isa 55:11; 1 Kgs 21:19
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

KINGS1_ECHO = {
  "22": {
    "19": [
      {"type": "allusion", "target": "Isa 6:1", "note": "Micaiah&#8217;s vision: &#8216;I saw YHWH sitting on his throne, and all the host of heaven standing on his right and on his left.&#8217; The heavenly throne-room vision is the defining prophetic experience of the OT: Isaiah&#8217;s vision of YHWH high and lifted up with the seraphim (Isa 6:1-3), Ezekiel&#8217;s chariot-throne (Ezek 1), Daniel&#8217;s Ancient of Days (Dan 7:9-10). Micaiah&#8217;s vision is a council scene rather than an inaugural vision — he sees the divine court deliberating about Ahab. The heavenly council (<em>sôd</em>) of YHWH with his host is the source of true prophetic knowledge (Jer 23:18,22: &#8216;who has stood in the council of YHWH?&#8217;). The council fulfills in the NT heavenly court of Rev 4-5 where the Lion-Lamb opens the sealed scroll of history."},
      {"type": "allusion", "target": "Rev 4:2", "note": "The vision of YHWH enthroned in Micaiah&#8217;s heavenly court is the OT type of John&#8217;s throne-room vision in Rev 4: &#8216;a throne stood in heaven, with one seated on the throne.&#8217; In both visions the heavenly host surrounds the throne and participates in the execution of divine purposes in history. The deliberation of the heavenly court in Micaiah&#8217;s vision (vv. 20-22) and the opening of the seals in Revelation (6:1ff.) are structurally the same: the throne-room determines what happens on earth, and the prophet is admitted to see the decision before it is enacted."}
    ],
    "22": [
      {"type": "allusion", "target": "John 8:44", "note": "YHWH asks who will entice Ahab; a spirit volunteers to be a lying spirit in the mouths of his prophets. The lying spirit that serves YHWH&#8217;s judicial purposes is the OT type of the devil as &#8216;a liar and the father of lies&#8217; (John 8:44). Christ&#8217;s identification of the devil as the original liar places the lying spirit of 1 Kgs 22 in a wider theological framework: the power that deceives is real, but it operates within YHWH&#8217;s sovereign permission and serves his ultimate purposes. The lying spirit that leads Ahab to his death is not an autonomous anti-god but a creature operating under divine governance."},
      {"type": "allusion", "target": "2 Thess 2:11", "note": "YHWH permits the lying spirit to go into Ahab&#8217;s prophets: &#8216;Go out and do so.&#8217; Paul&#8217;s description of the eschatological strong delusion: &#8216;God sends them a strong delusion, so that they may believe what is false, in order that all may be condemned who did not believe the truth but had pleasure in unrighteousness&#8217; (2 Thess 2:11-12). The divine permission of deception for those who have already chosen to reject the truth is the same theological principle in both passages: Ahab has already decided what answer he wants (v.8) before the prophets are consulted; the lying spirit confirms the deception he chose. The hardening principle — YHWH confirming the choice of those who refuse the true word — runs from Pharaoh (Exod 4:21) through Ahab to the eschatological strong delusion."}
    ],
    "23": [
      {"type": "allusion", "target": "Ezek 14:9", "note": "&#8216;YHWH has put a lying spirit in the mouth of all these your prophets; YHWH has declared disaster for you.&#8217; The divine use of false prophecy as judicial instrument is addressed by Ezekiel: &#8216;if the prophet is deceived and speaks a word, I YHWH have deceived that prophet&#8217; (Ezek 14:9) — YHWH&#8217;s &#8220;deception&#8221; of the false prophet is the confirmation of his own chosen falsehood. Micaiah&#8217;s announcement reveals the mechanism behind the lying prophets&#8217; confident unanimity: they speak what their audience wants to hear, and YHWH has given them up to this. The 450 prophets of Ahab are the type of the false teachers who &#8216;accumulate for themselves teachers to suit their own passions&#8217; (2 Tim 4:3)."}
    ],
    "24": [
      {"type": "allusion", "target": "John 18:22", "note": "Zedekiah son of Chenaanah struck Micaiah on the cheek: &#8216;Which way did the Spirit of YHWH pass from me to speak to you?&#8217; The physical assault on the lone true prophet by the representative of the false religious establishment is the type fulfilled in the passion narrative: &#8216;when Jesus had said this, one of the officers standing by struck him with his hand&#8217; (John 18:22) — the officer who struck Jesus in the high priest&#8217;s hall is acting out the Zedekiah pattern. Both assaults are accompanied by a challenge to the prophet&#8217;s authority. Paul received the same treatment before the Sanhedrin (Acts 23:2-3: struck on Ananias&#8217;s command). The lone prophetic witness before an institutional tribunal who speaks the truth and is physically assaulted for it is a recurring OT-to-NT pattern."},
      {"type": "allusion", "target": "Jer 20:2", "note": "Zedekiah&#8217;s physical assault on Micaiah for his true prophecy is the type of Pashhur the priest striking Jeremiah and putting him in stocks (Jer 20:2) — the pattern of violent suppression of the true prophetic word by the official religious establishment. The prophet who speaks YHWH&#8217;s inconvenient truth faces physical violence from those whose interests he threatens. This pattern reaches its fulfillment in the passion narrative where the true prophet is not merely struck but crucified. John the Baptist, Jesus, Stephen, Paul — each receives this assault in escalating intensity."}
    ],
    "27": [
      {"type": "allusion", "target": "Rev 2:10", "note": "&#8216;Put this man in prison and feed him nothing but bread and water until I return safely.&#8217; The imprisonment of the true prophet by the king who wants his word silenced is the type of the persecution the church faces for prophetic faithfulness. &#8216;Do not fear what you are about to suffer. Behold, the devil is about to throw some of you into prison, that you may be tested, and for ten days you will have tribulation. Be faithful unto death, and I will give you the crown of life&#8217; (Rev 2:10). Ahab&#8217;s &#8220;until I return safely&#8221; is the tyrant&#8217;s confidence that the true prophet&#8217;s word will be disproved; Micaiah&#8217;s counter-word shows the confidence is misplaced."},
      {"type": "allusion", "target": "Matt 10:19", "note": "The imprisoned prophet before the king is the type of the disciples hauled before governors and kings for Christ&#8217;s sake: &#8216;When they deliver you over, do not be anxious how you are to speak or what you are to say, for what you are to say will be given to you in that hour&#8217; (Matt 10:19). Micaiah&#8217;s confidence before Ahab — speaking YHWH&#8217;s word without modification despite the threat of imprisonment — is the model of the Spirit-empowered witness that Jesus promises his disciples. The prophet imprisoned for the truth does not recant; the disciples beaten for the name &#8216;went on their way rejoicing&#8217; (Acts 5:41)."}
    ],
    "28": [
      {"type": "allusion", "target": "Deut 18:22", "note": "Micaiah&#8217;s parting word: &#8216;If you ever return safely, YHWH has not spoken through me.&#8217; The true prophet staking his entire prophetic credibility on the fulfillment of his word is the application of the Deuteronomic criterion for true prophecy: &#8216;if a prophet speaks in the name of YHWH and the word does not come to pass or come true, that is a word that YHWH has not spoken&#8217; (Deut 18:22). Micaiah invites the test: Ahab&#8217;s return would falsify his prophecy; his death would confirm it. The confidence of the true prophet in the reliability of YHWH&#8217;s word is the type of Christ&#8217;s own certitude: &#8216;until heaven and earth pass away, not an iota, not a dot, will pass from the Law until all is accomplished&#8217; (Matt 5:18)."},
      {"type": "allusion", "target": "Jer 28:9", "note": "Micaiah&#8217;s staking of his credibility on the fulfillment of his word against Ahab reflects the prophetic principle Jeremiah articulates: &#8216;as for the prophet who prophesies peace, when the word of that prophet comes to pass, then it will be known that YHWH has truly sent the prophet&#8217; (Jer 28:9). The self-subjection of the true prophet to the verification-criterion of fulfillment — &#8216;if I am wrong, YHWH has not spoken through me&#8217; — is the mark of genuine prophetic confidence in YHWH&#8217;s reliability. The 400 prophets of Ahab never stake their credibility this way; only Micaiah does."}
    ],
    "34": [
      {"type": "allusion", "target": "Heb 4:13", "note": "&#8216;A certain man drew his bow at random and struck the king of Israel between the scale armor and the breastplate.&#8217; The random arrow that finds the one gap in Ahab&#8217;s disguised armor is the dramatic illustration of the inescapability of YHWH&#8217;s decreed judgment. Ahab&#8217;s elaborate disguise — concealing his royal identity from the Arameans who had orders to kill him specifically — could not evade YHWH&#8217;s appointed end. Heb 4:13: &#8216;nothing in all creation is hidden from God&#8217;s sight; everything is uncovered and laid bare before the eyes of him to whom we must give account.&#8217; No disguise avails before YHWH; no human precaution defeats the divine decree."},
      {"type": "allusion", "target": "Prov 21:30", "note": "The random arrow that defeats every human precaution Ahab took is the narrative embodiment of the wisdom principle: &#8216;there is no wisdom, no insight, no plan that can succeed against YHWH&#8217; (Prov 21:30). Ahab&#8217;s plan was elaborate: ask for a favorable prophecy, silence the unfavorable prophet, disguise himself in battle, let the allied king wear royal robes as a decoy. Every element of the plan was rational. The arrow was random. YHWH&#8217;s judicial decree operates through what appears to be chance — &#8216;the lot is cast into the lap, but its every decision is from YHWH&#8217; (Prov 16:33)."}
    ],
    "38": [
      {"type": "allusion", "target": "Isa 55:11", "note": "The dogs licked Ahab&#8217;s blood at the pool in Samaria, fulfilling Elijah&#8217;s word (1 Kgs 21:19). The precise fulfillment of the prophetic word — even the detail that prostitutes washed in the same water — demonstrates what YHWH declares through Isaiah: &#8216;my word that goes out from my mouth shall not return to me empty, but it shall accomplish that which I purpose, and shall succeed in the thing for which I sent it&#8217; (Isa 55:11). The gap between the prophecy (ch21) and its fulfillment (ch22) — through Ahab&#8217;s disguise, the random arrow, the king propped up in his chariot until evening — does not diminish but intensifies the demonstration of prophetic reliability."},
      {"type": "allusion", "target": "1 Kgs 21:19", "note": "The fulfillment of Elijah&#8217;s specific word against Ahab closes the Ahab narrative with a cross-reference to its origin: &#8216;in the place where dogs licked up Naboth&#8217;s blood, dogs will lick up your blood — yes, yours!&#8217; (1 Kgs 21:19). The blood of the one who murdered Naboth is licked by dogs in Samaria (though with a modification — the pool in Samaria rather than Jezreel, since partial fulfillment occurred in Ahab&#8217;s lifetime; the full Jezreel fulfillment comes with Joram in 2 Kgs 9:26). The covenant pattern of sin generating its appointed consequence — in the same element (blood licked by dogs), in the same political space (Samaria) — demonstrates that YHWH&#8217;s judgment is not merely punitive but precisely calibrated to covenant violation."}
    ]
  }
}

def main():
    e = load_echo('1kings')
    merge_echo(e, KINGS1_ECHO)
    save_echo('1kings', e)
    count = len(KINGS1_ECHO.get('22', {}))
    print(f'1kings echo ch22: wrote entries for {count} verses')

if __name__ == '__main__':
    main()
