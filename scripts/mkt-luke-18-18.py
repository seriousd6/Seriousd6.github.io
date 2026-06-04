"""
MKT Luke chapter 18 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-luke-18-18.py

Translation decisions:
- G166 (αἰώνιος, vv. 18, 30): "eternal" in L/M; T uses "eternal" and "age to come" — the
  adjective denotes the quality of the coming age, not only infinite duration; "age to come"
  (v30 T) keeps the temporal register explicit
- G4102 (πίστις, vv. 8, 42): "faith" throughout all three tiers — consistent with Luke 17
  rendering in prior script
- G4982 (σῴζω, v. 42): L: "has saved you"; M: "has healed you"; T: "has made you well" —
  the physical healing is foregrounded here (a blind man); carried forward from 17:19 pattern
  in the prior script where the physical σῴζω governs
- G1344 (δικαιόω, v. 14): L/M: "justified"; T: "right with God" — the forensic legal meaning
  is central to this parable; the T tier surfaces what the forensic declaration means
- G2962 (κύριος, vv. 6, 41): "Lord" throughout — v6 is Jesus' title, v41 blind man's address
- G476 (ἀντίδικος, v. 3): "adversary" (L) / "opponent" (M/T) — legal adversary in a lawsuit;
  the widow's legal dispute context calls for this precision
- G2433 (ἱλάσκομαι, v. 13): "be merciful" (L/M); T "have mercy" — the word is propitiation
  language but in this personal prayer context the plea for mercy governs the rendering
- G758 (ἄρχων, v. 18): "ruler" (L/M/T) — a civic/synagogue official; more precise than
  "leader"; the Greek term is not πλούσιος (rich man) — his wealth emerges from context
- G4179 (πολλαπλασίων, v. 30): "many times more" (L/M/T) — the multiplication promise;
  matches the Greek's πολλαπλασίων (manifold); "many times over" (T)
- Aspect notes: The aorist in the blind man pericope (ἀνέβλεψεν, v43) is punctiliar —
  "instantly he received his sight" (T). The imperfect προσήρχοντο (v15, infants being
  brought) is iterative — "people were bringing."
- OT echo: "Son of David" cry (vv. 38–39) evokes the Davidic Messiah expectation;
  a blind man's faith contrasts sharply with the disciples' incomprehension (v34)
- Luke 18 contains no text-critically disputed verses in the major Greek manuscripts
"""
import json, pathlib

ROOT  = pathlib.Path(__file__).parent.parent
DRAFT = ROOT / 'data' / 'translation' / 'draft'

def load(tier, book):
    p = DRAFT / tier / f'{book}.json'
    if p.exists():
        return json.loads(p.read_text())
    return {}

def save(tier, book, data):
    p = DRAFT / tier / f'{book}.json'
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=None))
    print(f'  wrote {p.relative_to(ROOT)}')

def merge_tier(existing, new_data, tier_key):
    for ch, verses in new_data.items():
        if ch not in existing:
            existing[ch] = {}
        for v, tiers in verses.items():
            existing[ch][v] = tiers[tier_key]

