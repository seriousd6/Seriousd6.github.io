"""
MKT 2 Corinthians chapters 7–9 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-2corinthians-7-9.py

Context: This is the first completed script for 2 Corinthians. Chapters 1–6 are in-progress
(2CO-1a, 2CO-1b). This script establishes several term conventions that should be carried
forward into those and subsequent 2 Corinthians scripts.

Chapters 7–9 cover three related movements: (7) Paul's joy at the Corinthians' repentance
through Titus's visit; (8) the theology and appeal for the Jerusalem collection; (9) the
theology of generous giving, ending with the "inexpressible gift" doxology.

Translation decisions:
- G3077 (λύπη): "grief" — the key distinction in 7:9–11 is between κατὰ θεόν λύπη
  (godly grief / grief according to God) and κόσμου λύπη (worldly grief). L: "grief"
  throughout; M: "godly grief" / "worldly grief"; T: makes the distinction interpretive.
- G3341 (μετάνοια): "repentance" — maintained as "repentance" in L/M; T: "genuine change"
  or "turning around" where the nuance of direction is key. Not mere remorse but reorientation.
- G5485 (χάρις): "grace" — this word saturates chapters 8–9. In cultic/gift-exchange contexts
  (8:1, 8:4, 8:6, 8:7, 8:19; 9:8, 9:14) it means both "gift/gracious act" and "divine grace."
  L: "grace" throughout; M: "grace" or "generous act" per context; T: makes the theological
  double sense explicit where Paul is playing on it (esp. 8:9).
- G26 (ἀγάπη): "love" — 8:8, 8:24; covenantal, self-giving sense; T surface this.
- G4561 (σάρξ): 7:1 — physical body in parallel with "spirit"; L: "flesh"; M/T: "body."
  No sinful-nature sense in these chapters.
- G4151 (πνεῦμα): 7:1 — human spirit (contrasted with body); 7:13 — Titus's spirit refreshed.
  Lowercase "spirit" throughout; not the Holy Spirit in these contexts.
- G1343 (δικαιοσύνη): 9:9–10 — OT citation (Ps 112:9); "righteousness" in all tiers.
  The righteousness here is the fruit of generosity that endures; T surfaces the OT echo.
- G2962 (κύριος): "Lord" throughout; 8:9 κύριος = Lord Jesus Christ.
- G2842 (κοινωνία): 8:4 — "fellowship/sharing/participation" — L: "fellowship"; M: "sharing";
  T: "to have a part in."
- G2745/G2744 (καύχημα/καυχάομαι): "boasting" — Paul's measured use of boasting language;
  not sinful pride but legitimate confidence in what God has done. Maintained from 1 Cor scripts.
- G4053 (περισσεύω): "abound/overflow" — 8:7, 9:8, 9:11; L: "abound"; M: "overflow/excel";
  T: conveys the excess that flows into generosity.
- G2470 (ἰσότης): 8:13–14 — "equality/fairness"; the principle of mutual provision.
  L: "equality"; M/T: "fairness" or "balance."
- 8:15: explicit OT quotation of Exodus 16:18 (manna narrative). T identifies the source.
- 9:9: explicit OT quotation of Psalm 112:9. T identifies the source.
- Aspect notes: present imperatives in ch. 8 (8:7 ἵνα καὶ ἐν ταύτῃ τῇ χάριτι περισσεύητε)
  = ongoing command to excel/abound; aorist in 8:1 (ἐδόθη) = completed bestowing of grace.
- Paul's "boasting" register (7:4, 7:14, 8:24, 9:2–4): honor-shame culture is pervasive;
  "boasting" is social-credit speech about a patron-client relationship, not vanity.
- 8:9 is the theological center of the collection appeal: Christ's voluntary kenosis as the
  model and motivation for generous giving. All three tiers render this as the hinge verse.
- 9:6 (sow/reap) and 9:7 (God loves a cheerful giver) are well-known; T avoids cliché
  while preserving the agricultural and covenantal resonances.
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

CORINTHIANS2 = {
  "7": {
    "1": {
      "L": "Having therefore these promises, beloved, let us cleanse ourselves from all defilement of flesh and spirit, completing holiness in the fear of God.",
      "M": "Since we have these promises, dear friends, let us cleanse ourselves from every defilement of body and spirit, bringing holiness to completion in the fear of God.",
      "T": "With promises like these before us, let us make a clean break from every impurity—of body and spirit alike—pressing on to complete the holiness that flows from reverence toward God."
    },
    "2": {
      "L": "Receive us; we wronged no one, we corrupted no one, we defrauded no one.",
      "M": "Make room for us in your hearts. We wronged no one, corrupted no one, defrauded no one.",
      "T": "Open your hearts to us. We wronged no one among you, exploited no one, cheated no one. We have nothing to hide."
    },
    "3": {
      "L": "I do not say this to condemn you; for I have said before that you are in our hearts, to die together and to live together.",
      "M": "I do not say this to condemn you, for I have already said that you are in our hearts, to die together and to live together.",
      "T": "I am not putting you on trial. You already know that you hold a place in our hearts so fixed that neither death nor life could dislodge you."
    },
    "4": {
      "L": "Great is my openness toward you, great is my boasting on your behalf; I am filled with comfort, I overflow with joy in all our tribulation.",
      "M": "I have great confidence in speaking to you; I take great pride in you. I am filled with comfort; I overflow with joy in all our affliction.",
      "T": "I hold nothing back with you—my confidence is unbounded, my pride in you immense. Even in the thick of all our sufferings I am overwhelmed with encouragement and brimming over with joy."
    },
    "5": {
      "L": "For when we came into Macedonia our flesh had no rest, but we were afflicted in every way—without were conflicts, within were fears.",
      "M": "When we arrived in Macedonia we had no rest in body; we were afflicted on every side—conflict on the outside, fear on the inside.",
      "T": "When we reached Macedonia there was no rest for us anywhere. Troubles pressed in from every direction—open conflicts in the world around us, inward anxieties within our own hearts."
    },
    "6": {
      "L": "But God, who comforts the downcast, comforted us by the arrival of Titus;",
      "M": "But God, who comforts those who are downcast, comforted us by the arrival of Titus;",
      "T": "But God, who never abandons the downhearted, came through for us—he sent Titus, and in Titus's arrival came the comfort we had been needing."
    },
    "7": {
      "L": "and not only by his arrival, but also by the comfort with which he was comforted in you—as he reported to us your longing, your mourning, your zeal for me—so that I rejoiced all the more.",
      "M": "and not only by his coming, but also by the comfort he had received from you, as he told us of your longing, your mourning, your passionate concern for me—so that I rejoiced even more.",
      "T": "Not just his coming, but the news he brought: how you longed to see me, how you grieved over what had happened, how fiercely loyal to me you were. When I heard all that, my joy doubled."
    },
    "8": {
      "L": "For though I grieved you with my letter, I do not regret it—though I did regret it—for I see that that letter grieved you, even if only for a time.",
      "M": "For even if I caused you grief with my letter, I do not regret it—though I did regret it, for I see that the letter grieved you, even if only for a while.",
      "T": "That letter of mine caused you pain—I know that—and for a moment I did regret sending it. But I no longer regret it, because I can see that the grief it produced served its purpose, even if only briefly."
    },
    "9": {
      "L": "Now I rejoice, not that you were grieved, but that you were grieved into repentance; for you were grieved in a godly way, so that you suffered no loss from us in anything.",
      "M": "Now I rejoice—not because you were caused grief, but because your grief led to repentance. For you were grieved in a godly way, so that you suffered no loss from us.",
      "T": "What gives me joy is not the pain itself but what the pain produced: it turned you around. And the grief that turned you was the right kind—grief that comes from God—so in the end you suffered no harm from it at all."
    },
    "10": {
      "L": "For godly grief produces repentance leading to salvation, leaving no regret; but worldly grief produces death.",
      "M": "For grief in accordance with God produces a repentance that leads to salvation and is not to be regretted, but worldly grief produces death.",
      "T": "There are two kinds of grief. One is God-shaped: it moves you to genuine change and ends in life, leaving nothing to regret. The other is merely human: it cycles back on itself and leads to death."
    },
    "11": {
      "L": "For behold, this very thing—that you sorrowed in a godly way—what earnestness it produced in you, what defense, what indignation, what fear, what longing, what zeal, what vindication! At every point you have proved yourselves to be innocent in this matter.",
      "M": "Just see what this godly grief produced in you: what eagerness, what clearing of yourselves, what indignation, what fear, what longing, what zeal, what justice! In every way you have proved yourselves blameless in this matter.",
      "T": "Look at the evidence: once God-shaped grief got hold of you, the results were remarkable—urgency to set things right, a vigorous defense of your own conduct, anger at the wrong that was done, holy reverence, longing for reconciliation, passionate loyalty, a demand for accountability. You have shown yourselves, at every point, completely in the clear."
    },
    "12": {
      "L": "So though I wrote to you, it was not for the sake of the one who wronged, nor for the sake of the one who was wronged, but that your earnestness toward us might be revealed to you in the sight of God.",
      "M": "So, even though I wrote to you, it was not for the sake of the one who did the wrong, or for the sake of the one who was wronged, but in order that your earnest care for us might be made known to you before God.",
      "T": "So my letter was not really about the offender or the offended. It was about you—so that you could see, standing before God, how deeply you care for us."
    },
    "13": {
      "L": "Therefore we have been comforted. And in addition to our comfort, we rejoiced even more exceedingly at the joy of Titus, because his spirit has been refreshed by all of you.",
      "M": "In all this we have been comforted. And besides our own comfort, we rejoiced even more at the joy of Titus, because his spirit had been refreshed by all of you.",
      "T": "All of this has been a source of deep comfort to us. And above and beyond that comfort came something more: Titus's own joy—because you had revived his spirit, and his joy became ours."
    },
    "14": {
      "L": "For whatever I boasted to him about you, I was not put to shame; but as we spoke everything to you in truth, so also our boasting before Titus has proved to be true.",
      "M": "For whatever I boasted to him about you, I have not been put to shame. Just as everything we said to you was true, so our boasting to Titus has proved equally true.",
      "T": "Everything I told Titus about you turned out to be accurate—I was not embarrassed. Just as we have always been straight with you, so what we said to Titus has been vindicated by your conduct."
    },
    "15": {
      "L": "And his heart goes out all the more to you as he recalls the obedience of all of you, how with fear and trembling you received him.",
      "M": "And his affection for you is all the more abundant as he remembers the obedience of all of you, and how you received him with fear and trembling.",
      "T": "His feelings for you have grown even warmer as he recalls how fully you complied, and with what reverent, trembling care you welcomed him."
    },
    "16": {
      "L": "I rejoice, therefore, that I am fully confident in you in all things.",
      "M": "I rejoice that I can be confident in you in every way.",
      "T": "I end with joy: in every matter that counts, I am fully confident in you."
    }
  },
  "8": {
    "1": {
      "L": "Now we make known to you, brothers, the grace of God given to the churches of Macedonia:",
      "M": "We want you to know, brothers and sisters, about the grace of God that has been given to the churches of Macedonia:",
      "T": "Here is something remarkable we want you to know: in the churches of Macedonia, God's grace showed up in an unexpected form."
    },
    "2": {
      "L": "how that in a great trial of affliction, the abundance of their joy and their deep poverty overflowed into the riches of their generosity.",
      "M": "In a severe test of affliction, their overflowing joy and their extreme poverty have overflowed into a wealth of generosity.",
      "T": "Tested by severe hardship, pressed down by grinding poverty, they gave with an exuberant joy that produced a stunning outpouring of generosity."
    },
    "3": {
      "L": "For according to their ability—I testify—and beyond their ability, of their own accord,",
      "M": "For according to their means—I can testify—and even beyond their means, of their own free will,",
      "T": "No one asked them to do it. They gave to the limit of what they had, and then beyond it—I saw this myself."
    },
    "4": {
      "L": "begging us with much urging for the favor of participation in the ministry to the saints—",
      "M": "begging us earnestly for the favor of sharing in the ministry to the saints—",
      "T": "in fact they came to us and pleaded—pleaded—to be allowed to have a part in the service for the saints in Jerusalem."
    },
    "5": {
      "L": "and this not as we had hoped, but first they gave themselves to the Lord and to us by the will of God.",
      "M": "And they did this not as we had expected, but first they gave themselves to the Lord and to us, in accordance with God's will.",
      "T": "What they gave exceeded anything we had expected, because the first thing they gave was themselves—to the Lord, and then to us as his instruments—and that settled everything."
    },
    "6": {
      "L": "So we urged Titus that, as he had begun, so he should also complete in you this grace as well.",
      "M": "So we urged Titus that, just as he had begun, he should also bring this act of grace to completion among you.",
      "T": "This is what prompted us to urge Titus to come back to you and bring to completion what he had already started—this gift, which is itself a work of grace."
    },
    "7": {
      "L": "But just as you abound in everything—in faith, speech, knowledge, all earnestness, and in the love from us that is in you—see that you abound in this grace also.",
      "M": "Since you excel in everything—in faith, speech, knowledge, all earnestness, and in the love that we have kindled among you—see that you excel in this act of grace as well.",
      "T": "You already overflow in so many ways—faith, eloquence, insight, energy, and the love we have seen growing among you. Let this act of generous giving overflow from you in the same way."
    },
    "8": {
      "L": "I am not saying this as a command, but through the eagerness of others I am testing the genuineness of your love.",
      "M": "I say this not as a command, but by using the eagerness of others as a test of the genuineness of your love.",
      "T": "I am not issuing orders here. But by holding up the example of others, I am giving your love the chance to prove itself genuine."
    },
    "9": {
      "L": "For you know the grace of our Lord Jesus Christ, that though he was rich, yet for your sakes he became poor, so that by his poverty you might become rich.",
      "M": "For you know the grace of our Lord Jesus Christ—that though he was rich, for your sake he became poor, so that through his poverty you might become rich.",
      "T": "The ultimate model for what I am asking you to do is this: the Lord Jesus Christ was immeasurably rich, and he stripped himself bare—for you—so that through his poverty you might inherit wealth you could never have earned."
    },
    "10": {
      "L": "And in this matter I give my judgment: this is expedient for you who began a year ago not only to do this but also to desire it.",
      "M": "And in this matter I give my opinion: it is to your advantage that you who began a year ago should have been the first not only to do this but also to desire it.",
      "T": "Here is my counsel—not a command, but advice: since you were the ones who started this a year ago, and started it with eager desire, finish what you began."
    },
    "11": {
      "L": "Now complete the doing, so that your readiness to desire it may be matched by your completing it out of what you have.",
      "M": "Now bring it to completion, so that the readiness to desire it may be matched by completing it from your resources.",
      "T": "The will was there from the start—now bring the deed to completion, contributing from what you actually have."
    },
    "12": {
      "L": "For if the willingness is present, it is acceptable according to what a man has, not according to what he does not have.",
      "M": "For if the willingness is there, a gift is acceptable according to what one has, not according to what one does not have.",
      "T": "God accepts the gift in proportion to what you have, not as a shortfall against what you lack. The willingness is the thing; the amount is secondary."
    },
    "13": {
      "L": "For I do not mean that others should be relieved and you burdened,",
      "M": "For I do not mean that there should be relief for others and hardship for you,",
      "T": "I am not asking you to exhaust yourselves so that others can take it easy."
    },
    "14": {
      "L": "but as a matter of equality, your abundance at the present time should supply their need, so that their abundance may also supply your need—that there may be equality,",
      "M": "but as a matter of fairness, your present abundance should supply their need, so that their abundance may also supply your need—so that there may be fairness.",
      "T": "The principle is reciprocal balance: right now your surplus covers their shortage; at another time, their surplus may cover yours. The goal is not charity that creates dependence, but mutual provision that creates genuine equality."
    },
    "15": {
      "L": "as it is written: 'He who gathered much had nothing left over, and he who gathered little had no lack.'",
      "M": "As it is written, 'Whoever gathered much had nothing left over, and whoever gathered little had no lack.'",
      "T": "Scripture captured this principle in the manna: in the wilderness, every morning's gathering levelled out—those who took much had no surplus, those who took little went without nothing. (Exodus 16:18)"
    },
    "16": {
      "L": "But thanks be to God who put the same earnestness on your behalf into the heart of Titus.",
      "M": "But thanks be to God, who put into the heart of Titus the same earnest care for you that I have.",
      "T": "I am grateful to God for this: he stirred the same deep concern for you in Titus's heart that burns in mine."
    },
    "17": {
      "L": "For he received the appeal but, being very eager, went to you of his own accord.",
      "M": "For he accepted the appeal, but being very eager, he went to you of his own accord.",
      "T": "Titus received my appeal, but he didn't need much persuading—his own eagerness sent him to you."
    },
    "18": {
      "L": "And we sent with him the brother who is praised throughout all the churches for his service to the gospel;",
      "M": "And with him we are sending the brother who is famous throughout all the churches for his service to the gospel;",
      "T": "With Titus we are also sending a brother whose work for the gospel has earned him a reputation across all the churches;"
    },
    "19": {
      "L": "and not only that, but he was also appointed by the churches to travel with us in connection with this gracious act that we are administering for the glory of the Lord himself and to show our eagerness—",
      "M": "And not only that, he has also been appointed by the churches to travel with us as we administer this gracious gift for the glory of the Lord himself and to show our eagerness to serve.",
      "T": "and not only that—the churches themselves chose him as our companion for this mission, since the whole collection is being administered for the Lord's glory and as a tangible sign of our eagerness to serve."
    },
    "20": {
      "L": "We aim to keep no one from finding fault with us over the handling of this abundant gift;",
      "M": "We are taking care that no one can find fault with us in our handling of this generous gift;",
      "T": "We have taken every precaution so that no one can accuse us of mishandling these funds—"
    },
    "21": {
      "L": "for we aim at what is honorable not only before the Lord but also before men.",
      "M": "for we have given thought to what is honorable, not only before the Lord but also in the sight of people.",
      "T": "we want what is right to be visible not only to God but to every human observer."
    },
    "22": {
      "L": "And we have sent with them our brother whom we have often tested and found eager in many matters, but now much more eager, because of his great confidence in you.",
      "M": "And with them we are sending our brother whom we have often tested and found eager in many matters, who is now even more eager because of his great confidence in you.",
      "T": "We are also sending another brother—someone we have tested and found trustworthy time and again—and his eagerness on this occasion is running high, because his confidence in you is strong."
    },
    "23": {
      "L": "As for Titus, he is my partner and fellow worker for your benefit; as for our brothers, they are messengers of the churches, the glory of Christ.",
      "M": "As for Titus, he is my partner and co-worker among you; as for our brothers, they are messengers of the churches, the glory of Christ.",
      "T": "To introduce them properly: Titus is my partner and fellow worker among you—fully trusted. The other brothers are envoys of the churches, bearers of Christ's honor."
    },
    "24": {
      "L": "Therefore show them before the churches the proof of your love and of our boasting about you.",
      "M": "So show them, before the churches, the proof of your love and the justification of our boasting on your behalf.",
      "T": "Give them something to take back: let the churches see, through how you treat these men, that the love is real—and that our boasting about you was no empty praise."
    }
  },
  "9": {
    "1": {
      "L": "For concerning the ministry to the saints, it is unnecessary for me to write to you;",
      "M": "Now regarding the ministry to the saints, it is unnecessary for me to write to you;",
      "T": "On the matter of the collection for God's people in Jerusalem, further instruction from me should be unnecessary—"
    },
    "2": {
      "L": "for I know your readiness, of which I boast to the Macedonians about you, saying that Achaia has been ready since last year; and your zeal has stirred up the majority of them.",
      "M": "for I know your eagerness, and I have boasted about you to the Macedonians, saying that Achaia has been ready since last year; and your enthusiasm has stirred up most of them.",
      "T": "I have already staked my reputation on it: I told the Macedonians that Achaia was ready a year ago. And that boast lit a fire—most of them were spurred to action by your example."
    },
    "3": {
      "L": "But I have sent the brothers, so that our boasting about you may not prove empty in this matter—so that, as I told them, you may be ready—",
      "M": "But I am sending the brothers so that our boasting about you may not prove empty in this case—so that you may be ready, as I said you would be—",
      "T": "Still, I am sending the brothers ahead precisely to make sure my boasting holds up. I said you were ready; I need you to be ready."
    },
    "4": {
      "L": "lest somehow if Macedonians come with me and find you unprepared, we—to say nothing of you—should be humiliated in this matter of which we were so confident.",
      "M": "For if any Macedonians come with me and find you unprepared, we would be humiliated—to say nothing of you—in this matter of which we have been so confident.",
      "T": "Think of how it would look: if the Macedonians arrive and find you empty-handed, we would be mortified—and so would you—after everything we said."
    },
    "5": {
      "L": "So I thought it necessary to urge the brothers to go on ahead to you and arrange in advance your promised gift, so that it might be ready as a generous gift, not as something extorted.",
      "M": "So I thought it necessary to urge the brothers to go on ahead to you and arrange your promised gift in advance, so that it may be ready as a generous act and not as an exaction.",
      "T": "That is why I am sending the brothers ahead—to get everything arranged before I arrive, so that the gift you already committed to is ready and waiting, given freely from generosity and not squeezed out under pressure."
    },
    "6": {
      "L": "This I say: he who sows sparingly will also reap sparingly, and he who sows bountifully will also reap bountifully.",
      "M": "Remember this: whoever sows sparingly will also reap sparingly, and whoever sows bountifully will also reap bountifully.",
      "T": "Here is the principle that governs all of this: you reap what you sow. A stingy sower goes home with a thin harvest; a generous sower fills his barn."
    },
    "7": {
      "L": "Each person must give as he has decided in his heart, not reluctantly or under compulsion, for God loves a cheerful giver.",
      "M": "Each one must give as he has decided in his heart, not reluctantly or under compulsion, for God loves a cheerful giver.",
      "T": "The only gift God delights in is the one given freely—decided in the heart beforehand, not dragged out under pressure. An eager, cheerful giver is precisely who God is looking for."
    },
    "8": {
      "L": "And God is able to make all grace abound toward you, so that having always all sufficiency in all things, you may abound in every good work.",
      "M": "And God is able to make every kind of grace abound toward you, so that having all sufficiency in all things at all times, you may overflow into every good work.",
      "T": "And here is what makes generosity sustainable: God himself replenishes the giver. He has the power to pour grace back into your life in such abundance that you are always fully provided for—and perpetually free to overflow into good work."
    },
    "9": {
      "L": "As it is written: 'He scattered, he gave to the poor; his righteousness endures forever.'",
      "M": "As it is written, 'He has scattered, he has given to the poor; his righteousness endures forever.'",
      "T": "Scripture describes this person perfectly in Psalm 112: 'He gave freely, he gave to those who had nothing—and the righteousness of that giving echoes on forever.'"
    },
    "10": {
      "L": "He who supplies seed to the sower and bread for food will supply and multiply your seed and increase the harvest of your righteousness.",
      "M": "He who supplies seed to the sower and bread for food will supply and multiply your seed and increase the harvest of your righteousness.",
      "T": "The God who gives the farmer his seed and gives the hungry their bread will do the same for you: he will give you more to give, and your generosity will keep bearing fruit."
    },
    "11": {
      "L": "You will be enriched in every way for all generosity, which produces thanksgiving to God through us.",
      "M": "You will be enriched in every way to produce all generosity, which through us produces thanksgiving to God.",
      "T": "As God makes you rich in every dimension of life, that richness pours out in generosity, which in turn flows back to God as the thanksgiving of those who receive it."
    },
    "12": {
      "L": "For the service rendered by this ministry not only supplies the needs of the saints but also overflows with many thanksgivings to God.",
      "M": "For the ministry of this service is not only supplying the needs of the saints, but is also overflowing through many thanksgivings to God.",
      "T": "This act of service accomplishes two things at once: it relieves real human need, and it sends up a flood of gratitude to God. The giving does more than the giving itself."
    },
    "13": {
      "L": "Through the proof of this service they glorify God for your obedience in professing the gospel of Christ and for the generosity of your sharing with them and with all.",
      "M": "Through the testing of this ministry they will glorify God for your obedience in acknowledging the gospel of Christ and for the generosity of your sharing with them and with everyone.",
      "T": "The ripple effects will reach further than the money itself. When they receive it, those saints in Jerusalem will glorify God—not just for the gift, but because your generosity is living proof that you have truly embraced the gospel of Christ."
    },
    "14": {
      "L": "And in their prayer for you, they will long for you because of the surpassing grace of God upon you.",
      "M": "And in their prayers for you, they will long for you because of the surpassing grace of God in you.",
      "T": "And you will gain something in return you could never buy: their prayers, and their hearts. They will ache with longing to know you, because they will have seen God's extraordinary grace at work in your lives."
    },
    "15": {
      "L": "Thanks be to God for his inexpressible gift!",
      "M": "Thanks be to God for his inexpressible gift!",
      "T": "And all of this—every strand of it—ends in the same place: thanks to God for the gift that surpasses every attempt to describe it."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, '2corinthians')
        merge_tier(existing, CORINTHIANS2, tier_key)
        save(tier_dir, '2corinthians', existing)
    print('2 Corinthians 7–9 written.')

if __name__ == '__main__':
    main()
