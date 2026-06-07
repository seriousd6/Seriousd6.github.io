"""
echo layer — Revelation chapter 8 (adds ch8; ch6,7,9,10,11 already present)
Output: data/echoes/revelation.json
Run: python3 scripts/zc-echo-revelation-6-11-full.py
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

REV_ECHO_CH8 = {
  "8": {
    "1": [
      {"type": "allusion", "target": "Zeph 1:7", "note": "Be silent before the Lord GOD — Zephaniah's command for cosmic silence before the approaching Day of the LORD provides the liturgical template for John's half-hour silence at the opening of the seventh seal; in both texts the silence precedes devastating divine judgment"},
      {"type": "allusion", "target": "Zech 2:13", "note": "Be silent before the LORD, all flesh — Zechariah's summons to creaturely silence before YHWH's action from his holy dwelling mirrors the heaven-wide silence that greets the Lamb's opening of the final seal"}
    ],
    "3": [
      {"type": "allusion", "target": "Ps 141:2", "note": "Let my prayer be counted as incense before you — David's prayer that his incense-like prayer rise before God is the liturgical template for the angel's golden censer whose incense mingles with the prayers of the saints and rises before God"},
      {"type": "allusion", "target": "Lev 16:12-13", "note": "Aaron shall take a censer full of coals from the altar and put incense on the fire before the LORD — the high-priestly Day of Atonement ritual of carrying burning coals and incense into the holy of holies is the priestly background for the interceding angel's golden censer at the heavenly altar"}
    ],
    "5": [
      {"type": "allusion", "target": "Ezek 10:2", "note": "Fill your hands with burning coals from between the cherubim and scatter them over the city — Ezekiel's vision of the glory-chariot attendant scattering fire-coals over Jerusalem in judgment is the direct prototype for John's angel filling the censer with altar-fire and hurling it to the earth, signaling the trumpet-judgment sequence to follow"}
    ],
    "7": [
      {"type": "allusion", "target": "Exod 9:23-25", "note": "Moses stretched out his staff toward heaven, and the LORD sent thunder and hail, and fire ran down to the earth — the seventh Egyptian plague (hail and fire mixed) is the explicit exodus-prototype for the first trumpet's hail and fire mixed with blood; Revelation recasts the plagues as cosmic eschatological judgment"},
      {"type": "allusion", "target": "Joel 2:30", "note": "I will show wonders in the heavens and on the earth: blood and fire and columns of smoke — Joel's signs of the Day of the LORD (blood, fire, smoke) converge with John's first-trumpet imagery; the partial destruction (one-third) signals a pre-final judgment warning rather than the end itself"}
    ],
    "8": [
      {"type": "allusion", "target": "Jer 51:25", "note": "I am against you, O destroying mountain, declares the LORD, which destroys the whole earth; I will stretch out my hand against you and roll you down from the crags, and make you a burned mountain — Jeremiah's oracle against Babylon as a 'destroying mountain' thrown down and burned provides the image of a great blazing mountain being cast into the sea"}
    ],
    "11": [
      {"type": "allusion", "target": "Jer 9:15", "note": "I will feed this people with wormwood and give them poisonous water to drink — Jeremiah's covenant-curse of wormwood-poisoning for Israel's apostasy is applied cosmically in Revelation; the star Wormwood poisoning a third of the fresh waters is the Jeremianic curse enacted on an eschatological scale"},
      {"type": "allusion", "target": "Lam 3:15", "note": "He has filled me with bitterness; he has sated me with wormwood — Lamentations' use of wormwood as the taste of divine judgment in the suffering of Jerusalem informs John's naming of the third-trumpet star; the bitterness that tasted like wormwood in the Babylonian exile now falls from heaven as literal cosmic judgment"}
    ],
    "12": [
      {"type": "allusion", "target": "Exod 10:21-23", "note": "Stretch out your hand toward heaven so that darkness may come over the land of Egypt — the ninth Egyptian plague of darkness (three days without light) is the exodus-prototype for the fourth trumpet's striking of a third of the sun, moon, and stars, turning them dark; the partial darkening (one-third) suggests a warning judgment before the full eschatological darkness"},
      {"type": "allusion", "target": "Isa 13:10", "note": "The stars of heaven and their constellations will not flash forth their light; the sun will be dark when it rises and the moon will not shed its light — Isaiah's Day of the LORD oracle against Babylon (sun, moon, and stars darkened) is the prophetic prototype for the fourth trumpet's cosmic dimming"}
    ],
    "13": [
      {"type": "allusion", "target": "Deut 28:49", "note": "The LORD will bring a nation against you from far away, as swift as the eagle flies — the covenant curse of the swooping eagle as divine agent of judgment provides the symbolic background for the eagle flying in midheaven proclaiming three woes; the eagle in both texts signals the arrival of a devastating divine judgment"},
      {"type": "allusion", "target": "Hos 8:1", "note": "Set the trumpet to your lips! Like an eagle over the house of the LORD — Hosea's trumpet-and-eagle combination announces judgment against faithless Israel; John's trumpet-judgment sequence culminating in the woe-eagle draws on the same prophetic pairing of trumpet blast and eagle as heralds of divine judgment"}
    ]
  }
}

if __name__ == '__main__':
    existing = load_echo('revelation')
    merge_echo(existing, REV_ECHO_CH8)
    save_echo('revelation', existing)
    for ch in ['6', '7', '8', '9', '10', '11']:
        has = bool(existing.get(ch, {}))
        entries = sum(len(v) for v in existing.get(ch, {}).values())
        print(f'  ch {ch}: {"present (" + str(entries) + " entries)" if has else "MISSING"}')
    all_present = all(existing.get(ch) for ch in ['6', '7', '8', '9', '10', '11'])
    print('All chapters present' if all_present else 'GAPS remain')
