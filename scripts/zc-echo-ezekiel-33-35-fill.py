"""
Echo Layer — Ezekiel chapters 33–35
Run: python3 scripts/zc-echo-ezekiel-33-35-fill.py

Ch 34 already has 1 entry (v.4 → Luke 15). This script fills in chs 33 and 35
and adds further entries to ch 34.

Major echo clusters:
- Ch 33: Watchman recommissioned — 33:6-9 → Acts 20:26-27 (Paul explicitly uses
  watchman blood-accountability language); 33:11 → 2 Pet 3:9; 33:31-32 →
  Matt 7:24-27 / Jas 1:22; 33:33 → John 13:19 (predictive prophecy vindicates)
- Ch 34: Good Shepherd oracle — the densest Christological chapter in Ezekiel;
  34:11-12 → John 10:11; Luke 15:4-7; 34:16 → Luke 4:18; 34:23 → John 10:14-16;
  Heb 13:20; 34:25 → Heb 13:20; 34:31 → John 10:27-28
- Ch 35: Edom/Mount Seir — 35:5 → Heb 12:16-17 (Esau/profane pattern);
  35:10 → Acts 17:28; 35:15 → Rev 7:9-10 (nations rejoicing in salvation)
"""

import json, pathlib

ROOT = pathlib.Path(__file__).parent.parent

def load_echoes(book):
    p = ROOT / 'data' / 'echoes' / f'{book}.json'
    return json.loads(p.read_text()) if p.exists() else {}

def save_echoes(book, data):
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

