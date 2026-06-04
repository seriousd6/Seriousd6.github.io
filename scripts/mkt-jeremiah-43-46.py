"""
MKT Jeremiah chapters 43–46 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-jeremiah-43-46.py

Translation decisions (consistent with mkt-jeremiah-1-3.py through mkt-jeremiah-33-36.py):

- H3068 (יהוה): "LORD" in L/M throughout; "Yahweh" in T where the personal-name
  force matters — oracle delivery, confrontation, divine oath. Formula "declares the LORD"
  → "Yahweh declares it" or "Yahweh's word" in T.

- H430 (אֱלֹהִים): "God" in all three tiers.

- H6635 (צְבָאוֹת): "of hosts" in L/M/T. Retained as established convention.

- Queen of Heaven (מֶלֶכֶת הַשָּׁמַיִם): ch. 44 — probably Ishtar/Astarte, attested in
  Mesopotamian and Canaanite cults. L/M: "the queen of heaven" (lowercase, following the
  convention that designations for foreign deities are not capitalized); T: "the queen of
  heaven" (same — but T notes will clarify the cult identity where useful). The irony of
  ch. 44:25 — Yahweh saying "confirm your vows" — is preserved in all three tiers.

- H7998 (שָׁלָל, šālāl, "spoil/plunder"): 45:5 — the idiom נֶפֶשׁ לְשָׁלָל = "your life
  as spoil/booty," meaning surviving with one's bare life as the only reward when everything
  else is lost. L: "your life as spoil"; M: "your life as a prize"; T: "you will escape with
  your life and nothing more." A consolation, not a reward.

- "Amon of No" (ch. 46:25): No = Thebes (Egyptian Nō-Amun = "abode of Amon"); Amon was the
  chief deity of Thebes, and by this period effectively the supreme state god of Egypt.
  L: "Amon of No"; M: "Amon of No" (retained — enough context from surrounding geography);
  T: "Amon, the god of Thebes" (surface the meaning for the reader).

- Nebuchadnezzar / Nebuchadrezzar: Jeremiah consistently uses the more historically accurate
  Aramaic-influenced form "Nebuchadrezzar" (נְבוּכַדְרֶאצַּר) rather than the more familiar
  "Nebuchadnezzar." All three tiers follow the Hebrew form "Nebuchadrezzar" — as in prior
  Jeremiah scripts.

- "My servant Nebuchadrezzar" (43:10): the same honorific applied to the foreign king in
  Jer 25:9; 27:6. Yahweh uses foreign powers as instruments of judgment. L/M: "my servant";
  T: "my instrument" (brings out the agency without flattening the surprising use of "servant").

- "Take your positions and be ready" vs. "Stand fast and prepare" (46:14): L preserves the
  military register; M/T render into natural English commands.

- "Full end" (כָּלָה, kālāh, 46:28): the "full end / utter destruction" formula appears also
  at Jer 4:27; 5:18; 30:11. Yahweh will make a full end of the nations but not of Jacob —
  discipline, not annihilation. L/M: "a full end"; T: "destroy you utterly."

Structural and textual notes:

- Ch. 43: The remnant's flight to Egypt despite Yahweh's explicit command to stay (cf. 42:1-22)
  demonstrates the pattern of the whole book: hearing and disobeying. The accusation against
  Baruch (v.3) recurs at 45:1-5 — the same Baruch receives a private oracle as consolation.
  The sign-act of the stones (vv.9-13) enacts prophetically what the oracle declares: Babylon
  will reach even Egypt.

- Ch. 44: The Queen of Heaven polemic reaches its sharpest point: the people respond to
  Jeremiah with explicit counter-theology — the Queen gave them prosperity, the abandonment
  of her cult brought disaster (vv.15-18). This is not ignorance but deliberate syncretism.
  Yahweh's ironic v.25 ("confirm your vows then") is a decree of abandonment, not permission.
  v.30 — Pharaoh Hophra (Apries) was indeed assassinated by Ahmose II in 570 BC, ~20 years
  after this prophecy was given.

- Ch. 45: A hinge chapter — set in the fourth year of Jehoiakim (605 BC, the same year the
  scroll was dictated), though placed here editorially. Baruch's grief echoes Jeremiah's own
  laments. Yahweh's response reframes the prophet's private anguish within cosmic demolition:
  what Baruch mourns is what Yahweh himself is doing. Seek survival, not advancement.

- Ch. 46: Oracle against Egypt falls into two parts: (A) Battle of Carchemish (605 BC,
  vv.1-12) — Neco's army routed by Nebuchadrezzar; (B) prophecy of Nebuchadrezzar's invasion
  of Egypt (vv.13-26). Both use dense poetic and martial imagery. The closing promise to Jacob
  (vv.27-28) echoes 30:10-11 verbatim — the same reassurance planted in the midst of oracles
  of judgment against the nations.

OT intertextuality:
- 43:10 — "my servant Nebuchadrezzar": Jer 25:9; 27:6 (same epithet).
- 44:25 — "confirm your vows": ironic echo of Num 30:2 (vow obligations). The permission
  is doom, not approval.
- 45:4 — "what I have built I will break down; what I have planted I will pluck up":
  echoes Jer 1:10 (Jeremiah's commissioning vocabulary) — the final outworking of the
  prophet's mandate.
- 46:10 — "a day of vengeance... a sacrifice": picks up Isa 34:6 (Edom oracle) imagery of
  sacrifice as divine judgment.
- 46:27-28 — exact parallel of Jer 30:10-11.
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


JEREMIAH = {
  "43": {
    "1": {
      "L": "And it came to pass, when Jeremiah had finished speaking to all the people all the words of the LORD their God — all these words that the LORD their God had sent him to speak to them —",
      "M": "When Jeremiah finished speaking to all the people all the words of the LORD their God — every word that the LORD their God had sent him to give them —",
      "T": "When Jeremiah had finished delivering to the people every word Yahweh their God had sent him to speak —"
    },
    "2": {
      "L": "then Azariah the son of Hoshaiah and Johanan the son of Kareah and all the arrogant men said to Jeremiah: You are speaking falsely! The LORD our God has not sent you to say, 'Do not go to Egypt to dwell there.'",
      "M": "Azariah son of Hoshaiah and Johanan son of Kareah and all the insolent men said to Jeremiah: You are speaking falsely! The LORD our God has not sent you to say, 'Do not go to Egypt to live there.'",
      "T": "Azariah son of Hoshaiah and Johanan son of Kareah and all the arrogant men said to Jeremiah: You are lying! Yahweh our God did not send you to say, 'Do not go to Egypt to live there.'"
    },
    "3": {
      "L": "But Baruch the son of Neriah is setting you against us, in order to hand us over into the hand of the Chaldeans, that they might put us to death or carry us away captive to Babylon.",
      "M": "But Baruch son of Neriah is inciting you against us, to deliver us into the hand of the Chaldeans, to put us to death or carry us into exile in Babylon.",
      "T": "It is Baruch son of Neriah who is setting you against us — trying to hand us over to the Chaldeans, who will kill us or drag us off to Babylon."
    },
    "4": {
      "L": "So Johanan the son of Kareah and all the commanders of the forces and all the people did not obey the voice of the LORD, to remain in the land of Judah.",
      "M": "So Johanan son of Kareah and all the commanders of the forces and all the people disobeyed the voice of the LORD, refusing to stay in the land of Judah.",
      "T": "So Johanan son of Kareah and all the military commanders and all the people refused to obey Yahweh's voice and stay in the land of Judah."
    },
    "5": {
      "L": "But Johanan the son of Kareah and all the commanders of the forces took all the remnant of Judah who had returned from all the nations where they had been driven to dwell in the land of Judah —",
      "M": "Instead, Johanan son of Kareah and all the commanders of the forces took the entire remnant of Judah who had returned from all the nations where they had been scattered — who had come back to dwell in the land of Judah —",
      "T": "Instead, Johanan son of Kareah and all the military commanders gathered every last survivor of Judah who had come back from all the nations where they had been scattered — those who had returned to live in Judah —"
    },
    "6": {
      "L": "the men, the women, the children, the king's daughters, and every person whom Nebuzaradan the captain of the guard had left with Gedaliah the son of Ahikam, the son of Shaphan — and Jeremiah the prophet and Baruch the son of Neriah —",
      "M": "men, women, and children, the royal daughters, and everyone whom Nebuzaradan the captain of the guard had placed under Gedaliah son of Ahikam son of Shaphan — including Jeremiah the prophet and Baruch son of Neriah —",
      "T": "men, women, and children, the king's daughters, everyone Nebuzaradan the commander of the guard had assigned to Gedaliah son of Ahikam son of Shaphan — Jeremiah the prophet and Baruch son of Neriah among them —"
    },
    "7": {
      "L": "and they came into the land of Egypt, for they did not obey the voice of the LORD; and they came as far as Tahpanhes.",
      "M": "They entered the land of Egypt, because they would not obey the voice of the LORD. They came as far as Tahpanhes.",
      "T": "They went to Egypt — straight into disobedience to Yahweh's word — and came all the way to Tahpanhes."
    },
    "8": {
      "L": "Then the word of the LORD came to Jeremiah in Tahpanhes, saying:",
      "M": "Then the word of the LORD came to Jeremiah in Tahpanhes:",
      "T": "In Tahpanhes, Yahweh's word came to Jeremiah:"
    },
    "9": {
      "L": "Take some large stones in your hands and hide them in the mortar in the pavement that is at the entrance to Pharaoh's palace in Tahpanhes, in the sight of the men of Judah.",
      "M": "Take some large stones in your hands and bury them in the mortar in the brick pavement at the entrance to Pharaoh's palace in Tahpanhes, in the sight of the men of Judah.",
      "T": "Take some large stones and bury them in the mortar of the brick terrace at the entrance to Pharaoh's palace here in Tahpanhes — do it where the men of Judah can see you."
    },
    "10": {
      "L": "And say to them: Thus says the LORD of hosts, the God of Israel: Behold, I will send and take Nebuchadrezzar the king of Babylon, my servant, and I will set his throne above these stones that I have hidden, and he will spread his royal canopy over them.",
      "M": "Then say to them: Thus says the LORD of hosts, the God of Israel: I am going to send for Nebuchadrezzar king of Babylon, my servant, and set his throne over these very stones I have buried here. He will pitch his royal canopy above them.",
      "T": "Then tell them: Yahweh of hosts, the God of Israel, says this: I am summoning Nebuchadrezzar king of Babylon — my instrument — and placing his throne directly over these stones I have buried here. He will spread his royal pavilion above them."
    },
    "11": {
      "L": "When he comes, he will strike the land of Egypt: whoever is destined for death, to death; whoever is destined for captivity, to captivity; whoever is destined for the sword, to the sword.",
      "M": "When he comes, he will strike the land of Egypt: those destined for death, he will bring to death; those destined for captivity, to captivity; those destined for the sword, to the sword.",
      "T": "When he comes, he will strike Egypt down. For those appointed to death — death. For those appointed to captivity — captivity. For those appointed to the sword — the sword."
    },
    "12": {
      "L": "And I will kindle a fire in the temples of the gods of Egypt, and he will burn them and carry them captive; and he will wrap himself in the land of Egypt as a shepherd wraps himself in his cloak, and he will go out from there in peace.",
      "M": "I will set fire to the temples of the gods of Egypt, and he will burn them and take them captive. He will pick clean the land of Egypt as a shepherd picks his cloak clean of lice, and he will depart from there in safety.",
      "T": "I will set fire to the temples of Egypt's gods. He will burn them and carry the images off as plunder. He will strip Egypt clean the way a shepherd strips his garment clean, and he will leave without opposition."
    },
    "13": {
      "L": "He will break the sacred pillars of Beth-shemesh, which is in the land of Egypt, and the temples of the gods of Egypt he will burn with fire.",
      "M": "He will demolish the sacred pillars of Beth-shemesh in the land of Egypt, and the temples of the gods of Egypt he will burn with fire.",
      "T": "He will smash the sacred obelisks of Heliopolis and burn to the ground every temple of Egypt's gods."
    }
  },
  "44": {
    "1": {
      "L": "The word that came to Jeremiah concerning all the Jews who lived in the land of Egypt, who dwelt at Migdol, at Tahpanhes, at Noph, and in the land of Pathros:",
      "M": "The word that came to Jeremiah concerning all the Jews who were living in the land of Egypt — at Migdol, at Tahpanhes, at Noph, and in the region of Pathros:",
      "T": "This is the word Yahweh gave to Jeremiah regarding all the Jews settled throughout Egypt — at Migdol, at Tahpanhes, at Memphis, and throughout the region of Pathros:"
    },
    "2": {
      "L": "Thus says the LORD of hosts, the God of Israel: You have seen all the disaster that I brought on Jerusalem and on all the cities of Judah; behold, this day they are a desolation, and no one dwells in them,",
      "M": "Thus says the LORD of hosts, the God of Israel: You have seen all the disaster I brought on Jerusalem and all the cities of Judah. Behold, they are a desolation this day, and no one lives there —",
      "T": "Yahweh of hosts, the God of Israel, says this: You have seen every disaster I brought down on Jerusalem and every town of Judah. Today they lie in ruins, without a single inhabitant —"
    },
    "3": {
      "L": "because of the evil that they committed to provoke me to anger, in that they went to make offerings and serve other gods that they did not know — neither they nor you nor your fathers.",
      "M": "because of the wickedness they committed, provoking me to anger by going to burn offerings to other gods — gods that neither they nor you nor your ancestors ever knew.",
      "T": "all because of the evil they chose: they provoked my fury by going after foreign gods and burning offerings to them — gods their ancestors never knew, gods you never knew."
    },
    "4": {
      "L": "Yet I sent to you all my servants the prophets, persistently rising and sending them, saying: Oh, do not do this abominable thing that I hate!",
      "M": "Yet I sent you all my servants the prophets, again and again, urgently saying: Do not do this detestable thing that I hate!",
      "T": "And yet I sent you my servants the prophets — sent them early and sent them often — crying: Do not do this abomination! I hate it!"
    },
    "5": {
      "L": "But they did not listen or incline their ear to turn from their wickedness and make no offerings to other gods.",
      "M": "But they did not listen or pay attention, to turn from their wickedness and stop making offerings to other gods.",
      "T": "But they would not listen. They would not even turn their heads. They kept on in their wickedness, kept on burning offerings to foreign gods."
    },
    "6": {
      "L": "Therefore my wrath and my anger were poured out and were kindled in the cities of Judah and in the streets of Jerusalem, and they became a waste and a desolation, as at this day.",
      "M": "Therefore my wrath and my anger were poured out and ignited in the cities of Judah and the streets of Jerusalem; and they became the waste and desolation you see today.",
      "T": "So my fury and my anger poured out and burned through every city of Judah and every street of Jerusalem — and they became the desolation that stands before you today."
    },
    "7": {
      "L": "And now thus says the LORD, the God of hosts, the God of Israel: Why are you committing this great evil against yourselves, to cut off from you man and woman, infant and child, from the midst of Judah, leaving yourselves no remnant?",
      "M": "And now thus says the LORD, the God of hosts, the God of Israel: Why are you doing this great harm to yourselves, cutting off from Judah man and woman, infant and child, leaving no remnant?",
      "T": "So now — Yahweh, the God of hosts, the God of Israel, says this: Why are you doing this terrible thing to yourselves? Why are you cutting off from Judah every man and woman, every infant and child, leaving no survivor?"
    },
    "8": {
      "L": "provoking me to anger with the works of your hands by burning offerings to other gods in the land of Egypt, where you have come to dwell, that you might cut yourselves off and become a curse and a reproach among all the nations of the earth?",
      "M": "You provoke me to anger with your own handiwork by burning offerings to other gods in the land of Egypt where you have gone to live — so that you would cut yourselves off and become a curse and a reproach among all the nations of the earth.",
      "T": "You are provoking me with your own hands by burning offerings to foreign gods here in Egypt — guaranteeing that you will be wiped out, a byword and a disgrace among every nation on earth."
    },
    "9": {
      "L": "Have you forgotten the wickedness of your fathers, the wickedness of the kings of Judah, the wickedness of their wives, your own wickedness, and the wickedness of your wives, which they committed in the land of Judah and in the streets of Jerusalem?",
      "M": "Have you forgotten the wickedness of your ancestors, the wickedness of the kings of Judah and their wives, your own wickedness and the wickedness of your wives — all that was done in the land of Judah and in the streets of Jerusalem?",
      "T": "Have you already forgotten the evil your ancestors committed, the evil of Judah's kings and their wives, and your own evil and the evil of your wives — everything that happened in Judah's cities and Jerusalem's streets?"
    },
    "10": {
      "L": "They have not been humbled to this day, nor have they feared, nor walked in my law and in my statutes that I set before you and before your fathers.",
      "M": "They have not been humbled even to this day. They have not feared, nor walked in my law and my statutes that I placed before you and your ancestors.",
      "T": "Even now, not one of them has been humbled. Not one has feared me. Not one has walked in my law and my statutes that I laid out clearly before you and your ancestors."
    },
    "11": {
      "L": "Therefore thus says the LORD of hosts, the God of Israel: Behold, I am setting my face against you for harm, to cut off all Judah.",
      "M": "Therefore thus says the LORD of hosts, the God of Israel: I am going to set my face against you for disaster, to cut off all Judah.",
      "T": "Therefore Yahweh of hosts, the God of Israel, says this: I am turning my face against you — for ruin, not rescue — to cut Judah off completely."
    },
    "12": {
      "L": "And I will take the remnant of Judah who have set their faces to come to the land of Egypt to dwell there, and they shall all be consumed; in the land of Egypt they shall fall; by the sword and by famine they shall be consumed, from the least to the greatest; they shall become an object of execration and horror, a curse and a reproach.",
      "M": "I will take the remnant of Judah who resolved to go to Egypt to live there, and they shall all be consumed. In the land of Egypt they shall fall — by sword and by famine they shall be consumed, from the least to the greatest. They shall become an object of execration, horror, cursing, and reproach.",
      "T": "I will take the whole remnant of Judah — those who set their faces toward Egypt and came here to settle — and they will be destroyed. In Egypt they will fall. By sword and famine they will be devoured, from the smallest to the greatest. They will become a source of cursing and horror, a byword of contempt."
    },
    "13": {
      "L": "For I will punish those who dwell in the land of Egypt, as I punished Jerusalem, with the sword, with famine, and with pestilence.",
      "M": "For I will punish those living in the land of Egypt just as I punished Jerusalem — with sword, famine, and plague.",
      "T": "I will visit Egypt's settlers with the same judgment I brought on Jerusalem — sword, famine, and plague."
    },
    "14": {
      "L": "So none of the remnant of Judah who have come into the land of Egypt to dwell there shall escape or survive to return to the land of Judah, to which they long to return to dwell there; for none shall return except some fugitives.",
      "M": "None of the remnant of Judah who have come to Egypt to live there will escape or survive to return to the land of Judah, which they long to go back to — none will return except a handful of fugitives.",
      "T": "No one from Judah's remnant who came to Egypt to settle will escape or survive to go home to Judah — though they long for it. No one will return. Only a few refugees will slip through."
    },
    "15": {
      "L": "Then all the men who knew that their wives had been making offerings to other gods, and all the women who stood there, a great assembly, and all the people who lived in Pathros in the land of Egypt, answered Jeremiah:",
      "M": "Then all the men who knew their wives had been making offerings to other gods, and all the women standing there — a large assembly — and all the people of Pathros in the land of Egypt, answered Jeremiah:",
      "T": "Then all the men who knew their wives had been burning offerings to foreign gods, and all the women who stood there — a vast crowd — and all the people of Pathros in Egypt, answered Jeremiah:"
    },
    "16": {
      "L": "As for the word that you have spoken to us in the name of the LORD, we will not listen to you.",
      "M": "As for the word you have spoken to us in the name of the LORD, we will not listen to you.",
      "T": "The word you have spoken to us in Yahweh's name — we will not obey it."
    },
    "17": {
      "L": "But we will surely do everything that we have vowed, making offerings to the queen of heaven and pouring out drink offerings to her, as we did — both we and our fathers, our kings and our officials — in the cities of Judah and in the streets of Jerusalem. For then we had plenty of food and prospered and saw no disaster.",
      "M": "We will do everything we have vowed — making offerings to the queen of heaven and pouring out drink offerings to her, just as we and our fathers and our kings and our officials did in the cities of Judah and the streets of Jerusalem. For in those days we had plenty of food and were well off, and saw no disaster.",
      "T": "We will do everything we vowed: burn offerings to the queen of heaven and pour out drink offerings to her, exactly as we and our fathers and our kings and our officials did in every city of Judah and in every street of Jerusalem. In those days we had food in abundance, we prospered, and no disaster touched us."
    },
    "18": {
      "L": "But since we left off making offerings to the queen of heaven and pouring out drink offerings to her, we have lacked everything and have been consumed by the sword and by famine.",
      "M": "But ever since we stopped making offerings to the queen of heaven and pouring out drink offerings to her, we have had nothing and have been consumed by sword and famine.",
      "T": "But the moment we stopped burning offerings to the queen of heaven and pouring out drink offerings to her, we lost everything. The sword and famine have been devouring us ever since."
    },
    "19": {
      "L": "And the women said: When we burned offerings to the queen of heaven and poured out drink offerings to her, was it without our husbands' approval that we made cakes for her in her image and poured out drink offerings to her?",
      "M": "The women added: When we burned offerings to the queen of heaven and poured out drink offerings to her, was it without our husbands' knowledge that we made cakes bearing her image and poured out drink offerings to her?",
      "T": "The women added: When we burned offerings to the queen of heaven and poured out drink offerings to her, did we shape the cakes in her image and pour out those offerings without our husbands knowing? Did we act on our own?"
    },
    "20": {
      "L": "Then Jeremiah said to all the people, to the men and the women, and to all the people who had given him that answer:",
      "M": "Jeremiah then said to all the people — the men, the women, and all who had given him this answer:",
      "T": "Jeremiah replied to all the people — men and women alike, everyone who had answered him:"
    },
    "21": {
      "L": "As for the offerings that you made in the cities of Judah and in the streets of Jerusalem — you and your fathers, your kings and your officials, and the people of the land — did the LORD not remember them? Did it not come into his mind?",
      "M": "The offerings you made in the cities of Judah and the streets of Jerusalem — you and your ancestors, your kings and your officials, the people of the land — did the LORD not remember them? Did he not keep them in mind?",
      "T": "The offerings you burned in Judah's cities and Jerusalem's streets — you and your ancestors, your kings and officials and the common people — do you think Yahweh forgot them? Do you think he did not notice?"
    },
    "22": {
      "L": "The LORD could no longer bear your evil deeds and the abominations that you committed; therefore your land has become a desolation and an astonishment and a curse, without inhabitant, as it is this day.",
      "M": "The LORD could no longer endure your evil deeds and the abominations you committed; therefore your land has become a desolation and a horror and a curse, without inhabitant, as it is today.",
      "T": "Yahweh could endure your evil deeds and your abominations no longer — and that is exactly why your land has become the desolation and the horror and the curse it is today, empty of all inhabitants."
    },
    "23": {
      "L": "It is because you burned offerings and because you sinned against the LORD and did not obey the voice of the LORD and did not walk in his law and in his statutes and in his testimonies that this disaster has come upon you, as it is this day.",
      "M": "Because you burned offerings and sinned against the LORD, and did not obey the voice of the LORD or walk in his law and his statutes and his testimonies, therefore this disaster has come upon you, as it is today.",
      "T": "Because you burned those offerings and sinned against Yahweh — because you refused to obey his voice, to walk in his law, his statutes, and his testimonies — this disaster has fallen on you. Everything you see today is the result."
    },
    "24": {
      "L": "Moreover Jeremiah said to all the people and to all the women: Hear the word of the LORD, all you of Judah who are in the land of Egypt.",
      "M": "Jeremiah said to all the people and to all the women: Hear the word of the LORD, all you of Judah who are in the land of Egypt.",
      "T": "Jeremiah continued — addressing all the people, and the women in particular: Hear Yahweh's word, all of you from Judah who are living here in Egypt."
    },
    "25": {
      "L": "Thus says the LORD of hosts, the God of Israel: You and your wives have declared with your mouths and fulfilled with your hands, saying: We will surely perform our vows that we have vowed, to make offerings to the queen of heaven and to pour out drink offerings to her. Then confirm your vows! And surely perform your vows!",
      "M": "Thus says the LORD of hosts, the God of Israel: You and your wives have stated with your mouths and fulfilled with your hands, saying: We will certainly carry out our vows to make offerings to the queen of heaven and pour out drink offerings to her. Go ahead then — confirm your vows and perform them!",
      "T": "Yahweh of hosts, the God of Israel, says this: You and your wives have declared openly — declared it aloud and backed it with your hands — 'We will make good our vows to the queen of heaven; we will burn offerings and pour out drink offerings.' Very well. Confirm your vows. Carry them out."
    },
    "26": {
      "L": "Therefore hear the word of the LORD, all you of Judah who dwell in the land of Egypt: Behold, I have sworn by my great name, says the LORD, that my name shall no longer be invoked by the mouth of any man of Judah in all the land of Egypt, saying: As the Lord GOD lives.",
      "M": "Therefore hear the word of the LORD, all you of Judah who dwell in the land of Egypt: I have sworn by my great name, says the LORD, that my name will no longer be spoken by the mouth of any man of Judah in all the land of Egypt, saying, 'As the Lord GOD lives.'",
      "T": "Therefore hear Yahweh's word, all of Judah in Egypt: I have sworn by my own great name — Yahweh declares it — that no one from Judah anywhere in Egypt will ever again swear by my name, saying 'As the Lord GOD lives.'"
    },
    "27": {
      "L": "Behold, I am watching over them for harm and not for good, and all the men of Judah who are in the land of Egypt shall be consumed by the sword and by famine until there is an end of them.",
      "M": "I am watching over them for harm, not for good, and all the men of Judah who are in the land of Egypt shall be consumed by sword and famine until they are finished.",
      "T": "I am watching over them for ruin, not rescue. Every man of Judah here in Egypt will be consumed by sword and famine until the last of them is gone."
    },
    "28": {
      "L": "And those who escape the sword shall return from the land of Egypt to the land of Judah, few in number; and all the remnant of Judah who came to the land of Egypt to dwell there shall know whose word will stand — mine or theirs.",
      "M": "Those who escape the sword will return from Egypt to Judah — but only a few. Then all the remnant of Judah who came to Egypt to live will know whose word has stood — mine or theirs.",
      "T": "A handful who survive the sword will make their way back from Egypt to Judah. And the entire remnant of Judah who came to Egypt to settle will find out whose word stands — mine or theirs."
    },
    "29": {
      "L": "And this shall be a sign for you, declares the LORD, that I will punish you in this place, so that you may know that my words against you will surely stand:",
      "M": "This will be your sign, declares the LORD — that I will punish you in this place — so you may know that my words of judgment against you will certainly come to pass:",
      "T": "And here is the sign I will give you — Yahweh declares it — proof that I will carry out my judgment against you right here in Egypt. You will know that every word I have spoken against you will stand:"
    },
    "30": {
      "L": "Thus says the LORD: Behold, I am going to give Pharaoh Hophra king of Egypt into the hand of his enemies and into the hand of those who seek his life, just as I gave Zedekiah king of Judah into the hand of Nebuchadrezzar king of Babylon, who was his enemy and sought his life.",
      "M": "Thus says the LORD: I am going to hand over Pharaoh Hophra king of Egypt to his enemies and to those who seek his life, just as I handed Zedekiah king of Judah to Nebuchadrezzar king of Babylon, who was his enemy and sought his life.",
      "T": "Yahweh says this: I am handing Pharaoh Hophra king of Egypt over to his enemies — to every faction that wants him dead — just as I handed Zedekiah king of Judah to Nebuchadrezzar king of Babylon, who was his enemy and came for his life."
    }
  },
  "45": {
    "1": {
      "L": "The word that Jeremiah the prophet spoke to Baruch the son of Neriah, when he wrote these words in a scroll at the dictation of Jeremiah, in the fourth year of Jehoiakim the son of Josiah, king of Judah, saying:",
      "M": "The word that the prophet Jeremiah spoke to Baruch son of Neriah when he wrote these words in a scroll at Jeremiah's dictation, in the fourth year of Jehoiakim son of Josiah, king of Judah:",
      "T": "This is the word Jeremiah the prophet spoke to Baruch son of Neriah when Baruch was writing down these words from Jeremiah's dictation — in the fourth year of Jehoiakim son of Josiah, king of Judah:"
    },
    "2": {
      "L": "Thus says the LORD, the God of Israel, to you, O Baruch:",
      "M": "Thus says the LORD, the God of Israel, to you, Baruch:",
      "T": "Yahweh, the God of Israel, says this to you, Baruch:"
    },
    "3": {
      "L": "You said: Woe is me! For the LORD has added grief to my sorrow. I am weary with my groaning, and I find no rest.",
      "M": "You said: Woe is me! For the LORD has added sorrow to my pain. I am weary with my groaning, and I find no rest.",
      "T": "You have said, 'I am undone! Yahweh has piled grief on top of grief. I am worn out with groaning and can find no rest.'"
    },
    "4": {
      "L": "Say this to him: Thus says the LORD: Behold, what I have built I am tearing down, and what I have planted I am plucking up — and this across the whole land.",
      "M": "Say this to him: Thus says the LORD: What I have built I am tearing down, and what I have planted I am uprooting — this entire land.",
      "T": "Say this to him: Yahweh says — what I built, I am now demolishing; what I planted, I am now tearing up. The whole land. All of it."
    },
    "5": {
      "L": "And you, do you seek great things for yourself? Do not seek them. For behold, I am bringing disaster upon all flesh, declares the LORD; but I will give you your life as spoil in all the places where you may go.",
      "M": "And you — are you seeking great things for yourself? Stop seeking them. For I am going to bring disaster on all flesh, declares the LORD. But I will give you your life as a prize wherever you go.",
      "T": "As for you — are you looking for something great for yourself? Stop looking. I am bringing disaster on every living thing. Yahweh declares it. But this much I give you: you will escape with your life wherever you go."
    }
  },
  "46": {
    "1": {
      "L": "The word of the LORD that came to Jeremiah the prophet concerning the nations:",
      "M": "The word of the LORD that came to Jeremiah the prophet concerning the nations:",
      "T": "This is the word Yahweh gave to Jeremiah the prophet concerning the nations:"
    },
    "2": {
      "L": "Concerning Egypt — about the army of Pharaoh Neco, king of Egypt, which was at the river Euphrates at Carchemish, which Nebuchadrezzar king of Babylon defeated in the fourth year of Jehoiakim the son of Josiah, king of Judah:",
      "M": "Concerning Egypt: about the army of Pharaoh Neco, king of Egypt, which was at the river Euphrates at Carchemish — the army that Nebuchadrezzar king of Babylon defeated in the fourth year of Jehoiakim son of Josiah, king of Judah:",
      "T": "Concerning Egypt: concerning the army of Pharaoh Neco, king of Egypt, stationed at the Euphrates at Carchemish — the army Nebuchadrezzar king of Babylon crushed in the fourth year of Jehoiakim son of Josiah, king of Judah:"
    },
    "3": {
      "L": "Order the buckler and shield, and draw near for battle!",
      "M": "Prepare the small shield and the large shield, and advance for battle!",
      "T": "Get your shields ready — small and large — and advance to the line!"
    },
    "4": {
      "L": "Harness the horses, and mount, O horsemen! Take your positions with your helmets! Polish the spears, put on your armor!",
      "M": "Harness the horses; mount, O horsemen! Fall in with your helmets! Polish the spears; put on your coats of armor!",
      "T": "Saddle the horses! Cavalry, mount up! Helmets on — take your positions! Sharpen the spears! Put on your armor!"
    },
    "5": {
      "L": "Why do I see them dismayed and turning backward? Their mighty ones are beaten down and have fled in haste; they look not back — terror is on every side! declares the LORD.",
      "M": "Why do I see them dismayed and retreating? Their warriors are beaten down and have fled headlong, without looking back — terror on every side! declares the LORD.",
      "T": "But what is this I see? They are in panic, turning and running. Their best warriors are cut down and fleeing headlong — not one of them looks back. Terror on every side! Yahweh declares it."
    },
    "6": {
      "L": "The swift cannot flee away, nor can the mighty man escape; in the north by the river Euphrates they stumble and fall.",
      "M": "The swift cannot flee away, nor can the mighty man escape; to the north, by the river Euphrates, they stumble and fall.",
      "T": "The swift cannot outrun this. The strongest cannot escape. They stumble and fall at the Euphrates, there in the north."
    },
    "7": {
      "L": "Who is this, rising like the Nile, like rivers whose waters churn?",
      "M": "Who is this, rising like the Nile, like rivers whose waters surge?",
      "T": "Who is this rising like the flooding Nile, swelling like rivers in flood?"
    },
    "8": {
      "L": "Egypt rises like the Nile, like rivers whose waters churn. He said: I will rise, I will cover the earth; I will destroy cities and their inhabitants.",
      "M": "Egypt rises like the Nile, like rivers whose waters surge. It said: I will rise, I will cover the earth; I will destroy cities and their inhabitants.",
      "T": "Egypt — surging like the Nile, swelling like flood-swollen rivers. Egypt said: I will rise up and drown the earth; I will destroy cities and wipe out everyone who lives in them."
    },
    "9": {
      "L": "Advance, O horses, and rage, O chariots! Let the mighty warriors go out — men of Ethiopia and Put who handle the shield, men of Lud who draw and bend the bow!",
      "M": "Advance, horses! Rage, chariots! Let the mighty men go forward — the men of Ethiopia and Put who handle the shield, and the men of Lud who draw and bend the bow!",
      "T": "Forward, cavalry! Charge, chariots! Let the crack troops advance — Ethiopian and Libyan shield-bearers, Lydian archers bending their bows!"
    },
    "10": {
      "L": "For that day is for the Lord GOD of hosts, a day of vengeance, to avenge himself on his foes. The sword shall devour and be sated and drink its fill of their blood; for the Lord GOD of hosts holds a sacrifice in the north country, by the river Euphrates.",
      "M": "For that day belongs to the Lord GOD of hosts — a day of vengeance, by which he avenges himself on his foes. The sword will devour and be satisfied and drink its fill of their blood. For the Lord GOD of hosts is holding a sacrifice in the northern land, by the river Euphrates.",
      "T": "But that day belongs to the Lord Yahweh of hosts — the day he settles the score with his enemies. The sword will eat its fill and drink deep of their blood. The Lord Yahweh of hosts is staging a great slaughter by the Euphrates in the north."
    },
    "11": {
      "L": "Go up to Gilead and take balm, O virgin daughter of Egypt! You multiply medicines in vain; there is no healing for you.",
      "M": "Go up to Gilead and get balm, O virgin daughter of Egypt! You pile up medicine upon medicine in vain; there is no healing for you.",
      "T": "Go to Gilead and get your medicines, O virgin daughter of Egypt! Stack remedy upon remedy — none of it will help. There is no cure for your wound."
    },
    "12": {
      "L": "The nations have heard of your shame, and your cry has filled the earth; for warrior has stumbled against warrior; together they have both fallen.",
      "M": "The nations have heard your shame, and the earth is filled with your cry; for warrior stumbled over warrior, and together they both fell.",
      "T": "Your humiliation has echoed among the nations; your cry has filled the earth. Warrior fell over warrior, and both went down together."
    },
    "13": {
      "L": "The word that the LORD spoke to Jeremiah the prophet about how Nebuchadrezzar king of Babylon would come and strike the land of Egypt:",
      "M": "The word that the LORD spoke to Jeremiah the prophet about how Nebuchadrezzar king of Babylon would come and strike the land of Egypt:",
      "T": "This is the word Yahweh spoke to Jeremiah the prophet concerning Nebuchadrezzar king of Babylon's coming campaign against Egypt:"
    },
    "14": {
      "L": "Declare in Egypt, and proclaim in Migdol; proclaim in Noph and in Tahpanhes: Take your positions and be ready, for the sword shall devour around you!",
      "M": "Announce it in Egypt, proclaim it in Migdol; proclaim it in Noph and in Tahpanhes: Take your positions and be ready, for the sword shall devour all around you!",
      "T": "Broadcast it through Egypt! Shout it in Migdol, Memphis, and Tahpanhes: Stand to your post — be ready! The sword is already cutting its way around you!"
    },
    "15": {
      "L": "Why have your mighty ones been swept away? They did not stand, because the LORD thrust them down.",
      "M": "Why have your warriors been swept away? They could not stand, because the LORD thrust them down.",
      "T": "Why have your mighty men been swept off their feet? They could not hold their ground — because Yahweh drove them down."
    },
    "16": {
      "L": "He made many stumble; indeed, they fell over one another, and said: Rise up, and let us go back to our own people and to the land of our birth, from before the sword of the oppressor!",
      "M": "He made many stumble; they fell one upon another and said: Arise! Let us go back to our own people and to our native land, away from the oppressor's sword!",
      "T": "He sent them stumbling and collapsing over each other, and they cried out: Get up — let's go home! Back to our own people, our own land, away from that devouring sword!"
    },
    "17": {
      "L": "They cried there: Pharaoh king of Egypt is but a noise — he has let the appointed hour pass by!",
      "M": "They cried out there: Pharaoh king of Egypt is nothing but noise — he has let the appointed time slip by!",
      "T": "There they gave him his true name: Pharaoh king of Egypt is nothing but bluster — he missed his moment."
    },
    "18": {
      "L": "As I live, declares the King, whose name is the LORD of hosts, like Tabor among the mountains and like Carmel by the sea, one shall come.",
      "M": "As I live, declares the King — the LORD of hosts is his name — like Tabor towering over the mountains and like Carmel standing against the sea, he shall come.",
      "T": "As I live — the King declares, Yahweh of hosts is his name — as surely as Tabor rises above the hills and Carmel stands over the sea, he is coming."
    },
    "19": {
      "L": "Prepare for yourself baggage for exile, O inhabitants of Egypt! For Memphis shall become a waste, a ruin, uninhabited.",
      "M": "Pack your bags for exile, O inhabitants of Egypt! For Memphis will become a desolation, a ruin without inhabitant.",
      "T": "Pack your bags for exile, all you who live in Egypt! Memphis will become a wasteland — a ghost city, empty of everyone."
    },
    "20": {
      "L": "A beautiful heifer is Egypt, but a horsefly from the north has come upon her, it has come.",
      "M": "Egypt is a beautiful heifer, but a horsefly from the north has come against her, it has come.",
      "T": "Egypt is a beautiful heifer — but the stinging fly from the north has found her."
    },
    "21": {
      "L": "Even the hired soldiers in her midst are like fattened calves; for they also have turned and fled together; they did not stand, for the day of their calamity had come upon them, the time of their punishment.",
      "M": "Even her hired soldiers in her midst are like fattened calves — they too have turned and fled together. They did not stand, for the day of their disaster came upon them, the time of their reckoning.",
      "T": "Even her mercenaries, penned and pampered like fattened calves — they too have turned tail and fled together. They would not stand their ground, for the day of their disaster arrived, the time of their accounting."
    },
    "22": {
      "L": "Her voice shall hiss like a serpent as they march in force; they shall come against her with axes, like woodcutters.",
      "M": "Her sound shall be like a hissing serpent, as they advance in force and come against her with axes, like woodcutters.",
      "T": "Egypt will hiss like a fleeing serpent as the army advances in full strength against her, axes raised like woodcutters come to level a forest."
    },
    "23": {
      "L": "They shall cut down her forest, declares the LORD, though it is impenetrable; for they are more than locusts, they are without number.",
      "M": "They shall cut down her forest, declares the LORD, though it is dense, for they are more in number than locusts and are without number.",
      "T": "They will cut down her forest — Yahweh declares it — even though it seems impossible to penetrate. For they come in numbers past counting, more than a swarm of locusts."
    },
    "24": {
      "L": "The daughter of Egypt is put to shame; she is delivered into the hand of a people from the north.",
      "M": "The daughter of Egypt is put to shame; she is handed over to a people from the north.",
      "T": "Egypt is shamed and handed over — delivered into the grip of a people from the north."
    },
    "25": {
      "L": "The LORD of hosts, the God of Israel, said: Behold, I am going to punish Amon of No and Pharaoh and Egypt and her gods and her kings — even Pharaoh and those who trust in him.",
      "M": "The LORD of hosts, the God of Israel, said: I am going to punish Amon of No, and Pharaoh, and Egypt with her gods and her kings — Pharaoh and all who put their trust in him.",
      "T": "Yahweh of hosts, the God of Israel, says this: I am bringing judgment on Amon, the god of Thebes, on Pharaoh, on Egypt, on her gods and her kings — on Pharaoh and on every person who trusts in him."
    },
    "26": {
      "L": "I will deliver them into the hand of those who seek their lives, into the hand of Nebuchadrezzar king of Babylon and into the hand of his servants. Afterward Egypt shall be inhabited as in the days of old, declares the LORD.",
      "M": "I will deliver them into the hand of those who seek their lives — into the hand of Nebuchadrezzar king of Babylon and his officers. But afterward Egypt will be inhabited again as in the days of old, declares the LORD.",
      "T": "I will hand them over to their enemies, into the power of Nebuchadrezzar king of Babylon and his commanders. But after that, Egypt will be inhabited again as it was in ancient times. Yahweh declares it."
    },
    "27": {
      "L": "But as for you, fear not, O Jacob my servant, and do not be dismayed, O Israel; for behold, I am going to save you from far away and your offspring from the land of their captivity. Jacob shall return and have rest and ease, and no one shall make him afraid.",
      "M": "But as for you, do not fear, O Jacob my servant, and do not be dismayed, O Israel; for I am going to save you from far away and your descendants from the land of their captivity. Jacob will return and live in peace and security, and no one will make him afraid.",
      "T": "But you — do not be afraid, Jacob my servant. Do not be terrified, Israel. I am going to save you from distant lands, your children from the land where they are captive. Jacob will come home to peace and safety, and no one will ever threaten him again."
    },
    "28": {
      "L": "Fear not, O Jacob my servant, declares the LORD, for I am with you; for I will make a full end of all the nations where I have driven you, but of you I will not make a full end; I will discipline you in measure, and I will in no way leave you unpunished.",
      "M": "Fear not, O Jacob my servant, declares the LORD, for I am with you. I will make a complete end of all the nations to which I have driven you, but I will not make a complete end of you. I will discipline you with justice, but I will not leave you entirely unpunished.",
      "T": "Do not fear, Jacob my servant — Yahweh declares it — for I am with you. Every nation where I have scattered you I will destroy utterly. But you I will not destroy utterly. I will correct you, fairly and proportionately — but I will not let you go entirely unpunished."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'jeremiah')
        merge_tier(existing, JEREMIAH, tier_key)
        save(tier_dir, 'jeremiah', existing)
    print('Jeremiah 43–46 written.')

if __name__ == '__main__':
    main()
