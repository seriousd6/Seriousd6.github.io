"""
1-2 Kings — all four layers.
Key NT: Elijah/Elisha (type of John the Baptist/Jesus), temple dedication (1 Kgs 8),
        Naaman's healing (Luke 4 context), widow of Zarephath (Luke 4),
        Josiah's reform, exile and its theological meaning.
"""

import json, pathlib

ROOT = pathlib.Path(__file__).parent.parent

def load_echo(book):
    p = ROOT / 'data' / 'echoes' / f'{book}.json'
    return json.loads(p.read_text()) if p.exists() else {}

def save_echo(book, data):
    p = ROOT / 'data' / 'echoes' / f'{book}.json'
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=None))
    print(f'  wrote {p.relative_to(ROOT)}')

def load_comm(layer, book):
    p = ROOT / 'data' / 'commentary' / layer / f'{book}.json'
    return json.loads(p.read_text()) if p.exists() else {}

def save_comm(layer, book, data):
    p = ROOT / 'data' / 'commentary' / layer / f'{book}.json'
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=None))
    print(f'  wrote {p.relative_to(ROOT)}')

def merge_echo(existing, new_data):
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

def merge_comm(existing, new_data):
    for ch, verses in new_data.items():
        if ch not in existing:
            existing[ch] = {}
        for v, html in verses.items():
            if v not in existing[ch]:
                existing[ch][v] = html

KINGS1_ECHO = {
  "8": {
    "27": [
      {"type": "allusion", "target": "Acts 7:48-50", "note": "But will God indeed dwell on the earth? Behold, heaven and the highest heaven cannot contain you, how much less this house that I have built — Solomon's prayer at the temple dedication acknowledges divine transcendence; Stephen quotes Isa 66:1-2 to make the same point: the Most High does not dwell in temples made by human hands; both point toward the incarnation as the true dwelling of God among his people (John 1:14)"}
    ]
  },
  "17": {
    "1": [
      {"type": "allusion", "target": "Jas 5:17", "note": "Elijah was a man with a nature like ours, and he prayed fervently that it might not rain, and for three years and six months it did not rain on the earth — James cites Elijah's prayer as an example of effective righteous prayer; the three-and-a-half-year drought is applied typologically in Revelation (11:6) to the witnesses' power"}
    ],
    "8": [
      {"type": "fulfillment", "target": "Luke 4:25-26", "note": "In truth I tell you, there were many widows in Israel in the days of Elijah ... and Elijah was sent to none of them but only to Zarephath, a city of Sidon, to a woman who was a widow — Jesus cites the widow of Zarephath (1 Kgs 17:8-16) as an OT precedent for divine grace going to a Gentile; the Nazareth congregation's rejection of Jesus follows their rejection of this theological point"}
    ]
  },
  "19": {
    "10": [
      {"type": "allusion", "target": "Rom 11:2-4", "note": "I have been very jealous for YHWH the God of hosts. For the people of Israel have forsaken your covenant, thrown down your altars, and killed your prophets with the sword, and I, even I only, am left — Paul cites Elijah's complaint and YHWH's response (seven thousand who have not bowed to Baal) as proof that God has not rejected Israel; the remnant principle is the OT basis for Israel's partial hardening and the elect remnant within"}
    ]
  }
}

KINGS1_ORIGINAL = {
  "8": {
    "46": "<p><strong>ki yechetau lecha ki ein adam asher lo yecheta</strong>: 'For there is no one who does not sin' — Solomon's prayer at the temple dedication contains the OT's clearest statement of universal sinfulness (v. 46), which shapes the entire temple theology: the temple is not a reward for Israel's righteousness but YHWH's provision for the people's ongoing need of forgiveness. The request for forgiveness when Israel sins (8:46-53) anticipates the entire sacrificial system's purpose. Paul quotes a similar principle in Rom 3:23 ('all have sinned and fall short of the glory of God') as the universal diagnosis that makes the gospel necessary.</p>"
  },
  "19": {
    "12": "<p><strong>ve-achar haesh qol demamah daqah</strong>: 'And after the fire the sound of a low whisper' (or 'a still small voice,' KJV). The theophany at Horeb (Elijah's experience in 1 Kgs 19) deliberately echoes Sinai: Elijah is at Horeb (another name for Sinai), the mountain of God; YHWH passes by with wind, earthquake, and fire (the Sinai theophanic elements, Exod 19:16-19). But the climax is not in the dramatic elements but in the <em>qol demamah daqah</em> — the sound of sheer silence, the gentle whisper, the still small voice. YHWH is not absent from the dramatic; but he speaks in the gentle. The NT's Spirit comes both in wind and fire (Acts 2:2-3) and in the interior witness of the heart (Rom 8:16).</p>"
  }
}

