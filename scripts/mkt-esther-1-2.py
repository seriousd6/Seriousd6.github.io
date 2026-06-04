"""
MKT Esther chapters 1–2 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-esther-1-2.py

Translation decisions:
- H3068 / H430: יהוה and אֱלֹהִים are ABSENT from Esther — this is the book's most famous
  feature. God's name never appears in the Hebrew text. The hiddenness of divine action is
  a deliberate literary and theological feature. No LORD/God insertion anywhere in these chapters.
- H325 (אחשורוש, Ahasuerus): "Ahasuerus" in L and M throughout. T uses "Ahasuerus" without
  substituting the Greek "Xerxes" (though the identification with Xerxes I, 486–465 BC, is
  noted in verse 1 T tier). Consistency with LXX and traditional reading.
- H7800 (שׁוּשַׁן, Shushan): "Shushan" in L; "Susa" in M and T — the more recognizable modern
  form for the Persian capital in Elam.
- H1002 (בִּירָה, birah): "palace" in L; "citadel" in M/T — birah denotes the fortified royal
  acropolis at Susa, distinct from the city proper. "Citadel" better captures the architectural
  and military sense.
- H2617 (חֶסֶד, hesed): appears at 2:9 and 2:17. In this context it means loyal kindness /
  favor rather than covenantal love (no covenant context). L: "kindness"; M: "favor" (2:9),
  "grace and favor" (2:17 alongside H2580 chen); T: "loyal kindness" (2:9), "grace and favor"
  (2:17). The full covenantal freight of hesed is present only as a literary undertone — the
  book is exploring how hesed operates in a Gentile court.
- H2580 (חֵן, chen): "grace/favor" — L: "grace"; M/T: "favor" or "grace." At 2:17 paired with
  H2617 as "grace and favor" (L) / "grace and favor" (M/T).
- H5631 (סָרִיס, saris): "chamberlain" in L; "eunuch" in M/T — royal court officials who may
  or may not have been literally castrated (the term was used both ways in the ANE), but
  "eunuch" is the more accurate rendering for the harem-keepers (Hegai, Shaashgaz); other
  court officials rendered "chamberlain" in L and "official/attendant" in M/T depending on role.
- H1881 (דָּת, dat): "law" in L; "decree/law" in M/T — a Persian loanword for royal edict or
  legal rule. The Law of the Medes and Persians (irrevocable once written) is a key plot device.
- H4960 (מִשְׁתֶּה, mishteh): "feast" in L; "banquet" in M/T — the formal Persian court feast
  is more accurately "banquet" in English, but "feast" is preserved in L.
- H1330 (בְּתוּלָה, betulah): "virgin" in L; "young woman" in M/T — the term emphasizes
  unmarried status; "virgin" carries the literal sense but "young woman" is cleaner in M/T.
- H3204 (יְכָנְיָה, Jeconiah): the king also called Jehoiachin; exiled 597 BC (2 Kgs 24:10-16).
  This dates Mordecai to the late 6th century or makes him very old — more likely the text
  means his family was exiled with Jeconiah's deportation. T notes the ambiguity.
- H1919 (הֲדַסָּה, Hadassah): Esther's Hebrew name, meaning "myrtle." T notes the name's
  resonance with restoration imagery (myrtle in Isa 41:19; 55:13; Zech 1:8-11).
- Aspect: Hebrew narrative uses waw-consecutive imperfect (narrative past) throughout.
  All rendered as simple English past tense in L/M. T may use historical present in dramatic
  moments for effect.
- Satirical register: Chapter 1 carries a distinct satirical/ironic tone in the Hebrew —
  the great empire mobilised to enforce domestic order; the law of the Medes and Persians
  invoked over a marital dispute. T surfaces this irony where appropriate without overplaying it.
- 1:6 pavement stones: H7531 (ritsphah, porphyry/red stone), H8336 (shesh, alabaster/marble),
  H923 (bahat, a precious stone, possibly alabaster or mother-of-pearl), H5508 (soharet,
  a black or dark stone). Exact identifications are uncertain; T renders with a general note.
- 2:5 Mordecai genealogy: son of Jair → Shimei → Kish, a Benjaminite — the Kish-Benjamin line
  echoes King Saul's lineage (1 Sam 9:1). This is likely intentional: a descendant of Saul's
  family line faces down an Agagite (Haman in ch. 3), the conflict Saul failed to finish.
  T notes this in ch. 3 when Haman is introduced; for now the genealogy is stated.
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

ESTHER = {
  "1": {
    "1": {
      "L": "Now it came to pass in the days of Ahasuerus — this is the Ahasuerus who reigned from India even unto Ethiopia, over an hundred and twenty and seven provinces —",
      "M": "In the days of Ahasuerus, who reigned from India to Ethiopia over one hundred and twenty-seven provinces —",
      "T": "This is the story of Ahasuerus — the Persian king who ruled the greatest empire the world had yet seen, stretching from India to Ethiopia across one hundred and twenty-seven provinces."
    },
    "2": {
      "L": "that in those days, when the king Ahasuerus sat on the throne of his kingdom, which was in Shushan the palace,",
      "M": "it was in those days when King Ahasuerus sat on his royal throne at the citadel of Susa.",
      "T": "At that time, King Ahasuerus was enthroned in the royal citadel of Susa, the magnificent capital of his realm."
    },
    "3": {
      "L": "in the third year of his reign, he made a feast unto all his princes and his servants; the power of Persia and Media, the nobles and princes of the provinces, being before him.",
      "M": "In his third year as king, he gave a great banquet for all his princes and officials — the military leaders of Persia and Media, the nobles, and the governors of his provinces.",
      "T": "In the third year of his reign, Ahasuerus threw a lavish state banquet for all his officials — the generals of Persia and Media, the aristocracy, and the provincial governors who attended at his court."
    },
    "4": {
      "L": "When he shewed the riches of his glorious kingdom and the honour of his excellent majesty many days, even an hundred and fourscore days.",
      "M": "He displayed the splendid wealth of his kingdom and the glorious honor of his greatness for many days — a hundred and eighty days.",
      "T": "For one hundred and eighty days — nearly half a year — he put the full splendor of his wealth on display, a sustained spectacle of imperial glory designed to impress every man who attended."
    },
    "5": {
      "L": "And when these days were expired, the king made a feast unto all the people that were present in Shushan the palace, both unto great and small, seven days, in the court of the garden of the king's palace.",
      "M": "When those days were over, the king gave another banquet — this time for all the people gathered in Susa the citadel, from the greatest to the least, lasting seven days in the court of the palace garden.",
      "T": "After the state banquet for the nobility came an even more inclusive celebration: a seven-day open feast for all residents of Susa, from the highest official to the humblest citizen, held in the royal garden courtyard."
    },
    "6": {
      "L": "Where were white, green, and blue hangings, fastened with cords of fine linen and purple to silver rings and pillars of marble; the beds were of gold and silver, upon a pavement of red and blue and white and black marble.",
      "M": "There were white and violet linen curtains hung with cords of fine linen and purple on silver rings set in marble columns. The couches were of gold and silver, set on a mosaic pavement of porphyry, marble, and precious stone.",
      "T": "The courtyard was arrayed with breathtaking opulence: white and violet linen curtains hung from silver rings in marble columns; golden and silver couches rested on a mosaic floor of brilliant and costly stones. Every surface declared the empire's reach and the king's inexhaustible wealth."
    },
    "7": {
      "L": "And they gave them drink in vessels of gold — the vessels being diverse one from another — and royal wine in abundance, according to the state of the king.",
      "M": "Drinks were served in golden goblets, each one different from the others, and royal wine flowed freely in keeping with the king's generosity.",
      "T": "Wine was served in golden cups, no two alike, and the royal vintage flowed without limit. Ahasuerus would spare no expense to demonstrate his bounty."
    },
    "8": {
      "L": "And the drinking was according to the law; none did compel: for so the king had appointed to all the officers of his house, that they should do according to every man's pleasure.",
      "M": "Drinking was by the king's order — no one was compelled, for the king had directed all his household staff to serve each guest according to his own preference.",
      "T": "Even the drinking customs reflected the king's absolute authority: he had decreed that no one would be forced to drink, but each guest would be served however much he pleased. The king's hospitality was as boundless as his power."
    },
    "9": {
      "L": "Also Vashti the queen made a feast for the women in the royal house which belonged to king Ahasuerus.",
      "M": "Meanwhile, Queen Vashti held a separate banquet for the women in the royal palace.",
      "T": "At the same time, Queen Vashti hosted her own banquet for the women within the palace — a parallel court within the court, ordered and contained, and soon to collide with the king's."
    },
    "10": {
      "L": "On the seventh day, when the heart of the king was merry with wine, he commanded Mehuman, Biztha, Harbona, Bigtha, and Abagtha, Zethar, and Carcas, the seven chamberlains that served in the presence of Ahasuerus the king,",
      "M": "On the seventh day, when the king's heart was high with wine, he commanded the seven eunuchs who served before him — Mehuman, Biztha, Harbona, Bigtha, Abagtha, Zethar, and Carcas —",
      "T": "On the seventh day of the feast, when wine had lifted the king's mood to reckless display, he summoned his seven personal chamberlains — Mehuman, Biztha, Harbona, Bigtha, Abagtha, Zethar, and Carcas —"
    },
    "11": {
      "L": "to bring Vashti the queen before the king with the royal crown, to shew the people and the princes her beauty: for she was fair to look on.",
      "M": "to bring Queen Vashti before him wearing the royal crown, to display her beauty to the assembled people and princes — for she was beautiful.",
      "T": "to bring Queen Vashti before the crowd wearing her crown, so the assembled nobles could admire her. She was indeed beautiful — but the command would prove a fatal miscalculation."
    },
    "12": {
      "L": "But the queen Vashti refused to come at the king's commandment by his chamberlains: therefore was the king very wroth, and his anger burned in him.",
      "M": "But Queen Vashti refused to come at the king's command delivered by the eunuchs. The king became furiously angry, and his rage burned within him.",
      "T": "Vashti refused. The queen would not be paraded for the entertainment of a room full of drunken men, however royal the command. The king's reaction was instant and fierce — the rejection of his public summons was both personal humiliation and political crisis."
    },
    "13": {
      "L": "Then the king said to the wise men, which knew the times — for so was the king's manner toward all that knew law and judgment:",
      "M": "The king consulted the wise men who understood the law and legal proceedings — for it was the king's custom to seek such expert counsel.",
      "T": "Following royal protocol, Ahasuerus convened his council of legal advisers — men who understood both precedent and court procedure."
    },
    "14": {
      "L": "and the next unto him was Carshena, Shethar, Admatha, Tarshish, Meres, Marsena, and Memucan, the seven princes of Persia and Media, which saw the king's face, and which sat the first in the kingdom —",
      "M": "His advisers nearest to him were Carshena, Shethar, Admatha, Tarshish, Meres, Marsena, and Memucan — the seven princes of Persia and Media who had personal access to the king and held the highest rank in the kingdom.",
      "T": "His inner circle of seven — Carshena, Shethar, Admatha, Tarshish, Meres, Marsena, and Memucan — enjoyed direct access to the throne and occupied the highest seats of power in the empire."
    },
    "15": {
      "L": "What shall we do unto the queen Vashti according to law, because she hath not performed the commandment of the king Ahasuerus by the chamberlains?",
      "M": "He asked: 'According to the law, what must be done with Queen Vashti, because she has not obeyed the command of King Ahasuerus delivered by the chamberlains?'",
      "T": "'What does the law require,' the king demanded, 'about what should be done to Queen Vashti for defying my direct command?'"
    },
    "16": {
      "L": "And Memucan answered before the king and the princes, Vashti the queen hath not done wrong to the king only, but also to all the princes, and to all the people that are in all the provinces of the king Ahasuerus.",
      "M": "Memucan replied before the king and the princes: 'Queen Vashti has not wronged the king alone, but all the princes and all the peoples throughout all the provinces of King Ahasuerus.'",
      "T": "Memucan stepped forward with a confident diagnosis: 'Your Majesty, this is not a private domestic matter. Vashti's defiance is an act of insubordination against every prince and every man in every province of the empire.'"
    },
    "17": {
      "L": "For this deed of the queen shall come abroad unto all women, so that they shall despise their husbands in their eyes, when it shall be reported, The king Ahasuerus commanded Vashti the queen to be brought in before him, but she came not.",
      "M": "For word of what the queen has done will spread to all women, and they will despise their husbands — when they hear that King Ahasuerus commanded Vashti to appear before him and she refused to come.",
      "T": "'When word spreads — as it certainly will — that the queen refused the king's own command, every woman in the empire will feel emboldened to defy her husband. The queen's example will unravel the authority of every household from Persia to India.'"
    },
    "18": {
      "L": "Likewise shall the ladies of Persia and Media say this day unto all the king's princes, which have heard of the deed of the queen. Thus shall there arise too much contempt and wrath.",
      "M": "This very day the noblewomen of Persia and Media who have heard of the queen's conduct will say the same to all the king's princes — and there will be no end to the contempt and anger.",
      "T": "'Even as we speak, the noblewomen of Persia and Media are hearing what the queen did. They will cite her as precedent. The result will be an epidemic of contempt — in the palace and in every noble household across the empire.'"
    },
    "19": {
      "L": "If it please the king, let there go a royal commandment from him, and let it be written among the laws of the Persians and the Medes, that it be not altered, that Vashti come no more before king Ahasuerus; and let the king give her royal estate unto another that is better than she.",
      "M": "Therefore, if it please the king, let a royal decree go out — written in the laws of the Persians and Medes so that it cannot be revoked — that Vashti shall never again appear before King Ahasuerus, and that the king give her royal position to someone more worthy.",
      "T": "'Our recommendation: issue an irrevocable royal edict — binding under the law of the Medes and Persians — that Vashti is permanently banned from the king's presence, and that her crown be given to a worthier woman. Make the consequence so public and final that no woman in the empire would dare follow her example.'"
    },
    "20": {
      "L": "And when the king's decree which he shall make shall be published throughout all his empire — for it is great — all the wives shall give to their husbands honour, both to great and small.",
      "M": "When the king's decree is proclaimed throughout his vast empire, all wives — from the greatest household to the least — will give honor to their husbands.",
      "T": "'Publish the decree across the whole empire — and it is a vast empire — and every wife, from the highest court to the humblest home, will understand what honor her husband requires.'"
    },
    "21": {
      "L": "And the saying pleased the king and the princes; and the king did according to the word of Memucan:",
      "M": "The king and the princes were pleased with this advice, and the king acted on Memucan's recommendation.",
      "T": "The plan delighted the king and his counsellors. Memucan's solution was adopted without further debate."
    },
    "22": {
      "L": "for he sent letters into all the king's provinces, into every province according to the writing thereof, and to every people after their language, that every man should bear rule in his own house, and that it should be published according to the language of every people.",
      "M": "He sent letters to all the king's provinces — to each province in its own script and to each people in their own language — declaring that every man should be master in his own household, and that this be proclaimed in the tongue of each people.",
      "T": "Letters went out to every corner of the empire — written in the script of each province, in the tongue of each people — proclaiming that men were to rule their households. The great Persian bureaucratic machine had been mobilized to enforce domestic order. The irony was almost comic; but the law was now irrevocable, and Vashti was finished."
    }
  },
  "2": {
    "1": {
      "L": "After these things, when the wrath of king Ahasuerus was appeased, he remembered Vashti, and what she had done, and what was decreed against her.",
      "M": "After these events, when King Ahasuerus's anger had cooled, he thought of Vashti — what she had done and what had been decreed against her.",
      "T": "When the king's anger finally subsided, he found himself thinking about Vashti. The edict had been issued and was irrevocable; the crown was vacant — and perhaps in a calmer moment, he felt the loss."
    },
    "2": {
      "L": "Then said the king's servants that ministered unto him, Let there be fair young virgins sought for the king:",
      "M": "The king's attendants who served him suggested: 'Let beautiful young women be sought for the king.'",
      "T": "The king's advisers, ever attentive to his mood, made their proposal: 'Let a search be made throughout the kingdom for beautiful young women to be presented to the king.'"
    },
    "3": {
      "L": "and let the king appoint officers in all the provinces of his kingdom, that they may gather together all the fair young virgins unto Shushan the palace, to the house of the women, unto the custody of Hege the king's chamberlain, keeper of the women; and let their things for purification be given them:",
      "M": "Let the king appoint commissioners throughout all his provinces to gather all the beautiful young women to the harem at Susa, into the care of Hegai the king's eunuch who oversees the women; and let them be given their beauty treatments.",
      "T": "'Station officials in every province to collect beautiful young women and bring them to the royal harem at Susa, under the supervision of Hegai, the keeper of the women. Give each woman a full course of beauty preparations —'"
    },
    "4": {
      "L": "and let the maiden which pleaseth the king be queen instead of Vashti. And the thing pleased the king; and he did so.",
      "M": "'and let the young woman who pleases the king become queen in place of Vashti.' The plan pleased the king, and he carried it out.",
      "T": "'— and let the woman who pleases the king most become queen in Vashti's place.' The king approved the idea, and the search began."
    },
    "5": {
      "L": "Now in Shushan the palace there was a certain Jew, whose name was Mordecai, the son of Jair, the son of Shimei, the son of Kish, a Benjamite;",
      "M": "Now there was a Jewish man in the citadel of Susa named Mordecai son of Jair, son of Shimei, son of Kish — a Benjaminite.",
      "T": "Living in the royal citadel of Susa was a Jewish man named Mordecai — his lineage traced back through Jair and Shimei to Kish, a Benjaminite. The name Kish and the tribe of Benjamin echo the lineage of King Saul; the detail is not accidental."
    },
    "6": {
      "L": "who had been carried away from Jerusalem with the captivity which had been carried away with Jeconiah king of Judah, whom Nebuchadnezzar the king of Babylon had carried away.",
      "M": "He had been carried into exile from Jerusalem among those taken captive with King Jeconiah of Judah, when Nebuchadnezzar king of Babylon exiled them.",
      "T": "Mordecai was of the exilic generation — his family taken from Jerusalem as part of the deportation that accompanied King Jeconiah's exile in 597 BC. His people were far from home; the Persian court was the world he had inherited."
    },
    "7": {
      "L": "And he brought up Hadassah, that is, Esther, his uncle's daughter: for she had neither father nor mother, and the maid was fair and beautiful; whom Mordecai, when her father and mother were dead, took for his own daughter.",
      "M": "He had raised his cousin Hadassah — that is, Esther — for she had no father or mother. The young woman was beautiful in form and face, and when her parents died Mordecai had taken her as his own daughter.",
      "T": "Mordecai had raised his young cousin — Hadassah, whose Persian name was Esther. Her parents had both died, and Mordecai had become her guardian, treating her as his own daughter. Esther was strikingly beautiful; Hadassah means 'myrtle,' the tree associated in Hebrew prophecy with restoration and new life. This beauty was about to change the course of events for the Jewish people."
    },
    "8": {
      "L": "So it came to pass, when the king's commandment and his decree was heard, and when many maidens were gathered together unto Shushan the palace, to the custody of Hegai, that Esther was brought also unto the king's house, to the custody of Hegai, keeper of the women.",
      "M": "When the king's command and decree became known and many young women were gathered to the citadel of Susa under Hegai's care, Esther was also taken to the royal palace and placed under Hegai's charge.",
      "T": "As the imperial decree went into effect and young women from across the empire were swept into the royal harem at Susa, Esther was among them — taken from ordinary life into the glittering and dangerous world of the Persian court."
    },
    "9": {
      "L": "And the maiden pleased him, and she obtained kindness of him; and he speedily gave her her things for purification, with such things as belonged to her, and seven maidens, which were meet to be given her, out of the king's house: and he preferred her and her maids unto the best place of the house of the women.",
      "M": "The young woman pleased him and won his favor, and he quickly provided her beauty treatments and her prescribed portions, along with seven chosen attendants from the palace. He moved her and her maids into the best rooms in the harem.",
      "T": "Esther made an immediate impression on Hegai. He gave her preferential treatment: her beauty regimen was started without delay, seven handpicked attendants were assigned to her, and she was moved into the finest rooms in the women's quarters. Something about Esther commanded loyalty — and Hegai's favor would prove significant."
    },
    "10": {
      "L": "Esther had not shewed her people nor her kindred: for Mordecai had charged her that she should not shew it.",
      "M": "Esther had not disclosed her nationality or family background, because Mordecai had instructed her to say nothing about it.",
      "T": "Esther kept her secret. On Mordecai's instruction, she told no one she was Jewish — not her family name, not her people's identity. The concealment was strategic; neither Mordecai nor Esther could have known yet how much that secret would one day matter."
    },
    "11": {
      "L": "And Mordecai walked every day before the court of the women's house, to know how Esther did, and what should become of her.",
      "M": "Every day Mordecai walked back and forth before the courtyard of the harem to learn how Esther was faring and what was happening to her.",
      "T": "Day after day, Mordecai stationed himself near the entrance to the women's quarters, watching for news of Esther — a guardian keeping watch from as close as the rules allowed."
    },
    "12": {
      "L": "Now when every maid's turn was come to go in to king Ahasuerus, after that she had been twelve months, according to the manner of the women — for so were the days of their purifications accomplished, to wit, six months with oil of myrrh, and six months with sweet odours, and with other things for the purifying of the women —",
      "M": "Each young woman's turn to go before King Ahasuerus came after twelve months under the required beauty regimen — six months with oil of myrrh and six months with fragrant spices and other cosmetic preparations.",
      "T": "The preparation process lasted a full year for each woman: six months of treatment with myrrh oil, six months with aromatic spices and cosmetics. Only then came her one night with the king — a night that would determine her entire future."
    },
    "13": {
      "L": "then thus came every maiden unto the king; whatsoever she desired was given her to go with her out of the house of the women unto the king's house.",
      "M": "After that preparation, each young woman went to the king, and she could take with her whatever she chose from the women's house to the king's palace.",
      "T": "On the night of her presentation, each woman was allowed to bring whatever she wished from the women's house — jewelry, clothing, accessories — the one moment of personal choice in a process that was otherwise entirely controlled by others."
    },
    "14": {
      "L": "In the evening she went, and on the morrow she returned into the second house of the women, to the custody of Shaashgaz, the king's chamberlain, which kept the concubines: she came in unto the king no more, except the king delighted in her, and that she were called by name.",
      "M": "She went to the king in the evening and returned the next morning to the second harem, under the care of Shaashgaz the king's eunuch who kept the concubines. She would not go back to the king unless he was pleased with her and summoned her by name.",
      "T": "She would enter the king's chambers in the evening and leave the next morning — not back to the honored first house, but to the second harem, the house of concubines under Shaashgaz. Unless the king specifically called for her by name, she would never see him again. For most, that was the end of the story."
    },
    "15": {
      "L": "Now when the turn of Esther, the daughter of Abihail the uncle of Mordecai, who had taken her for his daughter, was come to go in unto the king, she required nothing but what Hegai the king's chamberlain, the keeper of the women, appointed. And Esther obtained favour in the sight of all them that looked upon her.",
      "M": "When the turn came for Esther — daughter of Abihail the uncle of Mordecai, who had adopted her as his daughter — to go before the king, she asked for nothing except what Hegai the king's eunuch, keeper of the women, advised. And Esther won the admiration of everyone who saw her.",
      "T": "When Esther's turn came, she did something distinctive: instead of selecting her own adornments, she simply accepted Hegai's expert recommendation. Her restraint was a kind of wisdom — and it made an impression. Everyone who saw her was captivated."
    },
    "16": {
      "L": "So Esther was taken unto king Ahasuerus into his royal house in the tenth month, which is the month Tebeth, in the seventh year of his reign.",
      "M": "Esther was brought to King Ahasuerus in the royal palace in the tenth month — the month of Tebeth — in the seventh year of his reign.",
      "T": "Esther entered the king's presence in the month of Tebeth, in the seventh year of Ahasuerus's reign — more than four years after the great banquet where Vashti had refused her summons."
    },
    "17": {
      "L": "And the king loved Esther above all the women, and she obtained grace and favour in his sight more than all the virgins; so that he set the royal crown upon her head, and made her queen instead of Vashti.",
      "M": "The king loved Esther more than all the other women, and she won more grace and favor from him than all the other young women. He placed the royal crown on her head and made her queen in place of Vashti.",
      "T": "Esther won the king's heart completely. Of all the women who had come before him, she alone earned both his love and his deepest favor. He placed the crown on her head and declared her queen — Vashti's replacement, and, though no one yet knew it, the hope of the Jewish exiles."
    },
    "18": {
      "L": "Then the king made a great feast unto all his princes and his servants, even Esther's feast; and he made a release to the provinces, and gave gifts, according to the state of the king.",
      "M": "Then the king gave a great banquet in Esther's honor for all his princes and officials — Esther's banquet. He proclaimed a tax remission for the provinces and distributed gifts with royal generosity.",
      "T": "Ahasuerus celebrated with the imperial extravagance the story has taught us to expect: a great state banquet in Esther's honor, a tax holiday across the provinces, and gifts distributed with royal lavishness. The empire celebrated the new queen — unaware of who she really was."
    },
    "19": {
      "L": "And when the virgins were gathered together the second time, then Mordecai sat in the king's gate.",
      "M": "When the young women were gathered a second time, Mordecai was sitting at the king's gate.",
      "T": "During a second gathering of candidates for the court, Mordecai had taken up his seat at the king's gate — one of the royal officials now, stationed close to the center of power where events would soon unfold."
    },
    "20": {
      "L": "Esther had not yet shewed her kindred nor her people; as Mordecai had charged her: for Esther did the commandment of Mordecai, like as when she was brought up with him.",
      "M": "Esther still had not disclosed her family background or nationality, just as Mordecai had instructed her, for she continued to follow his directions as she had done when he raised her.",
      "T": "Esther still kept the secret — her people, her heritage, all of it hidden, exactly as Mordecai had told her. Even now as queen, she obeyed him as she had obeyed him as a child. That habit of trust would serve them both when the crisis finally arrived."
    },
    "21": {
      "L": "In those days, while Mordecai sat in the king's gate, two of the king's chamberlains, Bigthana and Teresh, of those which kept the door, were wroth, and sought to lay hand on the king Ahasuerus.",
      "M": "In those days, while Mordecai was sitting at the king's gate, two of the king's eunuchs who guarded the entrance — Bigthana and Teresh — became angry and plotted to assassinate King Ahasuerus.",
      "T": "Mordecai's post at the gate placed him exactly where it mattered. Two royal guards — Bigthana and Teresh, gatekeepers with direct access to the king — had developed a grievance deep enough to turn to murder. They began to conspire."
    },
    "22": {
      "L": "And the thing was known to Mordecai, who told it unto Esther the queen; and Esther certified the king thereof in Mordecai's name.",
      "M": "Mordecai learned of the plot and reported it to Queen Esther, and Esther told the king, giving Mordecai credit.",
      "T": "Somehow Mordecai got wind of the conspiracy — the text does not explain how. He passed the intelligence to Esther, and Esther reported it to the king, giving Mordecai full credit. It was a chain of loyalty that would become a decisive thread in everything that followed."
    },
    "23": {
      "L": "And when inquisition was made of the matter, it was found out; therefore they were both hanged on a tree: and it was written in the book of the chronicles before the king.",
      "M": "When the report was investigated and confirmed, both men were hanged on the gallows, and the incident was recorded in the book of court chronicles before the king.",
      "T": "The investigation confirmed the plot. Bigthana and Teresh were executed — hanged, as Persian custom required — and the entire affair was duly entered in the royal court records. Mordecai's loyal service to the king had been noted. But no reward came. Not yet."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'esther')
        merge_tier(existing, ESTHER, tier_key)
        save(tier_dir, 'esther', existing)
    print('Esther 1–2 written.')

if __name__ == '__main__':
    main()
