"""
echo layer: Ezekiel 44-46
Visionary temple-regulation chapters. Key NT echo clusters:
  - ch44 east gate shut/opened → Heb 10:19-22 (access by Christ's blood)
  - ch44 uncircumcised heart excluded → Eph 2:11-22; Rom 2:29
  - ch44 Zadokite priests → Heb 7:26 (holy, blameless, unstained)
  - ch44 "I am their inheritance" → 1 Pet 1:4; Eph 1:14
  - ch45 Passover prince provides atonement → 1 Cor 5:7; Heb 9:12
  - ch46 gate access and prince's approach → Heb 10:19-22; John 10:9
  - ch46 son vs. servant inheritance → Gal 4:7; John 8:35
"""

import json, pathlib

ROOT = pathlib.Path(__file__).parent.parent

def load_echo(book):
    p = ROOT / "data" / "echoes" / f"{book}.json"
    return json.loads(p.read_text()) if p.exists() else {}

def save_echo(book, data):
    p = ROOT / "data" / "echoes" / f"{book}.json"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=None))
    print(f"  wrote {p.relative_to(ROOT)}")

def merge_echo(existing, new_data):
    for ch, verses in new_data.items():
        if ch not in existing:
            existing[ch] = {}
        for v, entries in verses.items():
            if v not in existing[ch]:
                existing[ch][v] = entries
            else:
                seen = {(e["type"], e["target"]) for e in existing[ch][v]}
                for e in entries:
                    if (e["type"], e["target"]) not in seen:
                        existing[ch][v].append(e)
                        seen.add((e["type"], e["target"]))

