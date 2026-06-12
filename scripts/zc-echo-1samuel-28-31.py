"""
Echo Layer — 1 Samuel chapters 28–31
Run: python3 scripts/zc-echo-1samuel-28-31.py

Key echoes:
- 28:6  divine silence toward Saul → contrast with Christ always heard (John 11:42; Heb 5:7)
- 28:13-14  necromantic séance → the occult parody of resurrection; Christ is the true
            one who returns from the dead (Luke 16:31; Rev 1:18)
- 28:17  kingdom torn from Saul and given to David → Matt 21:43 — kingdom given to a
         nation bearing its fruits; the failed anointed replaced by the true anointed
- 28:19  "Tomorrow you and your sons will be with me" → Luke 23:43 — Jesus to the thief
         (conceptual echo only — one is a death sentence, the other a promise of paradise)
- 29:6   Achish: "I find no wrong in you" → Pilate's triple acquittal (John 18:38;
         19:4, 6); the innocent anointed attested by hostile witness
- 30:6   "David strengthened himself in YHWH his God" → Ps 22; Heb 5:7-8 — the
         anointed in utter desolation drawing strength from the Father
- 30:8   "Pursue — you will certainly overtake and rescue" → John 6:39; 10:28 — the
         Father's will is that Christ lose nothing given to him
- 30:18-19  "David recovered everything — nothing was missing" → John 18:9; Matt 18:12-14;
            Acts 3:21 — the anointed recovers all; the lost sheep found; restoration of all things
- 30:24  equal sharing with those who stayed behind → Matt 20:1-16; Eph 1:11 — full
         inheritance for all, not proportional to performance
- 31:4   Saul's voluntary death rather than capture → John 10:18 — Christ laid down his
         life voluntarily (ironic contrast: Saul evades the enemy; Christ gives himself to it)
- 31:11-13  Jabesh-gilead retrieves and buries Saul → Luke 23:50-53 — the faithful who
            honor the body of the fallen king
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

SAMUEL1_ECHOES = {
  "28": {
    "6": [
      {"type": "shadow", "target": "John 11:41-42",
       "note": "The LORD did not answer Saul — not through dreams, nor through the Urim, nor through prophets. Divine silence is the unmistakable mark of covenant rupture; YHWH has withdrawn. The contrast with Christ is total: at Lazarus's tomb Jesus says 'Father, I thank you that you have heard me — I knew that you always hear me' (John 11:41-42), and the writer of Hebrews states that his prayer in Gethsemane was 'heard because of his reverent submission' (Heb 5:7). The anointed who is always heard replaces the anointed who is never heard."}
    ],
    "13": [
      {"type": "shadow", "target": "Luke 16:31",
       "note": "The woman at Endor performs what appears to be a resurrection — bringing up the dead Samuel. This occult séance is the forbidden parody of what Christ alone achieves: 'If they do not hear Moses and the Prophets, neither will they be convinced if someone should rise from the dead' (Luke 16:31). The Endor episode demonstrates the human craving for word from beyond death; Christ's resurrection satisfies that craving with the only genuine answer."},
      {"type": "shadow", "target": "Rev 1:17-18",
       "note": "A divine figure rises from the earth — even the terminology of Samuel's appearance ('elohim coming up') mimics the language of resurrection. Christ's actual self-declaration in Rev 1:17-18 stands as the definitive contrast: 'I am the first and the last, and the living one. I died, and behold I am alive forevermore, and I have the keys of Death and Hades.' The true one who comes back from death holds the keys; necromancy is a counterfeit with no access to those keys."}
    ],
    "17": [
      {"type": "allusion", "target": "Matt 21:43",
       "note": "Samuel declares: 'The LORD has torn the kingdom out of your hand and given it to your neighbor David.' The principle — the kingdom removed from the disobedient and given to those who bear its fruit — is applied by Christ to the religious leaders who rejected him: 'the kingdom of God will be taken away from you and given to a people producing its fruits' (Matt 21:43). Both are transfers of covenant stewardship from those who forfeited it through unfaithfulness to those chosen by grace."}
    ],
    "19": [
      {"type": "theme", "target": "Dan 5:26-28",
       "note": "Samuel's death-sentence — 'Tomorrow you and your sons will be with me' — is the precise, timed prophetic announcement of the end of a king's reign. The same pattern appears in Daniel's handwriting-on-the-wall: 'You have been weighed in the balances and found wanting; your kingdom is divided and given to the Medes and Persians.' The pattern of the divine verdict pronounced the night before the fall is the OT's recurring warning that covenant faithlessness has a measured limit."},
      {"type": "theme", "target": "Luke 23:43",
       "note": "The verbal form 'tomorrow you will be with me' has an ironic NT counterpart in Christ's promise to the thief: 'today you will be with me in paradise' (Luke 23:43). Samuel's word is a death-sentence; Christ's is a life-promise. One announces imminent death as punishment; the other announces immediate presence as grace. The same grammatical structure ('you will be with me this day') carries opposite freight depending on whose mouth it comes from."}
    ]
  },
  "29": {
    "6": [
      {"type": "allusion", "target": "John 18:38",
       "note": "Achish tells David: 'As the LORD lives, you have been trustworthy... I have found no wrong in you from the day of your coming to me' — a pagan king testifying to the innocence of YHWH's anointed, against the suspicions of his own commanders. Pilate's triple declaration — 'I find no guilt in him' (John 18:38; 19:4, 6) — follows the same structure: the governing authority outside the covenant community testifies to the innocence of the one the covenant community wants to destroy. Both are hostile-witness attestations that the anointed is blameless."}
    ],
    "9": [
      {"type": "allusion", "target": "Luke 23:47",
       "note": "Achish declares David 'as good in my sight as a messenger from God' (<em>malʾak ʾĕlōhîm</em>) — divine-messenger language applied to the blameless anointed by the enemy himself. The Roman centurion at the cross says 'Certainly this man was innocent' (Luke 23:47; Matt 27:54: 'Truly this was the Son of God'). In both cases the outsider — the Philistine king, the Roman officer — provides the most striking testimony to the anointed's true identity precisely because they have no theological stake in the claim."}
    ]
  },
  "30": {
    "6": [
      {"type": "allusion", "target": "Heb 5:7",
       "note": "David was in great distress — his men spoke of stoning him — and he 'strengthened himself in YHWH his God' (<em>yit-ḥazzēq bYHWH</em>). The anointed king in absolute desolation, abandoned even by his own followers, draws renewed strength by turning to YHWH alone. Heb 5:7 describes Christ in Gethsemane: 'he offered up prayers and supplications, with loud crying and tears, to him who was able to save him from death, and he was heard because of his reverent submission.' Both the type and the fulfillment show the anointed not collapsing under abandonment but strengthening himself through radical dependence on the Father."},
      {"type": "allusion", "target": "Ps 22:24",
       "note": "'He did not despise or disdain the suffering of the afflicted one; he has not hidden his face from him but has listened to his cry for help' (Ps 22:24) — the psalm of desolation that David authored ends in YHWH's vindication of the one who cried. David's Ziklag crisis is the biographical situation that informs the whole arc of Ps 22: the anointed in extremity who discovers that YHWH has not abandoned him. Christ cites Ps 22:1 from the cross (Matt 27:46), entering the full desolation of the type's experience."}
    ],
    "8": [
      {"type": "allusion", "target": "John 6:39",
       "note": "YHWH answers David: 'Pursue, for you will certainly overtake and certainly rescue.' The certainty of the divine promise — 'surely overtake, surely rescue' — governs the whole recovery narrative. Christ expresses the same certainty about all the Father gives him: 'This is the will of him who sent me, that I should lose nothing of all that he has given me, but raise it up on the last day' (John 6:39). The anointed king who recovers everything taken from his people is the type of the one who loses none of what the Father entrusted to him."}
    ],
    "18": [
      {"type": "allusion", "target": "Luke 15:4-6",
       "note": "David recovered everything the Amalekites had taken — both of his wives, all the captives young and old, all the plunder. Not one was missing. The complete recovery by the anointed king of everyone taken captive parallels the parable of the lost sheep: the shepherd leaves the ninety-nine and searches until he finds the one that was lost, then returns rejoicing (Luke 15:4-6). The recovery is total, not approximate."}
    ],
    "19": [
      {"type": "allusion", "target": "Acts 3:21",
       "note": "'Nothing was missing — young or old, sons or daughters, plunder or anything else that had been taken. David brought everything back.' The completeness of David's recovery is a temporal type of the eschatological restoration Christ will accomplish. Peter in Acts 3:21 speaks of 'the time for restoring all things about which God spoke through his prophets.' The anointed who recovers everything taken — every son, every daughter, every lost thing — points to the final restoration in which nothing that belongs to God&rsquo;s people is left unredeemed."}
    ],
    "24": [
      {"type": "allusion", "target": "Matt 20:10-16",
       "note": "David rules that the share of those who stayed at the brook Besor is the same as the share of those who fought — 'as his share is who goes down into the battle, so shall his share be who stays by the baggage; they shall share alike' (v24). The jealousy of the 'wicked and worthless men' who fought mirrors the grumbling of the workers hired first in the parable of the vineyard (Matt 20:10-16: 'You have made them equal to us who have borne the burden of the day and the scorching heat'). In both cases the owner/king rules that the gift is not proportional to performance but equal for all who belong to the community."}
    ]
  },
  "31": {
    "4": [
      {"type": "shadow", "target": "John 10:18",
       "note": "Saul asks his armor-bearer to run him through — he will not be taken alive by the uncircumcised. He dies by his own sword, by his own hand, choosing death to avoid capture. The contrast with Christ is pointed: 'No one takes my life from me, but I lay it down of my own accord' (John 10:18). Both Saul and Christ choose their moment of death voluntarily — but Saul's choice is driven by fear of what the enemy will do to him, while Christ's is driven by love for those he will redeem. The voluntary death of the failed king throws the voluntary death of the true King into relief."}
    ],
    "6": [
      {"type": "shadow", "target": "Dan 2:44",
       "note": "'Saul died, and his three sons, and his armor-bearer, and all his men together on that same day.' The first Israelite king's dynasty ends in a single battle — the Saulide kingship proves mortal, like every other human kingdom. Daniel 2:44 promises a kingdom that 'will never be destroyed, nor will it be left to another people.' Luke 1:33 applies this to Christ: 'of his kingdom there will be no end.' The death of Saul's kingdom on Mount Gilboa is the historical demonstration of why every human dynasty falls short of what the covenant promise requires."}
    ],
    "11": [
      {"type": "allusion", "target": "Luke 23:50-53",
       "note": "When the people of Jabesh-gilead heard what the Philistines had done to Saul's body, their fighting men traveled through the night to retrieve and bury the bodies with honor. Jabesh-gilead owed Saul its existence (1 Sam 11 — he rescued them from Nahash); their loyal burial of the fallen king is covenant-gratitude expressed in service to the dead. Joseph of Arimathea similarly 'went to Pilate and asked for the body of Jesus' and provided an honorable burial (Luke 23:50-53) — the faithful person who honors the body of the condemned King at personal risk."}
    ],
    "13": [
      {"type": "theme", "target": "John 19:40",
       "note": "The men of Jabesh-gilead buried the bones of Saul and his sons under the tamarisk tree, then fasted seven days — a proper mourning rite for the dead king. The careful handling of the royal body and the accompanying ritual mourning parallels the attention given to Christ's body: Nicodemus and Joseph of Arimathea wrapping the body 'with the spices, as is the burial custom of the Jews' (John 19:40). The care for the body of the defeated king by those who remained loyal is a type of the love shown to the crucified Christ by the community that believed in him."}
    ]
  }
}

def main():
    existing = load_echo('1samuel')
    merge_echo(existing, SAMUEL1_ECHOES)
    save_echo('1samuel', existing)

    print('1 Samuel echo ch 28-31:')
    for ch in ['28', '29', '30', '31']:
        entries = existing.get(ch, {})
        status = 'done' if entries else 'MISSING'
        print(f'  ch {ch}: {status} ({len(entries)} verse(s) with entries)')
    print(f'Total chapters with entries: {len(existing)}')

if __name__ == '__main__':
    main()
