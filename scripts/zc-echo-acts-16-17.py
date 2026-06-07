"""
MKT Echo Layer — Acts chapters 16–17
Output: data/echoes/acts.json
Run: python3 scripts/zc-echo-acts-16-17.py

Key decisions:
- Acts 17:28 (Aratus/Epimenides quote) already present; merge_echoes skips it.
- Acts 16 (Philippi): Lydia's opened heart echoes Ezek 36:26; the exorcism of the
  slave girl echoes the OT's pattern of Spirit-driven expulsion; the earthquake-opened
  prison echoes Ps 107:10-16 and Isa 42:7; the Philippian jailer's conversion follows
  the Cornelius structural pattern.
- Acts 17 (Athens): the Areopagus speech is the most OT-saturated 'natural theology'
  speech in Acts — unknown God fulfills Isa 45; 'in him we live' echoes Jer 23:24;
  Paul's creation-from-one argument echoes Gen 1-2; resurrection-judgment echoes Dan 12.
- Echo entries anchor on the verse where the OT resonance is most explicit.
"""
import json, pathlib

ROOT = pathlib.Path(__file__).parent.parent

def load_echoes(book):
    p = ROOT / 'data' / 'echoes' / f'{book}.json'
    if p.exists():
        return json.loads(p.read_text())
    return {}

def save_echoes(book, data):
    p = ROOT / 'data' / 'echoes' / f'{book}.json'
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=None))
    print(f'  wrote {p.relative_to(ROOT)}')

def merge_echoes(existing, new_data):
    # INTENT: Add new chapter/verse echo entries without overwriting existing ones — safe to re-run.
    # CHANGE? If echo JSON structure changes from {ch:{v:[entries]}}, update this traversal.
    # VERIFY: Re-running should produce identical verse counts (no duplicated entries).
    for ch, verses in new_data.items():
        if ch not in existing:
            existing[ch] = {}
        for v, entries in verses.items():
            if v not in existing[ch]:
                existing[ch][v] = entries

