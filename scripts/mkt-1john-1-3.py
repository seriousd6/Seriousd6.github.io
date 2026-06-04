"""
MKT 1 John chapters 1–3 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-1john-1-3.py

Translation decisions:
- G3056 (λόγος): "Word" (capitalized) in 1:1 where it refers to the pre-existent Christ,
  echoing John's Prologue (ἀπ᾽ ἀρχῆς = "from the beginning" evokes John 1:1). Lowercase
  "word" elsewhere when referring to God's message or commandment.
- G166 (αἰώνιος): "eternal" in L/M throughout. In T at 2:25 expanded to "the life of the
  age to come" to surface the qualitative sense (not merely unending duration).
- G4151 (πνεῦμα): "Spirit" (capitalized) in 3:24 — the Spirit God has given to believers.
  No ambiguity here between Spirit/spirit/wind.
- G26 (ἀγάπη): "love" consistently in L/M. T surfaces the willed, covenant character where
  contextually warranted (3:16: "This is where we learn what love truly is").
- G1343 (δικαιοσύνη): "righteousness" in L/M. T uses "lives righteously" / "right living"
  where it reads more naturally (3:7, 3:10).
- G1342 (δίκαιος): "righteous" in L/M/T (2:1, 2:29, 3:7).
- G3875 (παράκλητος): "Advocate" in 2:1 — Jesus as defense attorney before the Father.
  Distinct from "Helper" used for the Spirit in John 14–16.
- G2434 (ἱλασμός): "propitiation" in L; "atoning sacrifice" in M; "the sacrifice that turns
  away God's wrath" in T at 2:2.
- G3306 (μένω): "abides" in L; "remains/lives in" in M; rendered contextually in T
  ("stays in union with," "take root," "dwells"). Key term throughout 1 John.
- G5040 (τεκνίον) / G3813 (παιδίον): Both "little children" in L; "dear children" in M/T.
- Aspect: Greek perfects throughout ch.1 (ἑωράκαμεν, ἀκηκόαμεν) rendered as past acts with
  present ongoing claim — "we have seen/heard" as eyewitness testimony carried forward.
- Tense shift 2:13/2:14: John shifts from γράφω (present "I write") in v.13 to ἔγραψα
  (aorist "I wrote/have written") in v.14 — likely epistolary aorist; rendered naturally.
- 2:20 textual note: "καὶ οἴδατε πάντες" (you all know) preferred over TR "πάντα"
  (you know all things); "you all know the truth" in M follows this reading.
- No Comma Johanneum (1 Jn 5:7 interpolation) in this range (chs 1–3).
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
  "1": {
    "1": {
      "L": "That which was from the beginning, which we have heard, which we have seen with our eyes, which we beheld and our hands handled, concerning the Word of life—",
      "M": "What was from the beginning—what we have heard, what we have seen with our own eyes, what we looked at and our hands touched—this we proclaim concerning the Word of life.",
      "T": "We are writing about something that has existed from the very beginning—something we have heard with our own ears, seen with our own eyes, gazed upon and touched with our own hands. This is our announcement: the Word who is life itself."
    },
    "2": {
      "L": "(and the life was manifested, and we have seen it and bear witness and declare to you the eternal life, which was with the Father and was manifested to us)—",
      "M": "The life appeared; we have seen it and testify to it, and we proclaim to you the eternal life, which was with the Father and has appeared to us.",
      "T": "This life actually broke into our world—we saw it with our own eyes and we bear witness to it. We now announce to you the eternal life that was with the Father from the beginning and was revealed to us in person."
    },
    "3": {
      "L": "what we have seen and heard we declare to you also, that you also may have fellowship with us; and indeed our fellowship is with the Father and with his Son Jesus Christ.",
      "M": "We proclaim to you what we have seen and heard, so that you also may have fellowship with us. And our fellowship is with the Father and with his Son, Jesus Christ.",
      "T": "We announce to you what we have seen and heard, so that you can share in the same life we share—a life of deep communion with the Father and with his Son Jesus Christ."
    },
    "4": {
      "L": "And these things we write, so that our joy may be made complete.",
      "M": "We write this to make our joy complete.",
      "T": "We are writing this so that our joy may be full to overflowing."
    },
    "5": {
      "L": "And this is the message which we have heard from him and announce to you: that God is light, and darkness is not in him at all.",
      "M": "This is the message we have heard from him and declare to you: God is light; in him there is no darkness at all.",
      "T": "Here is the message we received from him and now pass on to you: God is light—pure, undimmed light—and in him there is no darkness whatsoever."
    },
    "6": {
      "L": "If we say that we have fellowship with him and yet walk in the darkness, we lie and do not practice the truth.",
      "M": "If we claim to have fellowship with him and yet walk in the darkness, we lie and do not live out the truth.",
      "T": "If we claim to be in fellowship with God but keep living in darkness, we are lying—we are not living according to the truth."
    },
    "7": {
      "L": "But if we walk in the light, as he is in the light, we have fellowship with one another, and the blood of Jesus his Son cleanses us from all sin.",
      "M": "But if we walk in the light, as he is in the light, we have fellowship with one another, and the blood of Jesus his Son cleanses us from all sin.",
      "T": "But if we are walking in the light—as God himself is in the light—then we have genuine fellowship with one another, and the blood of Jesus his Son keeps purifying us from every sin."
    },
    "8": {
      "L": "If we say that we have no sin, we are deceiving ourselves, and the truth is not in us.",
      "M": "If we claim to be without sin, we deceive ourselves and the truth is not in us.",
      "T": "If we tell ourselves we have no sin, we are only deceiving ourselves—the truth has no place in us."
    },
    "9": {
      "L": "If we confess our sins, he is faithful and just to forgive us our sins and to cleanse us from all unrighteousness.",
      "M": "If we confess our sins, he is faithful and just and will forgive us our sins and purify us from all unrighteousness.",
      "T": "But if we confess our sins, he is faithful and righteous—he will forgive us our sins and cleanse us from every form of wrongdoing."
    },
    "10": {
      "L": "If we say that we have not sinned, we make him a liar, and his word is not in us.",
      "M": "If we claim we have not sinned, we make him out to be a liar and his word is not in us.",
      "T": "If we claim we have never sinned, we are calling God a liar, and his word has no home in our lives."
    }
  },
  "2": {
    "1": {
      "L": "My little children, I am writing these things to you so that you may not sin. And if anyone sins, we have an Advocate with the Father, Jesus Christ the righteous.",
      "M": "My dear children, I write this to you so that you will not sin. But if anybody does sin, we have an advocate with the Father—Jesus Christ, the Righteous One.",
      "T": "My dear children, I am writing this so that you will not sin. But when someone does sin, we have a defender who stands before the Father on our behalf—Jesus Christ, the Righteous One."
    },
    "2": {
      "L": "and he himself is the propitiation for our sins; and not for ours only but also for the sins of the whole world.",
      "M": "He is the atoning sacrifice for our sins, and not only for ours but also for the sins of the whole world.",
      "T": "He is the sacrifice that turns away God's wrath—not only for our sins but for the sins of the entire world."
    },
    "3": {
      "L": "And by this we know that we have come to know him, if we keep his commandments.",
      "M": "We know that we have come to know him if we keep his commands.",
      "T": "Here is how we know we truly know him: we keep his commands."
    },
    "4": {
      "L": "The one who says, 'I have come to know him,' and does not keep his commandments, is a liar, and the truth is not in that person.",
      "M": "Whoever says, 'I know him,' but does not do what he commands is a liar, and the truth is not in that person.",
      "T": "Anyone who claims to know God but ignores his commands is a liar—the truth has no home in them."
    },
    "5": {
      "L": "But whoever keeps his word, in him the love of God is truly perfected. By this we know that we are in him:",
      "M": "But if anyone obeys his word, love for God is truly made complete in them. This is how we know we are in him:",
      "T": "But when someone keeps his word, God's love reaches its full expression in their life. This is how we know we are truly united with him:"
    },
    "6": {
      "L": "the one who says he abides in him ought himself to walk in the same manner as he walked.",
      "M": "Whoever claims to live in him must live as Jesus did.",
      "T": "Anyone who claims to live in union with God must walk the same path Jesus walked."
    },
    "7": {
      "L": "Beloved, I am not writing a new commandment to you, but an old commandment which you have had from the beginning; the old commandment is the word which you have heard.",
      "M": "Dear friends, I am not writing you a new command but an old one, which you have had since the beginning. This old command is the message you have heard.",
      "T": "Dear friends, what I am writing is not a new command—it is the ancient one you have known from the start. This old command is simply the message you heard from the beginning."
    },
    "8": {
      "L": "On the other hand, I am writing a new commandment to you, which is true in him and in you, because the darkness is passing away and the true light is already shining.",
      "M": "Yet I am writing you a new command; its truth is seen in him and in you, because the darkness is passing and the true light is already shining.",
      "T": "And yet in another sense it is a new command—one already proving itself true in Christ and in you, because the old darkness is fading and the true light is already breaking through."
    },
    "9": {
      "L": "The one who says he is in the light and hates his brother is in the darkness until now.",
      "M": "Anyone who claims to be in the light but hates a brother or sister is still in the darkness.",
      "T": "Whoever says they are in the light while hating a fellow believer is still in the dark—nothing has changed for them."
    },
    "10": {
      "L": "The one who loves his brother abides in the light, and there is no cause for stumbling in him.",
      "M": "Anyone who loves their brother and sister lives in the light, and there is nothing in them to make them stumble.",
      "T": "But whoever loves their fellow believer is living in the light, and there is nothing in them to cause another to fall."
    },
    "11": {
      "L": "But the one who hates his brother is in the darkness and walks in the darkness, and does not know where he is going, because the darkness has blinded his eyes.",
      "M": "But anyone who hates a brother or sister is in the darkness and walks around in the darkness. They do not know where they are going, because the darkness has blinded them.",
      "T": "Anyone who hates a fellow believer is in the dark and walks in the dark—they don't even know where they are going, because the darkness has robbed them of their sight."
    },
    "12": {
      "L": "I am writing to you, little children, because your sins have been forgiven you for his name's sake.",
      "M": "I am writing to you, dear children, because your sins have been forgiven on account of his name.",
      "T": "I write to you, dear children, because your sins have already been forgiven—for the sake of his name."
    },
    "13": {
      "L": "I am writing to you, fathers, because you know him who has been from the beginning. I am writing to you, young men, because you have overcome the evil one. I am writing to you, children, because you know the Father.",
      "M": "I am writing to you, fathers, because you know him who is from the beginning. I am writing to you, young men, because you have overcome the evil one. I write to you, dear children, because you know the Father.",
      "T": "I write to you, fathers, because you have come to know the One who has been from the beginning. I write to you, young men, because you have conquered the evil one. I write to you, children, because you know the Father."
    },
    "14": {
      "L": "I have written to you, fathers, because you know him who has been from the beginning. I have written to you, young men, because you are strong, and the word of God abides in you, and you have overcome the evil one.",
      "M": "I write to you, fathers, because you know him who is from the beginning. I write to you, young men, because you are strong, and the word of God lives in you, and you have overcome the evil one.",
      "T": "I have written to you, fathers, because you have known the One who is from the beginning. I have written to you, young men, because you are strong—God's word has taken deep root in you, and you have overcome the evil one."
    },
    "15": {
      "L": "Do not love the world or the things in the world. If anyone loves the world, the love of the Father is not in him.",
      "M": "Do not love the world or anything in the world. If anyone loves the world, love for the Father is not in them.",
      "T": "Do not set your affections on the world or on what the world offers. If anyone is in love with the world, love for the Father has no place in them."
    },
    "16": {
      "L": "For everything in the world—the lust of the flesh and the lust of the eyes and the boastful pride of life—is not from the Father but is from the world.",
      "M": "For everything in the world—the lust of the flesh, the lust of the eyes, and the pride of life—comes not from the Father but from the world.",
      "T": "Everything the world offers—the craving of the body, the craving of the eyes, the arrogant display of wealth and status—none of it comes from the Father. It all belongs to the world."
    },
    "17": {
      "L": "And the world is passing away, and also its lusts; but the one who does the will of God abides forever.",
      "M": "The world and its desires pass away, but whoever does the will of God lives forever.",
      "T": "The world and all its cravings are fading away—but whoever does God's will stands firm forever."
    },
    "18": {
      "L": "Children, it is the last hour; and just as you heard that antichrist is coming, even now many antichrists have appeared; from this we know that it is the last hour.",
      "M": "Dear children, this is the last hour; and as you have heard that the antichrist is coming, even now many antichrists have come. This is how we know it is the last hour.",
      "T": "Dear children, we are in the final hour. You heard that the antichrist was coming—and sure enough, many antichrists have already arrived. This is how we know we are living in the end times."
    },
    "19": {
      "L": "They went out from us, but they were not of us; for if they had been of us, they would have remained with us. But they went out so that it would be shown that they all are not of us.",
      "M": "They went out from us, but they did not really belong to us. For if they had belonged to us, they would have remained with us; but their going showed that none of them belonged to us.",
      "T": "These people came from our community, but they never truly belonged to it. If they had really been part of us, they would have stayed. Their departure makes plain that none of them were genuinely ours."
    },
    "20": {
      "L": "But you have an anointing from the Holy One, and you all know.",
      "M": "But you have an anointing from the Holy One, and all of you know the truth.",
      "T": "But you have received an anointing from the Holy One—and all of you have knowledge of the truth."
    },
    "21": {
      "L": "I have not written to you because you do not know the truth, but because you do know it, and because no lie is of the truth.",
      "M": "I do not write to you because you do not know the truth, but because you do know it and because no lie comes from the truth.",
      "T": "I am not writing because you are ignorant of the truth—you know it well. I write because no lie can ever spring from the truth."
    },
    "22": {
      "L": "Who is the liar but the one who denies that Jesus is the Christ? This is the antichrist, the one who denies the Father and the Son.",
      "M": "Who is the liar? It is whoever denies that Jesus is the Christ. Such a person is the antichrist—denying the Father and the Son.",
      "T": "Who is the supreme liar? The one who denies that Jesus is the Christ. That is the antichrist—the one who refuses to acknowledge the Father and the Son."
    },
    "23": {
      "L": "No one who denies the Son has the Father; the one who confesses the Son has the Father also.",
      "M": "No one who denies the Son has the Father; whoever acknowledges the Son has the Father also.",
      "T": "Deny the Son and you forfeit the Father. Confess the Son and you have the Father as well."
    },
    "24": {
      "L": "As for you, let that abide in you which you heard from the beginning. If what you heard from the beginning abides in you, you also will abide in the Son and in the Father.",
      "M": "As for you, see that what you have heard from the beginning remains in you. If it does, you also will remain in the Son and in the Father.",
      "T": "Hold firmly to what you heard from the beginning—let it take deep root in you. If the original message stays in you, you will remain in union with the Son and with the Father."
    },
    "25": {
      "L": "And this is the promise which he himself promised to us: eternal life.",
      "M": "And this is what he promised us—eternal life.",
      "T": "And here is the promise he himself made to us: life that is eternal—the life of the age to come."
    },
    "26": {
      "L": "These things I have written to you concerning those who are deceiving you.",
      "M": "I am writing these things to you about those who are trying to lead you astray.",
      "T": "I write all this to warn you about those who are trying to lead you away from the truth."
    },
    "27": {
      "L": "As for you, the anointing which you received from him abides in you, and you have no need for anyone to teach you; but as his anointing teaches you about all things, and is true and is not a lie, and just as it has taught you, abide in him.",
      "M": "As for you, the anointing you received from him remains in you, and you do not need anyone to teach you. But as his anointing teaches you about all things and as that anointing is real, not counterfeit—just as it has taught you, remain in him.",
      "T": "But the anointing you received from him lives in you, and you don't need anyone else to teach you. His anointing teaches you about everything—it is genuine, not a counterfeit—so as it has taught you, stay in union with him."
    },
    "28": {
      "L": "And now, little children, abide in him, so that when he appears we may have confidence and not shrink away from him in shame at his coming.",
      "M": "And now, dear children, continue in him, so that when he appears we may be confident and unashamed before him at his coming.",
      "T": "And so, dear children, stay in union with him—so that when he appears, we will stand before him with confidence and will not cringe in shame at his arrival."
    },
    "29": {
      "L": "If you know that he is righteous, you know that everyone who practices righteousness also is born of him.",
      "M": "If you know that he is righteous, you know that everyone who does what is right has been born of him.",
      "T": "You know that he is righteous—so know this too: everyone who lives righteously has been born of him."
    }
  },
  "3": {
    "1": {
      "L": "See what kind of love the Father has given to us, that we should be called children of God; and so we are. For this reason the world does not know us, because it did not know him.",
      "M": "See what great love the Father has lavished on us, that we should be called children of God! And that is what we are! The reason the world does not know us is that it did not know him.",
      "T": "Look at the lavish love the Father has poured out on us—that we should actually be called God's children. And that is exactly what we are! The world does not recognize us, because it never recognized him."
    },
    "2": {
      "L": "Beloved, now we are children of God, and what we will be has not yet been manifested. We know that when he appears, we will be like him, because we will see him as he is.",
      "M": "Dear friends, now we are children of God, and what we will be has not yet been made known. But we know that when he appears, we shall be like him, for we shall see him as he is.",
      "T": "Dear friends, we are already God's children—though what we will become has not yet been fully revealed. But we know this: when he appears, we will be like him, because we will see him as he truly is."
    },
    "3": {
      "L": "And everyone who has this hope in him purifies himself, just as he is pure.",
      "M": "All who have this hope in him purify themselves, just as he is pure.",
      "T": "Anyone who holds this hope fixed on him will keep purifying themselves—because he himself is pure."
    },
    "4": {
      "L": "Everyone who practices sin also practices lawlessness; and sin is lawlessness.",
      "M": "Everyone who sins breaks the law; in fact, sin is lawlessness.",
      "T": "Whoever keeps on sinning is in open rebellion against God's law—that is what sin is: defiance of God's order."
    },
    "5": {
      "L": "And you know that he appeared to take away sins, and in him there is no sin.",
      "M": "But you know that he appeared so that he might take away our sins. And in him is no sin.",
      "T": "You know why he appeared: to take sins away. And in him there is absolutely no sin."
    },
    "6": {
      "L": "No one who abides in him keeps on sinning; no one who keeps on sinning has seen him or knows him.",
      "M": "No one who lives in him keeps on sinning. No one who continues to sin has either seen him or known him.",
      "T": "Whoever stays in union with him does not keep on sinning. Anyone who keeps on sinning has never truly seen him or known him."
    },
    "7": {
      "L": "Little children, let no one deceive you; the one who practices righteousness is righteous, just as he is righteous.",
      "M": "Dear children, do not let anyone lead you astray. The one who does what is right is righteous, just as he is righteous.",
      "T": "Dear children, don't let anyone mislead you: the person who actually lives righteously is righteous—just as he is righteous."
    },
    "8": {
      "L": "The one who practices sin is of the devil, for the devil has sinned from the beginning. For this purpose the Son of God appeared: to destroy the works of the devil.",
      "M": "The one who does what is sinful is of the devil, because the devil has been sinning from the beginning. The reason the Son of God appeared was to destroy the devil's work.",
      "T": "Whoever keeps sinning belongs to the devil—the devil has been sinning since the beginning. But the Son of God appeared for this very purpose: to dismantle everything the devil has built."
    },
    "9": {
      "L": "No one who is born of God practices sin, because his seed abides in him; and he cannot sin, because he is born of God.",
      "M": "No one who is born of God will continue to sin, because God's seed remains in them; they cannot go on sinning, because they have been born of God.",
      "T": "Those who have been born of God do not persist in sinning—because God's own life-seed lives in them. They cannot keep on sinning, because they have been born of God."
    },
    "10": {
      "L": "By this the children of God and the children of the devil are evident: everyone who does not practice righteousness is not of God, nor is the one who does not love his brother.",
      "M": "This is how we know who the children of God are and who the children of the devil are: Anyone who does not do what is right is not God's child, nor is anyone who does not love their brother and sister.",
      "T": "This is the clear dividing line between God's children and the devil's children: anyone who does not live righteously does not belong to God—and neither does anyone who does not love their fellow believers."
    },
    "11": {
      "L": "For this is the message which you heard from the beginning: that we should love one another.",
      "M": "For this is the message you heard from the beginning: We should love one another.",
      "T": "The message has been the same from the very start: we are to love one another."
    },
    "12": {
      "L": "not as Cain, who was of the evil one and slew his brother. And for what reason did he slay him? Because his deeds were evil, and his brother's were righteous.",
      "M": "Do not be like Cain, who belonged to the evil one and murdered his brother. And why did he murder him? Because his own actions were evil and his brother's were righteous.",
      "T": "Unlike Cain, who belonged to the evil one and killed his brother—why did he kill him? Because Cain's actions were evil and his brother's were righteous. Righteousness provokes hatred in those who have none."
    },
    "13": {
      "L": "Do not be surprised, brothers, if the world hates you.",
      "M": "Do not be surprised, my brothers and sisters, if the world hates you.",
      "T": "So do not be shocked, dear brothers and sisters, when the world hates you."
    },
    "14": {
      "L": "We know that we have passed from death into life, because we love the brethren. He who does not love abides in death.",
      "M": "We know that we have passed from death to life, because we love each other. Anyone who does not love remains in death.",
      "T": "We know that we have crossed over from death into life—because we love our fellow believers. Anyone who does not love is still living in death."
    },
    "15": {
      "L": "Everyone who hates his brother is a murderer; and you know that no murderer has eternal life abiding in him.",
      "M": "Anyone who hates a brother or sister is a murderer, and you know that no murderer has eternal life residing in them.",
      "T": "Whoever hates a fellow believer is, in God's sight, a murderer—and you know that no murderer has the life of the age to come living in them."
    },
    "16": {
      "L": "By this we know love, that he laid down his life for us; and we ought to lay down our lives for the brethren.",
      "M": "This is how we know what love is: Jesus Christ laid down his life for us. And we ought to lay down our lives for our brothers and sisters.",
      "T": "This is where we learn what love truly is: he laid down his life for us. That means we, too, ought to lay down our lives for one another."
    },
    "17": {
      "L": "But whoever has the world's goods and sees his brother in need and closes his heart against him, how does the love of God abide in him?",
      "M": "If anyone has material possessions and sees a brother or sister in need but has no pity on them, how can the love of God be in that person?",
      "T": "But if someone has what the world calls abundance, and sees a fellow believer going without, and shuts their heart—how can God's love possibly live in them?"
    },
    "18": {
      "L": "Little children, let us not love in word or in tongue, but in deed and in truth.",
      "M": "Dear children, let us not love with words or speech but with actions and in truth.",
      "T": "Dear children, let us not love merely with words or fine-sounding speeches—let us love through what we do and in truth."
    },
    "19": {
      "L": "By this we shall know that we are of the truth, and we shall assure our hearts before him",
      "M": "This is how we know that we belong to the truth and how we set our hearts at rest in his presence:",
      "T": "This is how we will know we belong to the truth, and how we will put our hearts at peace before him—"
    },
    "20": {
      "L": "in whatever our heart condemns us; for God is greater than our heart, and knows all things.",
      "M": "If our hearts condemn us, we know that God is greater than our hearts, and he knows everything.",
      "T": "even when our own hearts condemn us. For God is greater than our hearts, and he knows all things."
    },
    "21": {
      "L": "Beloved, if our heart does not condemn us, we have confidence before God;",
      "M": "Dear friends, if our hearts do not condemn us, we have confidence before God",
      "T": "Dear friends, if our hearts do not condemn us, we approach God with complete confidence—"
    },
    "22": {
      "L": "and whatever we ask we receive from him, because we keep his commandments and do the things that are pleasing in his sight.",
      "M": "and receive from him anything we ask, because we keep his commands and do what pleases him.",
      "T": "and receive from him whatever we ask, because we keep his commands and do what is pleasing in his sight."
    },
    "23": {
      "L": "And this is his commandment, that we believe in the name of his Son Jesus Christ, and love one another, just as he commanded us.",
      "M": "And this is his command: to believe in the name of his Son, Jesus Christ, and to love one another as he commanded us.",
      "T": "And his command comes down to this: believe in the name of his Son Jesus Christ, and love one another—just as he himself commanded."
    },
    "24": {
      "L": "And the one who keeps his commandments abides in him, and he in him. And by this we know that he abides in us, by the Spirit whom he has given to us.",
      "M": "The one who keeps God's commands lives in him, and he in them. And this is how we know that he lives in us: We know it by the Spirit he gave us.",
      "T": "Whoever keeps his commands stays in union with God, and God remains in them. And here is how we know that he dwells in us: by the Spirit he has given us."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, '1john')
        merge_tier(existing, JOHN1, tier_key)
        save(tier_dir, '1john', existing)
    print('1 John 1–3 written.')

if __name__ == '__main__':
    main()
