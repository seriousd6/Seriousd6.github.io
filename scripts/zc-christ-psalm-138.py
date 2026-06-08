"""
MKT Christ Commentary — Psalm 138 (8 verses — David's thanksgiving)
Run: python3 scripts/zc-christ-psalm-138.py
Key decisions:
- v1 praise-before-heavenly-assembly → Heb 2:12 Christ sings in the congregation
- v2 'exalted your promise above even your own name' → John 1:1 the pre-existent
  Word; the promise supremely exalted = the Word become flesh
- v4 all-kings-of-earth-will-praise → Phil 2:10-11; Rev 21:24
- v6 pays-attention-to-humble / perceives-arrogant-from-afar → Luke 1:52;
  Matt 23:12 Christ's inversion of human status
- v7 right-hand-rescues → Acts 2:24 impossible to hold by death; resurrection
- v8 LORD-will-fulfill-his-purpose → Phil 1:6 he who began will complete
"""
import json, pathlib

ROOT = pathlib.Path(__file__).parent.parent


def load_comm(layer, book):
    p = ROOT / "data" / "commentary" / layer / f"{book}.json"
    return json.loads(p.read_text()) if p.exists() else {}


def save_comm(layer, book, data):
    p = ROOT / "data" / "commentary" / layer / f"{book}.json"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=2))


def merge_comm(existing, new_data):
    # INTENT: Write only absent keys — safe to re-run after manual edits.
    # CHANGE? If psalms.json schema changes, update merge_comm and PSALMS below.
    # VERIFY: python3 -c "import json; d=json.load(open('data/commentary/mkt-christ/
    #   psalms.json')); print('138 v7:',d.get('138',{}).get('7','MISSING')[:60])"
    for ch, verses in new_data.items():
        existing.setdefault(ch, {})
        for v, text in verses.items():
            existing[ch].setdefault(v, text)


PSALMS = {
    "138": {
        "1": "<p>\"I will praise you, O LORD, with all my heart; in the presence of the <strong>heavenly assembly</strong> I will sing your praises\" — the wholehearted praise before the divine council. Hebrews 2:12 (quoting Ps 22:22): \"I will declare your name to my brothers and sisters; in the <strong>assembly I will sing your praises</strong>.\" Hebrews applies this to Christ himself — the wholehearted praise of Psalm 138:1 in the presence of the heavenly assembly is Christ's own song in the congregation of his people. He who is praised is also the one who leads the praise.</p>",
        "2": "<p>\"I will bow down toward your holy temple and praise your name for your steadfast love and faithfulness; for you have <strong>exalted your promise above even your own name</strong>\" — the divine word given supremacy above the divine name itself. John 1:1-2: \"In the beginning was the <strong>Word</strong>, and the Word was with God, and the Word was God.\" The promise/word that YHWH exalts above his own name is the pre-existent Logos — and the Incarnation is the supreme exaltation of that Word: \"The Word became flesh and made his dwelling among us\" (John 1:14). God's faithfulness to his promised Word reaches its highest expression when the Word becomes a person.</p>",
        "3": "<p>\"On the day I called out, you answered me; you filled my soul with bold strength\" — the answered prayer that brings courage. Hebrews 5:7: \"During the days of Jesus's life on earth, he offered up prayers and petitions with fervent cries and tears to the one who could save him from death, and <strong>he was heard</strong> because of his reverent submission.\" The Gethsemane prayer of Christ — the supreme day of calling out — was answered not by removal of the cross but by the resurrection that followed: the boldness given to the Son's prayer is the boldness of the resurrection (Acts 4:13: \"they saw the courage of Peter and John\").</p>",
        "4": "<p>\"All the kings of the earth will praise you, O LORD, when they hear the words you have spoken\" — the universal royal praise. Philippians 2:10-11: \"at the name of Jesus every knee should bow, in heaven and on earth and under the earth, and every tongue acknowledge that Jesus Christ is Lord.\" Revelation 21:24: \"The kings of the earth will bring their splendor into\" the new Jerusalem. The praise of all earth's kings in Psalm 138:4 is the eschatological worship of Christ as Lord — when the gospel reaches the ends of the earth, kings hear and respond.</p>",
        "5": "<p>\"They will sing of the paths of the LORD, for the glory of the LORD is great\" — the kings singing of YHWH's ways. The \"paths of the LORD\" that the kings sing about are the ways of God revealed supremely in the gospel: Romans 11:33: \"Oh, the depth of the riches of the wisdom and knowledge of God! How unsearchable his judgments, and his paths beyond tracing out!\" The kings who come to sing of the LORD's paths are the kings whose splendor enters the new Jerusalem (Rev 21:24) — drawn by the glory of the Lamb who is the city's light.</p>",
        "6": "<p>\"Though the LORD is exalted, he pays attention to the humble; but the arrogant he perceives from a distance\" — the divine inversions of status. Luke 1:52: \"He has brought down rulers from their thrones but has lifted up the humble.\" Matthew 23:12: \"For those who exalt themselves will be humbled, and those who humble themselves will be exalted.\" Christ embodies this perfectly: the most exalted one (Phil 2:9) took the most humble form (Phil 2:7-8: \"made himself nothing, taking the very nature of a servant\"). The principle of Psalm 138:6 is not merely a divine policy but a Christological pattern — God pays attention to the humble because his Son became the humblest of all.</p>",
        "7": "<p>\"Even when I walk through terrible trouble, you keep me alive; you reach out your hand against the fury of my enemies, and your <strong>right hand</strong> rescues me\" — divine rescue in the extremity of death. Acts 2:24: \"But God raised him from the dead, freeing him from the agony of death, because it was <strong>impossible for death to keep its hold on him</strong>.\" The right hand that rescues in Psalm 138:7 is the Father's hand that raises the Son from the dead and seats him at his right hand (Acts 2:33). The terrible trouble is the cross; the right-hand rescue is the resurrection. Christ walks through the extreme trouble of death and is kept alive by the God who cannot abandon his own Son.</p>",
        "8": "<p>\"The LORD will <strong>fulfill his purpose for me</strong>; your steadfast love, O LORD, endures forever — do not abandon what your hands have made\" — the confidence that God will complete what he has begun. Philippians 1:6: \"he who began a good work in you will carry it on to <strong>completion until the day of Christ Jesus</strong>.\" Romans 8:28: \"in all things God works for the good of those who love him, who have been called according to his purpose.\" The divine purpose-fulfillment of Psalm 138:8 is the guarantee that every redeemed person prays in Christ: the steadfast love that endures forever is the love that will not leave unfinished what the hands of God have made — in creation or in the new creation.</p>"
    }
}


def main():
    existing = load_comm("mkt-christ", "psalms")
    before = sum(len(v) for v in existing.values())
    merge_comm(existing, PSALMS)
    after = sum(len(v) for v in existing.values())
    save_comm("mkt-christ", "psalms", existing)
    print(f"{len(existing)} chapters, {after} verse entries total (+{after - before} new)")
    for v, kw in [("1", "assembly"), ("2", "Word"), ("7", "impossible"), ("8", "completion")]:
        entry = existing.get("138", {}).get(v, "MISSING")
        print(f"  Ps 138:{v} — {'OK' if kw.lower() in entry.lower() else 'CHECK'}")


if __name__ == "__main__":
    main()