ACTS_ECHOES = {
"16": {
    "6": [
        {
            "type": "typology",
            "target": "Ezek 1:3",
            "note": "The Spirit's repeated blocking of Paul's planned mission routes ('having been forbidden by the Holy Spirit to speak the word in Asia... the Spirit of Jesus did not allow them') echoes the prophetic tradition of divine redirection — Ezekiel constrained by the Spirit (Ezek 3:14), Jonah's route redirected, the word of the LORD closing and opening prophetic access. The Spirit drives the mission by alternately opening and closing doors."
        }
    ],
    "9": [
        {
            "type": "typology",
            "target": "Isa 46:11",
            "note": "The Macedonian vision ('Come over to Macedonia and help us') redirecting the mission to Europe echoes the divine calling of a man from the east to accomplish the LORD's purpose (Isa 46:11 — 'calling a bird of prey from the east, the man of my counsel from a far country'). The visionary summons from a distant region is the form in which the Spirit directs the mission across new geographic-cultural boundaries."
        }
    ],
    "13": [
        {
            "type": "allusion",
            "target": "Ps 137:1",
            "note": "The riverside prayer gathering outside Philippi (proseuche — a prayer place, often used by diaspora Jewish communities where a synagogue could not be established) echoes the exilic prayer-by-rivers: 'By the waters of Babylon, there we sat down and wept... On the willows there we hung up our lyres' (Ps 137:1). The Jewish diaspora prayed by rivers; Paul brings the gospel to that riverside prayer gathering."
        }
    ],
    "14": [
        {
            "type": "fulfillment",
            "target": "Ezek 36:26",
            "note": "'The Lord opened her heart to pay attention to what was said by Paul' — Lydia's divinely opened heart fulfills Ezekiel's new covenant promise: 'I will remove the heart of stone from your flesh and give you a heart of flesh' (Ezek 36:26). The opened heart is the new-covenant gift; it is God who opens, not human persuasion. The seller of purple from Thyatira receives the promise made to Israel and extended to the nations."
        }
    ],
    "16": [
        {
            "type": "typology",
            "target": "1 Sam 28:7",
            "note": "The slave girl 'having a spirit of divination' (pneuma puthōna — a Pythian spirit, the spirit of the Delphic oracle) echoes the OT's account of divination-spirits: the medium at En-dor (1 Sam 28:7), the Mosaic prohibition of those who consult spirits (Deut 18:10-11). The Spirit-of-Christ and the divination-spirit are the binary opposition that structures Luke-Acts's encounter with pagan spirituality."
        }
    ],
    "17": [
        {
            "type": "typology",
            "target": "Mark 1:24",
            "note": "The slave girl's cry 'These men are servants of the Most High God, who proclaim to you the way of salvation' echoes the demonic confession pattern in the Synoptic exorcism accounts — 'I know who you are — the Holy One of God' (Mark 1:24; Luke 4:34). The demonic realm's correct identification of God's messengers/agent is the pattern: they know, though the humans refuse to know. Paul silences the spirit as Jesus silenced the demons."
        }
    ],
    "18": [
        {
            "type": "typology",
            "target": "1 Kgs 18:18",
            "note": "Paul, 'having become greatly annoyed,' commands the spirit to come out in Jesus's name — the authoritative command-exorcism echoes Elijah's confrontation with the prophets of Baal (1 Kgs 18) and the OT pattern of prophetic authority over demonic forces. The name of Jesus is the functional equivalent of the name of YHWH invoked in prophetic confrontations with false spirits."
        }
    ],
    "25": [
        {
            "type": "typology",
            "target": "Ps 34:8",
            "note": "Paul and Silas praying and singing hymns at midnight in the prison echoes the Psalter's pattern of praise in extremity: 'I will bless the LORD at all times; his praise shall continually be in my mouth' (Ps 34:1); 'at midnight I rise to praise you' (Ps 119:62). The praise offered in prison before the earthquake is the enacted confidence in the God who delivers — the same posture as Shadrach, Meshach, and Abednego before the furnace (Dan 3:17-18)."
        }
    ],
    "26": [
        {
            "type": "fulfillment",
            "target": "Ps 107:14",
            "note": "The earthquake opening all the prison doors and unfastening all the prisoners' fetters fulfills Psalm 107:10-16 — 'Some sat in darkness and in the shadow of death, prisoners in affliction and in irons... He brought them out of darkness and the shadow of death, and burst their bonds apart.' The rescue-by-God of prisoners in darkness is a Psalter-theme that Acts repeatedly enacts: Acts 5:19 (angel opens the prison), 12:7 (Peter's rescue), now 16:26."
        }
    ],
    "28": [
        {
            "type": "allusion",
            "target": "1 Kgs 19:5",
            "note": "Paul's loud cry 'Do not harm yourself, for we are all here' preventing the jailer's suicide echoes the angel's preservation of Elijah at his lowest point: 'Arise and eat, for the journey is too great for you' (1 Kgs 19:7-8). The apostle's preservation of life at the point of despair mirrors the prophetic tradition of life-preservation in extremity. Both Elijah and the jailer encounter the living God immediately after their brush with death."
        }
    ],
    "30": [
        {
            "type": "typology",
            "target": "Acts 2:37",
            "note": "The jailer's 'Sirs, what must I do to be saved?' directly parallels the Pentecost crowd's 'What shall we do?' (Acts 2:37) — the two great conversion-questions of Acts are formally identical. The answer is also structurally identical: believe/repent + baptism. The Pentecost pattern of conviction → question → proclamation → baptism is repeated in the Philippian jail, confirming it as the normative conversion-structure."
        }
    ],
    "34": [
        {
            "type": "typology",
            "target": "Gen 18:5-8",
            "note": "The jailer bringing Paul and Silas into his house, setting food before them, and rejoicing with his whole household echoes the hospitality pattern of the patriarchs — Abraham setting food before the divine visitors at Mamre (Gen 18:5-8). The table-fellowship that follows conversion is the enacted reception of the kingdom: those who receive the apostles receive Christ (Luke 10:8-9), and the shared meal seals the household's welcome into the community of faith."
        }
    ]
},
"17": {
    "2": [
        {
            "type": "typology",
            "target": "Ezra 7:6",
            "note": "Paul reasoning with them 'from the Scriptures, explaining and proving that it was necessary for the Christ to suffer and to rise from the dead' follows the Ezra-model of the skilled scribe: 'Ezra had set his heart to study the Law of the LORD, and to do it and to teach his statutes and rules in Israel' (Ezra 7:10). The synagogue Torah-study context transforms the Scriptures into Christological proof; Paul is the scribe who brings out treasures old and new (Matt 13:52)."
        }
    ],
    "3": [
        {
            "type": "fulfillment",
            "target": "Isa 53:3-5",
            "note": "Paul 'explaining and proving that it was necessary for the Christ to suffer' (pathein ton Christon) centers on the Servant Songs as the scriptural basis for a suffering Messiah. The 'necessity' (edei — divine must) of the Christ's suffering is the Lukan Christological claim grounded in Isaiah 53's portrait of the Servant who is 'wounded for our transgressions, crushed for our iniquities.'"
        }
    ],
    "11": [
        {
            "type": "typology",
            "target": "Deut 17:9",
            "note": "The Bereans who 'received the word with all eagerness, examining the Scriptures daily to see if these things were so' model the Deuteronomic pattern of appealing to the written word for adjudication: Deut 17:9-11 commands going to the priests and judges to consult the written law on disputed matters. The Bereans treat the Scriptures as the arbiter of Paul's claims — the written word tests the oral proclamation."
        }
    ],
    "16": [
        {
            "type": "typology",
            "target": "Isa 44:9-20",
            "note": "Paul's spirit being 'provoked within him as he saw that the city was full of idols' echoes the prophetic grief and indignation at idolatry: Isaiah's extended polemic against idol-makers (Isa 44:9-20 — 'half of it he burned in the fire... and the rest of it he makes into a god, his idol'), Jeremiah's 'my soul weeps in secret for your pride' (Jer 13:17). The Spirit-provoked response to idolatry is the prophetic response."
        }
    ],
    "23": [
        {
            "type": "fulfillment",
            "target": "Isa 45:15",
            "note": "Paul's use of the altar 'to an unknown god' (agnōstō theō) as his entry-point inverts and fulfills Isaiah's ironic cry: 'Truly you are a God who hides himself, O God of Israel, the Savior' (Isa 45:15). The God whom the Athenians sensed but could not name is the one Isaiah said was hidden — now made known through the resurrection of Jesus. The 'unknown God' of Athenian religiosity is the 'hidden God' of Isaianic theology revealed."
        }
    ],
    "24": [
        {
            "type": "fulfillment",
            "target": "1 Kgs 8:27",
            "note": "'The God who made the world and everything in it, being Lord of heaven and earth, does not live in temples made by man' directly echoes Solomon's temple-dedication prayer: 'But will God indeed dwell on the earth? Behold, heaven and the highest heaven cannot contain you; how much less this house that I have built!' (1 Kgs 8:27). The Areopagus speech applies OT temple-theology to Athenian temples — even Israel's own king knew the temples cannot contain God."
        }
    ],
    "25": [
        {
            "type": "fulfillment",
            "target": "Ps 50:9-12",
            "note": "'Nor is he served by human hands, as though he needed anything, since he himself gives to all mankind life and breath and everything' echoes Psalm 50:9-12: 'I will not accept a bull from your house or goats from your folds... For every beast of the forest is mine, the cattle on a thousand hills... and the world and its fullness are mine.' The God who needs nothing and gives everything is the consistent OT counter-witness to the pagan economies of sacrifice-to-appease-the-gods."
        }
    ],
    "26": [
        {
            "type": "fulfillment",
            "target": "Gen 1:28",
            "note": "'He made from one man every nation of mankind to live on all the face of the earth, having determined allotted periods and the boundaries of their dwelling place' echoes Genesis 1:28 (the commission to fill the earth) and Deuteronomy 32:8 ('When the Most High gave to the nations their inheritance, when he divided mankind, he fixed the borders of the peoples according to the number of the sons of God'). The diversity of nations is not accident but divine ordering."
        }
    ],
    "27": [
        {
            "type": "allusion",
            "target": "Jer 23:23-24",
            "note": "'That they should seek God, and perhaps feel their way toward him and find him. Yet he is actually not far from each one of us' echoes the divine omnipresence of Jeremiah 23:23-24: 'Am I a God at hand, declares the LORD, and not a God far away? Can a man hide himself in secret places so that I cannot see him? Do I not fill heaven and earth?' Paul's 'not far from each one of us' is the Areopagus translation of Jeremiah's omnipresent God into Athenian philosophical language."
        }
    ],
    "28": [
        {
            "type": "fulfillment",
            "target": "Gen 2:7",
            "note": "Already present."
        }
    ],
    "30": [
        {
            "type": "fulfillment",
            "target": "Isa 45:22",
            "note": "'The times of ignorance God overlooked, but now he commands all people everywhere to repent' echoes the universal scope of Isaiah's call: 'Turn to me and be saved, all the ends of the earth!' (Isa 45:22). The 'now' of Paul's proclamation is the 'now' of Isaiah's eschatological invitation: the time of ignorance is past; the universal summons to turn to the living God has gone out to all nations."
        }
    ],
    "31": [
        {
            "type": "fulfillment",
            "target": "Dan 12:2",
            "note": "'He has fixed a day on which he will judge the world in righteousness by a man whom he has appointed, and of this he has given assurance to all by raising him from the dead' fulfills Daniel's judgment-scene: 'Many of those who sleep in the dust of the earth shall awake, some to everlasting life, and some to shame and everlasting contempt' (Dan 12:2), and the Son of Man given dominion and judgment (Dan 7:13-14). The Areopagus ends with the OT's eschatological judgment anchored in the resurrection."
        }
    ]
}
}

def main():
    existing = load_echoes('acts')
    merge_echoes(existing, ACTS_ECHOES)
    save_echoes('acts', existing)
    for ck in ['16', '17']:
        n = len(existing.get(ck, {}))
        print(f'Acts ch {ck}: {n} echo entries')

if __name__ == '__main__':
    main()
