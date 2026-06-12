"""
MKT Echo Layer — Proverbs chapters 22–24
Run: python3 scripts/zc-echo-proverbs-22-24.py

Source data used:
- data/interlinear/proverbs.json
- data/translation/draft/mediating/proverbs.json (MKT text)
- data/parallels/proverbs.json (no entries for chs 22–24)
- data/echoes/proverbs.json (existing entries for chs 1–18, 25–26)

Key decisions:
- "Words of the Wise" (22:17–24:22) parallels the Egyptian Instruction of Amenemope;
  echo entries focus on where individual proverbs are taken up by NT authors.
- 23:10–11 goel/redeemer image classified as 'type' toward Christ's redemption.
- 24:12 ("repay according to works") classified as 'theme' — foundational to NT
  judgment theology (Rom 2:6; Rev 20:12) but not a direct quote/fulfillment.
- 23:27–28 (the seductive woman as deep pit) classified 'shadow' toward Rev 17's
  great harlot who seduces the nations away from God.
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
  "22": {
    "2": [
      {"type": "theme", "target": "Gal 3:28", "note": "The LORD made both rich and poor — their common Maker establishes a dignity that overrides economic stratification. Paul's declaration that 'there is neither slave nor free... you are all one in Christ Jesus' (Gal 3:28) grounds that equality not in creation alone but in union with the one through whom all was made (John 1:3)."}
    ],
    "6": [
      {"type": "allusion", "target": "Eph 6:4", "note": "Train a child in the way he should go — Paul takes up this parental formation mandate: 'bring them up in the discipline and instruction of the Lord' (Eph 6:4). The pattern moves from wisdom-formation to Christ-centered formation; the teacher is now Christ himself rather than the parent-sage."}
    ],
    "9": [
      {"type": "allusion", "target": "2 Cor 9:6", "note": "A generous person will be blessed, for he shares his bread with the poor — Paul builds on this proverb's sowing-reaping logic: 'whoever sows sparingly will also reap sparingly, and whoever sows bountifully will also reap bountifully' (2 Cor 9:6). The NT grounds generosity not only in wisdom but in the grace of God who gave his Son (2 Cor 9:8–9)."}
    ],
    "11": [
      {"type": "allusion", "target": "Matt 5:8", "note": "Whoever loves a pure heart and whose speech is gracious will have the king as his friend — the beatitude 'blessed are the pure in heart, for they shall see God' (Matt 5:8) takes up the same association between inner purity and nearness to the sovereign. The king sought changes from an earthly ruler to God himself."}
    ],
    "22": [
      {"type": "allusion", "target": "Jas 5:4", "note": "Do not rob the poor or crush the afflicted at the city gate — the gate is the court of justice; exploiting legal power against the powerless is what James condemns when the cries of defrauded workers 'have reached the ears of the Lord of hosts' (Jas 5:4). The same divine advocacy for the poor structures both texts."}
    ],
    "24": [
      {"type": "allusion", "target": "Jas 1:19", "note": "Do not befriend an angry man or associate with someone hot-tempered — James draws on this wisdom about anger's contagion: 'let every person be quick to hear, slow to speak, slow to anger; for the anger of man does not produce the righteousness of God' (Jas 1:19–20). The rationale shifts from social self-protection to theological grounding in God's character."}
    ]
  },
  "23": {
    "10": [
      {"type": "type", "target": "Heb 9:12", "note": "Do not move the boundary stone of orphans, for their Redeemer is strong — the go'el (kinsman-redeemer) who champions the legally helpless foreshadows Christ as eschatological Redeemer. Hebrews presents him as one who 'entered once for all into the holy places... securing an eternal redemption' (Heb 9:12), the ultimate strong advocate for those without legal standing before God."}
    ],
    "13": [
      {"type": "allusion", "target": "Heb 12:11", "note": "Do not withhold discipline from a child; if you discipline him with the rod, he will not die — the equation of loving discipline with life is precisely the argument of Hebrews 12: 'for the moment all discipline seems painful rather than pleasant, but later it yields the peaceful fruit of righteousness' (Heb 12:11). Hebrews also cites the parental analogy explicitly (Heb 12:5–8) to ground God's discipline of his children."}
    ],
    "17": [
      {"type": "allusion", "target": "Heb 6:19", "note": "Live in the fear of the LORD all the day long, for surely there is a future and your hope will not be cut off — Proverbs' confidence in a future secured by God is taken up in Hebrews: 'we have this hope as an anchor for the soul, firm and secure' (Heb 6:19). The future Proverbs affirms for the God-fearer is identified in Hebrews as Christ himself, who has entered the inner sanctuary as our forerunner."}
    ],
    "22": [
      {"type": "allusion", "target": "Eph 6:2", "note": "Listen to your father who gave you life, and do not despise your mother when she grows old — Paul cites the fifth commandment ('Honor your father and mother') as 'the first commandment with a promise' (Eph 6:2); the Proverbs tradition consistently supplies that commandment with its relational texture and concrete motivations."}
    ],
    "23": [
      {"type": "theme", "target": "John 14:6", "note": "Buy the truth and do not sell it — wisdom, instruction, and understanding as well — Proverbs treats truth as something sought and purchased at great cost. The Johannine identification of Jesus as 'the truth' (John 14:6) fulfills what Proverbs figures as an elusive commodity: in Christ, truth is not an abstract virtue but a person who gives himself freely (John 1:14, 17)."}
    ],
    "27": [
      {"type": "shadow", "target": "Rev 17:1", "note": "A prostitute is a deep pit and an immoral woman is a narrow well — Proverbs' extended personification of the seductive 'strange woman' who lures men to death (chs 2, 5, 7, 9, 23) prefigures Revelation's 'great prostitute who is seated on many waters' (Rev 17:1), the city-system that seduces the nations away from God. Both texts deploy the same female-danger image to encode spiritual adultery — unfaithfulness to the living God."}
    ],
    "29": [
      {"type": "allusion", "target": "Eph 5:18", "note": "Who has grief? Who has anguish? Those who linger over wine — the catalogue of wine's destructive consequences (vv. 29–35) stands behind Paul's contrast: 'do not get drunk with wine, for that is debauchery, but be filled with the Spirit' (Eph 5:18). Both texts treat intoxication as a counterfeit fullness that destroys judgment and leads only to ruin."}
    ]
  },
  "24": {
    "3": [
      {"type": "allusion", "target": "Matt 7:24", "note": "By wisdom a house is built, and by understanding it is established — Jesus builds his climactic parable around exactly this image: 'everyone who hears these words of mine and does them will be like a wise man who built his house on the rock' (Matt 7:24). The shift is from abstract wisdom to hearing and obeying the words of Jesus as the only secure foundation."}
    ],
    "12": [
      {"type": "theme", "target": "Rom 2:6", "note": "Does not he who weighs the heart perceive it? Will he not repay each person according to what they have done? — one of Proverbs' clearest statements of retributive divine justice. Paul cites the same principle (from Ps 62:12) in Romans 2:6 to establish that God 'will render to each according to his works'; Revelation's final judgment follows the same pattern (Rev 20:12–13). Christ bears the weight of that repayment for those united to him (Rom 8:1–4)."}
    ],
    "16": [
      {"type": "allusion", "target": "Jas 5:11", "note": "A righteous person falls seven times and gets up again, but the wicked are brought down by calamity — the pattern of righteous perseverance through repeated adversity stands behind James's appeal to patient endurance: 'you have heard of the steadfastness of Job, and you have seen the purpose of the Lord' (Jas 5:11). The resurrection of Christ provides the deepest instance of 'getting up' that this proverb anticipates (Rom 6:4–5)."}
    ],
    "17": [
      {"type": "allusion", "target": "Rom 12:20", "note": "Do not gloat when your enemy falls or let your heart be glad when he stumbles — Paul cites the companion proverb (25:21–22) as the climax of his non-retaliation argument: 'do not be overcome by evil, but overcome evil with good' (Rom 12:21). Proverbs 24:17 provides the motivational heart of that command — the enemy's calamity is not our triumph."}
    ],
    "21": [
      {"type": "allusion", "target": "1 Pet 2:17", "note": "Fear the LORD and the king — Peter issues the same dual loyalty command: 'fear God; honor the king' (1 Pet 2:17). The Proverbs wisdom about divine and human authority carries forward into the NT exhortation, with Christ as the supreme authority to whom both king and subject answer (1 Pet 2:13–14)."}
    ],
    "29": [
      {"type": "allusion", "target": "Rom 12:17", "note": "Do not say, 'I will do to him what he did to me; I will repay him for what he has done' — Proverbs forbids the retaliatory calculus that human nature defaults to. Paul applies the same prohibition: 'repay no one evil for evil' (Rom 12:17); 'vengeance is mine, I will repay, says the Lord' (Rom 12:19). The logic runs from Proverbs through Paul to the cross, where God acts as the wronged party's advocate."}
    ]
  }
}

def main():
    existing = load_echo('proverbs')
    merge_echo(existing, PROVERBS_ECHOES)
    save_echo('proverbs', existing)
    print('Proverbs 22–24 echoes written.')

if __name__ == '__main__':
    main()
