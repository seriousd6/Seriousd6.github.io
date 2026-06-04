"""
MKT Luke chapter 19 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-luke-19-19.py

Translation decisions:
- G3414 (μνᾶ): "mina" (L/M/T) — NOT "pound" (KJV). The mina is a Greek monetary unit
  worth ~100 denarii (about 3 months' wages for a day-labourer). "Pound" obscures the
  economic stakes. Consistent with all three tiers throughout the parable (vv. 11–27).
- G754 (ἀρχιτελώνης): "chief tax collector" (L/M) / "head of the tax district" (T) —
  NOT "chief publican" (KJV, archaic). Zacchaeus supervised other collectors for Rome.
- G4809 (συκομορέα): "sycamore-fig tree" (L) / "sycamore tree" (M/T) — Ficus sycomorus,
  not the North American sycamore. The tree has low spreading branches suitable for
  climbing to see over a crowd.
- G3027 (λῃστής v.46): "robbers" (L/M) / "bandits" (T) — λῃστής is a violent brigand,
  stronger than κλέπτης (thief). Jeremiah 7:11 LXX uses the same word. "Den of robbers"
  (or bandits) names the commercial exploitation of a holy space.
- G4982 (σῴζω v.10): "save" (L/M) / "rescue" (T) — in the context of Zacchaeus, the
  soteriological sense is primary; T renders "rescue" to emphasize the directional act
  of seeking out what is lost.
- G4991 (σωτηρία v.9): "salvation" (L/M) / "salvation" (T) — the word stands; no
  deviation needed. But T makes explicit that it comes to the household.
- G1984 (ἐπισκοπή v.44): "visitation" (L/M) / "the hour when God came to you" (T) —
  ἐπισκοπή is the technical term for God's decisive coming to his people; in context
  the "visitation" is Jesus himself. T makes this explicit.
- G5482 (χάρακα v.43): "palisade" (L) / "siege works" (M/T) — a χάρακα is a military
  embankment or stake-palisade; the word evokes Roman siege warfare, specifically the
  circumvallation ditches and ramparts of Vespasian/Titus in 70 CE.
- G2962 (κύριος): "Lord" throughout when referring to Jesus (vv. 8, 16, 18, 20, 25, 31,
  34); "owners" (v.33 κύριοι = plural, the colt's owners) — Greek makes no distinction
  in spelling but context disambiguates clearly.
- G5207 τοῦ ἀνθρώπου (v.10): "Son of Man" in all three tiers — the titular usage is
  preserved; T does not smooth it away.
- v.38 OT echo: Psalm 118:26 (LXX) — "Blessed is he who comes in the name of the LORD."
  The Hallel psalm (sung at Passover) is deliberately applied to Jesus. T capitalises
  LORD to signal the divine name register.
- v.46 OT echoes: Isaiah 56:7 ("house of prayer") + Jeremiah 7:11 ("den of robbers").
  Luke omits "for all nations" (present in Mark 11:17) — T notes the covenantal breach
  rather than the universal mission angle.
- Aspect notes: aorist verbs in the parable of the minas (vv. 16–25) render as simple
  past or perfect ("has gained"). The present-tense narration of vv. 45–48 reflects
  the imperfect (ongoing action in temple precincts).
- v.13: The nobleman gives ten minas to ten servants (one each). The T tier clarifies
  this distribution, which the Greek implies but does not state explicitly.
- v.42 punctuation: The lament has an anacolouthon (broken syntax: "If you had
  known...!"); both M and T preserve the emotional interruption with a dash.
- Honour-shame dynamic: Zacchaeus's public pledge (v.8) is a shame-redemption act
  performed before the crowd that has just labelled him a sinner (v.7). T surfaces this.
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
    p.write_text(json.dumps(data, ensure_ascii=False, indent=None))
    print(f'  wrote {p.relative_to(ROOT)}')

def merge_tier(existing, new_data, tier_key):
    for ch, verses in new_data.items():
        if ch not in existing:
            existing[ch] = {}
        for v, tiers in verses.items():
            existing[ch][v] = tiers[tier_key]

LUKE_19 = {
 "19": {
  "1": {
   "L": "And having entered, he was passing through Jericho.",
   "M": "Jesus entered Jericho and was passing through.",
   "T": "He entered Jericho and made his way through it."
  },
  "2": {
   "L": "And behold, a man named Zacchaeus—and he was a chief tax collector—and he was rich.",
   "M": "A man was there by the name of Zacchaeus; he was a chief tax collector and was wealthy.",
   "T": "There was a man there named Zacchaeus—head of the local tax collectors and very rich."
  },
  "3": {
   "L": "And he was seeking to see who Jesus was, and could not because of the crowd, for he was small in stature.",
   "M": "He was trying to see who Jesus was, but could not because of the crowd, since he was short in stature.",
   "T": "He desperately wanted to see who Jesus was, but the crowd blocked him—he was too short to see over them."
  },
  "4": {
   "L": "And running ahead he climbed up a sycamore-fig tree to see him, for he was about to pass through that way.",
   "M": "So he ran ahead and climbed a sycamore tree to see him, since Jesus was going to pass that way.",
   "T": "He ran on ahead and climbed a sycamore tree to get a view—Jesus was about to pass that way."
  },
  "5": {
   "L": "And when he came to the place, Jesus looked up and said to him: Zacchaeus, hurry and come down, for today I must stay at your house.",
   "M": "When Jesus reached the spot, he looked up and said to him: Zacchaeus, come down immediately. I must stay at your house today.",
   "T": "When Jesus reached the spot, he looked up and said: Zacchaeus, come down quickly—I must stay at your house today."
  },
  "6": {
   "L": "And he hurried and came down and received him joyfully.",
   "M": "So he hurried and came down and welcomed him gladly.",
   "T": "He scrambled down at once and welcomed him with joy."
  },
  "7": {
   "L": "And when all saw it they began murmuring, saying that he had gone in to lodge with a sinful man.",
   "M": "All the people saw this and began to mutter: He has gone in to be the guest of a sinner.",
   "T": "Everyone who saw it grumbled: He has gone to be the guest of a sinner."
  },
  "8": {
   "L": "And standing, Zacchaeus said to the Lord: Behold, Lord, the half of my possessions I give to the poor, and if I have defrauded anyone of anything, I restore it fourfold.",
   "M": "But Zacchaeus stood up and said to the Lord: Look, Lord! Here and now I give half of my possessions to the poor, and if I have cheated anybody out of anything, I will pay back four times the amount.",
   "T": "But Zacchaeus rose to his feet and—in front of the whole crowd that had just called him a sinner—said to the Lord: Look, Lord! Right now I am giving half of everything I own to the poor, and if I have extorted anything from anyone, I will repay four times over."
  },
  "9": {
   "L": "And Jesus said to him: Today salvation has come to this house, since he also is a son of Abraham.",
   "M": "Jesus said to him: Today salvation has come to this house, because this man too is a son of Abraham.",
   "T": "Jesus said to him: Today, salvation has come to this household—for this man too is a son of Abraham."
  },
  "10": {
   "L": "For the Son of Man came to seek and to save the lost.",
   "M": "For the Son of Man came to seek and to save the lost.",
   "T": "The Son of Man came to seek out and rescue those who are lost."
  },
  "11": {
   "L": "And as they were hearing these things, he added and spoke a parable, because he was near Jerusalem and because they thought the kingdom of God was going to appear immediately.",
   "M": "While they were listening to this, he went on to tell them a parable, because he was near Jerusalem and the people thought the kingdom of God was going to appear at once.",
   "T": "While they were listening, he told a parable—because he was near Jerusalem and people were expecting the kingdom of God to break into view at any moment."
  },
  "12": {
   "L": "He said therefore: A certain man of noble birth went to a far country to receive for himself a kingdom and to return.",
   "M": "He said: A man of noble birth went to a distant country to have himself appointed king and then to return.",
   "T": "He said: A man of noble birth traveled to a distant land to be appointed king—and then to come back."
  },
  "13": {
   "L": "And calling ten of his servants he gave them ten minas and said to them: Do business until I come.",
   "M": "So he called ten of his servants, gave each one a mina, and said: Put this money to work until I come back.",
   "T": "He called ten of his servants and gave each one a mina—saying: Do business with this until I return."
  },
  "14": {
   "L": "But his citizens hated him and sent a delegation after him, saying: We do not want this man to reign over us.",
   "M": "But his subjects hated him and sent a delegation after him to say: We don't want this man to be our king.",
   "T": "But his own people hated him. They sent a delegation after him with this message: We will not have this man reign over us."
  },
  "15": {
   "L": "And it came to pass when he returned, having received the kingdom, that he ordered these servants to be called to him, to whom he had given the money, that he might know what they had gained by trading.",
   "M": "He was made king, however, and returned home. Then he sent for the servants to whom he had given the money, in order to find out what each had gained with it.",
   "T": "He received the kingship and came back. He summoned the servants he had given the money to—to find out what each had earned by trading."
  },
  "16": {
   "L": "And the first came, saying: Lord, your mina has gained ten minas.",
   "M": "The first one came and said: Sir, your mina has earned ten more minas.",
   "T": "The first came forward: Master, your one mina has earned ten more."
  },
  "17": {
   "L": "And he said to him: Well done, good servant! Because you have been faithful in a very little, you shall have authority over ten cities.",
   "M": "Well done, my good servant! his master replied. Because you have been trustworthy in a very small matter, take charge of ten cities.",
   "T": "He said to him: Well done, good servant! Because you proved faithful in a small thing, you will have authority over ten cities."
  },
  "18": {
   "L": "And the second came, saying: Your mina, Lord, has made five minas.",
   "M": "The second came and said: Sir, your mina has earned five minas.",
   "T": "The second came forward: Master, your mina has earned five more."
  },
  "19": {
   "L": "And he said to him also: And you, be over five cities.",
   "M": "His master answered: You take charge of five cities.",
   "T": "He said to this one: You will govern five cities."
  },
  "20": {
   "L": "And another came, saying: Lord, behold your mina, which I kept laid up in a cloth.",
   "M": "Then another servant came and said: Sir, here is your mina; I have kept it laid away in a piece of cloth.",
   "T": "Then another came: Master, here is your mina. I kept it wrapped in a cloth—I did nothing with it."
  },
  "21": {
   "L": "For I feared you, because you are an austere man; you take up what you did not put down and you reap what you did not sow.",
   "M": "I was afraid of you, because you are a hard man. You take out what you did not put in and reap what you did not sow.",
   "T": "I was afraid of you, because you are a hard man—you take what you did not deposit and harvest what you did not plant."
  },
  "22": {
   "L": "He says to him: By your own mouth I will judge you, wicked servant! You knew that I am an austere man, taking up what I did not put down and reaping what I did not sow.",
   "M": "His master replied: I will judge you by your own words, you wicked servant! You knew, did you, that I am a hard man, taking out what I did not put in and reaping what I did not sow?",
   "T": "He replied: I will judge you out of your own mouth, you wicked servant! You knew I was a hard man—taking what I did not deposit, harvesting what I did not plant?"
  },
  "23": {
   "L": "And why did you not put my money in the bank, so that at my coming I might have collected it with interest?",
   "M": "Then why didn't you put my money on deposit, so that when I came back I could have collected it with interest?",
   "T": "Then why didn't you at least put my money in the bank? When I returned, I could have collected it with interest."
  },
  "24": {
   "L": "And he said to those standing by: Take the mina from him and give it to the one who has ten minas.",
   "M": "Then he said to those standing by: Take his mina away from him and give it to the one who has ten minas.",
   "T": "He said to the bystanders: Take the mina from him and give it to the servant who has ten."
  },
  "25": {
   "L": "(And they said to him: Lord, he has ten minas!)",
   "M": "Sir, they said, he already has ten minas!",
   "T": "But Lord, they said, he already has ten minas!"
  },
  "26": {
   "L": "I tell you that to everyone who has it will be given; but from the one who does not have, even what he has will be taken from him.",
   "M": "He replied: I tell you that to everyone who has, more will be given; but as for the one who has nothing, even what they have will be taken away.",
   "T": "I tell you: to everyone who has, more will be given. But from the one who has nothing, even what little they have will be taken."
  },
  "27": {
   "L": "But those enemies of mine who did not want me to reign over them—bring them here and slaughter them before me.",
   "M": "But those enemies of mine who did not want me to be king over them—bring them here and kill them in front of me.",
   "T": "As for my enemies who refused to let me reign over them—bring them here and execute them before me."
  },
  "28": {
   "L": "And having said these things, he went ahead, ascending to Jerusalem.",
   "M": "After Jesus had said this, he went on ahead, going up to Jerusalem.",
   "T": "When he had said all this, he went on ahead, making his way up to Jerusalem."
  },
  "29": {
   "L": "And it came to pass, when he drew near to Bethphage and Bethany at the mountain called the Mount of Olives, he sent two of the disciples,",
   "M": "As he approached Bethphage and Bethany at the hill called the Mount of Olives, he sent two of his disciples,",
   "T": "As he neared Bethphage and Bethany, at the hill called the Mount of Olives, he sent two disciples ahead,"
  },
  "30": {
   "L": "saying: Go into the village ahead, in which upon entering you will find a colt tied, on which no one has yet ever sat; untie it and bring it.",
   "M": "saying: Go to the village ahead of you, and as you enter it you will find a colt tied there that no one has ever ridden. Untie it and bring it here.",
   "T": "saying: Go into the village straight ahead. As you enter it you will find a colt tied there—one no one has ever ridden. Untie it and bring it."
  },
  "31": {
   "L": "And if anyone asks you: Why are you untying it? you shall say thus: The Lord has need of it.",
   "M": "If anyone asks you: Why are you untying it? say: The Lord needs it.",
   "T": "If anyone asks why you are untying it, say: The Lord has need of it."
  },
  "32": {
   "L": "And those who were sent went and found it just as he had told them.",
   "M": "Those who were sent went and found it just as he had told them.",
   "T": "The two disciples went and found everything exactly as he had said."
  },
  "33": {
   "L": "And as they were untying the colt, its owners said to them: Why are you untying the colt?",
   "M": "As they were untying the colt, its owners asked them: Why are you untying the colt?",
   "T": "As they untied it, the owners asked: Why are you untying the colt?"
  },
  "34": {
   "L": "And they said: The Lord has need of it.",
   "M": "They replied: The Lord needs it.",
   "T": "They answered: The Lord has need of it."
  },
  "35": {
   "L": "And they led it to Jesus, and throwing their garments on the colt they set Jesus on it.",
   "M": "They brought it to Jesus, threw their cloaks on the colt and put Jesus on it.",
   "T": "They brought the colt to Jesus, threw their cloaks over it, and helped Jesus mount."
  },
  "36": {
   "L": "And as he went, they were spreading their garments on the road.",
   "M": "As he went along, people spread their cloaks on the road.",
   "T": "As he rode along, people spread their cloaks on the road before him."
  },
  "37": {
   "L": "And as he was drawing near, now at the descent of the Mount of Olives, the whole multitude of the disciples began to rejoice and to praise God with a loud voice for all the mighty works they had seen,",
   "M": "When he came near the place where the road goes down the Mount of Olives, the whole crowd of disciples began joyfully to praise God in loud voices for all the miracles they had seen:",
   "T": "As he descended the slope of the Mount of Olives, the entire crowd of disciples burst into joyful praise of God at the top of their voices—for all the mighty deeds they had witnessed:"
  },
  "38": {
   "L": "saying: Blessed is the King who comes in the name of the Lord! Peace in heaven and glory in the highest!",
   "M": "Blessed is the king who comes in the name of the Lord! Peace in heaven and glory in the highest!",
   "T": "Blessed is the King who comes in the name of the LORD! Peace in heaven—and glory in the highest heavens!"
  },
  "39": {
   "L": "And some of the Pharisees from the crowd said to him: Teacher, rebuke your disciples.",
   "M": "Some of the Pharisees in the crowd said to Jesus: Teacher, rebuke your disciples!",
   "T": "Some Pharisees in the crowd said to him: Teacher, order your disciples to stop!"
  },
  "40": {
   "L": "And he answered and said: I tell you, if these are silent, the stones will cry out.",
   "M": "I tell you, he replied, if they keep quiet, the stones will cry out.",
   "T": "He answered: I tell you—if they fell silent, the very stones would shout."
  },
  "41": {
   "L": "And as he drew near and saw the city, he wept over it,",
   "M": "As he approached Jerusalem and saw the city, he wept over it",
   "T": "As he came near and caught sight of the city, he wept over it,"
  },
  "42": {
   "L": "saying: If you had known—even you!—in this day the things for your peace! But now they are hidden from your eyes.",
   "M": "and said: If you, even you, had only known on this day what would bring you peace—but now it is hidden from your eyes.",
   "T": "saying: If only you had known—even you!—what belongs to your peace, on this very day. But now it is hidden from your sight."
  },
  "43": {
   "L": "For the days will come upon you when your enemies will cast a palisade around you and encircle you and press you in on every side,",
   "M": "The days will come upon you when your enemies will build an embankment against you and encircle you and hem you in on every side.",
   "T": "The days are coming when your enemies will throw up siege works all around you, encircle you, and press you in from every direction—"
  },
  "44": {
   "L": "and they will dash you to the ground, you and your children within you, and they will not leave in you one stone upon another, because you did not know the time of your visitation.",
   "M": "They will dash you to the ground, you and the children within your walls. They will not leave one stone on another, because you did not recognise the time of God's coming to you.",
   "T": "they will level you and your children within your walls to the ground, and will not leave one stone standing on another—because you did not recognise the hour when God came to you."
  },
  "45": {
   "L": "And entering the temple he began to cast out those who were selling,",
   "M": "When Jesus entered the temple courts, he began driving out those who were selling.",
   "T": "Entering the temple, he began to drive out those who were selling there,"
  },
  "46": {
   "L": "saying to them: It is written: My house shall be a house of prayer; but you have made it a den of robbers.",
   "M": "It is written, he said to them: My house will be a house of prayer; but you have made it a den of robbers.",
   "T": "saying to them: It stands written—My house shall be a house of prayer. But you have made it a den of bandits."
  },
  "47": {
   "L": "And he was teaching daily in the temple. But the chief priests and the scribes and the leading men of the people were seeking to destroy him,",
   "M": "Every day he was teaching at the temple. But the chief priests, the teachers of the law and the leaders among the people were trying to kill him.",
   "T": "Day after day he taught in the temple. But the chief priests, the scribes, and the leading men of the people were looking for a way to destroy him—"
  },
  "48": {
   "L": "and they could not find what they might do, for all the people were hanging upon him listening.",
   "M": "Yet they could not find any way to do it, because all the people were hanging on his words.",
   "T": "but could find no way to do it, because all the people were riveted to his every word."
  }
 }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'luke')
        merge_tier(existing, LUKE_19, tier_key)
        save(tier_dir, 'luke', existing)
    print('Luke 19 written.')

if __name__ == '__main__':
    main()
