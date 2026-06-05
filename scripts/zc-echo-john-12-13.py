"""
MKT Echo Layer — John chapters 12–13
Run: python3 scripts/zc-echo-john-12-13.py

Source data used:
- data/interlinear/john.json (Strongs tokens, chs 12–13)
- data/translation/draft/mediating/john.json (MKT text)
- data/translation/glossary-greek.json (G26 agapē, G1391 doxa, G5456 phōnē)
- data/parallels/john.json (ch12: vv 1, 12, 15, 38, 40; ch13: vv 18, 21 — absorbed)
- data/echoes/john.json (pre-existing entries for chs 1–6 — merge preserves these)
- data/commentary/ellicott/john.json, data/commentary/jfb/john.json

Key decisions:
- 12:3: The anointing is distinct from Luke 7:36-50 (different woman, place, occasion).
  Mary's act is treated here; Synoptic Bethany parallels absorbed as 'theme' (same event
  type, different angle) not duplicate echoes.
- 12:8: Deut 15:11 is the direct verbal antecedent for "the poor you always have with you" —
  classified as 'allusion' because John does not use the LXX quotation formula.
- 12:15: Zech 9:9 is a fulfillment citation; Isa 40:9/62:11 is classified as 'allusion'
  for the "Daughter Zion" address common to both.
- 12:31: "prince of this world" echoes Dan 10 principalities and Gen 3:15; both included.
- 12:32: Num 21:8-9 already present in John 3:14 echo layer (earlier script); not duplicated.
  Isa 52:13 (lifted up → exaltation) is the primary echo here for ch 12.
- 12:38,40: Parallels file lists these as 'prophecy-source'; promoted to 'fulfillment' (12:38)
  and 'quote' (12:40) because John uses the explicit fulfillment formula for both.
- 12:41: Isa 6:1-3 — John's claim that Isaiah saw the Son's glory is itself the interpretive
  key; echo classified as 'fulfillment' of the vision content.
- 13:16: The shaliach principle (a sent one is as the sender) is attested in rabbinic sources
  but the OT background is the Mal 3:1 messenger-sent theology; cited as 'allusion'.
- 13:18: Ps 41:9 — parallels file has this as 'prophecy-source'; promoted to 'fulfillment'
  because John uses hina plērōthē (so that the scripture might be fulfilled).
- 13:34: Lev 19:18 classified as 'shadow' not 'fulfillment' — Jesus calls the command new
  because the standard shifts from "as yourself" to "as I have loved you"; same OT root,
  Christologically transformed.
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


JOHN_ECHOES = {
  "12": {
    "1": [
      {
        "type": "theme",
        "target": "Exod 12:3-6",
        "note": "Six days before the Passover lamb was selected and set apart. John's precise time marker ('six days before the Passover') situates the Bethany events inside the countdown to slaughter, framing Jesus' arrival as the arrival of the lamb."
      },
      {
        "type": "theme",
        "target": "Matt 26:6-13",
        "note": "The Synoptic anointing at Bethany in Simon the leper's house (Matt 26:6-13; Mark 14:3-9) is a closely related tradition. John's account places Mary, Martha, and Lazarus at center and adds the detail that the house was filled with the fragrance — the parallel illuminates the shared theological weight (preparation for burial) despite differing details."
      }
    ],
    "2": [
      {
        "type": "allusion",
        "target": "Ps 23:5",
        "note": "The psalm declares 'You prepare a table before me in the presence of my enemies.' The Bethany dinner is set against the backdrop of plots against both Jesus and Lazarus (v. 10); the covenant meal in the shadow of death echoes the psalmist's confidence that the shepherd-host provides even in danger."
      }
    ],
    "3": [
      {
        "type": "allusion",
        "target": "Song 1:12",
        "note": "The Song of Songs speaks of nard's fragrance when the king reclines at his table. Mary's act of anointing with nard at the reclining table is set in the same sensory register — costly perfume, the beloved present, a scent that fills the room. Whether deliberate or not, the echo frames the act as one of intimate devotion."
      },
      {
        "type": "allusion",
        "target": "Isa 60:6",
        "note": "Isaiah's vision of the nations bringing gold and frankincense, 'and they shall bring good news, the praises of the LORD.' The house filled with fragrance evokes the eschatological offering; Mary's costly act is the prototype of the worship the nations will bring when the king arrives."
      }
    ],
    "4": [
      {
        "type": "allusion",
        "target": "Ps 41:9",
        "note": "The psalm ('He who shared my bread has lifted his heel against me') is explicitly cited at 13:18, but Judas is introduced here as the objector at the table — the same dynamic of a close companion souring toward the lord he serves. John flags the connection before the citation."
      }
    ],
    "5": [
      {
        "type": "allusion",
        "target": "Zech 11:12-13",
        "note": "The thirty pieces of silver are paid as the price of the shepherd in Zechariah — the connection between money, betrayal, and the valuation of the servant-shepherd is activated when Judas calculates nard's worth in denarii and later accepts payment for betrayal."
      }
    ],
    "6": [
      {
        "type": "theme",
        "target": "Ps 55:12-14",
        "note": "The psalmist laments that it was not an enemy who betrayed him but 'a man like myself, my companion, my close friend, with whom I once enjoyed sweet fellowship.' Judas as the treasurer-disciple who pilfers the common fund is a close companion turning hostile — the psalm's portrait of intimate betrayal is realized in miniature here before the larger betrayal."
      }
    ],
    "7": [
      {
        "type": "allusion",
        "target": "Num 19:11-13",
        "note": "The Mosaic law required elaborate purification for contact with the dead, but Jesus subverts the logic: Mary's anointing anticipates his burial without any suggestion of contamination flowing from corpse to devotee. The one who overcomes death cannot be defiled by proximity to it."
      }
    ],
    "8": [
      {
        "type": "allusion",
        "target": "Deut 15:11",
        "note": "Jesus' words ('you will always have the poor with you') are a near-verbal echo of Deut 15:11: 'There will always be poor people in the land.' The Deuteronomy context is a command to be openhanded toward the poor — Jesus is not dismissing obligation to the poor but asserting the unrepeatable urgency of his own presence."
      }
    ],
    "9": [
      {
        "type": "theme",
        "target": "Ezek 37:1-14",
        "note": "Lazarus raised from the dead draws a large crowd — the sign of resurrection life functions as the sign Ezekiel foresaw: when the breath of God enters the dry bones, 'the whole house of Israel' takes note. Lazarus is the enacted preview of the general resurrection that galvanizes Israel's attention."
      }
    ],
    "10": [
      {
        "type": "allusion",
        "target": "Jer 26:11",
        "note": "The priests and prophets conspired to put Jeremiah to death for his preaching. The chief priests' council to kill Lazarus (the living evidence of Jesus' power) follows the same logic: eliminate the witness. The pattern of priestly opposition to the one God has sent recurs in both cases."
      }
    ],
    "11": [
      {
        "type": "theme",
        "target": "Isa 52:10",
        "note": "Isaiah declares: 'The LORD will lay bare his holy arm in the sight of all the nations, and all the ends of the earth will see the salvation of our God.' The many Jews transferring their allegiance to Jesus because of the resurrection sign is the beginning of the visible saving act drawing people from across the covenant community."
      }
    ],
    "12": [
      {
        "type": "fulfillment",
        "target": "Ps 118:25-26",
        "note": "The crowd's cry 'Hosanna! Blessed is he who comes in the name of the LORD!' quotes Ps 118:25-26 verbatim — the Hallel psalm sung at Passover pilgrimage arrivals. Applying it to Jesus as the arriving king shifts the psalm from liturgical greeting to messianic acclamation; John presents it as fulfilled in this moment."
      },
      {
        "type": "allusion",
        "target": "Lev 23:40",
        "note": "Palm branches (lulavim) are prescribed for the Feast of Tabernacles (Sukkot), not Passover — the crowd uses Tabernacles' ritual object at the Passover festival. The conflation signals the eschatological character of the entry: all the feasts converge on this arrival."
      }
    ],
    "13": [
      {
        "type": "fulfillment",
        "target": "Ps 118:26",
        "note": "'Blessed is he who comes in the name of the LORD!' — the pilgrimage psalm reaches its intended referent in Jesus. The crowd in Ps 118 greets a king returning victorious from battle; the crowd in Jerusalem greets one whose victory will be won through death."
      },
      {
        "type": "theme",
        "target": "Zeph 3:14-15",
        "note": "Zephaniah calls Daughter Zion to shout for joy: 'The LORD has taken away your punishment, he has turned back your enemy. The LORD, the King of Israel, is with you; never again will you fear any harm.' The crowd's greeting echoes the tone of this prophetic welcome of the divine king."
      }
    ],
    "14": [
      {
        "type": "fulfillment",
        "target": "Zech 9:9",
        "note": "John cites this verse directly (v. 15 paraphrases it): 'See, your king comes to you, righteous and victorious, lowly and riding on a donkey, on a colt, the foal of a donkey.' The riding of a donkey rather than a war-horse is the precise detail that identifies Jesus' entry as the fulfillment of Zechariah's peaceable king."
      }
    ],
    "15": [
      {
        "type": "fulfillment",
        "target": "Zech 9:9",
        "note": "John's paraphrase of Zech 9:9 ('Do not be afraid, Daughter Zion; see, your king is coming, seated on a donkey's colt') explicitly marks this as scripture being fulfilled. The Zechariah king enters not as a military conqueror but as one bringing salvation — his weapon is peace."
      },
      {
        "type": "allusion",
        "target": "Isa 40:9",
        "note": "Isaiah addresses Daughter Zion as herald: 'Say to the towns of Judah, Here is your God!' The same address ('Daughter Zion') with a royal arrival announces the LORD's coming. John's narrative places Jesus in the position Isaiah envisioned: the God who comes to his people."
      }
    ],
    "16": [
      {
        "type": "theme",
        "target": "Ps 22:1-31",
        "note": "Psalm 22 describes a suffering servant whose situation is only fully understood in retrospect — the psalmist moves from dereliction to vindication in a way only comprehensible after the rescue. The disciples' retrospective understanding ('only after Jesus was glorified did they realize') is the interpretive pattern that applies to many OT texts: their meaning becomes clear after the event."
      }
    ],
    "17": [
      {
        "type": "theme",
        "target": "Isa 43:10",
        "note": "'You are my witnesses,' declares the LORD, 'and my servant whom I have chosen.' The crowd that witnessed Lazarus' resurrection becomes the witness-base for Jesus' entry; they testify not to abstract doctrine but to a specific act they saw. The eyewitness-as-covenant-witness pattern runs from Isa 43 through John's Gospel."
      }
    ],
    "18": [
      {
        "type": "theme",
        "target": "Isa 35:5-6",
        "note": "Isaiah's messianic sign-cluster includes the healing of the lame, blind, deaf, and mute. The 'sign' (sēmeion) of raising Lazarus is one such messianic indicator; people flock to Jesus because they have heard the sign, the same way Isaiah's healing signs were expected to identify the age of salvation."
      }
    ],
    "19": [
      {
        "type": "allusion",
        "target": "Ps 2:1-2",
        "note": "The Pharisees' complaint — 'the whole world has gone after him' — is the despair of those who resist the LORD's anointed. Ps 2 opens with nations and rulers raging against the LORD and his anointed; here the agents of resistance concede they are losing, while the psalm declares the futility of such opposition."
      }
    ],
    "20": [
      {
        "type": "fulfillment",
        "target": "Isa 56:6-7",
        "note": "Isaiah prophesies that foreigners who bind themselves to the LORD will be brought to his holy mountain: 'my house will be called a house of prayer for all nations.' Greeks coming up to worship at the feast and then seeking Jesus is the beginning of this ingathering — the moment John uses to trigger Jesus' announcement that the hour has come (v. 23)."
      }
    ],
    "21": [
      {
        "type": "allusion",
        "target": "Zech 8:22-23",
        "note": "Zechariah envisions many peoples and powerful nations coming to Jerusalem to seek the LORD: 'In those days ten people from all languages and nations will take firm hold of one Jew by the hem of his robe and say, Let us go with you, because we have heard that God is with you.' The Greeks' request — 'we would like to see Jesus' — is the fulfillment of this prophetic vision of Gentile approach."
      }
    ],
    "22": [
      {
        "type": "theme",
        "target": "Num 27:2",
        "note": "In the OT the approach of those outside the immediate circle (daughters of Zelophehad, Gentile converts) requires mediation through the designated leader who then brings the matter before the LORD. Philip and Andrew mediate the Greeks' request in the same pattern — the approach of the nations must be brought before the one appointed to receive it."
      }
    ],
    "23": [
      {
        "type": "allusion",
        "target": "Dan 7:13-14",
        "note": "The Son of Man receives glory and dominion before the Ancient of Days. Jesus' announcement that 'the hour has come for the Son of Man to be glorified' activates the Danielic register — but the glorification will come through the cross before the throne, inverting the sequence while fulfilling the destination."
      },
      {
        "type": "allusion",
        "target": "Isa 52:13",
        "note": "Isaiah's Servant Song opens: 'See, my servant will act wisely; he will be raised and lifted up and highly exalted.' The path of the Servant is suffering → glorification. Jesus uses 'glorified' (doxasthē) where Isaiah's LXX uses doxasthēsetai — the same vocabulary for the same trajectory."
      }
    ],
    "24": [
      {
        "type": "allusion",
        "target": "Isa 53:10",
        "note": "After the Servant's suffering, 'he will see his offspring and prolong his days, and the will of the LORD will prosper in his hand.' The grain of wheat that dies and bears much fruit is the agricultural image for the same logic: death as the condition for abundant life and progeny. The Servant's death produces the 'many' who are justified (Isa 53:11)."
      },
      {
        "type": "allusion",
        "target": "Hos 2:21-23",
        "note": "Hosea uses the language of sowing and harvest for the restoration of Israel: God will 'sow her for myself in the land.' The grain-of-wheat image trades on the same agricultural theology — death, planting, and abundant harvest as the pattern of divine redemption and community renewal."
      }
    ],
    "25": [
      {
        "type": "theme",
        "target": "Prov 8:35-36",
        "note": "Proverbs frames the choice for or against wisdom in life-and-death terms: 'Whoever finds me finds life... whoever fails to find me harms himself; all who hate me love death.' Jesus' paradox — loving one's life loses it; hating one's life keeps it — is structurally the same inversion: the counter-intuitive path (relinquishment) is the path to life."
      }
    ],
    "26": [
      {
        "type": "allusion",
        "target": "Isa 56:4-7",
        "note": "The servants who hold fast to God's covenant will be brought to the holy mountain and given a name that endures — 'an everlasting name that will endure forever.' Jesus' promise that 'where I am, my servant also will be' and that the Father will honor him is the personal form of this covenantal pledge."
      },
      {
        "type": "allusion",
        "target": "Ps 23:6",
        "note": "'Surely your goodness and love will follow me all the days of my life, and I will dwell in the house of the LORD forever.' The Servant's promise of presence — 'where I am, my servant also will be' — fulfills the psalmist's hope of dwelling with the LORD permanently."
      }
    ],
    "27": [
      {
        "type": "allusion",
        "target": "Ps 6:3-4",
        "note": "'My soul is in deep anguish. How long, LORD, how long? Turn, LORD, and deliver me.' The psalmist's language of a soul in distress becomes Jesus' own idiom in v. 27 ('Now my soul is troubled'). This is John's equivalent of Gethsemane (cf. Matt 26:38) — the Passion's interior moment, cast in the language of the Psalms."
      },
      {
        "type": "allusion",
        "target": "Ps 42:6",
        "note": "'Why, my soul, are you downcast? Why so disturbed within me?' The son of Korah's refrain captures the tension between present anguish and trust in God — the same tension Jesus expresses: his soul is troubled, yet he does not ask to be saved from the hour, because the hour is the purpose."
      }
    ],
    "28": [
      {
        "type": "allusion",
        "target": "Isa 6:3",
        "note": "The seraphim declare 'the whole earth is full of his glory.' The Father's response from heaven — 'I have glorified it, and will glorify it again' — is the divine self-assertion of glory that Isaiah's vision displayed. What the seraphim proclaimed as cosmic fact, the Father now announces as historical event through and in the Son."
      },
      {
        "type": "allusion",
        "target": "Exod 19:16-19",
        "note": "At Sinai, the LORD's voice came with thunder, fire, and earthquake — the crowd at Sinai heard a sound they could not fully comprehend. At Jerusalem, the Father speaks from heaven and the crowd hears only thunder. The same pattern: the divine voice at the covenant moment is heard by the masses as natural phenomenon, understood only by those with ears to hear."
      }
    ],
    "29": [
      {
        "type": "allusion",
        "target": "Ps 29:3-9",
        "note": "Psalm 29 is entirely the voice of the LORD — 'The voice of the LORD is over the waters; the God of glory thunders.' The crowd's interpretation ('it thundered') is theologically correct in a way they cannot see: it is precisely the voice of the LORD that they hear, just as Psalm 29 describes — God's voice over and in the storm."
      }
    ],
    "30": [
      {
        "type": "allusion",
        "target": "Deut 4:36",
        "note": "Moses tells Israel: 'From heaven he made you hear his voice to discipline you.' The divine voice from heaven is pedagogy — not primarily display but instruction for the people. Jesus says the voice came not for himself but for the crowd; he frames the event in the same pedagogical register Moses used for Sinai."
      }
    ],
    "31": [
      {
        "type": "allusion",
        "target": "Gen 3:15",
        "note": "The casting out of the prince of this world (archōn tou kosmou) enacts the promise to Eve: 'I will put enmity between you and the woman, and between your offspring and hers; he will crush your head, and you will strike his heel.' The cross is the moment of the serpent's decisive defeat — the heel-strike and the head-crushing occur simultaneously."
      },
      {
        "type": "allusion",
        "target": "Dan 10:13-20",
        "note": "Daniel's visions name 'the prince of Persia' and 'the prince of Greece' as spiritual powers behind earthly kingdoms. Jesus' 'prince of this world' is cast in the same framework — a cosmic ruler whose expulsion is the prerequisite for God's kingdom to extend without rival."
      }
    ],
    "32": [
      {
        "type": "allusion",
        "target": "Isa 52:13",
        "note": "The Servant 'will be raised and lifted up (hypsōthēsetai) and highly exalted.' John uses the same verb hypsōthō for Jesus' crucifixion-and-exaltation (vv. 32, 34) — the lifting up on the cross is simultaneously the lifting up into glory. Isaiah's trajectory of humiliation-then-exaltation is collapsed into a single event."
      },
      {
        "type": "allusion",
        "target": "Isa 11:12",
        "note": "Isaiah promises the root of Jesse will 'raise a banner for the nations and gather the exiles of Israel; he will assemble the scattered people of Judah from the four corners of the earth.' Jesus' 'I will draw all people to myself' is the first-person claim to be this banner — the crucified Christ as the gathering point of the nations."
      }
    ],
    "33": [
      {
        "type": "theme",
        "target": "Num 21:8-9",
        "note": "The bronze serpent 'lifted up' in the wilderness (already cited in John 3:14) provides the typological background for 'lifting up' as death-by-elevation. John's narrator interprets Jesus' statement as indicating the manner of his death, exactly as Moses' lifted serpent indicated what the Israelites needed to look at to live."
      }
    ],
    "34": [
      {
        "type": "allusion",
        "target": "Ps 89:36-37",
        "note": "The crowd cites 'the Law' that the Messiah remains forever — Ps 89 declares David's offspring will endure forever: 'his throne will endure before me like the sun; it will be established forever like the moon.' The crowd holds an expectation of permanent messianic reign that cannot square with Jesus' language of being 'lifted up' to die."
      },
      {
        "type": "allusion",
        "target": "Isa 9:7",
        "note": "'Of the greatness of his government and peace there will be no end.' The Isaianic messianic figure reigns without end — 'the zeal of the LORD Almighty will accomplish this.' The crowd's confusion arises from a correct reading of these texts; Jesus does not deny the permanence but redefines its path."
      }
    ],
    "35": [
      {
        "type": "allusion",
        "target": "Isa 2:5",
        "note": "'Come, descendants of Jacob, let us walk in the light of the LORD.' The invitation to walk in the light while it is available echoes Isaiah's summons. But Isaiah addresses those turning from idols to the LORD; Jesus addresses those who have the light present in person and will soon lose the opportunity."
      },
      {
        "type": "allusion",
        "target": "Ps 119:105",
        "note": "'Your word is a lamp for my feet, a light on my path.' The light that guides the walking is now identified with a person, not a text — Jesus is the light that must be followed before it departs. The lamp metaphor of the Psalm is concentrated and personalized."
      }
    ],
    "36": [
      {
        "type": "allusion",
        "target": "Isa 60:1-3",
        "note": "'Arise, shine, for your light has come, and the glory of the LORD rises upon you... Nations will come to your light.' Jesus' call to 'become children of light' and then hide himself enacts the same pattern of light-offered-and-withdrawn that Isa 60 uses for the age of gathering — the light of the LORD comes to Zion and draws the nations, but only those who respond become its bearers."
      }
    ],
    "37": [
      {
        "type": "allusion",
        "target": "Num 14:11",
        "note": "The LORD says to Moses: 'How long will these people treat me with contempt? How long will they refuse to believe in me, in spite of all the signs I have performed among them?' The pattern of unbelief in the face of signs is the wilderness pattern, now reprised at Jerusalem: signs multiplied, faith absent."
      }
    ],
    "38": [
      {
        "type": "fulfillment",
        "target": "Isa 53:1",
        "note": "John cites Isa 53:1 with explicit fulfillment formula (hina ho logos Ēsaïou plērōthē): 'Lord, who has believed our message and to whom has the arm of the LORD been revealed?' The report of the Servant goes unbelieved — the verse, spoken of the rejected Servant, is fulfilled in the rejection of Jesus."
      }
    ],
    "39": [
      {
        "type": "fulfillment",
        "target": "Isa 6:9-10",
        "note": "John introduces Isa 6:9-10 as the explanation for the impossibility of belief — not merely the prediction of unbelief but its cause. The divine hardening of Isaiah's commission is active in John's narrative: 'they could not believe because Isaiah says elsewhere...' This is a fulfillment in the strongest sense: the same judicial blinding Isaiah was sent to enact is at work."
      }
    ],
    "40": [
      {
        "type": "quote",
        "target": "Isa 6:10",
        "note": "John quotes Isa 6:10 directly: 'He has blinded their eyes and hardened their hearts, so they can neither see with their eyes nor understand with their hearts, nor turn — and I would heal them.' The Isaiah commission to preach to the spiritually unperceptive is applied to the response to Jesus' ministry. Notably John renders this as God's act (third-person: 'He has blinded'), where the LXX has the people's own choosing."
      }
    ],
    "41": [
      {
        "type": "fulfillment",
        "target": "Isa 6:1-3",
        "note": "John makes an extraordinary claim: when Isaiah saw 'the Lord seated on a throne, high and exalted... and the whole earth is full of his glory' (Isa 6:1-3), he saw Jesus' glory and spoke about him. The vision that commissioned Isaiah to preach to the unperceptive is identified as a pre-incarnate vision of the Son. This is the interpretive key to the whole Isa 6 citation above."
      }
    ],
    "42": [
      {
        "type": "theme",
        "target": "Isa 51:7",
        "note": "'Do not fear the reproach of mere mortals or be terrified by their insults.' The rulers who believe in secret, fearing expulsion from the synagogue, exemplify precisely the failure Isaiah's servant-people were warned against — fearing human reproach more than the LORD's approval. The synagogue ban is the social threat that overrides their better judgment."
      }
    ],
    "43": [
      {
        "type": "allusion",
        "target": "Ps 118:8-9",
        "note": "'It is better to take refuge in the LORD than to trust in humans; it is better to take refuge in the LORD than to trust in princes.' The rulers prefer human praise (doxa anthrōpōn) to divine praise (doxa tou theou) — an inversion of the Psalm's wisdom. The Psalm of the triumphal entry is used again, this time as the standard that the secret believers fail to meet."
      },
      {
        "type": "allusion",
        "target": "Prov 29:25",
        "note": "'Fear of man will prove to be a snare, but whoever trusts in the LORD is kept safe.' The crowd-pleasers of v. 43 are caught in the precise snare Proverbs names — their fear of human judgment (the Pharisees, the synagogue ban) overrides their recognition of Jesus."
      }
    ],
    "44": [
      {
        "type": "allusion",
        "target": "Deut 18:18-19",
        "note": "Moses promises: 'I will put my words in his mouth, and he will tell them everything I command him. I myself will call to account anyone who does not listen to my words.' Belief in Jesus is inseparable from belief in the Father who sent him — which is exactly the shaliach logic of Deut 18: the prophet speaks the Father's words; to receive the prophet is to receive the sender."
      }
    ],
    "45": [
      {
        "type": "theme",
        "target": "Exod 33:18-23",
        "note": "Moses asks to see God's glory and is told no one can see God's face and live. John 14:9 will say explicitly: 'Anyone who has seen me has seen the Father.' The claim in v. 45 that seeing Jesus is seeing the Father is the answer to Moses' unfulfilled request — the face of God is now visible in the face of the Son."
      }
    ],
    "46": [
      {
        "type": "allusion",
        "target": "Isa 49:6",
        "note": "'I will also make you a light for the Gentiles, that my salvation may reach to the ends of the earth.' Jesus identifies himself as the light who has come into the world — the servant whose mission Isa 49 describes. The coming of the Greeks in v. 20 triggered the announcement; here the light claims its own identity directly."
      },
      {
        "type": "allusion",
        "target": "Gen 1:3",
        "note": "'Let there be light.' The prologue of John (1:4-5) has already established the connection between the creative Word and the light. Jesus' 'I have come into the world as a light' is the first-person claim to be the new-creation light — not merely an analogy but the enacted reality of what God spoke at the beginning."
      }
    ],
    "47": [
      {
        "type": "allusion",
        "target": "Isa 61:1-2",
        "note": "'The Spirit of the Sovereign LORD is on me... to proclaim the year of the LORD's favor.' Isaiah's anointed one comes to save; the mention of 'the day of vengeance of our God' is held back in Luke 4:19. Jesus similarly distinguishes: he did not come to judge but to save — the judgment is real but belongs to a later moment."
      }
    ],
    "48": [
      {
        "type": "allusion",
        "target": "Deut 18:19",
        "note": "'I myself will call to account anyone who does not listen to my words that the prophet speaks in my name.' Jesus' word will judge at the last day — precisely the mechanism Deut 18 established for prophetic accountability. The words of God's prophet do not return void; they remain as witness and as judge."
      },
      {
        "type": "allusion",
        "target": "Dan 12:2",
        "note": "'Multitudes who sleep in the dust of the earth will awake: some to everlasting life, others to shame and everlasting contempt.' The 'last day' (eschate hēmera) judgment Jesus references draws on the Danielic vision of final resurrection-judgment — the same last day that determines the verdict."
      }
    ],
    "49": [
      {
        "type": "allusion",
        "target": "Jer 1:7-9",
        "note": "God says to Jeremiah: 'Do not say, I am too young. You must go to everyone I send you to and say whatever I command you.' He then touches Jeremiah's mouth: 'I have put my words in your mouth.' Jesus presents himself as the ultimate fulfillment of this commissioning pattern — not a prophet to whom words are given but the Son who speaks only what the Father has commanded."
      }
    ],
    "50": [
      {
        "type": "allusion",
        "target": "Isa 55:11",
        "note": "'So is my word that goes out from my mouth: it will not return to me empty, but will accomplish what I desire and achieve the purpose for which I sent it.' Jesus closes his public teaching by anchoring his speech in the Father's command that leads to eternal life — the divine word that achieves its end, which Isa 55 declares is the nature of God's word."
      }
    ]
  },
  "13": {
    "1": [
      {
        "type": "allusion",
        "target": "Exod 12:11-14",
        "note": "The meal takes place just before the Passover — the same night the original Passover lamb was slaughtered and the blood applied. 'Having loved his own... he loved them to the end (eis telos)' describes the Passover logic: the lamb's death is the complete expression of God's covenant loyalty to those under the blood."
      },
      {
        "type": "theme",
        "target": "Ps 136:1-26",
        "note": "The great Hallel is built on the refrain 'his love (chesed) endures forever' — 26 times across 26 verses. Jesus' love 'to the end' is the New Covenant expression of the same unfailing covenant love that Ps 136 celebrates through exodus, wilderness, and inheritance. The Last Supper is the Passover Seder context; this refrain would have been in the room."
      }
    ],
    "2": [
      {
        "type": "allusion",
        "target": "Gen 3:1-5",
        "note": "The devil prompts Judas as the serpent prompted Eve — both cases involve an adversarial figure working through a willing human agent to undermine the covenant. The language of 'putting into the heart' (balling into Judas) echoes the serpent's approach: working from within, through the desires and calculations of the person."
      },
      {
        "type": "allusion",
        "target": "Job 1:6-12",
        "note": "In Job the adversary (hassatan) appears before God and gains permission to act against Job. In John 13 the devil acts against Judas, a member of Jesus' inner circle. The pattern of satanic agency within the covenant community — the testing of the faithful from within — is the Job framework applied to the Passion narrative."
      }
    ],
    "3": [
      {
        "type": "fulfillment",
        "target": "Ps 110:1",
        "note": "'The LORD says to my lord: Sit at my right hand until I make your enemies a footstool for your feet.' Jesus' knowledge that 'the Father had put all things under his power' is the realized content of Ps 110:1 — not a future promise but a present reality informing his actions. His sovereign act of foot-washing flows from this authority, not despite it."
      },
      {
        "type": "allusion",
        "target": "Dan 7:14",
        "note": "The Son of Man was 'given authority, glory and sovereign power; all nations and peoples of every language worshiped him.' John's statement that the Father had given all things into Jesus' hands (v. 3) is the same conferral of universal authority Daniel envisioned — the sovereign who washes feet is the one to whom all authority belongs."
      }
    ],
    "4": [
      {
        "type": "allusion",
        "target": "Isa 53:12",
        "note": "The Servant 'poured out his life unto death, and was numbered with the transgressors.' Jesus removes his outer garment and wraps himself in the slave's towel — the voluntary divestiture of status before the ultimate divestiture on the cross. The physical act anticipates the kenotic logic of the Servant's self-emptying."
      },
      {
        "type": "allusion",
        "target": "Exod 29:4",
        "note": "Aaron and his sons were washed with water at the entrance to the tent of meeting as part of their priestly ordination. Jesus' washing of his disciples' feet enacts a priestly consecration in reverse — the high priest washes those he is presenting to God, as the one who makes his disciples a kingdom of priests (cf. Rev 1:6)."
      }
    ],
    "5": [
      {
        "type": "theme",
        "target": "Lev 8:6",
        "note": "Moses washed Aaron and his sons with water at their ordination as priests. Jesus' washing of the disciples' feet draws on the same priestly-purification register — but inverts the hierarchy: the greater (the Son of God) serves the lesser (the disciples), making priestly service the pattern of authority in the new covenant community."
      }
    ],
    "6": [
      {
        "type": "allusion",
        "target": "John 1:27",
        "note": "John the Baptist said he was 'not worthy to untie the strap of his sandal.' Foot-care was the task of the lowest household slave. Peter's protest ('Lord, are you going to wash my feet?') registers the same radical incongruity — but now it is not the Baptist declining the slave's role; it is the Lord performing it."
      }
    ],
    "7": [
      {
        "type": "theme",
        "target": "Isa 55:8-9",
        "note": "'My thoughts are not your thoughts, neither are your ways my ways,' declares the LORD. Peter cannot grasp what Jesus is doing — 'You do not realize now what I am doing, but later you will understand' — because divine action consistently exceeds the frame of human expectation. The pattern of retrospective comprehension runs through the prophets."
      }
    ],
    "8": [
      {
        "type": "allusion",
        "target": "Lev 16:30",
        "note": "On the Day of Atonement the high priest makes atonement for Israel: 'before the LORD you will be clean from all your sins.' Jesus' statement — 'Unless I wash you, you have no part with me' — establishes washing as the prerequisite for belonging, as the Yom Kippur cleansing was the prerequisite for the people's standing before God."
      },
      {
        "type": "allusion",
        "target": "Ps 51:7",
        "note": "'Wash me, and I will be whiter than snow.' David's penitential cry makes cleansing the condition for restored fellowship with God. Jesus' washing of Peter enacts what the psalm requests — not self-cleansing but cleansing from the one who can provide it."
      }
    ],
    "9": [
      {
        "type": "allusion",
        "target": "Isa 1:16",
        "note": "'Wash and make yourselves clean; take your evil deeds out of my sight.' Peter's request for full washing (hands and head as well) goes further than what is needed, just as Isaiah's audience needed to understand that God's call to washing was not about more water but about a different kind of cleansing altogether."
      }
    ],
    "10": [
      {
        "type": "theme",
        "target": "Lev 11:24-25",
        "note": "The Levitical distinction between a person who has become fully unclean (requiring full washing) and one who has touched something unclean (requiring only partial washing) underlies the teaching here. Jesus uses the purity framework of the Law to explain the distinction between being entirely cleansed (already clean, 15:3) and requiring the ongoing washing of community life."
      }
    ],
    "11": [
      {
        "type": "allusion",
        "target": "Ps 41:9",
        "note": "Jesus knows who will betray him — the one at the table who is 'not clean' (v. 10-11) — and this foreknowledge is part of the covenant logic: the Psalm ('he who shared my bread has lifted his heel against me') is being enacted with full awareness. The betrayal is known before it happens; it is absorbed into, not outside of, divine sovereignty."
      }
    ],
    "12": [
      {
        "type": "theme",
        "target": "Isa 52:13",
        "note": "The Servant 'will act wisely' (yaskil) — he acts with understanding. When Jesus resumes his garments and returns to his place, the question 'Do you understand what I have done for you?' mirrors the Servant's wisdom: his act is not arbitrary but laden with meaning that must be grasped, not merely observed."
      }
    ],
    "13": [
      {
        "type": "allusion",
        "target": "Mal 1:6",
        "note": "'A son honors his father, and a slave his master. If I am a father, where is the honor due me? If I am a master, where is the respect due me? says the LORD Almighty.' Jesus affirms that calling him Teacher and Lord is correct — what Malachi saw as owed to God (honor and respect), the disciples rightly give to Jesus."
      }
    ],
    "14": [
      {
        "type": "theme",
        "target": "Mic 6:8",
        "note": "'He has shown you, O mortal, what is good. And what does the LORD require of you? To act justly and to love mercy and to walk humbly with your God.' Humble service as the covenant obligation is the substance of the prophetic ethic; Jesus' command to wash one another's feet is not a new invention but the covenant ethic embodied and mandated by the one who embodies it."
      }
    ],
    "15": [
      {
        "type": "shadow",
        "target": "Deut 18:15-18",
        "note": "Moses set an example: 'The LORD your God will raise up for you a prophet like me from among you... you must listen to him.' Jesus' 'I have set you an example that you should do as I have done' is the definitive prophetic example — but unlike Moses, this prophet does not merely model obedience to God's commands; he embodies and commands the love that fulfills them all."
      }
    ],
    "16": [
      {
        "type": "allusion",
        "target": "Mal 3:1",
        "note": "'See, I will send my messenger, who will prepare the way before me.' The one sent is less than the one who sent; the messenger is not greater than the Lord. Jesus' principle — 'no servant is greater than his master, nor a messenger (apostolos) greater than the one who sent him' — invokes the shaliach principle that underlies Malachi's messenger theology."
      }
    ],
    "17": [
      {
        "type": "allusion",
        "target": "Ps 1:1-3",
        "note": "'Blessed (ashrei) is the one who does not walk in step with the wicked... whose delight is in the law of the LORD.' Jesus pronounces blessing on those who not merely know but do — the same wisdom-psalm logic that the blessed person is the one whose knowledge issues in action, not merely in understanding."
      },
      {
        "type": "allusion",
        "target": "Deut 28:1-2",
        "note": "'If you fully obey the LORD your God and carefully follow all his commands... all these blessings will come on you.' The covenant blessing structure conditions blessing on doing, not only knowing. Jesus' 'you will be blessed if you do them' is the same structure applied to the new-covenant community."
      }
    ],
    "18": [
      {
        "type": "fulfillment",
        "target": "Ps 41:9",
        "note": "Jesus cites Ps 41:9 with explicit fulfillment formula (hina hē graphē plērōthē): 'He who shared my bread has turned against me' (literally 'lifted his heel against me'). Sharing bread was the highest act of hospitality, creating a covenant bond; betrayal at the table was therefore the deepest treachery. The psalm's description of David's betrayal by a companion is fulfilled in Judas at the last meal."
      }
    ],
    "19": [
      {
        "type": "allusion",
        "target": "Isa 48:3-5",
        "note": "'I foretold the former things long ago, my mouth announced them and I made them known... before they happened I announced them to you so that you could not say, My images brought them about.' Jesus tells the disciples about Judas' betrayal before it happens so that when it does, they will recognize him as the I AM (ego eimi) — the divine name of Exod 3:14, claimed here in the context of prophetic foreknowledge."
      }
    ],
    "20": [
      {
        "type": "allusion",
        "target": "Deut 18:18-20",
        "note": "The prophet speaks God's words; receiving the prophet is receiving God. Jesus' statement — 'whoever accepts anyone I send accepts me; and whoever accepts me accepts the one who sent me' — is the apostolic extension of the prophet-sender chain Deut 18 establishes. The chain of reception (disciple → Jesus → Father) mirrors the chain of commission (Father → Jesus → disciples)."
      }
    ],
    "21": [
      {
        "type": "allusion",
        "target": "Ps 55:12-14",
        "note": "The psalmist laments: 'If an enemy were insulting me, I could endure it... but it is you, a man like myself, my companion, my close friend, with whom I once enjoyed sweet fellowship at the house of God.' Jesus is 'troubled in spirit' (etarachthē tō pneumati) — the same grief the psalm voices. The companion's betrayal is not a failure of divine planning but a depth of human evil that genuinely troubles the Son of Man."
      }
    ],
    "22": [
      {
        "type": "theme",
        "target": "Isa 6:9-10",
        "note": "The disciples 'look at one another, at a loss' — they cannot see what is plainly in front of them. The motif of incomprehension among the inner circle mirrors the broader pattern of Isaiah 6: even those closest to the word of God struggle to grasp what it says. The disciples' confusion is not deficiency but the nature of revelation that can only be fully understood after the events."
      }
    ],
    "23": [
      {
        "type": "allusion",
        "target": "Deut 33:12",
        "note": "The tribe of Benjamin is called 'the beloved of the LORD... [who] rests between his shoulders.' The Beloved Disciple reclining (literally: lying on the bosom) of Jesus is physically and spiritually in the same position — the one specially loved, resting in the closest proximity to the one who loves. John the disciple is never named, only defined by this intimacy."
      }
    ],
    "24": [
      {
        "type": "theme",
        "target": "Exod 33:11",
        "note": "'The LORD would speak to Moses face to face, as one speaks to a friend.' The Beloved Disciple has access to Jesus that Peter must request through intermediary — a mediated intimacy echoing the OT distinction between those who approach God directly and those who need a representative. The Beloved Disciple's role prefigures a different kind of access."
      }
    ],
    "25": [
      {
        "type": "theme",
        "target": "Song 1:2-4",
        "note": "The beloved of the Song leans against the king, desires to be drawn near, rests in his presence. The Beloved Disciple 'leaning back against Jesus' and asking his question is the image of intimate proximity — the one who is nearest is best positioned to receive revelation. Song's imagery of covenantal intimacy between the beloved and the king provides the register."
      }
    ],
    "26": [
      {
        "type": "allusion",
        "target": "Ps 41:9",
        "note": "The bread dipped in the dish and given to Judas is the act that simultaneously identifies the betrayer and enacts the psalm: 'he who shared my bread has lifted his heel against me.' The specific act of bread-sharing Jesus uses to reveal the betrayer is taken from the very text that predicted it — a fulfillment performed in the gesture of fulfillment."
      }
    ],
    "27": [
      {
        "type": "allusion",
        "target": "1 Chr 21:1",
        "note": "'Satan rose up against Israel and incited David to take a census of Israel.' Satanic entry and incitement to a destructive act against God's people is the pattern 1 Chronicles 21 describes. Here Satan enters Judas after the bread — the adversary uses the sacred act of table fellowship as the threshold for his entry."
      },
      {
        "type": "allusion",
        "target": "Gen 3:15",
        "note": "'You will strike his heel.' Jesus tells Judas: 'What you are about to do, do quickly' — he does not prevent the heel-strike but absorbs it into the divine purpose. The protoevangelium pattern: the wound is permitted because the head-crushing follows from it."
      }
    ],
    "28": [
      {
        "type": "theme",
        "target": "Isa 6:9-10",
        "note": "No one at the table understands what Jesus says to Judas. The disciples' incomprehension in the presence of the Lord echoes the hardening Isaiah was sent to announce — even those at the table with Jesus cannot see the meaning of what is happening. Understanding requires the Spirit and the resurrection (16:12-14)."
      }
    ],
    "29": [
      {
        "type": "allusion",
        "target": "Deut 15:7-11",
        "note": "The disciples guess that Jesus is sending Judas to give to the poor — an entirely plausible inference given that Deut 15:11 commands openhanded generosity to the poor, and this would be expected at Passover. The obliviousness of the disciples is highlighted by the contrast: what they imagine is a righteous errand is actually the beginning of betrayal."
      }
    ],
    "30": [
      {
        "type": "allusion",
        "target": "Gen 1:4-5",
        "note": "God separated the light from the darkness and called the darkness 'night.' 'And it was night' is John's most compressed theological statement — Judas steps out of the light (Jesus) into the darkness, and the darkness claims him. The creation framework of John 1 (light vs. darkness) is the interpretive grid for this closing phrase."
      },
      {
        "type": "allusion",
        "target": "John 1:5",
        "note": "'The light shines in the darkness, and the darkness has not overcome it.' By the time Judas goes out into the night, the darkness appears to be winning — it swallows one of the twelve. But the prologue's declaration stands: the darkness has not overcome the light, even when the darkness walks out the door with a mission."
      }
    ],
    "31": [
      {
        "type": "allusion",
        "target": "Dan 7:13-14",
        "note": "The Son of Man is glorified — this is the moment Daniel foresaw: 'He was given authority, glory and sovereign power.' But in John the glorification comes through the cross, not around it. The path to the throne room of Dan 7 runs through Golgotha; the mutual glorification of Father and Son occurs in the act of the greatest human humiliation."
      }
    ],
    "32": [
      {
        "type": "allusion",
        "target": "Isa 52:13",
        "note": "'My servant will act wisely; he will be raised and lifted up and highly exalted.' The swift glorification — 'will glorify him at once' — is the divine response to the Servant's willingness to go to the cross without delay. The exaltation follows the humiliation not at a measured distance but immediately, because the cross is simultaneously the humiliation and the glorification."
      }
    ],
    "33": [
      {
        "type": "allusion",
        "target": "John 7:34",
        "note": "Jesus said the same words to the Jewish authorities: 'Where I am going, you cannot come.' Now the disciples hear them. The disciples are placed in the same position the Pharisees were in — unable to follow Jesus into death and resurrection by their own power. The difference is that the disciples will follow 'later' (v. 36); the authorities will not."
      }
    ],
    "34": [
      {
        "type": "shadow",
        "target": "Lev 19:18",
        "note": "The command to 'love your neighbor as yourself' is the Old Covenant form; the new command has the same content but a new standard: 'As I have loved you.' This is why Jesus calls it 'new' — not because love of neighbor is new, but because the measure of love has been reset by the cross. The shadow of Lev 19:18 is now filled with the substance of cruciform love."
      },
      {
        "type": "theme",
        "target": "Deut 6:5",
        "note": "The Shema calls Israel to love God with all heart, soul, and strength. The new command recalibrates the love ethic: the community is now defined by love for one another, not merely love upward to God — because love for one another is now the outworking of the love that has come down (13:1). The vertical love of Deut 6:5 generates the horizontal love of 13:34."
      }
    ],
    "35": [
      {
        "type": "allusion",
        "target": "Isa 43:10-12",
        "note": "'You are my witnesses... and my servant whom I have chosen, so that you may know and believe me.' The disciples' love for one another is their apostolic witness — not merely a private virtue but the public sign by which the nations know who Jesus is and whose they are. The witness-community of Isa 43 becomes the love-community of John 13."
      }
    ],
    "36": [
      {
        "type": "allusion",
        "target": "Deut 31:1-3",
        "note": "Moses tells Israel: 'I am no longer able to lead you... The LORD your God himself will cross over ahead of you.' The departure of Moses and the succession to Joshua parallel the departure of Jesus and the succession to the Spirit (chs. 14-16). Peter's inability to follow now but promise of following later echoes the generation that cannot enter the land until the right time."
      }
    ],
    "37": [
      {
        "type": "allusion",
        "target": "Ruth 1:16-17",
        "note": "Ruth's loyalty oath — 'Where you go I will go, and where you stay I will stay... Where you die I will die, and there I will be buried' — is the OT model of covenant loyalty that will not be separated from the beloved. Peter's 'I will lay down my life for you' is sincere and modeled on this kind of covenantal pledge; his subsequent failure reveals the difference between declared loyalty and cruciform loyalty."
      }
    ],
    "38": [
      {
        "type": "theme",
        "target": "Isa 40:11",
        "note": "The shepherd 'gently leads those that have young' — the flock includes the weak and failing, not only the strong. Peter's three-fold denial and three-fold restoration (John 21:15-17) form the complete arc: the shepherd does not abandon the sheep who stumbles but pursues and restores. The rooster's crow is not the end of Peter's story in the Gospel's design."
      }
    ]
  }
}


def main():
    existing = load_echo('john')
    merge_echo(existing, JOHN_ECHOES)
    save_echo('john', existing)
    print('John 12–13 echoes written.')

if __name__ == '__main__':
    main()
