"""
MKT Revelation chapter 14 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-revelation-14-14.py

Translation decisions:
- G721 (ἀρνίον): "Lamb" (L/M/T) — capitalised throughout as a divine title; consistent
  with all prior Revelation scripts.
- G2342 (θηρίον): "beast" (L/M) / "the Beast" (T) where it functions as a proper title
  (vv. 9, 11) — consistent with mkt-revelation-7-12.py.
- G4151 (πνεῦμα): "Spirit" (capitalised) in v.13 where the Spirit explicitly speaks —
  consistent with mkt-revelation-7-12.py (11:11) and mkt-revelation-19-22.py.
- G166 (αἰώνιος): "eternal" for the adjective εὐαγγέλιον αἰώνιον (v.6); "forever and
  ever" (L/M) / "throughout all the ages of ages" (T) for εἰς αἰῶνας αἰώνων (v.11).
- G3841 (παντοκράτωρ): not present in ch.14; see mkt-revelation-19-22.py for convention.
- G2372 (θυμός): used twice with different nuance — (a) v.8 of Babylon's fornication:
  rendered "passion" (L/M) / "intoxicating passion" (T), capturing the seductive fury
  of her immorality; (b) v.10 of God's anger: "fury" (L/M/T), paired with ὀργή. This
  mirrors the convention at 16:19 "the cup of the wine of the fury of his wrath."
- G3709 (ὀργή): "wrath" (L/M/T) — consistent throughout Revelation.
- G117 (ἄκρατος): v.10 — "unmixed" (L) / "full strength" (M) / "undiluted" (T). Ancient
  wine was always diluted; serving it ἄκρατος (unmixed) conveyed excess and maximally
  potent force. The theological point: God's wrath is not diluted or tempered here.
- G4102 (πίστις) v.12 — "faith of Jesus" (L, preserving the Greek genitive literally) /
  "their faith in Jesus" (M, taking the objective genitive: trust directed toward Jesus) /
  "their faithfulness to Jesus" (T). The genitive is contested (subjective = Jesus's own
  faithfulness; objective = believers' faith in Jesus); in this perseverance context the
  objective reading is slightly preferred for M, but the T surfaces the covenantal
  reciprocity: their holding on to him, and his holding on to them.
- G3933 (παρθένος) v.4 — "virgins" (L/M). In apocalyptic idiom this denotes cultic/
  covenantal purity, not necessarily literal sexual abstinence. T renders the meaning
  explicitly: "those who kept themselves undefiled — their loyalty undivided."
- G536 (ἀπαρχή) v.4 — "firstfruits" (L/M/T). OT priestly term: the dedicated first of
  the harvest, consecrated to God before the rest is used.
- G5619 (υἱὸς ἀνθρώπου) v.14 — "son of man" (L/M); T makes the Daniel 7:13 allusion
  explicit — this is the heavenly figure who receives dominion from the Ancient of Days,
  now carrying a harvest sickle instead of a sword.
- v.8 "Fallen, fallen is Babylon the great" — the doubled cry echoes Isaiah 21:9 and
  Jeremiah 51:8; T notes this intertextual register.
- v.20 1,600 stadia — approximately 185 miles / 300 km. Symbolically matches the
  north-to-south length of Eretz Israel (approx. 200 Roman miles). T surfaces this
  geographical symbolism: the judgment covers the full breadth of the covenanted land.
- G2962 (κύριος): not explicitly present in ch.14; the address "Lord" in v.13 ("saith
  the Lord") follows prior convention — capitalised.
- Divine passive: "was given" forms throughout (vv. 7, 9 etc.) imply divine agency —
  preserved literally in L; M makes God's authority clear by context; T can name the
  agent where helpful.
"""

import json, pathlib

ROOT  = pathlib.Path(__file__).parent.parent
DRAFT = ROOT / 'data' / 'translation' / 'draft'

def load(tier, book):
    p = DRAFT / tier / f'{book}.json'
    if p.exists():
        return json.loads(p.read_text())
    return {}

def save(tier, book, data):
    p = DRAFT / tier / f'{book}.json'
    p.write_text(json.dumps(data, ensure_ascii=False, indent=None))
    print(f'  wrote {p.relative_to(ROOT)}')

def merge_tier(existing, new_data, tier_key):
    for ch, verses in new_data.items():
        if ch not in existing:
            existing[ch] = {}
        for v, tiers in verses.items():
            existing[ch][v] = tiers[tier_key]