LUKE_18 = {
 "18": {
  "1": {
   "L": "And he spoke a parable to them, to the end that they ought always to pray and not to lose heart,",
   "M": "Then Jesus told his disciples a parable to show them that they should always pray and not give up.",
   "T": "He told them a parable about why they should always pray and never give up."
  },
  "2": {
   "L": "saying: There was in a certain city a judge who neither feared God nor regarded man.",
   "M": "He said: In a certain city there was a judge who neither feared God nor cared what people thought.",
   "T": "He said: In a certain city there was a judge who had no fear of God and no concern for people."
  },
  "3": {
   "L": "And there was a widow in that city, and she kept coming to him, saying: Give me justice against my adversary.",
   "M": "And there was a widow in that city who kept coming to him with the plea: Grant me justice against my opponent.",
   "T": "In that city was a widow who kept coming to him, pleading: Give me justice against my opponent."
  },
  "4": {
   "L": "And for a time he was unwilling; but afterward he said within himself: Even if I neither fear God nor regard man,",
   "M": "For some time he refused. But finally he said to himself: Even though I don't fear God or care about people,",
   "T": "For a while he refused. But at last he said to himself: I care nothing for God or for people—"
  },
  "5": {
   "L": "yet because this widow keeps troubling me, I will give her justice, lest by her continual coming she wear me out.",
   "M": "yet because this widow keeps bothering me, I will see that she gets justice, so that she won't wear me down by her endless coming.",
   "T": "but because this widow won't stop troubling me, I will give her justice—before she finally wears me out completely."
  },
  "6": {
   "L": "And the Lord said: Hear what the unrighteous judge says.",
   "M": "And the Lord said: Listen to what the unjust judge says.",
   "T": "The Lord said: Listen to what this unjust judge says."
  },
  "7": {
   "L": "And shall not God avenge his elect, who cry to him day and night, though he bears long with them?",
   "M": "And will not God bring about justice for his chosen ones, who cry out to him day and night? Will he keep putting them off?",
   "T": "Will not God avenge his chosen ones who cry out to him day and night? Will he keep putting them off?"
  },
  "8": {
   "L": "I tell you that he will avenge them speedily. Nevertheless, when the Son of Man comes, will he find faith on the earth?",
   "M": "I tell you, he will see that they get justice, and quickly. However, when the Son of Man comes, will he find faith on the earth?",
   "T": "I tell you, he will give them justice—and quickly. But when the Son of Man comes, will he find faith on earth?"
  },
  "9": {
   "L": "He also spoke this parable to certain ones who trusted in themselves that they were righteous, and despised others:",
   "M": "To some who were confident of their own righteousness and looked down on everyone else, Jesus told this parable:",
   "T": "He told this parable to some who were sure of their own righteousness and looked down on everyone else:"
  },
  "10": {
   "L": "Two men went up to the temple to pray, one a Pharisee and the other a tax collector.",
   "M": "Two men went up to the temple to pray, one a Pharisee and the other a tax collector.",
   "T": "Two men went up to the temple to pray—one a Pharisee, the other a tax collector."
  },
  "11": {
   "L": "The Pharisee, standing, prayed thus with himself: God, I thank you that I am not like other men—swindlers, unrighteous, adulterers—or even like this tax collector.",
   "M": "The Pharisee stood and prayed about himself: God, I thank you that I am not like other people—robbers, evildoers, adulterers—or even like this tax collector.",
   "T": "The Pharisee stood and prayed about himself: God, I thank you that I am not like other people—thieves, wrongdoers, adulterers—or even like that tax collector."
  },
  "12": {
   "L": "I fast twice in the week; I give tithes of all that I get.",
   "M": "I fast twice a week and give a tenth of all I get.",
   "T": "I fast twice a week and give a tenth of everything I earn."
  },
  "13": {
   "L": "But the tax collector, standing far off, would not even lift up his eyes to heaven, but kept beating his breast, saying: God, be merciful to me, a sinner!",
   "M": "But the tax collector stood at a distance. He would not even look up towards heaven, but beat his breast and said: God, have mercy on me, a sinner.",
   "T": "But the tax collector stood at a distance and would not even look toward heaven. He beat his chest and cried: God, have mercy on me—I am a sinner!"
  },
  "14": {
   "L": "I tell you, this man went down to his house justified rather than the other; for everyone who exalts himself will be humbled, but the one who humbles himself will be exalted.",
   "M": "I tell you that this man, rather than the other, went home justified before God. For all those who exalt themselves will be humbled, and those who humble themselves will be exalted.",
   "T": "I tell you, this man went home right with God—the other did not. For everyone who exalts himself will be brought low, and everyone who humbles himself will be raised up."
  },
  "15": {
   "L": "And they were bringing even infants to him that he might touch them; but when his disciples saw it, they rebuked them.",
   "M": "People were also bringing babies to Jesus for him to place his hands on them. When the disciples saw this, they rebuked them.",
   "T": "People were bringing babies to him so he might touch them. When the disciples saw this, they rebuked the parents."
  },
  "16": {
   "L": "But Jesus called them to himself, saying: Let the little children come to me, and do not forbid them; for of such is the kingdom of God.",
   "M": "But Jesus called the children to him and said: Let the little children come to me, and do not hinder them, for the kingdom of God belongs to such as these.",
   "T": "Jesus called the children to himself and said: Let the little children come to me—don't stop them. The kingdom of God belongs to people like these."
  },
  "17": {
   "L": "Truly I say to you, whoever does not receive the kingdom of God as a little child does will in no wise enter into it.",
   "M": "Truly I tell you, anyone who will not receive the kingdom of God like a little child will never enter it.",
   "T": "Truly I tell you: whoever does not receive the kingdom of God like a child will never enter it."
  },
  "18": {
   "L": "And a certain ruler questioned him, saying: Good Teacher, what must I do to inherit eternal life?",
   "M": "A certain ruler asked him: Good teacher, what must I do to inherit eternal life?",
   "T": "A certain ruler asked him: Good Teacher, what must I do to inherit eternal life?"
  },
  "19": {
   "L": "And Jesus said to him: Why do you call me good? No one is good except God alone.",
   "M": "Why do you call me good? Jesus answered. No one is good—except God alone.",
   "T": "Jesus said to him: Why do you call me good? No one is good but God alone."
  },
  "20": {
   "L": "You know the commandments: Do not commit adultery, Do not kill, Do not steal, Do not bear false witness, Honor your father and your mother.",
   "M": "You know the commandments: Do not commit adultery, do not murder, do not steal, do not give false testimony, honour your father and mother.",
   "T": "You know the commandments: Do not commit adultery. Do not murder. Do not steal. Do not give false testimony. Honor your father and mother."
  },
  "21": {
   "L": "And he said: All these I have kept from my youth.",
   "M": "All these I have kept since I was a boy, he said.",
   "T": "All these I have kept from my youth, he said."
  },
  "22": {
   "L": "And when Jesus heard it, he said to him: One thing you still lack. Sell all that you have and distribute to the poor, and you will have treasure in heaven; and come, follow me.",
   "M": "When Jesus heard this, he said to him: You still lack one thing. Sell everything you have and give to the poor, and you will have treasure in heaven. Then come, follow me.",
   "T": "Hearing this, Jesus said to him: One thing you still lack. Sell everything you have and give to the poor—you will have treasure in heaven—and then come, follow me."
  },
  "23": {
   "L": "But when he heard these things, he became very sorrowful, for he was extremely rich.",
   "M": "When he heard this, he became very sad, because he was very wealthy.",
   "T": "Hearing this, he became deeply sorrowful—for he was very rich."
  },
  "24": {
   "L": "And Jesus, seeing that he had become very sorrowful, said: How difficult it is for those who have wealth to enter the kingdom of God!",
   "M": "Jesus looked at him and said: How hard it is for the rich to enter the kingdom of God!",
   "T": "Jesus, seeing how sorrowful he had become, said: How hard it is for the wealthy to enter the kingdom of God!"
  },
  "25": {
   "L": "For it is easier for a camel to go through the eye of a needle than for a rich man to enter the kingdom of God.",
   "M": "Indeed, it is easier for a camel to go through the eye of a needle than for someone who is rich to enter the kingdom of God.",
   "T": "It is easier for a camel to pass through the eye of a needle than for a rich person to enter the kingdom of God."
  },
  "26": {
   "L": "Those who heard said: Then who can be saved?",
   "M": "Those who heard this asked: Who then can be saved?",
   "T": "Those who heard this said: Then who can be saved?"
  },
  "27": {
   "L": "But he said: The things impossible with men are possible with God.",
   "M": "Jesus replied: What is impossible with man is possible with God.",
   "T": "He said: What is impossible for people is possible with God."
  },
  "28": {
   "L": "And Peter said: Behold, we have left our own things and followed you.",
   "M": "Peter said to him: We have left all we had to follow you.",
   "T": "Peter said: Look—we have left everything we had and followed you."
  },
  "29": {
   "L": "And he said to them: Truly I say to you, there is no one who has left house or wife or brothers or parents or children for the sake of the kingdom of God,",
   "M": "Truly I tell you, Jesus said to them, no one who has left home or wife or brothers or parents or children for the sake of the kingdom of God",
   "T": "He said to them: Truly I tell you—no one who has left home or wife or brothers or parents or children for the kingdom of God's sake"
  },
  "30": {
   "L": "who will not receive many times more in this present time, and in the age to come eternal life.",
   "M": "will fail to receive many times as much in this age, and in the age to come eternal life.",
   "T": "will fail to receive many times over in this life—and in the age to come, eternal life."
  },
  "31": {
   "L": "And he took the twelve to himself and said to them: Behold, we are going up to Jerusalem, and all things that are written through the prophets concerning the Son of Man will be accomplished.",
   "M": "Jesus took the Twelve aside and told them: We are going up to Jerusalem, and everything that is written by the prophets about the Son of Man will be fulfilled.",
   "T": "He took the Twelve aside and said: Look—we are going up to Jerusalem, and everything written through the prophets about the Son of Man will be fulfilled."
  },
  "32": {
   "L": "For he will be delivered over to the Gentiles, and will be mocked and shamefully treated and spat upon.",
   "M": "He will be handed over to the Gentiles. They will mock him, insult him and spit on him.",
   "T": "He will be handed over to the Gentiles—mocked, insulted, and spat upon."
  },
  "33": {
   "L": "And after they have scourged him, they will kill him; and on the third day he will rise.",
   "M": "They will flog him and kill him. On the third day he will rise again.",
   "T": "They will flog him and kill him. On the third day he will rise."
  },
  "34": {
   "L": "But they understood none of these things; this saying was hidden from them, and they did not know what was being said.",
   "M": "The disciples did not understand any of this. Its meaning was hidden from them, and they did not know what he was talking about.",
   "T": "But they understood none of it. The meaning was hidden from them, and they did not grasp what Jesus was saying."
  },
  "35": {
   "L": "And as he drew near to Jericho, a certain blind man was sitting by the road, begging.",
   "M": "As Jesus approached Jericho, a blind man was sitting by the roadside begging.",
   "T": "As he drew near to Jericho, a blind man sat by the road begging."
  },
  "36": {
   "L": "And hearing a crowd passing by, he asked what this might be.",
   "M": "When he heard the crowd going by, he asked what was happening.",
   "T": "Hearing the crowd passing by, he asked what was happening."
  },
  "37": {
   "L": "They told him: Jesus of Nazareth is passing by.",
   "M": "They told him: Jesus of Nazareth is passing by.",
   "T": "They told him: Jesus of Nazareth is passing by."
  },
  "38": {
   "L": "And he cried out, saying: Jesus, Son of David, have mercy on me!",
   "M": "He called out: Jesus, Son of David, have mercy on me!",
   "T": "He called out: Jesus, Son of David, have mercy on me!"
  },
  "39": {
   "L": "And those in front rebuked him so that he would be silent; but he cried out all the more: Son of David, have mercy on me!",
   "M": "Those who led the way rebuked him and told him to be quiet, but he shouted all the more: Son of David, have mercy on me!",
   "T": "Those in front rebuked him, telling him to be quiet. But he cried out all the louder: Son of David, have mercy on me!"
  },
  "40": {
   "L": "And Jesus stopped and commanded him to be brought to him. And when he came near, he asked him,",
   "M": "Jesus stopped and ordered the man to be brought to him. When he came near, Jesus asked him,",
   "T": "Jesus stopped and commanded that the man be brought to him. When he came close, Jesus asked him,"
  },
  "41": {
   "L": "saying: What do you want me to do for you? And he said: Lord, let me receive my sight.",
   "M": "What do you want me to do for you? Lord, I want to see, he replied.",
   "T": "What do you want me to do for you? Lord, he said, let me see again."
  },
  "42": {
   "L": "And Jesus said to him: Receive your sight; your faith has saved you.",
   "M": "Jesus said to him: Receive your sight; your faith has healed you.",
   "T": "Jesus said: Receive your sight—your faith has made you well."
  },
  "43": {
   "L": "And immediately he received his sight and followed him, glorifying God; and all the people, seeing it, gave praise to God.",
   "M": "Immediately he received his sight and followed Jesus, praising God. When all the people saw it, they also praised God.",
   "T": "Instantly he received his sight and followed Jesus, glorifying God—and when all the people saw it, they broke into praise to God."
  }
 }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'luke')
        merge_tier(existing, LUKE_18, tier_key)
        save(tier_dir, 'luke', existing)
    print('Luke 18 written.')

if __name__ == '__main__':
    main()
