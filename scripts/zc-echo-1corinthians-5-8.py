"""
Echo layer — 1 Corinthians chapters 5–8
Run: python3 scripts/zc-echo-1corinthians-5-8.py
Output: data/echoes/1corinthians.json (adds ch5-8)

1 Corinthians 5–8 covers: community discipline and the incest case (ch.5), lawsuits and sexual
ethics including the body-as-temple theology (ch.6), Paul's extended teaching on marriage, celibacy,
and the eschatological frame of "the time is short" (ch.7), and the food-offered-to-idols question
grounded in the Shema and the weak-conscience ethic (ch.8).

Parallels file absorbed:
- 5:7: prophecy-source → Exod 12:3-7 (Passover lamb) → type/fulfillment

Key classification decisions:
- 5:7 classified as "type" not "fulfillment": Paul draws the analogy explicitly but Christ as
  Passover is the NT antitype of the OT type; it is structural anticipation, not a predictive text
  claiming literal fulfillment
- 5:13 classified as "quote" of Deut 17:7 (the exact Deuteronomic formula "expel the wicked
  from among you" appears five times in Deuteronomy and Paul uses it verbatim in LXX form)
- 6:2 (saints judging the world) → allusion to Dan 7:22, not fulfillment: Paul is applying a
  principle from Daniel's vision, not claiming it is "now fulfilled"
- 6:16 classified as "quote" of Gen 2:24 (Paul explicitly cites it with "for it is said")
- 8:4-6 Shema application: classified as allusion/shadow since Paul does not explicitly cite
  Deut 6:4; the theological echo is unmistakable but it is structural reapplication, not citation
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

CORINTHIANS_ECHOES = {
  "5": {
    "1": [
      {"type": "allusion", "target": "Lev 18:8", "note": "Levitical law explicitly prohibits uncovering the nakedness of a father's wife (Lev 18:8; Deut 22:30; 27:20) — the sin Paul reports at Corinth is not merely socially scandalous but falls under the Holiness Code's specific prohibitions. Paul's phrase 'of a kind that even pagans do not tolerate' underscores that the church has fallen below even Gentile moral standards on a matter where Torah was explicit."}
    ],
    "6": [
      {"type": "allusion", "target": "Exod 12:15", "note": "The Passover requirement to remove all leaven from the house before the feast (Exod 12:15; 13:7) — Paul uses the Passover-leaven image to argue that just as leaven corrupts the whole batch, tolerated sin in the community corrupts the whole. The image is apt because the Passover/leaven removal follows immediately (v.7): Christ the Passover lamb has been sacrificed, so the community must remove the old leaven."}
    ],
    "7": [
      {"type": "type", "target": "Exod 12:3-7", "note": "The Passover lamb — selected beforehand, unblemished, slaughtered at twilight on Nisan 14, its blood applied for protection — is the OT type for which Christ is the antitype. Paul makes this explicit: 'Christ, our Passover lamb, has been sacrificed.' The structural precision is deliberate: selection (the eternal plan), without blemish (sinlessness), slaughtered at Passover (the timing of the crucifixion), blood applied (saving effect)."},
      {"type": "allusion", "target": "Isa 53:7", "note": "The Servant led like a lamb to slaughter, silent before its shearers — the Isaianic Servant as a lamb led to death enriches the Passover-lamb typology Paul invokes; both converge on Christ as the one who dies for others' deliverance without resistance."}
    ],
    "8": [
      {"type": "allusion", "target": "Exod 12:19-20", "note": "The command to eat nothing leavened during the seven days of the Feast of Unleavened Bread — Paul extends the Passover metaphor into an ethics of sustained purity: the 'festival' the community now keeps is not a single calendar event but a life lived in the sincerity and truth that the unleaven bread signified. The leaven of malice and wickedness maps onto the literal leaven removed at Passover."}
    ],
    "13": [
      {"type": "quote", "target": "Deut 17:7", "note": "Paul's closing command 'expel the wicked person from among you' is a verbatim citation (LXX) of the Deuteronomic formula that appears five times in Deuteronomy (Deut 13:5; 17:7; 19:19; 21:21; 22:21-24; 24:7) as the consequence for capital covenant sins. Paul applies Israel's covenant-community purification legislation directly to the church, presenting the community as the covenant assembly that must maintain the same holiness standards."}
    ]
  },
  "6": {
    "2": [
      {"type": "allusion", "target": "Dan 7:22", "note": "Daniel's vision: 'judgment was given in favor of the holy ones of the Most High' — the saints receiving judicial authority at the eschatological judgment provides the theological premise for Paul's rhetorical question. If the covenant community will share in judging the world at the final judgment (as Daniel's vision implies), it is absurd for them to take trivial disputes before those who will themselves be judged."}
    ],
    "9": [
      {"type": "allusion", "target": "Ezek 22:9-11", "note": "Ezekiel's indictment of Israel includes the same cluster of sins that Paul lists — sexual immorality, adultery, exploitation — as the reason for the covenant community's judgment. Paul's vice list stands in the prophetic tradition of cataloguing covenant failure; but his framing ('do not be deceived') warns that the new covenant community is not immune to the same pattern."}
    ],
    "11": [
      {"type": "allusion", "target": "Ezek 36:25-27", "note": "Ezekiel's new covenant promise: 'I will sprinkle clean water on you and you will be clean; I will give you a new heart and put a new spirit in you' — Paul's triad 'washed, sanctified, justified' describes the same transforming divine act. The washing corresponds to Ezekiel's sprinkling; the sanctification to the new heart; the Spirit of God to the Spirit placed within. The new covenant transformation is applied experientially to the Corinthians' conversion."}
    ],
    "16": [
      {"type": "quote", "target": "Gen 2:24", "note": "Paul explicitly cites Gen 2:24 ('for it is said: the two will become one flesh') to establish that sexual union creates a bodily bond that transcends the transaction. The creation-order text that defined marriage (one flesh union of husband and wife) is extended by Paul to any sexual union — the same relational bond is created, which makes sexual immorality a misuse of what God designed for covenant marriage."}
    ],
    "19": [
      {"type": "allusion", "target": "Exod 25:8", "note": "God's command to make the Tabernacle 'so that I may dwell among them' — the body-as-temple teaching applies to individual believers the dwelling-presence that the Tabernacle and Temple enacted corporately for Israel. Where the Shekinah filled the Tabernacle (Exod 40:34-35) and Temple (1 Kgs 8:10-11), the Holy Spirit now inhabits the believer's body; the same holiness logic applies."},
      {"type": "allusion", "target": "Ezek 37:27", "note": "My dwelling place will be with them; I will be their God and they will be my people — Ezekiel's new covenant vision of God's dwelling among his people is fulfilled not in a rebuilt physical temple but in the Spirit's residence in the community of believers. Paul's body-as-temple argument presupposes this eschatological fulfillment of Ezekiel's promise."}
    ],
    "20": [
      {"type": "allusion", "target": "Isa 43:1-3", "note": "God's declaration to redeemed Israel: 'Fear not, for I have redeemed you; I have summoned you by name, you are mine. I will give Egypt for your ransom...' — the redemption-price language ('bought at a price') echoes the Exodus ransom theology where God pays a price to reclaim what belongs to him. The Corinthians' bodies belong to God not merely by creation but by redemption; the purchase price is the blood of Christ (1 Pet 1:18-19)."}
    ]
  },
  "7": {
    "4": [
      {"type": "allusion", "target": "Exod 21:10", "note": "The Mosaic law requiring a husband not to deprive his wife of food, clothing, and marital rights (Exod 21:10 — the only OT reference to the conjugal obligation within marriage) — Paul extends this mutual-obligation logic to both spouses equally, a significant egalitarian development of the covenant principle. The marital duty is now framed as mutual authority rather than one-directional obligation."}
    ],
    "10": [
      {"type": "allusion", "target": "Mal 2:16", "note": "The LORD's declaration that he hates divorce (Mal 2:16) and his warning that breaking covenant with the wife of one's youth is faithlessness — Paul's appeal to the Lord's command on marriage grounds it in the prophetic tradition that presented marriage as a covenant modeled on YHWH's covenant with Israel. The Malachi background gives weight to what Paul presents as the Lord's direct instruction rather than his own opinion."}
    ],
    "19": [
      {"type": "allusion", "target": "Deut 10:16", "note": "Moses's command to circumcise the foreskin of your heart — the prophets consistently subordinated the physical sign to the covenantal reality it was meant to mark (Jer 4:4; Deut 30:6); Paul's declaration that circumcision counts for nothing echoes and makes explicit what the prophetic tradition implied. What matters is keeping God's commands — the same conclusion Deuteronomy drew."},
      {"type": "allusion", "target": "1 Sam 15:22", "note": "Samuel's declaration to Saul — 'To obey is better than sacrifice, to heed is better than the fat of rams' — stands behind Paul's principle that ritual marks (circumcision) are subordinate to covenant obedience. The prophetic tradition consistently prioritized interior covenant faithfulness over external religious markers."}
    ],
    "23": [
      {"type": "allusion", "target": "Lev 25:42", "note": "God's instruction to Israel regarding slaves: 'because the Israelites are my servants, whom I brought out of Egypt, they are not to be sold as slaves' — Paul reverses the slave-free status hierarchy using the same principle: those who have been redeemed by God (brought out at a price) belong to God as his servants, not to be re-enslaved to human masters. The Jubilee-redemption logic of Leviticus 25 applies to the new covenant community."}
    ],
    "29": [
      {"type": "allusion", "target": "Zeph 1:14", "note": "The great day of the LORD is near, near and hastening fast — Paul's 'the time is short' invokes the eschatological urgency of the Day of the LORD tradition; the crisis that shapes the marriage advice of chapter 7 is the same compressed eschatological horizon that the prophets announced. The practical counsel about marriage is shaped by the prophetic sense that the present age is ending."}
    ],
    "31": [
      {"type": "allusion", "target": "Isa 51:6", "note": "Lift up your eyes to the heavens, look at the earth beneath; the heavens will vanish like smoke, the earth will wear out like a garment — the transience of the present world-form that Paul announces ('the present form of this world is passing away') rests on the prophetic conviction, rooted in Isaiah's eschatology, that the existing created order is giving way to the new creation."}
    ]
  },
  "8": {
    "4": [
      {"type": "allusion", "target": "Deut 6:4", "note": "The Shema: 'Hear, O Israel: the LORD our God, the LORD is one' — Paul's declaration that 'there is no God but one' directly reprises the foundational Jewish monotheism of the Shema. The knowledge that idols have no real existence is grounded in the Shema's absolute claim; the Corinthians' theological clarity about idols flows from their Jewish inheritance even as Gentile converts."},
      {"type": "allusion", "target": "Isa 44:6-8", "note": "The LORD's declaration — 'I am the first and I am the last; apart from me there is no God... Is there any God besides me? No, there is no other Rock' — undergirds Paul's dismissal of idols as having no real existence. Isaiah's anti-idol polemic is the prophetic tradition Paul draws on to establish that idol-food is spiritually neutral because the 'god' behind it does not exist."}
    ],
    "6": [
      {"type": "allusion", "target": "Prov 8:22-30", "note": "Wisdom as God's co-worker in creation, present with him when he established the earth and set the heavens in place — Paul's description of Jesus Christ as the one 'through whom all things were made and through whom we exist' applies the personified Wisdom tradition to Jesus, placing him in the role that Prov 8 reserved for the Wisdom-agent of creation. This Christological extension of Wisdom theology is the most theologically dense move in 1 Corinthians 8."},
      {"type": "shadow", "target": "Deut 6:4", "note": "The Shema ('YHWH our God, YHWH is one') is expanded in v.6 into a bipartite formula — one God the Father + one Lord Jesus Christ — that reapplies the Shema's monotheistic structure to a two-person confession. Paul does not cite the Shema but restructures it: the theological categories of the Shema (one God) now include the Lord Jesus, placing him within the divine identity rather than alongside it as a second god."}
    ],
    "11": [
      {"type": "allusion", "target": "Isa 53:4", "note": "The Servant bearing the infirmities of others — 'Surely he took up our pain and bore our suffering' — Paul's argument that the strong who destroy the weak 'for whom Christ died' are sinning against Christ activates the Servant-bearing logic: Christ bore the weakness of the weak in his death; to destroy the weak by exercising rights over their conscience is to work against the purpose of the Servant's sacrifice."}
    ],
    "13": [
      {"type": "allusion", "target": "Dan 1:8", "note": "Daniel's resolve not to defile himself with the royal food and wine, accepting a restricted diet to maintain covenant purity — the model of voluntarily restricting one's permitted diet for the sake of conscience and holiness is Daniel's concrete example. Paul's willingness to never eat meat again for the sake of a brother's conscience applies the same principle: freedom is surrendered for a higher obligation."}
    ]
  }
}

def main():
    existing = load_echo('1corinthians')
    merge_echo(existing, CORINTHIANS_ECHOES)
    save_echo('1corinthians', existing)
    total_verses = sum(len(v) for v in existing.values())
    print(f'1 Corinthians 5–8 echoes written. {len(existing)} chapters, {total_verses} verses with connections.')

if __name__ == '__main__':
    main()
