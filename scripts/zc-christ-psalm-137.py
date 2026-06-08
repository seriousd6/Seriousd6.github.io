"""
MKT Christ Commentary — Psalm 137 (9 verses — By the rivers of Babylon)
Run: python3 scripts/zc-christ-psalm-137.py
Key decisions:
- v1 weeping-over-Zion → Luke 19:41 Christ weeps over Jerusalem — the exile
  grief is his own grief
- v2-4 harps-silenced-in-exile → Rev 5:8-9 the new song harps before the Lamb
  are the resurrection of the exilic silence
- v5-6 Jerusalem-fidelity → Heb 12:22 heavenly Jerusalem as the true goal;
  Gal 4:26 Jerusalem-that-is-above
- v7 Remember-what-Edom-did → Rev 6:10 martyrs' cry for justice; eschatological
  justice through Christ
- v8-9 Babylon-destruction / smashing-the-little-ones — the hardest verses:
  treated as imprecatory prayer awaiting divine eschatological justice
  (Rev 17-18 fall of Babylon; 2 Thess 1:6-8); NOT a command to violence
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
    #   psalms.json')); print('137 v1:',d.get('137',{}).get('1','MISSING')[:60])"
    for ch, verses in new_data.items():
        existing.setdefault(ch, {})
        for v, text in verses.items():
            existing[ch].setdefault(v, text)


PSALMS = {
    "137": {
        "1": "<p>\"By the rivers of Babylon we sat down and wept when we remembered Zion\" — the Exile's most famous opening image: the community of mourners at the rivers of their captivity, weeping for what they have lost. Luke 19:41: \"As he approached Jerusalem and saw the city, <strong>he wept over it</strong>.\" Christ's weeping over Jerusalem is the Zion-grief of Psalm 137:1 taken into the heart of the Son — he is the one who loves Jerusalem most perfectly and mourns most deeply over its coming destruction. The exile-tears of Babylon become the Gethsemane-tears of the Son who bears the full weight of Israel's tragedy.</p>",
        "2": "<p>\"We hung up our harps in the willow trees there\" — the silencing of the worship instruments, hung up and unused in the alien land. Revelation 5:8: \"the four living creatures and the twenty-four elders fell down before the Lamb. Each one had a harp and they were holding golden bowls full of incense, which are the prayers of God's people.\" The harps taken down from the willows of Babylon are the harps lifted again before the Lamb in heaven — Christ's resurrection and ascension makes possible the new song that the exile's silence was waiting for. The hung-up harp of Psalm 137:2 is the harp that sounds again in Revelation 5:9.</p>",
        "3": "<p>\"Our captors demanded that we sing for them; those who had ruined us wanted entertainment: 'Sing us a song of Zion!'\" — the taunt of the oppressors demanding sacred songs as entertainment. Matthew 27:29-31: the soldiers mock Jesus, dressing him in a purple robe, placing a crown of thorns on his head, calling \"Hail, king of the Jews!\" — the sacred is made into an entertainment spectacle. Christ enters fully into the experience of the community that is mocked when it is most vulnerable: the one who could summon legions of angels submits to the captor's taunt, participating in Israel's exile-humiliation.</p>",
        "4": "<p>\"But how could we sing the LORD's song in a foreign land?\" — the theological crisis: worship is tied to place. The question that the exile poses becomes the question the Incarnation answers: God comes to the foreign land himself. John 1:11: \"He came to his own.\" Christ enters the foreign land of human exile from God — \"the Word became flesh and made his dwelling among us\" (John 1:14) — and in doing so, makes it possible to sing the LORD's song in every land. The church sings in Babylon, in Rome, in every empire, because Christ has joined the exile and transformed it from within.</p>",
        "5": "<p>\"If I forget you, O Jerusalem, may my right hand lose all skill\" — the psalmist's vow of covenant fidelity to Jerusalem. Galatians 4:26: \"the Jerusalem that is above is free, and she is our mother.\" Hebrews 12:22: \"you have come to Mount Zion and to the city of the living God, the heavenly Jerusalem.\" The passionate fidelity to Jerusalem in Psalm 137:5 is fulfilled in Christ's fidelity to the heavenly city — he gives his life for the city of God (Rev 21:2: \"I saw the Holy City, the new Jerusalem, coming down out of heaven from God\"). The hand that would lose its skill is the hand Christ stretched wide at Calvary for the city he loves.</p>",
        "6": "<p>\"If I do not hold you in memory, may my tongue stick to the roof of my mouth — if I do not place Jerusalem above my greatest delight\" — the supreme devotion to Zion. The church's supreme delight is the heavenly Jerusalem where Christ reigns and to which his people are headed: Hebrews 11:10 describes the patriarchs as those \"looking forward to the city that has foundations, whose designer and builder is God.\" Philippians 3:20: \"our citizenship is in heaven.\" The tongue that would stick to the roof of the mouth is the tongue that must confess Jesus Christ as Lord (Phil 2:11) — and that confession is the new covenant's Jerusalem-fidelity.</p>",
        "7": "<p>\"Remember, O LORD, what Edom's sons did on the day Jerusalem fell — how they shouted, 'Tear it down! Tear it down to its very foundations!'\" — the cry for divine justice against those who cheered Jerusalem's destruction. Revelation 6:10: the martyrs under the altar cry \"How long, Sovereign Lord, holy and true, until you judge the inhabitants of the earth and avenge our blood?\" The imprecatory prayer of Psalm 137:7 is the prayer of the martyrs — those who have suffered injustice appealing to the Judge who will make all wrongs right. Christ is that Judge (Acts 17:31; 2 Thess 1:6-8) who \"remembered\" every act of injustice done to his people and will bring it to account.</p>",
        "8": "<p>\"O Babylon, marked for destruction — how happy will be the one who pays you back for what you did to us!\" — the longing for Babylon's fall. Revelation 18:6, 20: \"Give back to her as she has given; pay her back double for what she has done... Rejoice over her, you heavens! Rejoice, you people of God!\" The Revelation of John directly fulfills the imagery of Psalm 137:8 — \"Babylon the Great\" falls (Rev 17-18), and heaven rejoices. The prayer for Babylon's destruction is the prayer for the eschatological fall of every anti-God system, executed not by human vengeance but by divine judgment through Christ.</p>",
        "9": "<p>\"Blessed is he who takes your little ones and smashes them against the rocks\" — the most difficult verse in the Psalter: the raw cry for total retributive destruction. This is not a command or a model for human action, but a prayer for divine justice: the speaker calls on God, not themselves, to repay. Psalm 2:9: the Messianic King \"will dash them to pieces like pottery\" with his iron scepter — the eschatological judgment language overlaps. Revelation 2:27: the overcoming church will \"rule them with an iron scepter and dash them to pieces like pottery.\" The brutal imagery of Psalm 137:9 is the raw edge of the Psalter's cry for justice; Christ as the final Judge is the one who will execute the justice the psalmist can only cry for and leave to God.</p>"
    }
}


def main():
    existing = load_comm("mkt-christ", "psalms")
    before = sum(len(v) for v in existing.values())
    merge_comm(existing, PSALMS)
    after = sum(len(v) for v in existing.values())
    save_comm("mkt-christ", "psalms", existing)
    print(f"{len(existing)} chapters, {after} verse entries total (+{after - before} new)")
    for v, kw in [("1", "wept"), ("2", "Lamb"), ("7", "judge"), ("8", "Babylon")]:
        entry = existing.get("137", {}).get(v, "MISSING")
        print(f"  Ps 137:{v} — {'OK' if kw.lower() in entry.lower() else 'CHECK'}")


if __name__ == "__main__":
    main()
