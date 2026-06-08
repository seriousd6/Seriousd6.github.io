"""
MKT Christ Commentary — Isaiah 27 (13 verses)
Run: python3 scripts/zc-christ-isaiah-27.py
Key decisions:
- v1: Leviathan slain — DIRECT type: Rev 12:9 / 20:2-3 / Col 2:15
  (the dragon defeated by Christ at the cross and finally at the end of the age)
- vv2-6: The Beautiful Vineyard — the reversed Isaiah 5 vineyard; YHWH now
  guards and waters the restored vine; John 15:1-5 (Christ the true vine);
  the eschatological restoration answers the judgment of Isa 5:1-7
- v9: kāpar (H3722, atone/cover) — the guilt of Jacob covered; the atonement-
  language of judgment; Heb 9:22 (without shedding of blood no forgiveness);
  v9's stones of altar ground to dust = removal of false worship
- v12: Great harvest — Matt 13:30 / Rev 14:14-16 (the end-of-age grain harvest)
- v13: Great trumpet — Matt 24:31 / 1 Cor 15:52 / 1 Thess 4:16
  (the last trumpet gathering the elect)
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
    # CHANGE? If isaiah.json schema changes, update merge_comm and ISAIAH dict below.
    # VERIFY: python3 -c "import json; d=json.load(open('data/commentary/mkt-christ/
    #   isaiah.json')); print('Isa 27 v1:',d.get('27',{}).get('1','MISSING')[:80])"
    for ch, verses in new_data.items():
        existing.setdefault(ch, {})
        for v, text in verses.items():
            existing[ch].setdefault(v, text)


ISAIAH = {
    "27": {
        "1": "<p>\"In that day the LORD with his hard and great and strong sword will punish Leviathan the fleeing serpent, Leviathan the twisting serpent, and he will slay the dragon that is in the sea\" — the cosmic battle: YHWH's sword against Leviathan, the primordial sea-dragon of ancient Near Eastern myth (cf. Job 41; Ps 74:14; 89:10). The three descriptions (fleeing, twisting, dragon-of-the-sea) denote the chaos-force in all its manifestations. Revelation 12:9: \"The great dragon was hurled down — that ancient serpent called the devil, or Satan.\" 20:2-3: \"He seized the dragon, that ancient serpent, who is the devil, or Satan, and bound him for a thousand years.\" Colossians 2:15: \"having disarmed the powers and authorities, he made a public spectacle of them, triumphing over them by the cross.\" The sword that slays Leviathan in Isaiah 27:1 is the cross — the instrument by which Christ disarms the primordial serpent that has held creation in thrall since Genesis 3.</p>",
        "2": "<p>\"In that day: 'A pleasant vineyard, sing of it!'\" — the dramatic reversal of Isaiah 5's Song of the Vineyard. Isaiah 5 began with a song about the vineyard that yielded wild grapes and was destroyed; Isaiah 27 opens a new song about the vineyard that is now <em>pleasant</em> (<em>ḥemed</em>). The structural echo is deliberate: same form (a song about a vineyard), opposite content (destruction vs. restoration). John 15:1-5: \"I am the true vine, and my Father is the gardener.\" The Beautiful Vineyard of Isaiah 27 is the vineyard as it becomes through Christ — the true vine who produces genuine fruitfulness where Israel, the failed vine, produced only wild grapes. The song of restoration is the song of the true vine.</p>",
        "3": "<p>\"I, the LORD, am its keeper; every moment I water it. Lest anyone punish it, I keep it night and day\" — YHWH as the diligent vineyard-keeper: watering continuously, guarding unceasingly. The contrast with Isaiah 5:6 (\"I will command the clouds that they rain no rain upon it\") is total: there the rain was withheld as judgment; here YHWH waters \"every moment.\" John 10:28-29: \"I give them eternal life, and they shall never perish; no one will snatch them out of my hand. My Father, who has given them to me, is greater than all; no one can snatch them out of my Father's hand.\" The unceasing guarding of the vineyard in Isaiah 27:3 is the security of the sheep in the Father's and Son's hands — the restoration-vineyard is the community that cannot be lost because its Keeper never sleeps.</p>",
        "4": "<p>\"I have no wrath. Would that I had thorns and briers to battle! I would march against them, I would burn them up together\" — the remarkable divine self-restraint: YHWH declares no wrath against the restored vineyard; the only thing he would attack is the thorns and briers (the enemy). The thorns that were the judgment of Isaiah 5:6 (\"briers and thorns shall grow up\") are now the targets, not the contents, of the vineyard. Galatians 3:13: \"Christ redeemed us from the curse of the law by becoming a curse for us.\" The crown of thorns on Christ's head is the judgment-thorns taken into Christ himself — he bears the briers of the curse so that the restored vineyard is free of them. The wrath that YHWH says he has none of (toward his vineyard) is the wrath that Christ absorbed at the cross.</p>",
        "5": "<p>\"Or let them lay hold of my protection, let them make peace with me, let them make peace with me\" — the double invitation to peace: the repeated \"make peace with me\" (<em>yaʿăśeh šālôm lî</em>) is an urgent, gracious offer. The enemy (the thorns and briers of v4) is invited to lay hold of divine protection rather than face divine fire. Romans 5:1: \"Therefore, since we have been justified through faith, we have peace with God through our Lord Jesus Christ.\" Ephesians 2:14: \"For he himself is our peace.\" The double peace-invitation of Isaiah 27:5 is fulfilled in the double grace of the gospel: Christ both <em>is</em> our peace (Eph 2:14) and <em>makes</em> peace through the blood of his cross (Col 1:20). The invitation is irresistible in its urgency and genuine in its offer.</p>",
        "6": "<p>\"In days to come Jacob shall take root, Israel shall blossom and put forth shoots and fill the whole world with fruit\" — the eschatological fruitfulness: from the covenant people flowing outward to fill the whole world (<em>tēbēl</em>, the inhabited earth). The vocabulary is horticultural, but the scope is universal. John 15:5: \"I am the vine; you are the branches. If you remain in me and I in you, you will bear much fruit.\" John 15:16: \"I chose you and appointed you so that you might go and bear fruit — fruit that will last.\" Matthew 28:19: \"Therefore go and make disciples of all nations.\" The \"fill the whole world with fruit\" of Isaiah 27:6 is the commission of Matthew 28 — the restored vineyard/vine produces fruit that spreads to the nations through the missionary movement rooted in Christ.</p>",
        "7": "<p>\"Has he struck them as he struck those who struck them? Or have they been slain as their slayers were slain?\" — the measured judgment of Jacob compared to the full judgment of their oppressors. The rhetorical question expects the answer \"no\": YHWH's discipline of his people is milder than his full judgment of the nations that oppressed them. Hebrews 12:5-7: \"'My son, do not make light of the Lord's discipline, and do not lose heart when he rebukes you, because the Lord disciplines the one he loves.'\" The distinction between discipline and judgment is the distinction between covenant chastisement (which produces righteousness) and final condemnation (which does not). Christ's suffering was not discipline but substitutionary judgment — he received the full blow (\"as their slayers were slain\") so that his people receive only the measured discipline of the beloved.</p>",
        "8": "<p>\"Measure by measure, by exile you contended with them; he removed them with his fierce breath in the day of the east wind\" — the measured nature of the exile as discipline: not annihilation but contention (<em>rîb</em>, as in a legal dispute) administered by measure. The east wind (<em>rûaḥ qādîm</em>) is both the literal sirocco that desiccates and the instrument of divine judgment (cf. Exod 10:13; Jer 18:17). The breath/wind (<em>rûaḥ</em>) of YHWH blows in judgment — but the same <em>rûaḥ</em> breathes life in John 20:22 (\"he breathed on them and said, 'Receive the Holy Spirit'\"). The fierce breath of judgment becomes the life-giving breath of Pentecost: same divine <em>rûaḥ</em>, transformative direction.</p>",
        "9": "<p>\"Therefore by this the guilt of Jacob will be atoned for (<em>yĕkuppar</em>), and this will be the full fruit of the removal of his sin: when he makes all the stones of the altars like chalkstones crushed to pieces, no Asherah poles or incense altars will remain standing\" — the atonement (<em>kāpar</em>, H3722) language of covenant restoration: the guilt covered by the purging of false worship. Hebrews 9:22: \"Without the shedding of blood there is no forgiveness.\" The crushed altar-stones of Isaiah 27:9 are the removal of the competing loyalties — atonement is not merely the covering of guilt but the transformation of the worshiper, the end of divided allegiance. Colossians 3:5: \"Put to death, therefore, whatever belongs to your earthly nature: sexual immorality, impurity, lust, evil desires and greed, which is idolatry.\" The altar-crushing of Isaiah 27:9 is the mortification of idolatry that follows from atonement through Christ.</p>",
        "10": "<p>\"For the fortified city is solitary, a habitation deserted and forsaken, like the wilderness; there the calf grazes; there it lies down and strips its branches\" — the abandoned city: the strong place become a pasture for calves. The same city that was fortified is now grazed by cattle — the power of human construction reduced to a meadow. Revelation 18:2: \"Babylon the great has fallen!... She has become a dwelling for demons and a haunt for every impure spirit... a haunt for every unclean bird.\" The abandoned fortified city of Isaiah 27:10 is the type of every fallen empire — cities built on human power become wildernesses when YHWH withdraws his presence. Only the city whose builder and maker is God (Heb 11:10) will endure.</p>",
        "11": "<p>\"When its boughs are dry, they are broken; women come and make a fire of them. For this is a people without discernment; therefore he who made them will not have compassion on them; he who formed them will show them no favor\" — the dry branches broken for fuel: the judgment-language of withered wood. John 15:6: \"If you do not remain in me, you are like a branch that is thrown away and withers; such branches are picked up, thrown into the fire and burned.\" Christ takes the very image of Isaiah 27:11 and applies it to those who do not abide in him as the true vine — the dry branches broken for fire are the judgment on those who remain outside the restored vineyard. The \"people without discernment\" (<em>ʾên bînôt lô</em>) are those who cannot perceive the vine that is their only source of life.</p>",
        "12": "<p>\"In that day from the River Euphrates to the Brook of Egypt the LORD will thresh out the grain one by one, and you, O people of Israel, will be gathered one by one\" — the great harvest: the divine threshing across the whole promised land (from Euphrates to Egypt's border = the full Abrahamic territory), gathering the covenant people grain by grain. Matthew 13:30: \"Let both grow together until the harvest. At that time I will tell the harvesters: First collect the weeds and tie them in bundles to be burned; then gather the wheat and bring it into my barn.\" Revelation 14:14-16: \"the earth was harvested.\" The great threshing of Isaiah 27:12 is the eschatological harvest that Christ describes in his parables and John depicts in Revelation — gathering \"one by one\" is the personal, specific gathering of every individual whom the Father has given to the Son (John 6:39).</p>",
        "13": "<p>\"And in that day a great trumpet will be blown, and those who were lost in the land of Assyria and those who were driven out to the land of Egypt will come and worship the LORD on the holy mountain at Jerusalem\" — the great trumpet that ends the exile and gathers the scattered. Matthew 24:31: \"And he will send his angels with a loud trumpet call, and they will gather his elect from the four winds, from one end of the heavens to the other.\" 1 Corinthians 15:52: \"in a flash, in the twinkling of an eye, at the last trumpet. For the trumpet will sound, the dead will be raised imperishable, and we will be changed.\" 1 Thessalonians 4:16: \"For the Lord himself will come down from heaven... with the trumpet call of God, and the dead in Christ will rise first.\" The great trumpet of Isaiah 27:13 that ends the Assyrian and Egyptian exiles is the type of the last trumpet that ends the entire exile of death — gathering the scattered elect to the holy mountain of the new Jerusalem (Rev 21:10).</p>"
    }
}


def main():
    existing = load_comm("mkt-christ", "isaiah")
    before = sum(len(v) for v in existing.values())
    merge_comm(existing, ISAIAH)
    after = sum(len(v) for v in existing.values())
    save_comm("mkt-christ", "isaiah", existing)
    print(f"{len(existing)} chapters, {after} verse entries total (+{after - before} new)")
    for v, kw in [("1", "dragon"), ("6", "fruit"), ("9", "atone"), ("13", "trumpet")]:
        entry = existing.get("27", {}).get(v, "MISSING")
        print(f"  Isa 27:{v} — {'OK' if kw.lower() in entry.lower() else 'CHECK'}")
    ch = existing.get("27", {})
    missing = [str(i) for i in range(1, 14) if str(i) not in ch]
    print(f"  Missing verses: {missing if missing else 'none'}")


if __name__ == "__main__":
    main()
