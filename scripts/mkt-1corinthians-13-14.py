"""
MKT 1 Corinthians chapters 13–14 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-1corinthians-13-14.py

Translation decisions:
- G26 (ἀγάπη): "love" in all tiers — KJV "charity" is archaic; ἀγάπη is the willed, covenantal,
  self-giving love that Paul is contrasting with spiritual gifts. Never softened to "affection."
- G1100 (γλῶσσα): "tongue(s)" in L/M; T may specify "ecstatic speech" or "other language" where
  context clarifies the phenomenon (14:2 = ecstatic prayer speech; 14:21 = foreign human language).
- G4151 (πνεῦμα): lowercase "spirit" in ch 14 vv.2,14,15,16 — refers to the human spirit/spiritual
  faculty in prayer, not the divine Spirit. Contrast with capitalized "Spirit" in Pauline pneumatology
  contexts (as established in Romans script).
- G5046 (τέλειος): "complete" in M (13:10) — "perfect" is the classic rendering but risks Platonic
  overtones; Paul means eschatological wholeness, not ethical perfection. L retains "perfect."
- G2072 (ἔσοπτρον): 13:12 "mirror dimly" — ancient mirrors were polished bronze, giving an indirect
  and dark reflection. The Greek adds ἐν αἰνίγματι (in a riddle/enigma), preserved in L; M and T
  convey the sense of obscured, partial vision.
- G1577 (ἐκκλησία): "church" throughout — consistent with prior Pauline scripts (Romans, Galatians).
  "Assembly" is etymologically more accurate but "church" carries the full covenantal weight here.
- G3619 (οἰκοδομή) / G3618 (οἰκοδομέω): "edification" / "build up" — "build up" preferred in M/T
  because it preserves the architectural metaphor underlying Paul's entire argument in ch 14.
- G3114 (μακροθυμέω): 13:4 "patient" in M; L retains "long-suffering" to preserve the compound sense
  (long + passion/anger) — it is about holding the anger long, not merely waiting.
- G2399 (ἰδιώτης): 14:16,23,24 "outsider/inquirer" — not simply "unlearned"; it means one outside
  the circle of those with the gift, whether a nonbeliever or an unbaptised seeker. M renders
  "inquirer" at 14:23-24 where the context is corporate worship.
- 14:21 OT quotation: Isaiah 28:11-12, here called "the Law" (νόμος) as Paul uses the term broadly
  for the entire OT scripture. The LXX wording is followed; T adds the judicial note (judgment, not
  blessing) which is integral to Paul's argument about tongues as a sign of divine judgment.
- 14:34-35 textual note: these verses appear after v.40 in some Western manuscripts (D and others);
  Fee and Thiselton argue interpolation from 1 Tim 2:11-12. The verses are present in all major
  manuscripts and are translated in canonical position. T renders straightforwardly without excising,
  noting the contextual contrast with 11:5 where women prophesying is assumed permissible.
- 14:38 textual variant: Majority text "ἀγνοεῖτω" (let him be ignorant); some manuscripts read
  "ἀγνοεῖται" (he is not recognized). Both readings translated as "let him remain in his refusal"
  in T to cover the sense of divine/apostolic judgment on the recalcitrant.
- Aspect notes: Ch 13 uses gnomic presents throughout (vv.4-8) — "love IS patient" (ongoing
  characteristic, not one-time act). The aorists in v.11 (ἐγενόμην, κατήργηκα) mark clean
  transitions: I became a man / I did away with childish things = completed life-stage transition.
  The perfects at 13:12 (ἐπεγνώσθην) = "I have been fully known" with lasting state implication.
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

CORINTHIANS = {
  "13": {
    "1": {
      "L": "If I speak with the tongues of men and of angels, but have not love, I have become sounding brass or a clanging cymbal.",
      "M": "If I speak in the tongues of men or of angels, but have not love, I am only a resounding gong or a clanging cymbal.",
      "T": "Though I could speak every human language and the language of angels, if I have no love, I am nothing more than a noise—a hollow gong, a jangling cymbal."
    },
    "2": {
      "L": "And if I have prophecy and know all mysteries and all knowledge, and if I have all faith so as to remove mountains, but have not love, I am nothing.",
      "M": "If I have the gift of prophecy and can understand all mysteries and all knowledge, and if I have a faith that can move mountains, but have not love, I am nothing.",
      "T": "And if I had the power of prophecy and knew every hidden mystery, possessing all knowledge—even a faith that could move mountains—without love I would be nothing at all."
    },
    "3": {
      "L": "And if I give all my possessions to feed the poor, and deliver my body to be burned, but have not love, it profits me nothing.",
      "M": "If I give away everything I own to feed the poor, and surrender my body to the flames, but have not love, I gain nothing.",
      "T": "And if I distributed every last thing I owned to feed the hungry, and gave up my body to be burned—without love, it would gain me nothing."
    },
    "4": {
      "L": "Love is long-suffering, love is kind; love does not envy; love does not boast, is not puffed up;",
      "M": "Love is patient, love is kind. It does not envy, it does not boast, it is not proud.",
      "T": "Love holds on without giving up, and pours itself out in kindness. Love is not eaten up with envy. It does not strut or swagger. It is not full of itself."
    },
    "5": {
      "L": "Does not behave unseemly, does not seek its own things, is not easily provoked, does not take into account evil;",
      "M": "It does not dishonor others, it is not self-seeking, it is not easily angered, it keeps no record of wrongs.",
      "T": "Love does not act shamefully toward others. It does not insist on its own way. It does not flare up in anger. It does not file away a list of wrongs received."
    },
    "6": {
      "L": "Does not rejoice over unrighteousness, but rejoices with the truth;",
      "M": "Love does not delight in evil but rejoices with the truth.",
      "T": "Love takes no pleasure in evil; it celebrates only what is true."
    },
    "7": {
      "L": "Bears all things, believes all things, hopes all things, endures all things.",
      "M": "It always protects, always trusts, always hopes, always perseveres.",
      "T": "Love bears every burden, puts its full trust in God, holds on to hope in every circumstance, and stands firm through every storm."
    },
    "8": {
      "L": "Love never fails; but whether there are prophecies, they will be done away; whether there are tongues, they will cease; whether there is knowledge, it will be done away.",
      "M": "Love never fails. But where there are prophecies, they will cease; where there are tongues, they will be stilled; where there is knowledge, it will pass away.",
      "T": "Love will never come to an end. Prophecies will run their course and fall silent. Tongues will cease. Knowledge will be left behind. But love goes on."
    },
    "9": {
      "L": "For we know in part and we prophesy in part;",
      "M": "For we know in part and we prophesy in part,",
      "T": "Our knowledge is partial, and our prophesying is partial—"
    },
    "10": {
      "L": "but when the perfect comes, the partial will be done away.",
      "M": "but when completeness comes, what is in part disappears.",
      "T": "—but when what is whole and complete arrives, everything partial will be left behind."
    },
    "11": {
      "L": "When I was a child, I spoke as a child, I thought as a child, I reasoned as a child; when I became a man, I did away with the things of a child.",
      "M": "When I was a child, I talked like a child, I thought like a child, I reasoned like a child. When I became a man, I put the ways of childhood behind me.",
      "T": "When I was a child, I spoke like a child, thought like a child, and reasoned like a child. When I grew up, I left all those childish ways behind. One stage of life gives way to the next."
    },
    "12": {
      "L": "For now we see through a mirror in a riddle, but then face to face; now I know in part, but then I will know fully even as I also have been fully known.",
      "M": "For now we see only a reflection as in a mirror; then we shall see face to face. Now I know in part; then I shall know fully, even as I am fully known.",
      "T": "Right now we see only a dim, puzzling reflection—as if peering into a polished bronze mirror. But one day we will see face to face. Now I know only part of the truth; then I will know fully, just as God has always fully known me."
    },
    "13": {
      "L": "And now these three remain: faith, hope, love; but the greatest of these is love.",
      "M": "And now these three remain: faith, hope, and love. But the greatest of these is love.",
      "T": "Three things endure: faith, hope, and love. And the greatest of all three is love."
    }
  },
  "14": {
    "1": {
      "L": "Pursue love, and earnestly desire spiritual gifts, but especially that you may prophesy.",
      "M": "Follow the way of love and eagerly desire gifts of the Spirit, especially prophecy.",
      "T": "Make love your highest pursuit, and then be zealous for the gifts of the Spirit—above all, the gift of prophecy."
    },
    "2": {
      "L": "For the one speaking in a tongue does not speak to men but to God; for no one understands, but in the spirit he speaks mysteries.",
      "M": "For anyone who speaks in a tongue does not speak to people but to God. Indeed, no one understands them; they utter mysteries by the Spirit.",
      "T": "When someone speaks in a tongue, they are not addressing other people—they are speaking directly to God. No one can follow what they say, because by the Spirit they are speaking hidden things."
    },
    "3": {
      "L": "But the one who prophesies speaks to men edification and exhortation and comfort.",
      "M": "But the one who prophesies speaks to people for their strengthening, encouraging, and comfort.",
      "T": "But the one who prophesies speaks directly to people, building them up, urging them forward, and strengthening their hearts."
    },
    "4": {
      "L": "The one who speaks in a tongue edifies himself; but the one who prophesies edifies the church.",
      "M": "Anyone who speaks in a tongue edifies themselves, but the one who prophesies edifies the church.",
      "T": "Speaking in a tongue builds up the individual; prophesying builds up the whole congregation."
    },
    "5": {
      "L": "Now I desire all of you to speak in tongues, but rather that you would prophesy; and greater is the one who prophesies than the one who speaks in tongues, unless he interprets, so that the church may receive edification.",
      "M": "I would like every one of you to speak in tongues, but I would rather have you prophesy. The one who prophesies is greater than the one who speaks in tongues, unless someone interprets, so that the church may be built up.",
      "T": "I would be glad for every one of you to speak in tongues—but I would rather you prophesied. Unless someone interprets so that the congregation is built up, the prophet holds the greater gift."
    },
    "6": {
      "L": "But now, brothers, if I come to you speaking in tongues, what will I benefit you unless I speak to you either in revelation or in knowledge or in prophecy or in teaching?",
      "M": "Now, brothers and sisters, if I come to you and speak in tongues, what good will I be to you, unless I bring you some revelation or knowledge or prophecy or word of instruction?",
      "T": "Think about it, brothers and sisters: if I came to you and only spoke in tongues, what benefit would that be? I would only be helping you if I brought something you could actually receive—a revelation, a piece of knowledge, a prophetic word, or some teaching."
    },
    "7": {
      "L": "Yet even lifeless things that produce sound, whether pipe or harp, if they give no distinction in the notes, how will it be known what is piped or harped?",
      "M": "Even in the case of lifeless things that make sounds, such as the pipe or harp, how will anyone know what tune is being played unless there is a distinction in the notes?",
      "T": "Even inanimate instruments—a flute, a harp—have to produce distinct notes. Otherwise, how can anyone tell what melody is being played?"
    },
    "8": {
      "L": "For if the trumpet gives an uncertain sound, who will prepare himself for battle?",
      "M": "Again, if the trumpet does not sound a clear call, who will get ready for battle?",
      "T": "If a battle trumpet sounds an unclear note, no soldier will know to arm himself."
    },
    "9": {
      "L": "So also you, unless you utter by the tongue speech that is clear, how will it be known what is spoken? For you will be speaking into the air.",
      "M": "So it is with you. Unless you speak intelligible words with your tongue, how will anyone know what you are saying? You will just be speaking into the air.",
      "T": "The same applies when you speak: unless the words you use can be understood, you might as well be talking to the wind."
    },
    "10": {
      "L": "There are, it may be, many kinds of languages in the world, and none of them is without meaning.",
      "M": "Undoubtedly there are all sorts of languages in the world, yet none of them is without meaning.",
      "T": "There are countless languages spoken across the world, and every single one carries meaning for its speakers."
    },
    "11": {
      "L": "If then I do not know the meaning of the language, I will be a barbarian to the one speaking, and the one speaking will be a barbarian to me.",
      "M": "If I do not grasp the meaning of what someone is saying, I am a foreigner to the speaker, and the speaker is a foreigner to me.",
      "T": "But if I don't understand the language, I am a foreigner to the speaker—and the speaker is a foreigner to me. We are strangers to each other."
    },
    "12": {
      "L": "So also you, since you are zealous of spiritual things, seek to abound for the edification of the church.",
      "M": "So it is with you. Since you are eager for gifts of the Spirit, try to excel in those that build up the church.",
      "T": "You are clearly eager for spiritual things—so channel that zeal toward gifts that build others up."
    },
    "13": {
      "L": "Therefore let the one who speaks in a tongue pray that he may interpret.",
      "M": "For this reason the one who speaks in a tongue should pray that they may interpret what they say.",
      "T": "So if you speak in a tongue, pray also for the ability to interpret what you have said."
    },
    "14": {
      "L": "For if I pray in a tongue, my spirit prays, but my mind is unfruitful.",
      "M": "For if I pray in a tongue, my spirit prays, but my mind is unengaged.",
      "T": "When I pray in a tongue, my spirit is active in prayer—but my mind produces nothing anyone can receive."
    },
    "15": {
      "L": "What is it then? I will pray with the spirit, and I will also pray with the mind; I will sing with the spirit, and I will also sing with the mind.",
      "M": "So what shall I do? I will pray with my spirit, but I will also pray with my understanding; I will sing with my spirit, but I will also sing with my understanding.",
      "T": "So here is what I will do: I will pray with my spirit fully engaged—and I will pray so that my mind is engaged too. I will sing praise with my spirit—and with my mind as well."
    },
    "16": {
      "L": "Otherwise if you bless with the spirit, how will the one who fills the place of the outsider say the 'Amen' at your giving of thanks, since he does not know what you are saying?",
      "M": "Otherwise when you are praising God in the Spirit, how can someone else who is now in the position of an inquirer say 'Amen' to your thanksgiving, since they do not know what you are saying?",
      "T": "If you offer a blessing only in the Spirit, how can an outsider sitting with you say 'Amen' to your thanksgiving? They have no idea what you said."
    },
    "17": {
      "L": "For you indeed give thanks well, but the other person is not edified.",
      "M": "You are giving thanks well enough, but no one else is built up.",
      "T": "Your heart may be sincere in giving thanks, but the person beside you receives nothing."
    },
    "18": {
      "L": "I thank God, I speak in tongues more than all of you;",
      "M": "I thank God that I speak in tongues more than all of you.",
      "T": "I am thankful to God—I speak in tongues more than any of you."
    },
    "19": {
      "L": "but in the church I desire to speak five words with my mind, so that I may also instruct others, rather than ten thousand words in a tongue.",
      "M": "But in the church I would rather speak five intelligible words to instruct others than ten thousand words in a tongue.",
      "T": "Yet in a gathered congregation I would rather say five words that people can understand than ten thousand words in a tongue. Five words that teach are worth more than a flood of untranslated speech."
    },
    "20": {
      "L": "Brothers, do not be children in your thinking; but in evil be infants, and in your thinking be mature.",
      "M": "Brothers and sisters, stop thinking like children. In regard to evil be infants, but in your thinking be adults.",
      "T": "Brothers and sisters, don't stay at the childhood level in your thinking. When it comes to evil, yes—be as innocent as infants. But in your understanding, grow up."
    },
    "21": {
      "L": "In the Law it is written: 'By men of other tongues and by lips of others I will speak to this people, and even so they will not listen to Me,' says the Lord.",
      "M": "In the Law it is written: 'With other tongues and through the lips of foreigners I will speak to this people, but even then they will not listen to me, says the Lord.'",
      "T": "The scriptures themselves say it—and the Lord is the speaker—'With foreign tongues and the lips of strangers I will speak to this people, and even then they will not listen.' That word was a sign of judgment, not a blessing."
    },
    "22": {
      "L": "So then tongues are for a sign, not to those who believe but to unbelievers; but prophecy is not for unbelievers but for those who believe.",
      "M": "Tongues, then, are a sign, not for believers but for unbelievers; prophecy, however, is not for unbelievers but for believers.",
      "T": "Tongues, then, are a sign—not for the community of faith, but for those who do not believe. Prophecy, by contrast, is not aimed at outsiders but at those who belong to God."
    },
    "23": {
      "L": "Therefore if the whole church assembles together and all speak in tongues, and outsiders or unbelievers enter, will they not say that you are mad?",
      "M": "So if the whole church comes together and everyone speaks in tongues, and inquirers or unbelievers come in, will they not say that you are out of your mind?",
      "T": "So imagine the whole congregation gathering and everyone speaking in tongues. Then an outsider or a nonbeliever walks in—won't they conclude that you have all lost your minds?"
    },
    "24": {
      "L": "But if all prophesy and some unbeliever or outsider enters, he is convicted by all, he is examined by all;",
      "M": "But if an unbeliever or an inquirer comes in while everyone is prophesying, they are convicted of sin and are brought under judgment by all,",
      "T": "But if all are prophesying and a nonbeliever or outsider walks in—the word spoken to the congregation becomes the word that pierces that person. They find themselves exposed and called to account by what they hear."
    },
    "25": {
      "L": "the secrets of his heart are disclosed; and so falling on his face he will worship God, declaring that God is certainly among you.",
      "M": "as the secrets of their hearts are laid bare. So they will fall down and worship God, exclaiming, 'God is really among you!'",
      "T": "The hidden things of their heart are laid bare. And what happens? They fall on their face in worship, declaring, 'God is truly in this place.'"
    },
    "26": {
      "L": "What is it then, brothers? When you come together, each one has a psalm, has a teaching, has a revelation, has a tongue, has an interpretation. Let all things be done for edification.",
      "M": "What then shall we say, brothers and sisters? When you come together, each of you has a hymn, or a word of instruction, a revelation, a tongue or an interpretation. Everything must be done so that the church may be built up.",
      "T": "So then, brothers and sisters, what should your gatherings look like? When you come together, one person may bring a song of praise, another a word of teaching, another a revelation, another a tongue, another an interpretation. Let everything serve the building up of the community."
    },
    "27": {
      "L": "If any speak in a tongue, let it be by two or at the most three, and each in turn, and let one interpret.",
      "M": "If anyone speaks in a tongue, two—or at the most three—should speak, one at a time, and someone must interpret.",
      "T": "When tongues are used, limit it to two or three at most, and have them speak one at a time. And someone must interpret."
    },
    "28": {
      "L": "But if there is no interpreter, let him keep silence in the church, and let him speak to himself and to God.",
      "M": "If there is no interpreter, the speaker should keep quiet in the church and speak to himself and to God.",
      "T": "If no one present can interpret, the tongue-speaker should stay silent in the assembly—using that gift in private prayer to God instead."
    },
    "29": {
      "L": "Let two or three prophets speak, and let the others weigh what is said.",
      "M": "Two or three prophets should speak, and the others should weigh carefully what is said.",
      "T": "Let two or three prophets speak, and the rest of the congregation should carefully discern what has been said."
    },
    "30": {
      "L": "But if a revelation is made to another sitting by, let the first keep silence.",
      "M": "And if a revelation comes to someone who is sitting down, the first speaker should stop.",
      "T": "If a fresh word comes to someone else sitting in the congregation, the first speaker should give way."
    },
    "31": {
      "L": "For you can all prophesy one by one, so that all may learn and all may be encouraged.",
      "M": "For you can all prophesy in turn so that everyone may be instructed and encouraged.",
      "T": "You can all take turns prophesying, so that the whole community is taught and strengthened."
    },
    "32": {
      "L": "And the spirits of prophets are subject to the prophets,",
      "M": "The spirits of prophets are subject to the control of prophets.",
      "T": "The prophetic impulse does not override a prophet's self-control—what the Spirit stirs within them remains under their own governance."
    },
    "33": {
      "L": "for God is not a God of confusion but of peace—as in all the churches of the saints.",
      "M": "For God is not a God of disorder but of peace—as is the case in all the congregations of the Lord's people.",
      "T": "For the God we serve is not the author of chaos but of peace. This is the pattern in every congregation of God's people."
    },
    "34": {
      "L": "Let the women keep silence in the churches; for they are not permitted to speak, but let them be in subjection, as the Law also says.",
      "M": "Women should remain silent in the churches. They are not allowed to speak, but must be in submission, as the law says.",
      "T": "Women are to be silent in the assemblies; they are not permitted to speak, but are to hold their place, as the Law itself teaches."
    },
    "35": {
      "L": "And if they desire to learn anything, let them ask their own husbands at home; for it is shameful for a woman to speak in the church.",
      "M": "If they want to inquire about something, they should ask their own husbands at home; for it is disgraceful for a woman to speak in the church.",
      "T": "If they have questions about what was said, let them ask their husbands at home. It is a dishonour to the assembly for a woman to speak up in that context."
    },
    "36": {
      "L": "Or was it from you that the word of God went out? Or did it come to you only?",
      "M": "Or did the word of God originate with you? Or are you the only people it has reached?",
      "T": "Did the word of God begin with you? Did it reach you alone? Do you imagine yourselves the sole arbiters of how it is practiced?"
    },
    "37": {
      "L": "If anyone thinks himself to be a prophet or spiritual, let him recognize that the things I write to you are the Lord's commandment.",
      "M": "If anyone thinks they are a prophet or otherwise gifted by the Spirit, let them acknowledge that what I am writing to you is the Lord's command.",
      "T": "Anyone who claims to be a prophet or a Spirit-gifted person should be able to recognize that what I am writing here carries the authority of the Lord."
    },
    "38": {
      "L": "But if anyone is ignorant, let him be ignorant.",
      "M": "But if anyone ignores this, they will themselves be ignored.",
      "T": "If someone refuses to acknowledge it, let them remain in their refusal—God will sort it out."
    },
    "39": {
      "L": "Therefore, my brothers, earnestly desire to prophesy, and do not forbid speaking in tongues.",
      "M": "Therefore, my brothers and sisters, be eager to prophesy, and do not forbid speaking in tongues.",
      "T": "So, my dear brothers and sisters: be zealous for prophecy, and don't shut down the gift of tongues."
    },
    "40": {
      "L": "But let all things be done decently and in order.",
      "M": "But everything should be done in a fitting and orderly way.",
      "T": "Only let everything be done fittingly and with good order."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, '1corinthians')
        merge_tier(existing, CORINTHIANS, tier_key)
        save(tier_dir, '1corinthians', existing)
    print('1 Corinthians 13–14 written.')

if __name__ == '__main__':
    main()
