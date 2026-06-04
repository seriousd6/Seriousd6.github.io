"""
MKT 1 John chapters 4–5 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-1john-4-5.py

Translation decisions:
- G26 (ἀγάπη): "love" across all tiers — willed, covenantal, self-giving as distinct from φιλία.
  T tier surfaces the originating, initiative-taking quality of divine love explicitly.
- G4151 (πνεῦμα): "Spirit" (capitalised) when referring to the Holy Spirit (4:2, 4:6, 4:13,
  5:6-8); lowercase "spirit" for created or demonic spirits (4:1, 4:3). Greek lacks capitals;
  context determines the referent.
- G3306 (μένω): "abide" in L (source-accurate); "live in / dwell in" in M; T varies by context —
  "dwell in," "live in," "at home in" to honour the intimacy the verb carries.
- G2434 (ἱλασμός): "propitiation" in L (forensic accuracy); "atoning sacrifice" in M (ESV/NIV
  consensus); T: "atoning death" — preserves the propitiation concept without jargon.
- G3439 (μονογενής): "only-begotten" in L; "one and only Son" in M; "unique and beloved Son" in T.
- G166 (αἰώνιος): "eternal" in L/M (conventional rendering); T: "age-to-come" / "eternal" —
  John's use in 5:11-13,20 points to the quality of resurrection life, not merely duration.
- G4102 (πίστις): "faith" in L/M; T: "faith" — in 5:4 the article (ἡ νίκη... ἡ πίστις ἡμῶν)
  focuses on "our faith" as the specific instrument of victory over the world.
- G5547 (χριστός): "Christ" as title throughout — in 5:1 "the Christ" reflects the
  Greek article (τὸν Χριστόν), carrying the full messianic weight of the term.
- Textual note — 5:7: The Comma Johanneum (a Trinitarian clause found in some Latin mss,
  inserted as "the Father, the Word, and the Holy Ghost: and these three are one") is absent
  from all early Greek manuscripts and is not original. The authentic text of 5:7 is only
  "For there are three that testify:" and continues at 5:8 with the earthly witnesses.
  Our translation follows the critical Greek text (UBS5/NA28).
- G4190 (πονηρός): "the evil one" consistently (4:—, 5:18-19) — John's personalised usage
  (ὁ πονηρός with article) refers to Satan, not abstract evil.
- Sin "unto death" (5:16): not translated with commentary; left as "sin that leads to death"
  in M and T, acknowledging the long interpretive debate without resolving it in the text.
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

JOHN1 = {
  "4": {
    "1": {
      "L": "Beloved, not every spirit believe, but test the spirits whether they are from God, because many false prophets have gone out into the world.",
      "M": "Dear friends, do not believe every spirit, but test the spirits to see whether they are from God, for many false prophets have gone out into the world.",
      "T": "Dear friends, do not be credulous about every spiritual claim—test them to see which ones come from God. The reason is urgent: many false prophets have spread through the world."
    },
    "2": {
      "L": "By this you know the Spirit of God: every spirit that confesses Jesus Christ having come in flesh is from God,",
      "M": "This is how you can recognize the Spirit of God: Every spirit that acknowledges that Jesus Christ has come in the flesh is from God,",
      "T": "Here is how to recognize the Spirit of God: every spirit that openly confesses Jesus Christ as truly come in human flesh is from God,"
    },
    "3": {
      "L": "and every spirit that does not confess Jesus is not from God; and this is the spirit of the antichrist, which you have heard that it comes, and now is already in the world.",
      "M": "but every spirit that does not acknowledge Jesus is not from God. This is the spirit of the antichrist, which you have heard is coming and even now is already in the world.",
      "T": "but any spirit that refuses to confess Jesus is not from God—it is the spirit of antichrist. You have been warned this spirit is coming, and it is already at work in the world right now."
    },
    "4": {
      "L": "You are from God, little children, and have overcome them, because greater is he who is in you than he who is in the world.",
      "M": "You, dear children, are from God and have overcome them, because the one who is in you is greater than the one who is in the world.",
      "T": "But you, dear children, are from God, and you have conquered these spirits—because the One living inside you is far more powerful than the one at work in the world."
    },
    "5": {
      "L": "They are from the world; therefore they speak from the world, and the world hears them.",
      "M": "They are from the world and therefore speak from the world's perspective, and the world listens to them.",
      "T": "These false prophets belong to the world, so they speak its language, and the world recognizes its own voice and listens."
    },
    "6": {
      "L": "We are from God; he who knows God hears us, he who is not from God does not hear us. By this we know the Spirit of truth and the spirit of error.",
      "M": "We are from God, and whoever knows God listens to us; but whoever is not from God does not listen to us. This is how we recognize the Spirit of truth and the spirit of falsehood.",
      "T": "We are from God. Anyone who truly knows God will hear our message; anyone who is not from God will not. This is the test that distinguishes the Spirit of truth from the spirit of deception."
    },
    "7": {
      "L": "Beloved, let us love one another, because love is from God, and everyone who loves has been born of God and knows God.",
      "M": "Dear friends, let us love one another, for love comes from God. Everyone who loves has been born of God and knows God.",
      "T": "Dear friends, let us love one another with genuine love. Love itself originates in God, and everyone who loves demonstrates that they have been born of God and truly know him."
    },
    "8": {
      "L": "The one who does not love has not known God, because God is love.",
      "M": "Whoever does not love does not know God, because God is love.",
      "T": "But anyone who does not love has not truly known God at all—for God is love. That is his very nature."
    },
    "9": {
      "L": "In this the love of God was manifested toward us, that God sent his only-begotten Son into the world so that we might live through him.",
      "M": "This is how God showed his love among us: He sent his one and only Son into the world that we might live through him.",
      "T": "And here is how God's love became visible and concrete: he sent his unique, beloved Son into the world so that through him we might have life."
    },
    "10": {
      "L": "In this is love—not that we loved God but that he loved us and sent his Son as propitiation for our sins.",
      "M": "This is love: not that we loved God, but that he loved us and sent his Son as an atoning sacrifice for our sins.",
      "T": "And here is the true definition of love—not that we initiated anything toward God, but that he first loved us and sent his Son to deal with our sins through his atoning death."
    },
    "11": {
      "L": "Beloved, if God so loved us, we also ought to love one another.",
      "M": "Dear friends, since God so loved us, we also ought to love one another.",
      "T": "Dear friends, if God loved us with that kind of love, then loving one another is not optional—it is the only fitting response."
    },
    "12": {
      "L": "No one has ever seen God; if we love one another, God abides in us and his love has been perfected in us.",
      "M": "No one has ever seen God; but if we love one another, God lives in us and his love is made complete in us.",
      "T": "No human eye has ever seen God directly; but when we love one another, God lives in us and his love reaches its full, intended purpose in us."
    },
    "13": {
      "L": "By this we know that we abide in him and he in us, that he has given us of his Spirit.",
      "M": "This is how we know that we live in him and he in us: He has given us of his Spirit.",
      "T": "Here is how we know we dwell in him and he in us: he has shared his Spirit with us."
    },
    "14": {
      "L": "And we have seen and testify that the Father has sent the Son as Savior of the world.",
      "M": "And we have seen and testify that the Father has sent his Son to be the Savior of the world.",
      "T": "We are eyewitnesses to this, and we are declaring it publicly: the Father sent his Son to be the Savior of the world."
    },
    "15": {
      "L": "Whoever confesses that Jesus is the Son of God, God abides in him and he in God.",
      "M": "If anyone acknowledges that Jesus is the Son of God, God lives in them and they in God.",
      "T": "Whoever publicly declares that Jesus is the Son of God—God lives in that person, and that person lives in God."
    },
    "16": {
      "L": "And we have known and believed the love that God has for us. God is love, and he who abides in love abides in God, and God abides in him.",
      "M": "And so we know and rely on the love God has for us. God is love. Whoever lives in love lives in God, and God lives in them.",
      "T": "We have come to know, and to rest our whole weight upon, the love God has for us. The conclusion stands: God is love—and whoever lives in love lives in God, and God lives in them."
    },
    "17": {
      "L": "In this is love perfected with us, that we may have boldness in the day of judgment, because as he is so also are we in this world.",
      "M": "This is how love is made complete among us so that we will have confidence on the day of judgment: In this world we are like him.",
      "T": "And here is love's goal brought to completion: we stand before the judgment seat with boldness—not because we are innocent, but because we are united to him, and as he is, so are we in this world."
    },
    "18": {
      "L": "There is no fear in love, but perfect love casts out fear, because fear involves punishment, and the one who fears has not been perfected in love.",
      "M": "There is no fear in love. But perfect love drives out fear, because fear has to do with punishment. The one who fears is not made perfect in love.",
      "T": "Fear has no place where love is fully at home. Perfect love expels fear—because fear is always anticipating punishment. Anyone still caught in fear has not yet been brought to maturity in love."
    },
    "19": {
      "L": "We love, because he first loved us.",
      "M": "We love because he first loved us.",
      "T": "We are only capable of loving at all because he loved us first."
    },
    "20": {
      "L": "If anyone says, 'I love God,' and hates his brother, he is a liar; for he who does not love his brother whom he has seen cannot love God whom he has not seen.",
      "M": "Whoever claims to love God yet hates a brother or sister is a liar. For whoever does not love their brother and sister, whom they have seen, cannot love God, whom they have not seen.",
      "T": "Anyone who claims to love God while hating a fellow believer is lying to themselves. You cannot love the God you have never seen while refusing to love the brother or sister standing right in front of you."
    },
    "21": {
      "L": "And this commandment we have from him: that he who loves God should love his brother also.",
      "M": "And he has given us this command: Anyone who loves God must also love their brother and sister.",
      "T": "The command from God himself settles it: whoever loves God must love their brothers and sisters as well."
    }
  },
  "5": {
    "1": {
      "L": "Everyone who believes that Jesus is the Christ has been born of God, and everyone who loves the one who begat loves the one born of him.",
      "M": "Everyone who believes that Jesus is the Christ is born of God, and everyone who loves the father loves his child as well.",
      "T": "Every person who believes that Jesus is the Messiah has been born of God. And this follows: if you love the Father, you will also love his children."
    },
    "2": {
      "L": "By this we know that we love the children of God, when we love God and keep his commandments.",
      "M": "This is how we know that we love the children of God: by loving God and carrying out his commands.",
      "T": "Here is the proof that we love God's children: we love God himself and we actually keep his commands."
    },
    "3": {
      "L": "For this is the love of God—that we keep his commandments. And his commandments are not burdensome.",
      "M": "In fact, this is love for God: to keep his commands. And his commands are not burdensome.",
      "T": "For what does it actually mean to love God? It means keeping his commands. And those commands are not crushing—they do not weigh us down."
    },
    "4": {
      "L": "For everyone who is born of God overcomes the world; and this is the victory that has overcome the world—our faith.",
      "M": "for everyone born of God overcomes the world. This is the victory that has overcome the world, even our faith.",
      "T": "Because every child of God wins victory over the world. And what is the power that wins this victory? Our faith."
    },
    "5": {
      "L": "Who is the one who overcomes the world except the one who believes that Jesus is the Son of God?",
      "M": "Who is it that overcomes the world? Only the one who believes that Jesus is the Son of God.",
      "T": "And who exactly is this overcomer? Only the person who genuinely believes that Jesus is the Son of God."
    },
    "6": {
      "L": "This is the one who came through water and blood—Jesus Christ; not by water only, but by the water and the blood. And the Spirit is the one who testifies, because the Spirit is the truth.",
      "M": "This is the one who came by water and blood—Jesus Christ. He did not come by water only, but by water and blood. And it is the Spirit who testifies, because the Spirit is the truth.",
      "T": "Jesus Christ—this is the one whose coming was marked by the water of his baptism and the blood of his death. Not water only, but water and blood together. And the Spirit continues to testify about him, because the Spirit is truth itself."
    },
    "7": {
      "L": "For there are three that testify:",
      "M": "For there are three that testify:",
      "T": "There are three witnesses to this:"
    },
    "8": {
      "L": "the Spirit and the water and the blood; and these three agree as one.",
      "M": "the Spirit, the water and the blood; and the three are in agreement.",
      "T": "the Spirit, the water, and the blood—and these three witnesses say the same thing."
    },
    "9": {
      "L": "If we receive the testimony of men, the testimony of God is greater; for this is the testimony of God—that he has testified concerning his Son.",
      "M": "We accept human testimony, but God's testimony is greater because it is the testimony of God, which he has given about his Son.",
      "T": "We routinely accept human testimony in daily life. But God's testimony carries infinitely greater weight—and this is precisely what he has testified: the truth about his Son."
    },
    "10": {
      "L": "The one who believes in the Son of God has the testimony in himself; the one who does not believe God has made him a liar, because he has not believed the testimony that God has testified concerning his Son.",
      "M": "Whoever believes in the Son of God accepts this testimony in themselves. Whoever does not believe God has in effect called God a liar, because they have not believed the testimony God has given about his Son.",
      "T": "The person who trusts in the Son of God carries this testimony within themselves—they have internalized it. But anyone who refuses to believe is effectively calling God a liar, since they are rejecting God's own testimony about his Son."
    },
    "11": {
      "L": "And this is the testimony—that God gave us eternal life, and this life is in his Son.",
      "M": "And this is the testimony: God has given us eternal life, and this life is in his Son.",
      "T": "And here is what God's testimony says: he has given us age-to-come life—resurrection life, genuine and full—and this life exists only in his Son."
    },
    "12": {
      "L": "The one who has the Son has life; the one who does not have the Son of God does not have life.",
      "M": "Whoever has the Son has life; whoever does not have the Son of God does not have life.",
      "T": "Have the Son, and you have life. Reject the Son of God, and life is simply not yours."
    },
    "13": {
      "L": "These things I have written to you who believe in the name of the Son of God, that you may know that you have eternal life.",
      "M": "I write these things to you who believe in the name of the Son of God so that you may know that you have eternal life.",
      "T": "I am writing all of this to you who trust in the name of the Son of God—so that you can know with certainty, not merely hope, that you have this eternal life."
    },
    "14": {
      "L": "And this is the confidence that we have toward him—that if we ask anything according to his will he hears us.",
      "M": "This is the confidence we have in approaching God: that if we ask anything according to his will, he hears us.",
      "T": "And this is what that confidence looks like in practice: whenever we pray for anything that aligns with his will, he hears us—truly, attentively hears us."
    },
    "15": {
      "L": "And if we know that he hears us in whatever we ask, we know that we have the requests that we have asked from him.",
      "M": "And if we know that he hears us—whatever we ask—we know that we have what we asked of him.",
      "T": "If we know he is actually listening to every request we bring, then we can be certain: whatever we have asked for according to his will, it has been granted."
    },
    "16": {
      "L": "If anyone sees his brother sinning a sin not unto death, he shall ask and he will give him life—to those who sin not unto death. There is sin unto death; I do not say that he should ask concerning that.",
      "M": "If you see any brother or sister commit a sin that does not lead to death, you should pray and God will give them life. I refer to those whose sin does not lead to death. There is a sin that leads to death. I am not saying that you should pray about that.",
      "T": "If you see a fellow believer committing a sin that does not lead to death, pray for them—and God will grant life to that person. This applies to sins not leading to death. There is such a thing as a sin that leads to death—for that I am not directing you to pray."
    },
    "17": {
      "L": "All unrighteousness is sin, and there is sin that is not unto death.",
      "M": "All wrongdoing is sin, and there is sin that does not lead to death.",
      "T": "Every act of unrighteousness is sin—that is clear. But not every sin is the kind that leads to death."
    },
    "18": {
      "L": "We know that everyone who is born of God does not sin continually; but the one born of God protects him, and the evil one does not touch him.",
      "M": "We know that anyone born of God does not continue to sin; the One who was born of God keeps them safe, and the evil one cannot harm them.",
      "T": "We know this: every person born of God does not live a life dominated by sin. The Son of God—himself born of God—guards them, and the evil one cannot lay hold of them."
    },
    "19": {
      "L": "We know that we are from God, and the whole world lies in the evil one.",
      "M": "We know that we are children of God, and that the whole world is under the control of the evil one.",
      "T": "We know that we belong to God—and we also know that the whole world system lies under the power of the evil one."
    },
    "20": {
      "L": "And we know that the Son of God has come and has given us understanding so that we may know the true one; and we are in the true one, in his Son Jesus Christ. This one is the true God and eternal life.",
      "M": "We know also that the Son of God has come and has given us understanding, so that we may know him who is true. And we are in him who is true by being in his Son Jesus Christ. He is the true God and eternal life.",
      "T": "And we know that the Son of God has come—he is here—and he has given us the capacity to understand, so that we can know the One who is truly real. We live in the Real One, in his Son Jesus Christ. He—this Jesus Christ—is himself the true God and is eternal life."
    },
    "21": {
      "L": "Little children, guard yourselves from idols.",
      "M": "Dear children, keep yourselves from idols.",
      "T": "My dear children, guard yourselves from every substitute for God."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, '1john')
        merge_tier(existing, JOHN1, tier_key)
        save(tier_dir, '1john', existing)
    print('1 John 4–5 written.')

if __name__ == '__main__':
    main()
