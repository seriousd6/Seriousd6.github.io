"""
MKT Hebrews chapter 13 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-hebrews-13-13.py

Translation decisions:
- G5360 φιλαδελφία (v1): "brotherly love" in L/M — the compound word's etymology (love of
    brothers) is preserved. In T: "love one another as brothers and sisters" — the familial
    warmth and gender-inclusivity of the Greek address to the congregation are both captured.
- G5381 φιλοξενία (v2): "hospitality to strangers" in L — the full compound meaning
    (love-of-strangers) is explicit; "hospitality" in M/T since the stranger-context is
    established by "some have entertained angels."
- G1242 διαθήκη (v20): "covenant" in all tiers — the blood-sealed, formally structured
    relationship. Not "testament" (which implies death of testator without the covenant-
    relationship sense Hebrews consistently intends).
- G166 αἰώνιος (v20 "eternal covenant"): "eternal" in L/M/T — modifying διαθήκη, the
    permanence of the new covenant is the point (echoing Jer 32:40 and Isa 55:3 LXX).
    Different from prior uses in chs 4-6 where "age-to-come" surfacing was more interpretive;
    here "eternal" is the right rendering since the covenant's permanence (not duration) is
    being stressed in a benediction context.
- G3056 λόγος: appears in three senses this chapter:
    v7 "the word of God" — the gospel/teaching they proclaimed (L/M/T all "word of God")
    v17 "give account" (ἀποδιδόντες λόγον) — financial/legal idiom for rendering an account
        to a superior; rendered "give account" in L, "give an account" in M/T
    v22 "word of exhortation" — the letter itself as pastoral address; "word of exhortation"
        in L/M, "message of encouragement" in T
- G2233 ἡγέομαι (vv7, 17, 24): "leaders" in all tiers — consistent with prior Hebrews scripts.
    "Rulers" is too political; "guides" is too weak; "leaders" carries the pastoral authority
    the author has in mind for congregational elders/overseers.
- G4102 πίστις (v7): "faith" in all tiers — the active, trusting allegiance demonstrated in
    the leaders' manner of life, not merely abstract belief.
- G5590 ψυχή (v17): "souls" in L — literal, source-accurate; "you" in M (natural English,
    since leaders are watching over the people themselves); expanded in T.
- G1515 εἰρήνη (v20 "God of peace"): the title is retained in all tiers. Not paraphrased —
    the "God of peace" formula appears in Paul's benedictions and carries covenant-
    reconciliation overtones stronger than a mere adjective would convey.
- v4 ἔστω implied: "Let marriage be honored" — the imperative ἔστω ("let it be") is implied
    in the Greek; English supplies "let" to convey the hortatory force.
- v20-21 form a single Greek sentence: v20 sets the subject (God of peace who brought up
    Jesus from the dead) and v21 states the prayer (equip you). The translation preserves
    this structure with a dash or relative clause break.
- v25 manuscript subscription: the interlinear includes scribal subscription tokens
    (G1125 "Written to the Hebrews, dispatched from Italy by Timothy") which appear in some
    Byzantine manuscripts but are not original text. The canonical 13:25 is the grace
    benediction only; the subscription is ignored.
- OT intertextuality:
    v5: quotes Deut 31:6, 8 / Josh 1:5 (LXX) — the double-negative emphatic "I will never
        leave you nor forsake you" (οὐ μή + subjunctive, two-fold) is preserved in L;
        "never … nor" in M; doubled emphasis surfaced in T.
    v6: quotes Ps 118:6 (LXX 117:6) — rendered as direct Scripture quotation in all tiers.
    v10-13: echo the Day of Atonement ritual (Lev 16) — the bodies burned outside the camp
        (v11) is the type; Jesus suffering outside the gate (v12) is the antitype; surfaced
        explicitly in T tier.
    v20: echoes Isa 63:11 (LXX, "shepherd of the sheep"), Zech 9:11 (blood of the covenant),
        Jer 32:40 (eternal covenant). These OT resonances make v20 a summary of the entire
        book's typological argument; T surfaces the shepherd-imagery's OT roots.
- Aspect:
    v1 μενέτω (present imperative): ongoing instruction — "keep on" or "continue"
    v12 ἔπαθεν (aorist): completed past act of suffering
    v17 ἀγρυπνοῦσιν (present participle): ongoing watching — leaders are currently doing this
    v20 ἀναγαγών (aorist participle): completed resurrection act
    v21 καταρτίσαι (aorist optative): wish/prayer for a complete divine equipping
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

HEBREWS = {
  "13": {
    "1": {
      "L": "Let brotherly love continue.",
      "M": "Let brotherly love continue.",
      "T": "Keep on loving one another as brothers and sisters in the family of God."
    },
    "2": {
      "L": "Do not neglect hospitality to strangers; for by this some have entertained angels without knowing it.",
      "M": "Do not forget to show hospitality to strangers, for by doing so some have entertained angels without knowing it.",
      "T": "Keep welcoming strangers into your homes. Some who did so found, without realizing it, that their guests were angels."
    },
    "3": {
      "L": "Remember those who are in bonds, as if bound with them; those being badly treated, as yourselves also being in the body.",
      "M": "Remember those who are in prison as if you were their fellow prisoners, and those who are mistreated as if you yourselves were suffering.",
      "T": "Think of those in prison as if you were locked up with them. Think of those who are suffering mistreatment as if their pain were your own — because you are bound together in one body."
    },
    "4": {
      "L": "Let marriage be held in honor among all, and let the marriage bed be undefiled; for fornicators and adulterers God will judge.",
      "M": "Let marriage be held in honor by all, and let the marriage bed be kept pure, for God will judge the sexually immoral and the adulterous.",
      "T": "Honor marriage — every one of you. Let the marriage bed remain undefiled. As for sexual immorality and adultery, God is the judge."
    },
    "5": {
      "L": "Let your manner of life be free from love of money; being content with what you have. For he himself has said: 'I will never leave you, nor will I ever forsake you.'",
      "M": "Keep your life free from love of money, and be content with what you have, for he has said: 'Never will I leave you; never will I forsake you.'",
      "T": "Live without greed. Learn to be satisfied with what God has given you. After all, he has pledged: 'I will never abandon you — no, never will I leave you behind.'"
    },
    "6": {
      "L": "So that we may say with confidence: 'The Lord is my helper; I will not fear. What shall man do to me?'",
      "M": "So we say with confidence: 'The Lord is my helper; I will not be afraid. What can anyone do to me?'",
      "T": "That pledge is why we can say with complete confidence: 'The Lord stands at my side as my helper — whom then shall I fear? What can any human being do to me?'"
    },
    "7": {
      "L": "Remember your leaders, those who spoke to you the word of God; and considering the outcome of their conduct, imitate their faith.",
      "M": "Remember your leaders, who spoke the word of God to you. Consider the outcome of their way of life and imitate their faith.",
      "T": "Call to mind your former leaders — those who taught you God's word. Look at how their lives ended; let what their faithful living produced move you to imitate their faith."
    },
    "8": {
      "L": "Jesus Christ is the same yesterday and today and forever.",
      "M": "Jesus Christ is the same yesterday and today and forever.",
      "T": "Jesus Christ does not change. He is the same yesterday, today, and throughout all the ages to come."
    },
    "9": {
      "L": "Do not be carried away by diverse and strange teachings; for it is good for the heart to be established by grace, not by foods, which have not benefited those who walk in them.",
      "M": "Do not be carried away by all kinds of strange teachings. It is good for the heart to be strengthened by grace, not by food regulations, which are of no benefit to those who observe them.",
      "T": "Do not be swept off course by a tide of novel and foreign teachings. What fortifies the heart is grace — not ritual food regulations, which have never benefited those who kept them."
    },
    "10": {
      "L": "We have an altar from which those who serve the tabernacle have no right to eat.",
      "M": "We have an altar from which those who minister at the tabernacle have no right to eat.",
      "T": "We have an altar. Those who still officiate in the old tabernacle system have no right to eat from what is offered at ours."
    },
    "11": {
      "L": "For the bodies of those animals whose blood is brought into the sanctuary by the high priest as an offering for sin are burned outside the camp.",
      "M": "For the bodies of those animals whose blood is brought into the Most Holy Place by the high priest as a sin offering are burned outside the camp.",
      "T": "Here is the pattern from the Day of Atonement: the high priest carries blood into the sanctuary as a sin offering, but the bodies of those animals are burned outside the camp."
    },
    "12": {
      "L": "Therefore Jesus also, that he might sanctify the people through his own blood, suffered outside the gate.",
      "M": "And so Jesus also suffered outside the city gate to make the people holy through his own blood.",
      "T": "Jesus followed that same pattern — suffering outside the city gate so that, by his own blood, he might make his people holy."
    },
    "13": {
      "L": "Let us therefore go out to him outside the camp, bearing his reproach.",
      "M": "Let us, then, go to him outside the camp, bearing the disgrace he bore.",
      "T": "So let us go to him — outside the camp, outside the walls of accepted religious life — and bear the same shame he bore."
    },
    "14": {
      "L": "For here we do not have a continuing city, but we seek the city to come.",
      "M": "For here we do not have an enduring city, but we are looking for the city that is to come.",
      "T": "We have no permanent home here. We are a people who look forward to the city that is still to come."
    },
    "15": {
      "L": "Through him therefore let us offer up a sacrifice of praise to God continually, that is, the fruit of lips giving thanks to his name.",
      "M": "Through Jesus, therefore, let us continually offer to God a sacrifice of praise — the fruit of lips that openly profess his name.",
      "T": "Through Jesus, then, let us bring God a continual sacrifice of praise — the living thank-offering of lips that confess his name."
    },
    "16": {
      "L": "But do not neglect to do good and to share what you have; for with such sacrifices God is well pleased.",
      "M": "And do not forget to do good and to share with others, for with such sacrifices God is pleased.",
      "T": "Do not neglect the practical side of worship: doing good and sharing what you have with others. These are the sacrifices that truly please God."
    },
    "17": {
      "L": "Obey your leaders and submit to them; for they keep watch over your souls as those who will give account, that they may do this with joy and not with sighing; for that would be unprofitable for you.",
      "M": "Have confidence in your leaders and submit to their authority, because they keep watch over you as those who must give an account. Do this so that their work will be a joy, not a burden, for that would be of no benefit to you.",
      "T": "Trust your leaders and come under their guidance. They stand guard over you and will answer to God for how they have cared for you. Make their work a joy — not a grief. Resistance does you no good in the end."
    },
    "18": {
      "L": "Pray for us; for we are persuaded that we have a good conscience, desiring to live honorably in all things.",
      "M": "Pray for us. We are sure that we have a clear conscience and desire to live honorably in every way.",
      "T": "Please pray for us. We are clear in our own conscience, and our aim is to live with complete integrity in everything."
    },
    "19": {
      "L": "And I urge you the more earnestly to do this, that I may be restored to you the sooner.",
      "M": "I particularly urge you to pray so that I may be restored to you soon.",
      "T": "Above all, I am asking you to pray — because I long to be reunited with you, and soon."
    },
    "20": {
      "L": "Now the God of peace, who brought up from the dead our Lord Jesus, the great shepherd of the sheep, through the blood of the eternal covenant,",
      "M": "Now may the God of peace, who through the blood of the eternal covenant brought back from the dead our Lord Jesus, that great shepherd of the sheep,",
      "T": "And may the God of peace — the one who raised from death our Lord Jesus, the great Shepherd of the flock, through the blood of the eternal covenant —"
    },
    "21": {
      "L": "equip you in every good thing to do his will, working in us that which is well-pleasing in his sight through Jesus Christ; to whom be glory to the ages of ages. Amen.",
      "M": "equip you with everything good for doing his will, and may he work in us what is pleasing to him, through Jesus Christ, to whom be glory for ever and ever. Amen.",
      "T": "equip you fully with every good thing for doing his will, and may he himself produce in us what pleases him — all through Jesus Christ, to whom be glory for ever and ever. Amen."
    },
    "22": {
      "L": "And I urge you, brothers, bear with the word of exhortation, for I have also written to you briefly.",
      "M": "Brothers and sisters, I urge you to bear with my word of exhortation, for in fact I have written to you quite briefly.",
      "T": "Friends, I ask you to receive this message of encouragement patiently — after all, this letter has not been long."
    },
    "23": {
      "L": "Know that our brother Timothy has been released; with whom, if he comes soon, I will see you.",
      "M": "I want you to know that our brother Timothy has been released. If he arrives soon, I will come with him to see you.",
      "T": "I have good news: our brother Timothy has been set free. If he arrives in time, he will be with me when I come to see you."
    },
    "24": {
      "L": "Greet all your leaders and all the saints. Those from Italy send you greetings.",
      "M": "Greet all your leaders and all the Lord's people. Those from Italy send you their greetings.",
      "T": "Give our warm greetings to your leaders and to all God's people. Those here from Italy send their greetings to you."
    },
    "25": {
      "L": "Grace be with you all.",
      "M": "Grace be with you all.",
      "T": "May God's grace be with every one of you."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'hebrews')
        merge_tier(existing, HEBREWS, tier_key)
        save(tier_dir, 'hebrews', existing)
    print('Hebrews 13 written.')

if __name__ == '__main__':
    main()