EZEKIEL_ECHOES = {
  "44": {
    "2": [
      {"type": "allusion", "target": "Heb 10:19-22", "note": "This gate shall remain shut; it shall not be opened — the LORD, the God of Israel, has entered by it, therefore it is shut: the sealed eastern gate through which only the divine glory passes is the sanctuary barrier; Hebrews 10:19-22 announces the barrier has been opened for all believers by the blood of Jesus — the new and living way through the curtain (his flesh); what Ezekiel sees as permanently shut because of divine holiness, Christ opens for all who approach in faith"},
      {"type": "allusion", "target": "Matt 27:51", "note": "The gate that marks the boundary between divine presence and human access — at the crucifixion the temple curtain (the barrier to the Most Holy Place) was torn from top to bottom (Matt 27:51); Ezekiel's sealed gate and the temple veil are both expressions of the same principle — God's holiness bars unmediated access — and Christ's death opens what the sealed gate represented as permanently closed"}
    ],
    "7": [
      {"type": "fulfillment", "target": "Eph 2:11-14", "note": "You have admitted foreigners uncircumcised in heart and flesh to my sanctuary — the exclusion of the uncircumcised from the eschatological sanctuary is resolved in Christ: Paul addresses those who were once called uncircumcised by those who call themselves circumcised (Eph 2:11) and declares that in Christ Jesus you who once were far off have been brought near by the blood of Christ; the Ezekielian barrier of heart-circumcision is met by the Spirit's circumcision of the heart (Col 2:11) that makes all in Christ welcome in the true sanctuary"},
      {"type": "fulfillment", "target": "Rom 2:29", "note": "Uncircumcised in heart and flesh — Paul's doctrine of true circumcision resolves the barrier of Ezek 44:7: circumcision is a matter of the heart, by the Spirit, not by the letter (Rom 2:29); the uncircumcised-in-heart foreigner excluded from Ezekiel's temple is replaced by the Spirit-circumcised believer, Jew or Gentile, who is welcomed into the true sanctuary through Christ"}
    ],
    "15": [
      {"type": "allusion", "target": "Heb 7:26", "note": "The sons of Zadok who kept charge of my sanctuary when Israel went astray — they shall draw near to me to minister to me: the Zadokite priests who remained faithful while others defected are the OT type of the perfectly faithful high priest; Hebrews 7:26 applies this faithfulness to Christ: for it was indeed fitting that we should have such a high priest, holy, innocent, unstained, separated from sinners, and exalted above the heavens — the one true Zadokite who never went astray"}
    ],
    "23": [
      {"type": "allusion", "target": "1 Pet 2:9", "note": "They shall teach my people the difference between the holy and the common, and show them how to distinguish the unclean from the clean — 1 Peter 2:9 applies this priestly teaching function to the whole church: you are a royal priesthood, a holy nation, a people for his own possession, that you may proclaim the excellencies of him who called you out of darkness into his marvelous light; the Zadokite priestly discernment-teaching function is democratized in Christ and given to all his people"}
    ],
    "28": [
      {"type": "fulfillment", "target": "1 Pet 1:4", "note": "This shall be their inheritance: I am their inheritance — the Levitical priests receive no land-inheritance because YHWH himself is their portion; this is the pattern Peter applies to all believers: an inheritance that is imperishable, undefiled, and unfading, kept in heaven for you (1 Pet 1:4); God himself as inheritance is the ultimate fulfillment of the Levitical principle, now extended to all who are in Christ"},
      {"type": "fulfillment", "target": "Eph 1:14", "note": "I am their inheritance — the divine self-giving as inheritance: the Holy Spirit is the guarantee of our inheritance until we acquire possession of it (Eph 1:14); the Spirit's presence in the believer is the first-fruits installment of the final inheritance that is God himself; Ezekiel's 'I am their inheritance' is the promise that reaches its fullness when God is all in all (1 Cor 15:28)"}
    ]
  },
  "45": {
    "17": [
      {"type": "allusion", "target": "Heb 9:12", "note": "It shall be the prince's duty to provide the burnt offerings, grain offerings, and drink offerings at the feasts — to make atonement for the house of Israel: the eschatological prince who provides all the sacrificial worship is the type of Christ who entered once for all into the holy places, not by means of the blood of goats and calves but by means of his own blood, securing an eternal redemption (Heb 9:12); Christ is both the prince who provides and the sacrifice that is provided"},
      {"type": "allusion", "target": "John 11:50-52", "note": "The prince provides sin offerings to make atonement for the whole house of Israel — Caiaphas's unwitting prophecy echoes this: one man should die for the people (John 11:50); John explains this is a prophecy that Jesus would die for the nation, and not for the nation only but to gather the children of God scattered abroad; the eschatological prince's provision for the whole house becomes Christ's vicarious provision for the whole people of God"}
    ],
    "21": [
      {"type": "fulfillment", "target": "1 Cor 5:7", "note": "In the first month, on the fourteenth day, you shall keep the Passover — the eschatological Passover feast in Ezekiel's restored temple is fulfilled in Christ: our Passover lamb has been sacrificed (1 Cor 5:7); Jesus keeps the final Passover at the Last Supper (Luke 22:15-20) and declares the cup as the new covenant in his blood; the restored temple's Passover is the Lord's Supper"},
      {"type": "allusion", "target": "Heb 11:28", "note": "The Passover shall be kept — the eschatological renewal of Passover observance reaches back to the original: by faith Moses kept the Passover and sprinkled the blood, so that the destroyer of the firstborn might not touch them (Heb 11:28); the Passover's sacrificial logic — the blood that protects from the destroying angel — is the atonement logic that Christ fulfills as the once-for-all Passover sacrifice"}
    ],
    "9": [
      {"type": "allusion", "target": "Luke 4:18", "note": "Enough, O princes of Israel! Put away violence and oppression, and execute justice and righteousness — the prophetic demand for just governance by the eschatological prince connects to Jesus's inaugural Nazareth manifesto (Luke 4:18-19): good news to the poor, release to the captives, liberty to the oppressed; the just and non-oppressive prince who does not dispossess the people is the Messianic portrait Christ claims as his own mission"}
    ]
  },
  "46": {
    "1": [
      {"type": "allusion", "target": "Heb 10:19-22", "note": "The gate of the inner court facing east shall remain shut on the six working days but shall be opened on the Sabbath and on the day of the new moon — the rhythmic opening of the inner gate on sacred days, governed by the prince's approach, is the type of the permanent opening Hebrews announces: we have confidence to enter the holy places by the blood of Jesus, by the new and living way he opened for us through the curtain; the closed gate that opens only on sacred days is permanently opened by Christ's once-for-all sacrifice"}
    ],
    "9": [
      {"type": "allusion", "target": "John 10:9", "note": "Whoever enters by the north gate to worship shall go out by the south gate — no one returns through the gate by which he entered: the one-way traffic through the temple's gates is a figure of the irreversible transformation of those who enter through Christ; Jesus says: I am the gate; whoever enters through me will be saved and will come in and go out and find pasture (John 10:9); entering through Christ is a permanent transit — you do not return the way you came"}
    ],
    "16": [
      {"type": "allusion", "target": "Gal 4:7", "note": "If the prince makes a gift to any of his sons as an inheritance, it shall belong to his sons permanently — but a gift to servants reverts in the year of liberty: the contrast between the son's permanent inheritance and the servant's revocable gift is the logic Paul uses in Gal 4:7: you are no longer a slave but a son, and if a son then an heir through God; the slave's limited tenure becomes the son's permanent inheritance through adoption in Christ"},
      {"type": "allusion", "target": "John 8:35", "note": "The gift to sons is permanent inheritance; to servants it reverts at the year of liberty — Jesus makes the same distinction: the slave does not remain in the house forever; the son remains forever (John 8:35); the Jubilee-reversion of the servant's allotment contrasts with the permanent sonship; Christ came to give permanent sonship (John 1:12) where before there was only the limited tenure of servants under the law"}
    ],
    "18": [
      {"type": "allusion", "target": "Mark 10:42-45", "note": "The prince shall not take any of the people's inheritance, dispossessing them of their property — he shall give his sons inheritance from his own property: the non-dispossessing prince who gives from his own rather than taking from others is the model Jesus presents as the standard of kingdom authority; the rulers of the Gentiles lord it over them, but whoever would be great among you must be your servant; the Son of Man came not to be served but to serve and give his life as a ransom for many (Mark 10:42-45)"}
    ]
  }
}

def main():
    e = load_echo("ezekiel")
    merge_echo(e, EZEKIEL_ECHOES)
    save_echo("ezekiel", e)
    for ch in ["44", "45", "46"]:
        vv = e.get(ch, {})
        print(f"  ch{ch}: {len(vv)} verse(s) with echoes")

if __name__ == "__main__":
    main()
