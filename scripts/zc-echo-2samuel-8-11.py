"""
echo — 2 Samuel 8–11
run: python3 scripts/zc-echo-2samuel-8-11.py

Ch8: David's military victories and just administration — partial fulfillment of the royal ideal
Ch9: Mephibosheth — the clearest OT type of grace: the deserving-death outcast restored to the king's table
Ch10: Ammonite humiliation of David's envoys — the rejected-ambassador pattern
Ch11: Bathsheba — David's fall; even the ideal king fails; nothing is hidden from YHWH
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
  "8": {
    "15": [
      {"type": "allusion", "target": "Isa 9:7", "note": "David administered justice and equity to all his people — the OT royal ideal is that the Davidic king executes mishpat (justice) and tsedaqah (righteousness) for all his subjects; David partially fulfills this; Isa 9:7 prophesies the coming Son who establishes justice and righteousness permanently: 'of the increase of his government and of peace there will be no end... to establish it with justice and with righteousness from this time forth and forevermore'"},
      {"type": "allusion", "target": "Jer 23:5", "note": "David's justice and equity across his whole kingdom is the historical foundation for Jeremiah's prophecy of the Branch who 'shall reign as king and deal wisely, and shall execute justice and righteousness in the land' — David is the type; the Davidic Messiah is the antitype who fulfills what David could only approximate"}
    ]
  },
  "9": {
    "7": [
      {"type": "type", "target": "Eph 2:4-7", "note": "Do not be afraid, for I will show you kindness for the sake of your father Jonathan. I will restore to you all the land of Saul your father, and you shall eat at my table always — Mephibosheth is the OT's most fully developed type of grace: he is crippled (v3: lame in both feet), hiding in Lo-debar (a place of 'no pasture'), has no claim on the king, and himself says 'What is your servant, that you should show regard for a dead dog such as I?' (v8); David seeks him out by covenant-loyalty (hesed) to a third party (Jonathan); God's grace in Christ follows the exact pattern: 'even when we were dead in our trespasses, God, being rich in mercy... made us alive together with Christ' (Eph 2:4-5)"}
    ],
    "13": [
      {"type": "allusion", "target": "Luke 14:21", "note": "Mephibosheth lived in Jerusalem and ate always at the king's table, now lame in both feet — Jesus's parable of the great banquet (Luke 14:15-24) explicitly includes 'the poor and crippled and blind and lame' brought in from the streets to eat at the master's table; Mephibosheth — crippled, an outcast from the house of the former king — is the historical prototype for those guests"}
    ]
  },
  "10": {
    "4": [
      {"type": "allusion", "target": "Isa 50:6", "note": "Hanun seized David's servants and shaved off half their beards and cut their garments in the middle — the humiliation of the king's ambassadors (beard-shaving was profound dishonor in the ANE) is the pattern of the Servant's humiliation in Isa 50:6: 'I gave my back to those who strike, and my cheeks to those who pull out the beard; I hid not my face from disgrace and spitting'; in both cases, the king's representative is treated with contempt by those to whom he is sent"},
      {"type": "allusion", "target": "Matt 22:6", "note": "The Ammonites' humiliation of David's servants who came to show covenant-loyalty (hesed, v2) — sent to comfort, they are stripped and sent back in shame — is the historical backdrop for Jesus's parable of the king whose servants are humiliated and killed by those who refuse the wedding invitation (Matt 22:3-7); the pattern: the great king extends grace; it is rejected and his servants are treated with contempt"}
    ]
  },
  "11": {
    "4": [
      {"type": "allusion", "target": "Matt 5:28", "note": "David sent messengers and took her; and she came to him, and he lay with her — the progression in vv2-4 (saw → inquired → sent → took) is the anatomy of sin: desire, inquiry, opportunity, act; Jesus addresses the same progression at its root: 'everyone who looks at a woman with lustful intent has already committed adultery with her in his heart' (Matt 5:28); the root is the looking and desiring, not only the act"}
    ],
    "27": [
      {"type": "allusion", "target": "Heb 4:13", "note": "The thing that David had done displeased YHWH — the final verse of ch11 is YHWH's verdict on the entire sequence; what David thought was successfully concealed (the adultery hidden by Uriah's arranged death) is fully visible to YHWH; 'no creature is hidden from his sight, but all are naked and exposed to the eyes of him to whom we must give account' (Heb 4:13); the divine sight that David forgot is what Nathan's parable (ch12) makes visible"}
    ]
  }
}

def main():
    e = load_echo('2samuel')
    merge_echo(e, SAMUEL2_ECHO)
    save_echo('2samuel', e)
    print('2samuel ch8-11 echo: done')

if __name__ == '__main__':
    main()
