"""
MKT Echo Layer — Acts chapters 14–15
Output: data/echoes/acts.json
Run: python3 scripts/zc-echo-acts-14-15.py

Key decisions:
- Acts 15:16 (Amos 9:11-12 quote) already present; merge_echoes skips it.
- Acts 14 needs full coverage: the first missionary journey's Gentile cities are saturated
  with OT echoes — the healing of the lame man echoes Acts 3/Isa 35; the crowd's
  Zeus/Hermes acclamation is the anti-type of the prophets refusing worship; Paul's
  'living God who made heaven and earth' is the standard OT Creator-formula; the stoning
  echoes the stoned-prophets tradition.
- Acts 15 (Jerusalem Council) echoes Deut 17 (appeals to central authority), the Amos
  quotation is central, and the abstention requirements echo Lev 17-18 (Noahide-adjacent).
- Echo entries anchor on the verse where the echo is most concentrated.
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
"14": {
    "1": [
        {
            "type": "typology",
            "target": "Neh 8:1-3",
            "note": "Paul and Barnabas speaking 'in such a way that a great number of both Jews and Greeks believed' echoes the public reading of the Law that produced a great response in Nehemiah 8 — Ezra reading before the assembly while the people listened attentively. The synagogue as the setting, the public proclamation, and the mass response of understanding and belief follow the pattern of the restored community hearing the word."
        }
    ],
    "3": [
        {
            "type": "typology",
            "target": "Exod 4:28-31",
            "note": "'The Lord... bore witness to the word of his grace, granting signs and wonders to be done by their hands' echoes the pattern of Moses and Aaron — the LORD confirmed their mission at the exodus with signs and wonders (Exod 4:28-31; Ps 105:27). Signs and wonders authenticate the divine sending of messengers throughout the OT; the same authentication pattern accompanies the apostles' mission."
        }
    ],
    "8": [
        {
            "type": "typology",
            "target": "Isa 35:6",
            "note": "The man at Lystra 'crippled from birth, who had never walked' is the same category of person as Isaiah's new-exodus promise — 'then shall the lame man leap like a deer' (Isa 35:6). This is the third lame-man healing in Luke-Acts (Luke 5:17-26; Acts 3:1-10), each one an enacted installment of the new-exodus healings Isaiah promised. The faith-note ('he had faith to be made well,' v.9) distinguishes this healing as a response to proclamation."
        }
    ],
    "10": [
        {
            "type": "typology",
            "target": "Acts 3:6-8",
            "note": "Paul's 'Stand upright on your feet' (Anastēthi epi tous podas sou) and the man's leaping up and walking directly echoes Peter's healing of the lame man at the Beautiful Gate (Acts 3:6-8 — 'rise and walk... he leaping up stood and began to walk'). Luke frames both healings with identical structure: the apostle looks, speaks the command in Jesus's name/authority, the man rises, and the crowd marvels. Both fulfill Isaiah 35:6."
        }
    ],
    "11": [
        {
            "type": "typology",
            "target": "Gen 11:7",
            "note": "The crowd's cry in Lycaonian (their local language — 'they lifted up their voices, saying in Lycaonian') is a subtle anti-Babel echo: at Babel, God confused the languages to prevent unified idolatry (Gen 11:7); here, a local language is used to promote idolatry. The many-languages of post-Babel humanity serve both the spread of the gospel (Acts 2) and the persistence of old-covenant paganism."
        }
    ],
    "14": [
        {
            "type": "typology",
            "target": "Num 14:6",
            "note": "Paul and Barnabas tearing their garments (diarēxantes ta himatia autōn) at the crowd's attempt to worship them echoes Joshua and Caleb tearing their garments when the people rebelled against God's command to enter Canaan (Num 14:6). The garment-tearing is the standard prophetic gesture of absolute horror at blasphemy or apostasy — the body-language of 'this must not happen.'"
        }
    ],
    "15": [
        {
            "type": "fulfillment",
            "target": "Exod 20:11",
            "note": "'Turn from these vain things to a living God, who made the heaven and the earth and the sea and all that is in them' — the Creator-formula (heaven, earth, sea, and all in them) is the standard OT confession of YHWH as the living God (Exod 20:11; Ps 146:6; Neh 9:6). Paul's Gentile preaching appeals to creation-knowledge rather than the Mosaic covenant — the starting point available to all humanity through creation."
        },
        {
            "type": "allusion",
            "target": "Jer 10:3-5",
            "note": "'Vain things' (ta mataia — empty, worthless things) is the LXX translation of hevel (vanity/emptiness) applied to idols throughout the prophets: Jeremiah 10:3-5 ('the customs of the peoples are vanity... their idols are like scarecrows in a cucumber field'). Paul's appeal to turn from mataia echoes the prophetic polemic against idolatry as emptiness (Isa 44:9; Hos 5:11)."
        }
    ],
    "17": [
        {
            "type": "allusion",
            "target": "Deut 11:14",
            "note": "'He did not leave himself without witness, for he did good by giving you rains from heaven and fruitful seasons, satisfying your hearts with food and gladness' echoes Deuteronomy's covenant-blessing promises: 'he will give the rain for your land in its season, the early rain and the later rain' (Deut 11:14; 28:12). The rains-and-fruitful-seasons that pagans attribute to Zeus are the witness of the living God to all peoples through creation's providential order."
        }
    ],
    "19": [
        {
            "type": "typology",
            "target": "2 Kgs 2:12",
            "note": "Paul stoned and dragged out of the city and left for dead echoes the violence done to the prophets: Jeremiah was beaten and put in stocks (Jer 20:2); Zechariah was stoned in the temple court (2 Chr 24:21); Elijah fled for his life (1 Kgs 19:3). The stoning anticipates the disciples' standing in the prophetic line — 'blessed are you when others revile you and persecute you... for so they persecuted the prophets who were before you' (Matt 5:11-12)."
        }
    ],
    "20": [
        {
            "type": "typology",
            "target": "1 Kgs 19:8",
            "note": "Paul rising from apparent death and entering the city echoes Elijah's supernatural restoration at Horeb — 'he arose and ate and drank, and went in the strength of that food forty days and forty nights' (1 Kgs 19:8). Both the prophet and the apostle are left for dead (or exhausted) and then rise to continue the mission. The pattern of prophetic perseverance-through-death is the apostolic pattern."
        }
    ],
    "22": [
        {
            "type": "allusion",
            "target": "Dan 12:1",
            "note": "'Through many tribulations we must enter the kingdom of God' echoes Daniel's promise that there will be 'a time of trouble, such as never has been since there was a nation till that time' before the deliverance comes (Dan 12:1). The tribulation-before-the-kingdom structure is the standard eschatological expectation shaped by Daniel; the apostles announce that the tribulations are already underway as the kingdom arrives."
        }
    ],
    "23": [
        {
            "type": "typology",
            "target": "Exod 18:25-26",
            "note": "Paul and Barnabas appointing elders (presbyterous) in every church and committing them to the Lord echoes Moses appointing capable men as rulers over thousands and hundreds at Jethro's counsel (Exod 18:25-26) and Moses placing the Spirit on the seventy elders (Num 11:16-17). The commissioning of plural local leaders under prayer and fasting is the Moses-pattern of distributed, Spirit-confirmed governance."
        }
    ],
    "27": [
        {
            "type": "fulfillment",
            "target": "Isa 45:22",
            "note": "'He had opened a door of faith to the Gentiles' uses the 'door' metaphor for divine opportunity while describing the Gentile mission as accomplished. This fulfills Isaiah's universal invitation: 'Turn to me and be saved, all the ends of the earth! For I am God, and there is no other' (Isa 45:22). The opened door is the theological claim that God himself has opened access for Gentile faith — not merely that humans created opportunity."
        }
    ]
},
"15": {
    "1": [
        {
            "type": "allusion",
            "target": "Gen 17:10-14",
            "note": "The Judaizers insisting 'unless you are circumcised according to the custom of Moses, you cannot be saved' demand that the Abrahamic covenant-sign (circumcision, Gen 17:10-14) be required of Gentile believers. The Jerusalem Council will determine whether the new-covenant entrance-rite (baptism, faith) fulfills or requires the supplement of the Abrahamic covenant-sign — a question resolved by Peter's Cornelius report and James's Amos citation."
        }
    ],
    "8": [
        {
            "type": "fulfillment",
            "target": "Joel 2:28",
            "note": "Peter's testimony that 'God, who knows the heart, bore witness to them by giving them the Holy Spirit just as he did to us' restates the Cornelius-Pentecost event as the fulfillment of Joel 2:28 — Spirit poured on all flesh without ethnic distinction. The God who 'knows the heart' (kardiognōstēs — Acts 1:24) has bypassed circumcision as the criterion and used the heart-level Spirit-gift as the authenticating sign of inclusion."
        }
    ],
    "10": [
        {
            "type": "allusion",
            "target": "Deut 7:6",
            "note": "Peter's 'why are you putting God to the test by placing a yoke on the neck of the disciples that neither our fathers nor we have been able to bear?' alludes to the OT's own witness against Israel's consistent failure to keep the Mosaic law. The 'yoke' imagery (Mt 11:29-30; Sir 51:26) is the burden of the law as requirement for standing before God — a burden that the OT itself diagnoses as humanly unbearable."
        }
    ],
    "11": [
        {
            "type": "fulfillment",
            "target": "Hab 2:4",
            "note": "'We believe that we will be saved through the grace of the Lord Jesus, just as they will' — Peter's radical conclusion (Jews saved the same way Gentiles are: grace through faith) fulfills the Habakkuk principle: 'the righteous shall live by his faith' (Hab 2:4). There is no ethnic advantage in the salvation-economy of grace: Jew and Gentile stand before God on the same terms."
        }
    ],
    "14": [
        {
            "type": "fulfillment",
            "target": "Isa 19:24-25",
            "note": "James's summary that 'God first visited the Gentiles, to take from them a people for his name' (laon ex ethnōn — a people from the nations) is the fulfillment of the OT promises that God would have a people from the nations, not merely from Israel: Isaiah 19:24-25 ('Israel will be the third with Egypt and Assyria, a blessing in the midst of the earth') and Zechariah 2:11 ('many nations shall join themselves to the LORD in that day and shall be my people')."
        }
    ],
    "16": [
        {
            "type": "fulfillment",
            "target": "Amos 9:11-12",
            "note": "Already present."
        }
    ],
    "19": [
        {
            "type": "allusion",
            "target": "Lev 17:10-14",
            "note": "James's requirement that Gentile believers abstain from things polluted by idols, sexual immorality, what has been strangled, and blood echoes Leviticus 17-18's requirements that applied to 'the stranger who sojourns among you' (Lev 17:10-16; 18:26) — the Gentile resident-alien regulations within Israel. The Jerusalem decree applies the 'Noahide-adjacent' minimal holiness requirements to Gentiles living in proximity to Jewish believers."
        }
    ],
    "28": [
        {
            "type": "typology",
            "target": "Num 11:17",
            "note": "'It has seemed good to the Holy Spirit and to us to lay on you no greater burden than these requirements' — the Jerusalem Council's Spirit-guided consensus-decision echoes the pattern of Spirit-distributed governance in Numbers 11:17-25: the Spirit rested on the seventy elders, distributing Moses's burden of leadership to a plural council. The council's decision is not merely human deliberation but Spirit-guided communal discernment."
        }
    ]
}
}

def main():
    existing = load_echoes('acts')
    merge_echoes(existing, ACTS_ECHOES)
    save_echoes('acts', existing)
    for ck in ['14', '15']:
        n = len(existing.get(ck, {}))
        print(f'Acts ch {ck}: {n} echo entries')

if __name__ == '__main__':
    main()