KINGS1_CONTEXT = {
  "1": {
    "1": "<p>1-2 Kings (originally one book, divided in the LXX) narrates the history of the united monarchy (Solomon) and the divided kingdom (Israel/Judah) from ca. 971-561 BCE, ending with the release of Jehoiachin from Babylonian prison. Its authors (the 'Deuteronomistic historian') evaluate each king against the standard of Deuteronomy: fidelity to YHWH alone, worship only at the Jerusalem temple, and covenant obedience. The theological verdict is relentlessly critical: of the 20 kings of Judah, only Hezekiah and Josiah receive full approval. The narrative explains why the exile happened: Israel and Judah were destroyed because they refused to keep YHWH's covenant. This theological history is the background for understanding the exile as a covenant curse (Deut 28:36-37, 64-68) rather than YHWH's defeat.</p>"
  }
}

KINGS1_CHRIST = {
  "19": {
    "18": "<p>A direct revelation: 'Yet I will leave seven thousand in Israel, all the knees that have not bowed to Baal, and every mouth that has not kissed him.' The remnant principle — YHWH preserves a faithful minority even when the majority apostasizes — is one of the OT's most important theological contributions. Paul applies it directly to his own time (Rom 11:4-5): 'So too at the present time there is a remnant, chosen by grace.' The Elijah crisis reveals the structure of all subsequent covenant history: visible apostasy of the majority, invisible remnant of the elect, YHWH's sovereign preservation of his people through what appears to be total defeat. The cross looks like the end of Jesus's movement; Pentecost reveals it was the beginning of the new covenant remnant.</p>"
  }
}

KINGS2_ECHO = {
  "2": {
    "11": [
      {"type": "allusion", "target": "Luke 9:51", "note": "Elijah went up by a whirlwind into heaven — the ascension of Elijah (taken up without dying) is the OT's second ascension-figure (with Enoch, Gen 5:24); Jesus's ascension (Acts 1:9) fulfills the pattern; Luke explicitly notes Jesus 'set his face to go to Jerusalem' in the context of his upcoming departure (exodou, Luke 9:31) echoing Elijah's departure"},
      {"type": "fulfillment", "target": "Matt 17:3", "note": "Elijah and Moses appear with Jesus at the Transfiguration — the two figures who had unique mountaintop theophanies (Moses at Sinai, Elijah at Horeb/Sinai) flank the transfigured Jesus; the Transfiguration is the convergence of the Law (Moses) and the Prophets (Elijah) in the one of whom they spoke"}
    ]
  },
  "4": {
    "35": [
      {"type": "allusion", "target": "Acts 20:9-12", "note": "The child sneezed seven times and opened his eyes — Elisha raises the Shunammite's son (2 Kgs 4:32-37); Paul raises Eutychus in a similar pattern (fell from a third floor, Paul lay on him, he came to life); both instances frame the apostle as an Elisha-figure extending Jesus's resurrection ministry"}
    ]
  },
  "5": {
    "14": [
      {"type": "fulfillment", "target": "Luke 4:27", "note": "There were many lepers in Israel in the time of the prophet Elisha, and none of them was cleansed but only Naaman the Syrian — Jesus cites Naaman's healing as the OT precedent for grace going to a Gentile outsider; Naaman's healing is a type of Gentile inclusion, accomplished through the humbling medium of simple obedience (washing in the Jordan)"}
    ]
  }
}

KINGS2_ORIGINAL = {
  "2": {
    "9": "<p><strong>vehi peh shnayim beruchecha elai</strong>: 'Please let there be a double portion of your spirit on me.' Elisha's request for a 'double portion' (<em>pi shnayim</em>) is technically a request for the eldest son's inheritance share (Deut 21:17) — he is asking to be Elijah's primary heir and successor. Elijah responds that this is a 'hard thing' (<em>kasha</em>) but it will be granted if Elisha sees him taken. Elisha does see it, receives the spirit, and performs miracles that echo and exceed Elijah's. The Elijah-Elisha succession pattern shapes the NT's understanding of John the Baptist-Jesus relationship: John comes in the spirit and power of Elijah (Luke 1:17), and Jesus works in a pattern that exceeds John's, as Elisha's miracles exceeded Elijah's in number (Elijah performs 8 miracles in Kings; Elisha performs 16).</p>"
  }
}

KINGS2_CONTEXT = {
  "17": {
    "6": "<p>The fall of Samaria (722 BCE) to the Assyrian Empire (under Sargon II, 2 Kgs 17:6) ended the northern kingdom of Israel after 210 years and 19 kings (every one of whom 'did evil in the sight of YHWH'). The author of Kings provides the theological explanation in 17:7-23: because Israel sinned against YHWH, walked in the customs of the nations, built high places, served Baal — YHWH removed them out of his sight. The Assyrian exile of the northern tribes ('the ten lost tribes') was permanent: they were never restored as a distinct entity. The northern exile is the first fulfillment of the Deuteronomic covenant curses (Deut 28:36, 64); the Babylonian exile of Judah (586 BCE) is the second. Both are explained as covenant consequences, not historical accidents.</p>"
  }
}

