"""
MKT Revelation chapters 16–18 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-revelation-16-18.py

Translation decisions (carrying forward from mkt-revelation-1-2.py conventions):

- G4204 (πόρνη): "prostitute" (L/M) — consistent and accurate; T may use "whore" where the
  covenantal-betrayal and power-over-nations dimension is foregrounded (17:1, 17:5, 17:15).
  The Greek word carries both the sexual and the patron-exploitation senses.

- G4202 (πορνεία): "sexual immorality" (M); "fornication" (L, word-for-word); T renders by
  meaning — "immorality," "corruption," "adulteries." In 18:3 the phrase is "τοῦ θυμοῦ τῆς
  πορνείας αὐτῆς" — the θυμός here is passion/desire, not judicial wrath: rendered "the
  burning passion of her corruption."

- G2372 (θυμός) vs G3709 (ὀργή): Both rendered "wrath" in L/M where English needs one word.
  In 16:1 "τοῦ θυμοῦ τοῦ θεοῦ" = passionate, burning fury: T "burning wrath."
  In 16:19 both terms are stacked — "τοῦ θυμοῦ τῆς ὀργῆς αὐτοῦ" = fury-of-his-wrath:
  L/M "the fury of his wrath"; T "his fierce, burning wrath."

- G4151 (πνεῦμα): lowercase "spirits" for demonic spirits (16:13–14; 18:2); uppercase "Spirit"
  for the Holy Spirit (17:3 — "in the Spirit"). Consistent with chs 1–2.

- G3841 (παντοκράτωρ): "Almighty" (L/M); "All-Sovereign" (T) — consistent with chs 1–2.

- G3466 (μυστήριον): "Mystery" used as part of the woman's title in 17:5 — treated as a proper
  label in L (all-caps as in the text); M "a mystery: 'Babylon the Great…'"; T surfaces that the
  word marks it as a divine secret being decoded.

- G5478 (Χαλδαῖος) / Ἁρμαγεδών (16:16): Transliterated as "Armageddon"; T notes it is the
  Hebrew "Har Megiddo" (Mountain of Megiddo), the storied plain of Israel's great battles.

- G4983 (σῶμα) + G5590 (ψυχή) in 18:13: "bodies and souls of men" = human beings traded as
  slaves. L renders literally; M "human beings sold as slaves"; T makes the horror explicit:
  "human beings — bodies and souls bought and sold."

- "Thyine wood" (G2367 θύινον, 18:12): citron/thuja wood — a fragrant North African timber
  prized by Roman aristocrats. Rendered "citron wood" (L/M) / "precious citron timber" (T).

- Aspect notes specific to these chapters:
  - 16:9,11 "they did not repent" — aorist: a completed, specific refusal at each plague.
  - 17:2 "have been made drunk" (πεπότισται, perfect passive): they are and remain intoxicated —
    the ongoing state is part of the indictment.
  - 17:14 "the Lamb will conquer" (νικήσει, future): a certain future act stated with confidence.
  - 18:2 "she has become" (γέγονεν, perfect): past collapse, permanently settled.
  - 18:5 "her sins have reached heaven" (ἐκολλήθησαν, aorist): completed accumulation.
  - 18:20 "God has judged" (ἔκρινεν, aorist): specific completed verdict — the legal-vindication
    sense is prominent; T surfaces the courtroom imagery.

- OT intertextuality:
  - 16:2: Exodus 9:10–11 (plague of boils on Egypt). T notes the Exodus echo.
  - 16:5–7: The angel-of-waters doxology echoes Deut 32 (God's righteous judgments). T surfaces.
  - 16:12: Cyrus the Great dried up the Euphrates to conquer Babylon (Isa 44:27–45:1) — the
    sixth bowl uses that same geography; T notes this.
  - 16:15: Echoes of Matt 24:43; 1 Thess 5:2 — "thief" language for the parousia. T surfaces.
  - 16:19: Jer 25:15–17 (the cup of wrath given to the nations). T notes.
  - 17:1–5: Jer 51 (Babylon the great prostitute seated on many waters). T notes Jeremiah.
  - 18:2: Isa 13:21; 34:14 (Babylon as haunt of wild creatures after its fall). T notes Isaiah.
  - 18:4: Jer 51:45; Isa 48:20 — the call "Come out of her, my people." T notes both echoes.
  - 18:6: Jer 50:29 ("repay her according to her work"). T notes.
  - 18:7: Isa 47:7–8 (Babylon's boast: "I shall be queen forever"). T quotes Isaiah.
  - 18:21: Jer 51:63–64 (the prophet Seraiah throws a stone into the Euphrates as a sign of
    Babylon's sinking). T explicitly echoes Jeremiah.
  - 18:22–23: Jer 7:34; 16:9 (silence of bride-and-groom voices as a sign of judgment). T notes.

- Capitalization carried forward from chs 1–2:
  "Spirit" (divine); "Death and Hades" (personalised powers); "King of kings and Lord of lords"
  (titles); "Book of Life" (proper title); "Abyss" (proper designation).
  The woman's forehead inscription in 17:5 rendered in SMALL CAPS in L, M; T decodes it.
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
  "16": {
    "1": {
      "L": "And I heard a great voice out of the temple saying to the seven angels, 'Go and pour out the seven bowls of the wrath of God upon the earth.'",
      "M": "Then I heard a loud voice from the temple saying to the seven angels, 'Go and pour out the seven bowls of God's wrath on the earth.'",
      "T": "A great voice thundered out of the temple, commanding the seven angels: 'Go — pour out the seven bowls of God's burning wrath upon the earth.'"
    },
    "2": {
      "L": "And the first went and poured out his bowl upon the earth, and there fell a foul and painful sore upon the people who had the mark of the beast and who worshipped his image.",
      "M": "The first angel went and poured out his bowl on the land, and ugly, festering sores broke out on the people who had the mark of the beast and who worshiped its image.",
      "T": "The first angel emptied his bowl onto the earth. Vile, festering ulcers erupted on every person who bore the beast's mark and bowed in worship before its image — the same judgment the sixth plague brought on Egypt's magicians who could not stand before Moses."
    },
    "3": {
      "L": "The second angel poured out his bowl upon the sea, and it became blood, like that of a dead man, and every living soul in the sea died.",
      "M": "The second angel poured out his bowl on the sea, and it turned into blood like that of a dead person. Every living creature in the sea died.",
      "T": "The second angel emptied his bowl into the sea. It thickened into blood — dark and congealed, like the blood of a corpse. Every living creature in the sea perished."
    },
    "4": {
      "L": "The third angel poured out his bowl upon the rivers and the springs of water, and they became blood.",
      "M": "The third angel poured out his bowl on the rivers and springs of water, and they became blood.",
      "T": "The third angel emptied his bowl over the rivers and the springs. Every source of fresh water turned to blood."
    },
    "5": {
      "L": "And I heard the angel of the waters saying, 'You are righteous, O Lord, the one who is and who was, the Holy One, because you have judged in this way.'",
      "M": "Then I heard the angel in charge of the waters say: 'You are just in these judgments, you who are and who were, the Holy One, because you have judged in this way.'",
      "T": "The angel who presides over the waters cried out: 'Your judgments are righteous, O Lord — you who are and who were, the Holy One. These judgments are exactly right.'"
    },
    "6": {
      "L": "'For they shed the blood of saints and prophets, and you have given them blood to drink — they are worthy of it.'",
      "M": "'For they poured out the blood of your saints and prophets, and you have given them blood to drink. They deserve it.'",
      "T": "'They spilled the blood of your saints and prophets — so you have made them drink blood. The punishment fits the crime. Justice has been served.'"
    },
    "7": {
      "L": "And I heard the altar saying, 'Yes, Lord God Almighty, true and righteous are your judgments.'",
      "M": "And I heard the altar respond: 'Yes, Lord God Almighty, your judgments are true and just.'",
      "T": "The altar itself added its voice: 'Yes — Lord God, the All-Sovereign. True. Just. Every judgment you make.' The altar that once sheltered martyred souls crying for vindication now bears witness that justice has finally come."
    },
    "8": {
      "L": "The fourth angel poured out his bowl upon the sun, and it was given to it to scorch people with fire.",
      "M": "The fourth angel poured out his bowl on the sun, and the sun was given power to scorch people with fire.",
      "T": "The fourth angel emptied his bowl on the sun. Power was granted to it to sear people with scorching heat."
    },
    "9": {
      "L": "And people were scorched with great heat, and they blasphemed the name of God who has authority over these plagues, and they did not repent to give him glory.",
      "M": "People were scorched by the intense heat and they blasphemed the name of God, who had authority over these plagues. They refused to repent and give him glory.",
      "T": "They were burned with searing heat — yet they cursed the name of God who held power over these plagues. They would not turn back. They refused to give him glory. The refusal was deliberate and final."
    },
    "10": {
      "L": "The fifth angel poured out his bowl upon the throne of the beast, and his kingdom was plunged into darkness. People gnawed their tongues in agony,",
      "M": "The fifth angel poured out his bowl on the throne of the beast, and its kingdom was plunged into darkness. People gnawed their tongues in agony",
      "T": "The fifth angel emptied his bowl on the beast's very throne. Darkness swallowed its kingdom whole. People bit their tongues in torment —"
    },
    "11": {
      "L": "and they blasphemed the God of heaven because of their pains and their sores, and they did not repent of their deeds.",
      "M": "and cursed the God of heaven because of their pain and their sores. They refused to repent of what they had done.",
      "T": "— and still they cursed the God of heaven for their suffering and their sores. Still they would not repent. Not once."
    },
    "12": {
      "L": "The sixth angel poured out his bowl upon the great river Euphrates, and its water was dried up, to prepare the way for the kings from the east.",
      "M": "The sixth angel poured out his bowl on the great river Euphrates, and its water was dried up to prepare the way for the kings from the East.",
      "T": "The sixth angel emptied his bowl on the great Euphrates. The river went dry — drained to its bed — to open the road for the kings advancing from the East. As God once used Cyrus to drain the Euphrates and enter Babylon, so the great reversal now unfolds."
    },
    "13": {
      "L": "And I saw, coming out of the mouth of the dragon and out of the mouth of the beast and out of the mouth of the false prophet, three unclean spirits like frogs.",
      "M": "Then I saw three impure spirits that looked like frogs come out of the mouth of the dragon, out of the mouth of the beast, and out of the mouth of the false prophet.",
      "T": "Then from the mouth of the dragon, from the mouth of the beast, and from the mouth of the false prophet came three foul spirits — grotesque as frogs. The unholy trinity speaks, and only filth comes out."
    },
    "14": {
      "L": "For they are spirits of demons, performing signs, who go out to the kings of the whole inhabited world, to assemble them for the battle on the great day of God Almighty.",
      "M": "They are demonic spirits that perform miraculous signs, going out to the kings of the whole world to assemble them for battle on the great day of God Almighty.",
      "T": "These are demonic spirits working miracles, going out to every king on earth, herding them toward the great final battle — the day of reckoning of the All-Sovereign God."
    },
    "15": {
      "L": "'Behold, I am coming like a thief. Blessed is the one who stays awake and keeps his garments, so that he may not walk about naked and be seen in his shame.'",
      "M": "'Look, I come like a thief! Blessed is the one who remains awake and keeps his clothes, so as not to go naked and be shamefully exposed.'",
      "T": "'Watch — I am coming unannounced, like a thief. The person who stays alert and keeps his robe on is blessed. You do not want to be caught naked and shamed when I arrive.' Christ's own voice breaks into the vision — a sudden call to vigilance in the midst of gathering catastrophe."
    },
    "16": {
      "L": "And they assembled them at the place called in Hebrew Armageddon.",
      "M": "Then they gathered the kings to the place that in Hebrew is called Armageddon.",
      "T": "And so the kings were assembled at the place the Hebrew calls Armageddon — Har Megiddo, the Mountain of Megiddo, the ancient plain where Israel's great battles have always been decided."
    },
    "17": {
      "L": "The seventh angel poured out his bowl into the air, and a great voice came out of the temple, from the throne, saying, 'It is done!'",
      "M": "The seventh angel poured out his bowl into the air, and a loud voice came from the throne, out of the temple, saying, 'It is done!'",
      "T": "The seventh angel emptied his bowl into the air itself. From the throne, from the temple, came the great voice: 'It is accomplished — finished and sealed.' The perfect tense announces what can never be undone."
    },
    "18": {
      "L": "And there were flashes of lightning and rumblings and peals of thunder, and there was a great earthquake such as there had never been since man came to be upon the earth, so great and so mighty was that earthquake.",
      "M": "Then came flashes of lightning, rumblings, peals of thunder, and a severe earthquake — no earthquake like it has ever occurred since mankind has been on earth. It was so tremendous.",
      "T": "Lightning blazed. Thunder crashed. Voices rang out. Then the earth itself was torn apart — an earthquake unlike anything in human history, monstrous in scale, unprecedented in violence."
    },
    "19": {
      "L": "The great city was split into three parts, and the cities of the nations fell, and God remembered great Babylon, to give her the cup of the wine of the fury of his wrath.",
      "M": "The great city split into three parts, and the cities of the nations collapsed. God remembered great Babylon and gave her the cup filled with the wine of the fury of his wrath.",
      "T": "The great city fractured into three pieces. The cities of the nations crumbled and fell. And God — he had not forgotten Babylon the great. He brought the cup to her lips: the wine of his fierce and burning wrath, the cup of the nations' judgment that Jeremiah had long foretold."
    },
    "20": {
      "L": "And every island fled away, and no mountains were to be found.",
      "M": "Every island fled away and the mountains could no longer be found.",
      "T": "Every island vanished. The mountains themselves — gone. The created order was coming undone."
    },
    "21": {
      "L": "And great hailstones, about the weight of a talent, fell from heaven on people, and they blasphemed God because of the plague of the hail, for the plague was exceedingly severe.",
      "M": "From the sky huge hailstones, each weighing about a hundred pounds, fell on people. And they cursed God on account of the plague of hail, because the plague was so terrible.",
      "T": "Hailstones plummeted from the sky — each as heavy as a talent, nearly a hundred pounds of ice. People were crushed by them, yet even then they hurled curses at God. The plague was catastrophic, and still they would not relent."
    }
  },
  "17": {
    "1": {
      "L": "And one of the seven angels who had the seven bowls came and spoke with me, saying, 'Come, I will show you the judgment of the great prostitute who is seated on many waters,'",
      "M": "One of the seven angels who had the seven bowls came and said to me, 'Come, I will show you the punishment of the great prostitute, who sits enthroned over many waters.'",
      "T": "One of the seven bowl-angels came to me: 'Come — I will show you the verdict that is coming against the great whore, the one who sits enthroned over the many waters.' The imagery echoes Jeremiah 51 — Babylon the great, seated on the Euphrates."
    },
    "2": {
      "L": "'With her the kings of the earth have committed fornication, and the inhabitants of the earth have been made drunk with the wine of her fornication.'",
      "M": "'The kings of the earth committed adultery with her, and the inhabitants of the earth were made drunk on the wine of her immorality.'",
      "T": "'Every king on earth has gone to bed with her. The world's population has been drunk — and remains drunk — stupefied on the wine of her corruption. They have been intoxicated and have never sobered up.'"
    },
    "3": {
      "L": "And he carried me away in the Spirit into a wilderness, and I saw a woman sitting on a scarlet beast that was full of blasphemous names, having seven heads and ten horns.",
      "M": "Then the angel carried me away in the Spirit into a wilderness. There I saw a woman sitting on a scarlet beast covered with blasphemous names and having seven heads and ten horns.",
      "T": "The Spirit swept me away into a desert wasteland. There I saw a woman mounted on a scarlet beast — the beast plastered from head to tail with names that blasphemed God. It had seven heads and ten horns."
    },
    "4": {
      "L": "The woman was arrayed in purple and scarlet, and adorned with gold and precious stones and pearls, holding in her hand a golden cup full of abominations and the impurities of her sexual immorality.",
      "M": "The woman was dressed in purple and scarlet and glittered with gold, precious stones, and pearls. She held a golden cup in her hand, filled with abominable things and the filth of her adulteries.",
      "T": "The woman blazed in imperial purple and scarlet, glittering with gold, jewels, and pearls. In her hand she held a golden cup — beautiful on the outside, filled inside with the vile corruption of her immorality."
    },
    "5": {
      "L": "And on her forehead a name was written: 'MYSTERY, BABYLON THE GREAT, THE MOTHER OF PROSTITUTES AND OF THE EARTH'S ABOMINATIONS.'",
      "M": "On her forehead was written a name — a mystery: 'Babylon the Great, the Mother of Prostitutes and of the Abominations of the Earth.'",
      "T": "Branded across her forehead was a name — marked as a mystery to be decoded: BABYLON THE GREAT, MOTHER OF PROSTITUTES AND OF ALL THE EARTH'S ABOMINATIONS. The city that persecutes the saints is identified."
    },
    "6": {
      "L": "And I saw the woman, drunk with the blood of the saints and with the blood of the witnesses of Jesus. When I saw her, I marveled greatly.",
      "M": "I saw that the woman was drunk with the blood of God's holy people and the blood of those who bore testimony to Jesus. When I saw her, I was greatly astonished.",
      "T": "She was drunk — drunk with the blood of God's people, drunk with the blood of those who had died bearing witness to Jesus. The sight of her brought me to a complete stop. I was overcome with astonishment and horror."
    },
    "7": {
      "L": "And the angel said to me, 'Why do you marvel? I will tell you the mystery of the woman, and of the beast with seven heads and ten horns that carries her.'",
      "M": "Then the angel said to me: 'Why are you astonished? I will explain to you the mystery of the woman and of the beast she rides, which has the seven heads and ten horns.'",
      "T": "'Why are you so astonished?' the angel asked. 'I will disclose the hidden meaning: the woman, and the beast that is carrying her — the one with the seven heads and ten horns.'"
    },
    "8": {
      "L": "The beast that you saw was, and is not, and is about to ascend from the bottomless pit and go to destruction. And the inhabitants of the earth whose names have not been written in the book of life from the foundation of the world will marvel when they see the beast, because it was and is not and will come.",
      "M": "The beast you saw once was, now is not, and yet will come up out of the Abyss and go to its destruction. The inhabitants of the earth whose names have not been written in the book of life from the creation of the world will be astonished when they see the beast, because it once was, now is not, and yet will come.",
      "T": "The beast you saw was once present, then absent, and is now rising out of the Abyss — only to plunge toward its destruction. The people of the earth, all those whose names were never written in the Book of Life from before the world's foundation, will be thunderstruck when they see it: 'It was, and it was not, and now it is again.' A counterfeit of God's own eternal name — but this one is headed for ruin."
    },
    "9": {
      "L": "This calls for a mind with wisdom: the seven heads are seven mountains on which the woman is seated;",
      "M": "This calls for a mind with wisdom. The seven heads are seven hills on which the woman sits.",
      "T": "Here the reader needs wisdom to decode the image: the seven heads are seven hills — and the city built on seven hills, where this woman sits enthroned, was unmistakable to any first-century reader."
    },
    "10": {
      "L": "they are also seven kings, five of whom have fallen, one is, the other has not yet come, and when he comes he must remain only a little while.",
      "M": "They are also seven kings. Five have fallen, one is reigning, and the other has not yet come. But when he does come, he must remain for only a short time.",
      "T": "They are also seven kings: five already fallen, one now reigning, one still to come — but when that last one arrives, his time will be cut short."
    },
    "11": {
      "L": "And the beast that was and is not, it is an eighth and is one of the seven, and it goes to destruction.",
      "M": "The beast who once was and now is not is an eighth king. He belongs to the seven and is going to his destruction.",
      "T": "The beast itself — the one that was and is not — is an eighth king, rising from the seven and sharing their nature. But its destiny is fixed: destruction."
    },
    "12": {
      "L": "And the ten horns that you saw are ten kings who have not yet received a kingdom, but they receive authority as kings for one hour, together with the beast.",
      "M": "The ten horns you saw are ten kings who have not yet received a kingdom, but who for one hour will receive authority as kings along with the beast.",
      "T": "The ten horns are ten kings who hold no throne yet — but they will receive royal authority for a single hour, alongside the beast. Real power, but temporary."
    },
    "13": {
      "L": "These are of one mind, and they hand over their power and authority to the beast.",
      "M": "They have one purpose and will give their power and authority to the beast.",
      "T": "They are completely unified in purpose — every one of them handing their strength and authority to the beast."
    },
    "14": {
      "L": "They will make war on the Lamb, and the Lamb will conquer them, because he is Lord of lords and King of kings, and those with him are called and chosen and faithful.",
      "M": "They will wage war against the Lamb, but the Lamb will triumph over them because he is Lord of lords and King of kings — and with him will be his called, chosen, and faithful followers.",
      "T": "They will go to war against the Lamb — but the Lamb will conquer. He is Lord of lords and King of kings. Those who stand with him are the called, the chosen, the faithful."
    },
    "15": {
      "L": "And he said to me, 'The waters that you saw, where the prostitute is seated, are peoples and multitudes and nations and languages.'",
      "M": "Then the angel said to me, 'The waters you saw, where the prostitute sits, are peoples, multitudes, nations, and languages.'",
      "T": "'The waters you saw — where the prostitute sits,' the angel told me, 'represent peoples, multitudes, nations, and languages — every corner of humanity under her dominion.'"
    },
    "16": {
      "L": "And the ten horns that you saw and the beast, these will hate the prostitute, and will make her desolate and naked, and will devour her flesh and burn her up with fire.",
      "M": "The beast and the ten horns you saw will hate the prostitute. They will bring her to ruin and leave her naked; they will devour her flesh and burn her with fire.",
      "T": "The very beast and the ten kings who served her will turn on her. Their lust will curdle into hatred. They will strip her bare, leave her desolate, devour her like flesh, and burn what remains. God's purpose works even through the violence of enemies."
    },
    "17": {
      "L": "For God has put it into their hearts to carry out his purpose by being of one mind and handing over their royal power to the beast, until the words of God are fulfilled.",
      "M": "For God has put it into their hearts to accomplish his purpose by agreeing to hand over their royal power to the beast, until God's words are fulfilled.",
      "T": "For God himself planted this in their hearts — to serve his hidden purpose, to be of one mind, to give their power to the beast — all of this playing out until every word of God is accomplished. History's violence is not beyond his control."
    },
    "18": {
      "L": "And the woman that you saw is the great city that has dominion over the kings of the earth.",
      "M": "The woman you saw is the great city that rules over the kings of the earth.",
      "T": "The woman you saw is the great city — the one that holds dominion over every king on earth. The vision has been decoded."
    }
  },
  "18": {
    "1": {
      "L": "After this I saw another angel coming down from heaven, having great authority, and the earth was illuminated by his glory.",
      "M": "After this I saw another angel coming down from heaven. He had great authority, and the earth was lit up with his splendor.",
      "T": "Then another angel descended from heaven — great in authority, blazing with radiance. His glory was so overwhelming it illuminated the whole earth."
    },
    "2": {
      "L": "And he cried out with a mighty voice, saying, 'Fallen, fallen is Babylon the great! She has become a dwelling place of demons, a haunt for every unclean spirit, a cage for every hateful and unclean bird.'",
      "M": "With a mighty voice he shouted: 'Fallen! Fallen is Babylon the Great! She has become a dwelling place for demons and a haunt for every impure spirit, a cage for every hateful and unclean bird.'",
      "T": "'Fallen! Fallen! Babylon the Great has fallen!' he thundered. 'She has become the home of demons, a den for every foul spirit, a prison for every hateful and unclean bird.' The language of Isaiah's Babylon prophecy now finds its ultimate fulfillment."
    },
    "3": {
      "L": "For all the nations have drunk from the wine of the passion of her sexual immorality, and the kings of the earth have committed fornication with her, and the merchants of the earth have grown rich from the power of her luxurious living.",
      "M": "For all the nations have drunk the maddening wine of her adulteries. The kings of the earth committed adultery with her, and the merchants of the earth grew rich from her excessive luxuries.",
      "T": "Every nation has drunk deep of her intoxicating corruption. The world's kings were in bed with her. The world's merchants grew obscenely wealthy off her insatiable appetite for luxury."
    },
    "4": {
      "L": "Then I heard another voice from heaven saying, 'Come out from her, my people, lest you take part in her sins, lest you receive her plagues.'",
      "M": "Then I heard another voice from heaven say: 'Come out of her, my people, so that you will not share in her sins or receive any of her plagues.'",
      "T": "Then another voice from heaven: 'My people — get out of her now. Leave before you become entangled in her sins and share the plagues that are coming to her.' The same call God gave through Jeremiah and Isaiah: come out of Babylon, come home."
    },
    "5": {
      "L": "'For her sins have been heaped up as high as heaven, and God has remembered her iniquities.'",
      "M": "'For her sins are piled up to heaven, and God has remembered her crimes.'",
      "T": "'Her sins have been stacking up until they have reached heaven itself — and God has not forgotten a single one.'"
    },
    "6": {
      "L": "'Pay her back as she herself has paid others, and repay her double according to her deeds. Mix a double portion for her in the cup she mixed.'",
      "M": "'Give back to her as she has given; repay her double for what she has done. Mix a double portion for her in the cup she mixed for others.'",
      "T": "'Return to her what she dealt out — double it. She made others drink from her cup; fill it twice over for her. As Jeremiah commanded concerning Babylon, so now the sentence falls.'"
    },
    "7": {
      "L": "'As much as she glorified herself and lived in luxury, give her a like measure of torment and grief. Since she says in her heart, \"I sit as a queen, I am no widow, and I will never see grief,\"'",
      "M": "'Give her as much torment and grief as the glory and luxury she gave herself. In her heart she boasts: \"I sit as queen. I am no widow and I will never mourn.\"'",
      "T": "'She gloried in herself and wallowed in luxury — repay her with the same measure of anguish and grief. She sits in her own mind on an eternal throne: \"I am queen forever. I will never be a widow. Sorrow will never find me.\" This is Isaiah's Babylon speaking — and now Isaiah's judgment falls.'"
    },
    "8": {
      "L": "'Therefore in a single day her plagues will come — death and mourning and famine — and she will be burned up with fire, for mighty is the Lord God who judges her.'",
      "M": "'Therefore in one day her plagues will overtake her: death, mourning, and famine. She will be consumed by fire, for mighty is the Lord God who judges her.'",
      "T": "'So in a single day it all arrives at once: disease, grief, famine, fire. She will be consumed. The Lord God who judges her is the All-Sovereign — and he does not delay.'"
    },
    "9": {
      "L": "And the kings of the earth, who committed fornication and lived in luxury with her, will weep and wail over her when they see the smoke of her burning,",
      "M": "When the kings of the earth who committed adultery with her and shared her luxury see the smoke of her burning, they will weep and wail over her.",
      "T": "The kings of the earth — those who shared her bed and wallowed in her luxury — will watch the smoke rising from her ruins and weep and beat their breasts in grief."
    },
    "10": {
      "L": "standing far off in fear of her torment, saying, 'Alas! Alas! You great city, you mighty city, Babylon! For in a single hour your judgment has come.'",
      "M": "Terrified at her torment, they will stand far off and cry: 'Woe! Woe to you, great city, you mighty city of Babylon! In one hour your doom has come!'",
      "T": "Too terrified to come near, they stand at a distance and cry out: 'Woe! Woe, you great city — Babylon, city of power! Your sentence came in a single hour.'"
    },
    "11": {
      "L": "And the merchants of the earth weep and mourn for her, since no one buys their cargo anymore —",
      "M": "The merchants of the earth will weep and mourn over her because no one buys their cargo anymore —",
      "T": "The merchants of the world weep and grieve — because no one is buying their goods anymore. The whole economy built on her appetite has collapsed in an instant."
    },
    "12": {
      "L": "cargo of gold, silver, precious stones, and pearls, fine linen, purple cloth, silk, and scarlet cloth, all kinds of citron wood, all kinds of articles of ivory, all kinds of articles of costly wood, bronze, iron, and marble,",
      "M": "cargo of gold, silver, precious stones, and pearls; fine linen, purple, silk, and scarlet cloth; every sort of citron wood, and articles of every kind made of ivory, costly wood, bronze, iron, and marble;",
      "T": "Gold and silver, jewels and pearls. Fine linen, purple, silk, and scarlet. Fragrant citron wood and every kind of carved ivory, rare timber, bronze, iron, and marble."
    },
    "13": {
      "L": "cinnamon, spice, incense, myrrh, and frankincense, wine, oil, fine flour, and wheat, cattle and sheep, horses and carriages, and bodies and souls of men.",
      "M": "cinnamon and spice, incense, myrrh, and frankincense, wine and olive oil, fine flour and wheat; cattle and sheep; horses and carriages; and human beings sold as slaves.",
      "T": "Cinnamon, spice, incense, myrrh, and frankincense. Wine and oil, fine flour and wheat. Livestock — cattle and sheep. Horses and carriages. And last of all, at the bottom of the list: human beings — bodies and souls bought and sold. The empire's luxury rests on human trafficking."
    },
    "14": {
      "L": "'The fruit your soul longed for has gone from you, and all your delicacies and splendors have perished from you, never to be found again.'",
      "M": "'They will say, \"The fruit you longed for is gone from you. All your luxury and splendor have vanished, never to be recovered.\"'",
      "T": "'All the ripe fruit your soul craved — gone. Every luxurious and glittering thing — vanished. You will never find them again. The appetite that defined you is now your condemnation.'"
    },
    "15": {
      "L": "The merchants of these wares, who gained wealth from her, will stand far off in fear of her torment, weeping and mourning,",
      "M": "The merchants who sold these things and gained their wealth from her will stand far off, terrified at her torment. They will weep and mourn,",
      "T": "The merchants who had grown wealthy off her extravagance now stand at a safe distance, shaking with fear at what is happening to her, weeping and grieving —"
    },
    "16": {
      "L": "saying, 'Alas, alas, for the great city that was clothed in fine linen, in purple and scarlet, adorned with gold, with precious stones, and with pearls!'",
      "M": "and crying out: 'Woe! Woe to you, great city, dressed in fine linen, purple and scarlet, and glittering with gold, precious stones, and pearls!'",
      "T": "'Woe! Woe to you, great city — wrapped in fine linen, clothed in purple and scarlet, blazing with gold and jewels and pearls!'"
    },
    "17": {
      "L": "'For in a single hour all this great wealth has been laid waste.' And every shipmaster and all who sail to any place, and sailors, and all whose trade is on the sea, stood far off",
      "M": "'In one hour such great wealth has been brought to ruin!' Every sea captain, and all who travel by ship, the sailors, and all who earn their living from the sea, stood far off.",
      "T": "'In a single hour — all of it gone.' Every ship's captain, every seafarer, every sailor, every person who lives from the sea — they stand at a distance,"
    },
    "18": {
      "L": "and cried out as they watched the smoke of her burning: 'What city was like the great city?'",
      "M": "When they see the smoke of her burning, they will cry out: 'Was there ever a city like this great city?'",
      "T": "watching the smoke pour up from her burning and crying out: 'What city has ever been like this? There has never been anything like her.'"
    },
    "19": {
      "L": "And they threw dust on their heads and cried out, weeping and mourning, 'Alas, alas, for the great city where all who had ships at sea grew rich by her wealth! For in a single hour she has been laid waste.'",
      "M": "They will throw dust on their heads, and with weeping and mourning cry out: 'Woe! Woe to you, great city, through whose wealth all who had ships on the sea became rich! In one hour she has been brought to ruin!'",
      "T": "They throw dust on their heads — the ancient gesture of grief — and cry out, weeping and mourning: 'Woe! Woe to you, great city — you made every ship on the sea wealthy from your trade! In a single hour you are laid waste.'"
    },
    "20": {
      "L": "'Rejoice over her, O heaven, and you saints and apostles and prophets! For God has rendered his judgment against her on your behalf.'",
      "M": "'Rejoice over her, you heavens! Rejoice, you people of God and apostles and prophets! For God has judged her with the judgment she imposed on you.'",
      "T": "'Heaven, celebrate! God's holy people, apostles, prophets — celebrate! God has rendered the verdict. What she did to you — she has it done to her. The courtroom has ruled in your favor.'"
    },
    "21": {
      "L": "Then a mighty angel took up a stone like a great millstone and cast it into the sea, saying, 'So will Babylon the great city be thrown down with violence, and will be found no more at all.'",
      "M": "Then a mighty angel picked up a boulder the size of a large millstone and threw it into the sea, saying: 'With such violence the great city of Babylon will be thrown down, never to be found again.'",
      "T": "Then a powerful angel lifted a stone as large as a millstone and hurled it into the sea: 'That is how Babylon the great city will go down — with that kind of violence — and she will never be found again.' The sign echoes the scroll Seraiah hurled into the Euphrates at Jeremiah's command."
    },
    "22": {
      "L": "'And the sound of harpists and musicians, of flute players and trumpeters, will be heard in you no more, and a craftsman of any craft will be found in you no more, and the sound of the millstone will be heard in you no more,'",
      "M": "'The music of harpists and musicians, of pipers and trumpeters, will never be heard in you again. No worker of any trade will ever be found in you again. The sound of a millstone will never be heard in you again.'",
      "T": "'No more music in you — no harps, no songs, no flutes, no trumpets. No more craftsmen of any kind. The grinding of the millstone: silenced forever.'"
    },
    "23": {
      "L": "'And the light of a lamp will shine in you no more, and the voice of the bridegroom and bride will be heard in you no more, for your merchants were the great men of the earth, and all the nations were deceived by your sorcery.'",
      "M": "'The light of a lamp will never shine in you again. The voices of bride and groom will never be heard in you again. Your merchants were the world's important people. By your sorceries all the nations were led astray.'",
      "T": "'No lamplight will ever brighten your streets again. No wedding voices, no laughter of bride or groom — the joy that Jeremiah named when he announced judgment has been fully extinguished. Your merchants were the great ones of the world — and you bewitched every nation with your sorceries.'"
    },
    "24": {
      "L": "'And in her was found the blood of prophets and of saints, and of all who have been slaughtered on earth.'",
      "M": "'In her was found the blood of prophets and of God's holy people, of all who have been slaughtered on the earth.'",
      "T": "'And in her — exposed at last — the blood of prophets and saints, and the blood of every person ever slaughtered upon this earth. The great city stands guilty.'"
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'revelation')
        merge_tier(existing, REVELATION, tier_key)
        save(tier_dir, 'revelation', existing)
    print('Revelation 16–18 written.')

if __name__ == '__main__':
    main()
