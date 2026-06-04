"""
MKT 2 Kings chapter 25 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-2kings-25-25.py

This is the final chapter of 2 Kings: the fall of Jerusalem, the deportation,
Gedaliah's brief governorship, his assassination, the flight to Egypt, and the
hopeful epilogue of Jehoiachin's release.

Translation decisions:
- H3068 (יהוה): "LORD" (small-caps convention) in L/M; "the LORD" in T.
  Consistent with all prior 2 Kings scripts.
- H430 (אֱלֹהִים): "God" — not directly used in ch. 25, but carried from prior chapters.
- H5019 (נְבוּכַדְנֶאצַּר): "Nebuchadnezzar" — standard English form, consistent.
- H5018 (נְבוּזַרְאֲדָן): "Nebuzaradan" — standard transliteration.
- H7227 (רַב) in compound title "captain of the guard": rendered "captain of the guard" in
  L/M; "chief of the bodyguard" or "chief executioner" in T where the force of his role
  (executing prisoners) is in view (vv. 8, 18–20).
- H6667 (צִדְקִיָּהוּ): "Zedekiah" throughout.
- H1436 (גְּדַלְיָהוּ): "Gedaliah" — appointed governor (H6485 = "appoint/oversee").
- H1540 (גָּלָה): "carried into exile" in L/M; "taken into exile / gone from its land" in T.
  The summary in v. 21 "Judah was carried away from its land" is the theological
  climax of the entire book — T gives it full weight.
- H192 (אֱוִיל מְרֹדַךְ): "Evil-merodach" — transliterated form, retaining traditional
  English spelling.
- H3078 (יְהוֹיָכִין): "Jehoiachin" — the captive Davidic king whose release ends the book.
- H7218 (רֹאשׁ) "lift up the head" (v. 27): idiom meaning to pardon/restore from prison;
  L preserves the idiom literally; M/T clarify as "released" / "lifted… out of prison."
- H2896 (טוֹב) "kindly" (v. 28): "kindly" in L/M; "with genuine honour" in T.
  Evil-merodach's treatment of Jehoiachin is consistently positive in the text.
- H5178 (נְחֹשֶׁת): "bronze" throughout (vv. 13–17); the temple bronze items catalogued
  in vv. 13–17 recall 1 Kgs 7 — T notes the theological weight of their removal.
- H4409/Gedaliah son of Ahikam son of Shaphan: Shaphan was Josiah's royal secretary
  (22:8); Ahikam protected Jeremiah (Jer 26:24). The family pedigree is theologically
  significant — T surfaces it (v. 22).
- H3458 (יִשְׁמָאֵל) of royal seed (v. 25): "of the royal family" in M/T — his Davidic
  blood makes the assassination a politically charged act, not mere banditry.
- Aspect decisions:
  - Waw-consecutive imperfects = narrative past throughout.
  - The summary clause in v. 21 is a qatal (perfect) summarising completed history:
    "Judah was carried into exile from its land." T gives this finality.
  - The epilogue (vv. 27–30) uses narrative perfects that look back from a later vantage
    point; T renders the ongoing daily allowance (v. 30) as present continuity.
- OT intertextuality:
  - v. 7: Zedekiah's blinding fulfils both Jer 34:3 (he would see the king of Babylon)
    and Ezek 12:13 (he would go to Babylon but not see it). T notes this.
  - v. 9: The burning of the temple echoes and reverses 1 Kgs 9:3 — the Name that dwelt
    there is now departing in judgment (cf. Ezek 10–11).
  - v. 13: The bronze items recall 1 Kgs 7:15–47 (Solomon's temple furnishings). T notes
    that the book is completing a symmetry: what Solomon built, Babylon unmakes.
  - v. 21: The exile is the covenant curse of Deut 28:63–64 fully enacted.
  - v. 22: Gedaliah's family (Shaphan lineage) connects to the Josiah reform narrative
    of chs. 22–23.
  - vv. 27–30: The ending echoes the Joseph story pattern (prisoner elevated by foreign
    king). The Davidic covenant (2 Sam 7) is not over — it flickers on in Babylon.
    This epilogue is the seed of the hope that Ezra, Nehemiah, and the prophets will grow.
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


KINGS2 = {
  "25": {
    "1": {
      "L": "And it came to pass in the ninth year of his reign, in the tenth month, on the tenth day of the month, that Nebuchadnezzar king of Babylon came, he and all his host, against Jerusalem, and pitched against it; and they built siege-works against it round about.",
      "M": "In the ninth year of Zedekiah's reign, on the tenth day of the tenth month, Nebuchadnezzar king of Babylon advanced against Jerusalem with his entire army. They encamped against it and built siege works all around it.",
      "T": "In the ninth year of Zedekiah's reign — the tenth day of the tenth month — Nebuchadnezzar king of Babylon marched on Jerusalem with his full military force. They ringed the city with siege works. The judgment Manasseh's generation had stored up was arriving at last."
    },
    "2": {
      "L": "And the city was besieged unto the eleventh year of king Zedekiah.",
      "M": "The city remained under siege until the eleventh year of King Zedekiah.",
      "T": "Month after month the siege held. The city endured for two years — through Zedekiah's ninth year, his tenth, and into his eleventh — with no relief coming."
    },
    "3": {
      "L": "And on the ninth day of the fourth month the famine prevailed in the city, and there was no bread for the people of the land.",
      "M": "On the ninth day of the fourth month the famine had become severe in the city; there was no bread left for the people of the land.",
      "T": "By the ninth day of the fourth month, the siege had done its quiet, terrible work: famine gripped Jerusalem so hard that not a morsel of bread remained for anyone in the city."
    },
    "4": {
      "L": "And the city was broken up, and all the men of war fled by night by the way of the gate between the two walls, which is by the king's garden (the Chaldeans were round about the city), and the king went the way of the Arabah.",
      "M": "The city wall was breached. All the soldiers fled by night through the gate between the two walls near the king's garden, while the Chaldeans had the city surrounded. The king himself made for the Arabah.",
      "T": "The wall gave way. Under cover of darkness every soldier still capable of movement slipped out through the narrow passage between the double walls near the royal garden — the one gap the Chaldean ring had not fully closed. Zedekiah went with them, heading south toward the Jordan Valley, toward the open desert."
    },
    "5": {
      "L": "And the army of the Chaldeans pursued after the king and overtook him in the plains of Jericho; and all his army were scattered from him.",
      "M": "The Chaldean army pursued the king and overtook him in the plains of Jericho; his entire army scattered and abandoned him.",
      "T": "The Chaldeans gave chase and ran Zedekiah down in the broad plains near Jericho. His army dissolved around him as men fled in every direction. The king stood alone."
    },
    "6": {
      "L": "So they took the king and brought him up to the king of Babylon at Riblah, and they spoke judgment with him.",
      "M": "The soldiers seized the king and brought him to the king of Babylon at Riblah, where judgment was pronounced on him.",
      "T": "They seized Zedekiah and hauled him north to Riblah in Hamath, where Nebuchadnezzar had established his headquarters. There the great king of Babylon passed sentence on the last king of Judah."
    },
    "7": {
      "L": "And they slew the sons of Zedekiah before his eyes, and put out the eyes of Zedekiah, and bound him with fetters of bronze, and carried him to Babylon.",
      "M": "They killed Zedekiah's sons before his eyes, then gouged out his eyes, bound him in bronze shackles, and brought him to Babylon.",
      "T": "Zedekiah watched his sons executed one by one — the last sight he would ever see. Then his eyes were put out. Bound in bronze chains, he was led to Babylon blind. Both Jeremiah and Ezekiel were vindicated at once: he met the king of Babylon face to face, and he went to Babylon, yet he never saw it."
    },
    "8": {
      "L": "And in the fifth month, on the seventh day of the month — which is the nineteenth year of king Nebuchadnezzar king of Babylon — Nebuzaradan captain of the guard, a servant of the king of Babylon, came unto Jerusalem.",
      "M": "On the seventh day of the fifth month — the nineteenth year of King Nebuchadnezzar of Babylon — Nebuzaradan the captain of the guard, a servant of the king of Babylon, arrived in Jerusalem.",
      "T": "A month after the city fell, on the seventh day of the fifth month — Nebuchadnezzar's nineteenth regnal year — Nebuzaradan, his chief officer and head of the bodyguard, arrived in Jerusalem with orders to complete the destruction."
    },
    "9": {
      "L": "And he burned the house of the LORD, and the king's house; and all the houses of Jerusalem, even every great man's house, he burned with fire.",
      "M": "He burned the house of the LORD, the king's palace, and all Jerusalem; every important building he set on fire.",
      "T": "Nebuzaradan put the torch to the temple of the LORD — the house built by Solomon to shelter the divine Name, the crown of Israel's worship, the axis of the nation's life. The palace followed. Then every great house in Jerusalem was reduced to cinders. The city became ash and ruin."
    },
    "10": {
      "L": "And all the army of the Chaldeans that were with the captain of the guard brake down the walls of Jerusalem round about.",
      "M": "The entire Chaldean army under the captain of the guard tore down the walls of Jerusalem on every side.",
      "T": "Then the walls themselves — the stone perimeter that had defined the city of David for centuries — were pulled down by the Chaldean forces until nothing stood on every side."
    },
    "11": {
      "L": "Now the rest of the people that were left in the city, and the fugitives that fell away to the king of Babylon, with the rest of the multitude, did Nebuzaradan captain of the guard carry away into exile.",
      "M": "Nebuzaradan the captain of the guard carried into exile the rest of the people remaining in the city, those who had defected to the king of Babylon, and the rest of the populace.",
      "T": "Everyone still in the city was rounded up for deportation: those who had survived the siege, those who had surrendered to the Babylonians earlier, and any remaining crowds. Nebuzaradan marched them all away into exile."
    },
    "12": {
      "L": "But of the poor of the land the captain of the guard left some to be vinedressers and husbandmen.",
      "M": "But the captain of the guard left behind some of the poorest people of the land to work the vineyards and fields.",
      "T": "Only the very poorest — those with nothing worth taking — were left in place, kept on as agricultural laborers to maintain the land's productivity for the empire."
    },
    "13": {
      "L": "And the pillars of bronze that were in the house of the LORD, and the stands, and the bronze sea that was in the house of the LORD, did the Chaldeans break in pieces, and carried the bronze to Babylon.",
      "M": "The Chaldeans broke up the bronze pillars in the house of the LORD, the movable stands, and the bronze sea, and carried all the bronze to Babylon.",
      "T": "What Solomon had made with such care was dismantled for scrap: the twin bronze pillars that had flanked the temple entrance, the great wheeled stands, and the enormous bronze Sea — all were shattered and the metal carried off to Babylon. What 1 Kings 7 had catalogued in loving detail, this chapter strips away."
    },
    "14": {
      "L": "And the pots and the shovels and the snuffers and the dishes and all the vessels of bronze wherewith they ministered, took they away.",
      "M": "They took away the pots, the shovels, the snuffers, the dishes, and all the bronze utensils used in the temple service.",
      "T": "Even the smaller implements of priestly ministry were stripped out: the cooking pots, the ash shovels, the wick trimmers, the sprinkling bowls — the tools of daily service in the house of the LORD, taken piece by piece."
    },
    "15": {
      "L": "And the firepans and the bowls — that which was of gold, in gold, and that which was of silver, in silver — the captain of the guard took away.",
      "M": "The captain of the guard also took the firepans and the bowls — those of gold as gold, those of silver as silver.",
      "T": "The firepans and libation bowls were sorted and catalogued by metal before being hauled away — gold inventoried separately from silver. The sacred furnishings of worship had become a treasury audit."
    },
    "16": {
      "L": "The two pillars, the one sea, and the stands which Solomon had made for the house of the LORD — the bronze of all these vessels was without weight.",
      "M": "The bronze taken from the two pillars, the one sea, and the movable stands that Solomon had made for the house of the LORD was beyond weighing.",
      "T": "The total volume of bronze stripped from what Solomon had built — the two great pillars, the sea, the stands — was simply too vast to be weighed. It had taken decades to make; it was gone in days."
    },
    "17": {
      "L": "Eighteen cubits was the height of the one pillar; and upon it was a capital of bronze, the height of the capital being three cubits, and the wreathen work and the pomegranates upon the capital round about, all of bronze; and like unto these had the second pillar with wreathen work.",
      "M": "One pillar stood eighteen cubits high; its bronze capital was three cubits high, decorated all around with a network of bronze pomegranates. The second pillar was the same, with its own network.",
      "T": "Each of the twin pillars had stood eighteen cubits tall — nearly thirty feet — crowned by a capital three cubits high, ringed with bronze pomegranates woven into open latticework. The craftsmen who built them had cared about every detail. The text records the dimensions one final time as the pillars disappear into Babylon, as if to say: these things were real, and now they are gone."
    },
    "18": {
      "L": "And the captain of the guard took Seraiah the chief priest, and Zephaniah the second priest, and the three keepers of the threshold;",
      "M": "The captain of the guard seized Seraiah the chief priest, Zephaniah the second priest, and the three keepers of the entrance.",
      "T": "Nebuzaradan also arrested the religious leadership that had survived: Seraiah the high priest, Zephaniah the deputy high priest, and the three officials who had served as gatekeepers of the temple."
    },
    "19": {
      "L": "And out of the city he took an officer that was set over the men of war, and five men of them that were in the king's presence, which were found in the city, and the principal scribe of the host, who mustered the people of the land, and threescore men of the people of the land, that were found in the city.",
      "M": "From the city he took an officer commanding the soldiers, five royal advisers found in the city, the secretary of the army commander who had conscripted the people, and sixty men of the common people found in the city.",
      "T": "From the wreckage of the city he pulled out whoever still held authority: a military commandant, five of the king's council members who had remained in the city, the army's chief secretary who had administered the draft levy, and sixty ordinary citizens — a cross-section of Jerusalem's civil, military, and common life."
    },
    "20": {
      "L": "And Nebuzaradan captain of the guard took these and brought them to the king of Babylon to Riblah.",
      "M": "Nebuzaradan the captain of the guard took all of them and brought them to the king of Babylon at Riblah.",
      "T": "Nebuzaradan marched this entire group — priests, officials, soldiers, and citizens — north to Riblah, where Nebuchadnezzar was waiting."
    },
    "21": {
      "L": "And the king of Babylon smote them and slew them at Riblah in the land of Hamath. So Judah was carried away from its land.",
      "M": "The king of Babylon had them struck down and killed at Riblah in the land of Hamath. So Judah was taken into exile from its land.",
      "T": "Nebuchadnezzar had them all executed at Riblah in the territory of Hamath. With that, the account ends in four words of irreversible finality: Judah was carried from its land — the land promised to Abraham, granted through Joshua, held through centuries of obedience and disobedience, and now lost. The covenant curses of Deuteronomy 28 had come to their full conclusion."
    },
    "22": {
      "L": "And as for the people that remained in the land of Judah, whom Nebuchadnezzar king of Babylon had left, even over them he made Gedaliah the son of Ahikam, the son of Shaphan, governor.",
      "M": "Over the people who remained in the land of Judah whom Nebuchadnezzar king of Babylon had left behind, he appointed Gedaliah son of Ahikam, son of Shaphan, as governor.",
      "T": "The land was not entirely emptied. For the remnant left in Judah, Nebuchadnezzar appointed Gedaliah son of Ahikam as governor. The appointment was not arbitrary: Ahikam had once shielded Jeremiah (Jer 26:24), and his father Shaphan had been Josiah's royal secretary who first brought the rediscovered law-scroll to the king. Gedaliah came from a family that had stood for the faith."
    },
    "23": {
      "L": "And when all the captains of the armies, they and their men, heard that the king of Babylon had made Gedaliah governor, they came to Gedaliah at Mizpah, even Ishmael the son of Nethaniah, and Johanan the son of Careah, and Seraiah the son of Tanhumeth the Netophathite, and Jaazaniah the son of the Maacathite, they and their men.",
      "M": "When all the commanders of the forces and their men heard that the king of Babylon had appointed Gedaliah as governor, they came to him at Mizpah — Ishmael son of Nethaniah, Johanan son of Careah, Seraiah son of Tanhumeth the Netophathite, and Jaazaniah son of the Maacathite, together with their men.",
      "T": "Word spread to the guerrilla commanders who had evaded capture. One by one they came in from the hills and fields to Mizpah where Gedaliah held his court: Ishmael, Johanan, Seraiah, Jaazaniah — each with his band of followers. It looked like the beginning of a reconstruction."
    },
    "24": {
      "L": "And Gedaliah sware to them and to their men and said to them, Fear not to be the servants of the Chaldeans: dwell in the land and serve the king of Babylon, and it shall be well with you.",
      "M": "Gedaliah swore an oath to them and their men: 'Do not be afraid to serve the Chaldeans. Live in the land, serve the king of Babylon, and it will go well for you.'",
      "T": "Gedaliah bound himself with an oath to reassure them: 'There is nothing to fear from Babylonian rule. Settle in the land, submit to Nebuchadnezzar, and you will not only survive — you will prosper.' It was the counsel of hard-won wisdom: the very course Jeremiah had urged throughout the crisis."
    },
    "25": {
      "L": "But it came to pass in the seventh month, that Ishmael the son of Nethaniah, the son of Elishama, of the seed royal, came, and ten men with him, and smote Gedaliah, that he died, and the Jews and the Chaldeans that were with him at Mizpah.",
      "M": "But in the seventh month, Ishmael son of Nethaniah, son of Elishama, of royal descent, came with ten men and struck down Gedaliah so that he died, along with the Jews and Chaldeans who were with him at Mizpah.",
      "T": "The fragile hope lasted only weeks. In the seventh month, Ishmael — of Davidic blood, evidently unwilling to accept Babylonian-appointed governance — arrived with ten men and assassinated Gedaliah, killing also the Judeans and Babylonian officials present. The last organized remnant in the land was gone."
    },
    "26": {
      "L": "And all the people, both small and great, and the captains of the armies arose and came to Egypt; for they were afraid of the Chaldeans.",
      "M": "Then all the people, great and small, and the commanders of the forces set out and went to Egypt, because they feared reprisal from the Chaldeans.",
      "T": "In the panic that followed, all who remained — ordinary people and military commanders alike — abandoned Judah and fled to Egypt. They feared Babylonian vengeance for Gedaliah's murder would fall on them all. The land fell empty. The story that had begun with Abraham coming out of Egypt had now reversed: the children of the promise were running back into it."
    },
    "27": {
      "L": "And it came to pass in the thirty-seventh year of the exile of Jehoiachin king of Judah, in the twelfth month, on the twenty-seventh day of the month, that Evilmerodach king of Babylon, in the year that he began to reign, lifted up the head of Jehoiachin king of Judah out of prison.",
      "M": "In the thirty-seventh year of the exile of Jehoiachin king of Judah, on the twenty-seventh day of the twelfth month, Evil-merodach king of Babylon, in the first year of his own reign, released Jehoiachin king of Judah from prison.",
      "T": "But the book does not end in ash and empty land. Thirty-seven years into his captivity, on the twenty-seventh day of the twelfth month, a new king came to the throne of Babylon. Evil-merodach, son of Nebuchadnezzar, chose as one of his first acts to open the prison cell of Jehoiachin king of Judah. The Davidic heir was still alive."
    },
    "28": {
      "L": "And he spoke kindly to him and set his throne above the throne of the kings that were with him in Babylon.",
      "M": "He spoke kindly to him and gave him a seat of honor above the other captive kings held in Babylon.",
      "T": "Evil-merodach treated Jehoiachin with genuine respect — spoke to him with courtesy, seated him above the other subject kings being held in Babylon. The man who had surrendered Jerusalem to Nebuchadnezzar thirty-seven years earlier was now the most honored of captive monarchs."
    },
    "29": {
      "L": "And he changed his prison garments, and he did eat bread continually before him all the days of his life.",
      "M": "Jehoiachin changed out of his prison clothes, and he ate regularly at the king's table for the rest of his life.",
      "T": "Jehoiachin's prison clothes were exchanged for garments suited to a king. He took a place at Evil-merodach's table and dined there every day for the rest of his life — no longer a prisoner kept in isolation, but a guest, even if an exiled one."
    },
    "30": {
      "L": "And his allowance was a continual allowance given him of the king, a daily rate for every day, all the days of his life.",
      "M": "He received a regular daily allowance from the king for the rest of his life.",
      "T": "Day after day the provisions came — a steady royal stipend that never stopped. In this quiet, daily generosity from a pagan king, the book's last note is sounded: the Davidic line had not been extinguished. The promises made to David were not void. The candle still burned, far from home, in Babylon — and the reader who knew the rest of the story would understand that it was not finished yet."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, '2kings')
        merge_tier(existing, KINGS2, tier_key)
        save(tier_dir, '2kings', existing)
    print('2 Kings 25 written.')

if __name__ == '__main__':
    main()