REVELATION = {
  "14": {
    "1": {
      "L": "And I looked, and behold, the Lamb standing on Mount Zion, and with him one hundred forty-four thousand, having his name and the name of his Father written on their foreheads.",
      "M": "And I looked, and there was the Lamb standing on Mount Zion, and with him the one hundred forty-four thousand who had his name and his Father's name written on their foreheads.",
      "T": "I looked, and there stood the Lamb on Mount Zion — and with him the hundred forty-four thousand, each bearing on their foreheads the Lamb's own name and the name of his Father. This is the counter-seal to the beast's mark: divine ownership, not imperial bondage."
    },
    "2": {
      "L": "And I heard a voice from heaven like the sound of many waters and like the sound of great thunder, and the voice I heard was like harpists playing on their harps.",
      "M": "And I heard a voice from heaven like the sound of many waters and like the sound of loud thunder, and the voice I heard was like harpists playing their harps.",
      "T": "From heaven came a sound that was rushing water and rolling thunder at once — immense and layered — and woven through it the intimate clarity of harpers plucking their strings."
    },
    "3": {
      "L": "And they sing as it were a new song before the throne and before the four living creatures and the elders; and no one was able to learn the song except the one hundred forty-four thousand who had been redeemed from the earth.",
      "M": "And they were singing something like a new song before the throne and before the four living creatures and the elders, and no one was able to learn that song except the one hundred forty-four thousand who had been redeemed from the earth.",
      "T": "Before the throne and the four living creatures and the elders they sang — something no one else could learn, a new song shaped by what they had come through. Only the redeemed from the earth carried this music in them."
    },
    "4": {
      "L": "These are those who were not defiled with women, for they are virgins; these follow the Lamb wherever he goes; these were redeemed from among men as firstfruits to God and to the Lamb.",
      "M": "These are those who have not defiled themselves with women, for they are virgins. They follow the Lamb wherever he goes. They were redeemed from among humanity as firstfruits to God and to the Lamb.",
      "T": "These are those who kept themselves undefiled — virgins in the covenantal sense, their loyalty wholly undivided. They follow the Lamb wherever he leads, no other lord having any claim on them. They were purchased from humanity as the first of the harvest, consecrated entirely to God and to the Lamb."
    },
    "5": {
      "L": "And in their mouth was found no lie; they are blameless.",
      "M": "And in their mouth no lie was found; they are blameless.",
      "T": "No falsehood was ever found on their lips. They stand without blemish before God — a priestly community that bore the truth even when truth was costly."
    },
    "6": {
      "L": "And I saw another angel flying in midheaven, having an eternal gospel to preach to those who dwell on the earth, and to every nation and tribe and language and people,",
      "M": "Then I saw another angel flying directly overhead, carrying an eternal gospel to proclaim to those who dwell on the earth — to every nation and tribe and language and people.",
      "T": "Then I saw another angel cutting through the middle of the sky, bearing good news that will never expire — the eternal gospel — carried to every nation, every tribe, every language, every people on earth."
    },
    "7": {
      "L": "saying with a great voice, 'Fear God and give him glory, because the hour of his judgment has come; and worship him who made the heaven and the earth and the sea and the springs of water.'",
      "M": "He said with a loud voice, 'Fear God and give him glory, for the hour of his judgment has come! Worship him who made heaven and earth, the sea and the springs of water.'",
      "T": "'Fear God! Give him the glory he deserves — for the hour of his judgment has arrived. Worship the one who made the sky, the earth, the sea, and every spring of water.' This is the gospel stripped to its core: the Creator claims what belongs to him."
    },
    "8": {
      "L": "And another angel, a second, followed, saying, 'Fallen, fallen is Babylon the great, she who made all the nations drink of the wine of the passion of her sexual immorality.'",
      "M": "A second angel followed, saying, 'Fallen, fallen is Babylon the great — the city that made all the nations drink the wine of the passion of her sexual immorality.'",
      "T": "'Fallen! Fallen is Babylon the great!' — the cry doubles on itself like a death-knell, echoing Isaiah and Jeremiah before it. She who seduced the nations with the intoxicating passion of her corruption has fallen at last."
    },
    "9": {
      "L": "And another angel, a third, followed them, saying with a loud voice, 'If anyone worships the beast and his image, and receives a mark on his forehead or on his hand,'",
      "M": "Then a third angel followed them, saying with a loud voice, 'If anyone worships the beast and its image and receives a mark on his forehead or on his hand,'",
      "T": "A third angel followed, proclaiming at full volume: 'If anyone bows down to the Beast and its image, and takes its mark on forehead or hand —'"
    },
    "10": {
      "L": "he also shall drink of the wine of the wrath of God, poured unmixed in the cup of his fury; and he shall be tormented with fire and brimstone in the presence of the holy angels and in the presence of the Lamb.",
      "M": "he will also drink the wine of God's wrath, poured full strength into the cup of his fury, and he will be tormented with fire and sulfur in the presence of the holy angels and in the presence of the Lamb.",
      "T": "'— that person will drink the undiluted wine of God's wrath, poured at full force into the cup of his fury, and will be tormented with fire and sulfur before the holy angels and before the Lamb himself. There is no dilution here, no mercy cut with water.'"
    },
    "11": {
      "L": "And the smoke of their torment ascends forever and ever; and they have no rest day or night, those who worship the beast and his image, and whoever receives the mark of his name.",
      "M": "And the smoke of their torment ascends forever and ever. They have no rest, day or night — those who worship the beast and its image, and anyone who receives the mark of its name.",
      "T": "The smoke of that torment rises throughout all the ages of ages. No rest, day or night — not for those who worship the Beast and its image, not for anyone who wears the brand of its name."
    },
    "12": {
      "L": "Here is the patient endurance of the saints, those who keep the commandments of God and the faith of Jesus.",
      "M": "Here is a call for the patient endurance of the saints — those who keep the commandments of God and their faith in Jesus.",
      "T": "This is the summons to the saints' steadfast endurance: hold fast to God's commandments, and hold fast to your faithfulness to Jesus. His faithfulness answers yours."
    },
    "13": {
      "L": "And I heard a voice from heaven saying, 'Write: Blessed are the dead who die in the Lord from now on.' 'Yes,' says the Spirit, 'that they may rest from their labors; for their deeds follow them.'",
      "M": "And I heard a voice from heaven saying, 'Write: Blessed are the dead who die in the Lord from now on.' 'Yes,' says the Spirit, 'so that they may rest from their labors, for their deeds follow them.'",
      "T": "'Write this down: blessed are those who die in the Lord from this moment forward.' The Spirit answers: 'Yes — let them rest from everything they have endured, for all that they have done comes with them.'"
    },
    "14": {
      "L": "And I looked, and behold, a white cloud, and seated on the cloud one like a son of man, having on his head a golden crown and in his hand a sharp sickle.",
      "M": "Then I looked, and there was a white cloud, and seated on the cloud was one like a son of man, with a golden crown on his head and a sharp sickle in his hand.",
      "T": "I looked and saw a white cloud, and enthroned upon it one who looked like a son of man — Daniel's figure come to his hour, the one who receives dominion from the Ancient of Days. A golden crown crowned his head; in his hand, a sharp sickle."
    },
    "15": {
      "L": "And another angel came out of the temple, crying out with a loud voice to him who sat on the cloud, 'Put in your sickle and reap, for the hour to reap has come, because the harvest of the earth is ripe.'",
      "M": "Then another angel came out of the temple, calling with a loud voice to him who sat on the cloud, 'Put in your sickle and reap, for the hour to reap has come, for the harvest of the earth is fully ripe.'",
      "T": "An angel emerged from the temple and called out to the one on the cloud: 'Drive in your sickle and harvest — the hour has come, the earth's crop has reached full ripeness and stands ready for the blade.'"
    },
    "16": {
      "L": "And he who sat on the cloud swung his sickle over the earth, and the earth was reaped.",
      "M": "So he who sat on the cloud swung his sickle over the earth, and the earth was reaped.",
      "T": "The one on the cloud drove his sickle through the earth, and the harvest was gathered."
    },
    "17": {
      "L": "And another angel came out of the temple which is in heaven, he also having a sharp sickle.",
      "M": "Then another angel came out of the temple in heaven, and he too had a sharp sickle.",
      "T": "From the heavenly temple came another angel, and he too carried a sharp sickle."
    },
    "18": {
      "L": "And another angel came out from the altar, the one having authority over the fire, and he called with a loud voice to him who had the sharp sickle, saying, 'Put in your sharp sickle and gather the clusters of the vine of the earth, for its grapes are ripe.'",
      "M": "And another angel came out from the altar — the angel who has authority over fire — and he called with a loud voice to the one who had the sharp sickle, 'Put in your sharp sickle and gather the clusters from the vine of the earth, for its grapes are fully ripe.'",
      "T": "From the altar came another angel — the one with authority over fire — and he cried out to the angel with the sharp sickle: 'Swing your sickle; gather the grape clusters from the earth's vine, for the grapes hang at full ripeness, dark and swollen with what is coming.'"
    },
    "19": {
      "L": "So the angel swung his sickle to the earth and gathered the vintage of the earth, and threw it into the great winepress of the wrath of God.",
      "M": "So the angel swung his sickle over the earth and gathered the grape harvest of the earth and threw it into the great winepress of God's wrath.",
      "T": "The angel drove his sickle through the earth's vineyard, gathered all the vintage, and hurled it into the great winepress of God's fury."
    },
    "20": {
      "L": "And the winepress was trodden outside the city, and blood came out of the winepress up to the horses' bridles, for the distance of one thousand six hundred stadia.",
      "M": "And the winepress was trodden outside the city, and blood flowed from the winepress as high as a horse's bridle, for a distance of 1,600 stadia.",
      "T": "The winepress was trodden outside the city, and blood poured out of it all the way up to the horses' bridles across a distance of sixteen hundred stadia — a river of judgment stretching the full length of the land, from its northernmost edge to its southernmost, leaving nothing untouched."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'revelation')
        merge_tier(existing, REVELATION, tier_key)
        save(tier_dir, 'revelation', existing)
    print('Revelation 14 written.')

if __name__ == '__main__':
    main()
