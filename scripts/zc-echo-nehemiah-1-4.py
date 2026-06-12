"""
MKT Echo Layer — Nehemiah chapters 1–4
Run: python3 scripts/zc-echo-nehemiah-1-4.py

Key decisions:
- Ch1: Nehemiah's prayer as covenant-confession and intercession model; scatter/gather
  Deuteronomic pattern (v8-9) → Matt 24:31; "great and awesome God" formula → Dan 9:4
- Ch2: Nehemiah's commissioning as type of Christ's sending from the Father; arrow
  prayer (v4) → 1 Thess 5:17; "no share in Jerusalem" exclusion → Rev 21:27
- Ch3: Wall-builder register is selective; Tekoite nobles refusing → Luke 14:18;
  Shallum's daughters → Gal 3:28; priestly first-work → Heb 13:20-21
- Ch4: Praying and posting guards → Eph 6:18; "Our God will fight for us" → Rom 8:31;
  imprecatory prayer → Rev 6:10; workers armed while building → 2 Cor 10:3-5
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

NEH_ECHOES = {
  "1": {
    "5": [
      {
        "type": "allusion",
        "target": "Dan 9:4",
        "note": "Nehemiah's prayer opens with the same liturgical address as Daniel's great confession: 'O LORD, God of heaven, the great and awesome God, keeping covenant and steadfast love with those who love him and keep his commandments' (cf. Dan 9:4: 'O Lord, the great and awesome God, who keeps covenant and steadfast love with those who love him and keep his commandments'). The near-verbal identity indicates both prayers draw on a common liturgical formula of covenant address — the post-exilic community's standard petition grammar for approaching YHWH in situations of community need and covenant guilt. The formula structures the prayer as a covenant appeal: the one praying invokes YHWH's covenant attributes (greatness, awesomeness, covenant-keeping, steadfast-love-keeping) as the basis for the petition that follows. Both Daniel and Nehemiah confess communal sin before making a personal petition — the pattern Christ teaches in Matt 6:9-13."
      }
    ],
    "8": [
      {
        "type": "allusion",
        "target": "Deut 30:1-5",
        "note": "Nehemiah appeals to the Mosaic scatter-gather pattern: 'Remember the word you commanded your servant Moses: If you act unfaithfully, I will scatter you among the nations, but if you return to me and obey my commandments and keep them, then even if your exiles are at the far ends of the heavens, I will gather them from there and bring them to the place I have chosen as a dwelling for my Name.' This is a deliberate citation of Deut 30:1-5, the covenant's bilateral promise. Nehemiah's prayer is a deliberate activation of this Mosaic promise — he 'reminds' YHWH of the covenant terms as the basis for the restoration request. The same scatter-gather eschatology is taken up by Jesus in Matt 24:31 ('He will send out his angels... and they will gather his elect from the four winds, from one end of heaven to the other') and by Paul in Rom 11:25-26 — the Mosaic promise of regathering finding its eschatological fulfillment in Christ's final gathering."
      }
    ],
    "10": [
      {
        "type": "allusion",
        "target": "Rev 5:9",
        "note": "Nehemiah's appeal: 'They are your servants and your people, whom you redeemed by your great power and your mighty hand' uses the Exodus redemption vocabulary — <em>pādîtā</em> (you redeemed) + 'great power and mighty hand' (Deut 9:26, 29). The people's identity as YHWH's redeemed possessions is the basis of the intercession: what God has purchased, he must protect and restore. Rev 5:9 takes this redemption language into the new covenant register: 'you were slain, and by your blood you ransomed people for God from every tribe and language and people and nation.' The Mosaic redemption by power and mighty hand is the OT type; Christ's redemption by blood is the NT fulfillment — both establish God's ownership of the redeemed as the guarantee of his ongoing care."
      }
    ]
  },
  "2": {
    "4": [
      {
        "type": "theme",
        "target": "1 Thess 5:17",
        "note": "The 'arrow prayer' — Nehemiah prays to the God of heaven in the interval between the king's question ('What is it you want?') and his own answer — is the OT's most vivid illustration of instantaneous prayer within a pressing worldly context. There is no withdrawal, no extended ceremony — a single unspoken prayer to God while the king waits for an answer. Paul's injunction in 1 Thess 5:17 to 'pray without ceasing' (<em>ἀδιαλείπτως</em>) envisions exactly this kind of integrated prayer: not scheduled devotions that punctuate the day, but a continuous orientation of dependence on God that can be exercised in any moment, including before speaking to a king."
      }
    ],
    "5": [
      {
        "type": "type",
        "target": "John 17:18",
        "note": "Nehemiah says 'send me to Judah, to the city of my ancestors' — a petition to be sent on a mission of restoration. The pattern of the servant who volunteers to go, receives royal authorization (Artaxerxes' letters and escort), and departs on a mission of rebuilding the ruined covenant city is the OT narrative grammar that the Incarnation fulfills definitively. Jesus says in his high-priestly prayer, 'As you sent me into the world, so I have sent them into the world' (John 17:18). Nehemiah's royal commissioning for the Jerusalem mission types the Father's commissioning of the Son for the definitive restoration of God's dwelling — a mission that succeeds not because the walls are high but because the Sender has all authority."
      }
    ],
    "8": [
      {
        "type": "theme",
        "target": "Acts 11:21",
        "note": "The phrase 'the good hand of my God was upon me' (<em>yad ʾĕlōhay haṭṭôḇāh ʿālay</em>) is Nehemiah's signature formula for divine providence (appears in 2:8, 18; Ezra 7:6, 9, 28; 8:18, 22, 31). The 'hand of God' as metaphor for providential guidance and empowerment recurs throughout the restoration narratives. Acts 11:21 uses the same idiom for the Spirit's work in the early church: 'the hand of the Lord was with them, and a great number who believed turned to the Lord.' The language of the divine hand as the agent of blessing and direction bridges the OT restoration under Nehemiah and the NT expansion under the apostles — both are works of the same hand, operating in different covenant moments."
      }
    ],
    "12": [
      {
        "type": "allusion",
        "target": "2 Cor 8:16",
        "note": "Nehemiah rises by night having told no one 'what my God had put in my heart (<em>nātan ʾĕlōhay ʾel-libbî</em>) to do for Jerusalem.' The phrase 'God put it in my heart' is the OT formula for divine inner prompting — God working through the human will without external compulsion. Paul uses the same logic in 2 Cor 8:16 when thanking God who 'put into the heart of Titus the same earnestness I have for you.' Nehemiah's night survey of Jerusalem is driven by what God placed inwardly — the same sovereign inner-prompting that Paul identifies as God's ordinary mode of motivating his servants for kingdom work, anticipating the new covenant's law written on the heart (Jer 31:33)."
      }
    ],
    "17": [
      {
        "type": "theme",
        "target": "Rev 21:2",
        "note": "Nehemiah's call — 'You see the distress we are in — how Jerusalem lies in ruins with its gates burned. Come, let us rebuild the wall of Jerusalem, that we may no longer be a reproach' — is the OT's most direct expression of the impulse to restore the holy city from its ruin and disgrace. Rev 21:2 sets the eschatological fulfillment against this pattern of ruin: 'I saw the holy city, new Jerusalem, coming down out of heaven from God, prepared as a bride adorned for her husband.' Nehemiah's partial, earthly restoration — walls repaired, gates rehung, reproach removed — is the type of the complete, permanent restoration of the city that no enemy can breach, whose gates are never shut (Rev 21:25), and whose builder and maker is God himself (Heb 11:10)."
      }
    ],
    "19": [
      {
        "type": "allusion",
        "target": "Ps 22:6-7",
        "note": "Sanballat, Tobiah, and Geshem mock and despise Nehemiah's project: 'they mocked and ridiculed us' (<em>wayyiḇzû ʿālênû</em>). The pattern of covenant workers mocked and despised by enemies follows the Psalmic contour of the righteous sufferer: Ps 22:6-7 ('I am a worm, scorned by mankind and despised by the people; all who see me mock me'). The builders of the covenant community always face contempt from those outside — a pattern reaching its intensification in the passion, where Jesus is mocked, despised, and derided (Matt 27:39-44; Ps 22:7). Nehemiah's wall-building under mockery is one instance of the enduring pattern: covenant work done in the face of the world's contempt."
      }
    ],
    "20": [
      {
        "type": "allusion",
        "target": "Rev 21:27",
        "note": "Nehemiah declares to his opponents: 'You have no share or right or claim (<em>ḥēleq ûṣᵉḏāqāh ûzikkārôn</em>) in Jerusalem.' The triple exclusion — no portion, no righteous claim, no memorial — bars the mockers from any stake in the covenant city being rebuilt. Rev 21:27 applies the same exclusion principle to the new Jerusalem: 'nothing unclean will ever enter it, nor anyone who does what is detestable or false, but only those who are written in the Lamb's book of life.' Nehemiah's earthly exclusion of Sanballat, Tobiah, and Geshem from the restored Jerusalem is the type of the eschatological exclusion: those who oppose the building of God's city have no claim in the city that is finally and permanently established."
      }
    ]
  },
  "3": {
    "1": [
      {
        "type": "type",
        "target": "Heb 13:20",
        "note": "Eliashib the high priest and his fellow priests begin the wall-repair by rebuilding the Sheep Gate and dedicating it — the high priest initiates the communal restoration work. The Sheep Gate is where sacrificial animals entered Jerusalem (cf. John 5:2, the pool near the Sheep Gate). The high priest's first act restores access for the sacrificial system. Heb 13:20 addresses the fulfillment: 'the God of peace who brought again from the dead our Lord Jesus, the great shepherd of the sheep, by the blood of the eternal covenant.' The high priest rebuilding the Sheep Gate — the entryway for the lambs of sacrifice — types Christ the great Shepherd-Priest who, through his own blood as the sacrificial lamb, opens the way for those who are his sheep."
      }
    ],
    "5": [
      {
        "type": "theme",
        "target": "Luke 14:18",
        "note": "The Tekoite nobles 'would not put their shoulders to the work of their supervisors' (<em>wᵉʾaddîrêhem lōʾ-hēḇîʾû ṣawwᵉʾārām bᵉʿăḇōḏat ʾăḏōnêhem</em>) — an elite refusal to engage in common labor for the community's restoration. The text notes the Tekoite commoners built diligently while their nobles refused. This tension between willing common workers and unwilling elites appears in Christ's parable of the great banquet (Luke 14:18): 'they all alike began to make excuses' — it is precisely those with status and property who find reasons not to participate in the work of the kingdom. The Tekoite nobles who refused to put their shoulder to the wall are the narrative embodiment of the parable's invited-but-absent elite."
      }
    ],
    "12": [
      {
        "type": "theme",
        "target": "Gal 3:28",
        "note": "Shallum son of Hallohesh, ruler of a half-district of Jerusalem, repaired his section — 'he and his daughters' (<em>hûʾ ûḇᵉnōtāyw</em>). Women building the city wall is an exceptional detail in the ancient Near Eastern context, where wall-construction and military defense were exclusively male domains. The inclusion of daughters in the physical labor of covenant restoration anticipates the breaking-down of gender barriers in the people of God that Paul declares in Gal 3:28: 'there is neither male nor female, for you are all one in Christ Jesus.' The participation of women in the foundational work of rebuilding the covenant community is an early instance of the principle the new covenant fully establishes."
      }
    ],
    "20": [
      {
        "type": "theme",
        "target": "Titus 2:14",
        "note": "Baruch son of Zabbai 'zealously repaired another section' (<em>heḥĕrāh ḥāzaq</em> — literally 'made repairs with burning zeal'). The verb <em>ḥārar</em> (to burn/glow) applied to building work signals exceptional personal investment beyond assigned responsibility. Titus 2:14 describes the new covenant community Christ created as 'a people for his own possession who are zealous for good works' (<em>ζηλωτὴν καλῶν ἔργων</em>). Baruch's burning zeal for the wall-section he did not need to repair exemplifies the excess of covenant motivation that the new covenant's indwelling Spirit produces — building beyond obligation out of love for the community."
      }
    ]
  },
  "4": {
    "4": [
      {
        "type": "type",
        "target": "Rev 6:10",
        "note": "Nehemiah's imprecatory prayer — 'Hear us, O our God, for we are held in contempt. Turn their reproach back on their own heads... for they have provoked you to anger in the presence of the builders' — is a covenant-curse prayer calling for YHWH to adjudicate the injustice done to his workers. Nehemiah does not retaliate personally but appeals to divine justice against those who mock the covenant work. This prayer structure — appealing to God for vindication against persecutors — is the OT basis for the martyrs' cry in Rev 6:10: 'O Sovereign Lord, holy and true, how long before you will judge and avenge our blood on those who dwell on the earth?' Both Nehemiah and the martyred souls appeal to God's justice rather than taking matters into their own hands, trusting that the covenant Lord is the ultimate judge."
      }
    ],
    "6": [
      {
        "type": "allusion",
        "target": "Phil 2:13",
        "note": "'The people had the will/heart to work' (<em>lēḇ lāʿām laʿăśôt</em> — literally 'the people had a heart to do the work'). Despite mockery from enemies and physical exhaustion, the community completes the wall to half its height because of inner motivation. The locus of motivation is the <em>lēḇ</em> (heart/will) — the covenantal center of the person. Phil 2:13 articulates the NT parallel: 'it is God who works in you, both to will (<em>θέλειν</em>) and to work (<em>ἐνεργεῖν</em>) for his good pleasure.' The workers who have a 'heart to work' in Nehemiah's community are the OT instance of the Spirit-energized willing and working that Paul describes as God's ordinary operation within the covenant community."
      }
    ],
    "9": [
      {
        "type": "allusion",
        "target": "Eph 6:18",
        "note": "'We prayed to our God and posted a guard against them day and night' — the combination of prayer and practical preparation. Nehemiah does not choose between spiritual and practical response to the threat; he does both simultaneously. This both/and of prayer + action is the structure Paul articulates in Eph 6:18: after calling the community to 'put on the whole armor of God' (practical-metaphorical preparation), he calls them to 'pray in the Spirit on all occasions with all kinds of prayers and requests.' The Nehemiah community's guard-and-pray response to Sanballat's coalition is the OT narrative enactment of the spiritual-warfare logic Paul systematizes in Ephesians 6."
      }
    ],
    "14": [
      {
        "type": "allusion",
        "target": "Rom 8:31",
        "note": "Nehemiah tells the community: 'Do not be afraid of them. Remember the Lord, who is great and awesome, and fight for your brothers, your sons, your daughters, your wives, and your homes.' The basis for courage in the face of overwhelming opposition is the character of YHWH — 'great and awesome' — not the community's own resources. The same logic governs Paul's climactic declaration in Rom 8:31: 'If God is for us, who can be against us?' The theological grammar is identical: the community facing hostile forces is called to confidence not in its own strength but in the nature of the God who fights for it. Nehemiah's 'the great and awesome God' fighting for his people is the OT narrative instance of Paul's certainty about the God who justifies."
      }
    ],
    "20": [
      {
        "type": "allusion",
        "target": "Deut 20:4",
        "note": "'Our God will fight for us' (<em>ʾĕlōhênû yillāḥem lānû</em>) is the holy-war assurance formula — the promise that YHWH is the primary combatant in the covenant community's battles. Deut 20:4 is the Mosaic foundation: 'for YHWH your God is he who goes with you to fight for you against your enemies, to give you the victory.' Nehemiah's application of the holy-war promise to the wall-building project — labor with trowel and spear — shows the post-exilic community's understanding that the restoration of Jerusalem is a holy-war campaign: YHWH fighting not against nations with armies but against the opposition to his covenant purposes. The same logic governs the NT community's spiritual warfare (2 Cor 10:3-5): the weapons are not worldly, but the divine fighter is the same covenant God."
      }
    ]
  }
}

def main():
    existing = load_echo('nehemiah')
    merge_echo(existing, NEH_ECHOES)
    save_echo('nehemiah', existing)
    print('Nehemiah 1–4 echoes written.')

if __name__ == '__main__':
    main()
