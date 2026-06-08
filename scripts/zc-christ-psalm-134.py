"""
MKT Christ Commentary — Psalm 134 (3 verses — final Song of Ascents)
Run: python3 scripts/zc-christ-psalm-134.py
Key decisions:
- v2 raised-hands-toward-sanctuary → Luke 24:50 Christ raises hands in priestly
  blessing at the Ascension — the final high-priestly gesture
- v3 Creator-God-blesses-from-Zion → Gal 3:13-14 the Zion-blessing reaches
  all nations through Christ's redemption; Heb 7:7 greater blesses lesser
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
    # INTENT: Write only absent keys so re-running is safe after manual edits.
    # CHANGE? If psalms.json schema changes, update both merge_comm and PSALMS below.
    # VERIFY: python3 -c "import json; d=json.load(open('data/commentary/mkt-christ/
    #   psalms.json')); print('134 v2:',d.get('134',{}).get('2','MISSING')[:60])"
    for ch, verses in new_data.items():
        existing.setdefault(ch, {})
        for v, text in verses.items():
            existing[ch].setdefault(v, text)


PSALMS = {
    "134": {
        "1": "<p>\"Come, bless the LORD, all you servants of the LORD who stand watch in his house through the night\" — the final Song of Ascents is a brief nocturnal liturgy: pilgrims departing Jerusalem call out to the Levitical nightwatch, and the priests respond with a blessing (v3). The servants who keep watch through the night are the type of the new-covenant community's perpetual worship: Revelation 7:15 says the redeemed \"are before the throne of God and serve him day and night in his temple.\" Christ himself kept vigils in prayer — Mark 1:35: \"Very early in the morning, while it was still dark, Jesus got up... and went off to a solitary place, where he prayed.\" The nightwatch servant is a type of Christ and of every believer who watches with him.</p>",
        "2": "<p>\"Raise your hands toward the sanctuary and bless the LORD\" — the priestly hand-raising in blessing. This small verse finds its definitive NT fulfillment in Luke 24:50-51: \"When he had led them out to the vicinity of Bethany, he <strong>lifted up his hands and blessed them</strong>. While he was blessing them, he left them and was taken up into heaven.\" The raised hands toward the sanctuary in Psalm 134:2 are the hands Christ raises at the Ascension — the last gesture of the incarnate Son is the priestly blessing of his people, the high-priestly act that continues forever since \"he always lives to make intercession for them\" (Heb 7:25).</p>",
        "3": "<p>\"May the LORD, maker of heaven and earth, bless you from Zion\" — the priestly response: the Creator-God's blessing from the holy city. Hebrews 7:7: \"without doubt the lesser is blessed by the greater.\" Christ is the greater who blesses — the one through whom the Creator-God's blessing now flows to all people. Galatians 3:13-14: \"Christ redeemed us from the curse of the law by becoming a curse for us... He redeemed us in order that the blessing given to Abraham might come to the Gentiles through Christ Jesus.\" The Zion-blessing of Psalm 134:3 is the Abrahamic blessing that Christ, by his death and resurrection, extends from Zion to all nations — \"maker of heaven and earth\" giving his Son so that every human creature might be blessed.</p>"
    }
}


def main():
    existing = load_comm("mkt-christ", "psalms")
    before = sum(len(v) for v in existing.values())
    merge_comm(existing, PSALMS)
    after = sum(len(v) for v in existing.values())
    save_comm("mkt-christ", "psalms", existing)
    print(f"{len(existing)} chapters, {after} verse entries total (+{after - before} new)")
    entry = existing.get("134", {}).get("2", "MISSING")
    print(f"  Ps 134:2 — {'OK' if 'lifted up his hands' in entry else 'CHECK'}")


if __name__ == "__main__":
    main()
