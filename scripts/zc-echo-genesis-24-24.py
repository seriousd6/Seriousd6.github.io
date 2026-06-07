"""
Echo Layer — Genesis chapter 24
Run: python3 scripts/zc-echo-genesis-24-24.py

Genesis 24 is the longest chapter in Genesis (67 verses) and one of the richest typological
narratives in the OT. The primary type: Abraham's servant sent to find a bride for Isaac maps
onto the Holy Spirit sent by the Father to gather the church as bride for Christ.

Key echo trajectories:
- The servant = the Holy Spirit (sent, not self-seeking, glorifies the son, brings gifts)
  → John 15:26; 16:13-14; Eph 1:13-14
- Isaac = Christ (the son who goes to meet the bride)
  → John 14:2-3; Rev 19:7-9
- Rebekah = the church (choosing to go, given freely in response to invitation)
  → Rev 22:17; Eph 5:25-27
- The well-meeting: Rebekah at the well → John 4 (Jesus and the Samaritan woman);
  Jacob/Rachel at a well (Gen 29); Moses/Zipporah at a well (Exod 2) — three covenant-bride
  meetings at wells structure the patriarchal narrative
- v15 (answer before prayer complete): Isa 65:24 ('before they call I will answer')
- v67 (Isaac brings Rebekah into Sarah's tent): John 3:29; Rev 19:7 (wedding of the Lamb)

No parallels data to absorb for ch 24.
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

GENESIS_ECHOES = {
  "24": {
    "2": [
      {"type": "shadow", "target": "Heb 6:13", "note": "Abraham makes his servant swear 'by the LORD, the God of heaven and of earth' (24:3) — a covenant oath that binds the entire mission. Heb 6:13-17 develops the logic of divine oath-making: 'since there was no one greater than himself, he swore by himself.' The whole of Gen 24 turns on an oath freely given, structuring a mission of grace — the pattern behind the new covenant mission of the Spirit."}
    ],
    "4": [
      {"type": "shadow", "target": "Eph 5:27", "note": "Abraham's insistence that his son's wife must not be taken from the Canaanites but from his own kindred (24:4) — the bride must come from the covenant community, those who share the lineage of promise. Eph 5:27 uses the same logic to describe the church as the bride Christ presents to himself 'without spot or wrinkle or any such thing... holy and without blemish' — the bride's identity is defined by her relation to the Bridegroom's heritage."}
    ],
    "7": [
      {"type": "shadow", "target": "Matt 28:20", "note": "'He will send his angel before you' (24:7) — Abraham's confidence that God will guide the servant's mission echoes through every sending commission in Scripture. Jesus's Great Commission promise 'I am with you always, to the end of the age' (Matt 28:20) is the NT counterpart: the Son sends the Spirit (John 15:26; 16:7) and accompanies the mission the way God accompanies the servant in Gen 24."}
    ],
    "12": [
      {"type": "shadow", "target": "John 16:13", "note": "The servant's prayer at the well — 'Please grant me success today' (24:12) — is the model of Spirit-guided mission prayer: asking for divine direction in the work of finding the bride. Jesus describes the Spirit's mission in exactly these terms: 'he will guide you into all truth... he will glorify me' (John 16:13-14). The servant throughout Gen 24 refuses to speak of himself; the Spirit likewise does not speak of himself (John 16:13)."}
    ],
    "14": [
      {"type": "shadow", "target": "Eph 1:13", "note": "The servant sets a specific sign by which he will recognize the chosen bride: her willingness to draw water not just for him but for all his camels (24:14). This tests for generous, generous-beyond-what-is-asked service — the character of the one called. Similarly, the Spirit seals those who hear and believe (Eph 1:13-14), recognizing and ratifying the response of faith, not imposing it coercively."}
    ],
    "15": [
      {"type": "shadow", "target": "Isa 65:24", "note": "'Before he had finished speaking, behold, Rebekah... came out' (24:15) — the answer to prayer arrives before the prayer is complete, a mark of divine foreknowledge and provision already in motion. Isa 65:24: 'Before they call I will answer; while they are yet speaking I will hear' — the pattern of preemptive divine grace that grounds NT prayer confidence (Matt 6:8: 'your Father knows what you need before you ask him')."}
    ],
    "21": [
      {"type": "shadow", "target": "Acts 15:8", "note": "The servant 'gazed at her in silence to learn whether the LORD had prospered his journey or not' (24:21) — the deliberate, watching discernment of the divine sign. The NT parallel is the community watching for divine confirmation of who belongs to the covenant people: Acts 15:8 ('God, who knows the heart, bore witness to them, by giving them the Holy Spirit just as he did to us'). Divine confirmation, not human calculation, ratifies the mission's success."}
    ],
    "26": [
      {"type": "shadow", "target": "John 4:23", "note": "The servant bowed his head and worshiped the LORD at the moment the sign was confirmed (24:26) — worship as the immediate response to recognized divine grace. This is the pattern of true worship: not initiated by the worshiper's agenda but arising in response to divine disclosure. Jesus's description of Spirit-and-truth worship (John 4:23-24) to the Samaritan woman — herself encountered at a well — picks up this structural connection between the well, the bride-finding mission, and genuine worship."}
    ],
    "27": [
      {"type": "theme", "target": "Luke 1:78", "note": "'Blessed be the LORD, the God of my master Abraham, who has not forsaken his steadfast love (<em>ḥesed</em>) and his faithfulness toward my master' (24:27) — the servant's blessing formula upon recognizing divine provision. The combination of <em>ḥesed</em> (lovingkindness/covenant loyalty) and <em>emet</em> (faithfulness/truth) is the Exodus 34:6 character of God applied to mission-completion. Luke 1:78 ('the tender mercy of our God') uses the same covenantal vocabulary to interpret John's birth as the dawn of the promised visitation."}
    ],
    "33": [
      {"type": "shadow", "target": "John 4:34", "note": "'I will not eat until I have said what I have to say' (24:33) — the servant prioritizes his mission over his personal needs. Jesus declares the same priority in John 4:34: 'My food is to do the will of him who sent me and to accomplish his work.' The servant in Gen 24 is a type of the one sent who has no agenda of his own but only the mission of the sender — in John 4, the one sent is engaging in another well/bride-meeting conversation with the Samaritan woman."}
    ],
    "34": [
      {"type": "shadow", "target": "John 15:26", "note": "When the servant speaks to Laban and Bethuel, he begins: 'I am Abraham's servant' — and the entire narrative of vv.34-48 is the servant's account of his master's greatness, not his own. This is the Holy Spirit's characteristic mode: 'he will bear witness about me' (John 15:26), 'he will glorify me' (John 16:14). The servant does not commend himself; he commends his master and declares the master's gifts."}
    ],
    "49": [
      {"type": "shadow", "target": "Rev 22:17", "note": "'Now then, if you are going to show steadfast love and faithfulness to my master, tell me' (24:49) — the servant's appeal for a response to his master's offer. The free, invited response is essential to the structure of the narrative. Rev 22:17 ('the Spirit and the Bride say Come... let the one who desires take the water of life without price') mirrors this exactly: the Spirit-mission concludes with an open, free invitation to which the only required response is willingness."}
    ],
    "58": [
      {"type": "type", "target": "Rev 22:17", "note": "'Will you go with this man?' And she said, 'I will go' (24:58) — Rebekah's free consent to leave her family and travel to an unseen husband is the type of the church's response to the gospel. No compulsion; the servant has made the offer and presented the gifts; the decision belongs to Rebekah. Rev 22:17 ('let the one who is thirsty come; let the one who desires take the water of life without price') captures the same structure: the Spirit's mission concludes with a free response, not a mandate."}
    ],
    "63": [
      {"type": "type", "target": "John 14:3", "note": "Isaac went out to meditate in the field at evening and lifted up his eyes and saw the camels coming (24:63) — the son going out to receive the bride being brought to him. This is the type of the parousia: Christ who 'went to prepare a place' (John 14:2) and will 'come again and take you to myself' (John 14:3) going out to receive the bride gathered by the Spirit. The evening hour recalls Isa 25:6-8 (the eschatological feast at which death is swallowed up)."}
    ],
    "67": [
      {"type": "type", "target": "Rev 19:7", "note": "Isaac brought Rebekah into his mother Sarah's tent, and she became his wife, and he loved her (24:67) — the narrative reaches its goal: the wedding. The structure of the entire chapter (servant sent, bride found, freely consents, journey made, union accomplished) is the type of which Rev 19:7-9 is the antitype: 'The marriage of the Lamb has come, and his Bride has made herself ready.' Isaac's love for Rebekah is stated as the narrative's closing note — so the goal of the entire Spirit-mission is the Son's love for those given to him by the Father (John 17:24)."},
      {"type": "shadow", "target": "John 3:29", "note": "The friend of the bridegroom (the servant) has completed his mission; now the bridegroom takes the bride. John 3:29 ('the friend of the bridegroom, who stands and hears him, rejoices greatly at the bridegroom's voice') applies this structure to John the Baptist: the forerunner whose entire ministry was to prepare and present the bride (Israel) to Christ. The servant's completed mission in Gen 24:67 is the type of every preparatory ministry that brings people to Christ."}
    ]
  }
}

def main():
    existing = load_echo('genesis')
    merge_echo(existing, GENESIS_ECHOES)
    save_echo('genesis', existing)

    result = load_echo('genesis')
    n = len(result.get('24', {}))
    print(f'  Ch 24: {n} verses with echoes')
    total = len(result)
    print(f'  Genesis total: {total} chapters with echo data')
    print('Genesis 24 echoes written.')

if __name__ == '__main__':
    main()
