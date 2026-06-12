"""
Echo Commentary — Proverbs chapters 4–6
Run: python3 scripts/zc-echo-proverbs-4-6.py

No parallels entries exist for ch 4-6 in data/parallels/proverbs.json.

Ch 4: Father's wisdom instruction — the path / light imagery reaches forward to
    Christ as the Way (John 14:6) and Light (John 8:12); wisdom as the supreme prize
    points to Christ in whom all wisdom is hidden (Col 2:3).
Ch 5: Warning against the adulteress — the faithful-wife / adulteress structure is
    the marital typology that Paul explicitly applies to Christ and the church
    (Eph 5:25-32; 2 Cor 11:2); the sealed fountain (v15-18) echoes the bridal imagery
    of Song of Songs and Rev 21:9.
Ch 6: Laziness, the seven abominations, and adultery revisited — the lamp of the
    commandment (v23) points to Christ as the true light (John 1:9; 8:12); the
    jealousy of the wronged husband (v34-35) echoes the divine jealousy for the
    church as Christ's bride (2 Cor 11:2; Rev 2:4).
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

PROVERBS_ECHOES = {
  "4": {
    "4": [
      {"type": "allusion", "target": "John 15:7",
       "note": "The father's call to 'let your heart hold fast my words' is echoed by Jesus' condition for abiding fruitfulness: 'if you abide in me and my words abide in you.' The relational indwelling of the teacher's words that Proverbs 4 models as paternal instruction becomes the christological union in John 15."},
      {"type": "allusion", "target": "Deut 6:6",
       "note": "The Shema's demand that the words be 'on your heart' is the explicit background for the father's instruction; both command the same internalization of divine teaching, and both anticipate Jer 31:33's new covenant promise of law written on the heart by the Spirit."}
    ],
    "7": [
      {"type": "allusion", "target": "Col 2:3",
       "note": "The imperative 'get wisdom' as the beginning of wisdom points to the NT identification of Christ as the one in whom 'are hidden all the treasures of wisdom and knowledge.' The quest that Proverbs commands is christologically resolved: wisdom is not an abstraction to pursue but a person to receive."}
    ],
    "8": [
      {"type": "type", "target": "Phil 2:9",
       "note": "The father promises that wisdom will exalt the one who prizes her highly — the same structure as the Christ-hymn in Phil 2: the one who humbled himself (Incarnation, cross) was therefore highly exalted by the Father. Wisdom's exaltation of her lovers typifies the pattern of voluntary lowering that leads to divine exaltation."}
    ],
    "10": [
      {"type": "allusion", "target": "John 14:6",
       "note": "The father's promise that wisdom's paths lead to life and 'the years of your life will be many' anticipates Christ's identification of himself as 'the way' that leads to life. In Proverbs 4 the father shows the way; in John 14 the Son is the way — the personal embodiment of the instructional tradition of Proverbs."}
    ],
    "18": [
      {"type": "allusion", "target": "Matt 5:14",
       "note": "The path of the righteous as 'the light of dawn, shining brighter and brighter until full day' is the OT background for Jesus' 'you are the light of the world.' The progressive-dawn imagery (dawn → full day) describes both the growth of the righteous and the eschatological movement from anticipation (OT wisdom) to full revelation in Christ."},
      {"type": "theme", "target": "John 8:12",
       "note": "Christ's 'I am the light of the world; whoever follows me will not walk in darkness but will have the light of life' directly engages the Proverbs path/light tradition. The two-way framework of Prov 4:18-19 (light path vs. dark path) is the structural background for John's pervasive light/darkness dualism."}
    ],
    "19": [
      {"type": "allusion", "target": "John 3:19",
       "note": "The way of the wicked as 'deep darkness' where 'they do not know over what they stumble' mirrors the Johannine diagnosis: 'people loved the darkness rather than the light because their works were evil.' The stumbling-in-darkness that Proverbs treats as wisdom's contrast case becomes the spiritual condition that the Incarnate Light comes to address."}
    ],
    "23": [
      {"type": "allusion", "target": "John 4:14",
       "note": "The command to guard the heart 'for from it flow the springs of life' provides the OT spring/life vocabulary that Jesus employs at the well: 'the water that I will give him will become a spring of water welling up to eternal life.' The heart as the source of life-springs in Proverbs is the organ that Christ transforms by the indwelling Spirit."},
      {"type": "theme", "target": "Jer 17:9",
       "note": "The Proverbs exhortation to guard the heart assumes the heart can and must be guarded; Jeremiah 17:9's diagnosis ('the heart is deceitful above all things') reveals the problem that guarding alone cannot solve — creating the need for the new-covenant heart-replacement of Ezek 36:26-27."}
    ],
    "26": [
      {"type": "allusion", "target": "Heb 12:13",
       "note": "The wisdom call to 'ponder the path of your feet; then all your ways will be sure' is picked up in Hebrews' athletic metaphor for the Christian life: 'make straight paths for your feet, so that what is lame may not be put out of joint but rather be healed.' Both texts use the physical-path metaphor for moral-spiritual direction, with Hebrews applying it to endurance in Christ's discipline."}
    ]
  },
  "5": {
    "3": [
      {"type": "allusion", "target": "Rev 17:2",
       "note": "The forbidden woman whose lips 'drip honey' and whose speech is 'smoother than oil' but whose end is bitter and sharp as a sword is the archetype that Revelation's Babylon-harlot develops: she too intoxicates the nations with the wine of her fornication. The adulteress of Proverbs 5 is the individual-scale type of the corporate seduction that Babylon represents."}
    ],
    "15": [
      {"type": "allusion", "target": "Song 4:12",
       "note": "The call to 'drink water from your own cistern, flowing water from your own well' uses the same water/well/fountain vocabulary as Song of Songs 4:12 ('a garden locked, a spring locked, a sealed fountain') — both texts use the sealed water-source as the image of the exclusive marital gift. The confluence of the two texts is exploited in Rev 21:6's 'spring of the water of life' given to the thirsty."}
    ],
    "18": [
      {"type": "type", "target": "Eph 5:25",
       "note": "The call to 'rejoice in the wife of your youth' — delighting in the covenant partner rather than straying — is the OT foundation for Paul's explicit typology: husbands loving their wives as Christ loved the church. The exclusive marital delight commanded in Proverbs 5:18-19 is the type whose antitype is Christ's exclusive, self-giving love for the church as his bride."},
      {"type": "theme", "target": "2 Cor 11:2",
       "note": "Paul's 'divine jealousy' for the Corinthian church — 'I betrothed you to one husband, to present you as a pure virgin to Christ' — directly applies the faithful-wife logic of Proverbs 5 to the church's relation to Christ. The adulteress-warning of Proverbs (vv3-20) becomes in Paul the warning against spiritual adultery through false teaching."}
    ],
    "19": [
      {"type": "allusion", "target": "Eph 5:29",
       "note": "The husband's ravishment and intoxication in the arms of his wife ('let her breasts fill you at all times with delight; be intoxicated always in her love') is the domestic delight that Paul elevates to christological typology: Christ nourishes and cherishes the church as his own body, and the husband is commanded to do the same. The loving nurture of Proverbs 5:19 is the seed of the Christ-and-church parallel."}
    ],
    "21": [
      {"type": "theme", "target": "Heb 4:13",
       "note": "The observation that 'the ways of a man are before the eyes of the LORD, and he ponders all his paths' is the wisdom tradition's version of Hebrews 4:13: 'nothing in all creation is hidden from God's sight; everything is uncovered and laid bare before the eyes of him to whom we must give account.' Both texts frame divine omniscience as the ultimate context for human moral choices."}
    ],
    "22": [
      {"type": "theme", "target": "John 8:34",
       "note": "The wicked man trapped by 'his own iniquities' and 'the cords of his sin' that hold him fast describes the mechanism that Jesus names in John 8:34: 'everyone who practices sin is a slave to sin.' The Proverbs image of self-entangling cords is the concrete metaphor for the Johannine bondage that only the Son's freedom can break (v36: 'if the Son sets you free, you will be free indeed')."}
    ]
  },
  "6": {
    "6": [
      {"type": "theme", "target": "John 9:4",
       "note": "The ant's diligence in summer — 'go to the ant, O sluggard; consider her ways, and be wise' — shares the urgency-of-present-opportunity theme with Jesus' 'we must work the works of him who sent me while it is day; night is coming, when no one can work.' Both texts use the brevity of the favorable season as motivation for present diligence."}
    ],
    "16": [
      {"type": "theme", "target": "Luke 18:14",
       "note": "The first of the seven abominations God hates is 'haughty eyes' — the physiology of pride that Proverbs lists as the supreme divine offense. Jesus' parable of the Pharisee and tax collector ends with the same reversal: 'everyone who exalts himself will be humbled, and everyone who humbles himself will be exalted.' The haughty eyes that are the beginning of the abomination list are the spiritual condition Christ's parable diagnoses and inverts."},
      {"type": "allusion", "target": "Rev 6:10",
       "note": "Hands that shed innocent blood (second abomination) are the defining crime against God's saints whose cry is heard in Rev 6:10 ('how long before you judge and avenge our blood?'). The shedding of innocent blood that Proverbs identifies as uniquely hateful to God is the crime that the martyrs' prayer demands God avenge in the eschatological judgment."}
    ],
    "19": [
      {"type": "allusion", "target": "John 17:21",
       "note": "The final abomination — 'one who sows discord among brothers' — is the anti-type of Christ's high-priestly prayer for unity: 'that they may all be one, just as you, Father, are in me, and I in you.' What God supremely hates (the sower of discord) is precisely what Christ's cross and prayer supremely counters: the reconciling unity of those who were formerly divided."}
    ],
    "20": [
      {"type": "allusion", "target": "Eph 6:1",
       "note": "The exhortation to keep the father's commandment and not forsake the mother's teaching is the underlying text that Paul's fifth commandment application develops: 'children, obey your parents in the Lord, for this is right.' Both Proverbs and Ephesians ground filial obedience in divine authority, with Ephesians specifying that obedience is 'in the Lord' — the christological context of all family relationships."}
    ],
    "23": [
      {"type": "type", "target": "John 1:9",
       "note": "The identification of the commandment as 'a lamp' and the teaching as 'a light' (using the same Hebrew terms as Ps 119:105) anticipates Christ as the true and final Light: John 1:9 names Jesus 'the true light, which gives light to everyone, was coming into the world.' The lamp of the Torah that guides the path is the type of the Logos-Light who is himself the light of the world."},
      {"type": "allusion", "target": "Ps 119:105",
       "note": "The lamp/light/path triad of Prov 6:23 is identical in structure to Ps 119:105 ('your word is a lamp to my feet and a light to my path') — both are within the Torah-as-light tradition that the NT christologically relocates: what the word of instruction does in Proverbs and Psalms, Christ does personally as the Word who became flesh (John 1:14)."}
    ],
    "26": [
      {"type": "allusion", "target": "1 Cor 6:18",
       "note": "The adulteress who reduces a man 'to a loaf of bread' and whose body is a fatal trap parallels Paul's warning 'flee from sexual immorality' (1 Cor 6:18), which grounds its argument not in wisdom but in the body's status as a temple of the Holy Spirit (v19). Paul's christological body-theology radicalizes the Proverbs warning: the harm of sexual immorality is not merely social destruction but the violation of union with Christ."}
    ],
    "27": [
      {"type": "allusion", "target": "1 Cor 6:15",
       "note": "The rhetorical question 'can a man carry fire next to his chest and his clothes not be burned?' provides the logic underlying Paul's body-union argument in 1 Cor 6:15-17: taking the body into a sinful union is a union as real and ruinous as carrying coals in the bosom. Paul applies the same can't-contain-the-consequences logic but frames the body as a member of Christ, not merely a physical self."}
    ],
    "34": [
      {"type": "type", "target": "2 Cor 11:2",
       "note": "The jealousy of the wronged husband ('for jealousy makes a man furious, and he will not spare when he takes revenge') typifies the divine jealousy that Paul explicitly claims: 'I feel a divine jealousy for you, since I betrothed you to one husband, to present you as a pure virgin to Christ.' The injured husband's consuming jealousy for his exclusive covenant partner is the human type of God's / Christ's jealous love for the church."},
      {"type": "allusion", "target": "Rev 2:4",
       "note": "The husband's rage at adultery (v34-35) anticipates Christ's rebuke to the Ephesian church: 'you have abandoned the love you had at first.' The unfaithfulness that Proverbs 6 warns against at the individual level becomes the spiritual adultery that Christ addresses in Revelation's letters to the churches — the abandonment of the first love for the Bridegroom."}
    ]
  }
}

def main():
    existing = load_echo('proverbs')
    merge_echo(existing, PROVERBS_ECHOES)
    save_echo('proverbs', existing)
    total = sum(len(vv) for vv in PROVERBS_ECHOES.values())
    entries = sum(len(e) for ch in PROVERBS_ECHOES.values() for e in ch.values())
    print(f'Proverbs 4-6 echoes: {total} verses, {entries} entries written.')

if __name__ == '__main__':
    main()
