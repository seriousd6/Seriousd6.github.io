"""
MKT Revelation chapters 1–2 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-revelation-1-2.py

Translation decisions:
- G602 (ἀποκάλυψις): "Revelation" (L/M) / "Unveiling" (T, 1:1 only) — surfaces the Greek meaning
  of an authorized disclosure of hidden things. Subsequent occurrences: "revelation" lowercase.
- G4151 (πνεῦμα): "Spirit" (capitalised throughout) — in 1:4 "the seven Spirits" (sevenfold Spirit
  before the throne); in 1:10 John carried in the Spirit on the Lord's Day; in 2:7/11/17/29
  "what the Spirit says to the churches." All clearly divine. No ambiguous πνεῦμα in chs 1–2.
- G3087 (λυχνία): "lampstand" not "candlestick" — more accurate; the image is a standing oil-lamp
  holder, not a wax candle.
- G3841 (παντοκράτωρ): "Almighty" (L/M); "All-Sovereign" (T, 1:8) — conveys the unique LXX term
  for God's comprehensive governing power, common in Revelation and 2 Cor.
- G3144 (μάρτυς): "witness" (L/M); "faithful witness" left as-is in T — the word means one who testifies,
  with martyrdom as a possible cost; "martyr" (2:13) where context is actual death.
- G26 (ἀγάπη): "love" throughout — 2:4 "first love" is the covenantal, willed self-giving love that
  characterised the Ephesian church's early devotion; 2:19 "love" alongside faith, service, endurance.
- G4102 (πίστις): "faith" / "faithfulness" — 2:13 context (holding fast under persecution) = faithful
  adherence; 2:19 listed among virtues: rendered "faith."
- G2962 (κύριος): "Lord" — consistent with all prior NT scripts.
- G5474 (χαλκολίβανον): "burnished bronze" — a rare word of uncertain derivation; possibly orichalcum
  or a high-quality refined brass; rendered "burnished bronze" (L/M) / "polished bronze from the furnace" (T).
- G4501 (ῥομφαία): "sword" (all tiers) — the ῥομφαία is a large, broad-bladed weapon (Thracian), distinct
  from the shorter μάχαιρα. Used metaphorically: the word that comes from Christ's mouth.
- Textual variant 1:5 — λούσαντι (TR/KJV "washed us from our sins") vs. λύσαντι (SBLGNT/NA28
  "freed/released us from our sins"). Interlinear follows TR (G3068, λούω = wash). Critical text
  (λύω = loose/free) is stronger on external evidence. L/M use "freed" following critical text; T notes
  both images — freedom and cleansing are both present in the passage.
- Textual variant 1:11 — "I am the Alpha and Omega, the first and the last" (TR) is absent from
  SBLGNT/NA28 and omitted here. The seven churches and scroll command remain.
- OT intertextuality:
  - 1:7: Dan 7:13 (coming with clouds) + Zech 12:10 (pierced / national mourning). T makes both explicit.
  - 1:13: Dan 7:13 (Son of Man) + Dan 10:5 (linen, golden girdle). T surfaces the Daniel echo.
  - 1:14: Dan 7:9 (Ancient of Days — white hair, white garment). T notes this divine conflation.
  - 1:15: Ezek 1:24 / 43:2 (voice of many waters). T notes Ezekiel's theophany.
  - 2:27: Ps 2:9 (rod of iron, breaking clay vessels). T makes the messianic coronation psalm explicit.
- G3801 (ὁ ὢν καὶ ὁ ἦν καὶ ὁ ἐρχόμενος): "who is and who was and who is to come" — the deliberate
  Hebraic expansion of YHWH as the eternal one. L/M render literally; T surfaces the Exodus 3:14 echo.
- G4416 (πρωτότοκος): "firstborn" — from the dead in 1:5 (perfect aspect: past resurrection with
  permanent result). Carries OT covenantal weight (Ps 89:27).
- G758 (ἄρχων): "ruler/prince" — "ruler of the kings of the earth" in 1:5. L renders "ruler"; M "ruler";
  T "sovereign."
- Aspect notes:
  - 1:5 ἀγαπῶντι (present participle) = "who loves us" — ongoing love, not past only.
  - 1:6 ἐποίησεν (aorist) = completed act: "he has made us" — the royal priesthood is already established.
  - 2:5 μνημόνευε (present imperative) = ongoing remembering; πεσόν (aorist) = specific past fall.
  - 2:16 ἔρχομαί (present) = "I am coming" — imminent and certain.
- G3466 (μυστήριον): "mystery" — not an unsolvable puzzle but a divine secret now being disclosed
  through revelation. L/M "mystery"; T "hidden meaning."
- Capitalization: "Spirit" throughout; "Son of Man" (title); "First and the Last" / "Alpha and Omega"
  as divine self-designations (capitalised as titles); "Death and Hades" (personalised powers, cap).
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
  "1": {
    "1": {
      "L": "The Revelation of Jesus Christ, which God gave to him to show his servants the things that must come to pass shortly; and he signified it, having sent by his angel to his servant John,",
      "M": "The revelation of Jesus Christ, which God gave him to show his servants what must soon take place. He made it known by sending his angel to his servant John,",
      "T": "This is the Unveiling of Jesus Christ — what God gave him to disclose to his servants: events that must happen very soon. He communicated it in signs, dispatching his angel to his servant John."
    },
    "2": {
      "L": "who bore witness to the word of God and to the testimony of Jesus Christ, even of all things that he saw.",
      "M": "who bore witness to the word of God and to the testimony of Jesus Christ — everything he saw.",
      "T": "John testified to all he saw: the word of God and the testimony that Jesus himself bore."
    },
    "3": {
      "L": "Blessed is the one who reads aloud and those who hear the words of this prophecy and keep the things written therein, for the time is near.",
      "M": "Blessed is the one who reads aloud, and blessed are those who hear the words of this prophecy and keep what is written in it, for the time is near.",
      "T": "A blessing rests on the one who reads this prophecy aloud in the assembly, and on all who hear and take it to heart — for the appointed time is almost upon us."
    },
    "4": {
      "L": "John to the seven churches that are in Asia: Grace to you and peace from him who is and who was and who is to come, and from the seven Spirits who are before his throne,",
      "M": "John to the seven churches in Asia: Grace and peace to you from him who is and who was and who is to come, and from the seven Spirits before his throne,",
      "T": "John writes to the seven churches of Asia. Grace and peace be yours — from the eternal God who is, who was, and who is coming (the living name of Exodus 3:14 expanded to its fullest); from the sevenfold Spirit stationed before his throne;"
    },
    "5": {
      "L": "and from Jesus Christ, the faithful witness, the firstborn from the dead, and the ruler of the kings of the earth. To him who loves us and freed us from our sins by his own blood —",
      "M": "and from Jesus Christ, the faithful witness, the firstborn from the dead, and the ruler of the kings of the earth. To him who loves us and freed us from our sins by his own blood —",
      "T": "and from Jesus Christ: faithful witness, firstborn out of death, sovereign over every earthly king. He loves us with an ongoing love. He set us free from our sins — at the cost of his own blood."
    },
    "6": {
      "L": "and he made us a kingdom, priests to his God and Father — to him be the glory and the dominion forever and ever. Amen.",
      "M": "and he has made us a kingdom of priests to his God and Father — to him be glory and dominion forever and ever. Amen.",
      "T": "He has constituted us a royal priesthood, a kingdom serving his God and Father. To him belongs all glory and sovereign power, age upon endless age. Amen."
    },
    "7": {
      "L": "Behold, he comes with the clouds, and every eye will see him, even those who pierced him; and all the tribes of the earth will wail because of him. Yes, Amen.",
      "M": "Behold, he is coming with the clouds, and every eye will see him — even those who pierced him — and all the tribes of the earth will mourn because of him. Yes, Amen.",
      "T": "Look — he is coming on the clouds (Daniel 7:13). Every eye will see him — even those who drove the spear through him (Zechariah 12:10). Every tribe on earth will beat their breasts in grief. Yes. Amen."
    },
    "8": {
      "L": "\"I am the Alpha and the Omega,\" says the Lord God, who is and who was and who is to come, the Almighty.",
      "M": "\"I am the Alpha and the Omega,\" says the Lord God, who is and who was and who is to come — the Almighty.",
      "T": "\"I am the Alpha and the Omega,\" declares the Lord God — the one who is, who was, and who is coming, the All-Sovereign."
    },
    "9": {
      "L": "I, John, your brother and companion in the tribulation and kingdom and patient endurance in Jesus, was on the island called Patmos because of the word of God and the testimony of Jesus.",
      "M": "I, John, your brother and partner in the tribulation and kingdom and patient endurance that are ours in Jesus, was on the island of Patmos because of the word of God and the testimony of Jesus.",
      "T": "I am John — your brother, your fellow-sharer in the suffering, the kingdom, and the steadfast endurance that are ours together in Jesus. I was exiled to the island of Patmos for proclaiming the word of God and the testimony of Jesus."
    },
    "10": {
      "L": "I was in the Spirit on the Lord's day, and I heard behind me a great voice like a trumpet,",
      "M": "I was in the Spirit on the Lord's day, and I heard behind me a loud voice like a trumpet,",
      "T": "It was the Lord's Day. The Spirit seized me, and from behind me came a booming voice like a trumpet blast."
    },
    "11": {
      "L": "saying, \"What you see write in a scroll and send it to the seven churches: to Ephesus, and to Smyrna, and to Pergamum, and to Thyatira, and to Sardis, and to Philadelphia, and to Laodicea.\"",
      "M": "saying, \"Write in a scroll what you see and send it to the seven churches — to Ephesus, Smyrna, Pergamum, Thyatira, Sardis, Philadelphia, and Laodicea.\"",
      "T": "The voice commanded: \"Write everything you see in a scroll and send it to the seven churches — Ephesus, Smyrna, Pergamum, Thyatira, Sardis, Philadelphia, and Laodicea.\""
    },
    "12": {
      "L": "And I turned to see the voice that was speaking with me. And having turned, I saw seven golden lampstands,",
      "M": "I turned to see the voice that was speaking to me, and when I turned I saw seven golden lampstands,",
      "T": "I turned to face the voice addressing me — and there before me stood seven lampstands of gold."
    },
    "13": {
      "L": "and in the midst of the lampstands one like a son of man, clothed in a robe reaching to the feet and girded about the chest with a golden sash.",
      "M": "and in the midst of the lampstands stood one like a son of man, clothed in a long robe, with a golden sash across his chest.",
      "T": "Moving among the lampstands was a figure like the Son of Man from Daniel's vision — robed to his feet, a golden sash bound across his chest."
    },
    "14": {
      "L": "His head and hair were white like white wool, like snow, and his eyes were like a flame of fire.",
      "M": "His head and his hair were white like white wool, like snow, and his eyes were like a blazing flame.",
      "T": "His head and hair were pure white — white as wool, white as snow, like the Ancient of Days in Daniel 7. His eyes blazed like twin flames."
    },
    "15": {
      "L": "And his feet were like burnished bronze, refined as in a furnace, and his voice was like the sound of many waters.",
      "M": "His feet were like burnished bronze, glowing as though refined in a furnace, and his voice was like the roar of rushing waters.",
      "T": "His feet gleamed like polished bronze drawn fresh from the furnace. His voice thundered like a cataract — the voice of many waters that Ezekiel heard at the throne."
    },
    "16": {
      "L": "And he had in his right hand seven stars, and from his mouth issued a sharp two-edged sword, and his face shone like the sun shining in its full strength.",
      "M": "In his right hand he held seven stars, and from his mouth came a sharp double-edged sword. His face was like the sun blazing in full strength.",
      "T": "Seven stars gleamed in his right hand. A sharp, double-edged sword issued from his mouth. His face blazed like the noon sun at full power."
    },
    "17": {
      "L": "And when I saw him, I fell at his feet as one dead. And he laid his right hand on me, saying, \"Do not fear; I am the First and the Last,\"",
      "M": "When I saw him, I fell at his feet like a dead man. He placed his right hand on me and said, \"Do not be afraid. I am the First and the Last.\"",
      "T": "I collapsed at his feet as if dead. He laid his right hand on me and said: \"Stop being afraid. I am the First and the Last.\""
    },
    "18": {
      "L": "and the living one. I was dead, and behold, I am alive forevermore, and I have the keys of Death and of Hades.",
      "M": "\"I am the living one. I was dead, and behold, I am alive forever and ever! And I hold the keys of Death and Hades.\"",
      "T": "\"I am the Living One. I died — and look: I am alive to the ages of ages! The keys of Death and Hades are in my hand.\""
    },
    "19": {
      "L": "Write therefore the things that you saw, and the things that are, and the things that are about to come to pass after these.",
      "M": "\"Write therefore what you have seen, what is now, and what will take place after this.\"",
      "T": "\"Write it all down: what you have already seen, what is happening now, and what is still to come.\""
    },
    "20": {
      "L": "The mystery of the seven stars that you saw in my right hand, and the seven golden lampstands: the seven stars are the angels of the seven churches, and the seven lampstands are the seven churches.",
      "M": "\"The mystery of the seven stars in my right hand and the seven golden lampstands is this: the seven stars are the angels of the seven churches, and the seven lampstands are the seven churches.\"",
      "T": "\"Here is the hidden meaning of the seven stars in my right hand and the seven golden lampstands: the seven stars are the guardian angels of the seven churches, and the seven lampstands are the seven churches themselves.\""
    }
  },
  "2": {
    "1": {
      "L": "To the angel of the church in Ephesus write: 'These things says the one who holds the seven stars in his right hand, who walks in the midst of the seven golden lampstands:'",
      "M": "\"To the angel of the church in Ephesus write: 'These are the words of the one who holds the seven stars in his right hand and walks among the seven golden lampstands:'\"",
      "T": "Write to the messenger of the church in Ephesus. These are the words of the one who holds the seven stars in his right hand and strides among the seven golden lampstands:"
    },
    "2": {
      "L": "'I know your works and your labor and your patient endurance, and that you cannot bear evil men, and you have tested those who call themselves apostles and are not, and found them liars.'",
      "M": "'I know your deeds, your hard work, and your patient endurance. I know that you cannot tolerate wicked people — you have tested those who claim to be apostles but are not, and have found them to be liars.'",
      "T": "'I see what you do: your hard work, your endurance, your zero tolerance for evil people. You put those self-appointed apostles to the test and exposed them as frauds.'"
    },
    "3": {
      "L": "'And you have patient endurance and have borne for my name's sake and have not grown weary.'",
      "M": "'You have endured hardships for my name and have not grown weary.'",
      "T": "'You have kept on bearing burdens for my name's sake without giving up. You have not worn out.'"
    },
    "4": {
      "L": "'But I have this against you: that you have abandoned your first love.'",
      "M": "'But I have this against you: you have abandoned the love you had at first.'",
      "T": "'But I hold this against you: you have walked away from your first love — that early, ardent, covenantal devotion.'"
    },
    "5": {
      "L": "'Remember therefore from where you have fallen, and repent and do the first works; or else I am coming to you and will remove your lampstand from its place, unless you repent.'",
      "M": "'Remember then from how far you have fallen. Repent and do the deeds you did at first. If not, I will come to you and remove your lampstand from its place — unless you repent.'",
      "T": "'Think back to where you once stood and how far you have fallen. Turn back. Do the things you did when your love was alive. If you do not, I am coming — and I will snuff out your lampstand and remove you from your place among my churches.'"
    },
    "6": {
      "L": "'Yet this you have: that you hate the works of the Nicolaitans, which I also hate.'",
      "M": "'But you have this in your favor: you hate the practices of the Nicolaitans, which I also hate.'",
      "T": "'Give yourself this credit: you detest what the Nicolaitans do — and so do I.'"
    },
    "7": {
      "L": "'He who has an ear, let him hear what the Spirit says to the churches. To the one who overcomes I will give to eat from the tree of life, which is in the paradise of God.'",
      "M": "'Let anyone who has an ear listen to what the Spirit is saying to the churches. To the one who overcomes, I will give the right to eat from the tree of life, which is in the paradise of God.'",
      "T": "'If you have ears to hear, listen to what the Spirit is saying to the churches. Whoever conquers will eat from the tree of life — that tree growing in the very paradise of God.'"
    },
    "8": {
      "L": "And to the angel of the church in Smyrna write: 'These things says the First and the Last, who was dead and came to life:'",
      "M": "\"To the angel of the church in Smyrna write: 'These are the words of the First and the Last, who died and came to life again:'\"",
      "T": "Write to the messenger of the church at Smyrna. These are the words of the First and the Last — the one who died and came alive again:"
    },
    "9": {
      "L": "'I know your tribulation and your poverty — but you are rich — and the slander of those who say they are Jews and are not, but are a synagogue of Satan.'",
      "M": "'I know your affliction and your poverty — yet you are rich. And I know the slander of those who say they are Jews but are not — they are a synagogue of Satan.'",
      "T": "'I know your suffering and your poverty — and yet you are truly rich. I also know the vile slander coming from those who call themselves Jews but are not: they are a congregation of Satan.'"
    },
    "10": {
      "L": "'Do not fear what you are about to suffer. Behold, the devil is about to cast some of you into prison, that you may be tested, and you will have tribulation for ten days. Be faithful unto death, and I will give you the crown of life.'",
      "M": "'Do not be afraid of what you are about to suffer. Behold, the devil is about to throw some of you into prison to be tested, and you will face affliction for ten days. Be faithful to the point of death, and I will give you the crown of life.'",
      "T": "'Do not fear what is coming. The devil is about to throw some of you into prison to be put to the test — you will face pressure for ten days. Hold on. Be faithful right to the moment of death, and I will give you the victor's crown of life.'"
    },
    "11": {
      "L": "'He who has an ear, let him hear what the Spirit says to the churches. The one who overcomes will not be harmed by the second death.'",
      "M": "'Let anyone who has an ear listen to what the Spirit says to the churches. Whoever overcomes will not be harmed by the second death.'",
      "T": "'If you have ears to hear, listen to what the Spirit is saying to the churches. Whoever conquers will never be touched by the second death.'"
    },
    "12": {
      "L": "And to the angel of the church in Pergamum write: 'These things says the one who has the sharp two-edged sword:'",
      "M": "\"To the angel of the church in Pergamum write: 'These are the words of the one who has the sharp two-edged sword:'\"",
      "T": "Write to the messenger of the church at Pergamum. These are the words of the one who wields the sharp, double-edged sword:"
    },
    "13": {
      "L": "'I know where you dwell, where Satan's throne is; and you hold fast my name and did not deny my faith even in the days of Antipas my faithful witness, who was killed among you, where Satan dwells.'",
      "M": "'I know where you live — where Satan's throne is. Yet you hold fast to my name and did not deny your faith in me, even in the days when Antipas, my faithful witness, was killed among you, where Satan lives.'",
      "T": "'I know you live right where Satan has his throne. And still you cling to my name — you never disowned me, even in the days when Antipas, my faithful witness, was murdered in Satan's own territory among you.'"
    },
    "14": {
      "L": "'But I have a few things against you: that you have there some who hold the teaching of Balaam, who taught Balak to put a stumbling block before the sons of Israel, to eat things sacrificed to idols and to commit fornication.'",
      "M": "'But I have a few things against you. You have some there who hold to the teaching of Balaam, who taught Balak to put a stumbling block before the children of Israel — to eat food sacrificed to idols and to commit sexual immorality.'",
      "T": "'But I have charges against you. There are people among you following Balaam's old playbook — the same scheme he taught Balak to use on Israel: entice them with idol-feasts and draw them into sexual sin.'"
    },
    "15": {
      "L": "'So you also have some who hold the teaching of the Nicolaitans in the same way.'",
      "M": "'Likewise, you have some among you who hold to the teaching of the Nicolaitans.'",
      "T": "'And in the same vein, some of you are clinging to the Nicolaitans' doctrine.'"
    },
    "16": {
      "L": "'Repent therefore; or else I am coming to you quickly and will war against them with the sword of my mouth.'",
      "M": "'Repent then! If not, I will come to you soon and make war against them with the sword of my mouth.'",
      "T": "'Turn back — now. If you do not, I am coming quickly, and I will make war against those people with the sword that comes from my mouth.'"
    },
    "17": {
      "L": "'He who has an ear, let him hear what the Spirit says to the churches. To the one who overcomes I will give of the hidden manna, and I will give him a white stone with a new name written on the stone that no one knows except the one who receives it.'",
      "M": "'Let anyone who has an ear listen to what the Spirit says to the churches. To the one who overcomes, I will give some of the hidden manna, and I will give him a white stone with a new name written on it that no one knows except the one who receives it.'",
      "T": "'If you have ears to hear, listen to what the Spirit is saying to the churches. Whoever conquers will receive hidden manna — bread from the heavenly store. And I will give him a white stone engraved with a new name that no one knows but the one who receives it.'"
    },
    "18": {
      "L": "And to the angel of the church in Thyatira write: 'These things says the Son of God, who has eyes like a flame of fire and feet like burnished bronze:'",
      "M": "\"To the angel of the church in Thyatira write: 'These are the words of the Son of God, whose eyes are like blazing fire and whose feet are like burnished bronze:'\"",
      "T": "Write to the messenger of the church at Thyatira. These are the words of the Son of God — eyes burning like fire, feet like gleaming bronze:"
    },
    "19": {
      "L": "'I know your works, and your love and faith and service and patient endurance, and that your last works are more than the first.'",
      "M": "'I know your deeds — your love, faith, service, and endurance — and that your recent deeds surpass your earlier ones.'",
      "T": "'I see what you are doing: your love, your faith, your ministry, your endurance. And your latest works outshine your earliest — you are growing, not declining.'"
    },
    "20": {
      "L": "'But I have this against you: that you tolerate that woman Jezebel, who calls herself a prophetess and teaches and seduces my servants to commit fornication and to eat things sacrificed to idols.'",
      "M": "'But I have this against you: you tolerate that woman Jezebel, who calls herself a prophetess. She teaches and misleads my servants into sexual immorality and eating food sacrificed to idols.'",
      "T": "'But this I hold against you: you are letting that woman Jezebel have her way. She poses as a prophetess and is actively leading my servants into sexual immorality and idol worship.'"
    },
    "21": {
      "L": "'And I gave her time that she might repent, and she does not want to repent of her fornication.'",
      "M": "'I gave her time to repent, but she refuses to repent of her sexual immorality.'",
      "T": "'I gave her time and room to turn around — and she flatly refused to repent of her immorality.'"
    },
    "22": {
      "L": "'Behold, I am throwing her onto a sickbed, and those who commit adultery with her into great tribulation, unless they repent of her works.'",
      "M": "'Behold, I will throw her onto a bed of suffering, and those who commit adultery with her into great tribulation, unless they repent of her deeds.'",
      "T": "'So watch: I am striking her down with illness, and I am throwing those who go along with her into crushing affliction — unless they break free and repent of what she has led them to do.'"
    },
    "23": {
      "L": "'And I will kill her children with death. And all the churches will know that I am the one who searches minds and hearts, and I will give to each of you according to your works.'",
      "M": "'I will strike her children dead. Then all the churches will know that I am the one who searches minds and hearts, and I will give to each of you what your works deserve.'",
      "T": "'Her followers I will strike down with death. Then every church in the world will learn that I am the one who sees into minds and hearts — and that I repay each person precisely according to what their deeds have earned.'"
    },
    "24": {
      "L": "'But to the rest of you in Thyatira who do not hold this teaching, who have not known the so-called deep things of Satan, I say to you: I put upon you no other burden.'",
      "M": "'But to the rest of you in Thyatira who do not hold this teaching and have not learned what some call the deep secrets of Satan: I will not impose any additional burden on you.'",
      "T": "'As for the rest of you in Thyatira — those who have not swallowed this teaching, who have refused to probe what they are calling \"the deep things of Satan\" — I am not adding any extra weight to your load.'"
    },
    "25": {
      "L": "'But hold fast what you have until I come.'",
      "M": "'Only hold on to what you have until I come.'",
      "T": "'Just hold tight to what you already have — until I arrive.'"
    },
    "26": {
      "L": "'And the one who overcomes and keeps my works until the end, to him I will give authority over the nations,'",
      "M": "'To the one who overcomes and keeps my works to the end, I will give authority over the nations —'",
      "T": "'Whoever conquers and keeps faithfully doing my will right to the end — I will give that person authority over the nations.'"
    },
    "27": {
      "L": "'and he will rule them with a rod of iron, as vessels of a potter they will be broken to pieces — as I also received from my Father —'",
      "M": "'He will rule them with an iron rod and shatter them like clay vessels — just as I received this authority from my Father —'",
      "T": "'He will shepherd them with an iron scepter, dashing them like clay pots (Psalm 2:9 — the messianic coronation psalm) — the same authority I received from my Father.'"
    },
    "28": {
      "L": "'and I will give him the morning star.'",
      "M": "'And I will give him the morning star.'",
      "T": "'And I will give him the morning star itself — the promise of the new day that belongs to the risen Christ (cf. Rev 22:16).'"
    },
    "29": {
      "L": "'He who has an ear, let him hear what the Spirit says to the churches.'",
      "M": "'Let anyone who has an ear listen to what the Spirit says to the churches.'",
      "T": "'If you have ears to hear, then hear what the Spirit is saying to the churches.'"
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'revelation')
        merge_tier(existing, REVELATION, tier_key)
        save(tier_dir, 'revelation', existing)
    print('Revelation 1–2 written.')

if __name__ == '__main__':
    main()
