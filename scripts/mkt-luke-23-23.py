"""
MKT Luke chapter 23 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-luke-23-23.py

Translation decisions:
- G2917 (κρίμα, v. 40): "condemnation" in L/M; T "judgment" — the dying criminal acknowledges
  that their sentence is just; "condemnation" preserves the legal weight
- G3868 (παραιτέομαι, v. 18): "away with" — the crowd's cry; in context the phrase is
  the Greek equivalent of "Take him away"; all three tiers render it as "Away with"
- G5330 (Φαρισαῖος): not present in ch23 — the trial before the elders (council), not
  primarily a Pharisee dispute; the parties are chief priests, scribes, and elders
- G4561 (σάρξ): not present in ch23; no πνεῦμα/σάρξ theological tension in this chapter
- G2962 (κύριος, v. 42): "Lord" in v42 — the dying thief's address "Jesus, remember me
  when you come into your kingdom"; some MSS read "Lord" (κύριε) here explicitly
- G3857 (Παράδεισος, v. 43): "Paradise" in all three tiers — a technical term for the
  divine realm of the blessed dead (borrowed from Persian/LXX usage); do not substitute
  "heaven" as Paradise is the specific word Jesus uses, and the T tier notes its richness
- G2250 (ἡμέρα, v. 43): "today" (σήμερον) — the immediacy of the promise to the thief;
  all tiers preserve "today"; note that σήμερον is the word, not ἡμέρα
- G4893 (συνείδησις): not present; the "innocent" verdict from Pilate uses G3752 (αἴτιον)
  — "cause / charge / guilt" — L: "no guilt"; M: "no basis for a charge"; T: "nothing
  deserving death"
- G121 (ἀθῷος / αἴτιος, vv. 4, 14, 22): "no cause / fault / guilt" — three times Pilate
  declares Jesus innocent; L preserves the legal precision, M and T make it accessible
- G3689 (ὄντως, v. 47): "certainly / truly / indeed" — the centurion's declaration;
  L: "Truly"; M: "Surely"; T: "This man really was innocent / righteous" — the word
  δίκαιος (G1342) in v47 is the centurion's verdict: "righteous/innocent man"
- G1342 (δίκαιος, v. 47): "righteous" (L) / "innocent" (M) / "truly innocent, a righteous
  man" (T) — this is the centurion's declaration; both senses coexist: innocent of the
  charges and morally righteous; the T tier makes both explicit
- G5046 (τέλος): not present; the narrative moves to burial
- G1779 (ἐνταφιάζω / ἐντυλίσσω): not in Luke; Luke uses G1794 (ἐντυλίσσω, wrap/wind):
  "wrapped it" (v53) — refers to the linen cloth; all tiers use "wrapped"
- G4525 (σινδών, v. 53): "linen cloth / linen shroud" — L: "linen cloth"; M/T: "linen cloth"
- G3419 (μνῆμα / μνημεῖον, v. 53): "tomb" throughout — a rock-cut tomb in which no one
  had yet been laid
- Aspect notes: The imperfect forms in vv. 34–38 (casting lots, sneering) are iterative —
  they "kept dividing," "kept scoffing"; the T tier surfaces this through "kept" and
  "continued"
- OT echo: v34 "Father, forgive them" — echoes the Servant Song; Jesus fulfills Isaiah 53:12
  "he bore the sin of many and made intercession for the transgressors"; T tier notes
- Textual note: v34a ("Father, forgive them…") is absent in p75, Codex B, D*, W, and
  several ancient versions. However, it appears in א, A, C, L, and the majority text.
  The internal evidence favors authenticity (it's the kind of saying that might be
  deliberately omitted by scribes offended by the idea of forgiveness for Jerusalem).
  All three tiers translate it.
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

LUKE_23 = {
 "23": {
  "1": {
   "L": "And the whole multitude of them rose up and led him before Pilate.",
   "M": "Then the whole assembly rose and led him off to Pilate.",
   "T": "The entire assembly rose and brought Jesus to Pilate."
  },
  "2": {
   "L": "And they began to accuse him, saying: We found this man misleading our nation and forbidding the giving of tribute to Caesar, and saying that he himself is Christ, a king.",
   "M": "And they began to accuse him, saying: We have found this man subverting our nation. He opposes payment of taxes to Caesar and claims to be Messiah, a king.",
   "T": "They began their accusations: We found this man stirring up our nation, forbidding us to pay taxes to Caesar, and claiming to be the Messiah — a king."
  },
  "3": {
   "L": "And Pilate questioned him, saying: Are you the King of the Jews? And he answered him and said: You say so.",
   "M": "So Pilate asked Jesus: Are you the king of the Jews? You have said so, Jesus replied.",
   "T": "Pilate asked him: Are you the king of the Jews? Jesus answered: That is what you say."
  },
  "4": {
   "L": "And Pilate said to the chief priests and the crowds: I find no guilt in this man.",
   "M": "Then Pilate announced to the chief priests and the crowd: I find no basis for a charge against this man.",
   "T": "Pilate announced to the chief priests and the crowd: I find no charge against this man."
  },
  "5": {
   "L": "But they were insistent, saying: He stirs up the people, teaching throughout all Judea, beginning from Galilee even to here.",
   "M": "But they insisted: He stirs up the people all over Judea by his teaching. He started in Galilee and has come all the way here.",
   "T": "But they pressed harder: He is inciting the people with his teaching — all through Judea, from Galilee all the way to here."
  },
  "6": {
   "L": "When Pilate heard this, he asked whether the man was a Galilean.",
   "M": "On hearing this, Pilate asked if the man was a Galilean.",
   "T": "When Pilate heard this, he asked whether Jesus was from Galilee."
  },
  "7": {
   "L": "And when he learned that he was under Herod's jurisdiction, he sent him to Herod, who was himself also in Jerusalem in those days.",
   "M": "When he learned that Jesus was under Herod's jurisdiction, he sent him to Herod, who was also in Jerusalem at that time.",
   "T": "Learning that Jesus was under Herod's authority, he sent him to Herod, who was also in Jerusalem at that time."
  },
  "8": {
   "L": "Now when Herod saw Jesus, he was very glad, for he had been wanting to see him for a long time, because he had heard about him, and was hoping to see some sign done by him.",
   "M": "When Herod saw Jesus, he was greatly pleased, because for a long time he had been wanting to see him. From what he had heard about him, he hoped to see him perform a sign of some sort.",
   "T": "Herod was delighted to see Jesus — he had wanted to meet him for a long time. He had heard about him and was hoping to see him perform some miracle."
  },
  "9": {
   "L": "And he questioned him at length, but he answered him nothing.",
   "M": "He plied him with many questions, but Jesus gave him no answer.",
   "T": "He questioned Jesus at length, but Jesus said nothing."
  },
  "10": {
   "L": "And the chief priests and the scribes were standing by, vehemently accusing him.",
   "M": "The chief priests and the teachers of the law were standing there, vehemently accusing him.",
   "T": "The chief priests and teachers of the law stood there, hurling their accusations."
  },
  "11": {
   "L": "And Herod, with his soldiers, treating him with contempt and mocking him, dressed him in splendid clothing and sent him back to Pilate.",
   "M": "Then Herod and his soldiers ridiculed and mocked him. Dressing him in an elegant robe, they sent him back to Pilate.",
   "T": "Then Herod and his soldiers mocked and ridiculed him. They put a splendid robe on him and sent him back to Pilate."
  },
  "12": {
   "L": "And Herod and Pilate became friends with one another that very day, for before this they had been at enmity with each other.",
   "M": "That day Herod and Pilate became friends — before this they had been enemies.",
   "T": "That very day Herod and Pilate became friends — they had been enemies before."
  },
  "13": {
   "L": "And Pilate summoned the chief priests and the rulers and the people,",
   "M": "Pilate called together the chief priests, the rulers and the people,",
   "T": "Pilate called together the chief priests, the rulers, and the people."
  },
  "14": {
   "L": "and said to them: You brought me this man as one who was misleading the people. And behold, having examined him before you, I found no guilt in this man in any of the charges that you bring against him.",
   "M": "and said to them: You brought me this man as one who was inciting the people to rebellion. I have examined him in your presence and have found no basis for your charges against him.",
   "T": "He told them: You brought me this man as someone who was stirring up the people. I have examined him in your presence and found no basis whatsoever for your charges."
  },
  "15": {
   "L": "Neither did Herod, for he sent him back to us. Behold, nothing deserving death has been done by him.",
   "M": "Neither has Herod, for he sent him back to us; as you can see, he has done nothing to deserve death.",
   "T": "Nor has Herod — he sent him back to us. As you can see, this man has done nothing deserving death."
  },
  "16": {
   "L": "Therefore I will punish him and release him.",
   "M": "Therefore, I will punish him and then release him.",
   "T": "So I will have him flogged and then release him."
  },
  "17": {
   "L": "Now he was obligated to release one prisoner to them at the feast.",
   "M": "Now it was necessary for him to release one prisoner to them at the festival.",
   "T": "For it was the custom at the feast for him to release one prisoner to the people."
  },
  "18": {
   "L": "But they all cried out together, saying: Away with this man, and release to us Barabbas!",
   "M": "But the whole crowd shouted: Away with this man! Release Barabbas to us!",
   "T": "But they all shouted together: Away with this man! Release Barabbas to us!"
  },
  "19": {
   "L": "(who was one who had been thrown into prison for insurrection and murder that had taken place in the city).",
   "M": "(Barabbas had been thrown into prison for an insurrection in the city, and for murder.)",
   "T": "(Barabbas had been imprisoned for starting a rebellion in the city and for murder.)"
  },
  "20": {
   "L": "Pilate, wishing to release Jesus, addressed them again.",
   "M": "Wanting to release Jesus, Pilate appealed to them again.",
   "T": "Wanting to release Jesus, Pilate appealed to them a second time."
  },
  "21": {
   "L": "But they were shouting, saying: Crucify! Crucify him!",
   "M": "But they kept shouting: Crucify him! Crucify him!",
   "T": "But they kept shouting: Crucify him! Crucify him!"
  },
  "22": {
   "L": "And he said to them a third time: Why? What evil has this man done? I found in him no guilt deserving death. I will therefore punish him and release him.",
   "M": "For the third time he spoke to them: Why? What crime has this man committed? I have found in him no grounds for the death penalty. Therefore I will have him punished and then release him.",
   "T": "A third time he said to them: What crime has this man committed? I found nothing in him deserving death. I will have him flogged and release him."
  },
  "23": {
   "L": "But they were persistent with loud voices, demanding that he be crucified; and their voices prevailed.",
   "M": "But with loud shouts they insistently demanded that he be crucified, and their shouts prevailed.",
   "T": "But they shouted louder and louder, insisting that he be crucified — and their demands won."
  },
  "24": {
   "L": "And Pilate decided that their request should be granted.",
   "M": "So Pilate decided to grant their demand.",
   "T": "Pilate gave in and granted their demand."
  },
  "25": {
   "L": "And he released the one they asked for, who had been thrown into prison for insurrection and murder, but he delivered Jesus over to their will.",
   "M": "He released the man who had been thrown into prison for insurrection and murder, the one they asked for, and surrendered Jesus to their will.",
   "T": "He released the man imprisoned for insurrection and murder — the very one they demanded — and handed Jesus over to their will."
  },
  "26": {
   "L": "And as they led him away, they seized a certain Simon of Cyrene who was coming from the country, and they put the cross on him to carry behind Jesus.",
   "M": "As the soldiers led him away, they seized Simon from Cyrene, who was on his way in from the country, and put the cross on him and made him carry it behind Jesus.",
   "T": "As they led Jesus away, they seized a man named Simon of Cyrene who was coming in from the countryside. They laid the cross on him to carry behind Jesus."
  },
  "27": {
   "L": "And there was following him a great multitude of the people, and of women who were mourning and lamenting him.",
   "M": "A large number of people followed him, including women who mourned and wailed for him.",
   "T": "A great crowd followed, including women who were mourning and wailing for him."
  },
  "28": {
   "L": "But turning to them Jesus said: Daughters of Jerusalem, do not weep for me, but weep for yourselves and for your children.",
   "M": "Jesus turned and said to them: Daughters of Jerusalem, do not weep for me; weep for yourselves and for your children.",
   "T": "Jesus turned to them and said: Daughters of Jerusalem, do not weep for me — weep for yourselves and for your children."
  },
  "29": {
   "L": "For behold, the days are coming in which they will say: Blessed are the barren, and the wombs that never bore, and the breasts that never nursed.",
   "M": "For the time will come when you will say: Blessed are the childless women, the wombs that never bore and the breasts that never nursed!",
   "T": "For the days are coming when people will say: How fortunate are the childless women — those who never bore children and never nursed them!"
  },
  "30": {
   "L": "Then they will begin to say to the mountains: Fall on us! and to the hills: Cover us!",
   "M": "Then they will say to the mountains: Fall on us! and to the hills: Cover us!",
   "T": "Then people will cry to the mountains: Fall on us! and to the hills: Cover us!"
  },
  "31": {
   "L": "For if they do these things when the wood is green, what will happen when it is dry?",
   "M": "For if people do these things when the tree is green, what will happen when it is dry?",
   "T": "For if they do these things when the wood is green — to an innocent man — what will they do when it is dry, and judgment falls on the guilty?"
  },
  "32": {
   "L": "And two others also, who were criminals, were being led away with him to be executed.",
   "M": "Two other men, both criminals, were also led out with him to be executed.",
   "T": "Two other men — both criminals — were led out to be executed with him."
  },
  "33": {
   "L": "And when they came to the place called The Skull, there they crucified him and the criminals, one on the right and one on the left.",
   "M": "When they came to the place called the Skull, they crucified him there, along with the criminals — one on his right, the other on his left.",
   "T": "When they reached the place called The Skull, they crucified him there — and the two criminals with him, one on his right, one on his left."
  },
  "34": {
   "L": "And Jesus said: Father, forgive them, for they do not know what they are doing. And they divided his garments, casting lots.",
   "M": "Jesus said: Father, forgive them, for they do not know what they are doing. And they divided up his clothes by casting lots.",
   "T": "Jesus said: Father, forgive them — they do not know what they are doing. They divided his clothes by casting lots."
  },
  "35": {
   "L": "And the people were standing by watching; and the rulers were sneering, saying: He saved others; let him save himself, if this is the Christ of God, his Chosen One.",
   "M": "The people stood watching, and the rulers even sneered at him. They said: He saved others; let him save himself if he is God's Messiah, the Chosen One.",
   "T": "The crowd stood watching. The rulers kept sneering: He saved others — let him save himself, if he really is the Messiah of God, the Chosen One!"
  },
  "36": {
   "L": "The soldiers also mocked him, coming up and offering him sour wine,",
   "M": "The soldiers also came up and mocked him. They offered him wine vinegar",
   "T": "The soldiers also mocked him — coming up and offering him sour wine,"
  },
  "37": {
   "L": "and saying: If you are the King of the Jews, save yourself!",
   "M": "and said: If you are the king of the Jews, save yourself.",
   "T": "saying: If you are the King of the Jews, save yourself!"
  },
  "38": {
   "L": "And there was also an inscription above him: This is the King of the Jews.",
   "M": "There was a written notice above him, which read: This is the King of the Jews.",
   "T": "An inscription above him read: This is the King of the Jews."
  },
  "39": {
   "L": "One of the criminals hanging there was insulting him, saying: Are you not the Christ? Save yourself and us!",
   "M": "One of the criminals who hung there hurled insults at him: Aren't you the Messiah? Save yourself and us!",
   "T": "One of the criminals hanging beside him kept hurling abuse: Aren't you the Messiah? Save yourself — and us!"
  },
  "40": {
   "L": "But the other answered, rebuking him, saying: Do you not fear God, since you are under the same condemnation?",
   "M": "But the other criminal rebuked him: Don't you fear God, since you are under the same sentence?",
   "T": "But the other criminal rebuked him: Do you not fear God? We are under the same condemnation."
  },
  "41": {
   "L": "And we indeed are here justly, for we are receiving what our deeds deserve. But this man has done nothing wrong.",
   "M": "We are punished justly, for we are getting what our deeds deserve. But this man has done nothing wrong.",
   "T": "We deserve our sentence — we are getting exactly what our actions earned. But this man has done nothing wrong."
  },
  "42": {
   "L": "And he said: Jesus, remember me when you come into your kingdom.",
   "M": "Then he said: Jesus, remember me when you come into your kingdom.",
   "T": "Then he said: Jesus, remember me when you come into your kingdom."
  },
  "43": {
   "L": "And he said to him: Truly I say to you, today you will be with me in Paradise.",
   "M": "Jesus answered him: Truly I tell you, today you will be with me in paradise.",
   "T": "Jesus said to him: Truly I tell you — today you will be with me in Paradise."
  },
  "44": {
   "L": "And it was now about the sixth hour, and darkness came over the whole land until the ninth hour,",
   "M": "It was now about noon, and darkness came over the whole land until three in the afternoon,",
   "T": "It was about noon when darkness fell over the whole land, lasting until three in the afternoon."
  },
  "45": {
   "L": "the sun having failed. And the curtain of the temple was torn in two.",
   "M": "for the sun stopped shining. And the curtain of the temple was torn in two.",
   "T": "The sun stopped shining. And the curtain of the temple was torn in two."
  },
  "46": {
   "L": "And crying out with a loud voice, Jesus said: Father, into your hands I commit my spirit! And having said this, he breathed his last.",
   "M": "Jesus called out with a loud voice: Father, into your hands I commit my spirit! When he had said this, he breathed his last.",
   "T": "Then Jesus cried out with a loud voice: Father, into your hands I commit my spirit! Having said this, he breathed his last."
  },
  "47": {
   "L": "Now the centurion, seeing what happened, glorified God, saying: Truly this man was righteous.",
   "M": "The centurion, seeing what had happened, praised God and said: Surely this was a righteous man.",
   "T": "When the centurion saw what had happened, he glorified God and said: This man truly was innocent — a righteous man."
  },
  "48": {
   "L": "And all the crowds who had gathered for this spectacle, when they saw what had happened, returned home beating their breasts.",
   "M": "When all the people who had gathered to witness this sight saw what took place, they beat their breasts and went away.",
   "T": "All the crowds who had gathered for this spectacle, when they saw what had happened, went home beating their chests in grief."
  },
  "49": {
   "L": "And all his acquaintances and the women who had followed him from Galilee were standing at a distance watching these things.",
   "M": "But all those who knew him, including the women who had followed him from Galilee, stood at a distance, watching these things.",
   "T": "All his acquaintances and the women who had followed him from Galilee stood watching from a distance."
  },
  "50": {
   "L": "And behold, a man named Joseph, who was a member of the council, a good and righteous man",
   "M": "Now there was a man named Joseph, a member of the Council, a good and upright man,",
   "T": "Now there was a man named Joseph — a member of the Council, a good and righteous man —"
  },
  "51": {
   "L": "— this man had not consented to their purpose and deed — who was from Arimathea, a city of the Jews, who was waiting for the kingdom of God.",
   "M": "who had not consented to their decision and action. He came from the Judean town of Arimathea, and he himself was waiting for the kingdom of God.",
   "T": "who had not agreed with the Council's decision and action. He was from Arimathea, a town in Judea, and he was himself looking forward to the kingdom of God."
  },
  "52": {
   "L": "This man went to Pilate and asked for the body of Jesus.",
   "M": "Going to Pilate, he asked for Jesus' body.",
   "T": "He went to Pilate and asked for Jesus' body."
  },
  "53": {
   "L": "And taking it down, he wrapped it in a linen cloth and laid it in a tomb cut in stone, where no one had ever yet been laid.",
   "M": "Then he took it down, wrapped it in linen cloth and placed it in a tomb cut in the rock, one in which no one had yet been laid.",
   "T": "He took the body down, wrapped it in a linen cloth, and placed it in a rock-cut tomb where no one had ever been buried."
  },
  "54": {
   "L": "And it was the day of Preparation, and the Sabbath was drawing on.",
   "M": "It was Preparation Day, and the Sabbath was about to begin.",
   "T": "It was Preparation Day, and the Sabbath was beginning."
  },
  "55": {
   "L": "And the women who had come with him from Galilee followed after and saw the tomb and how his body was laid.",
   "M": "The women who had come with Jesus from Galilee followed Joseph and saw the tomb and how his body was laid in it.",
   "T": "The women who had come with Jesus from Galilee followed and saw the tomb and how his body was laid."
  },
  "56": {
   "L": "And they returned and prepared spices and ointments. And on the Sabbath they rested according to the commandment.",
   "M": "Then they went home and prepared spices and perfumes. But they rested on the Sabbath in obedience to the commandment.",
   "T": "Then they went home and prepared spices and perfumes. They rested on the Sabbath, as the commandment required."
  }
 }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'luke')
        merge_tier(existing, LUKE_23, tier_key)
        save(tier_dir, 'luke', existing)
    print('Luke 23 written.')

if __name__ == '__main__':
    main()
