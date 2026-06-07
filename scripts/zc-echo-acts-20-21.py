"""
MKT Echo Layer — Acts chapters 20–21
Output: data/echoes/acts.json
Run: python3 scripts/zc-echo-acts-20-21.py

Key decisions:
- Both chapters start empty; all entries are new.
- Acts 20 (Miletus farewell): Eutychus's death/raising echoes Elijah/Elisha resurrection
  pattern; Paul's farewell speech to Ephesian elders echoes Moses's farewell in Deuteronomy
  and Samuel's farewell in 1 Sam 12; the blood-of-the-flock shepherd imagery echoes Ezek 34.
- Acts 21 (Jerusalem approach): Paul's Spirit-warnings on the way echo Jeremiah's prophetic
  warnings about going to Egypt; Agabus's belt-binding echoes Jeremiah's prophetic-action
  tradition; Paul's Nazirite vow echoes Num 6; the temple riot echoes the Jeremiah temple
  sermon pattern.
- Echo entries anchor on the verse where the OT resonance is most concentrated.
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
"20": {
    "7": [
        {
            "type": "typology",
            "target": "Lev 23:11",
            "note": "Breaking bread on 'the first day of the week' (mia tōn sabbatōn) signals the Lord's Day gathering anchored in the resurrection — the new first-day that fulfills the Levitical first-fruits offering (Lev 23:11 — 'the priest shall wave the sheaf before the LORD on the day after the Sabbath'). The resurrection as first-fruits (1 Cor 15:20) makes the first day of the week the eschatological new-creation day."
        }
    ],
    "9": [
        {
            "type": "typology",
            "target": "1 Kgs 17:17",
            "note": "Eutychus falling asleep during Paul's extended teaching, falling from the third-floor window, and being 'taken up dead' precisely replicates the conditions for an Elijah/Elisha resurrection: a young person dies, the prophet goes down to them, and life is restored. The overnight teaching session and the death-by-falling create the crisis that frames the miracle."
        }
    ],
    "10": [
        {
            "type": "typology",
            "target": "2 Kgs 4:34-35",
            "note": "Paul 'falling upon' (epipesōn) Eutychus and embracing him while declaring 'his life is in him' mirrors the Elisha sequence at Shunem: Elisha 'lay on the child, putting his mouth on his mouth... and the flesh of the child became warm' (2 Kgs 4:34). The physical contact, the prophetic declaration, and the restoration of life follow the Elisha-pattern that Luke has already applied to Peter raising Tabitha (Acts 9:40)."
        }
    ],
    "17": [
        {
            "type": "typology",
            "target": "Deut 31:1-8",
            "note": "Paul's farewell speech to the Ephesian elders at Miletus is Luke's Deuteronomy — the great apostolic farewell that echoes Moses's last address to Israel (Deut 31-33) and Samuel's farewell to the elders of Israel (1 Sam 12). All three farewell speeches follow the same structure: appeal to blameless conduct, warning about future dangers, exhortation to faithfulness, and commendation to God."
        }
    ],
    "18": [
        {
            "type": "allusion",
            "target": "1 Sam 12:3",
            "note": "'You yourselves know how I lived among you the whole time from the first day that I set foot in Asia' echoes Samuel's appeal to Israel at his farewell: 'Here I am; testify against me before the LORD... whose ox have I taken? Or whose donkey have I taken? Or whom have I defrauded?' (1 Sam 12:3). The appeal to eyewitness testimony of blameless conduct is the standard form of the servant-of-God's self-vindication at the conclusion of his public ministry."
        }
    ],
    "26": [
        {
            "type": "allusion",
            "target": "Ezek 33:1-6",
            "note": "'I am innocent of the blood of all, for I did not shrink from declaring to you the whole counsel of God' directly echoes Ezekiel's watchman-passage: if the watchman fails to warn and the wicked die in their iniquity, 'their blood I will require at the watchman's hand' (Ezek 33:6). Paul declares himself a faithful watchman who has sounded every alarm. The blood-responsibility framework is Ezekiel's prophetic vocation-language."
        }
    ],
    "28": [
        {
            "type": "fulfillment",
            "target": "Ezek 34:11-16",
            "note": "'Pay careful attention to yourselves and to all the flock, in which the Holy Spirit has made you overseers, to care for the church of God, which he obtained with his own blood' fulfills Ezekiel 34's promise of the divine Shepherd who will 'seek out my sheep, and rescue them from all places... I will seek the lost, and I will bring back the strayed' (Ezek 34:11-12). The elders-as-shepherds under the Chief Shepherd who purchased the flock with his blood is the Ezekiel-34 pattern fulfilled."
        }
    ],
    "29": [
        {
            "type": "allusion",
            "target": "Ezek 34:2-3",
            "note": "'After my departure fierce wolves will come in among you, not sparing the flock' echoes Ezekiel's condemnation of the false shepherds who 'scattered my flock and have not attended to them' (Ezek 34:2-8) and Jesus's warning about false prophets who 'come to you in sheep's clothing but inwardly are ravenous wolves' (Matt 7:15). The wolf-flock imagery is the standard OT false-leader typology."
        }
    ],
    "32": [
        {
            "type": "allusion",
            "target": "Deut 33:1-3",
            "note": "Paul commending the elders 'to God and to the word of his grace, which is able to build you up and to give you the inheritance among all those who are sanctified' echoes Moses's final blessing: commending Israel to the God who keeps them. The 'inheritance among the sanctified' is the language of Deuteronomy's promised-land inheritance (Deut 33:4 — 'Moses commanded us a law, an inheritance for the congregation of Jacob')."
        }
    ],
    "35": [
        {
            "type": "allusion",
            "target": "Prov 11:24-25",
            "note": "Paul citing 'It is more blessed to give than to receive' as a word of the Lord Jesus echoes the Proverbs wisdom tradition: 'One gives freely, yet grows all the richer; another withholds what he should give, and only suffers want. Whoever brings blessing will be enriched, and one who waters will himself be watered' (Prov 11:24-25). The generosity-wisdom of Proverbs is here attributed to Jesus as its fulfillment and authority."
        }
    ]
},
"21": {
    "4": [
        {
            "type": "typology",
            "target": "Jer 42:1-7",
            "note": "The disciples at Tyre urging Paul 'through the Spirit not to go on to Jerusalem' echoes the tension in Jeremiah between prophetic warnings and prophetic obedience: the people ask Jeremiah whether to go to Egypt and he says no, but they go anyway (Jer 42-43). Paul's Spirit-warned-but-compelled journey to Jerusalem mirrors Jeremiah's own journey of prophetic faithfulness toward the city of rejection."
        }
    ],
    "9": [
        {
            "type": "fulfillment",
            "target": "Joel 2:28",
            "note": "Philip's four daughters who 'prophesied' (prophēteusai) are among the most direct NT fulfillments of Joel 2:28 — 'your sons and your daughters shall prophesy.' The Spirit poured on 'all flesh' explicitly includes daughters; the prophesying daughters of Philip, a Hellenist deacon and evangelist (Acts 6:5; 8:4-40), are the embodied Joel-2 fulfillment in the Gentile mission context."
        }
    ],
    "11": [
        {
            "type": "typology",
            "target": "Jer 13:1-11",
            "note": "Agabus binding himself with Paul's belt and declaring 'Thus says the Holy Spirit, So shall the Jews at Jerusalem bind the man who owns this belt' is a classic OT symbolic-action prophecy: Jeremiah burying the linen loincloth (Jer 13:1-11), Isaiah walking naked and barefoot (Isa 20:2-4), Ezekiel lying on his side (Ezek 4). The prophetic action enacts and interprets what is coming; 'thus says the Holy Spirit' is 'thus says the LORD' in pneumatological form."
        }
    ],
    "13": [
        {
            "type": "typology",
            "target": "Jer 26:12-15",
            "note": "Paul's 'I am ready not only to be imprisoned but even to die in Jerusalem for the name of the Lord Jesus' echoes Jeremiah's declaration at his temple trial: 'The LORD sent me to prophesy against this house... as for me, behold, I am in your hands. Do with me as seems good and right to you' (Jer 26:12-14). Both prophet and apostle accept death-at-Jerusalem as the possible cost of faithful proclamation."
        }
    ],
    "20": [
        {
            "type": "allusion",
            "target": "Gen 17:9-14",
            "note": "The Jerusalem elders' report that Jewish believers are 'all zealous for the law' and their proposal that Paul participate in a Nazirite vow to demonstrate his Torah-observance reflects the ongoing significance of the Abrahamic covenant-sign within Jewish Christianity. The tension between Mosaic observance and Gentile freedom from it is the Acts 15 question in individual form: the same Spirit permits both (1 Cor 9:20-21)."
        }
    ],
    "23": [
        {
            "type": "typology",
            "target": "Num 6:1-21",
            "note": "Paul's participation in the purification rites and Nazirite vow completion (paying for the four men's heads to be shaved) echoes the Nazirite legislation of Numbers 6. The vow-completion ceremony required shaving, burnt offerings, sin offerings, and peace offerings at the temple. Paul's willingness to sponsor this ceremony demonstrates his claim that he does not 'teach all the Jews who are among the Gentiles to forsake Moses' (v.21)."
        }
    ],
    "27": [
        {
            "type": "typology",
            "target": "Jer 7:1-15",
            "note": "The Asian Jews seizing Paul in the temple and crying 'Men of Israel, help!' (v.28 — 'this is the man who is teaching everyone everywhere against the people and the law and this place') echoes the accusations against Jeremiah at his temple sermon (Jer 26:9 — 'you shall die! Why have you prophesied in the name of the LORD, saying, This house shall be like Shiloh?'). The temple-context accusation of teaching against the temple is the standard mechanism for eliminating prophetic voices in Israel."
        }
    ],
    "30": [
        {
            "type": "typology",
            "target": "Jer 38:4-6",
            "note": "The whole city being 'stirred up' and the crowd 'dragging Paul out of the temple' echoes the mob-seizure of Jeremiah: the officials put Jeremiah in a cistern and the crowd sought his death (Jer 38:4-6). The pattern is consistent: the prophet who speaks in the temple against the religious establishment is seized by the crowd, dragged out, and subjected to mob violence."
        }
    ],
    "36": [
        {
            "type": "typology",
            "target": "Jer 26:8-9",
            "note": "The crowd's cry 'Away with him!' (Aire auton — lift him away, destroy him) echoes the Jerusalem crowd's cries at Jesus's trial (Luke 23:18 — 'Away with this man!') and the mob at Jeremiah's temple sermon ('You shall die!' — Jer 26:8). The same crowd-pattern that rejected the prophets and rejected Christ now moves against Christ's apostle — 'a servant is not greater than his master' (John 15:20)."
        }
    ],
    "40": [
        {
            "type": "typology",
            "target": "Neh 8:5",
            "note": "Paul standing on the steps and 'motioning with his hand to the people... when there was a great silence, he addressed them in the Hebrew language' echoes Ezra/Nehemiah's pattern of public proclamation: 'Ezra opened the book in the sight of all the people, for he was above all the people, and as he opened it all the people stood. And Ezra blessed the LORD, the great God, and all the people answered, Amen' (Neh 8:5-6). The elevated speaker, the silenced crowd, and the address in the Hebrew tongue are the conventions of covenant-assembly proclamation."
        }
    ]
}
}

def main():
    existing = load_echoes('acts')
    merge_echoes(existing, ACTS_ECHOES)
    save_echoes('acts', existing)
    for ck in ['20', '21']:
        n = len(existing.get(ck, {}))
        print(f'Acts ch {ck}: {n} echo entries')

if __name__ == '__main__':
    main()