KINGS2_CHRIST = {
  "5": {
    "14": "<p>A type: 'So he went down and dipped himself seven times in the Jordan, according to the word of the man of God, and his flesh was restored like the flesh of a little child, and he was clean.' Naaman's healing is one of the OT's most theologically rich type-narratives: (1) the outsider (a Gentile military commander) receives healing denied to insiders (Israelite lepers, Luke 4:27); (2) the healing comes through water — specifically the Jordan, the covenant-crossing water; (3) the means is foolishly simple (wash seven times) — Naaman expects a dramatic prophetic ritual; (4) the result is total cleansing. Jesus's citation of Naaman in Luke 4:27 to explain his own ministry to Nazareth (grace going to unexpected outsiders) and the Baptist's baptism in the Jordan both stand in the Naaman-and-the-Jordan typological stream: the Jordan is the water of covenant-entry and cleansing, fulfilled in baptism into Christ.</p>"
  }
}

KINGS1_ECHO_10_11 = {
    "10": {
        "1": [
            {"type": "allusion", "target": "Matt 12:42",
             "note": "The Queen of Sheba travels 'from the ends of the earth' to hear Solomon's wisdom. Jesus invokes her against his generation: 'the queen of the South will rise up at the judgment with this generation and condemn it, for she came from the ends of the earth to hear the wisdom of Solomon, and behold, something greater than Solomon is here' (Matt 12:42). A Gentile queen who sought merely human wisdom becomes the foil for those who have the incarnate Word and remain indifferent."},
            {"type": "allusion", "target": "Luke 11:31",
             "note": "Luke's parallel: 'the queen of the South will rise up at the judgment with the men of this generation and condemn them, for she came from the ends of the earth to hear the wisdom of Solomon, and behold, something greater than Solomon is here.' The queen's costly pursuit of wisdom is a judgment-standard: what she sought across continents is now present in person."}
        ],
        "23": [
            {"type": "allusion", "target": "Matt 6:29",
             "note": "Solomon exceeded all kings in wealth — his glory was the summit of human achievement. Jesus invokes Solomonic splendor only to supersede it: 'even Solomon in all his glory was not arrayed like one of these' (wildflowers of the field, Matt 6:29). The Father's care for creation surpasses the most glorious kingdom; therefore anxiety about provision is faithlessness, not prudence."}
        ]
    },
    "11": {
        "1": [
            {"type": "allusion", "target": "2 Cor 6:14",
             "note": "Solomon's 700 wives and 300 concubines from foreign nations 'turned his heart after other gods' (v.4). Paul's command 'do not be unequally yoked with unbelievers' (2 Cor 6:14) has Solomon's apostasy as its ultimate cautionary example: the wisest man who ever lived was brought down by covenant-violating intimate relationships that drew his devotion toward other gods."}
        ],
        "36": [
            {"type": "type", "target": "Luke 1:78",
             "note": "God promises to preserve 'one tribe to my servant David, that David my servant may always have a lamp before me in Jerusalem.' The preserved Davidic lamp — kept burning through political catastrophe, exile, and return — is the type of the messianic dawn Zechariah celebrates: 'the sunrise shall visit us from on high' (Luke 1:78). The lamp YHWH maintained for David's sake in Jerusalem finds its final flame in the one who is the light of the world."},
            {"type": "allusion", "target": "Rev 21:23",
             "note": "The Davidic lamp (v.36) — YHWH's commitment to sustain the line — points toward Revelation 21:23: 'the city has no need of sun or moon...for the glory of God gives it light, and its lamp is the Lamb.' The lamp YHWH promised David is ultimately the Lamb himself — the light the darkness has never extinguished (John 1:5)."}
        ]
    }
}

def main():
    books = [
        ('1kings', KINGS1_ECHO, KINGS1_ORIGINAL, KINGS1_CONTEXT, KINGS1_CHRIST),
        ('2kings', KINGS2_ECHO, KINGS2_ORIGINAL, KINGS2_CONTEXT, KINGS2_CHRIST),
    ]
    for book, echo_d, orig_d, ctx_d, chr_d in books:
        e = load_echo(book); merge_echo(e, echo_d); save_echo(book, e)
        c = load_comm('mkt-original', book); merge_comm(c, orig_d); save_comm('mkt-original', book, c)
        c = load_comm('mkt-context', book); merge_comm(c, ctx_d); save_comm('mkt-context', book, c)
        c = load_comm('mkt-christ', book); merge_comm(c, chr_d); save_comm('mkt-christ', book, c)
        print(f'{book}: all 4 layers written')
    e = load_echo('1kings'); merge_echo(e, KINGS1_ECHO_10_11); save_echo('1kings', e)

if __name__ == '__main__':
    main()
