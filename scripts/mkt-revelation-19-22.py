"""
MKT Revelation chapters 19–22 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-revelation-19-22.py

Translation decisions:
- G3056 (λόγος): "The Word of God" in 19:13 as a divine title for Christ (capitalised). This is the
  same Johannine λόγος from John 1; here it appears as a name on the rider's robe, tying the
  Christology of the Apocalypse back to the Gospel. L/M: "The Word of God"; T makes the Johannine
  connection explicit.
- G4151 (πνεῦμα): "Spirit" throughout (capitalised) — consistent with mkt-revelation-1-2.py.
  22:17 "the Spirit and the Bride say, 'Come'" — clearly the divine Spirit.
- G4102 (πίστις): "Faithful" in 19:11 (divine title "Faithful and True"); "faithfulness" implied
  in the martyrs' steadfastness. Consistent with prior chs.
- G1343 (δικαιοσύνη) / G1345 (δικαίωμα): 19:8 δικαιώματα τῶν ἁγίων = "righteous acts/deeds of
  the saints" — the plural δικαιώματα denotes individual righteous acts woven into the bride's linen.
  L: "righteous deeds"; M: "righteous acts"; T: "deeds of righteousness, woven by grace."
- G3841 (παντοκράτωρ): "Almighty" (L/M), "All-Sovereign" (T) — consistent with mkt-revelation-1-2.py.
- G721 (ἀρνίον): "Lamb" capitalised throughout as a divine title for Christ.
- G2288 (θάνατος) / G86 (ᾅδης): "Death" and "Hades" capitalised when personalised as powers
  (20:13-14), consistent with chs 1-2.
- G1228 (διάβολος) / G4567 (Σατανᾶς) / G1404 (δράκων): rendered "devil," "Satan," and "dragon"
  respectively; 20:2 identifies all four names with the same figure — rendered as an appositive chain.
- G5507 (χίλιοι ἔτη): "thousand years" — translated faithfully; no interpretive gloss for/against
  any millennial position (pre/a/post). The text says what it says.
- G1136/G3098 (Γώγ / Μαγώγ): "Gog and Magog" — the T tier notes the Ezekiel 38–39 echo in 20:8.
- Hallelujah: rendered "Hallelujah" (Hebrew transliteration) rather than "Alleluia" (Latin). The
  interlinear shows "Alleluia"; this translation restores the Hebrew register.
- G2652 (κατάθεμα): 22:3 "no curse any more" — the total reversal of Genesis 3:17; T makes the
  Eden restoration explicit.
- G3565 (νύμφη) / G1135 (γυνή): 21:2 "bride … adorned for her husband"; 21:9 "the bride, the
  wife of the Lamb" — both rendered with "bride." The Bride = the people of God / the holy city.
- Textual variant 22:14: "those who wash their robes" (SBLGNT/NA28, G4150) vs. "those who do his
  commandments" (TR, G1785+G4160). The interlinear tokens suggest the TR reading; following prior
  script practice (1:5 variant), L uses the interlinear source ("keep his commandments"), M/T use
  the better-attested critical text ("wash their robes").
- Textual variant 22:21: "with all" (SBLGNT, πάντων) vs. "with all the saints" (TR). Following
  critical text in all tiers.
- G239 (ἀλληλούϊα): "Hallelujah" in 19:1,3,4,6. The word is a Hebrew loanword (הַלְּלוּיָהּ) meaning
  "Praise Yah(weh)"; T surfaces this in 19:1.
- G4416 (πρωτότοκος): not in 19-22. G935 (βασιλεύς): "king/kings"; in 19:16 the double title
  "King of kings and Lord of lords" is rendered verbatim; T capitalises as a supreme title.
- OT intertextuality:
  - 19:2: Deut 32:43 (God avenges the blood of his servants). T notes this.
  - 19:11-16: The divine warrior riding out in righteousness echoes Isa 63:1-6 (the warrior with
    garments dipped in blood from treading the winepress). T makes this explicit.
  - 19:15: Ps 2:9 (rod of iron); Isa 63:3 (winepress of wrath). T surfaces both.
  - 20:8: Ezek 38–39 (Gog and Magog). T notes this.
  - 21:1: Isa 65:17; 66:22 (new heavens and new earth). T notes this.
  - 21:3: Lev 26:12; Ezek 37:27 (covenant formula: "I will be their God, they will be my people").
    T surfaces this.
  - 21:4: Isa 25:8 (God wipes away tears, abolishes death). T notes this.
  - 22:2: Gen 2:9; 3:22 (tree of life); Ezek 47:12 (healing leaves). T notes both.
  - 22:3: Gen 3:17 (the curse). T notes the reversal.
  - 22:13: Isa 44:6; 48:12 (First and Last). T notes this.
- Aspect notes:
  - 19:6 ἐβασίλευσεν (aorist): "has taken up his reign" — the aorist signals the decisive beginning
    of the reign; rendered with ingressive force in T.
  - 19:20 ἐβλήθησαν (aorist): "were hurled" — single decisive completed act.
  - 20:4 ἔζησαν (aorist): "came to life" — the first resurrection, a completed event.
  - 21:5 ποιῶ (present): "I am making" — ongoing creative act, not yet complete.
  - 22:20 ἔρχομαι (present): "I am coming" — imminent, certain.
- Capitalisation: "Spirit," "Lamb," "Word of God" (as title), "King of kings," "Lord of lords,"
  "First and Last," "Alpha and Omega," "Beginning and End," "Faithful and True" (as divine names);
  "Death" and "Hades" as personalised eschatological powers; "Bride" when referring to the Church.
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
  "19": {
    "1": {
      "L": "After these things I heard a great voice of many people in heaven, saying, 'Hallelujah! Salvation and glory and power belong to our God!'",
      "M": "After this I heard what sounded like the roar of a great multitude in heaven, shouting: 'Hallelujah! Salvation and glory and power belong to our God!'",
      "T": "Then the sound broke over me — a vast chorus from heaven, like the voice of an enormous crowd: 'Hallelujah! Salvation belongs to our God! Glory and power are his!'"
    },
    "2": {
      "L": "For true and righteous are his judgments, for he has judged the great prostitute who corrupted the earth with her fornication, and he has avenged the blood of his servants at her hand.",
      "M": "For his judgments are true and just. He has condemned the great prostitute who corrupted the earth with her sexual immorality, and he has avenged the blood of his servants shed by her hand.",
      "T": "His verdicts are true and just. He has passed sentence on the great prostitute who was corrupting the earth, and he has taken up the cause of his servants — avenging their blood from her hand (Deuteronomy 32:43)."
    },
    "3": {
      "L": "And a second time they said, 'Hallelujah! And her smoke rises up forever and ever.'",
      "M": "They cried out a second time: 'Hallelujah! The smoke from her goes up forever and ever.'",
      "T": "A second cry rose: 'Hallelujah! Her smoke ascends to the ages of ages — she is gone, and the verdict stands unreversed.'"
    },
    "4": {
      "L": "And the twenty-four elders and the four living creatures fell down and worshipped God who sits on the throne, saying, 'Amen. Hallelujah!'",
      "M": "The twenty-four elders and the four living creatures fell down and worshipped God who is seated on the throne, saying, 'Amen. Hallelujah!'",
      "T": "The twenty-four elders and the four living creatures threw themselves before God upon his throne, crying out together: 'Amen — Hallelujah!'"
    },
    "5": {
      "L": "And a voice came out from the throne, saying, 'Praise our God, all you his servants, all who fear him, both small and great!'",
      "M": "Then a voice came from the throne, saying: 'Praise our God, all you his servants, you who fear him, both small and great!'",
      "T": "Then a voice spoke out from the very throne: 'Give praise to our God — every servant of his, every person who fears him, great and small alike!'"
    },
    "6": {
      "L": "And I heard as it were the voice of a great multitude, and as the sound of many waters, and as the sound of mighty thunders, saying, 'Hallelujah! For the Lord our God the Almighty has taken up his reign.'",
      "M": "Then I heard what seemed to be the voice of a great multitude, like the roar of rushing waters and the crash of mighty thunder, crying out: 'Hallelujah! For the Lord our God the Almighty reigns!'",
      "T": "What came next sounded like a vast multitude — like a cataract, like massive thunder — crying: 'Hallelujah! For the Lord our God the All-Sovereign has taken up his reign!'"
    },
    "7": {
      "L": "Let us rejoice and be glad and give the glory to him, for the marriage of the Lamb has come, and his wife has made herself ready.",
      "M": "Let us rejoice and be glad and give him glory! For the wedding of the Lamb has come, and his bride has made herself ready.",
      "T": "Rejoice and celebrate — pour out your praise to him — for the wedding of the Lamb has arrived! His bride has prepared herself."
    },
    "8": {
      "L": "And to her was granted to clothe herself in fine linen, bright and clean; for the fine linen is the righteous deeds of the saints.",
      "M": "Fine linen, bright and clean, was given to her to wear — for the fine linen stands for the righteous acts of God's people.",
      "T": "Her garment — fine linen, shining and pure — was given to her. That radiant linen is the righteous deeds of the saints, woven into clothing by grace."
    },
    "9": {
      "L": "And he said to me, 'Write: Blessed are those who are called to the marriage supper of the Lamb.' And he said to me, 'These are the true words of God.'",
      "M": "Then he said to me, 'Write this: Blessed are those who are invited to the marriage supper of the Lamb.' And he added, 'These are the true words of God.'",
      "T": "The angel told me: 'Write this down: Blessed are those invited to the Lamb's wedding banquet.' Then he added: 'These are the genuine words of God — they are true.'"
    },
    "10": {
      "L": "And I fell at his feet to worship him. And he said to me, 'See that you do not do that; I am a fellow servant with you and with your brothers who hold the testimony of Jesus. Worship God; for the testimony of Jesus is the spirit of prophecy.'",
      "M": "I fell at his feet to worship him. But he said to me, 'Do not do that! I am a fellow servant with you and with your brothers who hold to the testimony of Jesus. Worship God! For the testimony of Jesus is the spirit of prophecy.'",
      "T": "I threw myself at his feet to worship him. He stopped me: 'No — do not do that! I am only a fellow servant, alongside you and your brothers who bear the testimony of Jesus. Worship God. For the testimony that Jesus bears is the very soul of prophecy.'"
    },
    "11": {
      "L": "And I saw heaven opened, and behold, a white horse! And the one sitting on it is called Faithful and True; and in righteousness he judges and makes war.",
      "M": "I saw heaven opened, and there before me was a white horse! Its rider is called Faithful and True, and with righteousness he judges and wages war.",
      "T": "Heaven opened — and I saw a white horse. Its rider bears the name Faithful and True. He judges and wages war by the measure of righteousness."
    },
    "12": {
      "L": "His eyes were like a flame of fire, and on his head were many diadems, and he had a name written that no one knows except himself.",
      "M": "His eyes are like blazing fire, and on his head are many crowns. He has a name written that no one knows except himself.",
      "T": "His eyes blazed like fire. Crown upon crown encircled his head. And he carries a name inscribed on him that no one but he himself has ever known."
    },
    "13": {
      "L": "And he is clothed in a garment dipped in blood, and his name is called The Word of God.",
      "M": "He is dressed in a robe dipped in blood, and the name he is called is The Word of God.",
      "T": "His robe was stained with blood — the blood of atonement and of battle, as in Isaiah 63:1-6. And the name he bears is The Word of God."
    },
    "14": {
      "L": "And the armies which are in heaven followed him on white horses, clothed in fine linen, white and pure.",
      "M": "The armies of heaven were following him on white horses, dressed in fine linen, white and pure.",
      "T": "Behind him came the armies of heaven — riding white horses, clothed in spotlessly white, pure fine linen."
    },
    "15": {
      "L": "And from his mouth proceeds a sharp sword, that with it he should smite the nations; and he will rule them with a rod of iron; and he treads the winepress of the fury of the wrath of God the Almighty.",
      "M": "From his mouth comes a sharp sword to strike down the nations. He will rule them with an iron rod. He will tread the winepress of the furious wrath of God the Almighty.",
      "T": "From his mouth issued a sharp sword — the weapon of his word — to cut down the nations. He will shepherd them with an iron scepter (Psalm 2:9). He treads the winepress of the fierce wrath of God the All-Sovereign (Isaiah 63:3)."
    },
    "16": {
      "L": "And he has on his garment and on his thigh a name written: King of kings and Lord of lords.",
      "M": "On his robe and on his thigh was written the name: King of kings and Lord of lords.",
      "T": "Written on his robe and on his thigh — the title that says everything: King of all kings. Lord of all lords."
    },
    "17": {
      "L": "And I saw one angel standing in the sun; and he cried with a great voice, saying to all the birds that fly in midheaven, 'Come, gather yourselves together for the great supper of God;'",
      "M": "And I saw an angel standing in the sun, and he called out with a loud voice to all the birds flying in midheaven: 'Come! Gather together for the great supper of God!'",
      "T": "Then I saw an angel stationed in the blazing sun. He cried out to every bird soaring through the middle heavens in a thundering voice: 'Come — assemble for the great feast of God!'"
    },
    "18": {
      "L": "that you may eat the flesh of kings, and the flesh of captains, and the flesh of mighty men, and the flesh of horses and of those who sit on them, and the flesh of all men, both free and slave, both small and great.",
      "M": "to eat the flesh of kings, the flesh of commanders, the flesh of the mighty, the flesh of horses and their riders, and the flesh of all — free and slave, small and great.",
      "T": "The feast was grim: the flesh of kings, the flesh of commanders, the flesh of the powerful — the flesh of horses and their riders — the flesh of every human being, slave or free, small or great."
    },
    "19": {
      "L": "And I saw the beast, and the kings of the earth, and their armies, gathered together to make war against him who sat on the horse, and against his army.",
      "M": "Then I saw the beast and the kings of the earth with their armies gathered together to wage war against the rider on the horse and against his army.",
      "T": "Then I saw it: the beast, together with the kings of the earth and all their assembled forces — drawn up for war against the rider on the white horse and the army behind him."
    },
    "20": {
      "L": "And the beast was taken, and with him the false prophet who worked signs in his presence, by which he deceived those who received the mark of the beast and those who worshipped his image; these two were thrown alive into the lake of fire that burns with brimstone.",
      "M": "But the beast was captured, and with it the false prophet who had performed the signs by which he deceived those who had received the mark of the beast and those who worshipped its image. The two of them were thrown alive into the lake of burning sulfur.",
      "T": "The beast was seized — and with it the false prophet who had worked signs in its presence to deceive all who wore the beast's mark and bowed before its image. Both were hurled alive into the lake of fire blazing with burning sulfur."
    },
    "21": {
      "L": "And the rest were killed with the sword of him who sat on the horse, even the sword which proceeded out of his mouth; and all the birds were filled with their flesh.",
      "M": "The rest were killed by the sword that came from the mouth of the rider on the horse, and all the birds gorged themselves on their flesh.",
      "T": "The rest were struck down by the sword that issued from the rider's mouth. And every bird feasted until it could eat no more."
    }
  },
  "20": {
    "1": {
      "L": "And I saw an angel coming down out of heaven, having the key of the bottomless pit and a great chain in his hand.",
      "M": "And I saw an angel coming down from heaven, holding in his hand the key to the Abyss and a great chain.",
      "T": "Then I saw an angel descending from heaven. He carried the key to the Abyss and a massive chain."
    },
    "2": {
      "L": "And he laid hold on the dragon, the old serpent, who is the devil and Satan, and bound him a thousand years,",
      "M": "He seized the dragon — that ancient serpent who is the devil and Satan — and bound him for a thousand years.",
      "T": "He grabbed hold of the dragon — that ancient serpent, the devil, Satan himself — and bound him in chains for a thousand years."
    },
    "3": {
      "L": "and cast him into the bottomless pit, and shut it, and sealed it over him, that he should deceive the nations no more, until the thousand years should be finished; after this he must be loosed for a little time.",
      "M": "He threw him into the Abyss, shut it, and sealed it over him, so that he could no longer deceive the nations until the thousand years were completed. After that he must be released for a short time.",
      "T": "He hurled him into the Abyss, locked it, and set a seal over it — sealing the deceiver away so that he could corrupt the nations no longer. Not until the thousand years are complete. After that, a brief release awaits him."
    },
    "4": {
      "L": "And I saw thrones, and they sat on them, and judgment was given to them; and I saw the souls of those who had been beheaded for the testimony of Jesus, and for the word of God, and those who had not worshipped the beast, nor his image, and had not received the mark upon their forehead and upon their hand; and they lived, and reigned with Christ a thousand years.",
      "M": "Then I saw thrones, and those seated on them were given authority to judge. And I saw the souls of those who had been beheaded because of their testimony about Jesus and because of the word of God — those who had not worshipped the beast or its image and had not received its mark on their foreheads or their hands. They came to life and reigned with Christ for a thousand years.",
      "T": "Then I saw thrones — and those enthroned on them were granted the authority to render judgment. I also saw the souls of those beheaded for their testimony about Jesus and for the word of God — who had refused to bow before the beast or its image, who had refused its mark on forehead or hand. They came to life again, and they reigned alongside Christ for a thousand years."
    },
    "5": {
      "L": "The rest of the dead lived not until the thousand years should be finished. This is the first resurrection.",
      "M": "The rest of the dead did not come to life until the thousand years were ended. This is the first resurrection.",
      "T": "The remaining dead did not come to life until the thousand years reached their end. This is what the first resurrection is."
    },
    "6": {
      "L": "Blessed and holy is he who has part in the first resurrection; over these the second death has no authority, but they shall be priests of God and of Christ, and shall reign with him a thousand years.",
      "M": "Blessed and holy are those who share in the first resurrection. The second death has no power over them, but they will be priests of God and of Christ and will reign with him for a thousand years.",
      "T": "How privileged and holy are those who belong to the first resurrection — the second death has no claim on them. They will serve as priests of God and of Christ, and they will reign with him through the thousand years."
    },
    "7": {
      "L": "And when the thousand years are finished, Satan shall be loosed out of his prison,",
      "M": "When the thousand years are over, Satan will be released from his prison,",
      "T": "When the thousand years expire, Satan will be freed from his confinement."
    },
    "8": {
      "L": "and shall come forth to deceive the nations which are in the four corners of the earth, Gog and Magog, to gather them together to the war: the number of whom is as the sand of the sea.",
      "M": "and will go out to deceive the nations in the four corners of the earth — Gog and Magog — to gather them for battle. Their number is like the sand on the seashore.",
      "T": "He will go out to seduce the nations spread across the four corners of the earth — Gog and Magog, the coalition drawn from Ezekiel's vision of the final assault (Ezekiel 38–39) — and muster them for war. Their number is beyond counting, like grains of sand by the sea."
    },
    "9": {
      "L": "And they went up over the breadth of the earth, and compassed the camp of the saints about, and the beloved city; and fire came down out of heaven, and devoured them.",
      "M": "They marched across the breadth of the earth and surrounded the camp of God's people, the city he loves. But fire came down from heaven and devoured them.",
      "T": "They spread across the face of the earth and ringed the camp of God's people — the beloved city — on every side. Then fire fell from heaven and consumed them utterly."
    },
    "10": {
      "L": "And the devil who deceived them was cast into the lake of fire and brimstone, where are also the beast and the false prophet; and they shall be tormented day and night forever and ever.",
      "M": "And the devil, who had deceived them, was thrown into the lake of burning sulfur, where the beast and the false prophet had been thrown. They will be tormented day and night forever and ever.",
      "T": "The devil who had led them all astray was hurled into the lake of fire and burning sulfur — joining the beast and the false prophet already there. They will be tormented day and night to the ages of ages."
    },
    "11": {
      "L": "And I saw a great white throne, and him that sat upon it, from whose face the earth and the heaven fled away; and there was found no place for them.",
      "M": "Then I saw a great white throne and the one who was seated on it. Earth and sky fled from his presence, and no place was found for them.",
      "T": "Then I saw it: a great white throne, and the one enthroned upon it. From the sight of his face, earth and sky fled — there was nowhere left for them to go."
    },
    "12": {
      "L": "And I saw the dead, the great and the small, standing before the throne; and books were opened; and another book was opened, which is the book of life; and the dead were judged out of the things which were written in the books, according to their works.",
      "M": "And I saw the dead, great and small, standing before the throne. Books were opened, and another book was opened — the book of life. The dead were judged according to what was written in the books, by what they had done.",
      "T": "I saw the dead — all of them, great and small — standing before the throne. The books were opened. Then another book was opened: the book of life. The dead were judged by what was written in those records, each one measured by what they had done."
    },
    "13": {
      "L": "And the sea gave up the dead that were in it; and Death and Hades gave up the dead that were in them; and they were judged every man according to their works.",
      "M": "The sea gave up the dead that were in it, and Death and Hades gave up the dead that were in them, and each person was judged according to what they had done.",
      "T": "The sea released its dead. Death and Hades surrendered theirs. And everyone — without exception — was judged by the record of their deeds."
    },
    "14": {
      "L": "And Death and Hades were cast into the lake of fire. This is the second death, even the lake of fire.",
      "M": "Then Death and Hades were thrown into the lake of fire. The lake of fire is the second death.",
      "T": "Then Death and Hades themselves were cast into the lake of fire. This is what the second death is — the lake of fire."
    },
    "15": {
      "L": "And if any was not found written in the book of life, he was cast into the lake of fire.",
      "M": "Anyone whose name was not found written in the book of life was thrown into the lake of fire.",
      "T": "And for everyone whose name was absent from the book of life — the lake of fire was their end."
    }
  },
  "21": {
    "1": {
      "L": "And I saw a new heaven and a new earth: for the first heaven and the first earth passed away; and the sea is no more.",
      "M": "Then I saw a new heaven and a new earth, for the first heaven and the first earth had passed away, and the sea was no more.",
      "T": "I saw it: a new heaven and a new earth (Isaiah 65:17; 66:22). The first heaven and the first earth had passed away — and the sea, that ancient symbol of chaos and death, was gone."
    },
    "2": {
      "L": "And I saw the holy city, new Jerusalem, coming down out of heaven from God, prepared as a bride adorned for her husband.",
      "M": "I saw the holy city, the new Jerusalem, coming down out of heaven from God, prepared as a bride beautifully dressed for her husband.",
      "T": "And I saw the holy city — new Jerusalem — descending from God out of heaven, arrayed like a bride who has made herself beautiful for her wedding day."
    },
    "3": {
      "L": "And I heard a great voice out of the throne saying, 'Behold, the tabernacle of God is with men, and he will dwell with them, and they shall be his people, and God himself shall be with them, and be their God.'",
      "M": "And I heard a loud voice from the throne saying: 'Behold, God's dwelling place is now among the people. He will dwell with them. They will be his people, and God himself will be with them and be their God.'",
      "T": "A powerful voice rang out from the throne: 'Look — the tabernacle of God is now with humanity. He will live among them. They will be his people, and God himself will be with them — their own God.' (The ancient covenant formula of Leviticus 26:12 and Ezekiel 37:27 is now fulfilled completely.)"
    },
    "4": {
      "L": "And he will wipe away every tear from their eyes; and death shall be no more; neither shall there be mourning, nor crying, nor pain, any more; the former things are passed away.",
      "M": "He will wipe every tear from their eyes. There will be no more death or mourning or crying or pain, for the old order of things has passed away.",
      "T": "He will wipe away every tear — every last one (Isaiah 25:8). Death will be abolished. Grief, weeping, and pain will be finished. The entire old order has passed away."
    },
    "5": {
      "L": "And he that sits on the throne said, 'Behold, I make all things new.' And he says, 'Write: for these words are faithful and true.'",
      "M": "He who was seated on the throne said, 'Behold, I am making all things new!' Then he said, 'Write this down, for these words are trustworthy and true.'",
      "T": "The one enthroned declared: 'Behold — I am making everything new.' And he said: 'Write it down. These words are reliable and true.'"
    },
    "6": {
      "L": "And he said to me, 'It is done. I am the Alpha and the Omega, the beginning and the end. I will give to him that is thirsty of the fountain of the water of life freely.'",
      "M": "He said to me: 'It is done. I am the Alpha and the Omega, the Beginning and the End. To the thirsty I will give water freely from the spring of the water of life.'",
      "T": "He declared: 'Done. I am the Alpha and the Omega — the Beginning and the End. To everyone who thirsts, I will give freely from the spring of the water of life.'"
    },
    "7": {
      "L": "He that overcomes shall inherit these things; and I will be his God, and he shall be my son.",
      "M": "Anyone who is victorious will inherit all this, and I will be their God and they will be my child.",
      "T": "Whoever conquers will inherit all of this — and I will be their God, and they will be my son."
    },
    "8": {
      "L": "But the fearful, and unbelieving, and abominable, and murderers, and fornicators, and sorcerers, and idolaters, and all liars, their part shall be in the lake that burns with fire and brimstone; which is the second death.",
      "M": "But the cowardly, the unbelieving, the vile, murderers, the sexually immoral, those who practice sorcery, idolaters, and all liars — their place will be in the lake of burning sulfur. This is the second death.",
      "T": "But the cowardly, the faithless, the morally repugnant, murderers, the sexually immoral, sorcerers, idol-worshippers, and every liar — their share is the lake burning with fire and sulfur. That is the second death."
    },
    "9": {
      "L": "And there came one of the seven angels who had the seven bowls, who were laden with the seven last plagues; and he spoke with me, saying, 'Come here, I will show you the bride, the wife of the Lamb.'",
      "M": "One of the seven angels who had the seven bowls full of the seven last plagues came and said to me, 'Come, I will show you the bride, the wife of the Lamb.'",
      "T": "Then one of the seven angels who carry the seven bowls brimming with the seven last plagues came and spoke to me: 'Come — I will show you the Bride, the Lamb's wife.'"
    },
    "10": {
      "L": "And he carried me away in the Spirit to a mountain great and high, and showed me the holy city Jerusalem, coming down out of heaven from God,",
      "M": "And he carried me away in the Spirit to a great and high mountain, and showed me the holy city Jerusalem coming down out of heaven from God.",
      "T": "The Spirit carried me away to the top of a vast, soaring mountain. From there the angel showed me the holy city Jerusalem descending from God out of heaven."
    },
    "11": {
      "L": "having the glory of God: her light was like a most precious stone, as it were a jasper stone, clear as crystal.",
      "M": "It shone with the glory of God, and its brilliance was like that of a very precious jewel — like a jasper, clear as crystal.",
      "T": "It was radiant with the glory of God — its light like the most precious of gems, like a jasper that blazes clear as crystal."
    },
    "12": {
      "L": "having a wall great and high; having twelve gates, and at the gates twelve angels; and names written thereon, which are the names of the twelve tribes of the children of Israel;",
      "M": "It had a great and high wall with twelve gates. At the gates were twelve angels, and on the gates were inscribed the names of the twelve tribes of Israel.",
      "T": "Its wall was great and high, pierced by twelve gates — each gate guarded by an angel, each gate bearing the name of one of the twelve tribes of Israel."
    },
    "13": {
      "L": "on the east were three gates; and on the north three gates; and on the south three gates; and on the west three gates.",
      "M": "There were three gates on the east, three on the north, three on the south, and three on the west.",
      "T": "Three gates faced east, three faced north, three faced south, three faced west."
    },
    "14": {
      "L": "And the wall of the city had twelve foundations, and on them twelve names of the twelve apostles of the Lamb.",
      "M": "The wall of the city had twelve foundations, and on them were the names of the twelve apostles of the Lamb.",
      "T": "The city's wall rested on twelve foundations, and inscribed on each foundation was the name of one of the twelve apostles of the Lamb."
    },
    "15": {
      "L": "And he that spoke with me had for a measure a golden reed to measure the city, and the gates thereof, and the wall thereof.",
      "M": "The angel who talked with me had a golden measuring rod to measure the city, its gates, and its walls.",
      "T": "The angel speaking with me held a golden measuring rod — to measure the city itself, its gates, and its walls."
    },
    "16": {
      "L": "And the city lies foursquare, and the length thereof is as great as the breadth: and he measured the city with the reed, twelve thousand furlongs; the length and the breadth and the height thereof are equal.",
      "M": "The city was laid out like a square, as long as it was wide. He measured the city with the rod and found it to be twelve thousand stadia in length, and its width and height were equal to that.",
      "T": "The city was perfectly square — length, width, and height all equal. The angel measured it: twelve thousand stadia on every side. A perfect cube — the shape of the Most Holy Place in Solomon's temple, now expanded to cosmic scale."
    },
    "17": {
      "L": "And he measured the wall thereof, a hundred and forty and four cubits, according to the measure of a man, that is, of an angel.",
      "M": "He measured its wall and found it to be 144 cubits thick, by human measurement, which is also the angel's measurement.",
      "T": "He measured the wall: one hundred forty-four cubits — measured in human units, the same standard the angel used. The number twelve squared speaks of completeness and the covenant community."
    },
    "18": {
      "L": "And the building of the wall thereof was jasper: and the city was pure gold, like unto pure glass.",
      "M": "The wall was made of jasper, and the city itself was pure gold, as pure as glass.",
      "T": "The wall was built of jasper. The city itself was pure gold — gold as transparent and radiant as glass."
    },
    "19": {
      "L": "The foundations of the wall of the city were adorned with all manner of precious stones. The first foundation was jasper; the second, sapphire; the third, chalcedony; the fourth, emerald;",
      "M": "The foundations of the city's walls were decorated with every kind of precious stone: the first jasper, the second sapphire, the third agate, the fourth emerald,",
      "T": "Every foundation of the city wall was set with precious gems — one for each. First: jasper. Second: sapphire. Third: agate. Fourth: emerald."
    },
    "20": {
      "L": "the fifth, sardonyx; the sixth, sardius; the seventh, chrysolite; the eighth, beryl; the ninth, topaz; the tenth, chrysoprase; the eleventh, jacinth; the twelfth, amethyst.",
      "M": "the fifth onyx, the sixth ruby, the seventh chrysolite, the eighth beryl, the ninth topaz, the tenth chrysoprase, the eleventh jacinth, the twelfth amethyst.",
      "T": "Fifth: onyx. Sixth: ruby. Seventh: chrysolite. Eighth: beryl. Ninth: topaz. Tenth: chrysoprase. Eleventh: jacinth. Twelfth: amethyst."
    },
    "21": {
      "L": "And the twelve gates were twelve pearls; each one of the gates was of one pearl: and the street of the city was pure gold, as it were transparent glass.",
      "M": "The twelve gates were twelve pearls — each gate made from a single pearl. And the main street of the city was pure gold, like transparent glass.",
      "T": "Each of the twelve gates was carved from a single pearl. And the great street of the city was pure gold — transparent as polished glass."
    },
    "22": {
      "L": "And I saw no temple therein: for the Lord God the Almighty, and the Lamb, are the temple thereof.",
      "M": "I did not see a temple in the city, because the Lord God Almighty and the Lamb are its temple.",
      "T": "There was no temple in the city — because the Lord God the All-Sovereign and the Lamb are the temple. They are the divine presence that every temple ever pointed to."
    },
    "23": {
      "L": "And the city has no need of the sun, neither of the moon, to shine upon it: for the glory of God did lighten it, and the lamp thereof is the Lamb.",
      "M": "The city does not need the sun or the moon to shine on it, for the glory of God illuminates it, and the Lamb is its lamp.",
      "T": "The city has no need for sun or moon — the glory of God is its light, and the Lamb himself is its lamp."
    },
    "24": {
      "L": "And the nations shall walk amidst the light thereof: and the kings of the earth bring their glory into it.",
      "M": "The nations will walk by its light, and the kings of the earth will bring their splendor into it.",
      "T": "The nations will walk in that light. The kings of the earth will bring all their glory and lay it at the city's feet."
    },
    "25": {
      "L": "And the gates thereof shall in no wise be shut by day (for there shall be no night there):",
      "M": "On no day will its gates ever be shut — for there will be no night there.",
      "T": "Its gates will never close — there is no night there, no darkness, nothing that needs to be locked out."
    },
    "26": {
      "L": "and they shall bring the glory and the honor of the nations into it.",
      "M": "The glory and honor of the nations will be brought into it.",
      "T": "All the glory and honor the nations carry will stream into it."
    },
    "27": {
      "L": "And there shall in no wise enter into it anything unclean, or he that makes an abomination and a lie: but only those who are written in the Lamb's book of life.",
      "M": "Nothing impure will ever enter it, nor will anyone who does what is shameful or deceitful — only those whose names are written in the Lamb's book of life.",
      "T": "Nothing defiled will pass through its gates. No one who practices abomination or lives by lies will ever enter. Only those enrolled in the Lamb's book of life belong there."
    }
  },
  "22": {
    "1": {
      "L": "And he showed me a river of water of life, bright as crystal, proceeding out of the throne of God and of the Lamb,",
      "M": "Then the angel showed me the river of the water of life, as clear as crystal, flowing from the throne of God and of the Lamb,",
      "T": "The angel showed me the river of the water of life — shining like crystal, pouring from the throne of God and of the Lamb —"
    },
    "2": {
      "L": "in the middle of the street thereof. And on this side of the river and on that was the tree of life, bearing twelve manner of fruits, yielding its fruit every month: and the leaves of the tree were for the healing of the nations.",
      "M": "flowing down the middle of the main street of the city. On each side of the river stood the tree of life, bearing twelve crops of fruit, yielding its fruit every month. And the leaves of the tree are for the healing of the nations.",
      "T": "— flowing down the center of the great street. On both banks grew the tree of life (Genesis 2:9; 3:22 — Eden restored and enlarged), bearing a different fruit every month, twelve harvests in a year. And the leaves of the tree bring healing to the nations (Ezekiel 47:12)."
    },
    "3": {
      "L": "And there shall be no curse any more: and the throne of God and of the Lamb shall be therein: and his servants shall serve him;",
      "M": "No longer will there be any curse. The throne of God and of the Lamb will be in the city, and his servants will serve him.",
      "T": "Nothing will be under the curse any longer — the curse of Genesis 3:17 is completely reversed. The throne of God and of the Lamb will stand there, and his servants will offer him worship and service."
    },
    "4": {
      "L": "and they shall see his face; and his name shall be on their foreheads.",
      "M": "They will see his face, and his name will be on their foreheads.",
      "T": "They will look upon his face — the beatific vision that the old age could not sustain — and his name will be written on their foreheads."
    },
    "5": {
      "L": "And there shall be no night no more; and they need no light of lamp, neither light of sun; for the Lord God shall give them light: and they shall reign for ever and ever.",
      "M": "There will be no more night. They will not need the light of a lamp or the light of the sun, for the Lord God will shine on them. And they will reign forever and ever.",
      "T": "No more night, ever. No need for lamp or sun — the Lord God himself is their light. And they will reign to the ages of ages."
    },
    "6": {
      "L": "And he said unto me, 'These words are faithful and true: and the Lord, the God of the spirits of the prophets, sent his angel to show unto his servants the things which must shortly come to pass.'",
      "M": "The angel said to me, 'These words are trustworthy and true. The Lord, the God who inspires the prophets, sent his angel to show his servants the things that must soon take place.'",
      "T": "'These words are reliable and true,' the angel told me. 'The Lord — who is the God of the spirits of the prophets — has sent his angel to show his servants what must happen very soon.'"
    },
    "7": {
      "L": "'And behold, I come quickly. Blessed is he that keeps the words of the prophecy of this book.'",
      "M": "'Behold, I am coming soon! Blessed is the one who keeps the words of the prophecy of this scroll.'",
      "T": "'And listen — I am coming quickly. Blessed is the person who takes these prophetic words to heart and holds on to them.'"
    },
    "8": {
      "L": "And I John am he that heard and saw these things. And when I heard and saw, I fell down to worship before the feet of the angel who showed me these things.",
      "M": "I, John, am the one who heard and saw these things. And when I heard and saw them, I fell down to worship at the feet of the angel who had been showing them to me.",
      "T": "I, John, am the one who heard and saw all of this. And when I had heard and seen it, I collapsed at the angel's feet to worship him."
    },
    "9": {
      "L": "And he says to me, 'See thou do it not: I am a fellow servant with you and with your brothers the prophets, and with those who keep the words of this book: worship God.'",
      "M": "But he said to me, 'Do not do that! I am a fellow servant with you and with your brothers the prophets and with all who keep the words of this scroll. Worship God!'",
      "T": "He stopped me immediately: 'No — not me! I am a fellow servant, alongside you and your brothers the prophets, alongside everyone who holds fast to the words of this book. God is the one to worship.'"
    },
    "10": {
      "L": "And he says to me, 'Seal not up the words of the prophecy of this book; for the time is at hand.'",
      "M": "Then he told me, 'Do not seal up the words of the prophecy of this scroll, because the time is near.'",
      "T": "'Do not seal this prophecy — keep it open. The time is already close.' (The contrast with Daniel 12:4,9 is deliberate: Daniel was told to seal his vision; this one is to remain unsealed.)"
    },
    "11": {
      "L": "He that is unrighteous, let him do unrighteousness still: and he that is filthy, let him be made filthy still: and he that is righteous, let him do righteousness still: and he that is holy, let him be made holy still.",
      "M": "Let the one who does wrong continue to do wrong; let the vile person continue to be vile; let the one who does right continue to do right; and let the holy person continue to be holy.",
      "T": "Let the unjust keep on being unjust. Let the filthy stay filthy. Let the righteous keep practicing righteousness. Let the holy person keep growing in holiness. The disclosure of the end leaves everyone as they are — character is being fixed."
    },
    "12": {
      "L": "Behold, I come quickly; and my reward is with me, to render to each man according as his work is.",
      "M": "Behold, I am coming soon! My reward is with me, and I will give to each person according to what they have done.",
      "T": "'Look — I am coming quickly, and my recompense comes with me. I will repay each person in full for what they have done.'"
    },
    "13": {
      "L": "I am the Alpha and the Omega, the first and the last, the beginning and the end.",
      "M": "I am the Alpha and the Omega, the First and the Last, the Beginning and the End.",
      "T": "'I am the Alpha and the Omega — the First and the Last, the Beginning and the End.' (Isaiah 44:6; 48:12 applied now to Christ, the divine speaker.)"
    },
    "14": {
      "L": "Blessed are they that keep his commandments, that they may have the right to come to the tree of life, and may enter in by the gates into the city.",
      "M": "Blessed are those who wash their robes, that they may have the right to the tree of life and may go through the gates into the city.",
      "T": "Blessed are those who wash their robes — they will have the right to the tree of life, and they will enter the city through the gates."
    },
    "15": {
      "L": "Outside are the dogs, and the sorcerers, and the fornicators, and the murderers, and the idolaters, and everyone who loves and makes a lie.",
      "M": "Outside are the dogs, those who practice sorcery, the sexually immoral, the murderers, the idolaters, and everyone who loves and practices falsehood.",
      "T": "Outside the gates: the dogs, the sorcerers, the sexually immoral, the murderers, the idol-worshippers — and everyone who loves to tell lies and live by them."
    },
    "16": {
      "L": "I Jesus have sent my angel to testify unto you these things for the churches. I am the root and the offspring of David, the bright and morning star.",
      "M": "I, Jesus, have sent my angel to give you this testimony for the churches. I am the Root and the Offspring of David, and the bright Morning Star.",
      "T": "Jesus himself speaks: 'I have sent my angel to give you this testimony for the churches. I am the Root and the Descendant of David — and the blazing Morning Star.'"
    },
    "17": {
      "L": "And the Spirit and the bride say, 'Come.' And he that hears, let him say, 'Come.' And he that is thirsty, let him come: he that will, let him take the water of life freely.",
      "M": "The Spirit and the Bride say, 'Come!' Let the one who hears say, 'Come!' Let the one who is thirsty come — let the one who wishes take the free gift of the water of life.",
      "T": "'Come!' says the Spirit. 'Come!' says the Bride. Let everyone who hears echo the cry: 'Come!' Let everyone who thirsts come. Let everyone who wants it drink freely from the water of life — no price, no barrier, no condition but desire."
    },
    "18": {
      "L": "I testify unto every man that hears the words of the prophecy of this book: if any man shall add unto them, God shall add unto him the plagues which are written in this book;",
      "M": "I warn everyone who hears the words of the prophecy of this scroll: if anyone adds anything to them, God will add to that person the plagues described in this scroll.",
      "T": "I give this solemn warning to everyone who hears the prophetic words of this book: if anyone adds anything to them, God will add to that person all the plagues recorded in this book."
    },
    "19": {
      "L": "and if any man shall take away from the words of the book of this prophecy, God shall take away his part from the tree of life, and out of the holy city, which are written in this book.",
      "M": "And if anyone takes words away from this scroll of prophecy, God will take away from that person any share in the tree of life and in the holy city, as described in this scroll.",
      "T": "And if anyone removes any words from this book of prophecy, God will strip away that person's share in the tree of life and in the holy city — all the blessings described in this book."
    },
    "20": {
      "L": "He who testifies these things says, 'Yes, I come quickly.' Amen. Come, Lord Jesus.",
      "M": "He who testifies to these things says, 'Yes, I am coming soon.' Amen. Come, Lord Jesus!",
      "T": "The one who testifies to all of this says: 'Yes — I am coming quickly.' Amen. Come, Lord Jesus!"
    },
    "21": {
      "L": "The grace of the Lord Jesus be with all. Amen.",
      "M": "The grace of the Lord Jesus be with God's people. Amen.",
      "T": "May the grace of the Lord Jesus Christ be with all of you. Amen."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'revelation')
        merge_tier(existing, REVELATION, tier_key)
        save(tier_dir, 'revelation', existing)
    print('Revelation 19–22 written.')

if __name__ == '__main__':
    main()
