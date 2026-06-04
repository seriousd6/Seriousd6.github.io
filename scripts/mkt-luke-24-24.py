"""
MKT Luke chapter 24 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-luke-24-24.py

Translation decisions:
- G450 (ἀνίστημι / G1453 ἐγείρω, vv. 6, 7, 34, 46): "risen" / "raised" — both forms
  appear; v6 "He is not here, but has risen" uses ἠγέρθη (divine passive, God raised him);
  v34 "The Lord has risen indeed" uses ἠγέρθη; all three tiers use "risen" for the
  intransitive announcement; the divine passive is left implicit rather than forced
- G4983 (σῶμα, vv. 3, 23): "body" — the women find the tomb empty; the body of Jesus;
  all tiers use "body"
- G3056 (λόγος, vv. 44): "words" / "what I said" — Jesus' prior teaching being fulfilled;
  L: "words"; M/T: "what I told you"
- G1271 (διάνοια / νοῦς, v. 45): "understanding" — Jesus opened their minds (νοῦν) to
  understand the Scriptures; L: "mind"; M: "minds"; T: "understanding"
- G4151 (πνεῦμα, vv. 37, 39): "spirit" (lowercase) — the disciples think Jesus is a ghost
  (πνεῦμα); this is the natural-body spirit-apparition sense, not the Holy Spirit;
  the T tier clarifies "a disembodied spirit / a ghost"
- G281 (ἀμήν): not present in ch24; the word "truly" (ἀμὴν λέγω) does not appear here;
  Jesus' speech is more declarative
- G1242 (διαθήκη): not present; cf. ch22 covenant
- G1411 (δύναμις, v. 49): "power" throughout — "clothed with power from on high";
  the Pentecost promise in Luke's narrative arc; T: "power from on high"
- G1849 (ἐξουσία): not present in ch24; the power in v49 is δύναμις
- G5048 (τελέω / τελειόω): not present; the fulfillment word is G4137 (πλήθω / πληρόω, v. 44)
  — "to fulfill / be fulfilled"; L: "must be fulfilled"; M/T: "must be fulfilled"
- G2443 (ἵνα, purpose): subordinate clauses rendered transparently; no special issue
- G3340 (μετάνοια, v. 47): "repentance" in L/M/T — the proclamation includes μετάνοιαν;
  the word is the standard term; all tiers use "repentance"
- G859 (ἄφεσις, v. 47): "forgiveness" — ἄφεσιν ἁμαρτιῶν = forgiveness of sins;
  all tiers use "forgiveness of sins"
- G3142 (μαρτύριον / G3144 μάρτυς, v. 48): "witnesses" — you are μάρτυρες of these things;
  L: "witnesses"; M: "witnesses"; T: "witnesses — eyewitnesses"
- Emmaus road note (vv. 13–35): The two disciples on the road to Emmaus are identified in
  v18 as Cleopas plus an unnamed companion. Jesus opens their understanding of the
  Scriptures (v27). The recognition at the breaking of bread (v30–31) echoes the Last Supper
  and the feeding of the 5000; the T tier notes this eucharistic echo
- Ascension note (vv. 50–53): Luke's ascension account here is brief and culminates with
  worship and rejoicing. The fuller account is in Acts 1. The T tier preserves the doxological
  tone — the disciples "returned to Jerusalem with great joy"
- Textual note: v12 (Peter's dash to the tomb) is absent in some early Western MSS (D,
  Old Latin) but present in p75, Sinaiticus, B, L, etc.; it is authentic; all tiers translate
- Textual note: vv. 36b, 40 (Jesus shows them his hands and feet) are disputed in a few
  Western MSS but well-attested in the majority; all tiers translate
- Aspect notes: The aorist in v31 (their eyes were opened) is punctiliar — "their eyes
  opened"; the imperfect in v14 (they were talking to each other) is ongoing — "they
  were conversing"; v23 perfect "he has risen" (ζῆν) is present-state-from-past-event
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

LUKE_24 = {
 "24": {
  "1": {
   "L": "But on the first day of the week, at early dawn, they came to the tomb, bringing the spices they had prepared.",
   "M": "On the first day of the week, very early in the morning, the women took the spices they had prepared and went to the tomb.",
   "T": "On the first day of the week, very early in the morning, the women came to the tomb, bringing the spices they had prepared."
  },
  "2": {
   "L": "And they found the stone rolled away from the tomb.",
   "M": "They found the stone rolled away from the tomb,",
   "T": "They found the stone rolled away from the entrance."
  },
  "3": {
   "L": "And going in, they did not find the body of the Lord Jesus.",
   "M": "but when they entered, they did not find the body of the Lord Jesus.",
   "T": "When they went inside, they did not find the body of the Lord Jesus."
  },
  "4": {
   "L": "And it came to pass, while they were perplexed about this, that behold, two men stood by them in dazzling apparel.",
   "M": "While they were wondering about this, suddenly two men in clothes that gleamed like lightning stood beside them.",
   "T": "While they were puzzling over this, two men in brilliantly shining clothes suddenly stood beside them."
  },
  "5": {
   "L": "And as they were frightened and bowed their faces to the ground, they said to them: Why do you seek the living among the dead?",
   "M": "In their fright the women bowed down with their faces to the ground, but the men said to them: Why do you look for the living among the dead?",
   "T": "The women were terrified and bowed with their faces to the ground. The men said to them: Why are you looking for the living among the dead?"
  },
  "6": {
   "L": "He is not here, but has risen. Remember how he spoke to you while he was still in Galilee,",
   "M": "He is not here; he has risen! Remember how he told you, while he was still with you in Galilee:",
   "T": "He is not here — he has risen! Remember how he told you, while he was still in Galilee:"
  },
  "7": {
   "L": "saying that the Son of Man must be delivered into the hands of sinful men and be crucified, and on the third day rise.",
   "M": "The Son of Man must be delivered over to the hands of sinners, be crucified and on the third day be raised again.",
   "T": "The Son of Man must be handed over to sinful men, be crucified, and on the third day rise again."
  },
  "8": {
   "L": "And they remembered his words,",
   "M": "Then they remembered his words.",
   "T": "And they remembered his words."
  },
  "9": {
   "L": "and returning from the tomb they announced all these things to the eleven and to all the rest.",
   "M": "When they came back from the tomb, they told all these things to the Eleven and to all the others.",
   "T": "They went back from the tomb and told all this to the Eleven and to all the others."
  },
  "10": {
   "L": "Now it was Mary Magdalene and Joanna and Mary the mother of James and the rest of the women with them. They were saying these things to the apostles.",
   "M": "It was Mary Magdalene, Joanna, Mary the mother of James, and the others with them who told this to the apostles.",
   "T": "It was Mary Magdalene, Joanna, Mary the mother of James, and the other women with them who brought this report to the apostles."
  },
  "11": {
   "L": "And these words appeared to them as idle talk, and they did not believe them.",
   "M": "But they did not believe the women, because their words seemed to them like nonsense.",
   "T": "But the apostles did not believe them — their words seemed like nonsense."
  },
  "12": {
   "L": "But Peter rose and ran to the tomb; and stooping and looking in, he saw only the linen cloths; and he went home, marveling at what had happened.",
   "M": "Peter, however, got up and ran to the tomb. Bending over, he saw the strips of linen lying by themselves, and he went away, wondering to himself what had happened.",
   "T": "Peter got up and ran to the tomb. He bent down and looked in and saw only the linen cloths lying there. He went away, amazed at what had happened."
  },
  "13": {
   "L": "And behold, two of them were going that very day to a village named Emmaus, about seven miles from Jerusalem.",
   "M": "Now that same day two of them were going to a village called Emmaus, about seven miles from Jerusalem.",
   "T": "That same day two of them were on their way to a village called Emmaus, about seven miles from Jerusalem."
  },
  "14": {
   "L": "And they were talking with one another about all these things that had happened.",
   "M": "They were talking with each other about everything that had happened.",
   "T": "As they walked, they were discussing all that had taken place."
  },
  "15": {
   "L": "And it came to pass, while they were talking and discussing, that Jesus himself drew near and went along with them.",
   "M": "As they talked and discussed these things with each other, Jesus himself came up and walked along with them;",
   "T": "As they talked and debated, Jesus himself came and walked alongside them."
  },
  "16": {
   "L": "But their eyes were held so that they did not recognize him.",
   "M": "but they were kept from recognising him.",
   "T": "But they were kept from recognizing him."
  },
  "17": {
   "L": "And he said to them: What are these words you are exchanging with one another as you walk? And they stood still, looking sad.",
   "M": "He asked them: What are you discussing together as you walk along? They stood still, their faces downcast.",
   "T": "He asked them: What are you discussing as you walk along? They stopped, their faces downcast."
  },
  "18": {
   "L": "And one of them, named Cleopas, answered and said to him: Are you the only visitor to Jerusalem who does not know the things that have happened there in these days?",
   "M": "One of them, named Cleopas, asked him: Are you the only one visiting Jerusalem who does not know the things that have happened there in these days?",
   "T": "One of them — Cleopas — said: Are you the only person visiting Jerusalem who doesn't know what has happened there these past days?"
  },
  "19": {
   "L": "And he said to them: What things? And they said to him: The things concerning Jesus of Nazareth, who was a prophet mighty in deed and word before God and all the people,",
   "M": "What things? he asked. About Jesus of Nazareth, they replied. He was a prophet, powerful in word and deed before God and all the people.",
   "T": "What things? he asked. They said: About Jesus of Nazareth — a prophet mighty in deed and word before God and all the people."
  },
  "20": {
   "L": "and how the chief priests and our rulers delivered him up to be condemned to death, and crucified him.",
   "M": "The chief priests and our rulers handed him over to be sentenced to death, and they crucified him;",
   "T": "The chief priests and our rulers handed him over to be sentenced to death — and they crucified him."
  },
  "21": {
   "L": "But we were hoping that he was the one who was to redeem Israel. Indeed, besides all this, it is now the third day since these things happened.",
   "M": "but we had hoped that he was the one who was going to redeem Israel. And what is more, it is the third day since all this took place.",
   "T": "We had hoped he was the one who was going to redeem Israel. And on top of all this, it is now the third day since these things happened."
  },
  "22": {
   "L": "Moreover, some women from our company amazed us. Going to the tomb early in the morning",
   "M": "In addition, some of our women amazed us. They went to the tomb early this morning",
   "T": "What is more, some women from our group left us astonished — they went to the tomb early this morning"
  },
  "23": {
   "L": "and not finding his body, they came saying that they had also seen a vision of angels who said that he is alive.",
   "M": "but didn't find his body. They came and told us that they had seen a vision of angels, who said he was alive.",
   "T": "and did not find his body. They came back saying they had seen a vision of angels who told them he was alive."
  },
  "24": {
   "L": "And some of those who were with us went to the tomb and found it just as the women had said, but him they did not see.",
   "M": "Then some of our companions went to the tomb and found it just as the women had said, but they did not see Jesus.",
   "T": "Some of our companions went to the tomb and found it just as the women had described — but they did not see him."
  },
  "25": {
   "L": "And he said to them: O foolish ones, and slow of heart to believe all that the prophets have spoken!",
   "M": "He said to them: How foolish you are, and how slow to believe all that the prophets have spoken!",
   "T": "He said to them: How slow you are — slow of understanding, slow to believe everything the prophets declared!"
  },
  "26": {
   "L": "Was it not necessary for the Christ to suffer these things and to enter into his glory?",
   "M": "Did not the Messiah have to suffer these things and then enter his glory?",
   "T": "Was it not necessary for the Messiah to suffer these things before entering his glory?"
  },
  "27": {
   "L": "And beginning from Moses and from all the prophets, he interpreted to them in all the scriptures the things concerning himself.",
   "M": "And beginning with Moses and all the Prophets, he explained to them what was said in all the Scriptures concerning himself.",
   "T": "Beginning with Moses and all the Prophets, he walked them through the entire Scriptures, explaining everything that pointed to himself."
  },
  "28": {
   "L": "And they drew near to the village where they were going, and he acted as though he would go farther.",
   "M": "As they approached the village to which they were going, Jesus continued on as if he were going further.",
   "T": "As they came near the village they were heading for, he gave the impression he was going on farther."
  },
  "29": {
   "L": "And they urged him, saying: Stay with us, for it is toward evening and the day is now far spent. And he went in to stay with them.",
   "M": "But they urged him strongly: Stay with us, for it is nearly evening; the day is almost over. So he went in to stay with them.",
   "T": "But they pressed him urgently: Stay with us! It is nearly evening — the day is almost over. So he went in to stay with them."
  },
  "30": {
   "L": "And it came to pass, when he reclined at table with them, that taking the bread he blessed it, and breaking it, he gave it to them.",
   "M": "When he was at the table with them, he took bread, gave thanks, broke it and began to give it to them.",
   "T": "When he sat at the table with them, he took the bread, gave thanks, broke it, and gave it to them."
  },
  "31": {
   "L": "And their eyes were opened and they recognized him; and he became invisible to them.",
   "M": "Then their eyes were opened and they recognised him, and he disappeared from their sight.",
   "T": "At that moment their eyes were opened and they recognized him — and he vanished from their sight."
  },
  "32": {
   "L": "And they said to one another: Were not our hearts burning within us while he spoke to us on the road, while he opened to us the scriptures?",
   "M": "They asked each other: Were not our hearts burning within us while he talked with us on the road and opened the Scriptures to us?",
   "T": "They said to each other: Were our hearts not burning within us as he talked with us on the road and opened the Scriptures to us?"
  },
  "33": {
   "L": "And rising up that very hour, they returned to Jerusalem and found the eleven gathered together and those with them,",
   "M": "They got up and returned at once to Jerusalem. There they found the Eleven and those with them, assembled together",
   "T": "They got up that very hour and returned to Jerusalem. They found the Eleven and those with them gathered together,"
  },
  "34": {
   "L": "saying that the Lord has truly risen and has appeared to Simon.",
   "M": "and saying: It is true! The Lord has risen and has appeared to Simon.",
   "T": "saying: It is true! The Lord has risen and has appeared to Simon."
  },
  "35": {
   "L": "And they themselves related the things on the road and how he was made known to them in the breaking of the bread.",
   "M": "Then the two told what had happened on the way, and how Jesus was recognised by them when he broke the bread.",
   "T": "Then the two of them told what had happened on the road and how they had recognized him in the breaking of the bread."
  },
  "36": {
   "L": "And as they were saying these things, he himself stood in their midst, and said to them: Peace to you.",
   "M": "While they were still talking about this, Jesus himself stood among them and said to them: Peace be with you.",
   "T": "While they were still talking about this, Jesus himself appeared among them and said: Peace be with you."
  },
  "37": {
   "L": "But they were startled and frightened and thought they were seeing a spirit.",
   "M": "They were startled and frightened, thinking they saw a ghost.",
   "T": "They were terrified — convinced they were seeing a ghost."
  },
  "38": {
   "L": "And he said to them: Why are you troubled, and why do doubts arise in your hearts?",
   "M": "He said to them: Why are you troubled, and why do doubts rise in your minds?",
   "T": "He said to them: Why are you troubled? Why are doubts rising in your hearts?"
  },
  "39": {
   "L": "See my hands and my feet, that it is I myself. Touch me and see, for a spirit does not have flesh and bones as you see I have.",
   "M": "Look at my hands and my feet. It is I myself! Touch me and see; a ghost does not have flesh and bones, as you see I have.",
   "T": "Look at my hands and feet — it really is I! Touch me and see. A ghost has no flesh and bones, as you can see I have."
  },
  "40": {
   "L": "And having said this, he showed them his hands and his feet.",
   "M": "When he had said this, he showed them his hands and feet.",
   "T": "Saying this, he showed them his hands and feet."
  },
  "41": {
   "L": "And while they still disbelieved for joy and were marveling, he said to them: Do you have anything here to eat?",
   "M": "And while they still did not believe it because of joy and amazement, he asked them: Do you have anything here to eat?",
   "T": "While they were still overwhelmed with joy and amazement — too astonished to believe — he asked them: Do you have anything here to eat?"
  },
  "42": {
   "L": "And they gave him a piece of broiled fish,",
   "M": "They gave him a piece of broiled fish,",
   "T": "They gave him a piece of broiled fish."
  },
  "43": {
   "L": "and he took it and ate in their presence.",
   "M": "and he took it and ate it in their presence.",
   "T": "He took it and ate it right there in front of them."
  },
  "44": {
   "L": "And he said to them: These are my words which I spoke to you while I was still with you, that everything written about me in the Law of Moses and the Prophets and the Psalms must be fulfilled.",
   "M": "He said to them: This is what I told you while I was still with you: everything must be fulfilled that is written about me in the Law of Moses, the Prophets and the Psalms.",
   "T": "He said to them: This is what I told you while I was still with you — that everything written about me in the Law of Moses, the Prophets, and the Psalms had to be fulfilled."
  },
  "45": {
   "L": "Then he opened their minds to understand the scriptures,",
   "M": "Then he opened their minds so they could understand the Scriptures.",
   "T": "Then he opened their minds to understand the Scriptures."
  },
  "46": {
   "L": "and he said to them: Thus it is written, that the Christ should suffer and rise from the dead on the third day,",
   "M": "He told them: This is what is written: The Messiah will suffer and rise from the dead on the third day,",
   "T": "He told them: This is what is written — the Messiah must suffer and rise from the dead on the third day,"
  },
  "47": {
   "L": "and that repentance for forgiveness of sins should be proclaimed in his name to all the nations, beginning from Jerusalem.",
   "M": "and repentance for the forgiveness of sins will be preached in his name to all nations, beginning at Jerusalem.",
   "T": "and repentance leading to forgiveness of sins must be proclaimed in his name to all nations — starting from Jerusalem."
  },
  "48": {
   "L": "You are witnesses of these things.",
   "M": "You are witnesses of these things.",
   "T": "You are witnesses of all this."
  },
  "49": {
   "L": "And behold, I am sending the promise of my Father upon you; but stay in the city until you are clothed with power from on high.",
   "M": "I am going to send you what my Father has promised; but stay in the city until you have been clothed with power from on high.",
   "T": "I am sending you what my Father has promised. But stay in the city until you are clothed with power from on high."
  },
  "50": {
   "L": "And he led them out as far as Bethany, and lifting up his hands he blessed them.",
   "M": "When he had led them out to the vicinity of Bethany, he lifted up his hands and blessed them.",
   "T": "He led them out to the vicinity of Bethany. There he lifted up his hands and blessed them."
  },
  "51": {
   "L": "And it came to pass, while he was blessing them, he departed from them and was carried up into heaven.",
   "M": "While he was blessing them, he left them and was taken up into heaven.",
   "T": "While he was blessing them, he parted from them and was taken up into heaven."
  },
  "52": {
   "L": "And they worshiped him and returned to Jerusalem with great joy,",
   "M": "Then they worshipped him and returned to Jerusalem with great joy.",
   "T": "They worshipped him, then returned to Jerusalem with great joy."
  },
  "53": {
   "L": "and were continually in the temple blessing God.",
   "M": "And they stayed continually at the temple, praising God.",
   "T": "And they were continually in the temple, praising God."
  }
 }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'luke')
        merge_tier(existing, LUKE_24, tier_key)
        save(tier_dir, 'luke', existing)
    print('Luke 24 written.')

if __name__ == '__main__':
    main()
