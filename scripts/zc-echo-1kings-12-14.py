"""
echo — 1 Kings 12–14
run: python3 scripts/zc-echo-1kings-12-14.py

Ch12: Division of the kingdom — Rehoboam's folly, Jeroboam's golden calves
Ch13: Man of God from Judah — prophecy against Bethel, old prophet's deception
Ch14: Ahijah's oracle — Jeroboam condemned; Rehoboam's sins; Shishak's plunder
"""

import json, pathlib

ROOT = pathlib.Path(__file__).parent.parent

def load_echo(book):
    p = ROOT / 'data' / 'echoes' / f'{book}.json'
    return json.loads(p.read_text()) if p.exists() else {}

def save_echo(book, data):
    p = ROOT / 'data' / 'echoes' / f'{book}.json'
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=None))
    print(f'  wrote {p.relative_to(ROOT)}')

def merge_echo(existing, new_data):
    for ch, verses in new_data.items():
        if ch not in existing:
            existing[ch] = {}
        for v, entries in verses.items():
            if v not in existing[ch]:
                existing[ch][v] = entries
            else:
                seen = {(e['type'], e['target']) for e in existing[ch][v]}
                for e in entries:
                    if (e['type'], e['target']) not in seen:
                        existing[ch][v].append(e)
                        seen.add((e['type'], e['target']))

KINGS1_ECHO = {
  "12": {
    "16": [
      {"type": "fulfillment", "target": "John 1:11", "note": "The people said to Rehoboam: What portion do we have in David? We have no inheritance in the son of Jesse. To your tents, O Israel! — this is the permanent political fulfillment of Sheba's cry in 2 Sam 20:1, which was a preview; the formula 'no portion in David' is the language of inheritance-rejection; John 1:11 announces the same rejection at its ultimate depth: he came to his own, and his own people did not receive him; the Davidic king is rejected by the very people he came to rule"},
      {"type": "allusion", "target": "Matt 21:43", "note": "The northern tribes' renunciation of the Davidic house — What portion have we in David? — withdraws from the covenant king the very kingdom he was anointed to rule; Jesus applies this to the religious leadership in Matt 21:43: the kingdom of God will be taken from you and given to a people producing its fruits; the split at Shechem is the historical type of which Matt 21 is the antitype"}
    ],
    "28": [
      {"type": "allusion", "target": "Acts 7:40", "note": "Jeroboam said: Here are your gods, O Israel, who brought you up out of the land of Egypt — the speech is verbatim Aaron's (Exod 32:4: 'These are your gods, O Israel'); Stephen cites Aaron's speech in Acts 7:40 as Exhibit A of Israel's persistent idolatry and its pattern of rejecting what YHWH provides in favor of self-made substitutes; Jeroboam's calves at Bethel and Dan repeat the Sinai golden calf, not as an accident but as a conscious founding act of the rival cultus"},
      {"type": "allusion", "target": "1 Cor 10:7", "note": "Jeroboam's golden calves and the feast he invented (v33) replicate the Sinai idolatry pattern that Paul warns the Corinthians about explicitly: do not be idolaters as some of them were; as it is written, the people sat down to eat and drink and rose up to play (1 Cor 10:7, quoting Exod 32:6); Paul reads the golden calf episode as a type of false worship for any subsequent covenant community"}
    ]
  },
  "13": {
    "4": [
      {"type": "allusion", "target": "Matt 12:10", "note": "When King Jeroboam heard the word of the man of God crying against the altar at Bethel, Jeroboam stretched out his hand from the altar, saying, Seize him! And his hand, which he stretched out against him, dried up, so that he could not draw it back — a hand stretched out at a false altar and withered as divine judgment; in Matt 12:10-13 Jesus restores a withered hand at the synagogue on the Sabbath, demonstrating his authority over the false religious structures the Pharisees were defending; the same gesture of hostility against YHWH's representative produces withering in 1 Kgs 13; Jesus reverses the pattern"},
      {"type": "allusion", "target": "Acts 13:11", "note": "The king's hand withers at his gesture against the man of God — the motif of the hand of an opponent of YHWH's messenger being struck recurs in Elymas the sorcerer struck blind at Paul's word (Acts 13:11: the hand of the Lord is upon you, and you will be blind); in both cases the sign is temporary and serves to authenticate the divine messenger and demonstrate divine protection over the prophetic word"}
    ]
  },
  "14": {
    "8": [
      {"type": "allusion", "target": "Acts 13:22", "note": "YHWH's indictment of Jeroboam includes the contrast: you have not been like my servant David, who kept my commandments and followed me with all his heart, doing only what was right in my eyes — the same evaluative formula Paul distills when announcing the Davidic Messiah in Acts 13:22: I have found in David the son of Jesse a man after my heart, who will do all my will; every king in the divided monarchy is measured against this standard, and the standard is ultimately fulfilled only by David's greater son"},
      {"type": "allusion", "target": "Heb 3:10", "note": "The contrast between Jeroboam (whose heart went wholly after Baal-substitutes) and David (who followed YHWH with all his heart) is the Old Testament form of the heart-diagnosis that runs through Hebrews: today if you hear his voice, do not harden your hearts; Jeroboam is the paradigm of the hardened heart — he received a prophetic word (1 Kgs 11:31-38), was given a conditional promise (vv37-38), and immediately on receiving power built the calves (12:28); the heart that will not follow is not a failure of information but of orientation"}
    ],
    "13": [
      {"type": "allusion", "target": "Rom 11:5", "note": "Of all Jeroboam's household the child Abijah alone shall come to the grave, because in him there is found something pleasing to YHWH — within the condemned dynasty YHWH identifies one pure soul who receives mercy: a merciful death before judgment falls (v12), mourning by all Israel (v13), and a honorable burial (unlike the rest of the household, v10-11); this micro-expression of the remnant principle — one elect individual within a condemned corporate body — is the structure Paul names in Rom 11:5: at the present time there is a remnant chosen by grace"},
      {"type": "allusion", "target": "Rev 3:4", "note": "The one child in Jeroboam's house who has something pleasing to YHWH receives particular mercy when judgment sweeps the rest away — exactly the promise to Sardis: you have still a few names in Sardis, people who have not soiled their garments, and they will walk with me in white, for they are worthy (Rev 3:4); the pattern is consistent across the OT and NT: within a corrupt institution YHWH marks those who remain faithful and treats them differently in the hour of judgment"}
    ]
  }
}

def main():
    e = load_echo('1kings')
    merge_echo(e, KINGS1_ECHO)
    save_echo('1kings', e)
    print('1kings ch12-14 echo: done')

if __name__ == '__main__':
    main()
