"""
MKT Echo Layer — Acts chapters 25–26
Run: python3 scripts/zc-echo-acts-25-26.py

Source data used:
- data/interlinear/acts.json
- data/parallels/acts.json (no parallels for ch25 or ch26)
- data/echoes/acts.json (existing ch26 v22: Isa 53:11 — merge_echo will preserve it)

Key decisions:
- Ch25 Paul's appeal to Caesar (v11): God's sovereign direction of Paul to Rome through the
  imperial legal system echoes Prov 21:1 (king's heart in God's hand); cross-references Acts 23:11
  promise ("you must testify in Rome") as the divine framework the appeal enacts
- Ch25 Festus's declarations of Paul's innocence (v25, v27): echo the Isaianic innocent-
  servant pattern (Isa 53:9; Ps 35:11-12) — Paul as a suffering-servant figure in miniature
- Ch26 resurrection question (v8): "incredible that God raises the dead" directly invokes the
  OT resurrection hope of Dan 12:2, Job 19:25-27, Isa 26:19 — Paul argues from the canon
- Ch26 commissioning formula (vv.16-18): the language of "open their eyes / darkness to light /
  power of Satan to God" is nearly verbatim from Isa 42:6-7 (Servant as light to nations and
  opener of blind eyes); Paul presents his own call as a Servant-call
- Ch26 v23 "light to his people and to the Gentiles": Isa 42:6 / 49:6 — the same Servant-
  mission texts used in Acts 13:47 and Acts 1:8, now stated as the content of Paul's gospel
- Echo entries are selective; v22 already present (Isa 53:11); no new entry added there
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
    # INTENT: merge echo entries; deduplicate by (type, target) within each verse
    # CHANGE? If echo schema changes, update dedup key here
    # VERIFY: spot-check acts.json ch25 v11 and ch26 v18 in browser echoes panel
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

ACTS_ECHOES = {
  "25": {
    "11": [
      {"type": "theme", "target": "Prov 21:1", "note": "Paul's appeal to Caesar — exercising his right as a Roman citizen — is the immediate occasion, but the deeper logic is Prov 21:1: 'The king's heart is a stream of water in the hand of the LORD; he turns it wherever he will.' Festus's judicial dilemma and the appeals process that results are the form through which God directs Paul to Rome in fulfillment of Acts 23:11 ('you must testify in Rome'). The empire's legal machinery is the instrument of divine purpose, exactly as Solomon's proverb describes."},
      {"type": "allusion", "target": "Isa 46:10", "note": "God's declaration 'my purpose will stand, and I will do all that I please' is the background to the divinely-guided chain from Paul's arrest (ch. 21) through Roman tribunals to the eventual Roman witness. Paul's appeal does not escape God's plan — it enacts it. The 'sovereign over all human authority' theme that runs from Daniel through Acts reaches its narrative fulfillment in Rome."}
    ],
    "19": [
      {"type": "allusion", "target": "Dan 12:2", "note": "Festus's report to Agrippa dismisses the Jewish dispute as being about 'a dead man named Jesus whom Paul claimed was alive' — precisely the resurrection question that OT prophecy had already raised. Daniel 12:2 ('Multitudes who sleep in the dust of the earth will awake') is the clearest OT statement that God would raise the dead; Festus's skepticism frames the exact claim that Paul will press in ch. 26."},
      {"type": "allusion", "target": "Job 19:25", "note": "Paul's claim that Jesus is alive echoes Job's confession: 'I know that my Redeemer lives, and that in the end he will stand upon the earth' (Job 19:25). Job's hope of a living vindicator who appears after death was the oldest scriptural expression of resurrection confidence; Paul's testimony that Jesus is alive is the announcement that Job's hope has been confirmed."}
    ],
    "25": [
      {"type": "allusion", "target": "Isa 53:9", "note": "Festus's public declaration — 'I found he had done nothing deserving of death' — echoes the Servant Song's statement about the suffering servant: 'he had done no violence, nor was any deceit in his mouth' (Isa 53:9). The Roman governor's repeated proclamations of innocence (25:25; cf. 26:31-32) are the secular-legal articulation of the same truth that Isaiah predicted: the servant condemned despite innocence. Paul's situation enacts the Isaianic pattern in miniature."},
      {"type": "allusion", "target": "Ps 35:11", "note": "False witnesses rise up to accuse the innocent — Paul's situation before Festus enacts Ps 35:11-12 ('ruthless witnesses come forward; they question me on things I know nothing about; they repay me evil for good'). The Jewish accusers bringing charges they cannot prove replicates the Psalm's pattern of unjust accusation against the righteous; Paul's defense echoes the Psalmist's appeal for vindication."}
    ]
  },
  "26": {
    "8": [
      {"type": "allusion", "target": "Dan 12:2", "note": "'Why should any of you consider it incredible that God raises the dead?' — Paul's rhetorical challenge invokes the OT canon's own resurrection witness. Daniel 12:2 establishes the resurrection of the dead as a prophetic certainty within Israel's scripture; Paul's argument is that those who accept Daniel cannot find it incredible that God raised Jesus. The question is apologetically directed at Agrippa's familiarity with the prophets (v.27)."},
      {"type": "allusion", "target": "Isa 26:19", "note": "Isaiah's resurrection passage — 'your dead will live; Lord, their bodies will rise — let those who dwell in the dust wake up and shout for joy' (Isa 26:19) — is one of the OT texts that grounds Paul's argument. The resurrection of Jesus is the eschatological event that Isaiah anticipated; incredulity at the resurrection is incredulity at Isaiah's promise."}
    ],
    "16": [
      {"type": "allusion", "target": "Jer 1:8", "note": "Paul's Damascus Road commissioning begins with the same fear-not, I-am-sending-you formula as Jeremiah's call: 'Do not be afraid of them, for I am with you and will rescue you' (Jer 1:8). As Jeremiah was sent to kings and nations (Jer 1:10), Paul is appointed to testify before kings (v.29) and to the Gentiles. The prophetic-call pattern is the frame through which Luke interprets Paul's apostolic vocation."},
      {"type": "allusion", "target": "Isa 42:6", "note": "The language of being raised up as 'a servant and as a witness' echoes Isaiah's description of the Servant: 'I will keep you and will make you to be a covenant for the people and a light for the Gentiles' (Isa 42:6). Paul is not merely a messenger but is himself patterned after the Servant — the one sent to be a witness. This is the same identification Paul and Barnabas made explicit in Acts 13:47."}
    ],
    "18": [
      {"type": "fulfillment", "target": "Isa 42:7", "note": "The commissioning phrase — 'to open their eyes and turn them from darkness to light, and from the power of Satan to God' — nearly verbatim echoes Isaiah 42:7: 'to open eyes that are blind, to free captives from prison and to release from the dungeon those who sit in darkness.' The Servant's mission as articulated in the Second Servant Song is being fulfilled through Paul's apostolic work among the Gentiles. This is the most direct Servant-Song echo in Paul's own account of his call."},
      {"type": "allusion", "target": "Isa 9:2", "note": "The 'darkness to light' imagery of Paul's commissioning echoes Isaiah 9:2 ('the people walking in darkness have seen a great light; on those living in the land of deep darkness a light has dawned'), which Matthew applies to Jesus's Galilean ministry (Matt 4:16). Paul continues the same light-in-darkness mission; the Gentile mission is the outward expansion of the light that first appeared in Israel."}
    ],
    "23": [
      {"type": "fulfillment", "target": "Isa 42:6", "note": "'That the Messiah would bring the message of light to his own people and to the Gentiles' — the dual scope of the gospel (Israel and the nations) fulfills Isaiah 42:6's Servant commission: 'I will make you a light for the Gentiles.' The risen Christ is the Servant who accomplished this through his death and resurrection, and Paul is the instrument through whom the Servant's light reaches the Gentile rulers present in this very scene."},
      {"type": "fulfillment", "target": "Isa 49:6", "note": "Paul's summary of the gospel content — the Messiah suffers, rises, and brings light to both peoples — fulfills the Second Servant Song's explicit command: 'I will make you a light for the Gentiles, that my salvation may reach to the ends of the earth' (Isa 49:6). Acts 13:47 had Paul directly cite this verse; here he states its content as the substance of what Moses and the prophets foretold, completing the Servant's mission in narrative form before Agrippa."},
      {"type": "allusion", "target": "Ps 16:10", "note": "The resurrection claim — 'the Messiah as the first to rise from the dead' — echoes Ps 16:10 ('you will not abandon me to the realm of the dead, nor will you let your faithful one see decay'), the same text Peter cited at Pentecost (Acts 2:27) and Paul cited in Pisidian Antioch (Acts 13:35). The canon's resurrection witness closes Paul's speech before Agrippa as it opened the early preaching."}
    ]
  }
}

def main():
    existing = load_echo('acts')
    merge_echo(existing, ACTS_ECHOES)
    save_echo('acts', existing)
    ch25_count = len(existing.get('25', {}))
    ch26_count = len(existing.get('26', {}))
    print(f'Acts 25-26 echoes: ch25={ch25_count} verses, ch26={ch26_count} verses.')

if __name__ == '__main__':
    main()
