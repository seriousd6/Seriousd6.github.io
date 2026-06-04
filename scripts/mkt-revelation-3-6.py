"""
MKT Revelation chapters 3–6 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-revelation-3-6.py

Translation decisions:
- G721 ἀρνίον (Lamb): "Lamb" in all tiers — the diminutive form is used exclusively in
    Revelation (28×) for Christ. It is a theological choice, not a synonym for G286 ἀμνός.
    The diminutive may heighten the paradox of the slain Lamb holding cosmic authority.
- G2962 κύριος (Lord): "Lord" in L/M; "Lord" retained in T — in Revelation κύριος is not
    translating יהוה so small-caps convention does not apply. Context always personalizes it.
- G3841 παντοκράτωρ (Almighty): "Almighty" in L/M; "the All-Sovereign" in T (4:8) — this
    title (used 9× in Revelation, once in Paul) emphasizes comprehensive executive power, not
    merely omnipotence. "All-Sovereign" surfaces that sense more forcefully in T.
- G2226 ζῷον (living creature): "living creature" in all tiers — NOT "beast." That is G2342
    θηρίον, used in Rev 6:8 for the wild animals that kill. The four ζῷα of ch.4–6 are the
    cherubic attendants of the throne; "beast" obscures this entirely.
- G2342 θηρίον (wild beast): "wild beasts" in 6:8 L; "wild beasts" in M/T — the destructive
    animals of the fourth seal, not the eschatological Beasts of chs.13–17.
- G4973 σφραγίς (seal): "seal" in all tiers — the wax seal on a rolled document. Each seal's
    breaking releases the next revelation of history's unfolding.
- G3528 νικάω (overcome/conquer): "overcomes" in L/M; "the victor" or "wins the victory"
    in T — the word is agonistic, used of military and athletic victory. In the seven-letter
    promises (chs.2–3) each promise is conditioned on ὁ νικῶν (the one conquering). T
    surfaces the active effort of perseverance implied.
- G1577 ἐκκλησία (assembly): "church" in L/M; "assembly" in T — "church" is the
    conventional rendering that will not confuse readers, but "assembly" in T recovers the
    civic/community force of the term: the called-out gathering of citizens of the Kingdom.
- G4151 πνεῦμα (Spirit): capitalized "Spirit" throughout — all occurrences in these chapters
    refer to the divine Spirit; Greek capitals are absent but theological context is clear.
- G746 ἀρχή (beginning/ruler, 3:14): "the beginning of the creation of God" in L; "the
    beginning of God's creation" in M; "the source and sovereign of all that God has made" in
    T — ἀρχή carries both senses (temporal beginning and ruling authority/source). T surfaces
    the ambiguity; the Colossian parallel (Col 1:15–18) informs the dual resonance.
- G2033 ἑπτά + G4151 (seven Spirits, 3:1; 4:5; 5:6): "seven Spirits of God" in L/M;
    "the sevenfold Spirit of God" in T — the numerical fullness of the Spirit, echoing
    Isa 11:2 (the seven-aspect Spirit resting on the Messiah). Not seven individual spirits.
- G165 αἰών (ages): "unto the ages of ages" in L; "forever and ever" in M; "to the ages of
    ages — without end" in T — the Revelation doxology formula uses the superlative idiom
    (ages of ages) rather than the simple αἰώνιος; T retains the formulaic ring while
    marking its force.
- G1203 δεσπότης (Sovereign Master, 6:10): "Master" in L; "Sovereign Lord" in M;
    "Absolute Sovereign" in T — δεσπότης is the stronger title for total ownership-authority,
    distinct from κύριος. The martyrs invoke it precisely because they are claiming God's right
    to judge his own household servants.
- G86 ᾅδης (Hades, 6:8): "Hades" in L/M; "the realm of the dead" in T — the Greek
    underworld, paired with Death as his companion/repository. T surfaces the function.
- G5515 χλωρός (pale/sickly green, 6:8): "pale" in L/M; "sickly pale" in T — χλωρός is
    the color of unripe grain, living vegetation, or a corpse's pallor. Here the pallor of
    death. T underscores the corpse-color aspect.
- G2218 ζυγός (balance/scales, 6:5): "balance" in L; "scales" in M/T — the instrument of
    rationing, measuring out scarce grain by weight. The famine seal is economic.
- OT intertextuality:
    4:8 Trishagion: echoes Isa 6:3 — the same three-fold "holy" from the throne-room vision.
        The T tier notes the deliberate echo by rendering the cadence similarly.
    5:5 "Lion of Judah / Root of David": echoes Gen 49:9–10 (lion scepter) and Isa 11:1, 10
        (root of Jesse/David). T surfaces both.
    5:9 "ransomed" (G59 ἀγοράζω = to purchase in the marketplace): the slave-market metaphor
        of redemption. L "purchased," M "ransomed," T surfaces the marketplace-liberation sense.
    6:8 four means of death: echoes Ezek 14:21 — sword, famine, wild beasts, and plague.
        G2288 θάνατος here likely = pestilence/plague (the LXX rendering of דֶּבֶר).
        L renders "death" (source-accurate); M "pestilence"; T "plague."
    6:9–10 "souls under the altar": echoes the blood of sacrificed animals poured under the
        altar (Lev 4:7). The martyrs' deaths are themselves sacrificial; T surfaces this.
    6:12–17 cosmic dissolution: echoes Isa 34:4; Joel 2:10, 31; Isa 2:19–21. These are
        prophetic conventions for divine judgment, not necessarily literal astronomy.
- Aspect notes:
    3:3 ἔχεις λάβης (perfect + aorist subjunctive): "have received" = continuing possession;
        "heard" = past reception. T preserves the dual tense.
    3:20 ἕστηκα (perfect): "I stand" — not just present action but a completed-state: I have
        taken my position and I am standing here. T: "I have taken my place … standing."
    5:6 ἑστηκός (perfect participle): "having stood" = the Lamb stands in the completed
        state of its slaughter — the wounds remain. L "standing, as having been slain."
    5:9 ᾖσαν (aorist) ᾄδω: a single completed act — they broke into song.
    6:4 δοθῆναι (aorist infinitive passive): the authority to take peace is divinely granted
        ("was permitted" = divine passive — God is the unnamed agent).
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
  "3": {
    "1": {
      "L": "And to the angel of the church in Sardis write: These things says the one who has the seven Spirits of God and the seven stars: I know your works, that you have a name that you are living, and you are dead.",
      "M": "And to the angel of the church in Sardis write: 'These are the words of the one who holds the seven Spirits of God and the seven stars: I know your works. You have a reputation for being alive, but you are dead.'",
      "T": "To the angel of the assembly in Sardis, write: These words come from the one who holds the sevenfold Spirit of God and all seven stars in his grip. I have seen your record: you carry the name Living — but what you actually are is dead."
    },
    "2": {
      "L": "Be watchful and strengthen the things that remain which are about to die, for I have not found your works complete before my God.",
      "M": "Wake up, and strengthen what remains and is about to die, for I have not found your works complete in the sight of my God.",
      "T": "Wake up, and shore up the last flickering embers of life before even those go cold. When I look at you before my God, what I see falls short — unfinished, hollow, incomplete."
    },
    "3": {
      "L": "Remember therefore how you have received and heard; hold fast, and repent. If therefore you do not watch, I will come as a thief, and you will not know what hour I will come upon you.",
      "M": "Remember, then, what you received and heard. Keep it, and repent. If you will not wake up, I will come like a thief, and you will not know at what hour I will come against you.",
      "T": "Go back to the beginning — what you first received, what you first heard. Hold it fast, and turn around. If you refuse to wake up, I will arrive like a thief in the night: unannounced, at an hour you will never see coming."
    },
    "4": {
      "L": "Yet you have a few names in Sardis who have not defiled their garments, and they shall walk with me in white, because they are worthy.",
      "M": "Yet you have a few people in Sardis who have not soiled their garments, and they will walk with me in white, for they are worthy.",
      "T": "Even in Sardis there is a remnant — a few who kept themselves uncontaminated, whose garments are still clean. These I will walk alongside in white, because they have proven themselves worth honoring."
    },
    "5": {
      "L": "The one overcoming thus shall be clothed in white garments, and I will not blot out his name from the book of life, and I will confess his name before my Father and before his angels.",
      "M": "The one who overcomes will be clothed in white garments, and I will never blot his name out of the book of life. I will confess his name before my Father and before his angels.",
      "T": "The victor will be robed in the white of the redeemed — his name stays written in the book of life, never erased. And before my Father and the entire heavenly court, I will speak that name as someone I claim as my own."
    },
    "6": {
      "L": "The one having an ear, let him hear what the Spirit says to the churches.",
      "M": "Let anyone who has an ear hear what the Spirit is saying to the churches.",
      "T": "If you have ears, put them to use: this is what the Spirit speaks into every assembly."
    },
    "7": {
      "L": "And to the angel of the church in Philadelphia write: These things says the holy one, the true one, who has the key of David, who opens and no one shuts, and shuts and no one opens:",
      "M": "And to the angel of the church in Philadelphia write: 'These are the words of the holy one, the true one, who holds the key of David — who opens and no one shuts, and shuts and no one opens:'",
      "T": "To the angel of the assembly in Philadelphia, write: The words come from the Holy and True One — the one who holds the key to David's kingdom, whose opened doors no power can close and whose closed doors no power can open:"
    },
    "8": {
      "L": "I know your works. Behold, I have placed before you an opened door which no one is able to shut, because you have a little power, and you have kept my word, and have not denied my name.",
      "M": "I know your works. Look — I have placed before you an open door that no one is able to shut. For you have a little power, and you have kept my word and have not denied my name.",
      "T": "I see your record. And here is what I have done in response: I set an open door directly before you, and no one in heaven or on earth can close it. You had only small strength — and yet you held fast to my word and never disowned my name."
    },
    "9": {
      "L": "Behold, I give of the synagogue of Satan, those saying they are Jews and are not but lie — behold, I will make them come and bow down before your feet, and know that I have loved you.",
      "M": "Behold, I will make those of the synagogue of Satan — who say they are Jews but are not, who are liars — I will make them come and bow down before your feet, so they will know that I have loved you.",
      "T": "Watch this: those who claim to be God's covenant people but are not — who belong instead to the adversary's assembly and lie about it — I will force them to come and prostrate themselves at your feet. They will have no choice but to acknowledge that you are the ones I love."
    },
    "10": {
      "L": "Because you kept the word of my patience, I also will keep you from the hour of testing which is about to come upon the whole inhabited earth, to test those dwelling on the earth.",
      "M": "Because you have kept my word about patient endurance, I will also keep you from the hour of trial that is coming on the whole world, to try those who dwell on the earth.",
      "T": "You held firm to the call to endure — so I will shelter you through the hour of testing that is about to break over the entire world, the great ordeal that will put to the test every soul that has made this present age its home."
    },
    "11": {
      "L": "I come quickly. Hold fast what you have, so that no one may take your crown.",
      "M": "I am coming soon. Hold fast to what you have, so that no one may seize your crown.",
      "T": "My arrival is near. Grip what you have been given — let no one snatch the victor's crown before you cross the finish line."
    },
    "12": {
      "L": "The one overcoming, I will make him a pillar in the temple of my God, and he will go out from it no more; and I will write upon him the name of my God and the name of the city of my God, the new Jerusalem which comes down out of heaven from my God, and my own new name.",
      "M": "The one who overcomes, I will make him a pillar in the temple of my God. He will never go out of it again. And I will write on him the name of my God, and the name of the city of my God — the new Jerusalem, which comes down from heaven from my God — and my own new name.",
      "T": "The victor I will set as a pillar in the sanctuary of my God — rooted, permanent, never displaced again. On him I will inscribe three names: the name of my God; the name of my God's city, the new Jerusalem that descends out of heaven from my God; and my own new name. He will bear my identity inscribed on his very person."
    },
    "13": {
      "L": "The one having an ear, let him hear what the Spirit says to the churches.",
      "M": "Let anyone who has an ear hear what the Spirit is saying to the churches.",
      "T": "If you have ears, put them to use: this is what the Spirit speaks into every assembly."
    },
    "14": {
      "L": "And to the angel of the church in Laodicea write: These things says the Amen, the faithful and true witness, the beginning of the creation of God:",
      "M": "And to the angel of the church in Laodicea write: 'These are the words of the Amen, the faithful and true witness, the beginning of God's creation:'",
      "T": "To the angel of the assembly in Laodicea, write: These words come from the Amen — the one who is himself the faithful and truthful witness, the source and sovereign of all that God has made:"
    },
    "15": {
      "L": "I know your works, that you are neither cold nor hot. I wish you were cold or hot.",
      "M": "I know your works: you are neither cold nor hot. Would that you were either cold or hot!",
      "T": "I see your record — and it is tepid in every direction. You have neither the cold clarity of opposition nor the burning heat of devotion. I would prefer you were decisively one or the other."
    },
    "16": {
      "L": "So, because you are lukewarm and neither hot nor cold, I am about to spew you out of my mouth.",
      "M": "So, because you are lukewarm, and neither hot nor cold, I will spit you out of my mouth.",
      "T": "But tepid water is nauseating. Because you are neither hot nor cold — just lukewarm — I am on the verge of spitting you out entirely."
    },
    "17": {
      "L": "Because you say, 'I am rich and I have grown wealthy and I have need of nothing,' and you do not know that you are the wretched one and pitiable one and poor one and blind one and naked one,",
      "M": "For you say, 'I am rich, I have prospered, and I need nothing,' not knowing that you are wretched, pitiable, poor, blind, and naked.",
      "T": "You have told yourself: rich, prosperous, self-sufficient — no needs whatsoever. The truth you cannot see is that in my sight you are wretched, pitiable, bankrupt, blind, and stripped bare."
    },
    "18": {
      "L": "I counsel you to buy from me gold refined by fire, that you may be rich, and white garments that you may clothe yourself and the shame of your nakedness may not be revealed, and eyesalve to anoint your eyes that you may see.",
      "M": "I counsel you to buy from me gold refined by fire, so that you may be rich, and white garments so that you may clothe yourself and the shame of your nakedness may not be seen, and salve to anoint your eyes, so that you may see.",
      "T": "Here is my counsel — at the cost only of your self-deception: come to me for gold that has actually passed through fire, real wealth that endures. Come for the white garments of the redeemed, to cover what your prosperity has left bare. And come for the eye-salve that restores sight — because right now you cannot see yourself as you truly are."
    },
    "19": {
      "L": "As many as I love, I rebuke and discipline. Be zealous therefore and repent.",
      "M": "Those whom I love, I rebuke and discipline. So be zealous and repent.",
      "T": "Everyone I love, I confront and correct — that is the nature of this love. So receive this word for what it is: an act of care. Fire up your devotion and turn back around."
    },
    "20": {
      "L": "Behold, I stand at the door and knock. If anyone hears my voice and opens the door, I will come in to him and will dine with him, and he with me.",
      "M": "Behold, I stand at the door and knock. If anyone hears my voice and opens the door, I will come in to him and eat with him, and he with me.",
      "T": "Listen: I have taken my place at the door of your assembly and I am knocking. If any one of you hears my voice and opens, I will enter — and we will share a meal together, the intimate table fellowship I intend for us."
    },
    "21": {
      "L": "The one overcoming, I will give to him to sit with me on my throne, as I also overcame and sat down with my Father on his throne.",
      "M": "The one who overcomes, I will grant him to sit with me on my throne, as I also overcame and sat down with my Father on his throne.",
      "T": "The victor earns the unimaginable: a seat beside me on my own throne. I won that seat by overcoming — and I offer the same throne-share to anyone who walks that same path."
    },
    "22": {
      "L": "The one having an ear, let him hear what the Spirit says to the churches.",
      "M": "Let anyone who has an ear hear what the Spirit is saying to the churches.",
      "T": "If you have ears, put them to use: this is what the Spirit speaks into every assembly."
    }
  },
  "4": {
    "1": {
      "L": "After these things I looked, and behold, a door standing open in heaven, and the first voice which I heard as a trumpet speaking with me, saying, 'Come up here, and I will show you what must take place after these things.'",
      "M": "After this I looked, and behold, a door was standing open in heaven. And the first voice, which I had heard speaking to me like a trumpet, said, 'Come up here, and I will show you what must take place after this.'",
      "T": "After the letters I looked up — and there was a door standing open in heaven. The same voice I had heard before, trumpet-clear and commanding, spoke to me: 'Come up. I have things to show you — things that must happen after all this.'"
    },
    "2": {
      "L": "Immediately I was in the Spirit, and behold, a throne was set in heaven, and upon the throne one sitting.",
      "M": "At once I was in the Spirit, and behold, a throne stood in heaven, with one seated on the throne.",
      "T": "In an instant the Spirit carried me up — and there it was: a throne, fixed and immovable, set in heaven. And on it, someone seated."
    },
    "3": {
      "L": "And the one sitting was in appearance like jasper and carnelian, and a rainbow was around the throne in appearance like an emerald.",
      "M": "And he who sat there had the appearance of jasper and carnelian, and around the throne was a rainbow that had the appearance of an emerald.",
      "T": "The one enthroned — I could not put a face to him; I can only describe light and color: the white fire of jasper, the deep red of carnelian. And ringing the throne, a rainbow of emerald green — the ancient sign of covenant mercy encircling the seat of absolute power."
    },
    "4": {
      "L": "And around the throne were twenty-four thrones, and on the thrones twenty-four elders sitting, clothed in white garments, and on their heads crowns of gold.",
      "M": "Around the throne were twenty-four thrones, and seated on the thrones were twenty-four elders, clothed in white garments, with golden crowns on their heads.",
      "T": "Encircling the great throne were twenty-four lesser thrones, and on each one an elder sat — white-robed, crowned with gold. The full company of God's people, represented and enthroned in honor around the center of all things."
    },
    "5": {
      "L": "And from the throne proceed lightnings and voices and thunders, and seven torches of fire burning before the throne, which are the seven Spirits of God.",
      "M": "From the throne came flashes of lightning, and rumblings and peals of thunder, and before the throne were burning seven torches of fire, which are the seven Spirits of God.",
      "T": "The throne crackled with storm — lightning, deep rumblings, peals of thunder. Before it blazed seven torches of fire, each flame an aspect of the sevenfold Spirit of God, burning in his presence."
    },
    "6": {
      "L": "And before the throne as it were a sea of glass like crystal; and in the midst of the throne and around the throne, four living creatures full of eyes in front and behind.",
      "M": "And before the throne there was as it were a sea of glass, like crystal. And around the throne, on each side, were four living creatures, full of eyes in front and behind.",
      "T": "Before the throne stretched something like a vast floor of glass — clear as crystal, a sea of perfect calm and transparency. And clustered around the throne on every side: four living creatures, covered in eyes front and back, seeing everything, nothing hidden from them."
    },
    "7": {
      "L": "And the first living creature was like a lion, and the second living creature like an ox, and the third living creature having a face as of a man, and the fourth living creature like a flying eagle.",
      "M": "The first living creature was like a lion, the second living creature like an ox, the third living creature had a face like a man, and the fourth living creature was like a flying eagle.",
      "T": "The first bore the face of a lion — wild, sovereign, fierce. The second, an ox — patient, powerful, bearing every burden. The third wore a human face. The fourth blazed with wings outstretched like an eagle in full flight. All of creation's modes of life, gathered into worship."
    },
    "8": {
      "L": "And the four living creatures, each one of them having six wings, are full of eyes around and within; and they rest not day and night, saying, 'Holy, holy, holy, Lord God the Almighty, who was and who is and who is to come.'",
      "M": "And the four living creatures, each of them with six wings, are full of eyes all around and within, and day and night they never cease saying, 'Holy, holy, holy, is the Lord God the Almighty, who was and is and is to come!'",
      "T": "Six wings each — and even the inner surfaces of the wings are covered in eyes, all-seeing. Without pause, day and night without end, they pour out the ancient cry: 'Holy — holy — holy! Lord God, the All-Sovereign! The one who was, who is, and who is always coming toward us!'"
    },
    "9": {
      "L": "And when the living creatures give glory and honor and thanks to the one sitting on the throne, who lives unto the ages of ages,",
      "M": "And whenever the living creatures give glory and honor and thanks to him who is seated on the throne, who lives forever and ever,",
      "T": "And whenever the living creatures break forth in glory and honor and gratitude toward the one enthroned — the one whose life stretches into ages beyond all counting —"
    },
    "10": {
      "L": "the twenty-four elders fall down before the one sitting on the throne, and worship the one living unto the ages of ages, and cast their crowns before the throne, saying,",
      "M": "the twenty-four elders fall down before him who is seated on the throne and worship him who lives forever and ever. They cast their crowns before the throne, saying,",
      "T": "— the twenty-four elders collapse face down before the eternally living one. They fling their golden crowns down at the foot of his throne — surrendering even the honors given to them — and cry out:"
    },
    "11": {
      "L": "'Worthy are you, our Lord and God, to receive the glory and the honor and the power, because you created all things, and by your will they were and they were created.'",
      "M": "'Worthy are you, our Lord and God, to receive glory and honor and power, for you created all things, and by your will they existed and were created.'",
      "T": "'You alone are worthy of glory, honor, and all power — you are our Lord and God. Everything that exists came into being because you willed it. Creation is your act; it persists by your ongoing choice. All praise belongs to you, and to you alone.'"
    }
  },
  "5": {
    "1": {
      "L": "And I saw upon the right hand of the one sitting on the throne a scroll written within and on the back, sealed with seven seals.",
      "M": "Then I saw in the right hand of him who was seated on the throne a scroll written on the inside and on the back, sealed with seven seals.",
      "T": "In the right hand of the one enthroned, I saw a scroll — both sides written full, not one blank space remaining. And fastened shut with seven seals."
    },
    "2": {
      "L": "And I saw a strong angel proclaiming with a great voice, 'Who is worthy to open the scroll and to loosen its seals?'",
      "M": "And I saw a mighty angel proclaiming with a loud voice, 'Who is worthy to open the scroll and break its seals?'",
      "T": "A powerful angel stepped forward and hurled the question out in all directions: 'Who is worthy? Who has what it takes to open this scroll and break its seals?'"
    },
    "3": {
      "L": "And no one in heaven or on earth or under the earth was able to open the scroll or to look upon it.",
      "M": "And no one in heaven or on earth or under the earth was able to open the scroll or to look into it.",
      "T": "Silence. Across all of heaven, all the earth, and all the depths below — not one qualified. No one could open it. No one could even look at it."
    },
    "4": {
      "L": "And I wept greatly, because no one was found worthy to open the scroll or to look upon it.",
      "M": "And I began to weep loudly because no one was found worthy to open the scroll or to look into it.",
      "T": "I broke down weeping — loud, uncontrolled grief — because it seemed the scroll would stay sealed forever. No one was found worthy."
    },
    "5": {
      "L": "And one of the elders says to me, 'Do not weep; behold, the Lion of the tribe of Judah, the Root of David, has overcome, to open the scroll and its seven seals.'",
      "M": "And one of the elders said to me, 'Weep no more; behold, the Lion of the tribe of Judah, the Root of David, has conquered, so that he can open the scroll and its seven seals.'",
      "T": "But one of the elders stopped me: 'No more tears. Look — the Lion of Judah's tribe, the one who springs from David's root, promised from Genesis and Isaiah — he has won. He conquered. And that victory has earned him the right to open the scroll and shatter every seal.'"
    },
    "6": {
      "L": "And I saw in the midst of the throne and of the four living creatures and in the midst of the elders a Lamb standing, as having been slain, having seven horns and seven eyes, which are the seven Spirits of God sent out into all the earth.",
      "M": "And between the throne and the four living creatures and among the elders I saw a Lamb standing, as though it had been slain, with seven horns and with seven eyes, which are the seven Spirits of God sent out into all the earth.",
      "T": "I looked for the Lion. What I saw instead was a Lamb — standing upright, but carrying the unmistakable marks of slaughter. Seven horns: the fullness of sovereign power. Seven eyes: the sevenfold Spirit of God, sent out as a searching light across every corner of the earth."
    },
    "7": {
      "L": "And he came and took out of the right hand of the one sitting on the throne.",
      "M": "And he went and took the scroll from the right hand of him who was seated on the throne.",
      "T": "He stepped forward. He reached up and took the scroll right out of the right hand of the one on the throne."
    },
    "8": {
      "L": "And when he had taken the scroll, the four living creatures and the twenty-four elders fell down before the Lamb, each having a harp and golden bowls full of incense, which are the prayers of the saints.",
      "M": "And when he had taken the scroll, the four living creatures and the twenty-four elders fell down before the Lamb, each holding a harp and golden bowls full of incense, which are the prayers of the saints.",
      "T": "The moment he took it, the four living creatures and all twenty-four elders went down before the Lamb. Each held a harp and a golden bowl of incense — and the incense was the accumulated prayers of God's people, rising at last before the throne."
    },
    "9": {
      "L": "And they sing a new song, saying, 'Worthy are you to take the scroll and to open its seals, because you were slain, and you purchased for God by your blood from every tribe and tongue and people and nation,'",
      "M": "And they sang a new song, saying, 'Worthy are you to take the scroll and to open its seals, for you were slain, and by your blood you ransomed people for God from every tribe and language and people and nation,'",
      "T": "And they broke into a new song — something that had never been sung before, because what it celebrates had never happened before: 'You are worthy — because you were slaughtered, and your blood was the purchase price that bought people out of bondage for God. From every tribe, language, people, and nation — you gathered them.'"
    },
    "10": {
      "L": "'and you made them a kingdom and priests to our God, and they shall reign on the earth.'",
      "M": "'and you have made them a kingdom and priests to our God, and they shall reign on the earth.'",
      "T": "'You remade them entirely: a kingdom — not subjects but co-regents. Priests — not spectators but those who draw near to God. And they will reign, here on this very earth, in the age to come.'"
    },
    "11": {
      "L": "And I saw, and I heard the voice of many angels around the throne and the living creatures and the elders, and the number of them was ten thousand times ten thousand and thousands of thousands,",
      "M": "Then I looked, and I heard around the throne and the living creatures and the elders the voice of many angels, numbering myriads of myriads and thousands of thousands,",
      "T": "I looked again — and heard it: an ocean of voices. Angels beyond all numbering, ringing the throne, surrounding the living creatures and the elders. Tens of millions upon tens of millions, thousands upon thousands."
    },
    "12": {
      "L": "saying with a great voice, 'Worthy is the Lamb who was slain to receive power and riches and wisdom and strength and honor and glory and blessing!'",
      "M": "saying with a loud voice, 'Worthy is the Lamb who was slain, to receive power and wealth and wisdom and might and honor and glory and blessing!'",
      "T": "And with one tremendous voice they declared: 'The Lamb who was slaughtered is worthy of everything — all power, all wealth, all wisdom, all might, all honor, all glory, all blessing. Every category of greatness belongs to him.'"
    },
    "13": {
      "L": "And every creature which is in heaven and on the earth and under the earth and on the sea, and all the things in them, I heard saying, 'To the one sitting on the throne and to the Lamb be blessing and honor and glory and might unto the ages of ages!'",
      "M": "And I heard every creature in heaven and on earth and under the earth and in the sea, and all that is in them, saying, 'To him who sits on the throne and to the Lamb be blessing and honor and glory and might forever and ever!'",
      "T": "Then everything joined in. Every creature, from every realm — heaven above, earth below, the depths beneath the earth, and the sea. All of them together, in one chorus: 'To the one on the throne and to the Lamb — blessing, honor, glory, and power — to the ages of ages, without end!'"
    },
    "14": {
      "L": "And the four living creatures said, 'Amen,' and the elders fell down and worshipped.",
      "M": "And the four living creatures said, 'Amen!' and the elders fell down and worshiped.",
      "T": "The four living creatures sealed it with a thundered 'Amen.' And the elders went down in worship."
    }
  },
  "6": {
    "1": {
      "L": "And I saw when the Lamb opened one of the seven seals, and I heard one of the four living creatures saying as with a voice of thunder, 'Come!'",
      "M": "Now I watched when the Lamb opened one of the seven seals, and I heard one of the four living creatures say with a voice like thunder, 'Come!'",
      "T": "I watched as the Lamb broke open the first of the seven seals. One of the four living creatures spoke — voice like rolling thunder: 'Come!'"
    },
    "2": {
      "L": "And I looked, and behold, a white horse, and the one sitting on it having a bow; and a crown was given to him, and he went out conquering and to conquer.",
      "M": "And I looked, and behold, a white horse! And its rider had a bow, and a crown was given to him, and he came out conquering, and to conquer.",
      "T": "I looked — a white horse, and on it a rider with a bow. A crown was given him — his authority was granted, not self-assumed — and he rode out with a single intent: to conquer, and to keep conquering."
    },
    "3": {
      "L": "And when he opened the second seal, I heard the second living creature saying, 'Come!'",
      "M": "When he opened the second seal, I heard the second living creature say, 'Come!'",
      "T": "The second seal broke open. The second living creature's call rang out: 'Come!'"
    },
    "4": {
      "L": "And there went out another horse, fiery red, and to the one sitting on it was given to take peace from the earth, and that they should slay one another, and there was given to him a great sword.",
      "M": "And out came another horse, bright red. Its rider was permitted to take peace from the earth, so that people should slay one another, and he was given a great sword.",
      "T": "A red horse — the color of blood — surged out. The rider was granted permission to strip peace from the earth, leaving behind only the violence of human beings turning on each other. In his hand, a great sword — the divine passive marking that this too is within God's governance."
    },
    "5": {
      "L": "And when he opened the third seal, I heard the third living creature saying, 'Come.' And I looked, and behold, a black horse, and the one sitting on it having a balance in his hand.",
      "M": "When he opened the third seal, I heard the third living creature say, 'Come!' And I looked, and behold, a black horse! And its rider had a pair of scales in his hand.",
      "T": "The third seal. The living creature's call: 'Come!' A black horse appeared, and its rider gripped a pair of scales — the instrument of rationing, of grain measured out in desperate scarcity."
    },
    "6": {
      "L": "And I heard as it were a voice in the midst of the four living creatures saying, 'A measure of wheat for a denarius, and three measures of barley for a denarius; and the oil and the wine do not hurt.'",
      "M": "And I heard what seemed to be a voice in the midst of the four living creatures, saying, 'A quart of wheat for a denarius, and three quarts of barley for a denarius, and do not harm the oil and wine!'",
      "T": "A voice rang out from within the ring of living creatures, announcing the terms of famine: a whole day's wages for one day's worth of wheat — enough for one person. Three times the grain for the same price if you buy barley, the poor man's staple. But the oil and wine — the luxuries of those who already have enough — left untouched."
    },
    "7": {
      "L": "And when he opened the fourth seal, I heard the voice of the fourth living creature saying, 'Come!'",
      "M": "When he opened the fourth seal, I heard the voice of the fourth living creature say, 'Come!'",
      "T": "The fourth seal broke open. The fourth living creature spoke: 'Come!'"
    },
    "8": {
      "L": "And I looked, and behold, a pale horse, and the one sitting on it — his name is Death, and Hades follows with him. And authority was given to them over a fourth of the earth, to kill by sword and by famine and by death and by the wild beasts of the earth.",
      "M": "And I looked, and behold, a pale horse! And its rider's name was Death, and Hades followed him. And they were given authority over a fourth of the earth, to kill with sword and with famine and with pestilence and by the wild beasts of the earth.",
      "T": "A sickly pale horse — the color of a corpse. The rider's name was Death, and right behind him came Hades, the grave itself, ready to receive what Death left behind. Together they were granted authority over a quarter of the earth: to kill by violence, by starvation, by plague, and by the teeth of wild animals — the four instruments of judgment that echo the prophet Ezekiel."
    },
    "9": {
      "L": "And when he opened the fifth seal, I saw under the altar the souls of those who had been slain for the word of God and for the testimony which they held.",
      "M": "When he opened the fifth seal, I saw under the altar the souls of those who had been slain for the word of God and for the witness they had borne.",
      "T": "The fifth seal broke open — and what appeared was not a horse or a rider, but something else entirely: beneath the heavenly altar, the souls of those who had been killed for holding to God's word and refusing to abandon their testimony. Their blood had been poured out like a sacrifice, and here they waited."
    },
    "10": {
      "L": "And they cried with a great voice, saying, 'How long, O Master, holy and true, do you not judge and avenge our blood upon those dwelling on the earth?'",
      "M": "They cried out with a loud voice, 'O Sovereign Lord, holy and true, how long before you will judge and avenge our blood on those who dwell on the earth?'",
      "T": "They called out with the full weight of their waiting: 'How long, Absolute Sovereign — you who are perfectly holy and completely true — how long before you judge? Before you call those who shed our blood to account?'"
    },
    "11": {
      "L": "And there was given to each of them a white robe, and it was said to them that they should rest still a little time, until both their fellow servants and their brothers who are about to be killed as also they were should be completed.",
      "M": "Then they were each given a white robe and told to rest a little longer, until the number of their fellow servants and their brothers should be complete — those who were to be killed as they themselves had been.",
      "T": "Each of them was given a white robe — the honored garment of the vindicated. And the answer to their question came: wait a little longer. There is a full number yet to be completed — fellow servants and brothers still to be killed, just as they were. When that number reaches its appointed fullness, judgment will come."
    },
    "12": {
      "L": "And I saw when he opened the sixth seal, and there was a great earthquake, and the sun became black as sackcloth of hair, and the whole moon became as blood,",
      "M": "When he opened the sixth seal, I looked, and behold, there was a great earthquake, and the sun became black as sackcloth, the full moon became like blood,",
      "T": "The sixth seal broke — and the world began to come undone. A catastrophic earthquake. The sun went black, not dimmed but extinguished, like a sheet of coarse sackcloth drawn across the sky. The moon turned the color of blood."
    },
    "13": {
      "L": "and the stars of heaven fell to the earth, as a fig tree casts its unripe figs when shaken by a great wind.",
      "M": "and the stars of the sky fell to the earth as the fig tree sheds its winter fruit when shaken by a gale.",
      "T": "The stars fell from heaven to earth — the way a fig tree stripped by a violent storm shakes every last unripe fruit loose at once, leaving itself bare in a single gust."
    },
    "14": {
      "L": "And the heaven was separated as a scroll being rolled up, and every mountain and island was removed from its places.",
      "M": "The sky vanished like a scroll that is being rolled up, and every mountain and island was removed from its place.",
      "T": "The sky itself split apart and rolled back like a scroll being wound shut. Every mountain shifted. Every island was torn from the sea floor. The familiar face of the earth dissolved."
    },
    "15": {
      "L": "And the kings of the earth and the great men and the commanders and the rich and the powerful and every slave and free man hid themselves in the caves and in the rocks of the mountains,",
      "M": "Then the kings of the earth and the great ones and the generals and the rich and the powerful, and everyone, slave and free, hid themselves in the caves and among the rocks of the mountains,",
      "T": "No rank or status offered any shelter. Kings, the powerful and great, military commanders, the wealthy — every layer of human hierarchy — fled for cover. And every ordinary person too, slave and free alike, scrambled into caves and pressed themselves into mountain clefts."
    },
    "16": {
      "L": "and they say to the mountains and to the rocks, 'Fall on us and hide us from the face of the one sitting on the throne and from the wrath of the Lamb;'",
      "M": "calling to the mountains and rocks, 'Fall on us and hide us from the face of him who is seated on the throne, and from the wrath of the Lamb,'",
      "T": "And they begged the mountains to bury them alive. They cried out to the rocks: 'Fall on us — crush us — anything to hide us from the face of the one on the throne. From the wrath of the Lamb.'"
    },
    "17": {
      "L": "'because the great day of their wrath has come, and who is able to stand?'",
      "M": "'for the great day of their wrath has come, and who is able to stand?'",
      "T": "'The great day of wrath has arrived — the wrath of the one on the throne and the wrath of the Lamb together. And not one soul is able to stand before it.'"
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'revelation')
        merge_tier(existing, REVELATION, tier_key)
        save(tier_dir, 'revelation', existing)
    print('Revelation 3–6 written.')

if __name__ == '__main__':
    main()
