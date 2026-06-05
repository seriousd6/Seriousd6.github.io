"""
MKT Echo Layer — John chapter 6
Run: python3 scripts/zc-echo-john-6-6.py

Source data used:
- data/interlinear/john.json (ch. 6 tokens)
- data/translation/draft/mediating/john.json (MKT text)
- data/parallels/john.json (absorbed: v14→Deut 18:15 upgraded to allusion; v31→Exod 16 quote; synoptic parallels for the feeding and water-walking excluded — NT-to-NT, not echo layer)

Note: Ten verses (3, 9, 14, 20, 31, 35, 45, 51, 63, 69) were written by
zc-echo-john-1-6.py and are present in data/echoes/john.json. merge_echo
will skip them; this script covers the remaining 61 verses.

Key decisions in this range:
- The chapter is structured as a new-Exodus episode: Passover near (v.4), feeding in
  a desolate place, bread-from-heaven discourse, wilderness murmuring (ἐγόγγυζον, vv.
  41, 43, 61 — same LXX word as Exod 16:2) → all classified as 'allusion' because John
  does not cite Exodus explicitly but the verbal and structural overlap is deliberate.
- Walking on water (vv. 18-19): 'allusion' to Job 9:8 and Ps 77:19 — God who treads
  the waves and whose path was through the sea. Jesus does not cite these texts but
  enacts what they assert about God alone.
- ἐγόγγυζον (vv. 41, 43, 61): 'allusion' to Exod 16:2 / Num 11:1 — exact LXX term
  for wilderness murmuring; classified 'allusion' (deliberate verbal echo, not citation).
- v40 "looks to the Son": 'type' connecting to Num 21:8-9 (look at the serpent and live)
  following the explicit application Jesus made in 3:14-15.
- v53 flesh-and-blood: 'type' to Exod 12 Passover lamb + Exod 24:8 covenant blood —
  both structural and verbal; not 'fulfillment' because John does not use fulfillment
  language here, but the type is tight.
- v62 Son of Man ascending: 'allusion' to Dan 7:13-14 — the Danielic Son of Man
  returning to the Ancient of Days; Jesus does not cite Dan 7 but the title and
  ascent-to-divine-presence are unmistakable.
- v64 betrayer foreknowledge: 'allusion' to Ps 41:9 — the bread-sharing close friend
  who turns; John 13:18 cites this psalm explicitly, so its presence here in the bread
  context is anticipatory and deliberate.
- Verses with no direct OT verbal allusion (vv. 7, 8, 16, 17, 22, 23, 24, 25, 59)
  carry 'theme' entries noting how they participate in the chapter's Exodus or
  shepherding framework.
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
    """Merge echo entries; deduplicate by (type, target) within each verse."""
    for ch, verses in new_data.items():
        if ch not in existing:
            existing[ch] = {}
        for v, entries in verses.items():
            if v not in existing[ch]:
                existing[ch][v] = entries
            else:
                seen = {(e['type'], e['target']) for e in existing[ch][v]}
                for e in entries:
                    if (e['type'], e['target']) not in seen:
                        existing[ch][v].append(e)
                        seen.add((e['type'], e['target']))


JOHN_CH6_ECHOES = {
  "6": {
    "1": [
      {
        "type": "theme",
        "target": "Exod 13:18",
        "note": "The opening geographic movement — across water toward a wilderness hillside at Passover time — sets the chapter's Exodus typology in motion. The Sea of Galilee functions as the narrative stage for a new-Exodus episode: bread from heaven, wilderness provision, murmuring crowds, and the disclosure of divine identity follow the structural contours of Israel's Sinai journey."
      }
    ],
    "2": [
      {
        "type": "allusion",
        "target": "Ps 78:11-12",
        "note": "The wilderness generation 'forgot his works and the wonders he had shown them' (Ps 78:11) despite following the God who performed miracles before their eyes. John's crowd pursues Jesus because of signs — a motive the Bread of Life discourse (v. 26) will expose as similarly inadequate: they followed the miracles without grasping their meaning."
      }
    ],
    "3": [
      {
        "type": "allusion",
        "target": "Exod 19:3",
        "note": "Moses went up the mountain to receive the Law and to mediate between God and Israel. Jesus going up a mountainside and sitting down with disciples mirrors this ascent pattern — the lawgiver-figure ascending to the place of divine disclosure before a feeding/teaching event that redefines Israel's relationship to bread from heaven."
      }
    ],
    "4": [
      {
        "type": "type",
        "target": "Exod 12:1-14",
        "note": "The Passover setting is not incidental. The feeding of the five thousand and the entire Bread of Life discourse unfold against the backdrop of the feast that commemorated Israel's rescue through the slain lamb. John structures the chapter around this Passover frame, climaxing in the flesh-and-blood language of vv. 53-56 — the lamb's flesh eaten, the covenant blood applied."
      }
    ],
    "5": [
      {
        "type": "allusion",
        "target": "Num 11:13",
        "note": "Moses cried out 'Where am I to get meat to give all this people?' — a question of human impossibility before divine provision. Jesus' question to Philip ('where shall we buy bread?') similarly exposes the disciples' human calculus (two hundred denarii, v. 7) before demonstrating that divine provision operates outside economic categories."
      }
    ],
    "6": [
      {
        "type": "allusion",
        "target": "Deut 8:2",
        "note": "God tested Israel in the wilderness 'to know what was in your heart' — not because God was ignorant, but to reveal Israel's dependence on him (Deut 8:3: 'man does not live on bread alone'). The Evangelist's aside mirrors this: Jesus tests Philip not because he lacks a plan, but to expose the shape of human reliance before divine action reshapes the situation."
      }
    ],
    "7": [
      {
        "type": "theme",
        "target": "2 Kgs 4:43",
        "note": "Elisha's servant asked 'How can I set this before a hundred men?' when instructed to feed them with twenty loaves. Philip's response is the same human arithmetic applied at far greater scale: the impossibility calculation is the foil that makes the miracle visible as miracle. The Elisha episode sets a precedent John's feeding scene knowingly exceeds."
      }
    ],
    "8": [
      {
        "type": "theme",
        "target": "1 Sam 17:17-18",
        "note": "Jesse sent David to the battlefield with bread and grain as a minor errand — the lesser figure who carries provisions into a situation of larger conflict. Andrew's role as the one who brings the boy with barley loaves to Jesus fits this pattern of the marginal figure whose act of presentation becomes the hinge of divine provision."
      }
    ],
    "9": [
      {
        "type": "allusion",
        "target": "2 Kgs 4:42-44",
        "note": "Elisha feeds a hundred men with twenty barley loaves and has leftovers — 'They ate and had some left over, as the LORD said.' The structural parallel is exact: small quantity, skeptical intermediary, miraculous multiplication, surplus. John's account escalates every dimension: five loaves, five thousand fed, twelve baskets surplus — signaling that Jesus exceeds the Elisha precedent by a prophetic order of magnitude."
      }
    ],
    "10": [
      {
        "type": "allusion",
        "target": "Ps 23:2",
        "note": "'He makes me lie down in green pastures' — the Shepherd Psalm's imagery of abundant provision in a place of rest is verbally evoked by the abundant grass (χόρτος πολύς) where five thousand men recline at Jesus' command. The echo frames Jesus as the divine shepherd providing in the wilderness, anticipating the 'I am the bread of life' disclosure that follows."
      }
    ],
    "11": [
      {
        "type": "type",
        "target": "Exod 16:4",
        "note": "The structure of Jesus' action — taking bread, giving thanks (εὐχαριστήσας), distributing as much as people want — mirrors the manna provision: God gave Israel bread from heaven, each receiving what they needed. The Passover timing (v. 4) adds a sacrificial register; the eucharistic overtones are deliberate and will be made explicit in the flesh-and-blood discourse of vv. 53-58."
      }
    ],
    "12": [
      {
        "type": "allusion",
        "target": "Exod 16:19-20",
        "note": "Moses commanded Israel not to leave manna overnight, a command many disobeyed. Jesus' instruction to gather fragments 'so that nothing is lost' (ἵνα μή τι ἀπόληται) inverts the manna economy: instead of expiry and scarcity, abundance is to be preserved. The same verb ἀπόλλυμι appears in v. 39 for the disciples Jesus will lose none of — the gathered fragments foreshadow the gathered people."
      }
    ],
    "13": [
      {
        "type": "theme",
        "target": "2 Kgs 4:44",
        "note": "Elisha's feeding miracle also had food left over 'as the LORD said' — surplus is the mark of divine provision exceeding human expectation. John adds the detail of twelve full baskets, tying the abundance to the twelve-tribes/apostles motif: the Twelve disciples (v. 67-70) gather the fragments of the new covenant community Jesus is forming around himself."
      }
    ],
    "14": [
      {
        "type": "allusion",
        "target": "Deut 18:15",
        "note": "The crowd's conclusion — 'Surely this is the Prophet who is to come into the world' — is an explicit identification with Moses' promise: 'The LORD your God will raise up for you a prophet like me from among you.' The feeding in the wilderness, with bread multiplied beyond natural means, triggers the Mosaic expectation. John's account shows the crowd correctly identifying the category while misapplying its political implication (v. 15)."
      }
    ],
    "15": [
      {
        "type": "allusion",
        "target": "1 Kgs 19:8-12",
        "note": "Elijah, fleeing the political violence of Ahab and Jezebel, went alone to Horeb — the mountain of God — to encounter the divine presence stripped of crowd and power. Jesus' retreat to the mountain when the crowd would crown him by force echoes this prophetic pattern: withdrawal from popular political pressure is the condition for authentic divine encounter, not flight from weakness but refusal to be defined by popular messianic categories."
      }
    ],
    "16": [
      {
        "type": "theme",
        "target": "Ps 107:23",
        "note": "Psalm 107 celebrates God's rescue of those who 'go down to the sea in ships' and encounter storm and darkness before divine deliverance. The disciples' descent to the sea as evening falls frames the episode that follows within this psalm's established pattern of maritime distress and divine rescue — a pattern John's reader would recognize as the shape of the episode before it unfolds."
      }
    ],
    "17": [
      {
        "type": "allusion",
        "target": "Ps 107:27-28",
        "note": "In Ps 107, sailors on the sea are 'at their wits' end' and 'cry to the LORD in their trouble.' The disciples' dark and directionless crossing — Jesus absent, storm rising — creates the exact situation Ps 107 describes. The episode is the narrative fulfillment of the psalm's pattern: distress in the dark sea, divine appearance, immediate arrival (v. 21)."
      }
    ],
    "18": [
      {
        "type": "allusion",
        "target": "Job 9:8",
        "note": "Job confesses that God 'alone stretches out the heavens and treads on the waves of the sea' (Job 9:8) — divine sovereignty over the chaos of the deep is presented as an exclusively divine prerogative. Jesus walking on the churning water in v. 19 is the narrative display of precisely this claim: only God treads the waves, and Jesus does what only God does."
      }
    ],
    "19": [
      {
        "type": "allusion",
        "target": "Ps 77:19",
        "note": "'Your path led through the sea, your way through the mighty waters, though your footprints were not seen' — Ps 77 celebrates God's Exodus crossing in terms of walking through the sea. Jesus walking on the water literalizes this Exodus theophany: the God whose path was through the sea now walks above it, revealing his identity (v. 20: ἐγώ εἰμι — I AM) in the act."
      }
    ],
    "20": [
      {
        "type": "allusion",
        "target": "Exod 3:14",
        "note": "Jesus' self-identification 'It is I' (Greek ἐγώ εἰμί, 'I AM') on the water echoes the divine name revealed to Moses at the burning bush. The use of ἐγώ εἰμί in a theophanic context — appearing on the water amid fear and darkness — mirrors OT divine-appearance formulas (cf. Isa 43:10-11; 51:12), where God announces his presence with 'I am he' to overcome fear."
      }
    ],
    "21": [
      {
        "type": "allusion",
        "target": "Ps 107:29-30",
        "note": "God 'stilled the storm to a whisper; the waves of the sea were hushed... he guided them to their desired haven' (Ps 107:29-30). The disciples' immediate arrival at shore — without further rowing, after receiving Jesus — recapitulates this psalm pattern: the distress of vv. 17-18 resolves through divine presence and the impossible journey is instantly completed."
      }
    ],
    "22": [
      {
        "type": "theme",
        "target": "Exod 14:22",
        "note": "Israel crossed through the sea while their pursuers could not follow by the same means; the crowd's inability to account for how Jesus crossed — only one boat, and he was not in it — mirrors the pattern of the miraculous transit that defies natural tracking. The Evangelist stresses the impossibility to mark Jesus' crossing as a sign in the category of Exodus wonders."
      }
    ],
    "23": [
      {
        "type": "theme",
        "target": "Gen 22:14",
        "note": "OT narrative regularly marks locations by the defining divine act that occurred there ('the LORD will provide — to this day it is said, On the mountain of the LORD it will be provided'). The narrator's parenthetical — locating these boats near 'the place where they had eaten the bread after the Lord had given thanks' — follows this convention: the site is defined by the eucharistic act, not its geography."
      }
    ],
    "24": [
      {
        "type": "theme",
        "target": "Deut 4:29",
        "note": "'If you seek the LORD your God, you will find him if you seek him with all your heart' — Deuteronomy frames earnest seeking as the condition of finding God. The crowd's energetic boat-crossing to find Jesus ironically resembles this faithful seeking while missing its object: v. 26 will reveal they pursue the sign-worker rather than the Sign itself, the bread-provider rather than the Bread."
      }
    ],
    "25": [
      {
        "type": "theme",
        "target": "Ps 139:7-8",
        "note": "'Where can I go from your Spirit? Where can I flee from your presence? If I go up to the heavens, you are there; if I make my bed in the depths, you are there.' The crowd's question — 'when did you get here?' — betrays their inability to account for Jesus' presence across an uncrossable sea. The Psalm's logic underlies the episode's irony: divine presence cannot be tracked by human categories of transport and timing."
      }
    ],
    "26": [
      {
        "type": "allusion",
        "target": "Ps 78:18-20",
        "note": "The wilderness generation 'tested God... by demanding the food they craved' (Ps 78:18) — pursuing the provision rather than the Provider. Jesus' indictment of the crowd's bread-seeking replays the Psalmist's analysis of the wilderness generation's failure: they saw the manna and still asked 'Can God prepare a table in the wilderness?' — gift without giver, sign without meaning."
      }
    ],
    "27": [
      {
        "type": "allusion",
        "target": "Isa 55:2",
        "note": "Isaiah's eschatological invitation asks 'Why spend money on what is not bread, and your labor on what does not satisfy?' — the contrast between perishing food and real sustenance freely given by God. Jesus sharpens this: the satisfying food is not something to purchase but to receive from the Son of Man, and the 'labor' for it (vv. 28-29) turns out to be belief — a reorientation of what it means to work."
      }
    ],
    "28": [
      {
        "type": "allusion",
        "target": "Mic 6:8",
        "note": "Micah's distillation of the law — 'What does the LORD require of you? To act justly, to love mercy, and to walk humbly with your God' — represents the OT tradition of reducing divine demand to its essence. Jesus' answer in v. 29 radically recenters the requirement: the singular work God requires is belief in the one he sent, displacing the plural works of moral and cultic performance."
      }
    ],
    "29": [
      {
        "type": "allusion",
        "target": "Deut 6:4-5",
        "note": "The Shema's call to love the LORD your God with all your heart, soul, and strength is the foundation of Israel's covenant obligation — a total orientation of the person toward God. Jesus' reduction of 'the works God requires' to a single act of belief echoes this shema logic: covenant life flows from a wholehearted orientation toward God, now exercised through the Son as its proper object."
      }
    ],
    "30": [
      {
        "type": "allusion",
        "target": "Num 14:11",
        "note": "'How long will these people treat me with contempt? How long will they refuse to believe in me, in spite of all the signs I have performed among them?' — God's lament to Moses after the wilderness generation demanded return to Egypt despite miraculous provision. The crowd's request for another sign — immediately after the feeding miracle — reprises this pattern exactly: sign-requiring unbelief despite signs already given."
      }
    ],
    "31": [
      {
        "type": "quote",
        "target": "Exod 16:4",
        "note": "The crowd quotes 'He gave them bread from heaven to eat' — conflating Exod 16:4 ('I will rain down bread from heaven') and Ps 78:24 ('he rained down manna for the people to eat, he gave them the grain of heaven'). The citation is real but its attribution is subtly wrong: God gave the manna through Moses, not Moses himself — a misattribution Jesus corrects directly in v. 32."
      }
    ],
    "32": [
      {
        "type": "allusion",
        "target": "Exod 16:15",
        "note": "When Israel saw the manna they asked 'What is it?' (מָן הוּא) and Moses explained 'It is the bread the LORD has given you to eat' — the manna was always God's gift through Moses, not Moses' own provision. Jesus' correction in v. 32 restores this agency: then as now, the Father is the source of bread from heaven. The shift is from past tense ('Moses gave') to present ('my Father gives') — the true bread is actively given now."
      }
    ],
    "33": [
      {
        "type": "type",
        "target": "Exod 16:4",
        "note": "The manna descended (יָרַד, LXX: καταβαίνω — 'come down') from heaven daily as physical provision for the wilderness camp. Jesus announces the fulfillment of that type: the bread that truly 'comes down from heaven' is not grain but a person, and its life-giving scope is not the camp of Israel but the whole world — the type's particularity is transcended by the antitype's universality."
      }
    ],
    "34": [
      {
        "type": "allusion",
        "target": "Num 11:4-6",
        "note": "The Israelites craved food in the wilderness and demanded 'Give us meat to eat!' — a request for perpetual provision in the form they already understood. The crowd's 'Lord, always give us this bread' similarly mistakes the substance (a person) for the type (food): they want perpetual manna before they understand that the bread Jesus offers is not grain to be distributed but himself to be received."
      }
    ],
    "35": [
      {
        "type": "allusion",
        "target": "Isa 55:1-2",
        "note": "Isaiah's eschatological invitation — 'Come, all you who are thirsty, come to the waters... why spend money on what is not bread?' — promises genuine satisfaction for those who come to God. Jesus' 'I am the bread of life; whoever comes to me will never go hungry, and whoever believes in me will never be thirsty' is the incarnate fulfillment of that invitation: the eschatological feast is not future but present in the person of the Son."
      }
    ],
    "36": [
      {
        "type": "allusion",
        "target": "Ps 78:22",
        "note": "The Psalmist summarizes the wilderness generation's failure: 'they did not believe in God or trust in his deliverance' — despite manna, water from the rock, and the pillar of cloud. Jesus' statement 'you have seen me and still you do not believe' echoes this verdict: sight of the miraculous does not produce faith, as the wilderness generation demonstrated, and the crowd here repeats."
      }
    ],
    "37": [
      {
        "type": "allusion",
        "target": "Isa 43:6-7",
        "note": "God promised the regathering of his people: 'Bring my sons from afar and my daughters from the ends of the earth — everyone who is called by my name, whom I created for my glory.' The Father's giving of people to the Son enacts this same divine initiative: God gathers his own to himself, and Jesus receives them as the place of that gathering — the 'I will never drive away' mirrors the unconditional nature of God's recall of the scattered."
      }
    ],
    "38": [
      {
        "type": "allusion",
        "target": "Ps 40:7-8",
        "note": "'I desire to do your will, my God; your law is within my heart' (Ps 40:7-8) — Hebrews 10:7 cites this psalm as Christ's declaration at the incarnation ('Here I am — it is written about me in the scroll — I have come to do your will, my God'). Jesus' self-description as one who descended to fulfill the Father's will rather than his own is the Johannine articulation of the same orientation: messianic mission as perfect alignment with the Father."
      }
    ],
    "39": [
      {
        "type": "allusion",
        "target": "Ezek 34:11-12",
        "note": "God declared through Ezekiel: 'I myself will search for my sheep and look after them... I will rescue them from all the places where they were scattered on a day of clouds and darkness.' Jesus' commitment to lose none of those given him fulfills this shepherding promise: the eschatological regathering of the scattered flock is concentrated in his person, with resurrection as the final rescue from the last scattering — death."
      }
    ],
    "40": [
      {
        "type": "type",
        "target": "Num 21:8-9",
        "note": "God instructed Moses to set up a bronze serpent so that 'when anyone was bitten and looked at the bronze serpent, they lived.' Jesus had applied this type explicitly in John 3:14-15 ('as Moses lifted up the serpent, so the Son of Man must be lifted up, that everyone who believes may have eternal life'). Verse 40's 'everyone who looks to the Son and believes' extends the type: seeing and believing in the lifted-up one is the condition of life, structurally identical to the wilderness bronze serpent."
      }
    ],
    "41": [
      {
        "type": "allusion",
        "target": "Exod 16:2",
        "note": "The Greek ἐγόγγυζον (grumbled) is the identical word used in the LXX for Israel's wilderness murmuring against Moses and Aaron in Exod 16:2 and Num 11:1. John's choice of this specific vocabulary is deliberate: the religious leaders' reaction to the Bread of Life discourse reprises the wilderness generation's murmuring response to divine provision — the same gift, the same unbelief, the same verb."
      }
    ],
    "42": [
      {
        "type": "allusion",
        "target": "Isa 53:2-3",
        "note": "Isaiah's Servant 'had no stately form or majesty that we should look at him, nothing in his appearance that we should desire him' — he was not recognized as the Lord's arm (Isa 53:1). The crowd's appeal to Jesus' human parentage to dismiss his heavenly origin is a form of this non-recognition: familiar origins (Joseph's son, known mother and father) become a stumbling block to receiving the one sent from God, exactly as Isa 53 predicted."
      }
    ],
    "43": [
      {
        "type": "allusion",
        "target": "Exod 16:7-8",
        "note": "Moses told Israel 'your grumbling is not against us, but against the LORD' and rebuked the murmuring directly (Exod 16:7-8). Jesus' command 'stop grumbling among yourselves' mirrors Moses' rebuke: the grumbling is not mere cultural dissatisfaction with Jesus but resistance to the Father who sent him (v. 44). Murmuring against the sent one is murmuring against the Sender."
      }
    ],
    "44": [
      {
        "type": "allusion",
        "target": "Jer 31:3",
        "note": "'I have loved you with an everlasting love; I have drawn you with unfailing kindness' (חֶסֶד — covenant-loyalty) — God draws his people to himself through his own prior initiative before they turn. Jesus applies the same drawing language (ἑλκύσῃ) to the Father's role in bringing people to the Son: divine sovereignty in salvation is the new-covenant form of the same hesed initiative Jeremiah announced."
      }
    ],
    "45": [
      {
        "type": "quote",
        "target": "Isa 54:13",
        "note": "Jesus explicitly cites 'It is written in the Prophets: They will all be taught by God' — reproducing the substance of Isa 54:13 ('all your children will be taught by the LORD, and great will be their peace'). The divine teaching promised to restored Israel is now located in coming to the Son: hearing the Father and learning from him leads to Jesus, not to the Torah study of the synagogue alone."
      }
    ],
    "46": [
      {
        "type": "allusion",
        "target": "Exod 33:20",
        "note": "God told Moses 'you cannot see my face, for no one may see me and live' — the invisibility of the divine face is a foundational OT constraint, reinforced in Isa 6:5 (Isaiah's dread at seeing the LORD) and 1 Tim 6:16 (God 'lives in unapproachable light'). Jesus' claim to exclusive access — 'only he who is from God has seen the Father' — positions him as the single exception to Exod 33:20: the one for whom the divine face is not deadly but constitutive of his identity."
      }
    ],
    "47": [
      {
        "type": "theme",
        "target": "Deut 30:15-19",
        "note": "Moses set before Israel 'life and prosperity, death and destruction... choose life, so that you and your children may live.' The covenant framing of obedience as the path to life underlies Jesus' distillation: the two-way path of Deuteronomy (obey and live, disobey and die) is now presented as the christological fork between belief and unbelief in the Son. The same life is offered; the condition has been transformed."
      }
    ],
    "48": [
      {
        "type": "type",
        "target": "Exod 16:4",
        "note": "The second 'I am the bread of life' (cf. v. 35) restates the type after the discourse on divine drawing (vv. 44-47): belief has a concrete object, and that object is the bread himself. The manna was the prototype — God-given, descending from heaven, daily, physical — and Jesus is the antitype: God-sent, descended from heaven, received once in faith, life-giving."
      }
    ],
    "49": [
      {
        "type": "allusion",
        "target": "Num 14:29-33",
        "note": "God declared that the wilderness generation 'will fall — their bodies will drop in this wilderness' because of their unbelief. Jesus invokes this historical death to establish the manna's essential limitation: physical provision without faith produced corpses in the desert, not inheritors of the promise. The manna fed bodies that still died; the true bread gives a life the wilderness generation never reached."
      }
    ],
    "50": [
      {
        "type": "type",
        "target": "Gen 3:22",
        "note": "After the fall, God excluded humanity from the Tree of Life lest they 'eat and live forever' in a state of sin — access to eternal life was barred at Eden. Jesus offers bread that anyone may eat and not die, reversing the Eden exclusion: the barrier to life-without-end is removed not by re-entering the garden but by receiving the one who is the bread from heaven — the tree's antitype in human form."
      }
    ],
    "51": [
      {
        "type": "allusion",
        "target": "Isa 53:12",
        "note": "The Servant 'poured out his life unto death' and 'bore the sin of many.' Jesus' offer — 'this bread is my flesh, which I will give for the life of the world' — maps onto the Servant's self-giving: flesh given for others, death as the mode of provision for life. The Evangelist does not cite Isa 53 here, but the structural parallel between the Servant's self-giving and Jesus' language of flesh-given-for-life is deliberate and close."
      }
    ],
    "52": [
      {
        "type": "allusion",
        "target": "Num 11:4-6",
        "note": "Israel craved meat in the wilderness and reduced God's provision to a physical demand: 'Give us meat to eat!' Moses despaired of satisfying their literal appetite. The crowd's objection — 'how can this man give us his flesh to eat?' — repeats this pattern of collapsing divine provision into literal categories, demanding a physical mechanism for what is being offered as a sacramental and incarnational reality."
      }
    ],
    "53": [
      {
        "type": "type",
        "target": "Exod 24:8",
        "note": "Moses sprinkled the covenant blood on the people, saying 'This is the blood of the covenant that the LORD has made with you.' The covenant was ratified through blood participation — the community was constituted by contact with the blood of sacrifice. Jesus intensifies this: the new covenant requires internalizing his blood, not receiving its external sprinkling, and the flesh language recalls the Passover lamb whose flesh was eaten and whose blood averted judgment (Exod 12:7-8)."
      }
    ],
    "54": [
      {
        "type": "allusion",
        "target": "Dan 12:2",
        "note": "'Multitudes who sleep in the dust of the earth will awake: some to everlasting life, others to shame and everlasting contempt' — Daniel's resurrection prophecy is the closest OT parallel to bodily resurrection at a definitive eschatological moment. Jesus' promise of raising up the flesh-and-blood participant 'at the last day' claims the same horizon but reframes it: the condition of belonging to the resurrection of life is union with the Son through receiving his flesh and blood."
      }
    ],
    "55": [
      {
        "type": "allusion",
        "target": "Ps 23:5",
        "note": "God 'prepares a table before me in the presence of my enemies; my cup overflows' — the Shepherd Psalm's abundant table provided by the divine host is the background for Jesus' claim that his flesh is real food and his blood real drink. The Psalm's cup and table represent genuine, satisfying provision from God himself; Jesus asserts that his person is the substance those images anticipated."
      }
    ],
    "56": [
      {
        "type": "allusion",
        "target": "Ezek 37:27",
        "note": "'My dwelling place will be with them; I will be their God, and they will be my people' — Ezekiel's vision of restored covenant culminates in mutual indwelling. The 'remains in me and I in them' language is the eschatological covenant indwelling Ezekiel anticipated: not proximity or patronage but organic mutual presence. The meal that effects this union is the Johannine vehicle for Ezekiel's new-covenant promise."
      }
    ],
    "57": [
      {
        "type": "theme",
        "target": "Ps 36:9",
        "note": "'With you is the fountain of life; in your light we see light' — the Psalmist traces life itself to God as its ultimate source. Jesus articulates a chain of derived life: the Father is the fount; the Son lives by the Father (ζῶ διὰ τὸν πατέρα); those who feed on the Son live by him. This participatory chain extends the Psalm's theology of divine source into incarnate, transmissible form."
      }
    ],
    "58": [
      {
        "type": "type",
        "target": "Exod 16:35",
        "note": "Israel ate manna 'forty years until they came to a land that was settled; they ate manna until they reached the border of Canaan' — the manna was provisional, bounded by the wilderness period, and terminated when the journey ended. Jesus' true bread has no such expiry or territorial limit: it gives life to the world (v. 33), and the life it gives is eternal (ζήσει εἰς τὸν αἰῶνα), persisting beyond all temporal and geographic boundaries."
      }
    ],
    "59": [
      {
        "type": "theme",
        "target": "Deut 4:10",
        "note": "God commanded Israel to 'assemble the people before me to hear my words' — divine teaching delivered at a formal gathered place. The synagogue at Capernaum is the institutional heir of this assembly tradition. The Bread of Life discourse is delivered in the same context of gathered Israel being addressed by God's word, now in the person of the Son who himself is the subject of what Moses pointed toward."
      }
    ],
    "60": [
      {
        "type": "allusion",
        "target": "Num 14:2-4",
        "note": "The wilderness generation said 'if only we had died in Egypt' and proposed choosing a new leader to return — they could not receive the provision that exceeds their categories. The disciples' complaint about a 'hard saying' and who can 'accept' (ἀκούειν — hear, receive) it replays this pattern: faced with divine bread that is scandalous to the natural appetite, many choose the familiar over the divine offer."
      }
    ],
    "61": [
      {
        "type": "allusion",
        "target": "Exod 16:8",
        "note": "Moses told Israel 'the LORD has heard your grumbling against him' — God's knowledge of the wilderness murmuring was complete despite the complaining being directed at Moses. Jesus' awareness of the disciples' grumbling (without being told) mirrors this divine omniscience: the provider knows the complaint, and the complaint reveals the heart of the complainer rather than a defect in what is provided."
      }
    ],
    "62": [
      {
        "type": "allusion",
        "target": "Dan 7:13-14",
        "note": "'One like a son of man, coming with the clouds of heaven, approached the Ancient of Days and was led into his presence. He was given authority, glory and sovereign power.' Jesus' reference to the Son of Man ascending to 'where he was before' invokes the Danielic vision of the Son of Man entering the divine presence — the ascension is the visible fulfillment of Dan 7's enthronement, confirming that his origin is the throne, not Nazareth."
      }
    ],
    "63": [
      {
        "type": "allusion",
        "target": "Ezek 37:14",
        "note": "'I will put my Spirit in you and you will live' — Ezekiel's dry bones passage climaxes in the Spirit as the exclusive source of life. Jesus' statement 'the Spirit gives life; the flesh counts for nothing' applies the same principle to his own discourse: the flesh-and-blood language of vv. 53-58 is not a cannibalistic prescription but a Spirit-mediated gift. The words themselves 'are full of the Spirit and life' in the way Ezekiel's breath-from-God was."
      }
    ],
    "64": [
      {
        "type": "allusion",
        "target": "Ps 41:9",
        "note": "'Even my close friend, someone I trusted, one who shared my bread, has turned against me' — the psalm explicitly cited for Judas in John 13:18 ('he who shares my bread has lifted up his heel against me'). Introducing Judas's foreknown betrayal here in the bread-sharing context of ch. 6 creates deliberate resonance with Ps 41:9: the one who will betray is already eating at the table of the one who is the Bread of Life."
      }
    ],
    "65": [
      {
        "type": "allusion",
        "target": "Jer 31:3",
        "note": "The Father's enabling (δέδοται — has been given) restates the hesed initiative of v. 44 with the same theological logic: God draws his people before they turn to him. This parallels Jeremiah's new-covenant promise that God will draw his people with unfailing kindness — divine initiative precedes and conditions human response. The same anchor point governs both the perseverance of the believing (v. 39) and the origin of belief itself."
      }
    ],
    "66": [
      {
        "type": "allusion",
        "target": "Num 14:4",
        "note": "'The people said to each other, We should choose a leader and go back to Egypt' — wholesale defection from God's appointed provision when the journey proved too demanding. The mass departure of disciples from Jesus ('no longer walked with him') parallels this Exodus moment exactly: faced with provision that exceeds the categories of their expectations, many turn back to the familiar."
      }
    ],
    "67": [
      {
        "type": "allusion",
        "target": "Josh 24:15",
        "note": "Joshua's covenant renewal confronted Israel with a fork: 'Choose for yourselves this day whom you will serve — whether the gods your ancestors served beyond the Euphrates, or the gods of the Amorites, in whose land you are living.' Jesus turns to the Twelve with the same rhetorical choice: the crowd has defected; will they also go? The question mirrors Joshua's challenge to covenant loyalty at the moment of mass apostasy."
      }
    ],
    "68": [
      {
        "type": "allusion",
        "target": "Deut 30:19-20",
        "note": "Moses set before Israel 'life and death, blessings and curses... choose life, so that you and your children may live, and that you may love the LORD your God, listen to his voice, and hold fast to him.' Peter's response is the choosing of life: 'to whom shall we go?' acknowledges there is no other source of life, and 'words of eternal life' collapses Moses' blessing language into Jesus himself — he is not the pointer to life but life's content."
      }
    ],
    "69": [
      {
        "type": "theme",
        "target": "Ps 16:10",
        "note": "Peter's confession 'the Holy One of God' (ὁ ἅγιος τοῦ θεοῦ) applies a designation used of the LORD's anointed in Ps 16:10 ('you will not let your holy one see decay') — a psalm Acts 2:27-31 interprets as a messianic prophecy fulfilled in Jesus' resurrection. The title anticipates the passion and resurrection: the one confessed as holy will be vindicated by God in precisely the terms Ps 16 promised."
      }
    ],
    "70": [
      {
        "type": "allusion",
        "target": "Ps 55:12-14",
        "note": "David laments the treachery of 'a close friend, one I walked with at the house of God' — the betrayal of the intimate companion is more devastating than enemy opposition. Jesus' disclosure that one of his chosen twelve is a devil (διάβολος) anticipates the betrayal pattern of Ps 55 and Ps 41:9 (signaled in v. 64): election and treachery coexist within the covenant community, as they did within the twelve tribes of Israel."
      }
    ],
    "71": [
      {
        "type": "theme",
        "target": "1 Sam 16:7",
        "note": "God's word to Samuel — 'the LORD does not look at things people look at; people look at outward appearance, but the LORD looks at the heart' — frames the election and treachery theme closing chapter 6. Judas was chosen, numbered among the Twelve, outwardly indistinguishable; Jesus' foreknowledge of his betrayal (vv. 64, 70) is the divine seeing that penetrates where human election processes cannot. The Evangelist names him to confirm that no betrayal escapes divine foreknowledge."
      }
    ]
  }
}


def main():
    existing = load_echo('john')
    merge_echo(existing, JOHN_CH6_ECHOES)
    save_echo('john', existing)
    print('John 6 echoes written.')

if __name__ == '__main__':
    main()
