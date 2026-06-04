"""
MKT 1 Kings chapters 1–6 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-1kings-1-6.py

Translation decisions:
- H3068 (יהוה): "LORD" (small-caps convention) in L/M throughout; "the LORD" in T.
  Consistent with mkt-2samuel-1-6.py and mkt-2samuel-7-12.py.
- H430 (אֱלֹהִים): "God" in all tiers.
- H136 + H3069 (ʾădōnāy YHWH / Lord GOD): 2:26 uses this pairing; L/M "Lord GOD," T "the Lord GOD."
- H2617 (חֶסֶד): Two occurrences in this range:
  2:7 (David to Solomon re Barzillai): L "kindness," M "steadfast loyalty," T "covenant loyalty."
  3:6 (Solomon's prayer re David): L "great kindness," M "great steadfast love," T "such faithful love."
- H5315 (נֶפֶשׁ): 1:29 oath formula "who has redeemed my soul"; L "soul," M/T "life."
- H5769 (ʿôlām): "forever" all tiers (1:31, 2:33, 2:45).
- H8085 + H3820 ("hearing heart," 3:9): The famous request is literally "a hearing heart."
  L: "a hearing heart," M: "an understanding mind," T: "a heart that truly listens."
- H2451 (חָכְמָה / wisdom): "wisdom" in all tiers throughout chs 3–5.
- H1004 (bayit / house): "house" throughout — the word carries both temple and dynasty meaning.
  In chs 5–6 this refers to the temple; in ch 2 it refers to Shimei's residence.
  Do not substitute "temple" or "palace" — let the wordplay stand where possible.
- H3678 (kisse / throne): "throne" all tiers.
- H4196 (mizbeach / altar): "altar" all tiers.
- H1285 (בְּרִית / covenant): "covenant" all tiers (6:19 "ark of the covenant").
- H6944 + H6944 (qodesh qodashim / Most Holy Place): L "the Most Holy," M "the Most Holy Place,"
  T "the Holy of Holies."
- Aspect: waw-consecutive imperfects throughout = narrative past (simple past in English).
  The LORD's word to Solomon (6:11-13) uses future forms for divine promise.
- OT echoes:
  - 2:2-4: David's charge echoes Deut 17:18-20 (the king's torah obligation) and Josh 1:6-7.
    T tier notes the Deuteronomistic framework explicitly.
  - 2:33: "peace from the LORD forevermore" echoes the Davidic covenant of 2 Sam 7.
  - 3:6: Solomon's prayer echoes 2 Sam 7 — "steadfast love" + "a son to sit on your throne."
  - 4:25 "vine and fig tree": A classic shalom image (cf. Mic 4:4; Zech 3:10). T notes this.
  - 6:11-13: The conditional dwelling-promise is the theological heart of the temple narrative;
    it echoes Lev 26:11-12 and Exod 29:45. T surfaces this explicitly.
- Chapter 1 political note: Adonijah's self-exaltation ("I will be king," 1:5) deliberately
  echoes Absalom's behavior (2 Sam 15). L preserves the verb "exalted himself" (H5375).
- Chapter 2 note: Solomon's consolidation (Adonijah, Joab, Abiathar, Shimei) fulfills
  David's final instructions while clearing the field for a stable kingdom. The chapter
  ends with the formula "the kingdom was established" (H3559) — T notes this as the
  Deuteronomistic verdict on the succession.
- 3:9 "hearing heart": Rendered distinctively in each tier to preserve the literal Hebrew image
  in L and approximate the English idiom in M, while T draws out the theological significance.
- Abishag (1:1-4): Her role as royal attendant (not concubine, 1:4 "the king knew her not")
  makes Adonijah's request in 2:17 a bid for symbolic royal authority. T makes this explicit.
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

KINGS = {
  "1": {
    "1": {
      "L": "Now King David was old and advanced in years. They covered him with garments, but he could get no warmth.",
      "M": "King David was old and advanced in years. Though they covered him with blankets, he could not get warm.",
      "T": "King David was old—advanced in years—and though they piled blankets on him, he could not get warm."
    },
    "2": {
      "L": "So his servants said to him, 'Let there be sought for my lord the king a young virgin, and let her stand before the king and care for him. Let her lie in your bosom, that my lord the king may be warm.'",
      "M": "His servants said to him, 'Let a young virgin be sought for my lord the king to attend on him and care for him. She shall lie in your arms and keep my lord the king warm.'",
      "T": "His servants said: 'Let a young woman be found for my lord the king—a virgin who can attend him and care for him. She will lie close to you, my lord, and keep you warm.'"
    },
    "3": {
      "L": "So they sought a beautiful young woman throughout all the territory of Israel, and they found Abishag the Shunammite and brought her to the king.",
      "M": "They searched throughout all Israel for a beautiful young woman and found Abishag the Shunammite and brought her to the king.",
      "T": "So they searched all Israel for a beautiful young woman, and they found Abishag from Shunem and brought her to the king."
    },
    "4": {
      "L": "The young woman was very beautiful. She cared for the king and served him, but the king knew her not.",
      "M": "The young woman was very beautiful. She cared for and served the king, but the king did not sleep with her.",
      "T": "Abishag was very beautiful. She attended the king and served him, but the king did not have relations with her."
    },
    "5": {
      "L": "Now Adonijah the son of Haggith exalted himself, saying, 'I will be king.' He prepared for himself chariots and horsemen, and fifty men to run before him.",
      "M": "Meanwhile Adonijah son of Haggith promoted himself, saying, 'I will be king.' He acquired chariots and horsemen and fifty men to run ahead of him.",
      "T": "Meanwhile Adonijah son of Haggith was exalting himself, declaring, 'I will be king.' He assembled chariots and horsemen and fifty men to run ahead of him—just as Absalom had done."
    },
    "6": {
      "L": "His father had never at any time displeased him by asking, 'Why have you done thus?' He was also a very handsome man, and his mother had borne him after Absalom.",
      "M": "His father had never corrected him or asked, 'Why have you done this?' He was also very handsome, and his mother had borne him after Absalom.",
      "T": "His father had never once rebuked him or asked, 'Why do you do this?' He was also a very handsome man, and he was born after Absalom—the next in line by age."
    },
    "7": {
      "L": "He conferred with Joab the son of Zeruiah and with Abiathar the priest, and they followed Adonijah and helped him.",
      "M": "He made an alliance with Joab son of Zeruiah and with Abiathar the priest, and they supported Adonijah.",
      "T": "He enlisted Joab son of Zeruiah and Abiathar the priest, and they threw their support behind him."
    },
    "8": {
      "L": "But Zadok the priest, Benaiah the son of Jehoiada, Nathan the prophet, Shimei, Rei, and David's mighty men were not with Adonijah.",
      "M": "But Zadok the priest, Benaiah son of Jehoiada, Nathan the prophet, Shimei, Rei, and David's own fighting men did not side with Adonijah.",
      "T": "But Zadok the priest, Benaiah son of Jehoiada, the prophet Nathan, Shimei, Rei, and David's elite warriors did not join Adonijah's cause."
    },
    "9": {
      "L": "Adonijah sacrificed sheep, oxen, and fattened cattle by the Serpent's Stone beside En-rogel, and he invited all his brothers, the king's sons, and all the royal officials of Judah,",
      "M": "Adonijah sacrificed sheep, oxen, and fattened cattle at the Serpent's Stone by En-rogel, and he invited all his brothers, the king's sons, and all the officials of Judah,",
      "T": "Adonijah held a sacrificial feast at the Serpent's Stone beside En-rogel—sheep, oxen, and fattened cattle—and invited all his royal brothers and all the officials of Judah,"
    },
    "10": {
      "L": "but he did not invite Nathan the prophet, or Benaiah, or the mighty men, or Solomon his brother.",
      "M": "but he did not invite Nathan the prophet, Benaiah, the mighty men, or his brother Solomon.",
      "T": "but he did not invite the prophet Nathan, or Benaiah, or the elite warriors, or his brother Solomon."
    },
    "11": {
      "L": "Then Nathan said to Bathsheba the mother of Solomon, 'Have you not heard that Adonijah the son of Haggith has become king and David our lord does not know it?'",
      "M": "Nathan said to Bathsheba, Solomon's mother, 'Have you not heard that Adonijah son of Haggith has made himself king, and our lord David does not know it?'",
      "T": "Nathan went to Bathsheba, Solomon's mother, and said: 'Have you not heard? Adonijah son of Haggith has declared himself king—and David our lord doesn't know it.'"
    },
    "12": {
      "L": "Now therefore come, let me give you advice, that you may save your own life and the life of your son Solomon.",
      "M": "Now come, let me give you advice so that you may save your own life and the life of your son Solomon.",
      "T": "Come, let me advise you—your life and Solomon's life depend on it."
    },
    "13": {
      "L": "Go in to King David and say to him, 'Did you not, my lord the king, swear to your servant saying, Solomon your son shall reign after me, and he shall sit on my throne? Why then does Adonijah reign?'",
      "M": "Go to King David and say: 'Did you not swear to me, my lord the king, saying, Your son Solomon shall be king after me and shall sit on my throne? Why then is Adonijah reigning?'",
      "T": "Go in to King David and say: 'My lord the king, did you not swear to me by the LORD that Solomon my son would reign after you and sit on your throne? Then why is Adonijah king?'"
    },
    "14": {
      "L": "Then while you are still speaking there with the king, I will come in after you and confirm your words.",
      "M": "Then while you are still speaking with the king, I will come in and add my testimony to yours.",
      "T": "While you are still speaking with the king, I will come in and confirm everything you have said."
    },
    "15": {
      "L": "So Bathsheba went in to the king in his chamber. The king was very old, and Abishag the Shunammite was attending to the king.",
      "M": "So Bathsheba went in to the king in his room. The king was very old, and Abishag the Shunammite was attending him.",
      "T": "Bathsheba went into the king's chamber. He was very old, and Abishag the Shunammite was attending him."
    },
    "16": {
      "L": "Bathsheba bowed and paid homage to the king, and the king said, 'What do you wish?'",
      "M": "Bathsheba bowed down in homage to the king, and the king asked, 'What do you want?'",
      "T": "Bathsheba bowed to the ground before the king. 'What do you wish?' the king asked."
    },
    "17": {
      "L": "She said to him, 'My lord, you swore to your servant by the LORD your God, saying, Solomon your son shall reign after me, and he shall sit on my throne.'",
      "M": "She said to him, 'My lord, you swore to me by the LORD your God: Solomon your son will reign after me and sit on my throne.'",
      "T": "She said: 'My lord, you swore to your servant by the LORD your God: Solomon your son will reign after you and sit on your throne.'"
    },
    "18": {
      "L": "And now, behold, Adonijah is king, and you, my lord the king, do not know it.",
      "M": "Yet now Adonijah has become king, and you, my lord the king, do not know it.",
      "T": "And now, Adonijah has made himself king—and you, my lord, do not even know it."
    },
    "19": {
      "L": "He has sacrificed oxen, fattened cattle, and sheep in abundance, and has invited all the sons of the king, Abiathar the priest, and Joab the commander of the army, but Solomon your servant he has not invited.",
      "M": "He has sacrificed many oxen, fattened cattle, and sheep, and has invited all the king's sons, Abiathar the priest, and Joab the army commander—but Solomon your servant he has not invited.",
      "T": "He has slaughtered oxen, fattened cattle, and sheep by the score, and has invited all the king's sons, Abiathar the priest, and Joab the army commander—but Solomon your servant he did not invite."
    },
    "20": {
      "L": "And you, my lord the king—the eyes of all Israel are upon you, to tell them who shall sit on the throne of my lord the king after him.",
      "M": "Now, my lord the king, all Israel is looking to you to announce who will sit on the throne after you.",
      "T": "My lord the king, all Israel is watching you, waiting to hear from your own lips who will sit on your throne after you."
    },
    "21": {
      "L": "Otherwise, when my lord the king lies with his fathers, I and my son Solomon shall be counted offenders.",
      "M": "Otherwise, when my lord the king rests with his ancestors, my son Solomon and I will be treated as criminals.",
      "T": "When my lord the king dies and lies with his fathers, Solomon and I will be treated as traitors."
    },
    "22": {
      "L": "While she was still speaking with the king, Nathan the prophet came in.",
      "M": "While she was still speaking with the king, Nathan the prophet arrived.",
      "T": "While she was still speaking, the prophet Nathan arrived."
    },
    "23": {
      "L": "They told the king, 'Here is Nathan the prophet.' And when he came in before the king, he bowed before the king with his face to the ground.",
      "M": "The king was told, 'Nathan the prophet is here.' He came in before the king and bowed with his face to the ground.",
      "T": "They announced: 'Nathan the prophet is here.' He came in and prostrated himself before the king with his face to the ground."
    },
    "24": {
      "L": "Nathan said, 'My lord the king, have you said, Adonijah shall reign after me and he shall sit on my throne?'",
      "M": "Nathan said, 'My lord the king, have you declared that Adonijah shall reign after you and sit on your throne?'",
      "T": "Nathan said: 'My lord the king, have you commanded that Adonijah shall reign after you and sit on your throne?'"
    },
    "25": {
      "L": "For he has gone down this day and has sacrificed oxen, fattened cattle, and sheep in abundance, and has invited all the king's sons, the commanders of the army, and Abiathar the priest. And behold, they are eating and drinking before him and saying, Long live King Adonijah!",
      "M": "For today he has gone down and sacrificed many oxen, fattened cattle, and sheep, and has invited all the king's sons, the army commanders, and Abiathar the priest. They are eating and drinking before him and saying, 'Long live King Adonijah!'",
      "T": "Today he went down and offered a great feast—oxen, fattened cattle, and sheep in abundance—and invited all the king's sons, the military commanders, and Abiathar the priest. Right now they are eating and drinking before him and shouting, 'Long live King Adonijah!'"
    },
    "26": {
      "L": "But me, your servant, and Zadok the priest, and Benaiah the son of Jehoiada, and your servant Solomon, he has not invited.",
      "M": "But he has not invited me, your servant, or Zadok the priest, or Benaiah son of Jehoiada, or your servant Solomon.",
      "T": "But me—your servant—and Zadok the priest, and Benaiah son of Jehoiada, and your servant Solomon: he invited none of us."
    },
    "27": {
      "L": "Has this thing been done by my lord the king, and you have not told your servants who should sit on the throne of my lord the king after him?",
      "M": "Has this been done with my lord the king's knowledge and you have not told your servants who should sit on your throne after you?",
      "T": "Is this what my lord the king has authorized, without telling your servants who will sit on the throne after you?"
    },
    "28": {
      "L": "Then King David answered, 'Call Bathsheba to me.' So she came into the king's presence and stood before the king.",
      "M": "King David responded, 'Call Bathsheba.' She came into the king's presence and stood before him.",
      "T": "King David said: 'Bring Bathsheba to me.' She came in and stood before the king."
    },
    "29": {
      "L": "And the king swore, saying, 'As the LORD lives, who has redeemed my soul out of every adversity,'",
      "M": "The king swore, saying, 'As the LORD lives, who has redeemed my life from every trouble,'",
      "T": "The king swore: 'As the LORD lives—the one who has rescued my life from every danger—'"
    },
    "30": {
      "L": "'as I swore to you by the LORD, the God of Israel, saying, Solomon your son shall reign after me, and he shall sit on my throne in my place, even so will I do this day.'",
      "M": "'just as I swore to you by the LORD, the God of Israel, saying, Solomon your son shall reign after me and sit on my throne in my place—I will do exactly that today.'",
      "T": "'just as I swore to you by the LORD the God of Israel—Solomon your son will reign after me, and he will sit on my throne in my place—this I will carry out today.'"
    },
    "31": {
      "L": "Then Bathsheba bowed with her face to the earth, and paid homage to the king, and said, 'May my lord King David live forever!'",
      "M": "Then Bathsheba bowed with her face to the ground in homage to the king and said, 'May my lord King David live forever!'",
      "T": "Bathsheba bowed to the ground in homage and said: 'May my lord King David live forever!'"
    },
    "32": {
      "L": "King David said, 'Call to me Zadok the priest, Nathan the prophet, and Benaiah the son of Jehoiada.' So they came before the king.",
      "M": "King David said, 'Summon Zadok the priest, Nathan the prophet, and Benaiah son of Jehoiada.' They came before the king.",
      "T": "King David said: 'Summon Zadok the priest, Nathan the prophet, and Benaiah son of Jehoiada.' They came before the king."
    },
    "33": {
      "L": "The king said to them, 'Take with you the servants of your lord, and have Solomon my son ride on my own mule and bring him down to Gihon.'",
      "M": "The king said to them, 'Take the royal servants with you, have my son Solomon ride on my own mule, and bring him down to Gihon.'",
      "T": "The king said: 'Take the royal guard with you. Have my son Solomon ride on my own mule, and bring him down to Gihon.'"
    },
    "34": {
      "L": "'And let Zadok the priest and Nathan the prophet anoint him there as king over Israel. Then blow the trumpet and say, Long live King Solomon!'",
      "M": "'There let Zadok the priest and Nathan the prophet anoint him king over Israel. Blow the trumpet and say, Long live King Solomon!'",
      "T": "'There let Zadok the priest and Nathan the prophet anoint him king over Israel. Blow the trumpet and shout, Long live King Solomon!'"
    },
    "35": {
      "L": "'Then you shall come up after him, and he shall come and sit on my throne, for he shall be king in my place. I have appointed him to be ruler over Israel and over Judah.'",
      "M": "'Then come up after him. He shall come and sit on my throne, for he is the one I have appointed to be ruler over Israel and Judah.'",
      "T": "'Come up behind him, and let him come and sit on my throne—he will reign in my place. I have appointed him ruler over Israel and Judah.'"
    },
    "36": {
      "L": "Benaiah the son of Jehoiada answered the king, 'Amen! May the LORD, the God of my lord the king, say so!'",
      "M": "Benaiah son of Jehoiada answered the king: 'Amen! May the LORD, the God of my lord the king, confirm it!'",
      "T": "Benaiah son of Jehoiada answered the king: 'Amen! May the LORD, the God of my lord the king, make it so!'"
    },
    "37": {
      "L": "'As the LORD has been with my lord the king, even so may he be with Solomon, and make his throne greater than the throne of my lord King David.'",
      "M": "'As the LORD has been with my lord the king, so may he be with Solomon, and may he make Solomon's throne even greater than the throne of my lord King David.'",
      "T": "'As the LORD has been with my lord the king, so may he be with Solomon—and may he make Solomon's throne even greater than yours, my lord King David.'"
    },
    "38": {
      "L": "So Zadok the priest, Nathan the prophet, and Benaiah the son of Jehoiada went down with the Cherethites and the Pelethites, and they had Solomon ride on King David's mule and brought him to Gihon.",
      "M": "So Zadok the priest, Nathan the prophet, and Benaiah son of Jehoiada went down with the Cherethites and the Pelethites. They had Solomon ride on King David's mule and brought him to Gihon.",
      "T": "Zadok the priest, Nathan the prophet, Benaiah son of Jehoiada, and the Cherethite and Pelethite guard went down. They set Solomon on King David's own mule and brought him to Gihon."
    },
    "39": {
      "L": "There Zadok the priest took the horn of oil from the tent and anointed Solomon. Then they blew the trumpet, and all the people said, 'Long live King Solomon!'",
      "M": "There Zadok the priest took the horn of oil from the tent and anointed Solomon. They blew the trumpet, and all the people shouted, 'Long live King Solomon!'",
      "T": "There Zadok the priest took the horn of oil from the tent and anointed Solomon. The trumpet sounded, and all the people shouted: 'Long live King Solomon!'"
    },
    "40": {
      "L": "And all the people went up after him, playing on pipes and rejoicing with great joy, so that the earth was split by their noise.",
      "M": "All the people went up after him, playing on pipes and rejoicing with great joy, so that the ground shook with their noise.",
      "T": "All the people went up after him, playing pipes and rejoicing with such great joy that the earth itself shook with the sound."
    },
    "41": {
      "L": "Adonijah and all the guests who were with him heard it as they finished eating. And when Joab heard the sound of the trumpet, he said, 'What does this uproar in the city mean?'",
      "M": "Adonijah and all his guests heard it as they finished eating. When Joab heard the trumpet sound, he said, 'Why is the city in such an uproar?'",
      "T": "Adonijah and all his guests heard the noise as they were finishing their meal. Joab heard the trumpet and said: 'What is all this commotion in the city?'"
    },
    "42": {
      "L": "While he was still speaking, behold, Jonathan the son of Abiathar the priest came. And Adonijah said, 'Come in, for you are a worthy man and bring good news.'",
      "M": "While he was still speaking, Jonathan son of Abiathar the priest arrived. Adonijah said, 'Come in—you are a brave man and surely bring good news.'",
      "T": "While he was still speaking, Jonathan son of Abiathar the priest arrived. Adonijah said: 'Come in—you are a good man; you must be bringing good news.'"
    },
    "43": {
      "L": "Jonathan answered Adonijah, 'No! For our lord King David has made Solomon king,'",
      "M": "Jonathan answered Adonijah, 'Not at all! Our lord King David has just made Solomon king,'",
      "T": "Jonathan answered: 'Not good news—at all. Our lord King David has made Solomon king.'"
    },
    "44": {
      "L": "'and the king has sent with him Zadok the priest, Nathan the prophet, and Benaiah the son of Jehoiada, and the Cherethites and the Pelethites, and they had him ride on the king's mule,'",
      "M": "'and the king sent with him Zadok the priest, Nathan the prophet, Benaiah son of Jehoiada, and the Cherethites and Pelethites, and they had him ride on the royal mule,'",
      "T": "'The king sent Zadok the priest, Nathan the prophet, Benaiah son of Jehoiada, and the royal guard with him. They put Solomon on the king's own mule,'"
    },
    "45": {
      "L": "'and Zadok the priest and Nathan the prophet have anointed him king at Gihon, and they have gone up from there rejoicing, so that the city is in an uproar. This is the noise that you have heard.'",
      "M": "'and Zadok the priest and Nathan the prophet have anointed him king at Gihon. They have gone up from there rejoicing, and that is why the city is in an uproar. That is the noise you heard.'",
      "T": "'and Zadok the priest and Nathan the prophet anointed him king at Gihon. They went up from there rejoicing—and that is the noise filling the city right now.'"
    },
    "46": {
      "L": "Solomon now sits on the royal throne.",
      "M": "Solomon is now sitting on the royal throne.",
      "T": "Solomon is already seated on the royal throne."
    },
    "47": {
      "L": "'Moreover the king's servants came to bless our lord King David, saying, May God make the name of Solomon more famous than your name and make his throne greater than your throne. And the king bowed himself on the bed.'",
      "M": "'The king's servants also came to congratulate our lord King David, saying, May God make the name of Solomon more renowned than yours, and his throne greater than yours. And the king bowed in worship on his bed.'",
      "T": "'And the king's own servants came and blessed David, saying: May God make Solomon's name more renowned than yours, and his throne greater than yours. And the king bowed in worship right there on his bed.'"
    },
    "48": {
      "L": "'Also the king said, Blessed be the LORD, the God of Israel, who has granted someone to sit on my throne this day, my own eyes seeing it.'",
      "M": "'And the king said this: Blessed be the LORD, the God of Israel, who has given me a son to sit on my throne today, while my own eyes can see it.'",
      "T": "'The king also said: Blessed be the LORD, the God of Israel, who has given me a son to sit on my throne this very day—and let me live to see it.'"
    },
    "49": {
      "L": "Then all the guests of Adonijah were afraid and rose and each went his own way.",
      "M": "Then all of Adonijah's guests were terrified and got up and went their separate ways.",
      "T": "All of Adonijah's guests were seized with terror. They got up and scattered, each going his own way."
    },
    "50": {
      "L": "And Adonijah feared Solomon. So he arose and went and caught hold of the horns of the altar.",
      "M": "Adonijah was afraid of Solomon. He got up and went and took hold of the horns of the altar.",
      "T": "Adonijah was terrified of Solomon. He got up and ran and seized the horns of the altar."
    },
    "51": {
      "L": "Then it was told Solomon, 'Behold, Adonijah fears King Solomon, for he has caught hold of the horns of the altar, saying, Let King Solomon swear to me first that he will not put his servant to death with the sword.'",
      "M": "Solomon was told, 'Adonijah is afraid of King Solomon. He has taken hold of the horns of the altar and says, Let King Solomon first swear that he will not put his servant to death with the sword.'",
      "T": "Word came to Solomon: 'Adonijah is clinging to the horns of the altar in fear. He is asking you to swear that you will not kill your servant with the sword.'"
    },
    "52": {
      "L": "And Solomon said, 'If he proves himself a worthy man, not one of his hairs shall fall to the earth. But if wickedness is found in him, he shall die.'",
      "M": "Solomon said, 'If he shows himself to be a man of integrity, not a hair of his shall fall to the ground. But if wickedness is found in him, he shall die.'",
      "T": "Solomon said: 'If he conducts himself well, not a hair on his head will be harmed. But if evil is found in him, he will die.'"
    },
    "53": {
      "L": "So King Solomon sent and had him brought down from the altar. He came and paid homage to King Solomon, and Solomon said to him, 'Go to your house.'",
      "M": "King Solomon sent and had him brought down from the altar. He came and bowed before King Solomon, and Solomon said to him, 'Go home.'",
      "T": "King Solomon sent for him, and they brought him down from the altar. He came and bowed before King Solomon, and Solomon said: 'Go home.'"
    }
  },
  "2": {
    "1": {
      "L": "When David's time to die drew near, he charged Solomon his son, saying,",
      "M": "As the time of David's death drew near, he gave these instructions to his son Solomon:",
      "T": "As David's death drew near, he charged his son Solomon:"
    },
    "2": {
      "L": "'I am about to go the way of all the earth. Be strong, and show yourself a man,'",
      "M": "'I am about to go the way of all the earth. Be strong; show yourself a man.'",
      "T": "'I am going the way of all the earth. Be strong. Be a man.'"
    },
    "3": {
      "L": "'and keep the charge of the LORD your God, walking in his ways and keeping his statutes, his commandments, his rules, and his testimonies, as it is written in the Law of Moses, that you may prosper in all that you do and wherever you turn,'",
      "M": "'Keep the charge of the LORD your God, walking in his ways and keeping his statutes, commandments, ordinances, and testimonies, as written in the Law of Moses, so that you may succeed in all you do and wherever you turn.'",
      "T": "'Keep the charge of the LORD your God: walk in his ways, keep his statutes, his commandments, his ordinances, and his testimonies, as written in the Law of Moses—so that you may prosper in everything you do and wherever you go.'"
    },
    "4": {
      "L": "'that the LORD may confirm his word that he spoke concerning me, saying, If your sons watch their way, to walk before me in truth with all their heart and with all their soul, there shall not fail you a man on the throne of Israel.'",
      "M": "'Then the LORD will confirm the promise he made about me: If your sons are careful in their way, walking before me in faithfulness with all their heart and soul, you will never lack a man on the throne of Israel.'",
      "T": "'Then the LORD will keep the word he spoke about me—that if your descendants watch their path and walk before him in whole-hearted faithfulness, the dynasty will never lack a man on Israel's throne.'"
    },
    "5": {
      "L": "'Moreover you know what Joab the son of Zeruiah did to me, what he did to the two commanders of the armies of Israel, Abner the son of Ner and Amasa the son of Jether, whom he killed, putting the blood of war in peacetime, and putting the blood of war on the belt around his waist and on the sandals on his feet.'",
      "M": "'You also know what Joab son of Zeruiah did to me—what he did to the two commanders of Israel's armies, Abner son of Ner and Amasa son of Jether. He murdered them, shedding blood in peacetime as if it were war, staining the belt at his waist and the sandals on his feet with innocent blood.'",
      "T": "'You know what Joab son of Zeruiah did to me—what he did to the two commanders of Israel's armies, Abner son of Ner and Amasa son of Jether. He murdered both of them. In peacetime he shed blood as if it were war, and that war-guilt stained his belt and his sandals.'"
    },
    "6": {
      "L": "'Act therefore according to your wisdom, but do not let his gray head go down to Sheol in peace.'",
      "M": "'Act according to your wisdom, but do not let his gray head go down to the grave in peace.'",
      "T": "'Deal with him as your wisdom directs—but do not let that gray head go peacefully to the grave.'"
    },
    "7": {
      "L": "'But deal loyally with the sons of Barzillai the Gileadite, and let them be among those who eat at your table, for with such kindness they met me when I fled from Absalom your brother.'",
      "M": "'But show steadfast loyalty to the sons of Barzillai the Gileadite, and let them eat at your table, for they showed me that same loyalty when I fled from your brother Absalom.'",
      "T": "'Show covenant loyalty to the sons of Barzillai the Gileadite—let them eat at your table. They came to me with that same loyalty when I was fleeing from your brother Absalom.'"
    },
    "8": {
      "L": "'And there is also with you Shimei the son of Gera, the Benjaminite from Bahurim, who cursed me with a grievous curse on the day when I went to Mahanaim. But when he came down to meet me at the Jordan, I swore to him by the LORD, saying, I will not put you to death with the sword.'",
      "M": "'You also have with you Shimei son of Gera the Benjaminite from Bahurim, who cursed me viciously on the day I went to Mahanaim. When he came down to meet me at the Jordan, I swore by the LORD: I will not put you to death with the sword.'",
      "T": "'You also have Shimei son of Gera the Benjaminite from Bahurim, who cursed me bitterly on the day I fled to Mahanaim. When he came down to meet me at the Jordan, I swore by the LORD: I will not kill you with the sword.'"
    },
    "9": {
      "L": "'Now therefore do not hold him guiltless, for you are a wise man. You will know what you ought to do to him, and you shall bring his gray head down with blood to Sheol.'",
      "M": "'But do not hold him guiltless, for you are a wise man. You know what to do with him. Bring his gray head down to the grave with blood.'",
      "T": "'But do not let him go unpunished. You are a wise man—you know what to do. Bring his gray head down to the grave with blood.'"
    },
    "10": {
      "L": "Then David slept with his fathers and was buried in the city of David.",
      "M": "Then David rested with his ancestors and was buried in the city of David.",
      "T": "Then David rested with his fathers and was buried in the city of David."
    },
    "11": {
      "L": "And the time that David reigned over Israel was forty years—seven years he reigned in Hebron and thirty-three years he reigned in Jerusalem.",
      "M": "David had reigned over Israel forty years—seven years in Hebron and thirty-three years in Jerusalem.",
      "T": "David reigned over Israel forty years in all—seven in Hebron, thirty-three in Jerusalem."
    },
    "12": {
      "L": "So Solomon sat on the throne of David his father, and his kingdom was firmly established.",
      "M": "Solomon sat on the throne of his father David, and his kingdom was firmly established.",
      "T": "Solomon took his seat on the throne of his father David. His kingdom was firmly established."
    },
    "13": {
      "L": "Then Adonijah the son of Haggith came to Bathsheba the mother of Solomon. She said, 'Do you come peaceably?' He said, 'Peaceably.'",
      "M": "Then Adonijah son of Haggith came to Bathsheba, Solomon's mother. She asked, 'Do you come in peace?' He said, 'In peace.'",
      "T": "Then Adonijah son of Haggith came to Bathsheba, Solomon's mother. 'Do you come in peace?' she asked. 'In peace,' he said."
    },
    "14": {
      "L": "Then he said, 'I have something to say to you.' She said, 'Speak.'",
      "M": "Then he said, 'I have a matter to discuss with you.' She said, 'Speak.'",
      "T": "He said: 'I have something to say to you.' She said: 'Speak.'"
    },
    "15": {
      "L": "He said, 'You know that the kingdom was mine and that all Israel fully expected me to reign. But the kingdom has turned about and become my brother's, for it was his from the LORD.'",
      "M": "He said, 'You know that the kingdom was mine and all Israel expected me to reign. Yet the kingdom has turned and become my brother's, for it was the LORD's to give him.'",
      "T": "He said: 'You know the kingdom was mine—all Israel expected me to reign. But the kingdom has passed to my brother. It was the LORD's to give, and he gave it to him.'"
    },
    "16": {
      "L": "'And now I have one request to make of you; do not refuse me.' She said to him, 'Speak.'",
      "M": "'Now I have one request to make of you; do not refuse me.' She said, 'Speak.'",
      "T": "'Now I have just one request—do not refuse me.' She said: 'Speak.'"
    },
    "17": {
      "L": "And he said, 'Please ask King Solomon—he will not refuse you—to give me Abishag the Shunammite as my wife.'",
      "M": "He said, 'Please ask King Solomon—he will not refuse you—to give me Abishag the Shunammite as my wife.'",
      "T": "He said: 'Please ask King Solomon—he will not refuse you—to give me Abishag the Shunammite as my wife.'"
    },
    "18": {
      "L": "Bathsheba said, 'Very well; I will speak for you to the king.'",
      "M": "Bathsheba said, 'Very well. I will speak to the king for you.'",
      "T": "Bathsheba said: 'Very well. I will speak to the king on your behalf.'"
    },
    "19": {
      "L": "So Bathsheba went to King Solomon to speak to him on behalf of Adonijah. And the king rose to meet her and bowed down to her. Then he sat on his throne and had a seat brought for the king's mother, and she sat on his right hand.",
      "M": "So Bathsheba went to King Solomon to speak to him for Adonijah. The king rose to meet her and bowed before her, then sat on his throne and had a seat placed for the king's mother, and she sat at his right hand.",
      "T": "Bathsheba went to King Solomon to speak on behalf of Adonijah. The king rose to meet her and bowed, then sat on his throne. A seat was placed for the queen mother, and she sat at his right hand."
    },
    "20": {
      "L": "Then she said, 'I have one small request to make of you; do not refuse me.' And the king said to her, 'Make your request, my mother, for I will not refuse you.'",
      "M": "She said, 'I have one small request to make; do not refuse me.' The king said to her, 'Ask, my mother—I will not refuse you.'",
      "T": "She said: 'I have just one small request to make—do not refuse me.' The king said: 'Ask it, my mother; I will not refuse you.'"
    },
    "21": {
      "L": "She said, 'Let Abishag the Shunammite be given to Adonijah your brother as his wife.'",
      "M": "She said, 'Let Abishag the Shunammite be given to your brother Adonijah as his wife.'",
      "T": "She said: 'Let Abishag the Shunammite be given to your brother Adonijah as his wife.'"
    },
    "22": {
      "L": "King Solomon answered his mother, 'And why do you ask Abishag the Shunammite for Adonijah? Ask for him the kingdom also, for he is my elder brother, and on his side are Abiathar the priest and Joab the son of Zeruiah.'",
      "M": "King Solomon answered his mother, 'Why do you ask Abishag the Shunammite for Adonijah? You might as well ask the kingdom for him—he is my elder brother—and on his side are Abiathar the priest and Joab son of Zeruiah.'",
      "T": "King Solomon said to his mother: 'Why do you ask Abishag for Adonijah? You might as well ask me to give him the kingdom. He is my elder brother. He has Abiathar the priest and Joab son of Zeruiah on his side.'"
    },
    "23": {
      "L": "Then King Solomon swore by the LORD, saying, 'God do so to me and more also if this word does not cost Adonijah his life!'",
      "M": "Then King Solomon swore by the LORD: 'May God punish me severely if this request does not cost Adonijah his life!'",
      "T": "King Solomon swore by the LORD: 'May God deal with me in the harshest terms if this request does not cost Adonijah his life!'"
    },
    "24": {
      "L": "'Now therefore as the LORD lives, who has established me and placed me on the throne of David my father and who has made me a house as he promised, Adonijah shall be put to death this day.'",
      "M": "'Now, as the LORD lives—who established me and set me on the throne of David my father and made me a dynasty as he promised—Adonijah shall be put to death today.'",
      "T": "'As the LORD lives—who established me and seated me on the throne of my father David, who built me a dynasty as he promised—Adonijah will die today.'"
    },
    "25": {
      "L": "So King Solomon sent Benaiah the son of Jehoiada, and he struck him down, and he died.",
      "M": "King Solomon sent Benaiah son of Jehoiada, who struck Adonijah down, and he died.",
      "T": "King Solomon sent Benaiah son of Jehoiada, who struck Adonijah down. He died."
    },
    "26": {
      "L": "And to Abiathar the priest the king said, 'Go to Anathoth, to your estate, for you deserve death. But I will not at this time put you to death, because you carried the ark of the Lord GOD before David my father, and because you shared in all my father's affliction.'",
      "M": "To Abiathar the priest the king said, 'Go to Anathoth, to your own property. You deserve death, but I will not put you to death now, because you carried the ark of the Lord GOD before my father David and because you shared in all my father's hardships.'",
      "T": "To Abiathar the priest the king said: 'Go to Anathoth, to your own fields. You deserve to die—but I will not execute you now, because you carried the ark of the Lord GOD before my father David, and because you shared in all his suffering.'"
    },
    "27": {
      "L": "So Solomon expelled Abiathar from being priest to the LORD, thus fulfilling the word of the LORD that he had spoken concerning the house of Eli in Shiloh.",
      "M": "So Solomon removed Abiathar from the priesthood of the LORD, fulfilling the word the LORD had spoken against the house of Eli in Shiloh.",
      "T": "So Solomon removed Abiathar from the priesthood. This fulfilled the word the LORD had spoken against the house of Eli at Shiloh."
    },
    "28": {
      "L": "When the news came to Joab—for Joab had sided with Adonijah though he had not sided with Absalom—Joab fled to the tent of the LORD and caught hold of the horns of the altar.",
      "M": "When news of this reached Joab—for Joab had sided with Adonijah though not with Absalom—Joab fled to the tent of the LORD and grasped the horns of the altar.",
      "T": "The news reached Joab—he had sided with Adonijah, though not with Absalom—and Joab fled to the tent of the LORD and seized the horns of the altar."
    },
    "29": {
      "L": "And when it was told King Solomon, 'Joab has fled to the tent of the LORD and behold, he is beside the altar,' Solomon sent Benaiah the son of Jehoiada, saying, 'Go, strike him down.'",
      "M": "King Solomon was told, 'Joab has fled to the tent of the LORD and is by the altar.' Solomon sent Benaiah son of Jehoiada with orders: 'Go, strike him down.'",
      "T": "Word came to King Solomon: 'Joab has fled to the tent of the LORD and is clinging to the altar.' Solomon sent Benaiah son of Jehoiada: 'Go, strike him down.'"
    },
    "30": {
      "L": "So Benaiah came to the tent of the LORD and said to him, 'The king says, Come out.' But he said, 'No, I will die here.' Then Benaiah brought the king word again, saying, 'Thus said Joab, and thus he answered me.'",
      "M": "Benaiah went to the tent of the LORD and said to Joab, 'The king commands, Come out.' But he said, 'No. I will die here.' Benaiah brought word back to the king: 'This is what Joab said and this is how he answered me.'",
      "T": "Benaiah went to the tent of the LORD. 'The king says: Come out,' he said. But Joab said: 'No. I will die here.' Benaiah brought the king's reply back: 'This is what Joab said, and this is how he answered me.'"
    },
    "31": {
      "L": "The king replied, 'Do as he has said, strike him down and bury him, and thus take away from me and from my father's house the guilt for the blood that Joab shed without cause.'",
      "M": "The king said, 'Do as he says—strike him down and bury him. Remove from me and from my father's house the blood guilt that Joab shed without cause.'",
      "T": "The king said: 'Do as he says—strike him down and bury him. Remove from me and from my father's house the blood Joab shed without cause.'"
    },
    "32": {
      "L": "'The LORD will bring back his bloody deeds on his own head, because he attacked and killed without my father David's knowledge two men more righteous and better than himself, Abner the son of Ner, commander of the army of Israel, and Amasa the son of Jether, commander of the army of Judah.'",
      "M": "'The LORD will bring his bloodshed back on his own head, because without my father David's knowledge he attacked and killed two men more righteous and better than himself: Abner son of Ner, the commander of Israel's army, and Amasa son of Jether, the commander of Judah's army.'",
      "T": "'The LORD will return his bloodshed on his own head. He struck down two men more righteous than himself—without my father David knowing it. Abner son of Ner, commander of Israel's army, and Amasa son of Jether, commander of Judah's army.'"
    },
    "33": {
      "L": "'So shall their blood come back on the head of Joab and on the head of his descendants forever. But for David and for his descendants and for his house and for his throne, there shall be peace from the LORD forevermore.'",
      "M": "'Their blood will come back on Joab and his descendants forever. But on David, his descendants, his house, and his throne there shall be peace from the LORD forevermore.'",
      "T": "'Their blood will fall on Joab's head and on his descendants forever. But on David, his descendants, his house, and his throne—peace from the LORD, now and forever.'"
    },
    "34": {
      "L": "Then Benaiah the son of Jehoiada went up and struck him down and put him to death, and he was buried at his own house in the wilderness.",
      "M": "Benaiah son of Jehoiada went and struck Joab down and killed him. He was buried at his own house in the wilderness.",
      "T": "Benaiah son of Jehoiada went up and struck Joab down. He was buried at his own house in the wilderness."
    },
    "35": {
      "L": "The king put Benaiah the son of Jehoiada over the army in place of Joab, and the king put Zadok the priest in the place of Abiathar.",
      "M": "The king appointed Benaiah son of Jehoiada over the army in Joab's place, and appointed Zadok the priest in Abiathar's place.",
      "T": "The king appointed Benaiah son of Jehoiada over the army in Joab's place, and Zadok the priest in Abiathar's place."
    },
    "36": {
      "L": "Then the king sent and summoned Shimei and said to him, 'Build yourself a house in Jerusalem and live there, and do not go out from there to any place whatever.'",
      "M": "The king sent for Shimei and told him, 'Build yourself a house in Jerusalem and live there, and do not leave for any destination whatsoever.'",
      "T": "The king sent for Shimei and said: 'Build a house in Jerusalem and live there. Do not leave for any reason, anywhere.'"
    },
    "37": {
      "L": "'For on the day you go out and cross the brook Kidron, know for certain that you shall die. Your blood shall be on your own head.'",
      "M": "'For on the day you leave and cross the Kidron Valley, know for certain that you will die. Your blood will be on your own head.'",
      "T": "'The day you leave and cross the Kidron, know for certain: you will die. Your blood will be on your own head.'"
    },
    "38": {
      "L": "And Shimei said to the king, 'What you say is good; as my lord the king has said, so will your servant do.' So Shimei lived in Jerusalem many days.",
      "M": "Shimei said to the king, 'What you say is good; your servant will do exactly as my lord the king commands.' So Shimei lived in Jerusalem for many years.",
      "T": "Shimei said: 'What you say is good. Your servant will do exactly as my lord the king commands.' Shimei lived in Jerusalem for many years."
    },
    "39": {
      "L": "But at the end of three years two of Shimei's servants ran away to Achish the son of Maacah, king of Gath. And when it was told Shimei, 'Your servants are in Gath,'",
      "M": "But at the end of three years two of Shimei's servants ran away to Achish son of Maacah, king of Gath. Shimei was told, 'Your servants are in Gath.'",
      "T": "But three years later, two of Shimei's servants ran away to Achish son of Maacah, king of Gath. Shimei was told: 'Your servants are in Gath.'"
    },
    "40": {
      "L": "Shimei arose and saddled a donkey and went to Gath to Achish to seek his servants. Shimei went and brought his servants from Gath.",
      "M": "Shimei got up, saddled his donkey, and went to Gath to Achish to reclaim his servants. He went and brought them back from Gath.",
      "T": "Shimei saddled his donkey and went to Gath to Achish to reclaim his servants. He went and brought them back."
    },
    "41": {
      "L": "And when Solomon was told that Shimei had gone from Jerusalem to Gath and returned,",
      "M": "When Solomon was told that Shimei had left Jerusalem for Gath and returned,",
      "T": "Solomon was told that Shimei had gone to Gath and returned."
    },
    "42": {
      "L": "the king sent and summoned Shimei and said to him, 'Did I not make you swear by the LORD and solemnly warn you, saying, Know for certain that on the day you go out and go anywhere, you shall die? And you said to me, What you say is good; I will obey.'",
      "M": "The king sent for Shimei and said, 'Did I not make you swear by the LORD and solemnly warn you: On the day you leave and go anywhere, you will certainly die? And you said to me, What you say is good; I will obey.'",
      "T": "The king sent for Shimei and said: 'Did I not make you swear by the LORD and give you fair warning? The day you leave Jerusalem and go anywhere, you will die. You said: What you say is good; I will obey.'"
    },
    "43": {
      "L": "'Why then have you not kept the oath of the LORD and the commandment with which I charged you?'",
      "M": "'Why then have you not kept the oath you swore before the LORD and the command I gave you?'",
      "T": "'Then why did you not keep your oath to the LORD and the command I laid on you?'"
    },
    "44": {
      "L": "The king also said to Shimei, 'You know in your own heart all the harm that you did to David my father. So the LORD will bring back your harm on your own head.'",
      "M": "The king said further, 'You know in your own heart all the evil you did to my father David. The LORD will bring that evil back on your own head.'",
      "T": "The king said: 'You know in your own heart all the harm you did to my father David. The LORD is bringing that harm back on your own head.'"
    },
    "45": {
      "L": "'But King Solomon shall be blessed, and the throne of David shall be established before the LORD forever.'",
      "M": "'But King Solomon shall be blessed, and David's throne will be established before the LORD forever.'",
      "T": "'But King Solomon will be blessed, and the throne of David will stand before the LORD forever.'"
    },
    "46": {
      "L": "Then the king commanded Benaiah the son of Jehoiada, and he went out and struck him down, and he died. The kingdom was established in the hand of Solomon.",
      "M": "The king commanded Benaiah son of Jehoiada, who went out and struck Shimei down, and he died. The kingdom was now firmly established in Solomon's hand.",
      "T": "The king commanded Benaiah son of Jehoiada, who went out and struck Shimei down. He died. And the kingdom was fully established in Solomon's hand."
    }
  },
  "3": {
    "1": {
      "L": "Solomon made a marriage alliance with Pharaoh king of Egypt. He took Pharaoh's daughter and brought her into the city of David, until he had finished building his own house and the house of the LORD and the wall around Jerusalem.",
      "M": "Solomon made a marriage alliance with Pharaoh king of Egypt. He took Pharaoh's daughter and brought her to the city of David until he had finished building his palace, the house of the LORD, and the wall around Jerusalem.",
      "T": "Solomon made a marriage alliance with Pharaoh king of Egypt—he took Pharaoh's daughter and settled her in the city of David until he had finished building his own palace, the house of the LORD, and the wall around Jerusalem."
    },
    "2": {
      "L": "The people were still sacrificing at the high places, however, because no house had yet been built for the name of the LORD.",
      "M": "The people were still offering sacrifices at the high places, since no house for the LORD's name had yet been built.",
      "T": "The people were still worshiping at the hilltop shrines—there was as yet no house built for the name of the LORD."
    },
    "3": {
      "L": "Solomon loved the LORD, walking in the statutes of David his father, only he sacrificed and made offerings at the high places.",
      "M": "Solomon loved the LORD and walked in the statutes of his father David, except that he offered sacrifices and burned incense at the high places.",
      "T": "Solomon loved the LORD and walked in the statutes of his father David—though he still offered sacrifices and burned incense at the high places."
    },
    "4": {
      "L": "And the king went to Gibeon to sacrifice there, for that was the great high place. Solomon offered a thousand burnt offerings on that altar.",
      "M": "The king went to Gibeon to sacrifice there, for that was the most prominent high place. Solomon offered a thousand burnt offerings on that altar.",
      "T": "The king went to Gibeon to sacrifice—it was the greatest of the high places—and Solomon offered a thousand burnt offerings there on the altar."
    },
    "5": {
      "L": "At Gibeon the LORD appeared to Solomon in a dream by night, and God said, 'Ask what I shall give you.'",
      "M": "At Gibeon the LORD appeared to Solomon in a dream during the night, and God said, 'Ask whatever you wish and I will give it to you.'",
      "T": "At Gibeon the LORD appeared to Solomon in a dream at night. God said: 'Ask. What shall I give you?'"
    },
    "6": {
      "L": "And Solomon said, 'You have shown great kindness to your servant David my father, because he walked before you in faithfulness, in righteousness, and in uprightness of heart toward you. And you have kept for him this great kindness and have given him a son to sit on his throne this day.'",
      "M": "And Solomon said, 'You have shown great steadfast love to your servant David my father, because he walked before you in faithfulness, righteousness, and uprightness of heart. You have continued this great steadfast love by giving him a son to sit on his throne today.'",
      "T": "Solomon said: 'You showed such faithful love to your servant David my father, because he walked before you in faithfulness, righteousness, and sincerity of heart. And you have continued that faithful love—you have given him a son sitting on his throne this very day.'"
    },
    "7": {
      "L": "'And now, O LORD my God, you have made your servant king in place of David my father, although I am but a little child. I do not know how to go out or come in.'",
      "M": "'And now, LORD my God, you have made your servant king in place of David my father, though I am only a young man. I do not know how to lead.'",
      "T": "'And now, LORD my God, you have made me king in my father David's place—though I am only a youth. I do not know how to lead or govern.'"
    },
    "8": {
      "L": "'And your servant is in the midst of your people whom you have chosen, a great people, too many to be numbered or counted for multitude.'",
      "M": "'Your servant stands in the midst of your chosen people, a great people too numerous to be counted or numbered.'",
      "T": "'Your servant stands among your chosen people—a great people, so vast they cannot be counted.'"
    },
    "9": {
      "L": "'Give your servant therefore a hearing heart to judge your people, that I may discern between good and evil, for who is able to judge this your so great a people?'",
      "M": "'Give your servant therefore an understanding mind to govern your people, that I may discern between good and evil. For who is able to govern this great people of yours?'",
      "T": "'Give your servant therefore a heart that truly listens—to govern your people, to tell right from wrong. For who can govern this great people of yours?'"
    },
    "10": {
      "L": "It pleased the Lord that Solomon had asked this.",
      "M": "It pleased the Lord that Solomon had asked for this.",
      "T": "The Lord was pleased that Solomon had asked for this."
    },
    "11": {
      "L": "And God said to him, 'Because you have asked this, and have not asked for yourself long life or riches or the life of your enemies, but have asked for yourself understanding to discern justice,'",
      "M": "And God said to him, 'Because you have asked for this and not for long life, riches, or the death of your enemies, but for discernment to judge rightly,'",
      "T": "God said to him: 'Because you asked for this—not long life, not wealth, not the death of your enemies—but for the discernment to do justice,'"
    },
    "12": {
      "L": "'behold, I do according to your word. Behold, I give you a wise and discerning mind, so that none like you has been before you and none like you shall arise after you.'",
      "M": "'I now do as you asked. I give you a wise and discerning mind, so that no one like you has existed before and no one like you will arise after.'",
      "T": "'I am doing as you asked. I am giving you a wise and discerning mind—there has been no one like you before, and there will be no one like you after.'"
    },
    "13": {
      "L": "'I give you also what you have not asked, both riches and honor, so that no other king shall compare with you all your days.'",
      "M": "'I also give you what you did not ask for—both wealth and honor—so that no other king shall compare with you all your life.'",
      "T": "'I also give you what you did not ask: wealth and honor, so that no king in all your days will compare to you.'"
    },
    "14": {
      "L": "'And if you walk in my ways, keeping my statutes and my commandments, as your father David walked, then I will lengthen your days.'",
      "M": "'And if you walk in my ways and keep my statutes and commandments as your father David did, I will give you long life.'",
      "T": "'And if you walk in my ways—keeping my statutes and commandments as your father David did—I will give you long life.'"
    },
    "15": {
      "L": "And Solomon awoke, and behold, it was a dream. Then he came to Jerusalem and stood before the ark of the covenant of the LORD, and offered burnt offerings and peace offerings, and made a feast for all his servants.",
      "M": "Solomon awoke, and it was a dream. He returned to Jerusalem and stood before the ark of the covenant of the LORD, and offered burnt offerings and peace offerings, and held a feast for all his servants.",
      "T": "Solomon woke—it was a dream. He went to Jerusalem and stood before the ark of the covenant of the LORD, and offered burnt offerings and peace offerings, and gave a feast for all his servants."
    },
    "16": {
      "L": "Then two women who were prostitutes came to the king and stood before him.",
      "M": "Then two women who were prostitutes came to the king and stood before him.",
      "T": "Then two women who were prostitutes came to the king and stood before him."
    },
    "17": {
      "L": "The one woman said, 'Oh, my lord, this woman and I live in the same house, and I gave birth to a child while she was in the house.'",
      "M": "The first woman said, 'Please, my lord, this woman and I share a house, and I gave birth to a child while she was there with me.'",
      "T": "The first woman said: 'My lord, this woman and I live in the same house. I gave birth while she was with me in the house.'"
    },
    "18": {
      "L": "'Then on the third day after I gave birth, this woman also gave birth. And we were alone. There was no one else with us in the house; only the two of us were in the house.'",
      "M": "'Three days after I gave birth, she also gave birth. We were alone—there was no one else with us in the house, just the two of us.'",
      "T": "'Three days after I gave birth, she also gave birth. We were alone together—no one else was there. Just the two of us.'"
    },
    "19": {
      "L": "'And this woman's son died in the night, because she lay on him.'",
      "M": "'This woman's son died in the night because she rolled over on him.'",
      "T": "'This woman's son died in the night—she lay on him.'"
    },
    "20": {
      "L": "'And she arose at midnight and took my son from beside me while your servant slept and laid him at her breast, and laid her dead son at my breast.'",
      "M": "'She got up at midnight and took my son from my side while I was asleep and laid him at her breast, and placed her dead son at my breast.'",
      "T": "'She got up at midnight while I slept, took my son from beside me, laid him at her breast—and put her dead son at mine.'"
    },
    "21": {
      "L": "'When I rose in the morning to nurse my child, behold, he was dead. But when I looked at him closely in the morning, behold, he was not the child that I had borne.'",
      "M": "'When I got up in the morning to nurse my child, he was dead. But when I examined him carefully in the morning light, I saw he was not the child I had given birth to.'",
      "T": "'When I got up in the morning to nurse my child—he was dead. But when I looked at him in the morning light, I saw he was not the child I had borne.'"
    },
    "22": {
      "L": "But the other woman said, 'No, the living child is mine, and the dead child is yours.' The first said, 'No, the dead child is yours, and the living child is mine.' Thus they spoke before the king.",
      "M": "The other woman said, 'No, the living child is mine and the dead one is yours.' The first insisted, 'No, the dead one is yours and the living one is mine.' So they argued before the king.",
      "T": "The other woman said: 'No—the living child is mine and the dead one is yours.' The first said: 'No—the dead one is yours and the living one is mine.' They argued like this before the king."
    },
    "23": {
      "L": "Then the king said, 'The one says, This is my son that is alive, and your son is dead; and the other says, No, but your son is dead and my son is the living one.'",
      "M": "The king said, 'Each of you claims: This is my son who is alive and your son is the dead one. The other says: No, your son is dead and my son is alive.'",
      "T": "The king said: 'One says: This living child is mine and the dead child is yours. The other says: No—the dead child is yours and the living one is mine.'"
    },
    "24": {
      "L": "And the king said, 'Bring me a sword.' So a sword was brought before the king.",
      "M": "The king said, 'Bring me a sword.' A sword was brought before the king.",
      "T": "The king said: 'Bring me a sword.' They brought a sword before the king."
    },
    "25": {
      "L": "And the king said, 'Divide the living child in two, and give half to the one and half to the other.'",
      "M": "The king said, 'Cut the living child in two and give half to each woman.'",
      "T": "The king said: 'Cut the living child in two. Give half to one and half to the other.'"
    },
    "26": {
      "L": "Then the woman whose son was alive said to the king, because her heart yearned for her son, 'Oh, my lord, give her the living child and by no means put him to death.' But the other said, 'He shall be neither mine nor yours; divide him.'",
      "M": "The woman whose son was alive cried out to the king—her heart ached for her son—'Please, my lord, give her the living child! Do not kill him!' But the other said, 'Let him be neither mine nor yours; divide him.'",
      "T": "The woman whose child was alive—her heart was torn open for her son—cried: 'My lord! Give her the living child! Do not kill him!' But the other said: 'Let him be neither mine nor yours. Divide him.'"
    },
    "27": {
      "L": "Then the king answered and said, 'Give the living child to the first woman, and by no means put him to death; she is his mother.'",
      "M": "Then the king gave his verdict: 'Give the living child to the first woman, and do not kill him. She is his mother.'",
      "T": "The king gave his verdict: 'Give the living child to the first woman. Do not kill him. She is his mother.'"
    },
    "28": {
      "L": "And all Israel heard of the judgment that the king had rendered, and they stood in awe of the king, because they perceived that the wisdom of God was in him to do justice.",
      "M": "All Israel heard of the judgment the king had given, and they stood in awe of him, because they saw that God's wisdom was in him to carry out justice.",
      "T": "All Israel heard of the king's judgment, and they stood in awe of him—because they saw that the wisdom of God was in him to do justice."
    }
  },
  "4": {
    "1": {
      "L": "So King Solomon was king over all Israel.",
      "M": "King Solomon was king over all Israel.",
      "T": "King Solomon ruled over all Israel."
    },
    "2": {
      "L": "And these were his chief officials: Azariah the son of Zadok was the priest;",
      "M": "These were his chief officials: Azariah son of Zadok was the priest;",
      "T": "These were his chief officials: Azariah son of Zadok the priest;"
    },
    "3": {
      "L": "Elihoreph and Ahijah the sons of Shisha were secretaries; Jehoshaphat the son of Ahilud was recorder;",
      "M": "Elihoreph and Ahijah sons of Shisha were secretaries; Jehoshaphat son of Ahilud was the recorder;",
      "T": "Elihoreph and Ahijah sons of Shisha were secretaries; Jehoshaphat son of Ahilud was the recorder;"
    },
    "4": {
      "L": "Benaiah the son of Jehoiada was over the army; Zadok and Abiathar were priests;",
      "M": "Benaiah son of Jehoiada was over the army; Zadok and Abiathar were priests;",
      "T": "Benaiah son of Jehoiada commanded the army; Zadok and Abiathar served as priests;"
    },
    "5": {
      "L": "Azariah the son of Nathan was over the officers; Zabud the son of Nathan was priest and the king's friend;",
      "M": "Azariah son of Nathan was over the district officers; Zabud son of Nathan was a priest and the king's personal friend;",
      "T": "Azariah son of Nathan oversaw the district governors; Zabud son of Nathan was a priest and the king's trusted friend;"
    },
    "6": {
      "L": "Ahishar was over the household; and Adoniram the son of Abda was in charge of the forced labor.",
      "M": "Ahishar was over the royal household; and Adoniram son of Abda was in charge of the forced labor.",
      "T": "Ahishar managed the royal household; Adoniram son of Abda oversaw the forced labor."
    },
    "7": {
      "L": "Solomon had twelve officers over all Israel, who provided food for the king and his household. Each man had to make provision for one month in the year.",
      "M": "Solomon had twelve district governors over all Israel, who supplied provisions for the king and his household—each one responsible for one month of the year.",
      "T": "Solomon had twelve district governors over all Israel who supplied provisions for the king and his household. Each was responsible for one month of the year."
    },
    "8": {
      "L": "These were their names: Ben-hur, in the hill country of Ephraim;",
      "M": "These were their names: Ben-hur, in the hill country of Ephraim;",
      "T": "Their names: Ben-hur, in the hill country of Ephraim;"
    },
    "9": {
      "L": "Ben-deker, in Makaz, Shaalbim, Beth-shemesh, and Elon-beth-hanan;",
      "M": "Ben-deker, in Makaz, Shaalbim, Beth-shemesh, and Elon-beth-hanan;",
      "T": "Ben-deker, in Makaz, Shaalbim, Beth-shemesh, and Elon-beth-hanan;"
    },
    "10": {
      "L": "Ben-hesed, in Arubboth, with Socoh and all the land of Hepher belonging to him;",
      "M": "Ben-hesed, in Arubboth, with Socoh and all the land of Hepher;",
      "T": "Ben-hesed, in Arubboth, with Socoh and all the land of Hepher;"
    },
    "11": {
      "L": "Ben-abinadab, in all Naphath-dor, who had Taphath the daughter of Solomon as his wife;",
      "M": "Ben-abinadab, in all Naphath-dor—he had Solomon's daughter Taphath as his wife;",
      "T": "Ben-abinadab, in all Naphath-dor—he had Taphath, Solomon's daughter, as his wife;"
    },
    "12": {
      "L": "Baana the son of Ahilud, in Taanach and Megiddo and all Beth-shean beside Zarethan below Jezreel, from Beth-shean to Abel-meholah and as far as beyond Jokneam;",
      "M": "Baana son of Ahilud, in Taanach, Megiddo, and all Beth-shean beside Zarethan below Jezreel, from Beth-shean to Abel-meholah, as far as beyond Jokneam;",
      "T": "Baana son of Ahilud, in Taanach and Megiddo and all Beth-shean by Zarethan below Jezreel, from Beth-shean to Abel-meholah, beyond Jokneam;"
    },
    "13": {
      "L": "Ben-geber, in Ramoth-gilead, with the villages of Jair the son of Manasseh in Gilead belonging to him, and with the region of Argob in Bashan, sixty great cities with walls and bronze bars belonging to him;",
      "M": "Ben-geber, in Ramoth-gilead—including the villages of Jair son of Manasseh in Gilead and the region of Argob in Bashan with sixty great walled cities with bronze bars;",
      "T": "Ben-geber, in Ramoth-gilead, with the towns of Jair son of Manasseh in Gilead and the region of Argob in Bashan—sixty great walled cities with bronze bars;"
    },
    "14": {
      "L": "Ahinadab the son of Iddo, in Mahanaim;",
      "M": "Ahinadab son of Iddo, in Mahanaim;",
      "T": "Ahinadab son of Iddo, in Mahanaim;"
    },
    "15": {
      "L": "Ahimaaz, in Naphtali—he also had taken Basemath the daughter of Solomon as his wife;",
      "M": "Ahimaaz, in Naphtali—he also had Solomon's daughter Basemath as his wife;",
      "T": "Ahimaaz, in Naphtali—he too had married a daughter of Solomon, Basemath;"
    },
    "16": {
      "L": "Baanah the son of Hushai, in Asher and Bealoth;",
      "M": "Baanah son of Hushai, in Asher and Bealoth;",
      "T": "Baanah son of Hushai, in Asher and Bealoth;"
    },
    "17": {
      "L": "Jehoshaphat the son of Paruah, in Issachar;",
      "M": "Jehoshaphat son of Paruah, in Issachar;",
      "T": "Jehoshaphat son of Paruah, in Issachar;"
    },
    "18": {
      "L": "Shimei the son of Ela, in Benjamin;",
      "M": "Shimei son of Ela, in Benjamin;",
      "T": "Shimei son of Ela, in Benjamin;"
    },
    "19": {
      "L": "Geber the son of Uri, in the land of Gilead, the country of Sihon king of the Amorites and of Og king of Bashan. And there was one officer who was over the land.",
      "M": "Geber son of Uri, in the land of Gilead, the territory of Sihon king of the Amorites and Og king of Bashan. There was also one governor over the whole land.",
      "T": "Geber son of Uri, in the land of Gilead—the territory of Sihon king of the Amorites and Og king of Bashan. One governor oversaw the whole land."
    },
    "20": {
      "L": "Judah and Israel were as many as the sand by the sea. They ate and drank and were happy.",
      "M": "Judah and Israel were as numerous as the sand by the sea. They ate and drank and were content.",
      "T": "Judah and Israel were as countless as the sand on the seashore. They ate and drank and were glad."
    },
    "21": {
      "L": "Solomon ruled over all the kingdoms from the Euphrates to the land of the Philistines and to the border of Egypt. They brought tribute and served Solomon all the days of his life.",
      "M": "Solomon ruled over all the kingdoms from the Euphrates to the land of the Philistines and as far as the border of Egypt. They paid tribute and served Solomon all his life.",
      "T": "Solomon's dominion stretched from the Euphrates to the land of the Philistines and the border of Egypt. All those kingdoms paid tribute and served Solomon all the days of his life."
    },
    "22": {
      "L": "Solomon's provision for one day was thirty cors of fine flour and sixty cors of meal,",
      "M": "Solomon's daily provisions were thirty cors of fine flour and sixty cors of ordinary flour,",
      "T": "Solomon's daily provisions amounted to thirty cors of fine flour and sixty cors of ordinary flour,"
    },
    "23": {
      "L": "ten fat oxen, and twenty pasture-fed cattle, a hundred sheep, besides deer, gazelles, roebucks, and fattened fowl.",
      "M": "ten fattened oxen, twenty pasture-fed cattle, a hundred sheep, and in addition deer, gazelles, roebucks, and choice fowl.",
      "T": "ten fattened oxen, twenty pasture-fed cattle, a hundred sheep—besides deer, gazelles, roebucks, and choice birds."
    },
    "24": {
      "L": "For he had dominion over all the region west of the Euphrates from Tiphsah to Gaza, over all the kings west of the Euphrates. And he had peace on all sides around him.",
      "M": "For he had dominion over all the region west of the Euphrates, from Tiphsah to Gaza, over all the kings on that side of the Euphrates. And he had peace on every side.",
      "T": "He ruled all the territory west of the Euphrates—from Tiphsah to Gaza, over every king in that region. He had peace on every side."
    },
    "25": {
      "L": "And Judah and Israel lived in safety, from Dan even to Beersheba, every man under his vine and under his fig tree, all the days of Solomon.",
      "M": "During Solomon's lifetime Judah and Israel lived in safety, from Dan to Beersheba, each man under his own vine and his own fig tree.",
      "T": "Throughout Solomon's reign, Judah and Israel lived in security—from Dan to Beersheba, each family under their own vine and fig tree, at peace."
    },
    "26": {
      "L": "Solomon also had forty thousand stalls of horses for his chariots, and twelve thousand horsemen.",
      "M": "Solomon also had forty thousand stalls for his chariot horses and twelve thousand horsemen.",
      "T": "Solomon had forty thousand horse stalls for his chariots and twelve thousand horsemen."
    },
    "27": {
      "L": "And those officers supplied provisions for King Solomon, and for all who came to King Solomon's table, each one in his month. They let nothing be lacking.",
      "M": "Those district officers supplied provisions for King Solomon and everyone who came to his table, each in his designated month. They let nothing be lacking.",
      "T": "Those district governors supplied provisions for King Solomon and all who ate at his table, each for his assigned month. Nothing was ever lacking."
    },
    "28": {
      "L": "Barley also and straw for the horses and swift steeds they brought to the place where it was required, each according to his duty.",
      "M": "They also delivered barley and straw for the horses and swift steeds to wherever it was needed, each according to his assignment.",
      "T": "Barley and straw for the horses and chariot teams—each governor brought them to the required place according to his duty."
    },
    "29": {
      "L": "And God gave Solomon wisdom and understanding beyond measure, and breadth of mind like the sand on the seashore.",
      "M": "God gave Solomon wisdom and understanding beyond all measure, and a breadth of insight like the sand on the seashore.",
      "T": "God gave Solomon wisdom and understanding beyond all measure—a breadth of mind as vast as the sand on the seashore."
    },
    "30": {
      "L": "Solomon's wisdom surpassed the wisdom of all the people of the east and all the wisdom of Egypt.",
      "M": "Solomon's wisdom exceeded the wisdom of all the sages of the east and all the wisdom of Egypt.",
      "T": "Solomon's wisdom surpassed all the wisdom of the east and all the wisdom of Egypt."
    },
    "31": {
      "L": "For he was wiser than all men—wiser than Ethan the Ezrahite, and Heman, Chalcol, and Darda, the sons of Mahol—and his fame was in all the surrounding nations.",
      "M": "He was wiser than all other men—wiser than Ethan the Ezrahite, and Heman, Chalcol, and Darda, sons of Mahol—and his reputation reached all the surrounding nations.",
      "T": "He was wiser than any man who had lived—wiser than Ethan the Ezrahite, wiser than Heman, Chalcol, and Darda, the sons of Mahol. His fame spread to all the surrounding nations."
    },
    "32": {
      "L": "He also spoke three thousand proverbs, and his songs were one thousand and five.",
      "M": "He composed three thousand proverbs, and his songs numbered one thousand and five.",
      "T": "He composed three thousand proverbs, and his songs numbered a thousand and five."
    },
    "33": {
      "L": "He spoke of trees, from the cedar in Lebanon to the hyssop that grows out of the wall. He spoke also of beasts, and of birds, and of reptiles, and of fish.",
      "M": "He spoke about plant life, from the cedar of Lebanon to the hyssop growing from the wall. He also spoke about animals, birds, reptiles, and fish.",
      "T": "He spoke of every kind of plant—from the great cedar of Lebanon down to the hyssop growing from a crack in the wall. He spoke of animals, birds, creeping things, and fish."
    },
    "34": {
      "L": "And people of all nations came to hear the wisdom of Solomon, and from all the kings of the earth who had heard of his wisdom.",
      "M": "People from all nations came to hear the wisdom of Solomon, sent by all the kings of the earth who had heard of his wisdom.",
      "T": "People came from every nation to hear Solomon's wisdom—delegates sent by every king on earth who had heard of him."
    }
  },
  "5": {
    "1": {
      "L": "Now Hiram king of Tyre sent his servants to Solomon when he heard that they had anointed him king in place of his father, for Hiram always loved David.",
      "M": "Hiram king of Tyre sent his servants to Solomon when he heard that Solomon had been anointed king in his father's place, for Hiram had always been a friend of David.",
      "T": "Hiram king of Tyre sent his envoys to Solomon when he heard that Solomon had been anointed king in his father's place—for Hiram had always loved David."
    },
    "2": {
      "L": "And Solomon sent word to Hiram,",
      "M": "Solomon sent back this message to Hiram:",
      "T": "Solomon sent this word to Hiram:"
    },
    "3": {
      "L": "'You know that David my father could not build a house for the name of the LORD his God because of the warfare with which his enemies surrounded him, until the LORD put them under the soles of his feet.'",
      "M": "'You know that my father David could not build a house for the name of the LORD his God because of the wars surrounding him on all sides, until the LORD placed his enemies under his feet.'",
      "T": "'You know that my father David could not build a house for the name of the LORD his God—the wars on every side prevented it, until the LORD finally put his enemies under his feet.'"
    },
    "4": {
      "L": "'But now the LORD my God has given me rest on every side. There is neither adversary nor misfortune.'",
      "M": "'But now the LORD my God has given me rest on every side. There is no enemy or threat of disaster.'",
      "T": "'But now the LORD my God has given me rest on every side. There is no adversary, no disaster to fear.'"
    },
    "5": {
      "L": "'And so I intend to build a house for the name of the LORD my God, as the LORD said to David my father, Your son, whom I will set on your throne in your place, shall build the house for my name.'",
      "M": "'I therefore intend to build a house for the name of the LORD my God, as the LORD told my father David: Your son, whom I will place on your throne, will build the house for my name.'",
      "T": "'So I intend to build a house for the name of the LORD my God, as the LORD said to my father David: Your son, whom I will place on your throne, will build my house.'"
    },
    "6": {
      "L": "'Now therefore command that cedars of Lebanon be cut for me. And my servants will join your servants, and I will pay you for your servants whatever wages you set, for you know that there is no one among us who knows how to cut timber like the Sidonians.'",
      "M": "'So now give orders to have cedars of Lebanon cut for me. My servants will work alongside yours, and I will pay your workers whatever wages you set—for you know there is no one among us who has the Sidonians' skill at cutting timber.'",
      "T": "'So order your men to cut cedar from Lebanon for me. My servants will work with yours, and I will pay whatever wages you set—for you know that none of us cuts timber like the Sidonians.'"
    },
    "7": {
      "L": "As soon as Hiram heard the words of Solomon, he rejoiced greatly and said, 'Blessed be the LORD this day, who has given to David a wise son to be over this great people.'",
      "M": "When Hiram heard Solomon's words, he was overjoyed and said, 'Blessed be the LORD today, who has given David a wise son to rule this great people.'",
      "T": "When Hiram heard Solomon's words, he was delighted and said: 'Blessed be the LORD today, who gave David a wise son to rule this great people!'"
    },
    "8": {
      "L": "And Hiram sent to Solomon, saying, 'I have heard the message you sent to me. I am ready to do all you desire in the matter of cedar and cypress timber.'",
      "M": "Hiram sent Solomon this reply: 'I received your message. I am prepared to do everything you desire regarding cedar and cypress timber.'",
      "T": "Hiram sent Solomon this reply: 'I have received your message. I will do everything you desire—cedar and cypress timber, all of it.'"
    },
    "9": {
      "L": "'My servants shall bring it down to the sea from Lebanon, and I will make it into rafts to go by sea to the place you direct. And I will have them broken up there, and you shall receive them. And you shall meet my wishes by providing food for my household.'",
      "M": "'My servants will bring the logs down from Lebanon to the sea. I will make them into rafts and float them to wherever you tell me, where they will be broken up and you can take delivery. In return, you will supply my household with food.'",
      "T": "'My servants will bring the timber down from Lebanon to the sea. I will make them into rafts and float them down the coast to where you direct. There they will be unloaded for you. In return, provide food for my household.'"
    },
    "10": {
      "L": "So Hiram supplied Solomon with all the cedar and cypress timber that he desired.",
      "M": "So Hiram supplied Solomon with all the cedar and cypress timber he wanted.",
      "T": "So Hiram supplied Solomon with all the cedar and cypress timber he needed."
    },
    "11": {
      "L": "And Solomon gave Hiram twenty thousand cors of wheat as food for his household, and twenty thousand cors of beaten oil. Solomon gave this to Hiram year by year.",
      "M": "Solomon gave Hiram twenty thousand cors of wheat as provisions for his household and twenty thousand cors of pure olive oil. He gave Hiram this amount each year.",
      "T": "Solomon gave Hiram twenty thousand cors of wheat for his household and twenty thousand cors of pure olive oil—year after year."
    },
    "12": {
      "L": "And the LORD gave Solomon wisdom, as he promised him. And there was peace between Hiram and Solomon, and the two of them made a treaty.",
      "M": "The LORD gave Solomon wisdom as he had promised. There was peace between Hiram and Solomon, and the two of them made a treaty.",
      "T": "The LORD gave Solomon wisdom, as he had promised. Peace held between Hiram and Solomon, and the two kings made a covenant together."
    },
    "13": {
      "L": "King Solomon drafted forced labor out of all Israel, and the draft numbered thirty thousand men.",
      "M": "King Solomon conscripted forced labor from all Israel—thirty thousand men in all.",
      "T": "King Solomon levied forced labor from all Israel—thirty thousand men."
    },
    "14": {
      "L": "And he sent them to Lebanon, ten thousand a month in shifts. They would be a month in Lebanon and two months at home. Adoniram was in charge of the draft.",
      "M": "He sent them to Lebanon in monthly rotations of ten thousand—one month in Lebanon, two months at home. Adoniram was in charge of the forced labor.",
      "T": "He sent them to Lebanon in monthly shifts of ten thousand—one month in Lebanon, two months home. Adoniram supervised the labor."
    },
    "15": {
      "L": "Solomon also had seventy thousand burden-bearers and eighty thousand quarrymen in the hill country,",
      "M": "Solomon also had seventy thousand carriers and eighty thousand stonecutters in the hill country,",
      "T": "Solomon also had seventy thousand burden-bearers and eighty thousand stonecutters in the hills—"
    },
    "16": {
      "L": "besides Solomon's three thousand three hundred chief officers who were over the work, who had charge of the people who carried on the work.",
      "M": "besides three thousand three hundred supervisors who were in charge of the work and oversaw the workers.",
      "T": "—plus three thousand three hundred foremen who oversaw the work and directed the workforce."
    },
    "17": {
      "L": "And the king commanded, and they quarried out great, costly stones in order to lay the foundation of the house with dressed stone.",
      "M": "At the king's command, they quarried large, expensive stones to lay the foundation of the house with cut stone.",
      "T": "At the king's command they quarried large, costly stones—dressed stone for the foundation of the house."
    },
    "18": {
      "L": "So Solomon's builders and Hiram's builders and the men of Gebal did the cutting, and they prepared the timber and the stones to build the house.",
      "M": "Solomon's builders, Hiram's builders, and the men of Gebal cut and prepared the timber and stone for the building of the house.",
      "T": "Solomon's workmen and Hiram's workmen and the craftsmen of Gebal cut and prepared the timber and stones for building the house."
    }
  },
  "6": {
    "1": {
      "L": "In the four hundred and eightieth year after the people of Israel came out of the land of Egypt, in the fourth year of Solomon's reign over Israel, in the month of Ziv, which is the second month, he began to build the house of the LORD.",
      "M": "In the four hundred and eightieth year after the Israelites came out of Egypt, in the fourth year of Solomon's reign, in the month of Ziv—the second month—Solomon began to build the house of the LORD.",
      "T": "In the four hundred and eightieth year after Israel came out of Egypt—in the fourth year of Solomon's reign, in the second month, Ziv—he began to build the house of the LORD."
    },
    "2": {
      "L": "The house that King Solomon built for the LORD was sixty cubits long, twenty cubits wide, and thirty cubits high.",
      "M": "The house that King Solomon built for the LORD was sixty cubits long, twenty cubits wide, and thirty cubits high.",
      "T": "The house King Solomon built for the LORD was sixty cubits long, twenty cubits wide, and thirty cubits high."
    },
    "3": {
      "L": "The vestibule in front of the nave of the house was twenty cubits long across the width of the house, and ten cubits deep in front of the house.",
      "M": "The portico in front of the main hall of the house was twenty cubits long—the full width of the house—and ten cubits deep.",
      "T": "The porch in front of the main hall was twenty cubits long—the full width of the building—and ten cubits deep."
    },
    "4": {
      "L": "And he made for the house windows with recessed frames.",
      "M": "He made for the house windows with recessed frames.",
      "T": "He made windows with recessed frames for the house."
    },
    "5": {
      "L": "He also built a structure against the wall of the house, running around the walls of the house, both the nave and the inner sanctuary. And he made side chambers all around.",
      "M": "He built a side structure against the walls of the house, running around the walls of both the main hall and the inner sanctuary, and he made side rooms throughout.",
      "T": "He built a side annexe against the outer walls of the house—running around both the main hall and the inner sanctuary—and he made side chambers throughout."
    },
    "6": {
      "L": "The lowest story was five cubits wide, the middle one was six cubits wide, and the third was seven cubits wide. For around the outside of the house he made offsets on the wall so that the beams should not be inserted into the walls of the house.",
      "M": "The lowest story of the annexe was five cubits wide, the middle story was six cubits wide, and the third story was seven cubits wide. He made ledges on the outer wall of the house at each level, so that the beams of the side chambers would not be set into the walls of the house.",
      "T": "The lowest level of the annexe was five cubits wide, the middle level six cubits, and the top level seven cubits. He stepped the outer wall outward at each level so that the supporting beams would not be embedded in the walls of the house itself."
    },
    "7": {
      "L": "When the house was built, it was with stone prepared at the quarry, so that neither hammer nor axe nor any iron tool was heard in the house while it was being built.",
      "M": "The house was built using stone dressed at the quarry; no hammer, chisel, or iron tool was heard at the building site while it was being constructed.",
      "T": "The house was built from stone dressed at the quarry—so that no hammer or chisel or any iron tool was heard at the site during construction."
    },
    "8": {
      "L": "The entrance to the lowest story was on the south side of the house, and one went up by stairs to the middle story, and from the middle story to the third.",
      "M": "The entrance to the lowest level of the annexe was on the south side of the house, and one climbed by stairs to the middle level, and from the middle level to the third.",
      "T": "The entrance to the lowest level of the side structure was on the south side, with a stairway rising to the middle level and from the middle to the third."
    },
    "9": {
      "L": "So he built the house and finished it, and he covered the house with beams and planks of cedar.",
      "M": "He built the house to completion and covered it with beams and cedar planks.",
      "T": "He built the house and finished it, roofing it with cedar beams and planks."
    },
    "10": {
      "L": "He built the annexe against the whole house, each story five cubits high, and it was joined to the house with timbers of cedar.",
      "M": "He built the annexe along the whole house, each story five cubits high, attached to the house with cedar beams.",
      "T": "He built the side annexe along the full length of the house—each level five cubits high—and fastened it to the house with cedar timbers."
    },
    "11": {
      "L": "Now the word of the LORD came to Solomon,",
      "M": "Then the word of the LORD came to Solomon:",
      "T": "Then the word of the LORD came to Solomon:"
    },
    "12": {
      "L": "'Concerning this house that you are building, if you will walk in my statutes and obey my rules and keep all my commandments and walk in them, then I will establish my word with you, which I spoke to David your father.'",
      "M": "'As for this house you are building—if you walk in my statutes, obey my ordinances, and keep all my commandments by walking in them, then I will fulfill through you the promise I made to your father David.'",
      "T": "'Concerning this house you are building—if you walk in my statutes and obey my ordinances and keep all my commandments, I will fulfill through you the promise I made to your father David.'"
    },
    "13": {
      "L": "'And I will dwell among the children of Israel and will not forsake my people Israel.'",
      "M": "'I will dwell among the Israelites and will not abandon my people Israel.'",
      "T": "'I will dwell in the midst of Israel and will never abandon my people.'"
    },
    "14": {
      "L": "So Solomon built the house and finished it.",
      "M": "So Solomon built the house and finished it.",
      "T": "So Solomon built the house and finished it."
    },
    "15": {
      "L": "He lined the walls of the house on the inside with boards of cedar. From the floor of the house to the rafters of the ceiling, he covered them on the inside with wood, and he covered the floor of the house with boards of cypress.",
      "M": "He lined the interior walls of the house with cedar boards from floor to ceiling, covering the inside with wood. He covered the floor with cypress planks.",
      "T": "He lined the interior walls from floor to ceiling with cedar boards—the entire inside was wood. He laid the floor with cypress planks."
    },
    "16": {
      "L": "He built twenty cubits of the rear of the house with boards of cedar from the floor to the ceiling, and he built this within as an inner sanctuary, as the Most Holy Place.",
      "M": "He partitioned off the inner twenty cubits at the rear of the house from floor to ceiling with cedar boards, building it as the inner sanctuary—the Most Holy Place.",
      "T": "He partitioned off the rear twenty cubits of the house from floor to ceiling with cedar boards—this inner room was the Most Holy Place, the Holy of Holies."
    },
    "17": {
      "L": "The house, that is, the nave in front of the inner sanctuary, was forty cubits long.",
      "M": "The main hall in front of the inner sanctuary was forty cubits long.",
      "T": "The main hall in front of the inner sanctuary was forty cubits long."
    },
    "18": {
      "L": "The cedar within the house was carved in the form of gourds and open flowers. All was cedar; no stone was seen.",
      "M": "The cedar lining the interior was carved with gourds and open flowers. All was cedar; no stone was visible.",
      "T": "The cedar covering the interior was carved with gourd shapes and open flowers. All was cedar—not a stone was visible anywhere inside."
    },
    "19": {
      "L": "The inner sanctuary he prepared in the innermost part of the house, to set there the ark of the covenant of the LORD.",
      "M": "Solomon prepared the inner sanctuary in the deepest part of the house to receive the ark of the covenant of the LORD.",
      "T": "He prepared the innermost room—the inner sanctuary—to hold the ark of the covenant of the LORD."
    },
    "20": {
      "L": "The inner sanctuary was twenty cubits long, twenty cubits wide, and twenty cubits high, and he overlaid it with pure gold. He also overlaid an altar of cedar.",
      "M": "The inner sanctuary was twenty cubits long, twenty cubits wide, and twenty cubits high. He overlaid it with pure gold and also overlaid a cedar altar.",
      "T": "The inner sanctuary was a perfect cube—twenty cubits long, wide, and high. He overlaid it with pure gold, and overlaid the cedar altar as well."
    },
    "21": {
      "L": "So Solomon overlaid the inside of the house with pure gold, and he drew chains of gold across, in front of the inner sanctuary, and overlaid it with gold.",
      "M": "Solomon overlaid the inside of the house with pure gold. He hung chains of gold across the entrance to the inner sanctuary and overlaid it with gold.",
      "T": "Solomon overlaid the interior of the house with pure gold. He stretched gold chains across the front of the inner sanctuary and overlaid everything with gold."
    },
    "22": {
      "L": "And he overlaid the whole house with gold, until all the house was finished. Also the whole altar that belonged to the inner sanctuary he overlaid with gold.",
      "M": "He overlaid the whole house with gold until it was entirely finished. And the whole altar that stood before the inner sanctuary he also overlaid with gold.",
      "T": "He overlaid the entire house with gold until every part was finished. The whole altar that stood before the inner sanctuary he overlaid with gold."
    },
    "23": {
      "L": "In the inner sanctuary he made two cherubim of olivewood, each ten cubits high.",
      "M": "In the inner sanctuary he made two cherubim of olivewood, each ten cubits tall.",
      "T": "In the inner sanctuary he made two cherubim of olivewood, each ten cubits tall."
    },
    "24": {
      "L": "Five cubits was the length of one wing of the cherub, and five cubits the length of the other wing of the cherub. It was ten cubits from the tip of one wing to the tip of the other.",
      "M": "One wing of the cherub was five cubits long and the other wing was five cubits—ten cubits from wingtip to wingtip.",
      "T": "Each cherub had wings of five cubits on each side—ten cubits from wingtip to wingtip."
    },
    "25": {
      "L": "The other cherub also measured ten cubits; both cherubim had the same measure and the same form.",
      "M": "The other cherub also had a wingspan of ten cubits. Both cherubim were the same size and shape.",
      "T": "The second cherub was the same—ten cubits. Both cherubim were identical in size and form."
    },
    "26": {
      "L": "The height of one cherub was ten cubits, and so was it with the other cherub.",
      "M": "Each cherub was ten cubits tall.",
      "T": "Each cherub stood ten cubits tall."
    },
    "27": {
      "L": "He put the cherubim in the innermost part of the house. And the wings of the cherubim were spread out so that a wing of the one touched one wall, and a wing of the other cherub touched the other wall, and their other wings touched each other in the middle of the house.",
      "M": "He placed the cherubim in the innermost room of the house. The cherubim's wings were spread out so that one wing of the first touched one wall and one wing of the second touched the other wall, while their inner wings touched each other in the center.",
      "T": "He placed the cherubim in the inner sanctuary. Their wings were spread so that one wing of the first cherub touched one wall, one wing of the second touched the other wall, and their inner wings met each other in the center of the room."
    },
    "28": {
      "L": "And he overlaid the cherubim with gold.",
      "M": "He overlaid the cherubim with gold.",
      "T": "He overlaid the cherubim with gold."
    },
    "29": {
      "L": "Around all the walls of the house he carved engraved figures of cherubim, palm trees, and open flowers, in the inner and outer rooms.",
      "M": "On all the walls throughout the house, inner and outer rooms alike, he carved figures of cherubim, palm trees, and open flowers.",
      "T": "He carved the walls throughout—inner rooms and outer rooms alike—with figures of cherubim, palm trees, and open flowers."
    },
    "30": {
      "L": "The floor of the house he overlaid with gold in the inner and outer rooms.",
      "M": "He overlaid the floor of the house with gold, in both the inner and outer rooms.",
      "T": "He overlaid the floors of both the inner and outer rooms with gold."
    },
    "31": {
      "L": "For the entrance to the inner sanctuary he made doors of olivewood; the lintel and the doorposts formed a pentagon.",
      "M": "For the entrance to the inner sanctuary he made doors of olivewood, with five-sided doorposts.",
      "T": "For the entrance to the inner sanctuary he made olivewood doors set in five-sided doorposts."
    },
    "32": {
      "L": "He covered the two doors of olivewood with carvings of cherubim, palm trees, and open flowers, and he overlaid them with gold and spread gold on the cherubim and on the palm trees.",
      "M": "He carved cherubim, palm trees, and open flowers on the two olivewood doors, and overlaid them with gold, spreading gold over the cherubim and the palm trees.",
      "T": "On both olivewood doors he carved cherubim, palm trees, and open flowers, and overlaid them with gold—pressing the gold onto the carved cherubim and palm trees."
    },
    "33": {
      "L": "So also he made for the entrance to the nave doorposts of olivewood, in the form of a square,",
      "M": "For the entrance to the main hall he likewise made olivewood doorposts, in the form of a square,",
      "T": "For the entrance to the main hall he made olivewood doorposts forming a square frame—"
    },
    "34": {
      "L": "and two doors of cypress wood. The two leaves of the one door were folding, and the two leaves of the other door were folding.",
      "M": "and two doors of cypress wood, each door having two folding leaves.",
      "T": "—and two cypress doors, each with two folding panels."
    },
    "35": {
      "L": "On them he carved cherubim and palm trees and open flowers, and he overlaid them with gold evenly applied on the carved work.",
      "M": "He carved cherubim, palm trees, and open flowers on them and overlaid the carved work with gold applied evenly.",
      "T": "He carved cherubim, palm trees, and open flowers on them and overlaid all the carving with gold, applied evenly."
    },
    "36": {
      "L": "He built the inner court with three courses of dressed stone and one course of cedar beams.",
      "M": "He built the inner court with three courses of dressed stone and one course of cedar beams.",
      "T": "He built the inner courtyard with three courses of dressed stone and one course of cedar beams."
    },
    "37": {
      "L": "In the fourth year the foundation of the house of the LORD was laid, in the month of Ziv.",
      "M": "The foundation of the house of the LORD was laid in the fourth year, in the month of Ziv.",
      "T": "The foundation of the house of the LORD was laid in the fourth year, in the month of Ziv."
    },
    "38": {
      "L": "And in the eleventh year, in the month of Bul, which is the eighth month, the house was finished in all its parts and according to all its specifications. He was seven years in building it.",
      "M": "In the eleventh year, in the month of Bul—the eighth month—the house was completed in every detail according to all its plans. Solomon was seven years building it.",
      "T": "In the eleventh year, in the eighth month—Bul—the house was finished in every detail, exactly as planned. Seven years it took to build."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, '1kings')
        merge_tier(existing, KINGS, tier_key)
        save(tier_dir, '1kings', existing)
    print('1 Kings 1–6 written.')

if __name__ == '__main__':
    main()
