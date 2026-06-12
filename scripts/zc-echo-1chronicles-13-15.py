"""
MKT Echo — 1 Chronicles chapters 13–15
Run: python3 scripts/zc-echo-1chronicles-13-15.py

Ch 13: Uzzah struck dead at the threshing floor — holiness of the ark; Obed-edom blessed
Ch 14: Baal-perazim ("LORD who breaks through"); divine-warrior pattern; David inquires of God
Ch 15: Proper Levitical transport of the ark; ark procession into Jerusalem; Michal's contempt

Key decisions:
- Uzzah (13:9-10): echo to Heb 10:31 and 1 Cor 11:29-30 (divine holiness enforced in worship)
- Baal-perazim (14:11): echo to Isa 28:21 (NT context: Paul's triumph language in 2 Cor 2:14)
- Ark procession (15:25-28): Triumphal Entry of Jesus into Jerusalem (Matt 21) is the NT
  structural echo; also Rev 11:19 (ark seen in heaven's temple)
- Parallels file: 1 Chr 15:25 has a 2 Sam 6 parallel — that is OT-to-OT, not absorbed here
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

CHRONICLES_ECHOES = {
  "13": {
    "9": [
      {"type": "shadow", "target": "Heb 10:31", "note": "Uzzah reached out to steady the ark and was struck dead — the incident embodies the principle that Hebrews 10:31 articulates: it is a fearful thing to fall into the hands of the living God; the holy presence cannot be approached on human initiative or handled with casual familiarity, a principle the Levitical regulations existed to enforce."},
      {"type": "allusion", "target": "1 Cor 11:29", "note": "The death at the ark for failing to discern its holiness prefigures Paul's warning in 1 Cor 11:29-30 that eating the Lord's Supper without discerning the body brings judgment; both passages apply the same principle — improper contact with God's sacred presence has lethal consequences — to different covenant contexts."}
    ],
    "12": [
      {"type": "shadow", "target": "Heb 12:28", "note": "David's fearful question — How can I bring the ark of God to me? — is the existential question of how sinful humanity approaches a holy God; Hebrews 12:28-29 answers: through reverence and awe, because our God is a consuming fire — the same God whose holiness David encountered at the threshing floor of Chidon."}
    ],
    "14": [
      {"type": "theme", "target": "Jas 4:8", "note": "The house of Obed-edom was blessed for three months while hosting the ark — the presence of God brings blessing to those who receive it; James 4:8 ('draw near to God and he will draw near to you') applies the same principle: proximity to the divine presence is the source of blessing, not merely of danger."}
    ]
  },
  "14": {
    "2": [
      {"type": "shadow", "target": "Acts 2:36", "note": "David perceived that YHWH had established him as king over Israel for the sake of his people — the Davidic recognition that his kingship is divine appointment for others' benefit; Acts 2:36 announces the greater fulfillment: God made Jesus both Lord and Christ, the Davidic king enthroned after resurrection, whose reign is the ultimate establishment of the covenant promise behind David's kingship."}
    ],
    "11": [
      {"type": "allusion", "target": "2 Cor 2:14", "note": "Baal-perazim — the Lord who breaks through like a breaking-through of waters (14:11); Isaiah 28:21 recalls this site as a paradigm of YHWH's decisive act; Paul's language in 2 Cor 2:14 (God always leads us in triumphal procession in Christ) draws on the same divine-warrior tradition of YHWH going before his people to break through the enemy, now fulfilled in Christ's resurrection-victory."},
      {"type": "allusion", "target": "Isa 28:21", "note": "David named the place Baal-perazim after YHWH's breakthrough; Isaiah 28:21 explicitly recalls this site as the paradigm of YHWH's 'strange work' — his decisive intervention against enemies — projecting a future Baal-perazim on a cosmic scale; the NT reads Christ's resurrection as that ultimate divine breakthrough."}
    ],
    "12": [
      {"type": "theme", "target": "1 Cor 10:20", "note": "The Philistines abandoned their gods at Baal-perazim and David burned them — the futility and abandonment of idols when confronted by YHWH's power; Paul applies the same principle in 1 Cor 10:20-21: the idols of the nations are nothing beside the God whose presence is incompatible with competing loyalties."}
    ],
    "15": [
      {"type": "shadow", "target": "Rev 19:11", "note": "The signal — the sound of marching in the tops of the balsam trees, then YHWH goes out before the army to strike the Philistines — is the divine-warrior pattern of YHWH going ahead of his people into battle; Revelation 19:11-16 presents the final fulfillment: Christ riding out as the divine warrior, the armies of heaven following, going before his people to ultimate victory."}
    ]
  },
  "15": {
    "2": [
      {"type": "shadow", "target": "Heb 8:5", "note": "David's insistence that only the Levites carry the ark — as Moses commanded — reestablishes the proper order of approach to God's presence; Hebrews 8:5 sees the entire Mosaic worship structure as a copy and shadow of the heavenly realities; the Levitical precision about who approaches God and how prefigures the one mediator through whom all access to God now comes."}
    ],
    "13": [
      {"type": "shadow", "target": "Heb 9:6", "note": "The first attempt failed because the Levites did not carry the ark as prescribed — the LORD broke out against them; Hebrews 9:6-7 describes the Levitical priests performing their regular service in the first section of the tabernacle; the pattern of prescribed approach versus improvised approach underlies the entire argument of Hebrews: Christ's priestly service follows the heavenly pattern, not a humanly devised one."}
    ],
    "25": [
      {"type": "allusion", "target": "Matt 21:9", "note": "The ark procession into Jerusalem — elders, commanders, shouting, trumpets, cymbals, harps, and the cry of celebration (15:28) — is the OT pattern behind the triumphal entry of Jesus into Jerusalem (Matt 21:9: the crowds shouting Hosanna, son of David, blessed is he who comes in the name of the Lord); where David brought the ark of YHWH's presence into his city with acclamation, Jesus enters as YHWH incarnate, the ark and the presence in one person."}
    ],
    "28": [
      {"type": "allusion", "target": "Rev 11:19", "note": "All Israel brought up the ark of the covenant of the LORD with shouting and musical instruments (15:28); Revelation 11:19 shows the ark of the covenant appearing in the opened temple of heaven at the moment of the kingdom's consummation — the earthly ark procession finds its eschatological completion when the covenant of which the ark was the sign is fully established in the new creation."}
    ],
    "29": [
      {"type": "theme", "target": "Matt 11:19", "note": "Michal daughter of Saul despised David in her heart when she saw him dancing before the LORD — the rejection of authentic, exuberant worship by those who judge by appearances and propriety; Jesus faced the same pattern: John's asceticism was criticized, his own celebration was criticized (Matt 11:18-19); both David and Jesus were scorned by those whose cultural expectations excluded the form that divine joy actually took."}
    ]
  }
}

def main():
    existing = load_echo('1chronicles')
    merge_echo(existing, CHRONICLES_ECHOES)
    save_echo('1chronicles', existing)
    ch_count = len(CHRONICLES_ECHOES)
    v_count = sum(len(vv) for vv in CHRONICLES_ECHOES.values())
    print(f'1 Chronicles 13-15 echoes written ({ch_count} chapters, {v_count} verses).')

if __name__ == '__main__':
    main()
