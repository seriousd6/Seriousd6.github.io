"""
MKT Echo Layer — Ecclesiastes chapters 10–12
Run: python3 scripts/zc-echo-ecclesiastes-10-12.py

Ch10: Little-folly-ruins-much (10:1) → Gal 5:9; 1 Cor 5:6;
      social inversions (10:5-7) → Luke 1:52; 1 Cor 1:27;
      fool's words devour him (10:12-14) → Matt 12:36-37; Jas 3:5-6
Ch11: Cast bread on waters (11:1) → 2 Cor 9:6-8;
      don't know path of wind (11:5) → John 3:8;
      sow morning and evening (11:6) → Mark 4:26-29;
      youth is vapor (11:10) → Jas 4:14
Ch12: Fear God and keep his commandments (12:13) → Matt 22:37-40 [already present]
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

ECHOES = {
  "10": {
    "1": [
      {"type": "allusion", "target": "Gal 5:9", "note": "Dead flies cause the perfumer's ointment to give off a foul smell; so a little folly outweighs wisdom and honor — the contamination-by-small-amount principle. Paul uses the same image for moral contamination in two directions: 'a little leaven leavens the whole lump' (Gal 5:9; 1 Cor 5:6). The perfumer's ointment represents wisdom accumulated through character formation — a little folly spoils the entire compound, just as one leavening agent works through the whole batch. Both Qohelet and Paul are making the same observation about the disproportionate power of moral compromise."},
      {"type": "theme", "target": "Jas 3:5", "note": "The small-thing-causing-great-damage principle — James applies it to the tongue: 'how great a forest is set ablaze by such a small fire! And the tongue is a fire' (Jas 3:5-6). The dead flies of Ecclesiastes 10:1 and the spark of James 3:5 are the same observation about the asymmetry between the size of the contaminating agent and the damage it produces. Wisdom literature across both testaments recognizes that moral corruption tends to operate through small, seemingly insignificant compromises that have outsized destructive effect."}
    ],
    "4": [
      {"type": "theme", "target": "Rom 12:17-21", "note": "If the ruler's anger flares against you, do not abandon your post — composure can defuse even serious offenses — the wisdom of measured non-reactive response to authority's anger. Paul's instruction for the community under hostile authority: 'never avenge yourselves... if your enemy is hungry, feed him' (Rom 12:17-21). The composure that Qohelet commends is the same non-retaliatory posture Paul instructs — both grounded in the observation that reactive self-defense escalates while composed perseverance opens the possibility of de-escalation."},
      {"type": "allusion", "target": "Matt 5:5", "note": "The composure that defuses the ruler's anger is the practical wisdom form of the beatitude 'blessed are the meek, for they shall inherit the earth' (Matt 5:5). The meekness Christ commends is not passivity but the controlled strength that Qohelet observes can defuse serious offenses — the person who can remain composed under pressure exercises more power than the reactive person who escalates."}
    ],
    "6": [
      {"type": "theme", "target": "1 Cor 1:27", "note": "Fools are appointed to high positions while the capable sit in lowly ones — the social inversion Qohelet observes as an evil under the sun. Paul makes this inversion central to the theology of the cross: 'God chose what is foolish in the world to shame the wise; God chose what is weak in the world to shame the strong' (1 Cor 1:27-28). What Qohelet laments as disorder, Paul identifies as the divine counter-strategy — the appointing of the apparently foolish and low is not cosmic malfunction but God's method of confounding the wisdom of the world."},
      {"type": "allusion", "target": "Luke 1:52", "note": "The Magnificat addresses the same social inversion: 'he has brought down the mighty from their thrones and exalted those of humble estate' (Luke 1:52). What Qohelet catalogues as an observed injustice — capable people in lowly positions, fools in high ones — Mary announces as God's reversing action in Christ. The incarnation is the maximum expression of the capable (the Son of God) taking the lowest position, overturning the inverted order Qohelet laments."}
    ],
    "8": [
      {"type": "theme", "target": "Gal 6:7", "note": "Whoever digs a pit may fall into it, and whoever breaks through a wall may be bitten by a snake — the self-returning harm of wickedness. Paul states this as a theological principle: 'whatever a person sows, that will they also reap' (Gal 6:7). The pit-digger falling into his own pit is the wisdom tradition's concrete illustration of the sowing-and-reaping principle. Qohelet's observation fits within the broader biblical pattern in which the trap set for others becomes the trap of the one who set it (cf. Prov 26:27; Ps 7:15-16)."}
    ],
    "12": [
      {"type": "allusion", "target": "Matt 12:36-37", "note": "A wise person's words earn goodwill, but a fool's words devour him — the self-consuming speech of the fool. Christ extends the observation into eschatological accountability: 'I tell you, on the day of judgment people will give account for every careless word they speak, for by your words you will be justified, and by your words you will be condemned' (Matt 12:36-37). The fool whose words devour him is the one whose careless speech condemns him at judgment. Qohelet makes the observation about present social consequences; Christ makes it about ultimate accountability."},
      {"type": "theme", "target": "Jas 3:6", "note": "The tongue of the fool that begins with foolishness and ends in wicked madness (10:13) is the fire-tongue James describes: 'the tongue is a fire, a world of unrighteousness... it sets on fire the entire course of life, and is set on fire by hell' (Jas 3:6). The escalation Qohelet describes — beginning in folly, ending in madness — is the course of the tongue set on the fire trajectory James identifies. Both texts observe that destructive speech does not remain contained but amplifies."}
    ],
    "16": [
      {"type": "theme", "target": "Rom 13:1-4", "note": "Woe to the land whose king is a boy and whose rulers carouse in the morning — the governance-quality observation that public welfare depends on the moral character of rulers. Paul's instruction that governing authorities are God's servants for good (Rom 13:1-4) is the theological framework that makes Qohelet's governance-observation coherent: when rulers fulfill their role as God's servants they produce blessing; when they are corrupt (carousing in the morning instead of governing) they produce the woe Qohelet describes. The connection between ruler character and land welfare is a consistent thread across wisdom and epistolary literature."}
    ],
    "20": [
      {"type": "theme", "target": "Matt 10:26", "note": "Do not curse the king, even in your thoughts, for a bird may carry your words — the saying about hidden speech becoming public. Christ inverts the principle: 'nothing is covered that will not be revealed, or hidden that will not be known' (Matt 10:26). Qohelet warns that private words become public through unexpected channels; Christ announces that concealment itself will be removed in the eschatological disclosure. The bird-carrying-your-words is the folk-wisdom version of the comprehensive final revelation Christ announces."}
    ]
  },
  "11": {
    "1": [
      {"type": "allusion", "target": "2 Cor 9:6-8", "note": "Cast your bread upon the waters, for you will find it again after many days — the return of generous dispersal after an extended period. Paul uses the same agricultural image for generosity: 'whoever sows sparingly will also reap sparingly, and whoever sows bountifully will also reap bountifully' (2 Cor 9:6). The bread-upon-waters that returns is the seed that grows; the many days before the return is the interval between sowing and harvest. Both texts make the same investment-in-the-unknown argument for generosity: the return is real but deferred, which is why it requires trust."},
      {"type": "theme", "target": "Luke 6:38", "note": "Give a share to seven, even to eight (11:2) extends the generosity principle with explicit surplus-giving: giving beyond calculated sufficiency, because you do not know what calamity may come. Luke 6:38: 'give, and it will be given to you. Good measure, pressed down, shaken together, running over, will be put into your lap.' The giving-without-knowing-the-return principle is the NT's theological articulation of Qohelet's wisdom-observation about the economics of generosity."}
    ],
    "5": [
      {"type": "allusion", "target": "John 3:8", "note": "Just as you cannot know the path of the wind or how bones form in the womb of a pregnant woman, so you do not know the work of God who makes everything — Qohelet's double image for the inscrutable: wind and embryology, both beyond human comprehension. Christ uses precisely the wind image for the Spirit: 'the wind blows where it wishes, and you hear its sound, but you do not know where it comes from or where it goes. So it is with everyone born of the Spirit' (John 3:8). The path-of-the-wind that Qohelet identifies as the paradigm of the unknowable becomes in Christ's teaching the image for the Spirit's sovereign regenerating work — the inscrutable that Qohelet observes becomes the Spirit that Jesus announces as the agent of new birth."}
    ],
    "6": [
      {"type": "allusion", "target": "Mark 4:26-29", "note": "Sow your seed in the morning, and in the evening do not let your hand rest — for you do not know which sowing will prosper, or whether both will do equally well — the diligent sowing in ignorance of which will succeed. Christ's parable of the seed growing secretly (Mark 4:26-29) operates on the same principle: the farmer sows and goes to sleep, not knowing how the seed grows — 'the earth produces by itself.' Qohelet's advice to sow in ignorance of which sowing will succeed becomes in Christ's teaching a theological observation about the kingdom: the sower does his part without controlling or fully comprehending the growth-process. The parable is the theology of what Qohelet observed as practical wisdom."}
    ],
    "9": [
      {"type": "theme", "target": "2 Cor 5:10", "note": "Rejoice, young man, in your youth — follow the ways of your heart... but know that for all these things God will bring you into judgment — the joy-with-accountability formula. Paul: 'we must all appear before the judgment seat of Christ, so that each one may receive what is due for what he has done in the body, whether good or evil' (2 Cor 5:10). The judgment that follows the freedom of youth is not the cancellation of the joy but its framing condition — both Qohelet and Paul hold joy and accountability together without collapsing one into the other."},
      {"type": "allusion", "target": "Heb 9:27", "note": "It is appointed for man to die once, and after that comes judgment (Heb 9:27) — the same joy-accountable structure Qohelet states here. Hebrews then announces Christ's solution: as Christ was offered once to bear the sins of many (Heb 9:28), the judgment that would otherwise terminate the young person's joy has been addressed in him. The judgment Qohelet warns about and Hebrews confirms is the judgment Christ absorbed on behalf of those who belong to him."}
    ],
    "10": [
      {"type": "allusion", "target": "Jas 4:14", "note": "Banish anxiety from your heart and put away pain from your body, for childhood and youth are vapor (hebel) — the vanity-of-youth observation closing the youth-instruction. James uses the same hebel/vapor image: 'what is your life? For you are a mist that appears for a little time and then vanishes' (Jas 4:14). Qohelet's observation about the brevity of youth is James's observation about the brevity of life itself — the vapor that appears and vanishes. Both texts use this as a call to present faithfulness rather than as despair: Qohelet calls for joy free from anxiety; James calls for submission to God's will rather than presumptuous planning."}
    ]
  }
}

def main():
    e = load_echo('ecclesiastes')
    merge_echo(e, ECHOES)
    save_echo('ecclesiastes', e)
    new_chs = sum(1 for ch in ECHOES if ch not in ['12'])
    print(f'ecclesiastes echo: added entries for ch 10-11 ({sum(len(v) for ch, v in ECHOES.items())} verses)')

if __name__ == '__main__':
    main()
