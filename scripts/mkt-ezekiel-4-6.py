"""
MKT Ezekiel chapters 4–6 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-ezekiel-4-6.py

Translation decisions:

- H3068 (יהוה): "LORD" in L/M throughout. "Yahweh" in T for covenant-identity declarations
  (the repeated "I am the LORD / Yahweh" formula — וְיָדְעוּ כִּי אֲנִי יְהוָה — in 6:7,
  6:10, 6:13, 6:14) and divine speech introductions in 6:1. This is the defining Ezekiel
  refrain; the T tier uses "Yahweh" to preserve the personal-name force that "LORD" obscures.

- H3069 (יְהוִה with Adonai vowels) + H136 (אֲדֹנָי): Rendered "the Lord GOD" in L/M
  (following the convention of showing Adonai-Yahweh as Lord GOD in small caps), and
  "the Lord Yahweh" in T. This combined form appears frequently in Ezekiel's oracles.

- H120 + H1121 (בֶּן־אָדָם / ben-adam): "son of man" throughout all tiers. Ezekiel's
  distinctive address; T may occasionally expand to "Son of man" with slight elaboration
  in surrounding clause but never changes the address itself.

- H5771 (עָוֹן / ʿāwôn): "iniquity" in L/M; "guilt" in T. The term carries both the act
  and its ongoing consequence-weight — Ezekiel must physically "bear" it (ch 4). T renders
  it "guilt" to foreground the weight-of-consequence dimension.

- H1544 (גִּלּוּל / gillul): "idols" throughout. Ezekiel's distinctive, contemptuous term
  for idols (literally "dung-pellets" or "rolling things"). The contempt is preserved in
  T where context allows without being anachronistic.

- H7307 (רוּחַ): In 5:2 and 5:10 it is clearly "wind" (directional scatter) — not Spirit.
  Used "wind" consistently in chs 4–6, where the context is always the four winds of
  dispersal, never the divine Spirit.

- H5315 (נֶפֶשׁ) at 4:14: Ezekiel says "my soul has not been polluted." In context this is
  his entire embodied self — not a Greek immaterial soul. L: "my soul"; M: "I have never
  defiled myself"; T: "every fibre of my being." Avoids importing Greek anthropology.

- H2617 (חֶסֶד): Does not appear in chs 4–6. The tone is entirely judgment, not covenant
  loyalty; hesed is absent from these sign-act and oracle chapters.

- Sign-act genre: Chs 4–5 are prophetic sign-acts (מוֹפֵת / mōpet). The T tier explicitly
  frames the enacted drama as enacted prophecy where helpful, without becoming commentary.

- "Staff of bread" (H4294 + H3899): A Hebrew idiom for the food supply ("break the staff
  of bread" = cut off the food entirely). L preserves the idiom; M unpacks it slightly
  ("food supply"); T renders the meaning directly.

- 390 days / 40 days (4:5–6): The numbers correspond to years of iniquity. The "day for
  a year" principle (cf. Num 14:34) is explicit in v6. All tiers preserve the numeric
  precision without smoothing it.

- Famine cannibalism (5:10): "Fathers shall eat sons... sons shall eat fathers" — the
  ultimate horror of siege starvation. Referenced in Deut 28:53–57; Lam 4:10. All tiers
  preserve the shocking directness; T does not soften.

- "I am broken" at 6:9: H7665 (שָׁבַר) applied to God — "I am broken [over their
  whorish heart]." This is remarkable divine pathos language. L preserves it literally;
  M: "I was grieved"; T: "I was broken-hearted." The pathos is intentional and should
  not be flattened.

- Diblah (6:14): Some MSS read "Diblah" (דִּבְלָה), others "Riblah" (רִבְלָה). Riblah
  was a known Syrian city at the northern border (2 Kgs 23:33); Diblah may be a
  scribal error. The sense is the same: a northern wilderness marker. All tiers use
  "Diblah" following the MT as read, noting the variant is a single letter shift.

- "Pleasing aroma / sweet savour" (6:13): נִיחֹחַ (nîhōah) — the same term used for
  legitimate sacrifice (Gen 8:21; Exod 29:18). Used here ironically: incense to idols
  rising where corpses will now lie. The irony is preserved in T.

- Acrostic / poetry note: Chs 4–6 are prophetic prose, not poetry. No special line-break
  formatting in the T tier (unlike Lamentations). T pursues rhythmic cadence and concrete
  imagery rather than formal versification.
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

EZEKIEL = {
  "4": {
    "1": {
      "L": "And you, son of man, take for yourself a clay tile and lay it before you; and portray upon it the city, even Jerusalem.",
      "M": "Now you, son of man, take a clay tile and place it before you, then inscribe on it the city — Jerusalem.",
      "T": "Son of man, here is what you must do: Take a clay tile and set it in front of you. Draw Jerusalem on it — the city about to be besieged."
    },
    "2": {
      "L": "And lay a siege against it, and build a siege wall against it, and cast a ramp against it, and set camps against it, and place battering rams against it all around.",
      "M": "Lay siege to it: build a siege wall against it, throw up a ramp, set up encampments, and place battering rams all around it.",
      "T": "Then enact the siege: raise a siege wall, pile up a ramp, ring it with encampments, set battering rams at every approach."
    },
    "3": {
      "L": "Then take for yourself an iron pan and set it as an iron wall between you and the city; set your face toward it, and let it be under siege, and you shall press the siege against it. This shall be a sign to the house of Israel.",
      "M": "Then take an iron griddle and stand it upright as an iron wall between yourself and the city; turn your face toward it so that it is under siege, and press the siege against it. This will be a sign to the house of Israel.",
      "T": "Take an iron griddle and stand it upright as a wall between you and Jerusalem. Face toward it and press the siege. This enacted drama is a sign to Israel of what is coming."
    },
    "4": {
      "L": "Then lie upon your left side and lay the iniquity of the house of Israel upon it; according to the number of the days that you shall lie upon it, you shall bear their iniquity.",
      "M": "Then lie on your left side and take up the iniquity of the house of Israel upon yourself; the number of days you lie there corresponds to the years of their iniquity you are bearing.",
      "T": "Next, lie down on your left side. Take the guilt of Israel's house onto your own body — each day you lie there stands for one year of guilt they have accumulated."
    },
    "5": {
      "L": "For I have laid upon you the years of their iniquity, according to the number of the days — three hundred and ninety days — and so you shall bear the iniquity of the house of Israel.",
      "M": "I have assigned you the years of their iniquity as a number of days: three hundred and ninety days, so you shall bear the guilt of the house of Israel.",
      "T": "The count is three hundred and ninety days — one for each year of Israel's guilt. I have placed that weight on you, and you will carry it."
    },
    "6": {
      "L": "And when you have accomplished these days, you shall lie again on your right side and bear the iniquity of the house of Judah forty days; a day for each year I have appointed for you.",
      "M": "When those days are finished, roll onto your right side and bear the iniquity of the house of Judah: forty days, a day for each year — I have appointed it so.",
      "T": "When those three hundred ninety days are done, roll over onto your right side. Now you bear Judah's guilt — forty more days, still one day per year. I have fixed the count."
    },
    "7": {
      "L": "And toward the siege of Jerusalem you shall set your face, with your arm bared, and you shall prophesy against her.",
      "M": "Turn your face toward the besieged Jerusalem with your arm bared, and prophesy against her.",
      "T": "Turn your gaze on Jerusalem, arm bared as if for combat, and declare what is coming against her."
    },
    "8": {
      "L": "And behold, I will lay bands upon you so that you shall not turn from one side to the other until you have ended the days of your siege.",
      "M": "I will put cords on you so that you cannot turn from side to side until the days of your siege are complete.",
      "T": "I will bind you so that you cannot shift position — you will lie there, fixed, until the full count of siege-days is done."
    },
    "9": {
      "L": "Take also for yourself wheat and barley and beans and lentils and millet and emmer, and put them in a single vessel and make bread of them; for the number of the days that you lie upon your side — three hundred and ninety days — you shall eat it.",
      "M": "Also take wheat, barley, beans, lentils, millet, and emmer wheat; put them all in one vessel and bake bread from them. That is what you shall eat for the three hundred and ninety days you lie on your side.",
      "T": "Make your bread from whatever can be gathered — wheat, barley, beans, lentils, millet, spelt — all mixed together in one jar. That is your food for the entire three hundred and ninety days."
    },
    "10": {
      "L": "And the food you eat shall be by weight, twenty shekels a day; from time to time you shall eat it.",
      "M": "Your food shall be rationed: twenty shekels' worth by weight each day, eaten at set intervals.",
      "T": "Ration it strictly: twenty shekels' weight per day, eaten at fixed hours. Nothing more than that."
    },
    "11": {
      "L": "And water you shall drink by measure, the sixth part of a hin; from time to time you shall drink.",
      "M": "And drink water measured out: one sixth of a hin, drunk at set times.",
      "T": "Your water is rationed too — a sixth of a hin per day, drunk on a strict schedule."
    },
    "12": {
      "L": "And you shall eat it as a barley cake, and you shall bake it over human dung in their sight.",
      "M": "You shall eat it as a barley cake, baking it over human excrement in the sight of the people.",
      "T": "Bake that bread as barley cakes over human dung — right there in full view of the people."
    },
    "13": {
      "L": "And the LORD said: Even so shall the children of Israel eat their unclean bread among the nations where I will drive them.",
      "M": "The LORD said: 'This is how the Israelites will eat their defiled bread among the nations to which I drive them.'",
      "T": "Yahweh said: This is Israel's future — eating unclean food in the countries where I scatter them. Every meal will carry the mark of exile and defilement."
    },
    "14": {
      "L": "Then I said: Ah, Lord GOD! Behold, my soul has not been polluted; for from my youth until now I have not eaten what dies of itself or is torn in pieces, and no abominable flesh has entered my mouth.",
      "M": "Then I said: 'Ah, Lord GOD! I have never defiled myself — from my youth until now I have not eaten anything that died on its own or was mauled by animals, and no unclean meat has ever entered my mouth.'",
      "T": "I cried out: 'Lord Yahweh, no — not this. Every fibre of my being recoils at it. From childhood to this moment I have never eaten carrion or torn flesh. Nothing forbidden has ever passed my lips.'"
    },
    "15": {
      "L": "Then he said to me: See, I will give you cow's dung in place of human dung, and you shall prepare your bread over it.",
      "M": "He said to me: 'Very well — I will allow you to use cattle dung instead of human dung; prepare your bread over that.'",
      "T": "Then he relented: 'All right. Use cattle dung instead of human waste. Bake your bread over that.'"
    },
    "16": {
      "L": "Moreover he said to me: Son of man, behold, I will break the staff of bread in Jerusalem; and they shall eat bread by weight and with anxiety, and they shall drink water by measure and with dismay.",
      "M": "Then he said to me: 'Son of man, I am about to break the food supply in Jerusalem; they will eat their rationed bread with dread and drink their measured water with despair.'",
      "T": "Then he said to me: Son of man — I am cutting off Jerusalem's food supply. They will gnaw at rationed bread in a panic and gulp their measured water in despair."
    },
    "17": {
      "L": "That they may lack bread and water, and be appalled at one another, and waste away under their iniquity.",
      "M": "They will lack bread and water, look at each other in horror, and waste away because of their iniquity.",
      "T": "They will run out of both bread and water. They will stare at each other in hollow-eyed horror — and wither away under the weight of their guilt."
    }
  },
  "5": {
    "1": {
      "L": "And you, son of man, take for yourself a sharp sword; take it as a barber's razor and cause it to pass over your head and your beard; then take for yourself balances to weigh and divide the hair.",
      "M": "And you, son of man, take a sharp sword and use it as a barber's razor — run it over your head and your beard; then use a scale to divide the hair into equal portions.",
      "T": "Son of man, take a sharp blade and use it like a barber's razor — shave your head and beard completely. Then weigh the hair and divide it into three exact portions."
    },
    "2": {
      "L": "A third part you shall burn with fire in the midst of the city when the days of the siege are fulfilled; and a third part you shall take and strike around it with a sword; and a third part you shall scatter to the wind, and I will draw out a sword after them.",
      "M": "When the days of the siege are completed, burn a third in the middle of the city; take another third and cut it with a sword around the city; scatter the final third to the wind — and I will draw a sword in pursuit of them.",
      "T": "When the siege days end, burn a third of the hair inside the city. Take a third and cut it to pieces just outside the walls. Scatter the last third to the winds — and I will chase those scattered ones with the sword."
    },
    "3": {
      "L": "You shall also take a small number of them and bind them in the edges of your robe.",
      "M": "Take a small number of the hairs and tuck them into the folds of your cloak.",
      "T": "But take a few strands and hide them safe inside your robe — a small remnant, kept close."
    },
    "4": {
      "L": "Then take some of these and cast them into the midst of the fire and burn them in the fire; from there a fire shall go out into all the house of Israel.",
      "M": "Then take some of those very hairs and throw them into the fire to burn; from that fire a flame will spread to all the house of Israel.",
      "T": "Then take some even of those and throw them into the fire. The remnant itself is not safe — the fire will spread from it to consume all of Israel."
    },
    "5": {
      "L": "Thus says the Lord GOD: This is Jerusalem; I have set her in the midst of the nations, with countries all around her.",
      "M": "This is what the Lord GOD says: This is Jerusalem — I placed her in the center of the nations, with countries surrounding her on all sides.",
      "T": "The Lord Yahweh declares: This is what Jerusalem was — the city I set at the center of the nations, positioned to be a light at the hub of the world."
    },
    "6": {
      "L": "But she has changed my judgments into wickedness more than the nations, and my statutes more than the countries around her; for they have rejected my judgments and have not walked in my statutes.",
      "M": "But she has turned against my laws more than the nations, and defied my statutes more than the surrounding countries; for they have rejected my ordinances and refused to walk in my statutes.",
      "T": "But she has been more rebellious than all of them put together. She turned my judgments into occasions for wickedness and discarded my statutes — she refused both, and the nations around her did better by their own standards."
    },
    "7": {
      "L": "Therefore thus says the Lord GOD: Because you have surpassed the nations around you and have not walked in my statutes, nor kept my judgments, nor even done according to the judgments of the nations around you —",
      "M": "Therefore this is what the Lord GOD says: Because you have exceeded the nations around you in rebellion — you have not followed my statutes, kept my ordinances, or even lived up to the standards of the nations surrounding you —",
      "T": "Therefore the Lord Yahweh declares: You have outdone every nation around you in unfaithfulness. You did not live by my statutes. You did not keep my judgments. You did not even do as well as the pagan nations that surround you."
    },
    "8": {
      "L": "Therefore thus says the Lord GOD: Behold, I, even I, am against you, and I will execute judgments in your midst in the sight of the nations.",
      "M": "Therefore this is what the Lord GOD says: I — yes, I myself — am against you, and I will carry out my judgments against you in the full sight of the nations.",
      "T": "So the Lord Yahweh says: I am against you. Yes — I myself, the God who placed you at the center of everything. I will execute my judgments against you in the open, before all the watching nations."
    },
    "9": {
      "L": "And I will do in you what I have not done, and will not do again the like of, because of all your abominations.",
      "M": "I will do to you what I have never done before, and what I will never do again, on account of all your abominations.",
      "T": "What I am about to do to you I have never done before — and I will never do it again. Your abominations have brought you to an entirely unprecedented judgment."
    },
    "10": {
      "L": "Therefore fathers shall eat sons in your midst, and sons shall eat their fathers; and I will execute judgments in you and scatter the whole remnant of you to all the winds.",
      "M": "Therefore fathers will eat their sons within you, and sons will eat their fathers; I will execute judgments among you and scatter all your survivors to every wind.",
      "T": "It will come to this: fathers eating their sons, sons eating their fathers — siege starvation pushed past every human limit. And when it is over I will scatter whoever remains to every wind."
    },
    "11": {
      "L": "Surely, as I live, declares the Lord GOD: Because you have defiled my sanctuary with all your detestable things and with all your abominations, I will also withdraw; my eye shall not spare, and I will have no pity.",
      "M": "As I live — the declaration of the Lord GOD — because you defiled my sanctuary with all your vile practices and abominations, I will cut you down; my eye will not spare and I will show no pity.",
      "T": "By my own life, declares the Lord Yahweh: You filled my sanctuary with every filth you could devise — detestable things, abominations without end. So I will reduce you. I will not look away in mercy. I will not spare."
    },
    "12": {
      "L": "A third part of you shall die by pestilence and be consumed by famine in your midst; a third part shall fall by the sword all around you; and a third part I will scatter to every wind, and I will draw out a sword after them.",
      "M": "A third of you will die by plague and be consumed by famine within the city; a third will fall by the sword around you; and a third I will scatter to every wind — drawing a sword in pursuit of them.",
      "T": "One third will die inside the city — by plague, by starvation. One third will be cut down by the sword just outside the walls. The last third I will scatter to every wind — and I will chase the scattered ones with the sword as they flee."
    },
    "13": {
      "L": "Thus shall my anger spend itself, and I will satisfy my fury upon them and take comfort; and they shall know that I, the LORD, have spoken in my zeal, when I have spent my fury upon them.",
      "M": "Then my anger will be exhausted, my fury will rest upon them and find its end; and they will know that I, the LORD, have spoken in my jealous anger, when I have spent my fury on them.",
      "T": "When it is done, my anger will be spent. My fury will settle and find its resting place. I will be satisfied. And they will know — finally — that I, Yahweh, spoke what I meant, and that my zeal was utterly real."
    },
    "14": {
      "L": "Moreover I will make you a waste and a reproach among the nations that are around you, in the sight of all who pass by.",
      "M": "Furthermore, I will make you a ruin and a disgrace among the surrounding nations, in the sight of all who pass by.",
      "T": "Jerusalem will be left a wreck. Every nation around her will see the ruins and shudder. Everyone passing through will see what became of the city set at the center of the world."
    },
    "15": {
      "L": "So you shall be a reproach and a taunt, a warning and an astonishment, to the nations around you, when I execute judgments against you in anger and in fury and in furious rebukes. I, the LORD, have spoken.",
      "M": "You will be a disgrace and a mockery, a warning and a horror, to the surrounding nations when I carry out my judgments against you in anger, in fury, and with blazing rebukes. I, the LORD, have spoken.",
      "T": "Jerusalem will become what nations point to in horror — a byword, a lesson in catastrophe that is told for generations. And when I carry out this fury, it will be Yahweh himself who has done it."
    },
    "16": {
      "L": "When I send against you the evil arrows of famine that bring destruction, which I will send to destroy you, I will also heap more famine upon you and break the staff of bread among you.",
      "M": "When I launch against you the deadly arrows of famine aimed at destruction, I will intensify the famine upon you and cut off your food supply.",
      "T": "I will fire the arrows of famine at you — arrows designed to kill — and I will multiply them until your food supply is gone. There will be nothing left to keep you alive."
    },
    "17": {
      "L": "So I will send upon you famine and evil beasts, and they shall bereave you; and pestilence and blood shall pass through you; and I will bring the sword upon you. I, the LORD, have spoken.",
      "M": "I will unleash famine, ferocious beasts to bereave you, pestilence, bloodshed, and the sword upon you. I, the LORD, have spoken.",
      "T": "Famine, wild animals, plague, bloodshed, the sword — I will send all of them against you. I, Yahweh, have spoken it."
    }
  },
  "6": {
    "1": {
      "L": "And the word of the LORD came to me, saying:",
      "M": "The word of the LORD came to me:",
      "T": "Yahweh's word came to me again:"
    },
    "2": {
      "L": "Son of man, set your face toward the mountains of Israel and prophesy against them,",
      "M": "Son of man, turn your face toward the mountains of Israel and prophesy against them.",
      "T": "Son of man, face the mountains of Israel and speak against them."
    },
    "3": {
      "L": "And say: You mountains of Israel, hear the word of the Lord GOD! Thus says the Lord GOD to the mountains and to the hills, to the ravines and to the valleys: Behold, I, even I, am bringing a sword upon you, and I will destroy your high places.",
      "M": "Say: 'Mountains of Israel, hear the word of the Lord GOD. This is what the Lord GOD says to the mountains and hills, to the ravines and valleys: I am bringing a sword against you, and I will destroy your high places.'",
      "T": "Speak this: Mountains of Israel, hear the word of the Lord Yahweh. Here is what the Lord Yahweh says to the mountains, the hills, the ravines, and the valleys: I am bringing a sword against you, and I will pull down every high place — every shrine built on every height."
    },
    "4": {
      "L": "Your altars shall be desolate and your incense stands shall be shattered; and I will cast your slain before your idols.",
      "M": "Your altars will be laid waste, your incense altars shattered, and your slain will be hurled down before your idols.",
      "T": "Your altars will be rubble. Your incense stands will be smashed. And your corpses will lie at the feet of the very idols you worshipped."
    },
    "5": {
      "L": "And I will lay the dead bodies of the children of Israel before their idols, and I will scatter your bones around your altars.",
      "M": "I will place the corpses of the Israelites before their idols and scatter your bones around your altars.",
      "T": "The bodies of Israel's people will be strewn at the feet of the idols they served. Their bones will be scattered around the altars where they burned offerings."
    },
    "6": {
      "L": "In all your dwelling places the cities shall be laid waste, and the high places shall be made desolate, so that your altars may be ruined and desolate, your idols broken and ended, your incense stands cut down, and your works blotted out.",
      "M": "In all your settlements the cities will be laid waste and the high places made desolate, so that your altars are ruined, your idols smashed and finished, your incense stands cut down, and everything you made wiped out.",
      "T": "Every city, every settlement — laid waste. Every high place — emptied. Every altar — in ruins. Every idol — shattered. Every incense stand — chopped down. Every work of your hands — erased."
    },
    "7": {
      "L": "And the slain shall fall in your midst, and you shall know that I am the LORD.",
      "M": "The slain will fall among you, and you will know that I am the LORD.",
      "T": "The dead will pile up in your midst. And when it is over, you will know that I am Yahweh."
    },
    "8": {
      "L": "Yet I will leave a remnant — some who will escape the sword among the nations when you are scattered through the lands.",
      "M": "Yet I will spare a remnant — those who escape the sword when you are scattered among the nations and lands.",
      "T": "Even so, I will preserve a remnant — survivors of the sword, scattered to the nations."
    },
    "9": {
      "L": "And those of you who escape shall remember me among the nations where they are carried captive — how I was broken over their whorish heart that departed from me and over their eyes that go whoring after their idols; and they shall loathe themselves for the evils they committed in all their abominations.",
      "M": "Those who survive among the nations where they are taken captive will remember me — how I was grieved by their adulterous heart that turned away from me, and by their eyes that strayed after their idols; they will loathe themselves for all the evil they committed in all their abominations.",
      "T": "The survivors will carry the memory of me into every land where they are taken. They will remember what they left behind — a God who loved them and was broken-hearted, while their hearts chased idols like faithless lovers. They will be ashamed. That shame is part of how restoration begins."
    },
    "10": {
      "L": "And they shall know that I am the LORD; I have not said in vain that I would do this evil to them.",
      "M": "They will know that I am the LORD; I did not speak idly when I threatened to bring this disaster — I said it and I did it.",
      "T": "They will know that I am Yahweh. I did not speak empty words. Every warning I gave was real."
    },
    "11": {
      "L": "Thus says the Lord GOD: Strike with your hand and stamp with your foot, and say, Alas! for all the evil abominations of the house of Israel, who shall fall by the sword, by famine, and by pestilence.",
      "M": "This is what the Lord GOD says: Clap your hands, stamp your foot, and cry out, 'Alas!' over all the wicked abominations of the house of Israel — for they will fall by sword, famine, and plague.",
      "T": "The Lord Yahweh says: Slap your hands together, stomp your feet, and cry out — Alas! — over every evil thing Israel has done. They are going to die: by the sword, by famine, by plague."
    },
    "12": {
      "L": "The one who is far off shall die by pestilence, and the one who is near shall fall by the sword, and the one who remains and is besieged shall die by famine; so I will spend my fury upon them.",
      "M": "Those far away will die by plague; those nearby will fall by the sword; those remaining under siege will die by famine. So I will exhaust my fury upon them.",
      "T": "Those far from the city will be cut down by plague. Those close by will fall to the sword. Those trapped inside will starve to death. Every path leads to judgment — I will exhaust my fury on them completely."
    },
    "13": {
      "L": "Then you shall know that I am the LORD, when their slain lie among their idols around their altars, on every high hill, on all the mountaintops, under every green tree, and under every leafy oak — wherever they offered pleasing aroma to all their idols.",
      "M": "Then you will know that I am the LORD, when the slain lie among the idols around the altars — on every high hill, on every mountaintop, under every green tree, under every spreading oak — everywhere they offered fragrant sacrifices to their idols.",
      "T": "You will know I am Yahweh when the dead lie at the feet of the idols they loved — on every hilltop, on every mountain peak, under every sacred green tree, under every spreading oak — every place where incense once rose sweetly will be a place of corpses."
    },
    "14": {
      "L": "And I will stretch out my hand against them and make the land more desolate and waste than the wilderness toward Diblah, throughout all their dwelling places; and they shall know that I am the LORD.",
      "M": "I will stretch out my hand against them and make the land utterly desolate — more barren than the wilderness toward Diblah — throughout all their settlements; then they will know that I am the LORD.",
      "T": "I will reach out my hand and leave this land emptier than any desert — more barren than the wasteland that stretches toward Diblah — across every place where my people once lived. And they will know: I am Yahweh."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'ezekiel')
        merge_tier(existing, EZEKIEL, tier_key)
        save(tier_dir, 'ezekiel', existing)
    print('Ezekiel 4–6 written.')

if __name__ == '__main__':
    main()
