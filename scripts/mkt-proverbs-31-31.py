"""
MKT Proverbs chapter 31 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-proverbs-31-31.py

Translation decisions:

- H2428 (חַיִל, chayil): "valor / strength / worth" — the same word used in v3 (strength the
  king is warned not to squander on destructive women) and in v10/v29 (the woman of chayil at
  the climax of the book). The echo is structural and intentional. L: "valor" (v10), "virtuously"
  (v29); M: "excellent" (v10), "excellently" (v29); T: "valor" (v10), "excellence" (v29).

- H3068 (יהוה, YHWH): "LORD" in L/M; "the LORD" in T — consistent with all prior Proverbs scripts.

- H2617 (חֶסֶד, hesed): v26 "the instruction of kindness / torah of faithful love." This is not
  merely 'nice teaching' but speech shaped by covenant loyalty. L: "law of kindness"; M: "faithful
  instruction"; T: surfaces the hesed dynamic explicitly.

- H4853 (מַשָּׂא, massa'): v1 "oracle / burden / prophecy." This is the technical term for a
  prophetic utterance or weighty word. Applied here to a mother's instruction to a king — the
  weight of the word is real even though the speaker is not a classical prophet. L: "prophecy";
  M: "oracle"; T: "word of weight."

- H5315 (נֶפֶשׁ, nephesh): v6 "bitter of soul" — the embodied, grieving self, not an immaterial
  soul. L: "soul"; M: "those bitter in soul"; T: contextual.

- H8144 (שָּׁנִי, shani): v21 "scarlet." The household is clothed in scarlet — quality wool
  dyed at cost, indicating genuine provision, not mere adequacy. L/M: "scarlet"; T: notes the
  quality dimension.

- H1248 (בַּר, bar): v2 three-fold "son" using the Aramaic loanword bar, not the Hebrew ben —
  marking the non-Israelite (likely Arabian) origin of the Lemuel oracle. L/M/T: "son" rendered
  simply; the Aramaic register noted here, not cluttered into the text.

- Structural note: vv. 1–9 are the oracle of Lemuel's mother — practical royal advice (against
  women, wine, and injustice). vv. 10–31 are the 'Eshet Chayil' poem, an alphabetic acrostic
  (Hebrew letters aleph through taw — the full alphabet, A to Z). The acrostic cannot be
  reproduced in English; the T tier acknowledges the structure and surfaces the full interpretive
  weight of each verse.

- The Eshet Chayil (vv. 10–31) is frequently misread as a domestic ideal. The poem describes
  a woman of commerce, investment, charity, wisdom, and public honor — chayil, the same word
  used for military valor. T tier consistently surfaces this dimension.

- Gnomic aspect: Hebrew participles and imperfects in the acrostic rendered as simple present
  throughout — the poem describes a characteristic type, not a one-time event.

- v21 "scarlet" (H8144): some MSS tradition reads "double garments" (layered for warmth) by
  paronomasia. The MT is "scarlet." L/M follow MT; T notes the range.

- v10 "rubies" (H6443, peninim): pearls, corals, or red gems — the exact stone is uncertain.
  "Rubies" is the traditional rendering and is retained here.
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


PROVERBS = {
  "31": {
    "1": {
      "L": "The words of King Lemuel, the prophecy which his mother taught him.",
      "M": "The words of King Lemuel, the oracle that his mother taught him.",
      "T": "What follows are the words of King Lemuel — an oracle, a word of weight, that his mother pressed deep into him. The voice behind the king is his mother's."
    },
    "2": {
      "L": "What, my son? And what, son of my womb? And what, son of my vows?",
      "M": "What should I say, my son? What, son of my womb? What, son of my vows?",
      "T": "What do I tell you — my son, the child of my own body, the one I vowed to God before you arrived? What is the one thing worth saying to a king before he rules? The three questions are not rhetorical anxiety; they are the intensity of a mother searching for the most important words."
    },
    "3": {
      "L": "Give not your strength to women, nor your ways to those who destroy kings.",
      "M": "Do not give your strength to women, nor your vigor to those who ruin kings.",
      "T": "Do not pour the best of yourself — your chayil, your strength and valor — into women who will drain it, nor let your path be shaped by those who have brought kings down before you. The warning is precise: it is not women as such but the dissipation of ruling strength that destroys."
    },
    "4": {
      "L": "It is not for kings, O Lemuel, it is not for kings to drink wine, nor for rulers to crave strong drink.",
      "M": "It is not for kings, O Lemuel — not for kings to drink wine, nor for rulers to desire strong drink.",
      "T": "O Lemuel — this is not for you. The person who holds power over other people's lives cannot afford to fog that power with wine. What ordinary men can afford to do with their evenings, kings cannot afford to do at all."
    },
    "5": {
      "L": "Lest they drink and forget the law and pervert the rights of all the afflicted.",
      "M": "Lest they drink and forget the law and pervert the judgment of all the afflicted.",
      "T": "Here is what drunken rule produces: the king forgets the legal protections owed to the powerless. He bends verdicts toward whoever caught his clouded attention last. The afflicted, who have no advocate but the king, lose their case before they open their mouths."
    },
    "6": {
      "L": "Give strong drink to the one who is perishing, and wine to those who are bitter of soul.",
      "M": "Give strong drink to one who is perishing, and wine to those who are bitter in soul.",
      "T": "Strong drink does have a use — for the dying, for those whose grief runs so deep that nothing else reaches it. There, wine is a mercy. It is not for the king, who needs clarity to govern; it is for the one who is past governing and simply needs relief."
    },
    "7": {
      "L": "Let him drink and forget his poverty and remember his misery no more.",
      "M": "Let him drink and forget his poverty and remember his misery no more.",
      "T": "The poor man whose suffering has no remedy — let him have, at least, the mercy of forgetting it for an evening. This is not a prescription for society; it is a concession to human pain. Some suffering cannot be solved right now. Temporary relief is still relief."
    },
    "8": {
      "L": "Open your mouth for the mute, for the rights of all the destitute.",
      "M": "Open your mouth for the mute, for the cause of all who are left desolate.",
      "T": "Some people cannot plead their own case — silenced by powerlessness, by poverty, by a system that has already set them aside. The king's voice is their only voice. Use it for them."
    },
    "9": {
      "L": "Open your mouth, judge righteously, and plead the cause of the poor and needy.",
      "M": "Open your mouth, judge righteously, and defend the cause of the poor and needy.",
      "T": "This is the whole of royal justice in two lines: speak, judge fairly, and be the advocate the poor cannot be for themselves. The king who does this has fulfilled the purpose of kingship. The oracle closes here; the poem begins."
    },
    "10": {
      "L": "A wife of valor, who can find? She is far more precious than rubies.",
      "M": "An excellent wife — who can find her? Her worth far surpasses that of rubies.",
      "T": "Eshet chayil — a woman of strength and valor. The same word the mother used in warning the king not to squander his chayil is now the word for the woman the book has been moving toward. The question is not despair but wonder at her rarity and worth. She is beyond price."
    },
    "11": {
      "L": "The heart of her husband trusts in her, and he shall have no lack of gain.",
      "M": "Her husband's heart trusts in her fully, and he will have no shortage of good things.",
      "T": "He trusts her completely — not just emotionally but practically, financially. She has earned a depth of confidence that makes his life richer in every dimension. The man who can fully trust his wife is not spending energy defending himself at home."
    },
    "12": {
      "L": "She does him good and not evil all the days of her life.",
      "M": "She does him good and not evil all the days of her life.",
      "T": "The orientation of her whole life is his good. Not passively, not only when convenient, but as the consistent direction she is pointed. The days accumulate into a life, and the net effect of all those days is his flourishing."
    },
    "13": {
      "L": "She seeks wool and flax and works with willing hands.",
      "M": "She seeks out wool and flax and works willingly with her hands.",
      "T": "She is the one seeking — not waiting for materials to appear, but going out to source them. The willingness is internal. She works at this because she is the kind of person who wants to work well."
    },
    "14": {
      "L": "She is like merchant ships; she brings her food from afar.",
      "M": "She is like merchant ships; she brings her food from far away.",
      "T": "Merchant ships do not wait for goods to arrive at the dock — they sail out to find them. She has this same reach: she is not limited to what is near. She goes out into the wider market and brings back what her household needs."
    },
    "15": {
      "L": "She rises while it is yet night and provides food for her household and portions for her maidens.",
      "M": "She rises while it is still dark and gives food to her household and assigns tasks to her servant girls.",
      "T": "She is up before the house stirs, organizing what the day requires. The household does not run on its own — someone has to plan it, start it, set it in motion. She is that person. Her servants do not wait idle; her family does not go hungry."
    },
    "16": {
      "L": "She considers a field and buys it; with the fruit of her hands she plants a vineyard.",
      "M": "She evaluates a field and buys it; from her earnings she plants a vineyard.",
      "T": "She is not just managing the household — she is investing. She examines the field, makes a business judgment, completes the purchase, and then plants for the long term. The vineyard will not produce quickly. She is thinking across years."
    },
    "17": {
      "L": "She girds her loins with strength and makes her arms strong.",
      "M": "She girds herself with strength and makes her arms powerful.",
      "T": "Girding the loins is the posture of readiness — the ancient equivalent of rolling up your sleeves. She prepares herself for work; strength is something she actively puts on. In this poem, strength is always chosen, never just inherited."
    },
    "18": {
      "L": "She perceives that her merchandise is good; her lamp does not go out at night.",
      "M": "She sees that her trade is profitable; her lamp does not go out at night.",
      "T": "She pays attention to outcomes. She notices whether what she is doing is working, and she adjusts. And when the work runs long, she does not stop simply because the sun has gone down. The lamp stays lit."
    },
    "19": {
      "L": "She puts her hands to the distaff, and her hands grasp the spindle.",
      "M": "She reaches out her hands to the distaff, and her fingers hold the spindle.",
      "T": "No detail of household production is beneath her. The distaff and spindle are the tools of the textile industry — essential, unglamorous, and in her hands constantly. She is not managing from a distance; she is at the work herself."
    },
    "20": {
      "L": "She opens her hand to the poor and stretches out her hands to the needy.",
      "M": "She opens her hand to the poor and extends her hands to the needy.",
      "T": "The poem has described her business acumen, her planning, her industry — and then pivots here to charity. The same hands that hold the spindle, that plant vineyards, that earn and invest — those hands open toward the poor. Her generosity is funded by her productivity."
    },
    "21": {
      "L": "She is not afraid of snow for her household, for all her household are clothed in scarlet.",
      "M": "She has no fear of snow for her household, for all her household are clothed in warm garments.",
      "T": "Winter cannot surprise her — she has already prepared for it. Her household is clothed in scarlet, quality wool dyed at cost. The preparation that looked tedious during summer reveals itself, when snow comes, as love made concrete. Fear has no room where readiness already lives."
    },
    "22": {
      "L": "She makes herself coverings; her clothing is fine linen and purple.",
      "M": "She makes her own bed coverings; her clothing is fine linen and purple.",
      "T": "She clothes herself with what she makes. Fine linen and purple — both marks of quality. The woman who provides abundantly for others is not neglecting herself. She wears what she has produced, and it is good."
    },
    "23": {
      "L": "Her husband is known in the gates when he sits among the elders of the land.",
      "M": "Her husband is known in the gates where he sits among the elders of the land.",
      "T": "The gates of the city are where judicial and civic business is transacted. Her husband sits there in recognized standing, among the elders. Part of what makes that possible is what she has built at home. A man whose household is well-ordered can show up fully in public life."
    },
    "24": {
      "L": "She makes linen garments and sells them and delivers sashes to the merchant.",
      "M": "She makes linen garments and sells them and supplies sashes to the traders.",
      "T": "Her production is not only for household use — it reaches the market. She makes goods of sufficient quality that merchants buy them. She is a producer in the economic life of her community, not merely a consumer within it."
    },
    "25": {
      "L": "Strength and dignity are her clothing, and she laughs at the days to come.",
      "M": "Strength and honor are her clothing, and she faces the future with joy.",
      "T": "She is clothed in strength and dignity — not as a metaphor for success, but as the substance of her character. And she laughs at the future. Not naively, not because nothing could go wrong, but because her preparation is real and her character is solid. The coming days hold no terror for someone who has met each day with strength."
    },
    "26": {
      "L": "She opens her mouth with wisdom, and the law of kindness is on her tongue.",
      "M": "She opens her mouth with wisdom, and faithful instruction is on her tongue.",
      "T": "Her speech is as careful as her hands. When she opens her mouth, wisdom comes out — not anxious chatter, but genuine understanding. And the instruction she offers is shaped by hesed, by covenant loyalty. She does not simply teach; she teaches in a way that is fundamentally trustworthy and kind."
    },
    "27": {
      "L": "She looks well to the ways of her household and does not eat the bread of idleness.",
      "M": "She watches over the affairs of her household and does not eat the bread of idleness.",
      "T": "She oversees — she knows what is happening in her house, and her oversight is active, not remote. And she does not consume what her household produces without contributing to it. The bread of idleness is not on her table."
    },
    "28": {
      "L": "Her children rise up and call her blessed; her husband also, and he praises her.",
      "M": "Her children rise and call her blessed; her husband also praises her.",
      "T": "The people closest to her — the ones who cannot be deceived by reputation because they live with her every day — stand up and declare her blessed. Her husband, who has seen everything this poem describes, opens his mouth and praises her. The honor begins at home before it reaches the gates."
    },
    "29": {
      "L": "Many daughters have done virtuously, but you surpass them all.",
      "M": "Many women have done excellently, but you surpass them all.",
      "T": "This is the voice of husband or community speaking directly to her. Many women have shown strength and worth — chayil in its fullest sense. But she has exceeded them all. The superlative is not flattery; it is the honest conclusion of the poem."
    },
    "30": {
      "L": "Charm is deceitful and beauty is vain, but a woman who fears the LORD is to be praised.",
      "M": "Charm is deceptive and beauty is fleeting, but a woman who fears the LORD is to be praised.",
      "T": "The poem ends by naming its foundation. Charm: impressive, but it performs — appearance aimed at effect. Beauty: real, but temporary. What sustains all the strength, honor, and wisdom the poem has described is the fear of the LORD. Her competence is not the root; it is the fruit. This is what the whole of Proverbs has been moving toward."
    },
    "31": {
      "L": "Give her of the fruit of her hands, and let her own works praise her in the gates.",
      "M": "Give her the fruit of her hands, and let her works praise her in the gates.",
      "T": "Let her be honored with what her labor has produced. Let her not be invisible — let the gates, where honor is publicly transacted, be the place where her works speak for her. She does not need borrowed praise or someone else's testimony. Her own deeds are her vindication."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'proverbs')
        merge_tier(existing, PROVERBS, tier_key)
        save(tier_dir, 'proverbs', existing)
    print('Proverbs 31 written.')

if __name__ == '__main__':
    main()
