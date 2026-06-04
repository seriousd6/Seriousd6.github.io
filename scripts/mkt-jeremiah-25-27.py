"""
MKT Jeremiah chapters 25–27 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-jeremiah-25-27.py

Translation decisions (consistent with mkt-jeremiah-1-3.py through mkt-jeremiah-19-22.py):

- H3068 (יהוה): "LORD" in L/M; "Yahweh" in T for oracle delivery, divine addresses,
  and the cup scene. Narrative formulas use "Yahweh" in T for immediacy.
- H430 (אֱלֹהִים): "God" in all tiers; "other gods" for foreign deities.
- H5019 (נְבוּכַדְרֶאצַּר): Hebrew preserves Aramaic-influenced spelling. "Nebuchadrezzar"
  in L; "Nebuchadnezzar" in M/T for recognizability.
- H5650 (עֶבֶד, servant): Both 25:9 and 27:6 call Nebuchadnezzar "my servant" —
  a deliberately shocking theological claim. Preserved as "my servant" in all three
  tiers; T surfaces the weight: Yahweh uses a pagan empire as his instrument of judgment.
- H3709 (כּוֹס, cup): 25:15–29 — the cup of wrath sign-act. "Cup" in all tiers; T
  connects the image to its broader prophetic and apocalyptic resonance.
- H8339 (שֵׁשַׁךְ, Sheshach): 25:26 — atbash cipher for Babylon (š→b, k→l in reverse
  Hebrew alphabet). Preserved as proper name "Sheshach" in L/M; T surfaces the cipher
  explicitly: "Sheshach — code for Babylon."
- H7657 (שִׁבְעִים, seventy): The 70-year prophecy (25:11–12) is preserved simply as
  "seventy" in all tiers; T notes the theological weight: a bounded, finite judgment.
- H7307 (רוּחַ): 25:32 — "a great whirlwind/tempest" — physical weather, not Spirit.
- H1471 (גּוֹי): "nations" in all tiers.
- H5030 (נָבִיא, prophet): "prophet/prophets" in all tiers; "false prophets" only in T
  where clarity requires it.
- H2534/H7110 (חֵמָה/קֶצֶף): "wrath" and "fury" by context; H2534 (burning heat/wrath)
  = "fierce anger" or "burning wrath" in T.
- H4687 (מִצְוָה, commandment): "law" in M for 26:4 (the Torah of Moses); T uses "Torah"
  to preserve the covenant-instruction sense.
- H3627 (כְּלִי, vessel/jar): 25:34 — "precious vessel" — same imagery as the shattered
  potter's flask of ch. 19 and the rejected jar of 22:28 (Coniah). Rendered "precious
  vessel" in L; "fine vessel" in M; T connects the recurring pottery motif explicitly.

Textual notes:
- 27:1 — The MT reads "Jehoiakim son of Josiah" but the chapter's events clearly belong
  to Zedekiah's reign (vv. 3, 12; cf. 28:1). The LXX reads "Zedekiah." Almost certainly
  a scribal error (influenced by 26:1). L follows MT ("Jehoiakim"); M/T correct to
  "Zedekiah" per context and LXX. The discrepancy is documented here.
- 25:13 — "all that is written in this book" — a rare self-referential editorial seam;
  widely regarded as the conclusion of an early Jeremianic collection.
- 26:18 — Quotes Micah 3:12 verbatim — the only OT instance of one prophet citing
  another by name with a direct quotation.
- 25:34 — "precious vessel / fine vessel": same H3627 + H2532 (kělî ḥemdâ) as 22:28
  (Coniah = the worthless vessel). The T tier connects both passages.

Structural notes:
  Ch. 25 divides into:
    vv. 1–7:   Retrospective indictment (23 years of unheeded prophecy, 627–605 BCE)
    vv. 8–14:  Babylon as Yahweh's instrument; the 70-year judgment period
    vv. 15–29: The Cup of Wrath sign-act — Jeremiah as cosmic steward of judgment
    vv. 30–38: The divine warrior roars — cosmic judgment hymn

  Ch. 26: The Temple Sermon's legal aftermath. Trial structure:
    vv. 1–6:   Commission and content of the temple sermon
    vv. 7–11:  Arrest; charge of capital prophesy
    vv. 12–15: Jeremiah's defense — I was sent; innocent blood is on you if you kill me
    vv. 16–19: Acquittal; elders invoke the Micah precedent (Micah 3:12)
    vv. 20–24: Counter-narrative of Uriah — executed for the same message;
               Ahikam protects Jeremiah

  Ch. 27: The yoke sign-act — submit to Babylon or die.
    vv. 1–11:  Yoke made; message to surrounding nations via their ambassadors
    vv. 12–15: Direct address to Zedekiah
    vv. 16–22: Message to priests and people: the vessels will not return soon

OT echoes:
  25:4–5 — "rising early and sending" is a Jeremiah refrain (7:13,25; 11:7; 32:33;
    35:14,15; 44:4) — a formula for God's persistent, unrequited appeal.
  25:11–12 — Fulfilled (in one reading) when Cyrus issues the edict 538 BCE
    (2 Chr 36:21–23; Ezra 1:1; cf. Dan 9:2 where Daniel reads this very passage).
  25:15 — "Cup of wrath" echoes Ps 75:8; Isa 51:17,22; Hab 2:16; and reaches its
    fullest form in Rev 14:10, 16:19, 18:6.
  25:30 — "The LORD will roar from on high" echoes Amos 1:2 and Joel 3:16. Grape-
    treading image echoes Isa 63:1–6 (the divine warrior blood-stained from battle).
  27:5 — "By my great power and my outstretched arm" — the Exodus formula reversed
    (Deut 4:34; 5:15; 26:8): in the Exodus God fought FOR Israel with outstretched arm;
    now that same arm bestows all nations on Nebuchadnezzar. Consistent with 21:5.
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
            if v not in existing[ch]:
                existing[ch][v] = tiers[tier_key]

JEREMIAH = {
  "25": {
    "1": {
      "L": "The word that came to Jeremiah concerning all the people of Judah in the fourth year of Jehoiakim son of Josiah, king of Judah — that was the first year of Nebuchadrezzar king of Babylon —",
      "M": "This is the word that came to Jeremiah concerning all the people of Judah in the fourth year of Jehoiakim son of Josiah, king of Judah — which was the first year of Nebuchadnezzar king of Babylon.",
      "T": "This is the word Yahweh gave to Jeremiah about all the people of Judah — in the fourth year of Jehoiakim son of Josiah, which was the first year of Nebuchadnezzar king of Babylon."
    },
    "2": {
      "L": "which Jeremiah the prophet spoke to all the people of Judah and to all the inhabitants of Jerusalem, saying:",
      "M": "Jeremiah the prophet spoke it to all the people of Judah and to all the people of Jerusalem:",
      "T": "Jeremiah the prophet addressed it to all the people of Judah and all the inhabitants of Jerusalem:"
    },
    "3": {
      "L": "From the thirteenth year of Josiah son of Amon, king of Judah, to this day — these twenty-three years — the word of the LORD has come to me, and I have spoken to you rising early and speaking, but you have not listened.",
      "M": "From the thirteenth year of Josiah son of Amon, king of Judah, to this very day — twenty-three years — the word of the LORD has been coming to me, and I have spoken to you persistently, but you have not listened.",
      "T": "For twenty-three years — from the thirteenth year of Josiah son of Amon until this very day — the word of Yahweh has been coming to me. I have been speaking it to you, rising early, pressing it upon you. But you have not listened."
    },
    "4": {
      "L": "And the LORD has sent to you all his servants the prophets, sending them persistently — but you have not listened or inclined your ear to hear —",
      "M": "The LORD has persistently sent you all his servants the prophets, but you have not listened or paid attention —",
      "T": "Yahweh sent you prophet after prophet — his servants, sent urgently and repeatedly. But you would not listen. You would not even turn your ear toward them."
    },
    "5": {
      "L": "saying: Turn now every one of you from your evil way and from the evil of your deeds, and dwell upon the land that the LORD has given to you and your fathers for ever and ever.",
      "M": "They said: Turn back, each of you, from your evil way and from your wicked deeds, and live in the land that the LORD gave to you and your ancestors for ever and ever.",
      "T": "The message was always the same: Turn — every one of you — from your evil path, from the wrong you are doing. Live in the land Yahweh gave you and your ancestors, the land meant to be yours forever."
    },
    "6": {
      "L": "Do not go after other gods to serve them and worship them, and do not provoke me to anger with the work of your hands. Then I will do you no harm.",
      "M": "Do not follow other gods to serve and worship them, and do not provoke me to anger with what your hands have made. Then I will not harm you.",
      "T": "Do not run after other gods to serve them and bow down to them. Do not goad me to anger with the things your hands have made. Turn, and I will not harm you."
    },
    "7": {
      "L": "Yet you have not listened to me, declares the LORD, so that you have provoked me to anger with the work of your hands, to your own harm.",
      "M": "But you have not listened to me, declares the LORD, and you have provoked me to anger with what your hands have made — to your own ruin.",
      "T": "But you did not listen, says Yahweh. You kept provoking me with your idols — and the harm falls on you."
    },
    "8": {
      "L": "Therefore thus says the LORD of hosts: Because you have not obeyed my words,",
      "M": "Therefore this is what the LORD of hosts says: Because you have not obeyed my words —",
      "T": "So Yahweh of hosts says: Because you have not obeyed —"
    },
    "9": {
      "L": "behold, I will send for and take all the clans of the north, declares the LORD, and I will send for Nebuchadrezzar king of Babylon, my servant, and I will bring them against this land and its inhabitants and against all these surrounding nations. I will devote them to destruction and make them a horror, a hissing, and everlasting desolations.",
      "M": "I am going to summon all the peoples of the north, declares the LORD, and I will bring Nebuchadnezzar king of Babylon, my servant, and all his forces against this land and its people and all these neighboring nations. I will devote them to destruction and make them an object of horror, of scorn, and of everlasting desolation.",
      "T": "I am calling up every clan from the north, says Yahweh — and I am calling up Nebuchadnezzar king of Babylon, my servant. I will bring them against this land, its people, and all the nations around it. I will place them under the ban of destruction and make them a horror, a contempt, a permanent wasteland."
    },
    "10": {
      "L": "Moreover I will banish from them the sound of mirth and the sound of gladness, the voice of the bridegroom and the voice of the bride, the grinding of the millstones and the light of the lamp.",
      "M": "I will silence among them the sounds of joy and gladness, the voice of the bridegroom and the bride, the grinding of the millstones and the light of the lamp.",
      "T": "I will take away every sound of joy — the laughter, the celebration, the voices of bride and bridegroom, the grind of millstones in the morning, the lamp-light at night. All of it silenced."
    },
    "11": {
      "L": "And this whole land shall become a ruin and a waste, and these nations shall serve the king of Babylon seventy years.",
      "M": "This whole land will become a desolate wasteland, and these nations will serve the king of Babylon for seventy years.",
      "T": "This whole land will become a wasteland, and all these nations will be subject to the king of Babylon for seventy years — a bounded, finite judgment, not an open-ended destruction."
    },
    "12": {
      "L": "Then after seventy years are accomplished, I will punish the king of Babylon and that nation, the land of the Chaldeans, for their iniquity, declares the LORD, and will make it an everlasting desolation.",
      "M": "But when seventy years are over, I will punish the king of Babylon and that nation, the land of the Chaldeans, for their guilt, declares the LORD, and I will make it a desolation forever.",
      "T": "But when those seventy years are complete, I will call Babylon to account — king, nation, land of the Chaldeans — for their own guilt. The oppressor of nations will itself be made a ruin forever."
    },
    "13": {
      "L": "I will bring upon that land all my words that I have spoken against it — all that is written in this book, which Jeremiah has prophesied against all the nations.",
      "M": "I will bring upon that land everything I have spoken against it — all that is recorded in this book, which Jeremiah prophesied against all the nations.",
      "T": "Every word I have spoken against Babylon I will bring to pass — everything written in this book, all that Jeremiah has prophesied against the nations."
    },
    "14": {
      "L": "For many nations and great kings shall make them their servants; and I will repay them according to their deeds and according to the work of their hands.",
      "M": "For many nations and great kings will enslave them in turn, and I will repay them according to their deeds and the work of their hands.",
      "T": "Many nations and great kings will make Babylon serve them. And I will repay Babylon exactly according to what they have done — deeds for deeds, hand for hand."
    },
    "15": {
      "L": "Thus says the LORD, the God of Israel, to me: Take from my hand this cup of the wine of wrath, and make all the nations to whom I send you drink it.",
      "M": "This is what the LORD, the God of Israel, said to me: Take this cup of the wine of wrath from my hand, and make all the nations to whom I send you drink it.",
      "T": "Yahweh, God of Israel, said to me: Take this cup from my hand — the cup of the wine of my wrath — and make every nation I send you to drink from it."
    },
    "16": {
      "L": "They shall drink and stagger and be maddened, because of the sword that I am sending among them.",
      "M": "They will drink, and reel, and go out of their minds, because of the sword I am sending among them.",
      "T": "They will drink and stagger and lose their minds — driven mad by the sword I am unleashing among them."
    },
    "17": {
      "L": "So I took the cup from the LORD's hand, and made all the nations to whom the LORD sent me drink it:",
      "M": "So I took the cup from the LORD's hand and made all the nations to whom the LORD had sent me drink it:",
      "T": "So I took the cup from Yahweh's hand and went to every nation he sent me to, and I made them drink:"
    },
    "18": {
      "L": "Jerusalem and the cities of Judah, its kings and its princes — to make them a desolation, a waste, a hissing, and a curse, as at this day —",
      "M": "Jerusalem and the cities of Judah, their kings and officials — to make them a ruin and a wasteland, an object of scorn and cursing, as they are to this day —",
      "T": "First, Jerusalem and the towns of Judah — their kings and their leaders — reduced to ruin, to scorn, to a curse that lasts to this day."
    },
    "19": {
      "L": "Pharaoh king of Egypt, his servants, his princes, and all his people;",
      "M": "Pharaoh king of Egypt, his officials, his court, and all his people;",
      "T": "Then Pharaoh king of Egypt — his servants, his officials, all his people."
    },
    "20": {
      "L": "all the mixed peoples; all the kings of the land of Uz; all the kings of the land of the Philistines — Ashkelon, Gaza, Ekron, and the remnant of Ashdod;",
      "M": "all the foreign peoples; all the kings of the land of Uz; all the kings of Philistia — Ashkelon, Gaza, Ekron, and what remains of Ashdod;",
      "T": "All the mixed peoples. The kings of Uz. The kings of Philistia — Ashkelon, Gaza, Ekron, and what is left of Ashdod."
    },
    "21": {
      "L": "Edom, Moab, and the sons of Ammon;",
      "M": "Edom, Moab, and the Ammonites;",
      "T": "Edom. Moab. The Ammonites."
    },
    "22": {
      "L": "all the kings of Tyre, all the kings of Sidon, and the kings of the coastlands across the sea;",
      "M": "all the kings of Tyre, all the kings of Sidon, and the kings of the coastlands beyond the sea;",
      "T": "All the kings of Tyre, all the kings of Sidon, and every king on the islands and coastlands across the sea."
    },
    "23": {
      "L": "Dedan, Tema, Buz, and all who cut the corners of their hair;",
      "M": "Dedan, Tema, Buz, and all who shave their temples;",
      "T": "Dedan, Tema, Buz — all the desert tribes who crop their hair at the temples."
    },
    "24": {
      "L": "all the kings of Arabia and all the kings of the mixed peoples who dwell in the desert;",
      "M": "all the kings of Arabia and all the kings of the various peoples who live in the desert;",
      "T": "All the kings of Arabia. Every king of the mixed peoples scattered through the open desert."
    },
    "25": {
      "L": "all the kings of Zimri, all the kings of Elam, and all the kings of Media;",
      "M": "all the kings of Zimri, all the kings of Elam, all the kings of Media;",
      "T": "The kings of Zimri. The kings of Elam. The kings of Media."
    },
    "26": {
      "L": "all the kings of the north, near and far, one after another — and all the kingdoms of the world that are on the face of the earth. And the king of Sheshach shall drink after them.",
      "M": "all the kings of the north, near and far, one after another — all the kingdoms on the face of the earth. And last of all, the king of Sheshach will drink.",
      "T": "All the kings of the north — near and far, one after another — every kingdom on the face of the earth. And at the end of the list: the king of Sheshach will drink too. Sheshach is the cipher name for Babylon."
    },
    "27": {
      "L": "Then you shall say to them: Thus says the LORD of hosts, the God of Israel — Drink, be drunk, and vomit, fall and rise no more, because of the sword that I am sending among you.",
      "M": "Then say to them: This is what the LORD of hosts, the God of Israel, says — Drink, get drunk and vomit; fall down and never rise again, because of the sword I am sending among you.",
      "T": "Then say to them: Yahweh of hosts, God of Israel, says this — Drink. Get drunk and retch. Fall down and do not get up, because of the sword I am sending among you."
    },
    "28": {
      "L": "And if they refuse to take the cup from your hand to drink, then you shall say to them: Thus says the LORD of hosts — You shall certainly drink!",
      "M": "But if they refuse to take the cup from your hand to drink, say to them: This is what the LORD of hosts says — You must drink!",
      "T": "If they refuse to take the cup from your hand, say to them: Yahweh of hosts says — You will drink. There is no refusal."
    },
    "29": {
      "L": "For behold, I am beginning to bring disaster on the city that is called by my name, and shall you then go unpunished? You shall not go unpunished, for I am calling a sword against all the inhabitants of the earth, declares the LORD of hosts.",
      "M": "For I am already beginning to bring disaster on the city that bears my own name — do you think you will escape judgment? You will not escape, for I am summoning the sword against all who live on earth, declares the LORD of hosts.",
      "T": "I am starting with the city that carries my own name — and if I am doing that to Jerusalem, do you imagine you will go free? You will not. I am summoning the sword against every inhabitant of the earth. Yahweh of hosts has declared it."
    },
    "30": {
      "L": "Therefore prophesy against them all these words, and say to them: The LORD will roar from on high, and from his holy habitation he will utter his voice; he will roar mightily over his fold, and shout like those who tread grapes against all the inhabitants of the earth.",
      "M": "Therefore prophesy all these words against them and say: The LORD will roar from on high; from his holy dwelling he will thunder; he will roar mightily over his flock and shout like the grape-treaders against all who live on earth.",
      "T": "Prophesy all of this against them. Say: Yahweh roars from on high. From his holy dwelling his voice thunders. He roars over his flock like a lion, and shouts against all the inhabitants of the earth the way a grape-treader shouts at harvest — exultant, relentless, the weight of the harvest underfoot."
    },
    "31": {
      "L": "The uproar will reach to the end of the earth, for the LORD has an indictment against the nations; he is entering into judgment with all flesh, and the wicked he has given over to the sword, declares the LORD.",
      "M": "The noise will reach to the ends of the earth, for the LORD brings charges against the nations; he is entering into judgment with all humanity, and the wicked he will hand over to the sword, declares the LORD.",
      "T": "The sound reaches the ends of the earth — because Yahweh has filed his indictment against the nations. He is putting all flesh on trial, and the guilty he is giving over to the sword."
    },
    "32": {
      "L": "Thus says the LORD of hosts: Behold, disaster is going forth from nation to nation, and a great tempest is stirring from the farthest parts of the earth!",
      "M": "This is what the LORD of hosts says: Disaster is spreading from nation to nation, and a great storm is rising from the far reaches of the earth!",
      "T": "Yahweh of hosts says: Calamity is rolling outward from nation to nation, and a great whirlwind is rising from the ends of the earth."
    },
    "33": {
      "L": "Those slain by the LORD on that day shall extend from one end of the earth to the other. They shall not be lamented or gathered or buried; they shall be like dung on the surface of the ground.",
      "M": "Those killed by the LORD on that day will stretch from one end of the earth to the other. No one will mourn them, no one will gather them, no one will bury them — they will lie like dung on the ground.",
      "T": "The dead that day will be strewn from one end of the earth to the other. No lament will be sung for them. No one will gather them. No one will bury them. They will lie like dung on the face of the ground."
    },
    "34": {
      "L": "Wail, you shepherds, and cry out, and roll in the dust, you lords of the flock, for the days of your slaughter have come and are fulfilled, and you shall fall like a precious vessel.",
      "M": "Wail, you shepherds, and cry out! Roll in the dust, you leaders of the flock! For the time of your slaughter has arrived; you will fall and shatter like a fine vessel.",
      "T": "Wail, shepherds — cry out! Roll in the ashes, you who lead the flock! The days of your slaughter have come and cannot be deferred. You will fall and shatter like a precious jar — the same image Jeremiah enacted at Tophet."
    },
    "35": {
      "L": "No refuge will remain for the shepherds, nor escape for the lords of the flock.",
      "M": "The shepherds will have nowhere to flee, and the leaders of the flock no way to escape.",
      "T": "There is no escape for the shepherds, no way out for the leaders of the flock."
    },
    "36": {
      "L": "Hear the cry of the shepherds and the wail of the lords of the flock! For the LORD is laying waste their pasture —",
      "M": "Hear the cry of the shepherds and the wailing of the leaders of the flock! For the LORD is devastating their pasture —",
      "T": "Listen: the cry of the shepherds, the wail of those who led the flock. Yahweh is destroying their pastures."
    },
    "37": {
      "L": "and the peaceful folds are destroyed because of the fierce anger of the LORD.",
      "M": "the peaceful grazing lands are laid waste because of the LORD's fierce anger.",
      "T": "Every quiet pasture is laid waste by the heat of Yahweh's burning anger."
    },
    "38": {
      "L": "Like a lion he has left his lair, for their land has become a waste because of the sword of the oppressor and because of his fierce anger.",
      "M": "Like a lion he has left his den, for their land has become a desolation because of the oppressor's sword and because of his fierce anger.",
      "T": "He has left his lair like a lion — because their land has been turned to ruin by the oppressor's sword and by the blazing force of his wrath."
    }
  },
  "26": {
    "1": {
      "L": "In the beginning of the reign of Jehoiakim son of Josiah, king of Judah, this word came from the LORD:",
      "M": "At the beginning of the reign of Jehoiakim son of Josiah, king of Judah, this word came from the LORD:",
      "T": "At the very start of Jehoiakim son of Josiah's reign as king of Judah, this word came from Yahweh:"
    },
    "2": {
      "L": "Thus says the LORD: Stand in the court of the LORD's house and speak to all the cities of Judah that come to worship in the LORD's house all the words that I command you to speak to them; do not hold back a word.",
      "M": "This is what the LORD says: Stand in the court of the LORD's temple and speak to all the people from the cities of Judah who come there to worship. Speak everything I command you; do not hold back a single word.",
      "T": "Yahweh says: Stand in the court of the temple. Speak to all the people who come from Judah's towns to worship. Say everything I command — every word, nothing withheld."
    },
    "3": {
      "L": "Perhaps they will listen, and each man will turn from his evil way, so that I may relent of the disaster that I intend to do to them because of their evil deeds.",
      "M": "Perhaps they will listen, and each one will turn from his evil way. Then I can relent from the disaster I am planning to bring on them because of their evil deeds.",
      "T": "Perhaps they will listen. Perhaps they will turn from their evil ways, and I can turn from the judgment I have planned against them because of what they have done."
    },
    "4": {
      "L": "You shall say to them: Thus says the LORD: If you will not listen to me, to walk in my law that I have set before you,",
      "M": "Say to them: This is what the LORD says — If you will not listen to me, if you will not walk in my law that I have placed before you,",
      "T": "Say to them: Yahweh says — If you will not listen to me, if you will not walk by the Torah I have set before you,"
    },
    "5": {
      "L": "by listening to the words of my servants the prophets whom I send to you urgently — though you have not listened —",
      "M": "and if you will not listen to the words of my servants the prophets whom I keep sending to you urgently — though you have not listened —",
      "T": "and if you will not hear my servants the prophets, whom I keep sending persistently — you who have never listened —"
    },
    "6": {
      "L": "then I will make this house like Shiloh, and I will make this city a curse for all the nations of the earth.",
      "M": "then I will make this house like Shiloh, and I will make this city a curse for all the nations on earth.",
      "T": "then I will make this house what Shiloh became — and I will make this city a curse word in the mouth of every nation on earth."
    },
    "7": {
      "L": "The priests and the prophets and all the people heard Jeremiah speaking these words in the LORD's house.",
      "M": "The priests, the prophets, and all the people heard Jeremiah speaking these words in the LORD's temple.",
      "T": "The priests, the prophets, and all the people heard Jeremiah deliver that message in the temple."
    },
    "8": {
      "L": "And when Jeremiah had finished speaking all that the LORD had commanded him to speak to all the people, then the priests and the prophets and all the people seized him, saying: You shall surely die!",
      "M": "As soon as Jeremiah had finished saying everything the LORD had commanded him to say, the priests, the prophets, and all the people seized him and said: You must die!",
      "T": "The moment Jeremiah finished the full message Yahweh had commanded him to deliver, the priests and the prophets and all the people grabbed him. You are going to die! they said."
    },
    "9": {
      "L": "Why have you prophesied in the name of the LORD, saying: This house shall be like Shiloh, and this city shall be desolate, without inhabitant? And all the people gathered around Jeremiah in the LORD's house.",
      "M": "Why have you prophesied in the name of the LORD, saying that this temple will become like Shiloh, and this city will be left empty with no inhabitant? All the people crowded around Jeremiah in the LORD's temple.",
      "T": "How dare you prophesy in Yahweh's name and say this house will become like Shiloh, that this city will lie empty with no one in it! All the people closed in around Jeremiah in the temple court."
    },
    "10": {
      "L": "When the princes of Judah heard these things, they came up from the king's house to the LORD's house and sat down at the entrance of the New Gate of the LORD's house.",
      "M": "When the officials of Judah heard what was happening, they came up from the palace to the LORD's temple and took their seats at the entrance of the New Gate.",
      "T": "When the officials of Judah heard what was going on, they came up from the royal palace to the temple and sat down at the New Gate — the place of public judgment."
    },
    "11": {
      "L": "Then the priests and the prophets said to the princes and to all the people: This man deserves the sentence of death, for he has prophesied against this city, as you have heard with your own ears.",
      "M": "The priests and the prophets said to the officials and all the people: This man deserves to die — he has prophesied against this city, as you heard with your own ears.",
      "T": "The priests and the prophets pressed their case to the officials and all the people: This man deserves death. You heard it yourselves — he prophesied against this city."
    },
    "12": {
      "L": "Then Jeremiah spoke to all the princes and all the people, saying: The LORD sent me to prophesy against this house and against this city all the words you have heard.",
      "M": "Then Jeremiah spoke to all the officials and all the people: The LORD sent me to prophesy against this house and this city all the words you have heard.",
      "T": "Jeremiah answered the officials and all the people: Yahweh sent me. He sent me to prophesy against this house and against this city — every word you heard."
    },
    "13": {
      "L": "Now therefore mend your ways and your deeds and obey the voice of the LORD your God, and the LORD will relent of the disaster that he has pronounced against you.",
      "M": "So now, reform your ways and your deeds, obey the voice of the LORD your God, and the LORD will relent of the disaster he has pronounced against you.",
      "T": "Now then — change your ways and change your deeds, and listen to the voice of Yahweh your God. If you do, Yahweh will turn from the disaster he has decreed against you."
    },
    "14": {
      "L": "But as for me, behold, I am in your hands. Do with me as seems good and right to you.",
      "M": "As for me, I am in your hands. Do with me whatever you consider good and right.",
      "T": "As for me — I am in your hands. Do whatever you think is right."
    },
    "15": {
      "L": "Only know for certain that if you put me to death, you will bring innocent blood upon yourselves and upon this city and its inhabitants, for in truth the LORD sent me to you to speak all these words in your ears.",
      "M": "But know this for certain: if you put me to death, you will bring the guilt of innocent blood upon yourselves, upon this city, and upon its people — for in truth the LORD did send me to speak all these words to you.",
      "T": "But know this for certain: if you kill me, you are loading innocent blood onto yourselves, onto this city, onto everyone in it. Yahweh truly sent me to speak every one of these words to you."
    },
    "16": {
      "L": "Then the princes and all the people said to the priests and the prophets: This man does not deserve the sentence of death, for he has spoken to us in the name of the LORD our God.",
      "M": "Then the officials and all the people said to the priests and prophets: This man does not deserve death — he has spoken to us in the name of the LORD our God.",
      "T": "Then the officials and all the people rendered their verdict to the priests and prophets: This man is not guilty of a capital offense. He spoke to us in the name of Yahweh our God."
    },
    "17": {
      "L": "And certain of the elders of the land arose and spoke to all the assembly of the people, saying:",
      "M": "Some of the elders of the land stood up and addressed the whole assembly:",
      "T": "Then some of the elders of the land rose to address the full assembly:"
    },
    "18": {
      "L": "Micah of Moresheth prophesied in the days of Hezekiah king of Judah and said to all the people of Judah: Thus says the LORD of hosts: Zion shall be plowed as a field; Jerusalem shall become a heap of ruins, and the mountain of the house a wooded height.",
      "M": "Micah of Moresheth prophesied in the days of Hezekiah king of Judah and said to all the people of Judah: This is what the LORD of hosts says — Zion will be plowed like a field, Jerusalem will become a heap of rubble, and the temple mount will be overgrown with brush.",
      "T": "Micah of Moresheth prophesied during Hezekiah's reign. He said to all the people of Judah: Yahweh of hosts says — Zion will be plowed under like a field. Jerusalem will be a heap of stones. The temple mount will be a thicket."
    },
    "19": {
      "L": "Did Hezekiah king of Judah and all Judah put him to death? Did he not fear the LORD and entreat the favor of the LORD, and did not the LORD relent of the disaster that he had pronounced against them? But we — we would be bringing great evil on ourselves.",
      "M": "Did Hezekiah king of Judah and all of Judah put him to death? No — Hezekiah feared the LORD and sought his favor, and the LORD relented from the disaster he had pronounced against them. If we kill this man, we will be bringing great disaster on ourselves.",
      "T": "Did Hezekiah and all Judah execute Micah for saying that? No. Hezekiah feared Yahweh and pleaded with him, and Yahweh relented from the disaster he had announced. If we kill this man, we bring tremendous evil down on ourselves."
    },
    "20": {
      "L": "And there was also another man who prophesied in the name of the LORD, Urijah son of Shemaiah from Kiriath-jearim. He prophesied against this city and against this land in words similar to all those of Jeremiah.",
      "M": "There was also another man who prophesied in the name of the LORD — Urijah son of Shemaiah from Kiriath-jearim. He prophesied against this city and this land in words that matched Jeremiah's.",
      "T": "But there was another man who prophesied in Yahweh's name — Urijah son of Shemaiah from Kiriath-jearim. He preached the same message against this city and this land."
    },
    "21": {
      "L": "And when King Jehoiakim and all his warriors and all the officials heard his words, the king sought to put him to death. But when Urijah heard of it, he was afraid and fled and escaped to Egypt.",
      "M": "When King Jehoiakim, with all his soldiers and officials, heard his words, the king tried to have him executed. Urijah heard about it, was afraid, and fled to Egypt.",
      "T": "When King Jehoiakim heard him — along with all his officers and warriors — the king wanted him dead. Urijah found out and fled in fear to Egypt."
    },
    "22": {
      "L": "Then King Jehoiakim sent to Egypt certain men — Elnathan son of Achbor and others with him —",
      "M": "But King Jehoiakim sent men to Egypt — Elnathan son of Achbor and others with him —",
      "T": "But Jehoiakim sent a team to Egypt — Elnathan son of Achbor and others with him."
    },
    "23": {
      "L": "and they took Urijah from Egypt and brought him to King Jehoiakim, who struck him down with the sword and threw his dead body into the burial place of the common people.",
      "M": "They brought Urijah back from Egypt to King Jehoiakim, who had him executed. His body was thrown into the common burial ground.",
      "T": "They brought Urijah back from Egypt. Jehoiakim had him put to the sword. His body was thrown into the graves of the common people — not a royal burial, not even a named grave."
    },
    "24": {
      "L": "But the hand of Ahikam son of Shaphan was with Jeremiah, so that he was not given into the hand of the people to be put to death.",
      "M": "But Ahikam son of Shaphan used his influence to protect Jeremiah, so that he was not handed over to the people to be executed.",
      "T": "Ahikam son of Shaphan stood with Jeremiah, and his protection kept Jeremiah out of the hands of those who wanted him dead."
    }
  },
  "27": {
    "1": {
      "L": "In the beginning of the reign of Jehoiakim son of Josiah, king of Judah, this word came to Jeremiah from the LORD:",
      "M": "In the beginning of the reign of Zedekiah son of Josiah, king of Judah, this word came to Jeremiah from the LORD: [Note: the Hebrew text has 'Jehoiakim' — a scribal error; the rest of the chapter addresses Zedekiah.]",
      "T": "At the start of Zedekiah son of Josiah's reign as king of Judah, this word came to Jeremiah from Yahweh. (The Hebrew text reads 'Jehoiakim' — almost certainly a scribal slip; the chapter plainly addresses Zedekiah throughout.)"
    },
    "2": {
      "L": "Thus says the LORD to me: Make yourself yoke-bars and straps, and put them on your neck.",
      "M": "This is what the LORD said to me: Make a yoke with its crossbars and straps, and put it on your neck.",
      "T": "Yahweh told me: Make a yoke — crossbars and straps — and put it on your neck."
    },
    "3": {
      "L": "Send word to the king of Edom, the king of Moab, the king of the sons of Ammon, the king of Tyre, and the king of Sidon, by the hand of the envoys who have come to Jerusalem to Zedekiah king of Judah.",
      "M": "Send word to the king of Edom, the king of Moab, the king of the Ammonites, the king of Tyre, and the king of Sidon, through the envoys who have come to Jerusalem to visit Zedekiah king of Judah.",
      "T": "Use the envoys who have come to Jerusalem to meet with Zedekiah — send word to the king of Edom, the king of Moab, the king of the Ammonites, the king of Tyre, and the king of Sidon."
    },
    "4": {
      "L": "Give them this charge for their masters: Thus says the LORD of hosts, the God of Israel — say to your masters:",
      "M": "Give them this message for their masters: This is what the LORD of hosts, the God of Israel, says. Say to your masters:",
      "T": "This is what to deliver to their kings: Yahweh of hosts, God of Israel, says this. Tell your masters:"
    },
    "5": {
      "L": "It is I who by my great power and my outstretched arm have made the earth, with the men and animals that are on it, and I give it to whoever seems right to me.",
      "M": "I made the earth — with the people and animals on it — by my great power and my outstretched arm, and I give it to whoever I see fit.",
      "T": "I made the earth. I made every person and animal on it — by my great power, with my outstretched arm. And I give it to whoever I choose. The arm that delivered Israel from Egypt now gives the world to Babylon."
    },
    "6": {
      "L": "Now I have given all these lands into the hand of Nebuchadrezzar king of Babylon, my servant, and I have given him also the beasts of the field to serve him.",
      "M": "Now I am giving all these lands into the hands of Nebuchadnezzar king of Babylon, my servant, and I am giving him even the wild animals to serve him.",
      "T": "And right now, I am giving all these lands into the hand of Nebuchadnezzar king of Babylon — my servant. I am even putting the wild animals under his authority."
    },
    "7": {
      "L": "All the nations shall serve him and his son and his grandson, until the time of his own land comes; then many nations and great kings shall make him their servant.",
      "M": "All the nations will serve him, and his son, and his grandson, until the time of his own land comes; then many nations and great kings will make him their subject.",
      "T": "All nations will serve him — him, his son, his grandson — until the moment of reckoning comes for his own land. Then many nations and great kings will put Babylon under the yoke."
    },
    "8": {
      "L": "But if any nation or kingdom will not serve this Nebuchadrezzar king of Babylon and will not put its neck under the yoke of the king of Babylon, that nation I will punish with the sword, with famine, and with pestilence, declares the LORD, until I have consumed it by his hand.",
      "M": "But if any nation or kingdom will not serve Nebuchadnezzar king of Babylon or submit to his yoke, I will punish that nation with the sword, famine, and plague, declares the LORD, until I have destroyed it by his hand.",
      "T": "But any nation that refuses to serve Nebuchadnezzar, that will not put its neck under Babylon's yoke — I will punish it with sword, famine, and plague, says Yahweh, until I have consumed it by his hand."
    },
    "9": {
      "L": "So do not listen to your prophets, your diviners, your dreamers, your fortune-tellers, or your sorcerers, who are saying to you: You shall not serve the king of Babylon.",
      "M": "So do not listen to your prophets, your diviners, your dreamers, your fortune-tellers, or your sorcerers, who tell you: You will not have to serve the king of Babylon.",
      "T": "Do not listen to your prophets, your diviners, your dreamers, your soothsayers, your sorcerers — the ones telling you that you will not have to serve the king of Babylon."
    },
    "10": {
      "L": "For it is a lie that they are prophesying to you, with the result that you will be removed far from your land, and I will drive you out, and you will perish.",
      "M": "They are prophesying a lie to you, and the result will be that you will be driven far from your land — I will drive you out, and you will perish.",
      "T": "They are feeding you lies. The outcome will be that you are torn from your land — I will drive you out, and you will be destroyed."
    },
    "11": {
      "L": "But the nation that brings its neck under the yoke of the king of Babylon and serves him — I will let remain on its own land, to till it and dwell there, declares the LORD.",
      "M": "But the nation that submits to the yoke of the king of Babylon and serves him — I will let it remain in its own land to farm it and live there, declares the LORD.",
      "T": "But the nation that puts its neck under Babylon's yoke and serves — that nation I will leave in its own land to farm and inhabit. Yahweh's word."
    },
    "12": {
      "L": "To Zedekiah king of Judah I spoke in accordance with all these words, saying: Bring your necks under the yoke of the king of Babylon, and serve him and his people, and live.",
      "M": "I spoke all the same words to Zedekiah king of Judah: Submit to the king of Babylon's yoke, serve him and his people, and live.",
      "T": "I spoke the same message directly to Zedekiah king of Judah: Put your neck under Babylon's yoke. Serve him and his people. Live."
    },
    "13": {
      "L": "Why should you and your people die by the sword, by famine, and by pestilence, as the LORD has spoken against any nation that will not serve the king of Babylon?",
      "M": "Why should you and your people die by sword, famine, and plague, as the LORD has spoken against every nation that refuses to serve the king of Babylon?",
      "T": "Why die by sword, famine, and plague — the exact fate Yahweh has announced for every nation that refuses to submit to Babylon?"
    },
    "14": {
      "L": "Do not listen to the words of the prophets who are saying to you: You shall not serve the king of Babylon — for they are prophesying a lie to you.",
      "M": "Do not listen to the prophets who tell you: You will not have to serve the king of Babylon — they are prophesying a lie to you.",
      "T": "Do not listen to the prophets who say you will not serve Babylon. They are lying to you."
    },
    "15": {
      "L": "For I have not sent them, declares the LORD, and they are prophesying falsely in my name, with the result that I will drive you out and you will perish — you and the prophets who are prophesying to you.",
      "M": "I have not sent them, declares the LORD. They are prophesying falsely in my name, and the outcome will be that I drive you out and you perish — you and the prophets who are prophesying to you.",
      "T": "I did not send them, says Yahweh. They prophesy falsely in my name. The outcome will be that I drive you out and you are destroyed — you and the very prophets you are listening to."
    },
    "16": {
      "L": "Then I spoke to the priests and to all this people, saying: Thus says the LORD: Do not listen to the words of your prophets who prophesy to you, saying, Behold, the vessels of the LORD's house will be brought back from Babylon very soon — for they are prophesying a lie to you.",
      "M": "I also said to the priests and all the people: This is what the LORD says — Do not listen to your prophets who keep telling you the vessels of the LORD's temple will soon be brought back from Babylon. That is a lie.",
      "T": "Then I addressed the priests and all the people: Yahweh says — Do not listen to your prophets who keep saying the temple vessels will be brought back from Babylon any day now. It is a lie."
    },
    "17": {
      "L": "Do not listen to them; serve the king of Babylon and live. Why should this city become a desolation?",
      "M": "Do not listen to them. Serve the king of Babylon and live. Why let this city be made into a wasteland?",
      "T": "Do not listen to them. Serve Babylon and live. Why would you let this city be turned into a ruin?"
    },
    "18": {
      "L": "But if they are prophets and if the word of the LORD is with them, let them now intercede with the LORD of hosts that the vessels remaining in the LORD's house and in the house of the king of Judah and in Jerusalem should not go to Babylon.",
      "M": "But if they truly are prophets and if the word of the LORD is really with them, let them pray and intercede with the LORD of hosts that the vessels still in the LORD's temple and in the royal palace and in Jerusalem are not taken to Babylon.",
      "T": "If they are truly prophets, if Yahweh's word is actually with them — let them intercede. Let them pray to Yahweh of hosts that the vessels still in the temple, in the palace, in Jerusalem not be taken to Babylon. That would be worth praying about."
    },
    "19": {
      "L": "For thus says the LORD of hosts concerning the pillars, the sea, the stands, and the rest of the vessels that remain in this city,",
      "M": "For this is what the LORD of hosts says about the bronze pillars, the large bronze basin, the movable stands, and all the other vessels remaining in this city —",
      "T": "Yahweh of hosts has spoken about the great bronze pillars, the bronze sea, the movable stands, and all the remaining vessels still in this city —"
    },
    "20": {
      "L": "which Nebuchadrezzar king of Babylon did not take when he carried into exile Jeconiah son of Jehoiakim, king of Judah, from Jerusalem to Babylon, with all the nobles of Judah and Jerusalem —",
      "M": "which Nebuchadnezzar king of Babylon did not take when he deported Jeconiah son of Jehoiakim, king of Judah, from Jerusalem to Babylon, along with all the leading men of Judah and Jerusalem —",
      "T": "the vessels Nebuchadnezzar did not take when he exiled Jeconiah son of Jehoiakim to Babylon, along with all the nobility of Judah and Jerusalem —"
    },
    "21": {
      "L": "thus says the LORD of hosts, the God of Israel, concerning the vessels that remain in the LORD's house and in the house of the king of Judah and in Jerusalem:",
      "M": "this is what the LORD of hosts, the God of Israel, says about those vessels still in the LORD's temple, in the royal palace, and in Jerusalem:",
      "T": "Yahweh of hosts, God of Israel, says this about those remaining vessels in the temple and the palace and throughout Jerusalem:"
    },
    "22": {
      "L": "They shall be carried to Babylon and remain there until the day when I visit them, declares the LORD, and then I will bring them back and restore them to this place.",
      "M": "They will be taken to Babylon and remain there until the day when I attend to them, declares the LORD. Then I will bring them back and restore them to this place.",
      "T": "They will be carried to Babylon. They will stay there until the day I come for them, says Yahweh. Then I will bring them back and restore them to this place."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'jeremiah')
        merge_tier(existing, JEREMIAH, tier_key)
        save(tier_dir, 'jeremiah', existing)
    print('Jeremiah 25–27 written.')

if __name__ == '__main__':
    main()
