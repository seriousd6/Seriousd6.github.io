"""
MKT Echo Layer — John chapter 5
Run: python3 scripts/zc-echo-john-5-5.py

Source data used:
- data/interlinear/john.json (Strongs tokens, ch 5)
- data/translation/draft/mediating/john.json (MKT text)
- data/translation/glossary-greek.json (G2222 ζωή dispute_level 2; G3056 λόγος dispute_level 3)
- data/parallels/john.json (empty for ch 5 — nothing to absorb)
- data/echoes/john.json (pre-existing entries for vv 17, 22, 23, 28, 29, 35, 39, 46 — merge preserves these)
- data/commentary/ellicott/john.json, data/commentary/jfb/john.json

Key decisions:
- v4: Textually suspect (omitted in P66, P75, ‭א, B); echo notes the tradition without asserting
  canonical authority. Thematic echo to Ezek 47:8-9 (healing waters from temple) preferred.
- v5: The 38-year parallel to Deut 2:14 (Israel's wilderness wandering) is noted as contested —
  the verbal parallel is notable but scholars dispute intentionality; classified as 'allusion' with caveat.
- v21: Deut 32:39 chosen as primary echo (YHWH's exclusive claim to give/take life, now claimed by Son)
  over the Elijah/Elisha precedents (1 Kgs 17, 2 Kgs 4), which are types of prophetic life-giving,
  not of divine authority.
- v25: Ezek 37 (valley of dry bones) is the primary OT antecedent for the dead hearing a voice and living.
- v26: Exod 3:14 chosen for the 'life in himself' / self-subsistent being claim.
- vv 28-29, 22-23, 17, 35, 39, 46: Already present in echoes file; merge_echo will deduplicate and
  may add supplementary entries only.
- NT-internal references (Heb 3:5-6 for v47) avoided — OT antecedents only in this layer.
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
  "5": {
    "1": [
      {
        "type": "shadow",
        "target": "Exod 23:17",
        "note": "Three times a year all Israelite males were to appear before the LORD in Jerusalem. Jesus' pilgrimage to the feast follows the Mosaic festival calendar, situating his ministry inside Israel's covenant rhythm — the one the festivals anticipated is now present at them."
      }
    ],
    "2": [
      {
        "type": "allusion",
        "target": "Neh 3:1",
        "note": "The Sheep Gate is the first structure rebuilt in Nehemiah's restoration of Jerusalem — rebuilt by the priests, and associated with the temple's sacrificial system. The pool by that gate becomes the site where Jesus heals; the place of priestly restoration becomes the place of messianic healing."
      },
      {
        "type": "theme",
        "target": "Ezek 47:8-9",
        "note": "Ezekiel's vision of water flowing from the temple — 'wherever the river flows, there will be large numbers of fish... and everything will live where the river goes.' The pool at Jerusalem's temple precinct sits as a foil: the still water heals only one at a time; the living water from the true temple gives life to all."
      }
    ],
    "3": [
      {
        "type": "allusion",
        "target": "Isa 35:5-6",
        "note": "Isaiah's messianic promise: 'Then will the eyes of the blind be opened and the ears of the deaf unstopped. Then will the lame leap like a deer.' The crowd of blind, lame, and paralyzed at Bethesda is the exact population Isaiah named; their presence at this pool frames the scene as a stage for the anticipated age of healing."
      }
    ],
    "4": [
      {
        "type": "theme",
        "target": "Ezek 47:8-9",
        "note": "The tradition behind this verse — absent from the earliest manuscripts — imagines angelic agitation of water producing healing for the first entrant. Whether original or a scribal gloss explaining local practice, the theological pattern it assumes is the OT one: God acts through water and messenger to heal. Ezekiel's temple-water vision provides the canonical framework within which this popular expectation makes sense."
      }
    ],
    "5": [
      {
        "type": "allusion",
        "target": "Deut 2:14",
        "note": "Thirty-eight years is precisely the span Israel wandered from Kadesh Barnea to crossing the Wadi Zered — the generation condemned to die in the wilderness. The verbal parallel (38 years, helplessness, inability to move forward) is notable, though scholars debate whether the Evangelist intends the echo. If deliberate, the invalid embodies Israel's wilderness paralysis; Jesus' word achieves in a moment what Israel's 38 years could not."
      }
    ],
    "6": [
      {
        "type": "theme",
        "target": "Ps 107:17-20",
        "note": "Psalm 107 describes those 'afflicted because of their iniquities' whom God rescues: 'He sent out his word and healed them; he rescued them from the grave.' Jesus sees the man, knows his long condition, and heals by word alone — the Psalmist's pattern of God's word going out to the helpless is enacted in a specific encounter."
      }
    ],
    "7": [
      {
        "type": "theme",
        "target": "Ps 40:1-2",
        "note": "The Psalmist waited in a 'slimy pit, in the muddy clay,' and the LORD lifted him out and set his feet on solid ground. The invalid's long wait — no one to help, always beaten to the water — mirrors the Psalmist's helpless waiting; the deliverance comes not from human aid but from divine initiative."
      }
    ],
    "8": [
      {
        "type": "allusion",
        "target": "Isa 35:6",
        "note": "The command 'Get up, pick up your mat and walk' immediately fulfills the messianic sign: the lame leaping. Isaiah's promise is not evoked by quotation but by event — the pattern of prophecy actualized in a specific word of command."
      }
    ],
    "9": [
      {
        "type": "theme",
        "target": "Gen 2:3",
        "note": "The Sabbath as a day God blessed and made holy was the boundary the healing crossed. The tension the narrator signals — 'the day on which this took place was a Sabbath' — is not incidental; it frames the rest of the chapter's dispute. The Creator-God who rested on the seventh day is now present and working through his Son on that same day."
      }
    ],
    "10": [
      {
        "type": "allusion",
        "target": "Jer 17:21-22",
        "note": "Jeremiah's warning is specific: 'Be careful not to carry a load on the Sabbath day or bring it through the gates of Jerusalem.' This is the exact provision the leaders invoke when they see the man carrying his mat. Jesus' healing deliberately triggers the Jeremiah Sabbath-load prohibition, initiating a confrontation about who defines Sabbath observance."
      }
    ],
    "11": [
      {
        "type": "theme",
        "target": "Isa 43:10",
        "note": "'You are my witnesses,' declares the LORD. The healed man becomes a witness, transmitting Jesus' command. His testimony is unlearned and direct — 'the man who made me well said to me' — exactly the pattern of witness: reporting what was received, not inventing."
      }
    ],
    "12": [
      {
        "type": "theme",
        "target": "Isa 53:2",
        "note": "The leaders' question — 'Who is this fellow?' — reflects the Servant's obscurity: 'He had no beauty or majesty to attract us to him, nothing in his appearance that we should desire him.' The one who healed goes unrecognized not from absence but from hiddenness; the Servant pattern of anonymous power is present in the crowd."
      }
    ],
    "13": [
      {
        "type": "theme",
        "target": "Isa 45:15",
        "note": "'Truly you are a God who hides himself, O God and Savior of Israel.' Jesus slips away into the crowd immediately after healing — a pattern of withdrawal that runs through John. The God who saves is also the God who conceals himself from those who do not seek him."
      }
    ],
    "14": [
      {
        "type": "allusion",
        "target": "Ps 103:3",
        "note": "Psalm 103 pairs forgiveness and healing in a single divine act: 'who forgives all your sins and heals all your diseases.' Jesus finds the man in the temple — the appropriate place for thanksgiving — and links his healed condition to a warning against sin. The Psalm's pairing is present: physical restoration and moral responsibility belong together."
      }
    ],
    "15": [
      {
        "type": "theme",
        "target": "Ps 40:9-10",
        "note": "'I proclaim your saving acts in the great assembly; I do not seal my lips, LORD.' The man goes and tells the Jewish leaders that Jesus made him well — a report that will bring persecution to the one who healed him. He fulfills the pattern of the witness who speaks, though what follows is confrontation rather than praise."
      }
    ],
    "16": [
      {
        "type": "allusion",
        "target": "Jer 26:11",
        "note": "The priests and prophets demanded Jeremiah's death for speaking in God's name: 'This man should be sentenced to death because he has prophesied against this city.' The structural pattern recurs — religious leaders persecuting the one who acts under divine commission — and it escalates in the same direction: from persecution toward death."
      }
    ],
    "18": [
      {
        "type": "allusion",
        "target": "Lev 24:16",
        "note": "'Anyone who blasphemes the name of the LORD is to be put to death.' The charge that Jesus 'was calling God his own Father' is a blasphemy charge — claiming divine sonship in the Johannine register is claiming equality with God. The legal mechanism the leaders are already reaching for is Lev 24's death penalty for blasphemy."
      },
      {
        "type": "allusion",
        "target": "Ps 2:7",
        "note": "'You are my Son; today I have begotten you.' The divine sonship declaration from the royal enthronement psalm is precisely the claim Jesus is being prosecuted for — and the psalm that frames it as the anointed king's prerogative, not blasphemy."
      }
    ],
    "19": [
      {
        "type": "theme",
        "target": "Amos 3:7",
        "note": "'Surely the Sovereign LORD does nothing without revealing his plan to his servants the prophets.' Jesus' claim — the Son does only what he sees the Father doing — draws on the OT prophetic model: the true spokesman for God acts only on what God discloses. But where prophets received partial revelation, the Son sees everything the Father does."
      }
    ],
    "20": [
      {
        "type": "allusion",
        "target": "Prov 8:30",
        "note": "Wisdom declares: 'I was constantly at his side. I was filled with delight day after day, rejoicing always in his presence.' The Father's love for the Son and his showing him all he does mirrors the Wisdom tradition's intimacy between divine Wisdom and God in creation. The Johannine Son embodies what Proverbs personified as Wisdom."
      }
    ],
    "21": [
      {
        "type": "allusion",
        "target": "Deut 32:39",
        "note": "The Song of Moses: 'I put to death and I bring to life... and no one can deliver out of my hand.' This is YHWH's exclusive, unshared prerogative. Jesus claims it for the Son — 'the Son gives life to whom he is pleased to give it' — a direct appropriation of the divine monopoly on life and death that the Mosaic song reserves for God alone."
      }
    ],
    "24": [
      {
        "type": "allusion",
        "target": "Hab 2:4",
        "note": "'The righteous person will live by his faithfulness.' The faith-life link that Paul deploys for justification (Rom 1:17) Jesus states as a present reality: the one who hears and believes 'has eternal life' now, not merely as a future hope. The Habakkuk axiom is radicalized — faith in the Son transfers the believer from death to life immediately."
      }
    ],
    "25": [
      {
        "type": "allusion",
        "target": "Ezek 37:4-10",
        "note": "God commands Ezekiel: 'Prophesy to these bones, say to them... I will make breath enter you and you will come to life.' Dry bones hear the prophetic word and live. Jesus' declaration that 'the dead will hear the voice of the Son of God and those who hear will live' enacts the Ezekiel pattern — but the voice is no longer a prophet relaying God's word; it is the Son speaking with divine authority directly."
      }
    ],
    "26": [
      {
        "type": "allusion",
        "target": "Exod 3:14",
        "note": "God's self-disclosure as 'I AM WHO I AM' — the one whose being is from himself alone — is the OT basis for the claim that the Father 'has life in himself.' That the Son also has life in himself is a claim to participate in the divine mode of self-subsistent existence, not merely to receive life as creatures do."
      }
    ],
    "27": [
      {
        "type": "fulfillment",
        "target": "Dan 7:13-14",
        "note": "The Ancient of Days gives the one like a son of man 'authority, glory and sovereign power.' Jesus states this as the ground of his judicial authority: 'he has given him authority to judge because he is the Son of Man.' The Danielic investiture is not merely parallel — Jesus explicitly invokes the title 'Son of Man' as the source of the delegated authority to judge."
      }
    ],
    "30": [
      {
        "type": "allusion",
        "target": "Deut 1:17",
        "note": "Moses charged Israel's judges: 'Do not show partiality in judging; hear both small and great alike. Do not be afraid of anyone, for judgment belongs to God.' Jesus' claim — 'my judgment is just, for I seek not to please myself but him who sent me' — fulfills the Deuteronomic ideal of judgment that is entirely God's and entirely unbiased, impossible for human judges but realized in the Son."
      }
    ],
    "31": [
      {
        "type": "allusion",
        "target": "Deut 19:15",
        "note": "'One witness is not enough to convict anyone accused of any crime or offense they may have committed. A matter must be established by the testimony of two or three witnesses.' Jesus acknowledges the Mosaic evidentiary standard directly — his self-testimony alone would be legally insufficient — and proceeds to marshal four independent witnesses. The legal framework is Deuteronomic."
      }
    ],
    "32": [
      {
        "type": "theme",
        "target": "Isa 43:10",
        "note": "'You are my witnesses,' declares the LORD, 'and my servant whom I have chosen.' The 'another who testifies' is initially the Father, though in context John the Baptist has just been named. The witness structure in John 5 mirrors the OT pattern in which God provides witnesses to establish truth — here reconstituted around the Son."
      }
    ],
    "33": [
      {
        "type": "fulfillment",
        "target": "Mal 3:1",
        "note": "'I will send my messenger, who will prepare the way before me.' John the Baptist's testimony to Jesus fulfills the Malachi messenger prophecy — Jesus has already identified John in this role (Matt 11:10), and here acknowledges it: 'You have sent to John and he has testified to the truth.' The sent messenger has borne witness to the one who sends him."
      }
    ],
    "34": [
      {
        "type": "theme",
        "target": "Isa 45:22",
        "note": "'Turn to me and be saved, all you ends of the earth.' Jesus accepts John's testimony not for his own validation but so that his audience 'may be saved' — the salvific orientation of divine witness. The point of the testimony-chain is not legal self-justification but the rescue of the hearers."
      }
    ],
    "36": [
      {
        "type": "allusion",
        "target": "Isa 61:1-2",
        "note": "The Spirit-anointed servant's works — good news to the poor, freedom for captives, recovery of sight, release of the oppressed — constitute his testimony. Jesus points to 'the works the Father has given me to finish' as weightier testimony than John's; the works are the enacted messianic agenda that Isaiah described."
      }
    ],
    "37": [
      {
        "type": "allusion",
        "target": "Deut 4:12",
        "note": "At Sinai, Israel 'heard the sound of words but saw no form; there was only a voice.' Jesus tells the same audience's descendants: 'You have never heard his voice nor seen his form.' The irony is precise — Israel was constituted at Sinai by a voice they could not see, and now the Father's voice testifies to Jesus, but they remain as unable to perceive it as they were at Horeb."
      }
    ],
    "38": [
      {
        "type": "allusion",
        "target": "Jer 31:33",
        "note": "The new covenant promise: 'I will put my law in their minds and write it on their hearts.' The old covenant required Israel to internalize the law (Deut 6:6); the new covenant was to accomplish it. Jesus' accusation — 'his word does not dwell in you' — diagnoses their failure to achieve even the old covenant's interior appropriation, let alone the new covenant's transformation."
      }
    ],
    "40": [
      {
        "type": "allusion",
        "target": "Prov 8:35",
        "note": "Wisdom declares: 'For those who find me find life and receive favor from the LORD.' They search the Scriptures — which are Wisdom's testimony — but refuse to come to Jesus, who is Wisdom's fulfillment. They consult the menu but refuse the meal; the refusal is not ignorance but a willed rejection of the one to whom Wisdom pointed."
      }
    ],
    "41": [
      {
        "type": "theme",
        "target": "Isa 42:8",
        "note": "'I am the LORD; that is my name! I will not yield my glory to another or my praise to idols.' Jesus does not seek the glory that humans offer — consistent with the divine character that refuses to share glory with creatures. His indifference to human honor mirrors the divine refusal of competitor glory."
      }
    ],
    "42": [
      {
        "type": "allusion",
        "target": "Isa 29:13",
        "note": "'These people come near to me with their mouth and honor me with their lips, but their hearts are far from me.' Isaiah's indictment of formal religion without interior devotion is what Jesus diagnoses in his audience: external Torah-study without the love of God that the Torah commands. Isaiah named the pattern; Jesus identifies it in the specific audience before him."
      }
    ],
    "43": [
      {
        "type": "allusion",
        "target": "Ps 118:26",
        "note": "'Blessed is he who comes in the name of the LORD.' The royal entrance psalm anticipates a messianic figure coming in God's name; Jesus claims exactly this. The irony is that the crowd that shouted Ps 118:26 at the triumphal entry will be the same population that rejects the one it describes — and here, ahead of that moment, Jesus makes the rejection visible."
      }
    ],
    "44": [
      {
        "type": "allusion",
        "target": "Ps 115:1",
        "note": "'Not to us, LORD, not to us but to your name be the glory, because of your love and faithfulness.' The pursuit of honor from fellow humans — the social economy of the synagogue and Sanhedrin — is incompatible with seeking 'the glory that comes from the only God.' The Psalmist's doxology states the proper orientation; Jesus exposes its absence."
      }
    ],
    "45": [
      {
        "type": "allusion",
        "target": "Deut 31:19-22",
        "note": "God commanded Moses to write the covenant song 'as a witness for me against the Israelites.' Moses wrote the Torah not merely as instruction but as a witness that would testify against covenant-breakers. Jesus activates this function: Moses, whom they invoke as their defender, is in fact their covenant accuser — the Torah functions exactly as Deut 31 said it would."
      }
    ],
    "47": [
      {
        "type": "allusion",
        "target": "Isa 6:9-10",
        "note": "God's commission to Isaiah: 'Be ever hearing, but never understanding; be ever seeing, but never perceiving. Make the heart of this people calloused... lest they... turn and be healed.' Jesus' closing question — if they do not believe Moses' writings, how will they believe his words? — assumes this entrenched unbelief. Isaiah's hardening oracle describes the condition of those who have Moses but cannot receive him."
      }
    ]
  }
}


def main():
    existing = load_echo('john')
    merge_echo(existing, JOHN_ECHOES)
    save_echo('john', existing)
    print('John 5 echoes written.')

if __name__ == '__main__':
    main()
