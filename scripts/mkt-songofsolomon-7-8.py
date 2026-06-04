"""
MKT Song of Solomon chapters 7–8 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-songofsolomon-7-8.py

Translation decisions:
- H160 (אַהֲבָה, ahavah): "love" (L/M) / "devoted love" or "covenant love" (T) — the word for
  willed, committed love; used in 8:6–7 for love that rivals death
- H8669 (תְּשׁוּקָה, teshugah): "desire" (L/M) / "longing" (T) — 7:10 echoes Gen 3:16 where
  the same word describes the woman's desire for her husband; the echo reverses the curse-dynamic
- H5081 (נָדִיב, nadib): "prince's daughter" (L) / "noble daughter" (M) / "daughter of nobility" (T)
  — refers to the Shulammite's bearing/dignity, not necessarily literal royalty
- H7585 (שְׁאוֹל, Sheol): rendered "Sheol" in L/M, "the grave's domain" in T — Hebrew underworld
- H7957/שַׁלְהֶבֶתְיָה (shalhevetyah): "most vehement flame" (L/M) / "Yah's own flame" (T)
  — the final word of 8:6 can be read as a superlative (KJV tradition) or as containing the divine
  name Yah (יָהּ), meaning "a flame of Yahweh"; many modern scholars and ESV margin favor "flame of
  Yah"; the T tier surfaces this theological dimension explicitly
- H7068 (קִנְאָה, qina): "jealousy" (L/M) / "fierce devotion" (T in 8:6) — in covenantal love
  contexts the word carries the sense of exclusive, burning commitment, not merely envy
- H7965 (שָׁלוֹם, shalom): "peace/favour" (L) / "peace" (M) / "shalom" (T at 8:10) — the
  multivalent Hebrew word is best left transliterated in T to preserve its fullness
- Speaker attribution 7:9b: Following majority critical tradition, the Beloved (woman) takes over
  mid-verse at "for my beloved, flowing smoothly" — acknowledged in L/M sentence structure; T makes
  the switch explicit
- No explicit H3068 (יהוה) in these chapters; the divine name element in 8:6 is the one possible
  reference — see H7957 note above
- Hebrew poetry: T tier preserves line breaks in the wasf praise-poem (7:1–9) and the climactic
  passage 8:6–7; elsewhere T uses prose with heightened register
- The wasf form (7:1–9): ascending body-praise poem from feet to head, a genre attested in ancient
  Near Eastern love poetry; T preserves the catalogue structure while giving each image its force
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

SONGOFSOLOMON = {
  "7": {
    "1": {
      "L": "How beautiful are your feet in sandals, O daughter of a prince! The curves of your thighs are like ornaments, the work of a craftsman's hands.",
      "M": "How beautiful are your feet in sandals, O noble daughter! Your graceful thighs are like jeweled ornaments, crafted by a skilled artisan.",
      "T": "What beauty adorns your feet in sandals, O daughter of nobility!\nThe sculpted curves of your thighs are like fine-wrought ornaments,\nfashioned by a master craftsman's hands."
    },
    "2": {
      "L": "Your navel is a rounded bowl that lacks not mixed wine; your belly is a heap of wheat encircled with lilies.",
      "M": "Your navel is like a rounded goblet that never lacks spiced wine; your belly is like a mound of wheat encircled with lilies.",
      "T": "Your navel — a bowl of rounded grace, ever filled with mingled wine;\nyour belly like a mound of wheat, ringed round about with lilies."
    },
    "3": {
      "L": "Your two breasts are like two fawns, twins of a gazelle.",
      "M": "Your two breasts are like two fawns, twins of a gazelle.",
      "T": "Your breasts are like a pair of young fawns —\ntwin offspring of a gazelle."
    },
    "4": {
      "L": "Your neck is as a tower of ivory; your eyes are like the pools of Heshbon by the gate of Bath-rabbim; your nose is as the tower of Lebanon looking toward Damascus.",
      "M": "Your neck is like a tower of ivory; your eyes are like the pools of Heshbon beside the gate of Bath-rabbim; your nose is like the tower of Lebanon that looks out toward Damascus.",
      "T": "Your neck — white as an ivory tower;\nyour eyes, still as the pools of Heshbon by the city gate of Bath-rabbim;\nyour nose, proud as the tower of Lebanon gazing out toward Damascus."
    },
    "5": {
      "L": "Your head upon you is like Carmel, and the flowing hair of your head is like purple; a king is held captive in the tresses.",
      "M": "Your head crowns you like Mount Carmel, and your flowing hair is like royal purple; a king is held captive in your tresses.",
      "T": "Your head rises upon you like Mount Carmel's crown;\nyour flowing locks shimmer like royal purple —\na king himself is ensnared in your tresses."
    },
    "6": {
      "L": "How beautiful and how pleasant are you, O love, among delights!",
      "M": "How beautiful you are and how pleasant, O love, in your delights!",
      "T": "How beautiful! How exquisite you are, my love — pure delight embodied."
    },
    "7": {
      "L": "This your stature is like a palm tree, and your breasts are like its clusters.",
      "M": "Your stature is like a palm tree, and your breasts are like its clusters of dates.",
      "T": "You stand tall as a palm tree,\nand your breasts like the full clusters of dates at its crown."
    },
    "8": {
      "L": "I said, 'I will climb the palm tree; I will lay hold of its boughs.' Let your breasts be now like clusters of the vine, and the fragrance of your breath like apples.",
      "M": "I said, 'I will climb the palm tree and take hold of its boughs.' May your breasts be like clusters of the vine, and the scent of your breath like apples.",
      "T": "I resolve to climb that palm tree and grasp its fruit-laden branches.\nLet your breasts be like clusters of the vine,\nand every breath you draw as sweet as apples."
    },
    "9": {
      "L": "And your palate like good wine, going smoothly for my beloved, flowing over the lips of those who sleep.",
      "M": "And your kisses like the best wine — flowing smoothly for my beloved, gliding gently over sleeping lips.",
      "T": "And your kisses — like the finest wine,\npouring smooth and sweet for my beloved,\ngliding past the lips of those at rest."
    },
    "10": {
      "L": "I am my beloved's, and his desire is toward me.",
      "M": "I am my beloved's, and his desire is for me.",
      "T": "I belong wholly to my beloved — and his longing is toward me alone."
    },
    "11": {
      "L": "Come, my beloved, let us go out into the field; let us lodge in the villages.",
      "M": "Come, my beloved, let us go out to the fields and spend the night in the villages.",
      "T": "Come away, my love — let us go out into the open fields\nand spend the night among the scattered villages."
    },
    "12": {
      "L": "Let us rise early to the vineyards; let us see if the vine has budded, if the blossom has opened, if the pomegranates are in bloom. There I will give you my love.",
      "M": "Let us rise early and go to the vineyards to see whether the vine has budded, whether the blossoms have opened, and whether the pomegranates are in bloom. There I will give you my love.",
      "T": "At dawn let us go to the vineyards —\nto see whether the vines have budded, whether their blossoms have opened,\nwhether the pomegranates have come into flower.\nThere, in that garden-place, I will give you my love."
    },
    "13": {
      "L": "The mandrakes give forth their scent, and at our doors are all choice fruits, new and old, which I have stored up for you, my beloved.",
      "M": "The mandrakes give forth their fragrance, and at our doors are all choice fruits, both new and old, which I have kept in store for you, my beloved.",
      "T": "The mandrakes breathe out their fragrance;\nall manner of choice fruit waits at our door —\nold vintages and new, every treasure I have laid in store for you, my love."
    }
  },
  "8": {
    "1": {
      "L": "Oh that you were like a brother to me, who nursed at my mother's breasts! If I found you outside I would kiss you, and none would despise me.",
      "M": "If only you were like a brother to me, one who nursed at my mother's breasts! If I found you in the street I would kiss you, and no one would look down on me.",
      "T": "I wish you were like a brother to me — nursed at my own mother's breast! Then if I found you in the open street I could kiss you freely, and no one would think less of me."
    },
    "2": {
      "L": "I would lead you and bring you into my mother's house; she would teach me. I would give you spiced wine to drink, the juice of my pomegranate.",
      "M": "I would lead you and bring you into my mother's house, where she would instruct me. I would give you spiced wine to drink, the nectar of my pomegranate.",
      "T": "I would take you by the hand and bring you into my mother's house — that place of learning and of love — and give you spiced wine to drink, the sweet-pressed juice of my own pomegranate."
    },
    "3": {
      "L": "His left hand is under my head, and his right hand embraces me.",
      "M": "His left hand is under my head, and his right hand embraces me.",
      "T": "His left hand cradles my head; his right arm wraps around me."
    },
    "4": {
      "L": "I adjure you, O daughters of Jerusalem: do not stir up or awaken love until it pleases.",
      "M": "I charge you, O daughters of Jerusalem: do not arouse or awaken love until it is ready.",
      "T": "I put you on oath, daughters of Jerusalem:\ndo not rouse love, do not stir it from its sleep —\nnot before it is ready, not before the time."
    },
    "5": {
      "L": "Who is this coming up from the wilderness, leaning upon her beloved? Under the apple tree I awakened you; there your mother was in labor with you; there she who bore you was in labor.",
      "M": "Who is this coming up from the wilderness, leaning on her beloved? Under the apple tree I awakened you; there your mother was in labor with you; there she who bore you labored in birth.",
      "T": "Who is this rising from the desert, leaning on the arm of her beloved?\nBeneath the apple tree I woke you —\non the very ground where your mother went into labor,\nwhere she who bore you first felt her birth-pangs."
    },
    "6": {
      "L": "Set me as a seal upon your heart, as a seal upon your arm; for love is strong as death, jealousy fierce as Sheol; its flashes are flashes of fire, a most vehement flame.",
      "M": "Set me as a seal upon your heart, as a seal upon your arm; for love is as strong as death, jealousy as fierce as Sheol; its flashes are flashes of fire, the most vehement flame.",
      "T": "Seal me upon your heart — seal me upon your arm —\nfor love is as relentless as death,\nand jealous devotion as fierce as Sheol's own grip.\nIts embers are fire's coals — a flame that is Yah's very breath,\nthe greatest of all flames."
    },
    "7": {
      "L": "Many waters cannot quench love, neither can floods drown it. If a man would give all the wealth of his house for love, it would be utterly despised.",
      "M": "Many waters cannot quench love, and rivers cannot drown it. If a man offered all the wealth of his house in exchange for love, he would be utterly despised.",
      "T": "No rush of many waters can quench love; no flood can drown it.\nShould a man offer his entire fortune for love,\nhe would only earn contempt."
    },
    "8": {
      "L": "We have a little sister, and she has no breasts. What shall we do for our sister on the day when she is spoken for?",
      "M": "We have a little sister, and she has no breasts as yet. What shall we do for our sister on the day when she is spoken for in marriage?",
      "T": "We have a younger sister — still a child, with no breasts yet to speak of. What will we do for her on the day she is sought in marriage?"
    },
    "9": {
      "L": "If she is a wall, we will build upon her a battlement of silver; but if she is a door, we will enclose her with boards of cedar.",
      "M": "If she is a wall, we will build on her a parapet of silver; but if she is a door, we will enclose her with panels of cedar.",
      "T": "If she proves steadfast as a wall, we will crown her with silver battlements; if she opens freely like a door, we will board her in with cedar planks."
    },
    "10": {
      "L": "I am a wall, and my breasts are like towers; then I was in his eyes as one who finds peace.",
      "M": "I am a wall, and my breasts are like towers; so I have become in his eyes as one who brings peace.",
      "T": "I am a wall, and my breasts are towers of strength — and in his eyes I am one who has found shalom."
    },
    "11": {
      "L": "Solomon had a vineyard at Baal-hamon; he gave the vineyard to keepers; each one was to bring for its fruit a thousand pieces of silver.",
      "M": "Solomon had a vineyard at Baal-hamon; he entrusted it to tenant keepers; each one was to bring a thousand pieces of silver for its fruit.",
      "T": "Solomon kept a great vineyard at Baal-hamon, leased to tenant farmers — each one owing a thousand silver pieces for the fruit of its harvest."
    },
    "12": {
      "L": "My own vineyard is before me; the thousand is for you, O Solomon, and two hundred for those who tend its fruit.",
      "M": "My very own vineyard is my own; the thousand is yours, O Solomon, and two hundred for those who tend its fruit.",
      "T": "But my vineyard — mine alone — is entirely my own.\nKeep your thousand pieces, Solomon;\nlet two hundred go to the keepers of the vines.\nMy love is not for sale."
    },
    "13": {
      "L": "O you who dwell in the gardens, companions are listening for your voice; let me hear it.",
      "M": "O you who dwell in the gardens, while companions are listening for your voice, let me hear you.",
      "T": "You who dwell among the gardens —\nyour companions strain to hear your voice.\nLet me hear it."
    },
    "14": {
      "L": "Make haste, my beloved, and be like a gazelle or a young stag upon the mountains of spices.",
      "M": "Make haste, my beloved, and be like a gazelle or a young stag upon the mountains of spices.",
      "T": "Come swiftly, my love!\nLeap like a gazelle — like a young stag bounding\nover mountains heavy with spice."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'songofsolomon')
        merge_tier(existing, SONGOFSOLOMON, tier_key)
        save(tier_dir, 'songofsolomon', existing)
    print('Song of Solomon 7–8 written.')

if __name__ == '__main__':
    main()