EZK_ECHOES = {
  "33": {
    "6": [
      {"type": "allusion-source", "target": "Acts 20:26", "note": "The watchman who fails to warn is accountable for the blood of those who die — Paul quotes this exact principle at his Ephesian farewell: 'I am innocent of the blood of all of you, for I did not shrink from declaring to you the whole counsel of God.' Paul understands his apostolic ministry through the Ezekiel watchman framework."},
      {"type": "allusion", "target": "Acts 18:6", "note": "When Paul is rejected at Corinth, he shakes out his garments and says, 'Your blood be on your own heads; I am clean.' The watchman's blood-accountability of Ezekiel 33:4-6 is the OT template for Paul's apostolic absolution when the warning has been given and rejected."}
    ],
    "11": [
      {"type": "allusion-source", "target": "2 Pet 3:9", "note": "As I live, declares the Lord GOD, I take no pleasure in the death of the wicked but rather that the wicked turn from his way and live — 2 Peter builds on this Ezekielian principle: the Lord is not slow concerning his promise, but patient toward you, not willing that any should perish but that all should come to repentance."},
      {"type": "allusion", "target": "Luke 13:3", "note": "'Turn back, turn back from your evil ways! Why will you die, O house of Israel?' Jesus repeats the same urgent call: 'unless you repent, you will all likewise perish.' The urgency of Ezekiel's watchman-call is continuous with Jesus's own call to repentance before the catastrophe comes."}
    ],
    "24": [
      {"type": "allusion-source", "target": "Gal 3:7-9", "note": "'Abraham was one man, yet he possessed the land; but we are many' — the remnant in the ruins claim Abrahamic land-rights by physical descent. Paul's counter-argument in Galatians 3:7-9 redefines Abrahamic descent: those of faith are sons of Abraham; those who have faith are blessed with Abraham the man of faith."}
    ],
    "31": [
      {"type": "allusion-source", "target": "Matt 7:26-27", "note": "They hear your words but will not act on them — Jesus builds his parable directly on this pattern: the foolish builder who hears the words of Jesus but does not put them into practice is like a man who builds his house on sand and collapses when the storm comes. The failure to act on heard words is the defining distinction between false and genuine disciples."},
      {"type": "allusion", "target": "Jas 1:22-24", "note": "Coming to hear the prophet like an audience entertained by beautiful music — James makes the same diagnosis: do not merely listen to the word and so deceive yourselves; do what it says. Anyone who listens but does not do is like someone who looks at his face in a mirror and immediately forgets what he looks like."}
    ],
    "33": [
      {"type": "allusion-source", "target": "John 13:19", "note": "When it comes to pass, then they will know that a prophet has been among them — Jesus uses exactly this logic: 'I am telling you now before it happens, so that when it does happen you will believe that I am he.' Predictive fulfillment is the validation of the true prophet, and Jesus applies this same criterion to himself."},
      {"type": "allusion", "target": "John 14:29", "note": "I have told you now before it happens, so that when it does happen you will believe — the watchman's vindication through fulfilled prediction is the model for Jesus's own practice of announcing events before they occur so that their fulfillment will produce faith."}
    ]
  },
  "34": {
    "2": [
      {"type": "allusion-source", "target": "John 10:12-13", "note": "Woe to the shepherds of Israel who feed themselves and not the flock — Jesus's description of the hired hand who abandons the sheep when the wolf comes and flees because he does not own the sheep is the NT counterpart to Ezekiel's indictment. The shepherd who feeds himself rather than the flock is the hired hand who cares nothing for the sheep."},
      {"type": "allusion", "target": "Matt 23:4", "note": "The leaders who burden others but do not lift a finger — the scribes and Pharisees whom Jesus indicts in Matthew 23 are Ezekiel's self-feeding shepherds in a new guise: they eat the fat (honor, legal fees, temple commerce) while not feeding the flock."}
    ],
    "11": [
      {"type": "allusion-source", "target": "Luke 15:4", "note": "I myself will search for my sheep and seek them out — Jesus's parable of the lost sheep is the direct fulfillment of this divine promise: what man of you, having a hundred sheep and losing one, does not leave the ninety-nine in the open country and go after the one that is lost until he finds it? YHWH's 'I myself will search' is Jesus's 'I will go.'"},
      {"type": "allusion", "target": "John 10:11", "note": "I am the Good Shepherd — Jesus's self-identification is the explicit fulfillment of Ezekiel 34:11-16: YHWH's promise to be the shepherd of his own flock is fulfilled when the Son of God takes on flesh and does what YHWH promised."}
    ],
    "16": [
      {"type": "allusion-source", "target": "Luke 4:18-19", "note": "I will seek the lost, bring back the strayed, bind up the injured, strengthen the weak — Jesus's Nazareth manifesto reads as the direct enactment of this divine program: to preach good news to the poor, release to captives, sight to the blind, freedom for the oppressed, to proclaim the year of the Lord's favor. Each ministry item fulfills one of Ezekiel's shepherd-tasks."},
      {"type": "allusion", "target": "Matt 11:28-30", "note": "Come to me, all who are weary and burdened, and I will give you rest — Jesus invites the bruised and burdened (those who should have been bound up and strengthened by their shepherds) to come to him directly, promising what the failed shepherds never provided."}
    ],
    "23": [
      {"type": "allusion-source", "target": "John 10:14-16", "note": "I will set up one shepherd over them, my servant David — the one-shepherd oracle is fulfilled in Jesus, the Son of David: I am the Good Shepherd, I know my own and my own know me. I have other sheep that are not of this fold; I must bring them also, and they will listen to my voice; then there will be one flock, one shepherd."},
      {"type": "allusion", "target": "Heb 13:20", "note": "The one Davidic shepherd who tends YHWH's flock under a covenant — may the God of peace, who through the blood of the eternal covenant brought back from the dead our Lord Jesus, that great Shepherd of the sheep, equip you with everything good. The resurrection of the great Shepherd fulfills Ezekiel 34:23's David-oracle."}
    ],
    "25": [
      {"type": "allusion-source", "target": "Eph 2:14-17", "note": "I will make a covenant of peace with them — Christ is our peace; through his cross he made peace and came and preached peace to those who were far away and peace to those who were near. The covenant of peace Ezekiel announces YHWH making with the gathered flock is the peace that Christ achieves by blood."},
      {"type": "allusion", "target": "Acts 3:19-20", "note": "Showers of blessing sent in their season (vv.26) — Peter's call to repentance promises that times of refreshing will come from the Lord; the covenant of peace made through the Messiah brings the refreshing that Ezekiel's showers of blessing anticipate."}
    ],
    "31": [
      {"type": "allusion-source", "target": "John 10:27-28", "note": "You are my sheep, the human sheep of my pasture, and I am your God — Jesus: my sheep hear my voice, and I know them, and they follow me. I give them eternal life, and they will never perish, and no one will snatch them out of my hand. The covenant formula 'you are my sheep; I am your God' reaches its fulfillment in Jesus's guarantee of eternal security."}
    ]
  },
  "35": {
    "5": [
      {"type": "allusion", "target": "Heb 12:16-17", "note": "Perpetual enmity — the Esau/Edom pattern of nursing enmity against Jacob, seizing his moment at the calamity. Hebrews invokes Esau's irreversible choice as the warning against profaning sacred things: see that no one is sexually immoral or unholy like Esau, who for a single meal sold his birthright. Afterward, when he wanted to inherit the blessing, he was rejected, though he sought it with tears."}
    ],
    "10": [
      {"type": "allusion", "target": "Acts 17:28", "note": "'These two countries shall be mine' — although the LORD was there. The Edomites claim what belongs to YHWH without recognizing his presence: for in him we live and move and have our being, Paul tells the Athenians. The failure to perceive YHWH's presence in what one claims is the Edom pattern applied universally."}
    ],
    "15": [
      {"type": "allusion", "target": "Rev 7:9-10", "note": "While the whole earth rejoices, I will make you a desolation — the contrast between Edom's desolation and the whole earth's rejoicing over the promised restoration is fulfilled eschatologically: a great multitude from every nation, tribe, people and language stands before the throne and before the Lamb, crying out 'Salvation belongs to our God.' The nations' joy over YHWH's salvation is the positive counterpart to Edom's permanent exclusion."}
    ]
  }
}

def main():
    existing = load_echoes('ezekiel')
    merge_echo(existing, EZK_ECHOES)
    save_echoes('ezekiel', existing)

    out = json.loads((ROOT / 'data/echoes/ezekiel.json').read_text())
    for ch in [33, 34, 35]:
        ck = str(ch)
        count = sum(len(v) for v in out.get(ck, {}).values())
        status = 'done' if out.get(ck) else 'MISSING'
        print(f'ch {ch}: {status} ({len(out.get(ck, {}))} verse-keys, {count} entries total)')

if __name__ == '__main__':
    main()
