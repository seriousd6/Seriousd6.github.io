"""
MKT 1 Chronicles chapters 11-16 -- three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-1chronicles-11-16.py

Translation decisions:
- H3068 (yhwh): "LORD" in L/M throughout; "the LORD" in T. Consistent with mkt-1chronicles-1-5.
- H430 (elohim): "God" in all tiers.
- H1285 (berit): "covenant" in all tiers.
- H7307 (ruach): Ch 12:18 -- "the Spirit" capitalised in all tiers (divine agency clothing Amasai
  for prophetic speech; same idiom as Judg 6:34, 2 Chr 24:20). Contrast 5:26 where spirit of Pul
  = human political impulse, lowercase.
- H2617 (hesed): "steadfast love" in M/T (ch 16:34, 41). No English word captures covenant
  loyalty + active kindness; "steadfast love" is the closest available.
- H5769 (olam): "forever" / "everlasting" depending on syntactic role.
- H727 (aron): "ark" throughout.
- H3519 (kavod): "glory" in ch 16 psalm.
- H5797 (oz): "strength" in ch 16 psalm.
- H6944 (qodesh): "holy" / "holiness" by syntactic role.
- H5315 (nephesh): 11:19 -- tokens read "jeopardy of their lives"; L/M render "lives"; T renders
  "lifeblood" to surface the embodied-self valence of nephesh.
- H8416 (tehillah): "praise" throughout.
- H441 (allup): "chief" not "duke" -- consistent with prior script.

Textual notes:
- 11:6: Joab becomes chief by going up first against Jebus; Chronicles omits the water-shaft
  detail of 2 Sam 5:8. The Chronicler's streamlined account is followed.
- 11:11: "Three hundred" slain by Jashobeam; 2 Sam 23:8 has "eight hundred." Chronicles' number kept.
- 11:20-21: Abishai is "more honoured than the three" yet "did not attain to the three" -- a tension
  in the source; retained without harmonising.
- 12:18: "The Spirit clothed Amasai" (wayyilbash ha-ruach) -- Spirit as garment, surrounding for
  a moment of revelation. T tier foregrounds the theology.
- 13:9: "Chidon" in Chronicles vs. "Nacon" in 2 Sam 6:6 -- variant name for the threshing floor;
  Chronicles' form retained.
- 15:27: David wears a linen ephod (not the full high-priestly garment) and a linen robe; Chenaniah
  is "master of the song." Rendered as "song-master" in T.
- 16:8-36: Compiled psalm -- vv.8-22 = Ps 105:1-15; vv.23-33 = Ps 96:1-13;
  vv.34-36 = Ps 106:1, 47-48. T tier uses line breaks to honour the poetic structure.

Hebrew aspect: Waw-consecutive imperfects throughout = simple narrative past in English.
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

CHRONICLES1 = {
  "11": {
    "1": {
      "L": "Then all Israel gathered themselves to David at Hebron, saying, Behold, we are your bone and your flesh.",
      "M": "Then all Israel gathered to David at Hebron and said, 'Behold, we are your bone and your flesh.'",
      "T": "All Israel converged on Hebron to say what was already true in blood: 'We are your bone and your flesh.' The bond they name is the bond of family -- not political calculation but kinship. David had been doing the work of king for years; now his own people came to name him as theirs."
    },
    "2": {
      "L": "And moreover in time past, even when Saul was king, you were the one who led out and brought in Israel; and the LORD your God said to you, You shall shepherd my people Israel, and you shall be ruler over my people Israel.",
      "M": "Even in the past, when Saul was king, it was you who led out and brought in Israel. And the LORD your God said to you, 'You shall shepherd my people Israel, and you shall be ruler over my people Israel.'",
      "T": "They name the open secret: even under Saul, David was the one leading Israel's armies out and home. And the LORD had said it first -- 'You shall shepherd my people Israel.' The language of shepherd is constitutional, not decorative. The king is shepherd: he moves the flock to pasture, guards it from predators, lays down his life for the sheep. David had been doing it already."
    },
    "3": {
      "L": "Therefore came all the elders of Israel to the king at Hebron; and David made a covenant with them at Hebron before the LORD; and they anointed David king over Israel, according to the word of the LORD through Samuel.",
      "M": "So all the elders of Israel came to the king at Hebron, and David made a covenant with them at Hebron before the LORD. They anointed David king over Israel, according to the word of the LORD through Samuel.",
      "T": "The elders made a covenant with David -- the formal, oath-bound compact binding king and people together before the LORD. And they anointed him: the third anointing. First Samuel had anointed him privately in his father's house; then Judah alone had crowned him; now all Israel united in this act. The word spoken through Samuel was being fulfilled."
    },
    "4": {
      "L": "And David and all Israel went to Jerusalem, that is Jebus, where the Jebusites were, the inhabitants of the land.",
      "M": "Then David and all Israel marched to Jerusalem, that is, Jebus, where the Jebusites, the inhabitants of the land, were living.",
      "T": "The first act of the united kingdom: march on Jerusalem. The city had been Jebusite since the conquest -- Israelite territory on the map but Jebusite in fact. That would end now."
    },
    "5": {
      "L": "And the inhabitants of Jebus said to David, You shall not come in here. Nevertheless David took the stronghold of Zion, which is the city of David.",
      "M": "The inhabitants of Jebus said to David, 'You shall not come in here.' But David captured the stronghold of Zion, which became the city of David.",
      "T": "The Jebusites jeered: 'You shall not come in here.' Their confidence was misplaced. David took the stronghold of Zion -- the high fortified ridge above the Kidron -- and made it his own. From this moment, the city has two names: Zion, and the city of David."
    },
    "6": {
      "L": "And David said, Whoever first strikes the Jebusites shall be chief and captain. And Joab the son of Zeruiah went up first, and was made chief.",
      "M": "David had said, 'Whoever strikes the Jebusites first shall be chief and captain.' Joab son of Zeruiah went up first, and so became chief.",
      "T": "David made it a contest: whoever goes first becomes commander. It was a dangerous promise, and Joab seized it. He led the assault, took the prize, and cemented his position as David's general -- a relationship that would prove lifelong, complicated, and ultimately irreplaceable."
    },
    "7": {
      "L": "And David lived in the stronghold; therefore they called it the city of David.",
      "M": "David took up residence in the stronghold, and so they called it the city of David.",
      "T": "David settled in the stronghold he had taken. The city takes his name -- not as vanity but as covenant: the place is now bound to the man, and the man to the promise."
    },
    "8": {
      "L": "And he built the city around it from the Millo even round about; and Joab repaired the rest of the city.",
      "M": "He built the city around it from the Millo to the surrounding area, and Joab repaired the rest of the city.",
      "T": "David extended and fortified Jerusalem from the Millo -- the stepped stone fill-terrace at the city's heart -- outward in every direction. Joab, now chief commander, rebuilt the quarters his assault had damaged. The king builds; his general repairs. Conquest becomes city."
    },
    "9": {
      "L": "And David waxed greater and greater, for the LORD of hosts was with him.",
      "M": "David grew greater and greater, for the LORD of hosts was with him.",
      "T": "The formula the Chronicler uses for God's blessing: 'David grew greater and greater' -- each step of expansion, each military victory, each act of justice was the LORD of hosts at work. This is not David's political genius; it is the presence of God."
    },
    "10": {
      "L": "These also are the chief of the mighty men whom David had, who strengthened themselves with him in his kingdom, together with all Israel, to make him king, according to the word of the LORD concerning Israel.",
      "M": "These are the chiefs of David's mighty men, who, along with all Israel, gave him strong support in his kingdom to make him king, according to the word of the LORD concerning Israel.",
      "T": "Here begins the honour roll of David's mighty men -- warriors who bound themselves to him before his kingship was secure and held him up as the word of the LORD was working itself out. Their loyalty was not to a winner; they were loyal when the outcome was still uncertain."
    },
    "11": {
      "L": "And this is the number of the mighty men whom David had: Jashobeam, a Hachmonite, chief of the thirty; he lifted up his spear against three hundred and slew them at one time.",
      "M": "This is the number of David's mighty men: Jashobeam the Hachmonite, chief of the thirty; he raised his spear against three hundred men and killed them at one time.",
      "T": "At the head of the honour roll: Jashobeam the Hachmonite, chief of the thirty. One man, one stand, three hundred dead. The Chronicler does not explain the battle; he records the fact. Some feats require no commentary."
    },
    "12": {
      "L": "And after him was Eleazar the son of Dodo the Ahohite, who was one of the three mighty men.",
      "M": "After him was Eleazar son of Dodo the Ahohite, one of the three mighty men.",
      "T": "Second in the inner circle: Eleazar son of Dodo the Ahohite. One of the three -- a smaller, more elite group still."
    },
    "13": {
      "L": "He was with David at Pasdammim, where the Philistines were gathered together to battle; and there was a plot of ground full of barley; and the people fled from before the Philistines.",
      "M": "He was with David at Pasdammim when the Philistines gathered there for battle. There was a field full of barley, and when the people fled from the Philistines,",
      "T": "At Pasdammim, where the Philistines massed for battle, Israel's army broke and ran from a barley field. Not a great fortress, not a strategic ridge -- a barley field. And Eleazar stayed."
    },
    "14": {
      "L": "And they set themselves in the midst of that plot, and defended it, and slew the Philistines; and the LORD saved them by a great deliverance.",
      "M": "they took their stand in the middle of that field and defended it, and struck down the Philistines. And the LORD saved them by a great deliverance.",
      "T": "He and David held the ground in the centre of that barley field and cut down the Philistines until the enemy broke. Then the rest of Israel returned -- to collect the spoil from a victory they had not fought. The LORD gave the deliverance; Eleazar and David held the line long enough to receive it."
    },
    "15": {
      "L": "Now three of the thirty captains went down to the rock to David, into the cave of Adullam; and the host of the Philistines encamped in the valley of Rephaim.",
      "M": "Three of the thirty chiefs went down to David at the rock, to the cave of Adullam, while a band of Philistines was encamped in the Valley of Rephaim.",
      "T": "A different story, same courage. Three of the thirty made their way to David in hiding at the cave of Adullam -- the fugitive years, when the king-to-be sheltered in caves and his men sought him out. The Philistines held the valley of Rephaim below."
    },
    "16": {
      "L": "And David was then in the stronghold, and the garrison of the Philistines was then at Bethlehem.",
      "M": "David was in the stronghold at that time, and the Philistines had a garrison at Bethlehem.",
      "T": "David was in hiding; the Philistines had garrisoned Bethlehem -- his hometown, his father's fields, the well he had drunk from as a boy."
    },
    "17": {
      "L": "And David longed, and said, Oh that one would give me drink of the water of the well of Bethlehem, that is at the gate!",
      "M": "David expressed a longing and said, 'Oh, that someone would give me water to drink from the well of Bethlehem that is by the gate!'",
      "T": "David's longing broke out in words: 'If only someone would bring me water from the well at Bethlehem's gate!' Not a command. Not a request. A moment of raw homesickness, a king in exile aching for the taste of home."
    },
    "18": {
      "L": "And the three broke through the host of the Philistines, and drew water out of the well of Bethlehem, that was by the gate, and took it and brought it to David; but David would not drink of it, but poured it out to the LORD,",
      "M": "So the three broke through the Philistine camp, drew water from the well of Bethlehem by the gate, and brought it to David. But David would not drink it; he poured it out to the LORD,",
      "T": "Three men heard the longing and acted. They broke through the Philistine lines, filled a vessel from the Bethlehem well, and brought it back through enemy territory. And David -- when he saw what they had done -- refused to drink. He poured it out before the LORD."
    },
    "19": {
      "L": "and said, My God forbid it me, that I should do this thing: shall I drink the blood of these men that have put their lives in jeopardy? for with the jeopardy of their lives they brought it. Therefore he would not drink it.",
      "M": "saying, 'My God, far be it from me to do this! Shall I drink the blood of these men who risked their lives? For they brought it at the risk of their own lives.' So he would not drink it.",
      "T": "'My God, far be it from me -- shall I drink the lifeblood of these men?' The word nephesh sits in the sentence: their embodied selves, their very lives, they had staked on a cup of water. Water drawn at that cost was not water anymore. It was blood. It belonged to God. David poured it out as an offering. These three mighty men did this."
    },
    "20": {
      "L": "And Abishai the brother of Joab, he was chief of the three: for lifting up his spear against three hundred, he slew them, and had a name among the three.",
      "M": "Abishai the brother of Joab was chief of the three. He raised his spear against three hundred and killed them, and won a name among the three.",
      "T": "Abishai, Joab's brother, was the leader of a second tier -- the three who were not the three. He raised his spear and killed three hundred, earning his place in the record alongside the inner circle."
    },
    "21": {
      "L": "Of the three, he was more honourable than the two, and was their captain: howbeit he attained not to the first three.",
      "M": "Among the three he was more honoured than the other two, and became their commander, but he did not attain to the first three.",
      "T": "More honoured than his two, yet not the equal of the first three -- the text holds the tension without resolving it. Abishai led but was not at the summit. Some hierarchies remain irreducible."
    },
    "22": {
      "L": "Benaiah the son of Jehoiada, the son of a valiant man of Kabzeel, who had done great acts; he slew two lion-like men of Moab; also he went down and slew a lion in a pit in a snowy day.",
      "M": "Benaiah son of Jehoiada was a valiant man from Kabzeel, a man of great deeds. He killed two of the mightiest warriors of Moab. He also went down into a pit on a snowy day and killed a lion.",
      "T": "Benaiah son of Jehoiada of Kabzeel: great deeds in three registers. First -- he killed two lion-like men of Moab, warriors so formidable the text reaches for an animal metaphor. Second -- on a snowy day, he went down into a pit and killed a lion. Not drove it off. Killed it. In a pit. In the snow."
    },
    "23": {
      "L": "And he slew an Egyptian, a man of great stature, five cubits high; and in the Egyptian's hand was a spear like a weaver's beam; and he went down to him with a staff, and plucked the spear out of the Egyptian's hand, and slew him with his own spear.",
      "M": "He also killed an Egyptian, a man of great stature -- five cubits tall. The Egyptian had a spear like a weaver's beam, but Benaiah went down to him with only a staff, snatched the spear out of his hand, and killed him with his own spear.",
      "T": "Third -- he faced a giant Egyptian, seven and a half feet of trained warrior with a spear as thick as a loom-beam. Benaiah went at him with a walking staff. He snatched the spear from the Egyptian's hands and drove it back through him. The story is told in three steps: the disparity, the courage, the reversal. Benaiah's weapon was what he took from someone else."
    },
    "24": {
      "L": "These things did Benaiah the son of Jehoiada, and had the name among the three mighties.",
      "M": "These were the deeds of Benaiah son of Jehoiada, and he won a name among the three mighty men.",
      "T": "Three acts, each beyond ordinary courage, earned Benaiah his place in the circle of the three."
    },
    "25": {
      "L": "Behold, he was honourable among the thirty, but he attained not to the first three: and David set him over his guard.",
      "M": "He was honoured among the thirty, but he did not attain to the first three. And David put him in charge of his personal guard.",
      "T": "Benaiah stood above the thirty -- yet not at the summit of the three. David's response was practical honour: he made Benaiah commander of his personal bodyguard. The man who kills lions and giants becomes the one who stands closest to the king."
    },
    "26": {
      "L": "Also the valiant men of the armies were: Asahel the brother of Joab, Elhanan the son of Dodo of Bethlehem,",
      "M": "Among the warriors of the armies: Asahel the brother of Joab, Elhanan son of Dodo of Bethlehem,",
      "T": "The wider list begins: Asahel, Joab's youngest brother -- swift as a gazelle, killed in battle by Abner -- and Elhanan of Bethlehem."
    },
    "27": {
      "L": "Shammoth the Harorite, Helez the Pelonite,",
      "M": "Shammoth the Harorite, Helez the Pelonite,",
      "T": "Shammoth the Harorite, Helez the Pelonite."
    },
    "28": {
      "L": "Ira the son of Ikkesh the Tekoite, Abiezer the Antothite,",
      "M": "Ira son of Ikkesh the Tekoite, Abiezer the Antothite,",
      "T": "Ira son of Ikkesh of Tekoa -- the same southern Judaean city that would later produce the prophet Amos. Abiezer of Anathoth."
    },
    "29": {
      "L": "Sibbecai the Hushathite, Ilai the Ahohite,",
      "M": "Sibbecai the Hushathite, Ilai the Ahohite,",
      "T": "Sibbecai the Hushathite, Ilai the Ahohite."
    },
    "30": {
      "L": "Maharai the Netophathite, Heled the son of Baanah the Netophathite,",
      "M": "Maharai the Netophathite, Heled son of Baanah the Netophathite,",
      "T": "Two warriors from Netophah, a village near Bethlehem -- Maharai and Heled son of Baanah."
    },
    "31": {
      "L": "Ithai the son of Ribai of Gibeah of the sons of Benjamin, Benaiah the Pirathonite,",
      "M": "Ithai son of Ribai from Gibeah of Benjamin, Benaiah the Pirathonite,",
      "T": "Ithai from Gibeah of Benjamin -- Saul's own hometown producing warriors for David. Benaiah of Pirathon."
    },
    "32": {
      "L": "Hurai of the brooks of Gaash, Abiel the Arbathite,",
      "M": "Hurai of the brooks of Gaash, Abiel the Arbathite,",
      "T": "Hurai from the ravines near Mount Gaash, Abiel of Beth-arabah."
    },
    "33": {
      "L": "Azmaveth the Baharumite, Eliahba the Shaalbonite,",
      "M": "Azmaveth the Baharumite, Eliahba the Shaalbonite,",
      "T": "Azmaveth the Baharumite, Eliahba of Shaalbon."
    },
    "34": {
      "L": "The sons of Hashem the Gizonite, Jonathan the son of Shage the Hararite,",
      "M": "The sons of Hashem the Gizonite, Jonathan son of Shage the Hararite,",
      "T": "The sons of Hashem the Gizonite; Jonathan son of Shage the Hararite."
    },
    "35": {
      "L": "Ahiam the son of Sacar the Hararite, Eliphal the son of Ur,",
      "M": "Ahiam son of Sacar the Hararite, Eliphal son of Ur,",
      "T": "Ahiam son of Sacar the Hararite, Eliphal son of Ur."
    },
    "36": {
      "L": "Hepher the Mecherathite, Ahijah the Pelonite,",
      "M": "Hepher the Mecherathite, Ahijah the Pelonite,",
      "T": "Hepher the Mecherathite, Ahijah the Pelonite."
    },
    "37": {
      "L": "Hezro the Carmelite, Naarai the son of Ezbai,",
      "M": "Hezro the Carmelite, Naarai son of Ezbai,",
      "T": "Hezro of Carmel, Naarai son of Ezbai."
    },
    "38": {
      "L": "Joel the brother of Nathan, Mibhar the son of Hagri,",
      "M": "Joel the brother of Nathan, Mibhar son of Hagri,",
      "T": "Joel the brother of Nathan, Mibhar son of Hagri."
    },
    "39": {
      "L": "Zelek the Ammonite, Naharai the Berothite, the armourbearer of Joab the son of Zeruiah,",
      "M": "Zelek the Ammonite, Naharai the Berothite, who was the armour-bearer of Joab son of Zeruiah,",
      "T": "Zelek the Ammonite -- a foreigner in David's inner circle. Naharai of Beeroth, who carried Joab's weapons in battle."
    },
    "40": {
      "L": "Ira the Ithrite, Gareb the Ithrite,",
      "M": "Ira the Ithrite, Gareb the Ithrite,",
      "T": "Two Ithrites -- Ira and Gareb."
    },
    "41": {
      "L": "Uriah the Hittite, Zabad the son of Ahlai,",
      "M": "Uriah the Hittite, Zabad son of Ahlai,",
      "T": "Uriah the Hittite. His name here, in the honour roll of David's most faithful warriors, stands as a silent accusation against what is coming. He is also, at this point in the Chronicler's narrative, simply loyal. Zabad son of Ahlai."
    },
    "42": {
      "L": "Adina the son of Shiza the Reubenite, a captain of the Reubenites, and thirty with him,",
      "M": "Adina son of Shiza the Reubenite, a commander of the Reubenites, and thirty with him,",
      "T": "Adina son of Shiza the Reubenite -- a clan-captain who brought thirty men with him, a whole company folded into David's service."
    },
    "43": {
      "L": "Hanan the son of Maachah, and Joshaphat the Mithnite,",
      "M": "Hanan son of Maacah, and Joshaphat the Mithnite,",
      "T": "Hanan son of Maacah, Joshaphat the Mithnite."
    },
    "44": {
      "L": "Uzzia the Ashterathite, Shama and Jehiel the sons of Hothan the Aroerite,",
      "M": "Uzzia the Ashterathite, and Shama and Jeiel the sons of Hothan the Aroerite,",
      "T": "Uzzia of Ashteroth, and two brothers -- Shama and Jeiel, sons of Hothan of Aroer."
    },
    "45": {
      "L": "Jediael the son of Shimri, and Joha his brother, the Tizite,",
      "M": "Jediael son of Shimri, and Joha his brother, the Tizite,",
      "T": "Brothers in arms -- Jediael son of Shimri and his brother Joha the Tizite."
    },
    "46": {
      "L": "Eliel the Mahavite, and Jeribai and Joshaviah, the sons of Elnaam, and Ithmah the Moabite,",
      "M": "Eliel the Mahavite, Jeribai and Joshaviah the sons of Elnaam, and Ithmah the Moabite,",
      "T": "Eliel the Mahavite; Jeribai and Joshaviah, sons of Elnaam; Ithmah the Moabite -- another foreigner serving Israel's king."
    },
    "47": {
      "L": "Eliel, and Obed, and Jaasiel the Mesobaite.",
      "M": "Eliel, Obed, and Jaasiel the Mesobaite.",
      "T": "Eliel, Obed, and Jaasiel the Mesobaite. The roll ends here -- not with commentary but with names. The Chronicler's conviction is that names matter: these men existed, fought, and are remembered."
    }
  },
  "12": {
    "1": {
      "L": "Now these are they that came to David to Ziklag, while he yet kept himself close because of Saul the son of Kish; and they were among the mighty men, helpers of the war.",
      "M": "These are the men who came to David at Ziklag while he was still keeping himself hidden from Saul son of Kish. They were among the mighty men, helpers in battle.",
      "T": "A second list -- those who came to David not after his coronation but before it, during the fugitive years at Ziklag. When helping David was a risk, these men came. The Chronicler names them to honour a particular kind of loyalty: loyalty given before the outcome was known."
    },
    "2": {
      "L": "They were armed with bows, and could use both the right hand and the left in hurling stones and shooting arrows out of a bow, even of Saul's brethren of Benjamin.",
      "M": "They were armed with bows and could use both right and left hands to sling stones and shoot arrows. They were from Benjamin, Saul's own kindred.",
      "T": "Ambidextrous archers and slingers -- trained to throw from either hand, twice as dangerous in close terrain. And they were Benjaminites -- Saul's own tribe, Saul's own blood, choosing David. The Chronicler marks the defection without embellishment. These men crossed a tribal line."
    },
    "3": {
      "L": "The chief was Ahiezer, then Joash, the sons of Shemaah the Gibeathite; and Jeziel, and Pelet, the sons of Azmaveth; and Berachah, and Jehu the Antothite,",
      "M": "Their chief was Ahiezer, then Joash, the sons of Shemaah the Gibeathite; Jeziel and Pelet the sons of Azmaveth; Berachah and Jehu the Antothite,",
      "T": "The Benjaminite contingent: Ahiezer and Joash of Gibeah; Jeziel and Pelet of Azmaveth; Berachah and Jehu of Anathoth --"
    },
    "4": {
      "L": "and Ishmaiah the Gibeonite, a mighty man among the thirty, and over the thirty; and Jeremiah, and Jahaziel, and Johanan, and Josabad the Gederathite,",
      "M": "and Ishmaiah the Gibeonite, a mighty man among the thirty and leader over them; Jeremiah, Jahaziel, Johanan, and Jozabad the Gederathite,",
      "T": "-- and Ishmaiah the Gibeonite, who stood among the thirty and above them, a warrior-leader from a city with its own complicated covenant history. With him: Jeremiah, Jahaziel, Johanan, Jozabad of Gederah."
    },
    "5": {
      "L": "Eluzai, and Jerimoth, and Bealiah, and Shemariah, and Shephatiah the Haruphite,",
      "M": "Eluzai, Jerimoth, Bealiah, Shemariah, and Shephatiah the Haruphite,",
      "T": "Eluzai, Jerimoth, Bealiah, Shemariah, Shephatiah of Haruph."
    },
    "6": {
      "L": "Elkanah, and Jesiah, and Azareel, and Joezer, and Jashobeam, the Korhites,",
      "M": "Elkanah, Jesiah, Azareel, Joezer, and Jashobeam -- the Korhites,",
      "T": "Elkanah, Jesiah, Azareel, Joezer, Jashobeam -- all from the Korahite clans, descendants of the Levite family through which temple music would later flow."
    },
    "7": {
      "L": "And Joelah, and Zebadiah, the sons of Jeroham of Gedor.",
      "M": "and Joelah and Zebadiah, sons of Jeroham of Gedor.",
      "T": "And Joelah and Zebadiah, brothers from Gedor, sons of Jeroham."
    },
    "8": {
      "L": "And of the Gadites there separated themselves unto David into the hold to the wilderness men of might, and men of war fit for the battle, that could handle shield and buckler, whose faces were like the faces of lions, and were as swift as the roes upon the mountains;",
      "M": "From the Gadites there came over to David in the stronghold in the wilderness warriors fit for battle, who could handle shield and spear, whose faces were like the faces of lions and were as swift as gazelles on the mountains:",
      "T": "From the tribe of Gad, men crossed the Jordan to join David in the wilderness stronghold. The Chronicler paints them in animal terms: faces like lions, speed like gazelles. These were not soldiers who marched in formation -- they were hunters and warriors who moved like the animals they hunted. They could handle shield and spear and they chose David."
    },
    "9": {
      "L": "Ezer the first, Obadiah the second, Eliab the third,",
      "M": "Ezer the first, Obadiah the second, Eliab the third,",
      "T": "The Gadite leaders in order: Ezer first, Obadiah second, Eliab third,"
    },
    "10": {
      "L": "Mishmannah the fourth, Jeremiah the fifth,",
      "M": "Mishmannah the fourth, Jeremiah the fifth,",
      "T": "Mishmannah fourth, Jeremiah fifth,"
    },
    "11": {
      "L": "Attai the sixth, Eliel the seventh,",
      "M": "Attai the sixth, Eliel the seventh,",
      "T": "Attai sixth, Eliel seventh,"
    },
    "12": {
      "L": "Johanan the eighth, Elzabad the ninth,",
      "M": "Johanan the eighth, Elzabad the ninth,",
      "T": "Johanan eighth, Elzabad ninth,"
    },
    "13": {
      "L": "Jeremiah the tenth, Machbanai the eleventh.",
      "M": "Jeremiah the tenth, Machbanai the eleventh.",
      "T": "Jeremiah tenth, Machbanai eleventh. Eleven lion-faced men."
    },
    "14": {
      "L": "These were of the sons of Gad, captains of the host: one of the least was over a hundred, and the greatest over a thousand.",
      "M": "These Gadites were captains of the army; the least of them commanded a hundred men, the greatest commanded a thousand.",
      "T": "The smallest of these Gadite captains led a hundred men; the greatest led a thousand. They did not come as individuals but as commanders, bringing their own companies with them. The movement to David was a mass transfer of military force."
    },
    "15": {
      "L": "These are they that went over Jordan in the first month, when it had overflowed all his banks; and they put to flight all them of the valleys, both toward the east, and toward the west.",
      "M": "These are the ones who crossed the Jordan in the first month, when it had overflowed all its banks, and they put to flight all those in the valleys, to the east and to the west.",
      "T": "They crossed the Jordan at flood stage -- the first month, when the river ran bank-full and unfordable to ordinary travellers. Not these men. They drove out everyone in the valley, east and west. It was a demonstration of what they were."
    },
    "16": {
      "L": "And there came of the children of Benjamin and Judah to the hold unto David.",
      "M": "Then some of the men of Benjamin and Judah also came to David in the stronghold.",
      "T": "More came -- from Benjamin and Judah both, men of two different tribes making the same choice. The movement toward David was building."
    },
    "17": {
      "L": "And David went out to meet them, and answered and said unto them, If ye be come peaceably unto me to help me, mine heart shall be knit unto you: but if ye be come to betray me to mine enemies, seeing there is no wrong in mine hands, the God of our fathers look thereon, and rebuke it.",
      "M": "David went out to meet them and said to them: 'If you have come to me in peace, to help me, my heart will be joined to yours; but if you have come to betray me to my enemies when there is no wrong in my hands, may the God of our fathers see it and judge.'",
      "T": "David went out personally to meet them -- a vulnerable act, meeting armed strangers in the open. His words are honest about the danger: 'If you come in peace, I am yours entirely. But if you come to sell me to my enemies -- and I have done no wrong -- then may God himself see it and act.' He offers fellowship or appeals to divine justice. He does not threaten. The appeal to the God of the fathers is the only security available to a man in hiding."
    },
    "18": {
      "L": "Then the Spirit came upon Amasai, who was chief of the captains, and he said, Thine are we, David, and on thy side, thou son of Jesse: peace, peace be unto thee, and peace be to thine helpers; for thy God helpeth thee. Then David received them, and made them captains of the band.",
      "M": "Then the Spirit came upon Amasai, chief of the captains, who said: 'We are yours, David! We are with you, son of Jesse! Peace, peace to you, and peace to those who help you, for your God helps you.' Then David received them and made them commanders of his raiding party.",
      "T": "The Spirit clothed Amasai -- the word is wayyilbash, the Spirit as garment, wrapping a person for a moment of divine speech. The answer comes not as policy but as prophecy:\n'We are yours, David!\nWe are with you, son of Jesse!\nPeace to you, peace to those who help you --\nfor your God helps you.'\nDavid received them and gave them command. The Spirit had spoken through an enemy-tribe commander to seal the covenant. There was no better warrant."
    },
    "19": {
      "L": "And there fell some of Manasseh to David, when he came with the Philistines against Saul to battle: but they helped them not: for the lords of the Philistines upon advisement sent him away, saying, He will fall to his master Saul to the jeopardy of our heads.",
      "M": "Some men of Manasseh also defected to David when he came with the Philistines against Saul in battle. However, they did not actually help the Philistines, because the Philistine lords dismissed David on advice, saying, 'He will defect to his master Saul at the cost of our heads.'",
      "T": "At the moment of greatest ambiguity -- David marching with the Philistines against Saul -- some Manassites defected to him. The Philistine lords sent David away before the battle, fearing exactly this: that David would switch sides in the fight. The Manassites never had to choose. Providence arranged it cleanly."
    },
    "20": {
      "L": "As he went to Ziklag, there fell to him of Manasseh, Adnah, and Jozabad, and Jediael, and Michael, and Jozabad, and Elihu, and Zilthai, captains of the thousands that were of Manasseh.",
      "M": "As David went to Ziklag, Adnah, Jozabad, Jediael, Michael, Jozabad, Elihu, and Zilthai came over to him from Manasseh -- all commanders of thousands belonging to Manasseh.",
      "T": "Seven commanders of thousands from Manasseh joined David on the road back to Ziklag: Adnah, Jozabad, Jediael, Michael, another Jozabad, Elihu, and Zilthai. Seven thousand-commanders -- a significant transfer of military capacity at a vulnerable moment."
    },
    "21": {
      "L": "And they helped David against the band of the rovers: for they were all mighty men of valour, and were captains in the host.",
      "M": "They helped David against the raiding party, for they were all men of great valour and became commanders in the army.",
      "T": "These men proved themselves immediately: they helped David fight off the Amalekite raiders who had burned Ziklag. Their valour was tested at once. All were made commanders in David's growing army."
    },
    "22": {
      "L": "For at that time day by day there came to David to help him, until it was a great host, like the host of God.",
      "M": "For at that time men came to David day by day to help him, until there was a great army, like the army of God.",
      "T": "Day by day they came -- a trickle becoming a river becoming an ocean. The Chronicler compares the final host to the army of God, the divine council's warriors. The hyperbole is theological: this gathering was not merely political momentum but divine purpose working through human choices."
    },
    "23": {
      "L": "And these are the numbers of the bands that were ready armed to the war, and came to David to Hebron, to turn the kingdom of Saul to him, according to the word of the LORD.",
      "M": "These are the numbers of the divisions of the armed warriors who came to David at Hebron to transfer Saul's kingdom to him, according to the word of the LORD:",
      "T": "Now the final muster: the full count of those who came to Hebron for the great coronation. The Chronicler frames the whole event theologically -- they came 'according to the word of the LORD.' The transfer of power from Saul's house to David was not a coup. It was covenant fulfilment."
    },
    "24": {
      "L": "The children of Judah that bare shield and spear were six thousand and eight hundred, ready armed to the war.",
      "M": "From Judah: six thousand eight hundred, bearing shield and spear, ready armed for war.",
      "T": "Judah sent 6,800 -- armed with shield and spear, David's own tribe leading the muster."
    },
    "25": {
      "L": "Of the children of Simeon, mighty men of valour for the war, seven thousand and one hundred.",
      "M": "From Simeon: seven thousand one hundred mighty men of valour for war.",
      "T": "Simeon sent 7,100 warriors -- embedded in Judah's territory but present and counted."
    },
    "26": {
      "L": "Of the children of Levi four thousand and six hundred.",
      "M": "From Levi: four thousand six hundred.",
      "T": "Levi sent 4,600 -- the priestly tribe also had men of war, and they came."
    },
    "27": {
      "L": "And Jehoiada was the leader of the Aaronites, and with him were three thousand and seven hundred;",
      "M": "Jehoiada was the leader of the Aaronites; with him were three thousand seven hundred.",
      "T": "Jehoiada the Aaronite leader brought 3,700 of his own -- the priestly clan sending its sons to crown the king."
    },
    "28": {
      "L": "And Zadok, a young man mighty of valour, and of his father's house twenty and two captains.",
      "M": "And Zadok, a young man mighty in valour, with twenty-two commanders from his father's house.",
      "T": "And Zadok -- young, valiant, bringing twenty-two captains from his own household. This Zadok will become the great high priest of David's and Solomon's reigns. He arrives at Hebron as a warrior."
    },
    "29": {
      "L": "And of the children of Benjamin, the kindred of Saul, three thousand: for hitherto the greatest part of them had kept the ward of the house of Saul.",
      "M": "From Benjamin, Saul's own kindred: three thousand, for until now most of them had remained loyal to the house of Saul.",
      "T": "Benjamin sent only 3,000 -- the smallest tribal contingent. The Chronicler notes the reason honestly: they had been keeping Saul's house until now. Three thousand is not a ringing endorsement of David from Saul's home tribe, but it is a beginning."
    },
    "30": {
      "L": "And of the children of Ephraim twenty thousand and eight hundred, mighty men of valour, famous throughout the house of their fathers.",
      "M": "From Ephraim: twenty thousand eight hundred, mighty men of valour, famous in their own clans.",
      "T": "Ephraim sent 20,800 -- warriors of renown, already famous in their own clans, now adding their fame to David's cause."
    },
    "31": {
      "L": "And of the half tribe of Manasseh eighteen thousand, which were expressed by name, to come and make David king.",
      "M": "From the half-tribe of Manasseh: eighteen thousand, who were listed by name to come and make David king.",
      "T": "The western half of Manasseh sent 18,000, each man named on a list -- not a general levy but a deliberate enrolment, names recorded as a covenant act."
    },
    "32": {
      "L": "And of the children of Issachar, which were men that had understanding of the times, to know what Israel ought to do; the heads of them were two hundred; and all their brethren were at their commandment.",
      "M": "From Issachar: two hundred chiefs who understood the times and knew what Israel should do; and all their kinsmen were under their command.",
      "T": "Issachar is described differently from every other tribe: not by military numbers but by wisdom. Two hundred chiefs who understood the times -- who could read the hour, who knew what Israel ought to do. Their whole clan followed their lead. Discernment, not just courage, was their gift."
    },
    "33": {
      "L": "Of Zebulun, such as went forth to battle, expert in war, with all instruments of war, fifty thousand, which could keep rank: they were not of double heart.",
      "M": "From Zebulun: fifty thousand who could go out to war, trained in all weapons, keeping rank and not of double heart.",
      "T": "Zebulun sent 50,000 -- the largest single tribal contingent. Trained in every weapon, disciplined in formation, and 'not of double heart.' The Hebrew idiom for undivided loyalty: they did not come hedging their bets or keeping one eye on Saul's remnant. They came whole."
    },
    "34": {
      "L": "And of Naphtali a thousand captains, and with them with shield and spear thirty and seven thousand.",
      "M": "From Naphtali: a thousand commanders and with them thirty-seven thousand bearing shield and spear.",
      "T": "Naphtali sent a thousand commanders leading 37,000 men -- the ratio of officers to soldiers speaks to the quality of organisation."
    },
    "35": {
      "L": "And of the Danites expert in war twenty and eight thousand and six hundred.",
      "M": "From Dan: twenty-eight thousand six hundred, expert in war.",
      "T": "Dan sent 28,600 seasoned warriors."
    },
    "36": {
      "L": "And of Asher, such as went forth to battle, expert in war, forty thousand.",
      "M": "From Asher: forty thousand who could go out to war, expert in battle.",
      "T": "Asher sent 40,000 -- a full mobilisation of the northern coastal tribe."
    },
    "37": {
      "L": "And on the other side of Jordan, of the Reubenites, and the Gadites, and of the half tribe of Manasseh, with all manner of instruments of war for the battle, an hundred and twenty thousand.",
      "M": "From beyond the Jordan -- the Reubenites, Gadites, and the half-tribe of Manasseh -- with every kind of weapon for war: one hundred twenty thousand.",
      "T": "The Transjordanian tribes sent 120,000 -- the eastern side of Israel crossing the Jordan to crown the western king. All twelve tribes, every region, all the way to the edges of the promised land, represented in this gathering."
    },
    "38": {
      "L": "All these men of war, that could keep rank, came with a perfect heart to Hebron, to make David king over all Israel: and all the rest also of Israel were of one heart to make David king.",
      "M": "All these men of war, who could keep rank, came to Hebron with a perfect heart to make David king over all Israel. And all the rest of Israel were also of one heart to make David king.",
      "T": "The Chronicler's great summary: every soldier came with 'a perfect heart' -- undivided, whole, without reservation. And all Israel beyond the army -- the whole nation -- was of one heart too. This is the Chronicler's vision of the ideal moment: all Israel united, no division, no dissent, one king, one LORD, one people."
    },
    "39": {
      "L": "And there they were with David three days, eating and drinking: for their brethren had prepared for them.",
      "M": "They spent three days there with David, eating and drinking, for their kinsmen had prepared food for them.",
      "T": "Three days of feasting at Hebron -- the great coronation feast. Their brothers had made provision. The army did not forage; they were fed by their own people. The whole nation at table, three days, celebrating the king."
    },
    "40": {
      "L": "Moreover they that were nigh them, even unto Issachar and Zebulun and Naphtali, brought bread on asses, and on camels, and on mules, and on oxen, and meat, meal, cakes of figs, and bunches of raisins, and wine, and oil, and oxen, and sheep abundantly: for there was joy in Israel.",
      "M": "Also, their neighbours from as far as Issachar, Zebulun, and Naphtali came bringing bread on donkeys, camels, mules, and oxen -- food, flour, cakes of figs, clusters of raisins, wine, oil, oxen, and sheep in abundance. For there was joy in Israel.",
      "T": "From across the land they brought food: bread loaded on donkeys and camels, grain and pressed figs and raisin-clusters, wine and oil, livestock in abundance. The feast was provisioned by the people themselves. The Chronicler ends the chapter with a single sentence that carries the whole weight: 'For there was joy in Israel.' Not relief, not triumph -- joy. The covenant was working."
    }
  },
  "13": {
    "1": {
      "L": "And David consulted with the captains of thousands and hundreds, and with every leader.",
      "M": "David consulted with the commanders of thousands and hundreds, and with every leader.",
      "T": "The newly crowned king's first domestic act: he calls a council. Every commander, every leader is consulted. David does not simply decree -- he seeks the agreement of those he leads."
    },
    "2": {
      "L": "And David said unto all the congregation of Israel, If it seem good unto you, and that it be of the LORD our God, let us send abroad unto our brethren every where, that are left in all the land of Israel, and with them also to the priests and Levites which are in their cities and suburbs, that they may gather themselves unto us: and let us bring again the ark of our God to us: for we enquired not at it in the days of Saul.",
      "M": "David said to all the assembly of Israel: 'If it seems good to you, and if it is of the LORD our God, let us send word everywhere to our kinsmen remaining in all the land of Israel, and also to the priests and Levites in their towns with pasture lands, so they may come together to us. Then let us bring the ark of our God back to us, for we did not seek it during the days of Saul.'",
      "T": "David frames the project as a question, not a command: 'If it seems good to you, and if this is of the LORD.' Both conditions matter -- popular will and divine will, tested together. The stated reason cuts deep: 'We did not seek the ark in the days of Saul.' A whole reign had passed without the ark at its centre; the presence of God had been neglected. David intends to end that neglect."
    },
    "3": {
      "L": "And let us bring again the ark of our God to us: for we enquired not at it in the days of Saul.",
      "M": "And let us bring the ark of our God back to us, for we did not inquire of it during Saul's days.",
      "T": "The ark had been at Kiriath-jearim, sidelined, for a generation. Saul had reigned without it. David names this as a failure -- not merely a logistical oversight but a spiritual one. To not seek the ark was to not seek the LORD. David's kingship will be different."
    },
    "4": {
      "L": "And all the congregation said that they would do so: for the thing was right in the eyes of all the people.",
      "M": "And all the assembly agreed to do so, for the thing seemed right to all the people.",
      "T": "The people agree unanimously. The Chronicler underlines it: 'right in the eyes of all the people.' There is no dissent. Bringing the ark home was, in everyone's judgment, the right thing. The good beginning makes what follows all the more terrible."
    },
    "5": {
      "L": "So David gathered all Israel together, from Shihor of Egypt even unto the entering of Hemath, to bring the ark of God from Kirjathjearim.",
      "M": "So David assembled all Israel, from Shihor of Egypt to the entrance of Hamath, to bring the ark of God from Kiriath-jearim.",
      "T": "The gathering is pan-Israelite -- from the Nile delta (Shihor) in the south to Hamath in the far north. The whole land, the whole promise, assembling for the one purpose: bring the ark home."
    },
    "6": {
      "L": "And David went up, and all Israel, to Baalah, that is, to Kirjathjearim, which belonged to Judah, to bring up thence the ark of God the LORD, that dwelleth between the cherubims, whose name is called on it.",
      "M": "David and all Israel went up to Baalah, that is, to Kiriath-jearim, which belongs to Judah, to bring up from there the ark of God -- the LORD, who is enthroned above the cherubim -- on which his name is called.",
      "T": "Baalah -- the old Canaanite name for Kiriath-jearim, preserved in the text alongside the Israelite name. The ark carries a full title: the ark of God the LORD, who is enthroned above the cherubim, on which the Name is called. This is not merely a wooden box. It is the portable throne of the Creator of the universe."
    },
    "7": {
      "L": "And they carried the ark of God in a new cart out of the house of Abinadab: and Uzza and Ahio drove the cart.",
      "M": "They carried the ark of God on a new cart from the house of Abinadab, and Uzza and Ahio were driving the cart.",
      "T": "A new cart -- presumably the most honorable transport available, the same method the Philistines had used to return the ark in 1 Samuel 6. This is the first mistake, though no one knows it yet. The ark was not designed for carts; it was designed to be carried by Levites on their shoulders with poles. The good intention did not sanctify the wrong method."
    },
    "8": {
      "L": "And David and all Israel played before God with all their might, and with singing, and with harps, and with psalteries, and with timbrels, and with cymbals, and with trumpets.",
      "M": "And David and all Israel were celebrating before God with all their might, with song and with harps, lyres, tambourines, cymbals, and trumpets.",
      "T": "Every instrument the culture possessed, every voice, all strength -- the procession was total worship. And it was genuine. The celebration was real. The disaster was not the result of impure motive but of impure method."
    },
    "9": {
      "L": "And when they came unto the threshingfloor of Chidon, Uzza put forth his hand to hold the ark; for the oxen stumbled.",
      "M": "When they came to the threshing floor of Chidon, the oxen stumbled, and Uzza reached out his hand to take hold of the ark.",
      "T": "The oxen stumbled -- not a dramatic military defeat, not a theological crisis, just a bad step in the road. The cart tilted. Uzza's instinct was to protect the ark. He reached out his hand."
    },
    "10": {
      "L": "And the anger of the LORD was kindled against Uzza, and he smote him, because he put his hand to the ark: and there he died before God.",
      "M": "Then the anger of the LORD was kindled against Uzza, and he struck him down because he put his hand on the ark, and he died there before God.",
      "T": "The LORD's anger broke out against Uzza, and he died there before the ark. The Chronicler does not soften it or explain it theologically -- he reports it. The ark was holy; the boundary around the holy was absolute. Uzza's instinct was protective; his act was transgressive. Both things are true simultaneously. He died at the place where the holy and the human intersected without the ordained mediation."
    },
    "11": {
      "L": "And David was displeased, because the LORD had made a breach upon Uzza: wherefore that place is called Perezuzza to this day.",
      "M": "David was angry because the LORD had broken out against Uzza; and so that place is called Perez-uzza to this day.",
      "T": "David was angry. The text does not flinch from this: he was angry at what the LORD had done. It was not a small response to a small event. And yet -- the name he gives the place means 'breach of Uzza.' David names the site of his anger and his grief together. The anger will pass; the name will remain."
    },
    "12": {
      "L": "And David was afraid of God that day, saying, How shall I bring the ark of God home to me?",
      "M": "David was afraid of God that day and said, 'How can I bring the ark of God to me?'",
      "T": "The anger became fear. If the LORD had done this to Uzza -- whose only sin was an instinct to protect -- what might he do to David himself? The question is honest and unanswerable in the moment: 'How can I bring the ark home?' He did not yet know the answer."
    },
    "13": {
      "L": "So David brought not the ark home to himself to the city of David, but carried it aside into the house of Obededom the Gittite.",
      "M": "So David did not take the ark to the city of David but carried it aside to the house of Obed-edom the Gittite.",
      "T": "David turned aside. He took the ark not to Jerusalem but to the house of Obed-edom the Gittite -- a Philistine by origin, living near Jerusalem. A foreigner became the temporary keeper of Israel's most sacred object. The irony is not lost on the Chronicler."
    },
    "14": {
      "L": "And the ark of God remained with the family of Obededom in his house three months. And the LORD blessed the house of Obededom, and all that he had.",
      "M": "The ark of God remained with the family of Obed-edom in his house for three months, and the LORD blessed the household of Obed-edom and everything that belonged to him.",
      "T": "Three months, and the LORD blessed Obed-edom's entire household. This will become David's evidence. The ark was not a curse to those who honoured it rightly; it was a fountain of blessing. Someone told David about the blessing -- and that report would be the catalyst for chapter 15."
    }
  },
  "14": {
    "1": {
      "L": "Now Hiram king of Tyre sent messengers to David, and timber of cedars, with masons and carpenters, to build him an house.",
      "M": "Hiram king of Tyre sent messengers to David, along with cedar timber, stonemasons, and carpenters, to build a house for him.",
      "T": "The great Phoenician king reaches out to the new Israelite one. Cedar timber, skilled craftsmen -- Hiram's gesture was both diplomatic recognition and material partnership. The finest builder in the region was acknowledging David's legitimacy."
    },
    "2": {
      "L": "And David perceived that the LORD had confirmed him king over Israel, for his kingdom was lifted up on high, because of his people Israel.",
      "M": "David perceived that the LORD had established him as king over Israel and that his kingdom had been exalted highly for the sake of his people Israel.",
      "T": "David read Hiram's gesture correctly -- not as personal flattery but as confirmation. The LORD had confirmed him. The kingdom was being built not for David's glory but for Israel's sake: 'for the sake of his people.' The Chronicler marks the distinction."
    },
    "3": {
      "L": "And David took more wives at Jerusalem: and David begat more sons and daughters.",
      "M": "David took more wives in Jerusalem, and fathered more sons and daughters.",
      "T": "The royal household grew in Jerusalem. More wives, more children -- the fruitfulness that in the ancient world signalled divine favour. The Chronicler lists the children without the moral commentary of Samuel-Kings."
    },
    "4": {
      "L": "Now these are the names of his children which he had in Jerusalem: Shammua, and Shobab, Nathan, and Solomon,",
      "M": "These are the names of the children born to him in Jerusalem: Shammua, Shobab, Nathan, and Solomon,",
      "T": "The sons of Jerusalem: Shammua, Shobab, Nathan, and Solomon -- through Nathan Luke will trace the line to Jesus; through Solomon Matthew will. Both lines from the same Bathsheba household."
    },
    "5": {
      "L": "And Ibhar, and Elishua, and Elpalet,",
      "M": "and Ibhar, Elishua, and Elpelet,",
      "T": "Ibhar, Elishua, Elpelet --"
    },
    "6": {
      "L": "And Nogah, and Nepheg, and Japhia,",
      "M": "and Nogah, Nepheg, and Japhia,",
      "T": "Nogah, Nepheg, Japhia --"
    },
    "7": {
      "L": "And Elishama, and Beeliada, and Eliphalet.",
      "M": "and Elishama, Beeliada, and Eliphelet.",
      "T": "-- Elishama, Beeliada, and Eliphelet. Thirteen sons named in Jerusalem; the dynasty's roots deepening."
    },
    "8": {
      "L": "And when the Philistines heard that David was anointed king over all Israel, all the Philistines went up to seek David. And David heard of it, and went out against them.",
      "M": "When the Philistines heard that David had been anointed king over all Israel, all the Philistines went up to search for David. David heard about it and went out to meet them.",
      "T": "The Philistines heard about the united kingdom and acted immediately. They had tolerated David as a tribal chieftain; they could not tolerate David as king of all Israel. They came seeking him -- not to negotiate but to destroy the threat before it consolidated. David did not wait for them to reach Jerusalem. He went out."
    },
    "9": {
      "L": "And the Philistines came and spread themselves in the valley of Rephaim.",
      "M": "The Philistines came and spread out in the Valley of Rephaim.",
      "T": "The Valley of Rephaim, the ancient battlefield southwest of Jerusalem, named for a race of giants. The Philistines spread themselves across it -- occupying the approaches to David's city."
    },
    "10": {
      "L": "And David enquired of God, saying, Shall I go up against the Philistines? and wilt thou deliver them into mine hand? And the LORD said unto him, Go up; for I will deliver them into thine hand.",
      "M": "David inquired of God: 'Shall I go up against the Philistines? Will you hand them over to me?' The LORD answered him: 'Go up, for I will deliver them into your hand.'",
      "T": "Before moving, David asks. The model of Saul's reign haunts everything here by contrast -- Saul acted without asking; David asks before acting. The answer comes direct: 'Go up. I will deliver them.' The battle plan is divine authorisation, not human calculation."
    },
    "11": {
      "L": "So they came up to Baalperazim; and David smote them there. Then David said, God hath broken in upon mine enemies by mine hand like the breaking forth of waters: therefore they called the name of that place Baalperazim.",
      "M": "They went up to Baal-perazim, and David struck them down there. David said, 'God has broken through my enemies by my hand like a bursting flood.' So that place was called Baal-perazim.",
      "T": "David gives the victory its name on the spot: Baal-perazim -- 'master of breakthroughs,' 'lord of the bursting flood.' He pictures the enemy line giving way like a dam wall, the divine warrior pouring through the breach. The metaphor is as sudden and irresistible as the battle itself."
    },
    "12": {
      "L": "And when they had left their gods there, David gave a commandment, and they were burned with fire.",
      "M": "The Philistines had abandoned their gods there, and David gave the command that they be burned with fire.",
      "T": "The Philistines left their idols on the field. David burned them. There is no interest here in captured gods, no booty of divine images. The command to destroy them was the point. Deuteronomy had said to burn the images of the nations -- David obeyed without hesitation."
    },
    "13": {
      "L": "And the Philistines yet again spread themselves abroad in the valley.",
      "M": "Once again the Philistines spread out in the valley.",
      "T": "They came back. The Philistines were not broken by one defeat; they simply re-grouped in the same valley. The second battle would require a different strategy."
    },
    "14": {
      "L": "Therefore David enquired again of God; and God said unto him, Go not up after them; turn away from them, and come upon them over against the mulberry trees.",
      "M": "David inquired of God again, and God said to him: 'Do not go up directly after them; circle around them and come at them in front of the balsam trees.'",
      "T": "David asks again -- even the same enemy, even the same valley, requires a fresh inquiry. And the LORD gives a different answer this time: not 'go up' but 'circle around, come at them from a different angle, wait for a sign.' The strategy has changed. Two victories through two different methods -- the Chronicler's point is that David always asked, and the LORD always answered specifically."
    },
    "15": {
      "L": "And it shall be, when thou shalt hear a sound of going in the tops of the mulberry trees, that then thou shalt go out to battle: for God is gone forth before thee to smite the host of the Philistines.",
      "M": "When you hear the sound of marching in the tops of the balsam trees, then go out to battle, for God has gone out before you to strike the Philistine army.",
      "T": "The sign: a sound in the treetops, like the rustle of a marching army passing overhead. When you hear that, move -- because by then God has already gone out before you. The battle is already won in the unseen realm; the visible engagement is catching up to the spiritual reality."
    },
    "16": {
      "L": "David therefore did as God commanded him: and they smote the host of the Philistines from Gibeon even to Gazer.",
      "M": "David did as God commanded, and they struck down the Philistine army from Gibeon to Gezer.",
      "T": "David did exactly as commanded and the route was total -- from Gibeon northwest all the way to Gezer on the Philistine border, a fifteen-mile rout. Obedience and decisive action working together."
    },
    "17": {
      "L": "And the fame of David went out into all lands; and the LORD brought the fear of him upon all nations.",
      "M": "And the fame of David spread throughout all the lands, and the LORD brought the fear of him upon all nations.",
      "T": "The Chronicler closes the chapter with a summary of David's international standing: his fame spread to all lands, and the nations feared him -- not because of his military genius but because 'the LORD brought the fear of him.' It was God's doing, not merely David's reputation. This is what the blessing of the covenant looks like on the international stage."
    }
  },
  "15": {
    "1": {
      "L": "And David made him houses in the city of David, and prepared a place for the ark of God, and pitched for it a tent.",
      "M": "David built houses for himself in the city of David and prepared a place for the ark of God, pitching a tent for it.",
      "T": "After three months the news came: Obed-edom's house was blessed since the ark arrived. David was ready to try again. Before anything else he prepared a place -- a tent, deliberately pitched in Jerusalem, waiting for the ark. The preparation precedes the procession."
    },
    "2": {
      "L": "Then David said, None ought to carry the ark of God but the Levites: for them hath the LORD chosen to carry the ark of God, and to minister unto him for ever.",
      "M": "Then David said, 'No one ought to carry the ark of God except the Levites, for the LORD has chosen them to carry the ark of God and to minister to him forever.'",
      "T": "Now David understands what went wrong. The ark was carried on a cart; it should have been carried by Levites on poles. The law of Moses was explicit -- Numbers 4:15 assigned the sons of Kohath to carry the holy things on their shoulders. David had used the Philistine method. Now he names the correction: only Levites, on their shoulders, as Moses commanded. Understanding came through grief."
    },
    "3": {
      "L": "And David gathered all Israel together to Jerusalem, to bring up the ark of the LORD unto his place, which he had prepared for it.",
      "M": "David assembled all Israel at Jerusalem to bring up the ark of the LORD to the place he had prepared for it.",
      "T": "A second national assembly. The first procession had ended in death; this one would begin with preparation. David called all Israel to Jerusalem again -- not despite what had happened but because of it."
    },
    "4": {
      "L": "And David assembled the children of Aaron, and the Levites:",
      "M": "David brought together the sons of Aaron and the Levites:",
      "T": "Specifically: the sons of Aaron and the Levites. The right people, in the right role, in the right order. The Chronicler lingers on the preparation because correct worship requires correct preparation."
    },
    "5": {
      "L": "Of the sons of Kohath; Uriel the chief, and his brethren an hundred and twenty:",
      "M": "From the sons of Kohath: Uriel the chief, and his kinsmen, one hundred twenty.",
      "T": "Kohath's Levites: Uriel the chief with 120 -- the sons of the clan charged to carry the ark itself."
    },
    "6": {
      "L": "Of the sons of Merari; Asaiah the chief, and his brethren two hundred and twenty:",
      "M": "From the sons of Merari: Asaiah the chief, and his kinsmen, two hundred twenty.",
      "T": "Merari's clan: Asaiah with 220."
    },
    "7": {
      "L": "Of the sons of Gershom; Joel the chief, and his brethren an hundred and thirty:",
      "M": "From the sons of Gershom: Joel the chief, and his kinsmen, one hundred thirty.",
      "T": "Gershom's clan: Joel with 130."
    },
    "8": {
      "L": "Of the sons of Elizaphan; Shemaiah the chief, and his brethren two hundred:",
      "M": "From the sons of Elizaphan: Shemaiah the chief, and his kinsmen, two hundred.",
      "T": "Elizaphan's clan: Shemaiah with 200."
    },
    "9": {
      "L": "Of the sons of Hebron; Eliel the chief, and his brethren fourscore:",
      "M": "From the sons of Hebron: Eliel the chief, and his kinsmen, eighty.",
      "T": "Hebron's Levites: Eliel with 80."
    },
    "10": {
      "L": "Of the sons of Uzziel; Amminadab the chief, and his brethren an hundred and twelve.",
      "M": "From the sons of Uzziel: Amminadab the chief, and his kinsmen, one hundred twelve.",
      "T": "Uzziel's clan: Amminadab with 112. Six Levitical families, all present, all counted, all assigned. The disorder of the first attempt has been replaced by order."
    },
    "11": {
      "L": "And David called for Zadok and Abiathar the priests, and for the Levites, for Uriel, Asaiah, and Joel, Shemaiah, and Eliel, and Amminadab,",
      "M": "And David summoned the priests Zadok and Abiathar, and the Levites: Uriel, Asaiah, Joel, Shemaiah, Eliel, and Amminadab.",
      "T": "David summoned them by name -- the two great priests, Zadok and Abiathar, and the six Levitical chiefs, Uriel, Asaiah, Joel, Shemaiah, Eliel, and Amminadab. This is the full leadership of the cult, gathered for briefing."
    },
    "12": {
      "L": "And said unto them, Ye are the chief of the fathers of the Levites: sanctify yourselves, both ye and your brethren, that ye may bring up the ark of the LORD God of Israel unto the place that I have prepared for it.",
      "M": "He said to them: 'You are the heads of the Levitical fathers' houses. Sanctify yourselves, you and your brothers, so that you may bring up the ark of the LORD, the God of Israel, to the place I have prepared for it.'",
      "T": "The command is precise: 'Sanctify yourselves.' Before the ark is moved, the movers must be prepared. Holiness is not assumed; it is prepared for. David gives the instruction that should have been given the first time."
    },
    "13": {
      "L": "For because ye did it not at the first, the LORD our God made a breach upon us, for that we sought him not after the due order.",
      "M": "For because you Levites did not carry it the first time, the LORD our God broke out against us, because we did not seek him according to the proper order.",
      "T": "David names the mistake plainly: 'You did not carry it the first time. We did not seek the LORD according to the rule.' He uses 'we' -- the king accepting corporate responsibility. The disaster at Chidon's threshing floor was not Uzza's fault alone; it was a communal failure to follow the law of Moses. This is David at his best: acknowledging error, correcting method, taking responsibility."
    },
    "14": {
      "L": "So the priests and the Levites sanctified themselves to bring up the ark of the LORD God of Israel.",
      "M": "So the priests and the Levites sanctified themselves to bring up the ark of the LORD, the God of Israel.",
      "T": "They obeyed. The priests and Levites underwent the rites of consecration -- the washing, the abstentions, the preparations prescribed by law. The second procession would begin from a different spiritual position."
    },
    "15": {
      "L": "And the children of the Levites bare the ark of God upon their shoulders with the staves thereon, as Moses commanded according to the word of the LORD.",
      "M": "And the Levites carried the ark of God on their shoulders with the poles on it, as Moses had commanded according to the word of the LORD.",
      "T": "Poles. Shoulders. Levites. Exactly as Moses had commanded in Numbers 4. The four words that summarise the entire correction: no more cart, no more oxen, no more deviation. The word of the LORD through Moses was the standard, and they met it."
    },
    "16": {
      "L": "And David spake to the chief of the Levites to appoint their brethren to be the singers with instruments of musick, psalteries and harps and cymbals, sounding, by lifting up the voice with joy.",
      "M": "David also told the chiefs of the Levites to appoint their fellow Levites as singers who would play musical instruments -- lyres, harps, and cymbals -- sounding aloud and lifting their voices with joy.",
      "T": "The procession must also have music. David assigns the Levitical chiefs to appoint singers and musicians -- lyres, harps, cymbals, voices lifted in joy. The worship is ordered, not improvised; every role assigned, every sound intentional. The first procession had music but not order; this one will have both."
    },
    "17": {
      "L": "So the Levites appointed Heman the son of Joel; and of his brethren, Asaph the son of Berechiah; and of the sons of Merari their brethren, Ethan the son of Kushaiah;",
      "M": "So the Levites appointed Heman son of Joel, and from his fellow Levites Asaph son of Berechiah, and from the sons of Merari their kinsmen Ethan son of Kushaiah.",
      "T": "Three master musicians appointed: Heman, Asaph, and Ethan -- the great triad of Levitical psalmody. Asaph's name will appear on psalms in the final collection; Heman's and Ethan's each appear on one. Here they are assigned to the procession of the ark."
    },
    "18": {
      "L": "And with them their brethren of the second degree, Zechariah, Ben, and Jaaziel, and Shemiramoth, and Jehiel, and Unni, Eliab, and Benaiah, and Maaseiah, and Mattithiah, and Elipheleh, and Mikneiah, and Obededom, and Jeiel, the porters.",
      "M": "With them, of the second rank, were their fellow Levites: Zechariah, Jaaziel, Shemiramoth, Jehiel, Unni, Eliab, Benaiah, Maaseiah, Mattithiah, Elipheleh, Mikneiah, Obed-edom, and Jeiel the gatekeepers.",
      "T": "Thirteen Levites of the second rank -- the corps of musicians supporting the three masters. Obed-edom appears here among them: the man in whose house the ark had rested for three months, now in the procession that brings it home. His name is woven through these chapters."
    },
    "19": {
      "L": "So the singers, Heman, Asaph, and Ethan, were appointed to sound with cymbals of brass;",
      "M": "The singers Heman, Asaph, and Ethan were appointed to sound bronze cymbals;",
      "T": "Heman, Asaph, and Ethan: the three masters at the bronze cymbals, the percussion that drives the rhythm of the whole ensemble."
    },
    "20": {
      "L": "And Zechariah, and Aziel, and Shemiramoth, and Jehiel, and Unni, and Eliab, and Maaseiah, and Benaiah, with psalteries on Alamoth;",
      "M": "Zechariah, Aziel, Shemiramoth, Jehiel, Unni, Eliab, Maaseiah, and Benaiah played lyres set to Alamoth;",
      "T": "Eight lyrists playing in the Alamoth mode -- probably the higher register, the soprano or treble tuning."
    },
    "21": {
      "L": "And Mattithiah, and Elipheleh, and Mikneiah, and Obededom, and Jeiel, and Azaziah, with harps on the Sheminith to excel.",
      "M": "Mattithiah, Elipheleh, Mikneiah, Obed-edom, Jeiel, and Azaziah played harps set to the Sheminith to lead.",
      "T": "Six harpists in the Sheminith -- the 'eighth,' probably the bass register, the lower, fuller tone. The full harmonic range: treble lyres, bass harps, percussion cymbals, voices. The procession of the ark was orchestrated."
    },
    "22": {
      "L": "And Chenaniah, chief of the Levites, was for song: he instructed about the song, because he was skilful.",
      "M": "Chenaniah, the chief of the Levites, was in charge of the music; he directed the music because he was skilful.",
      "T": "Chenaniah: the song-master. Not a performer so much as a director -- he oversaw the whole musical enterprise because he was genuinely skilled. The Chronicler's criterion for musical leadership is simply competence. Chenaniah was good at it."
    },
    "23": {
      "L": "And Berechiah and Elkanah were doorkeepers for the ark.",
      "M": "Berechiah and Elkanah were gatekeepers for the ark.",
      "T": "Berechiah and Elkanah as gatekeepers at the ark itself -- the guardians of the threshold, keeping the boundary between the holy object and the pressing crowd."
    },
    "24": {
      "L": "And Shebaniah, and Jehoshaphat, and Nethaneel, and Amasai, and Zechariah, and Benaiah, and Eliezer, the priests, did blow with the trumpets before the ark of God: and Obededom and Jehiah were doorkeepers for the ark.",
      "M": "Shebaniah, Joshaphat, Nethanel, Amasai, Zechariah, Benaiah, and Eliezer the priests were blowing the trumpets before the ark of God. Obed-edom and Jehiah also were gatekeepers for the ark.",
      "T": "Seven priests with trumpets walking before the ark -- the silver priestly trumpets of Numbers 10, prescribed for processions and holy assemblies. Obed-edom appears once more, now as a gatekeeper: in three verses he has moved from the man whose house blessed the ark to a formal officer of the ark's procession."
    },
    "25": {
      "L": "So David, and the elders of Israel, and the captains over thousands, went to bring up the ark of the covenant of the LORD out of the house of Obededom with joy.",
      "M": "So David, along with the elders of Israel and the commanders of thousands, went to bring up the ark of the covenant of the LORD from the house of Obed-edom with great joy.",
      "T": "The leaders lead: David himself, the elders of Israel, the commanders of thousands. The whole authority structure of the nation present for the procession. And they go with joy -- the same joy that characterises all of David's worship in Chronicles, and that will fill the completed psalm in chapter 16."
    },
    "26": {
      "L": "And it came to pass, when God helped the Levites that bare the ark of the covenant of the LORD, that they offered seven bullocks and seven rams.",
      "M": "Because God helped the Levites who were carrying the ark of the covenant of the LORD, they sacrificed seven bulls and seven rams.",
      "T": "God helped the Levites as they carried it. The help was evident -- the ark did not topple, no one died, the procession moved. In gratitude they stopped and offered seven bulls and seven rams -- a generous sacrifice, the number seven signalling completeness. The first time the procession was stopped by judgment; this time it is stopped by gratitude."
    },
    "27": {
      "L": "And David was clothed with a robe of fine linen, and all the Levites that bare the ark, and the singers, and Chenaniah the master of the song with the singers: David also had upon him an ephod of linen.",
      "M": "David was wearing a robe of fine linen, as were all the Levites who carried the ark, and the singers, and Chenaniah the song-master among the singers. David also wore a linen ephod.",
      "T": "The whole procession was robed in fine linen -- David, the ark-bearers, the singers, Chenaniah. And David wore a linen ephod: the priestly garment that signalled he was acting in a cultic capacity, not merely a royal one. He was not vesting himself as high priest -- he was not Levitically qualified -- but he was deliberately taking on the vestment of one drawing near to God. Michal will despise this. The narrative is setting up the contrast."
    },
    "28": {
      "L": "Thus all Israel brought up the ark of the covenant of the LORD with shouting, and with sound of the cornet, and with trumpets, and with cymbals, making a noise with psalteries and harps.",
      "M": "So all Israel brought up the ark of the covenant of the LORD with shouting, with the sound of the ram's horn, with trumpets, cymbals, and the loud music of lyres and harps.",
      "T": "All Israel: not just the Levites, not just the musicians, not just the commanders -- all Israel shouting and playing and processing. The ark of the covenant coming home to the city of David was the event of the generation."
    },
    "29": {
      "L": "And it came to pass, as the ark of the covenant of the LORD came to the city of David, that Michal the daughter of Saul looking out at a window saw king David dancing and playing: and she despised him in her heart.",
      "M": "As the ark of the covenant of the LORD came into the city of David, Michal daughter of Saul looked out through a window and saw King David dancing and celebrating, and she despised him in her heart.",
      "T": "Michal, daughter of Saul, looked out from a window -- the queen watching from behind glass what the people were experiencing in the street. She saw David dancing and celebrating, and she despised him. The Chronicler does not explain the contempt or resolve it here; he reports it as a shadow falling across the procession's joy. One heart, in the palace, was not of one heart with Israel."
    }
  },
  "16": {
    "1": {
      "L": "So they brought the ark of God, and set it in the midst of the tent that David had pitched for it: and they offered burnt sacrifices and peace offerings before God.",
      "M": "So they brought in the ark of God and set it inside the tent that David had pitched for it. They offered burnt offerings and peace offerings before God.",
      "T": "The ark is home. It is set in the centre of the tent David had prepared -- not the tabernacle at Gibeon but a new tent in Jerusalem, at the city's heart. Burnt offerings consumed entirely for God; peace offerings shared between God and people. The altar smoked; the covenant was intact."
    },
    "2": {
      "L": "And when David had made an end of offering the burnt offerings and the peace offerings, he blessed the people in the name of the LORD.",
      "M": "When David had finished offering the burnt offerings and the peace offerings, he blessed the people in the name of the LORD.",
      "T": "The king as priest -- or nearly. David blessed the people in the LORD's name when the sacrifices were finished. Not a priestly act in the technical sense, but a royal-priestly act on the model of Melchizedek: king and priest together, blessing the people from before God's presence."
    },
    "3": {
      "L": "And he dealt to every one of Israel, both man and woman, to every one a loaf of bread, and a good piece of flesh, and a flagon of wine.",
      "M": "He distributed to every Israelite man and woman a loaf of bread, a piece of meat, and a raisin cake.",
      "T": "Every Israelite -- man and woman, no exceptions -- received from the king's hand: a loaf of bread, a portion of roasted meat, a cake of pressed raisins. The king feeds the people from before God's tent. This is the covenant meal made universal: the whole nation eating together at David's table before the ark."
    },
    "4": {
      "L": "And he appointed certain of the Levites to minister before the ark of the LORD, and to record, and to thank and praise the LORD God of Israel:",
      "M": "He appointed certain Levites to minister before the ark of the LORD, to invoke, to give thanks, and to praise the LORD, the God of Israel.",
      "T": "David establishes a permanent liturgy. The Levites at the ark have three mandated functions: to invoke (call the people to remember), to give thanks, and to praise. These three movements -- memory, gratitude, adoration -- become the shape of Israel's worship before the presence of God."
    },
    "5": {
      "L": "Asaph the chief, and next to him Zechariah, Jeiel, and Shemiramoth, and Jehiel, and Mattithiah, and Eliab, and Benaiah, and Obededom: and Jeiel with psalteries and with harps; but Asaph made a sound with cymbals;",
      "M": "Asaph was the chief; next to him were Zechariah, Jeiel, Shemiramoth, Jehiel, Mattithiah, Eliab, Benaiah, and Obed-edom -- with harps and lyres. Asaph was to sound the cymbals.",
      "T": "The permanent roster at the Jerusalem tent: Asaph the chief, with eight fellow-Levites playing harps and lyres -- and Asaph himself at the cymbals, keeping the rhythm of the daily song."
    },
    "6": {
      "L": "Benaiah also and Jahaziel the priests with trumpets continually before the ark of the covenant of God.",
      "M": "The priests Benaiah and Jahaziel were to blow the trumpets continually before the ark of the covenant of God.",
      "T": "Two priests -- Benaiah and Jahaziel -- appointed to blow trumpets before the ark continually. Not once, not on festivals only: continually. The presence of God was not to be approached in silence."
    },
    "7": {
      "L": "Then on that day David delivered first this psalm to thank the LORD into the hand of Asaph and his brethren.",
      "M": "On that day David first appointed Asaph and his brothers to give thanks to the LORD with this psalm.",
      "T": "On the day the ark arrived, David gave Asaph a psalm. This is the Chronicler's first explicit record of David as poet-liturgist: the king handing the song-master a text to be sung before the LORD. The transition from procession to permanent worship begins with a psalm."
    },
    "8": {
      "L": "Give thanks unto the LORD; call upon his name: make known his deeds among the people.",
      "M": "Give thanks to the LORD; call upon his name; make known his deeds among the peoples!",
      "T": "Give thanks to the LORD;\ncall upon his name;\nmake known his deeds among the peoples!\nThe psalm opens with three imperatives, each building: gratitude, address, proclamation. Worship that stays private has not yet become complete -- it must overflow into testimony."
    },
    "9": {
      "L": "Sing unto him, sing psalms unto him, talk ye of all his wondrous works.",
      "M": "Sing to him, sing praises to him; tell of all his wondrous works!",
      "T": "Sing to him, sing praises to him;\ntell of all his wondrous works!\nSong and speech together -- the whole range of voice employed. Wondrous works: the acts of God in creation and history, the things that do not have natural explanations."
    },
    "10": {
      "L": "Glory ye in his holy name: let the heart of them rejoice that seek the LORD.",
      "M": "Glory in his holy name; let the hearts of those who seek the LORD rejoice!",
      "T": "Glory in his holy name --\nlet the hearts of those who seek the LORD rejoice!\nThe name is holy: it is the character of God made audible. To glory in the name is to find your joy in who God is, not merely in what he gives."
    },
    "11": {
      "L": "Seek the LORD and his strength, seek his face continually.",
      "M": "Seek the LORD and his strength; seek his presence continually!",
      "T": "Seek the LORD and his strength;\nseek his face continually!\nThe seeking is double: seek his power for the journey, seek his face for the relationship. And not once but continually -- the daily renewal of orientation toward God."
    },
    "12": {
      "L": "Remember his marvellous works that he hath done, his wonders, and the judgments of his mouth;",
      "M": "Remember the wondrous works that he has done, his miracles and the judgments he has uttered,",
      "T": "Remember his wondrous works that he has done,\nhis miracles and the judgments of his mouth --\nMemory is an act of worship. To remember what God has done is to refuse the amnesia of the present, to situate oneself in the long story of divine faithfulness."
    },
    "13": {
      "L": "O ye seed of Israel his servant, ye children of Jacob, his chosen ones.",
      "M": "O offspring of Israel his servant, children of Jacob, his chosen ones!",
      "T": "O offspring of Israel his servant,\nchildren of Jacob, his chosen ones!\nThe psalm addresses its congregation: you are Israel -- the servant-people, the chosen. The identity is not earned; it is received. But it carries obligation: to remember, to seek, to sing."
    },
    "14": {
      "L": "He is the LORD our God; his judgments are in all the earth.",
      "M": "He is the LORD our God; his judgments are in all the earth.",
      "T": "He is the LORD our God;\nhis judgments are in all the earth.\nNot just in Israel's territory -- in all the earth. The scope of the LORD's governance is universal. What looks like a national God is the God of every nation, whether they know it yet or not."
    },
    "15": {
      "L": "Be ye mindful always of his covenant; the word which he commanded to a thousand generations;",
      "M": "Remember his covenant forever, the word he commanded for a thousand generations --",
      "T": "Remember his covenant forever,\nthe word he commanded for a thousand generations --\nA thousand generations: the covenant is not bounded by the span of any single nation's life. It was made before Israel existed and reaches forward past Israel's horizon."
    },
    "16": {
      "L": "Even of the covenant which he made with Abraham, and of his oath unto Isaac;",
      "M": "the covenant he made with Abraham, his sworn oath to Isaac,",
      "T": "the covenant he made with Abraham,\nhis sworn oath to Isaac --\nThe covenant has a history: Abraham first, then confirmed to Isaac. The oath-structure matters: God bound himself with an oath, the strongest form of commitment available to a moral being."
    },
    "17": {
      "L": "And hath confirmed the same to Jacob for a law, and to Israel for an everlasting covenant,",
      "M": "which he confirmed to Jacob as a statute, to Israel as an everlasting covenant,",
      "T": "which he confirmed to Jacob as a statute,\nto Israel as an everlasting covenant --\nConfirmed: not invented fresh at each generation but ratified again. The word means the covenant was already in place and was being re-established. Everlasting: without a foreseeable end."
    },
    "18": {
      "L": "Saying, Unto thee will I give the land of Canaan, the lot of your inheritance:",
      "M": "saying, 'To you I will give the land of Canaan as your portion for an inheritance.'",
      "T": "saying: 'To you I will give the land of Canaan\nas your allotted inheritance.'\nThe content of the covenant: land. Specific land. The lot -- the portion assigned by divine decision. When the psalm is sung before the ark in Jerusalem, Israel is standing on the fulfilment of this promise."
    },
    "19": {
      "L": "When ye were but few, even a few, and strangers in it.",
      "M": "When you were few in number, of little account, and strangers in the land,",
      "T": "When you were few in number,\nhardly a handful,\nstrangers in the land --\nThe contrast is deliberate: then, a family of wanderers; now, a nation in its own territory. The psalm invites Israel to stand in the gap between those two moments and feel the distance that grace has covered."
    },
    "20": {
      "L": "And when they went from nation to nation, and from one kingdom to another people;",
      "M": "when they wandered from nation to nation, from one kingdom to another people,",
      "T": "wandering from nation to nation,\nfrom one kingdom to another people --\nThe patriarchal wanderings: Abraham to Egypt, to Canaan, to the Negev; Jacob to Paddan-aram, back to Canaan, down to Egypt. The family of the promise was a family of perpetual displacement."
    },
    "21": {
      "L": "He suffered no man to do them wrong: yea, he reproved kings for their sakes;",
      "M": "he allowed no one to oppress them; he rebuked kings on their account,",
      "T": "he allowed no one to oppress them;\nhe rebuked kings for their sake --\nEven in their weakness and wandering, God was their guardian. Pharaoh was rebuked; Abimelech was warned in a dream. The kings of the earth could not touch the patriarch without touching God's purpose."
    },
    "22": {
      "L": "Saying, Touch not mine anointed, and do my prophets no harm.",
      "M": "saying, 'Touch not my anointed ones; do my prophets no harm!'",
      "T": "'Touch not my anointed ones;\ndo my prophets no harm!'\nThe patriarchs as anointed ones -- not by oil but by covenant; prophets -- not by office but by the word God spoke through them. The identity is gift, not achievement."
    },
    "23": {
      "L": "Sing unto the LORD, all the earth; shew forth from day to day his salvation.",
      "M": "Sing to the LORD, all the earth! Proclaim his salvation from day to day.",
      "T": "Sing to the LORD, all the earth!\nProclaim his salvation from day to day.\nThe scope expands from Israel to all the earth. What began as covenant memory becomes missionary proclamation: tell the nations what God has done. Every day, the same news, freshly told."
    },
    "24": {
      "L": "Declare his glory among the heathen; his marvellous works among all nations.",
      "M": "Declare his glory among the nations, his marvellous works among all peoples!",
      "T": "Declare his glory among the nations,\nhis marvellous works among all peoples!\nGlory -- the weight and brightness of who God is -- to be declared outside Israel's borders. The marvellous works are not Israel's private possession; they are evidence for the whole world."
    },
    "25": {
      "L": "For great is the LORD, and greatly to be praised: he also is to be feared above all gods.",
      "M": "For great is the LORD, and greatly to be praised; he is to be feared above all gods.",
      "T": "For great is the LORD, and greatly to be praised;\nhe is to be feared above all gods.\nThe comparison is not between equals. The gods are real presences in their cultures; but the LORD is of a different order entirely. To fear him above the gods is to locate him outside the category of deity-as-usual."
    },
    "26": {
      "L": "For all the gods of the people are idols: but the LORD made the heavens.",
      "M": "For all the gods of the peoples are idols, but the LORD made the heavens.",
      "T": "For all the gods of the peoples are idols --\nbut the LORD made the heavens.\nThe contrast is total. The gods are elilim -- nonentities, nothings, carved shapes without power. The LORD made the substance in which all the gods' shrines sit. Creator and creature are not comparable."
    },
    "27": {
      "L": "Glory and honour are in his presence; strength and gladness are in his place.",
      "M": "Splendour and majesty are before him; strength and joy are in his dwelling place.",
      "T": "Splendour and majesty are before him;\nstrength and joy are in his dwelling place.\nThe four attributes surrounding the divine presence: splendour (the outward beauty), majesty (the sovereign weight), strength (the power that sustains), and joy (the delight that overflows). These are not decorations; they are what the holy place radiates."
    },
    "28": {
      "L": "Give unto the LORD, ye kindreds of the people, give unto the LORD glory and strength.",
      "M": "Ascribe to the LORD, O families of the peoples, ascribe to the LORD glory and strength!",
      "T": "Ascribe to the LORD, O families of the peoples,\nascribe to the LORD glory and strength!\nThe nations are addressed again: not commanded to convert but to ascribe -- to acknowledge what is already true. The LORD's glory and strength exist whether the nations name them or not; the call is to name them."
    },
    "29": {
      "L": "Give unto the LORD the glory due unto his name: bring an offering, and come before him: worship the LORD in the beauty of holiness.",
      "M": "Ascribe to the LORD the glory due his name; bring an offering and come before him. Worship the LORD in the splendour of holiness.",
      "T": "Ascribe to the LORD the glory his name is owed;\nbring an offering and come before him;\nworship the LORD in the splendour of holiness.\nThe three movements of approach: acknowledgment of who God is, offering brought, worship performed. Holiness is the atmosphere of the divine presence -- its beauty is not aesthetic decoration but the overwhelming reality of the sacred."
    },
    "30": {
      "L": "Fear before him, all the earth: the world also shall be stable, that it be not moved.",
      "M": "Tremble before him, all the earth! The world is firmly established; it cannot be moved.",
      "T": "Tremble before him, all the earth!\nThe world is firmly established -- it cannot be moved.\nThe call to tremble is not terror but the appropriate awe of a creature before its Creator. And the earth is stable because God holds it: the cosmos does not shake because its Maker does not change."
    },
    "31": {
      "L": "Let the heavens be glad, and let the earth rejoice: and let men say among the nations, The LORD reigneth.",
      "M": "Let the heavens be glad, and let the earth rejoice, and let them say among the nations, 'The LORD reigns!'",
      "T": "Let the heavens be glad,\nand let the earth rejoice;\nlet them say among the nations: The LORD reigns!\nThe cosmic choir and the human proclamation together. The heavens and the earth are not passive scenery; they are participants in the praise. And the proclamation 'The LORD reigns' is the centre of everything: the psalm's thesis, Israel's creed, creation's testimony."
    },
    "32": {
      "L": "Let the sea roar, and the fulness thereof: let the fields rejoice, and all that is therein.",
      "M": "Let the sea roar and all it contains; let the fields exult and all that is in them!",
      "T": "Let the sea roar and all that fills it;\nlet the fields exult and everything in them!\nThe sea, which in ancient imagination was both beautiful and threatening; the fields in their harvest-fullness -- both categories of creation summoned to the choir. Nothing in the natural world is excluded from the praise."
    },
    "33": {
      "L": "Then shall the trees of the wood sing out at the presence of the LORD, because he cometh to judge the earth.",
      "M": "Then shall the trees of the forest sing for joy before the LORD, for he comes to judge the earth.",
      "T": "Then shall the trees of the forest sing for joy\nbefore the LORD -- for he comes to judge the earth.\nThe trees singing is not metaphor decorating a small truth; it is the Chronicler's way of saying that the coming of the LORD to judge transforms even the inanimate into worshippers. Judgment here is not punishment primarily but the establishment of justice -- the setting-right of all that has been wrong."
    },
    "34": {
      "L": "O give thanks unto the LORD; for he is good; for his mercy endureth for ever.",
      "M": "Oh give thanks to the LORD, for he is good; for his steadfast love endures forever!",
      "T": "Oh give thanks to the LORD, for he is good;\nfor his steadfast love endures forever!\nThe hinge of the psalm: hesed, the covenant loyalty that is also active kindness, the word that has no English equivalent. It endures forever. This is the theological spine on which all the praise hangs: God is good, and his goodness is not occasional but permanent."
    },
    "35": {
      "L": "And say ye, Save us, O God of our salvation, and gather us together, and deliver us from the heathen, that we may give thanks to thy holy name, and glory in thy praise.",
      "M": "Say also: 'Save us, O God of our salvation; gather us and deliver us from among the nations, so that we may give thanks to your holy name and glory in your praise.'",
      "T": "Say also:\n'Save us, O God of our salvation!\nGather us and deliver us from among the nations,\nthat we may give thanks to your holy name\nand glory in your praise!'\nThe psalm does not pretend Israel is already in the final state. Exile is real; scattering is real; deliverance is still needed. The Chronicler places this petition in David's mouth before the exile -- which means when the Chronicler's original audience heard it, they heard it as the prayer of their own moment."
    },
    "36": {
      "L": "Blessed be the LORD God of Israel for ever and ever. And all the people said, Amen, and praised the LORD.",
      "M": "Blessed be the LORD, the God of Israel, from everlasting to everlasting! And all the people said, 'Amen!' and praised the LORD.",
      "T": "Blessed be the LORD, the God of Israel,\nfrom everlasting to everlasting!\nAnd all the people said, 'Amen!' and praised the LORD.\nThe doxology and the congregational response. The psalm that began with 'Give thanks to the LORD' ends with the people giving thanks. The circle closes. Every voice that could speak spoke; every heart that could praise praised. The ark was home."
    },
    "37": {
      "L": "So he left there before the ark of the covenant of the LORD Asaph and his brethren, to minister before the ark continually, as every day's work required:",
      "M": "David left Asaph and his brothers there before the ark of the covenant of the LORD to minister regularly before the ark, as each day required.",
      "T": "The great celebration ends; the regular order begins. Asaph and his brothers are established at the ark for the daily ministry -- not an occasional performance but the permanent rhythm of worship, each day its own requirement. The Chronicler's David is above all else the king who set worship on its permanent footing."
    },
    "38": {
      "L": "And Obededom with their brethren, threescore and eight; Obededom also the son of Jeduthun and Hosah to be porters:",
      "M": "Also Obed-edom with their kinsmen, sixty-eight of them; and Obed-edom son of Jeduthun and Hosah were to be gatekeepers.",
      "T": "Obed-edom one final time: sixty-eight men under him, and he himself appointed gatekeeper at the ark's tent -- the man whose house had sheltered the ark for three months now serving as its permanent guardian. The continuity is the Chronicler's theology in miniature: faithfulness maintained is faithfulness rewarded with greater access."
    },
    "39": {
      "L": "And Zadok the priest, and his brethren the priests, before the tabernacle of the LORD in the high place that was at Gibeon,",
      "M": "David also left Zadok the priest and his brothers the priests before the tabernacle of the LORD at the high place at Gibeon,",
      "T": "A parallel worship arrangement: Zadok and his priestly brothers remain at Gibeon, where the tabernacle of Moses still stood. Jerusalem has the ark but no tabernacle; Gibeon has the tabernacle but no ark. The two centres of worship -- split by David's arrangements -- will not be reunited until Solomon builds the temple. For now, Israel worships in two places at once."
    },
    "40": {
      "L": "To offer burnt offerings unto the LORD upon the altar of the burnt offering continually morning and evening, and to do according to all that is written in the law of the LORD, which he commanded Israel;",
      "M": "to offer burnt offerings to the LORD on the altar of burnt offering continually, morning and evening, and to do according to all that is written in the Law of the LORD that he commanded Israel.",
      "T": "The morning and evening burnt offering: the tamid, the daily sacrifice prescribed in Numbers 28:3-8, the heartbeat of the Mosaic cult. Zadok keeps it going at Gibeon while Asaph keeps the psalms going at Jerusalem. Law and praise, two pulses of the one worship."
    },
    "41": {
      "L": "And with them Heman and Jeduthun, and the rest that were chosen, who were expressed by name, to give thanks to the LORD, because his mercy endureth for ever;",
      "M": "With them were Heman and Jeduthun and the rest of those chosen and designated by name to give thanks to the LORD, for his steadfast love endures forever.",
      "T": "Heman and Jeduthun at Gibeon, named and designated -- echoing the psalm's refrain: 'his steadfast love endures forever.' The refrain is not only for the ark-tent in Jerusalem; it is the watchword of the whole Israelite cult, repeated morning and evening at both worship sites. Hesed never stops being true; the worship that names it never stops either."
    },
    "42": {
      "L": "And with them Heman and Jeduthun with trumpets and cymbals for those that should make a sound, and with musical instruments of God. And the sons of Jeduthun were porters.",
      "M": "Heman and Jeduthun had trumpets and cymbals for the music and instruments for sacred song. The sons of Jeduthun were appointed to the gate.",
      "T": "Trumpets and cymbals at Gibeon, as at Jerusalem -- the same sound in both places. And Jeduthun's sons at the gate, continuing the family's service. The Chronicler closes the liturgical arrangements with this detail of continuity: every post filled, every gate guarded, the worship of God ordered and permanent."
    },
    "43": {
      "L": "And all the people departed every man to his house: and David returned to bless his household.",
      "M": "Then all the people departed, each to his own house, and David returned to bless his household.",
      "T": "The great day ends as all days end: the people go home. David goes home. The extraordinary becomes ordinary again, as it must -- the ark in its place, the worship established, the covenant renewed. And David, having blessed the nation, goes to bless his own household. The king who built the altar also tends his family. The private and the public, worship and home, held together in the last verse of the day."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, '1chronicles')
        merge_tier(existing, CHRONICLES1, tier_key)
        save(tier_dir, '1chronicles', existing)
    print('1 Chronicles 11-16 written.')

if __name__ == '__main__':
    main()
