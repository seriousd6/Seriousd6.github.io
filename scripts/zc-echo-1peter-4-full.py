"""
echo layer — 1 Peter chapter 4 (adds ch4 entries; ch1-3 already present)
Output: data/echoes/1peter.json
Run: python3 scripts/zc-echo-1peter-4-full.py
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
    # INTENT: Merge new echo entries without overwriting already-present chapter/verse keys.
    # CHANGE? If echo JSON structure changes from {ch:{v:[entries]}}, update this traversal.
    # VERIFY: Re-running should produce identical output.
    for ch, verses in new_data.items():
        if ch not in existing:
            existing[ch] = {}
        for v, entries in verses.items():
            if v not in existing[ch]:
                existing[ch][v] = entries

ONEPETER_ECHO = {
  "4": {
    "1": [
      {"type": "allusion", "target": "Isa 53:3-4", "note": "He was despised and rejected, a man of sorrows acquainted with grief — Peter's call to arm oneself with Christ's suffering attitude draws on the Servant's paradigm of suffering as the path of obedience; the Servant who suffered in the body is the model Peter applies"},
      {"type": "allusion", "target": "Isa 50:7", "note": "I have set my face like flint — the Servant's resolve to endure physical suffering in obedience to God is the antecedent of Peter's 'arm yourselves with the same attitude'; suffering willingly accepted becomes the decisive severance from sin"}
    ],
    "3": [
      {"type": "allusion", "target": "Deut 18:9-14", "note": "Do not practice divination, sorcery, or the abominations of the nations — Peter's list of Gentile vices (debauchery, lusts, drunkenness, orgies, carousing, lawless idolatry) echoes the catalogue of condemned Gentile practices in Deuteronomy; the converted community is called to the same separation from pagan practice that Israel was commanded at the conquest"},
      {"type": "allusion", "target": "Amos 2:8", "note": "They drink wine taken as fines and lie on garments taken in pledge — Amos's indictment of Israel for adopting Canaanite debauchery at worship-sites provides the prophetic background for Peter's catalogue; the vices he lists are the same practices the prophets condemned in Israel when she assimilated to the nations"}
    ],
    "5": [
      {"type": "allusion", "target": "Dan 7:9-10", "note": "The court sat in judgment and the books were opened — Peter's 'judge the living and the dead' language stands in the tradition of Daniel's throne-room judgment scene; the one ready to judge is the Lord to whom the Son of Man is given dominion over all peoples"},
      {"type": "allusion", "target": "Joel 3:1-2", "note": "I will gather all nations and bring them down to the Valley of Jehoshaphat, and I will enter into judgment with them — Joel's eschatological judgment of the nations corresponds to Peter's universal judgment; the one 'ready to judge' is the LORD of Joel's oracle, fulfilled in the risen Christ"}
    ],
    "8": [
      {"type": "quote", "target": "Prov 10:12", "note": "Hatred stirs up strife, but love covers all offenses — Peter directly cites (in slightly adapted form) the Solomonic wisdom maxim; the covering of sins through love is the horizontal expression of the divine forgiveness of sin that Peter has been addressing throughout the letter"}
    ],
    "12": [
      {"type": "allusion", "target": "Isa 48:10", "note": "I have tried you in the furnace of affliction — Isaiah's 'furnace of affliction' image for Israel's purification in Babylonian exile is the background for Peter's 'fiery ordeal' (pyrōsei) as a test rather than a punishment; suffering is the refiner's work, not divine abandonment"},
      {"type": "allusion", "target": "Mal 3:2-3", "note": "He is like a refiner's fire... he will sit as a refiner and purifier of silver — Malachi's eschatological refiner who purifies the Levites provides the typological background for Peter's fiery trial; the same purifying work that Malachi projects onto the Messiah's coming is now applied to the community that belongs to the Messiah"}
    ],
    "13": [
      {"type": "allusion", "target": "Isa 53:3-12", "note": "He was wounded for our transgressions, crushed for our iniquities — participation in Christ's sufferings (koinōneite tois tou Christou pathēmasin) is rooted in the Servant's vicarious suffering pattern; those who share the Servant's suffering will also share his vindication and glory"},
      {"type": "allusion", "target": "Ps 22:1-31", "note": "My God, my God, why have you forsaken me? ... He has not despised or scorned the suffering of the afflicted one — Psalm 22 spans the full arc from desolation to vindication that Peter maps onto the community's experience: present suffering leads to eschatological rejoicing at the revelation of Christ's glory"}
    ],
    "14": [
      {"type": "allusion", "target": "Isa 11:2", "note": "The Spirit of the LORD will rest on him — the Spirit of glory that rests on the suffering believer is the same Spirit promised to rest on the Branch from Jesse; the community that bears Christ's name participates in the Spirit-anointing that characterized the Messiah's own ministry"},
      {"type": "allusion", "target": "Num 6:25", "note": "The LORD make his face shine on you — the Aaronic blessing of the LORD's shining face upon Israel corresponds to the Spirit of glory resting on the suffering community; divine favor expressed through eschatological glory is the blessing of those who bear the name"}
    ],
    "17": [
      {"type": "allusion", "target": "Ezek 9:6", "note": "Begin at my sanctuary — Ezekiel's vision of divine judgment beginning with the sanctuary and its elders before moving to the city provides the template for Peter's judgment beginning with God's household; the sequence (household first, then the disobedient) replicates the Ezekiel pattern"},
      {"type": "allusion", "target": "Jer 25:29", "note": "I am beginning to bring disaster on the city that bears my name; and will you indeed go unpunished? — Jeremiah's oracle of judgment on Jerusalem before the nations provides the structural logic for Peter's argument: if judgment begins with God's own people, what awaits those who reject the gospel?"}
    ],
    "18": [
      {"type": "quote", "target": "Prov 11:31", "note": "If the righteous are barely saved, what will become of the ungodly and the sinner? — Peter quotes Prov 11:31 LXX directly (via the exact wording); the Solomonic wisdom observation about the difficulty of the righteous man's path becomes an eschatological warning about the fate of the ungodly who have no standing before the coming Judge"}
    ],
    "19": [
      {"type": "allusion", "target": "Ps 31:5", "note": "Into your hands I commit my spirit — Peter's call to 'commit yourselves to your faithful Creator' (paratithesthōsan tas psychas) echoes the Psalm of trust that Jesus himself cited at his death (Luke 23:46); suffering according to God's will is surrendered to the same faithful God to whom the righteous have always entrusted themselves"}
    ]
  }
}

if __name__ == '__main__':
    existing = load_echo('1peter')
    merge_echo(existing, ONEPETER_ECHO)
    save_echo('1peter', existing)
    import json as _json
    il = _json.load(open(ROOT / 'data' / 'interlinear' / '1peter.json'))
    for ch in ['1', '2', '3', '4']:
        has = bool(existing.get(ch, {}))
        print(f'  ch {ch}: {"present" if has else "MISSING"}')
    print('All chapters present' if all(existing.get(ch) for ch in ['1','2','3','4']) else 'GAPS remain')
