"""
echo | Numbers | chapters 4–5
Run: python3 scripts/zc-echo-numbers-4-5-fill.py

Ch 4: Levitical transport duties — Kohathite ark-carrying with covered holy things;
      "lest they die" restriction types Heb 10:19-22 boldness; 30-year service start
      types Luke 3:23; veil-covered ark types 2 Cor 3:14-16 glory-veiling.
Ch 5: Camp purity and the sotah (bitter water ordeal); removal of unclean from camp
      types Heb 13:11-13; confession/restitution types 1 John 1:9/Col 2:14; the
      scroll-curse washed into water and drunk types Gal 3:13 / Rev 10:8-10.
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

ECHO = {
  "4": {
    "3": [
      {"type": "allusion", "target": "Luke 3:23", "note": "The service age for Levitical tabernacle labor is thirty to fifty years old (Num 4:3,23,30,35,39,43,47); Luke records that Jesus began his ministry at 'about thirty years of age' (Luke 3:23). The priestly-service age floor of thirty is the threshold at which sacred service begins; Jesus enters his public ministry at the same threshold, fulfilling the Levitical service-commencement age in his own priestly vocation."}
    ],
    "5": [
      {"type": "type", "target": "2 Cor 3:14", "note": "When the camp breaks up, Aaron and his sons cover the ark of the covenant with the inner veil (the parochet of Exod 26:31), then with dolphin skin and a cloth of solid blue. The covering of the ark during transit — hiding the glory of the mercy seat and cherubim — is the type of the veil that lay over Moses's face (Exod 34:33-35) and, by extension, over Israel's understanding of the Mosaic covenant: 'to this day whenever Moses is read a veil lies over their hearts' (2 Cor 3:15). The veil is lifted only in Christ (2 Cor 3:14-16)."}
    ],
    "15": [
      {"type": "allusion", "target": "Heb 10:19", "note": "The sons of Kohath shall carry the covered holy things, 'but they must not touch the holy things, lest they die' — the prohibition against touching the most holy objects even while carrying them is the Levitical form of the principle that direct approach to divine holiness is lethal for sinful humanity. Hebrews 10:19-22 announces its reversal: 'we have confidence to enter the holy places by the blood of Jesus.' The 'lest they die' restriction is answered by the 'confidence to enter' of the new covenant — the same holiness approached, but through the blood that makes approach safe rather than lethal."}
    ],
    "20": [
      {"type": "allusion", "target": "Heb 9:8", "note": "The Kohathites must not go in to look at the holy things even for a moment, lest they die — the prohibition on seeing the covered holy things, even briefly, is the spatial form of the principle Hebrews 9:8 articulates: 'the Holy Spirit is indicating this: the way into the holy places is not yet opened as long as the first section is still standing.' The curtain that restricted vision and access is the same that Christ's death tears open (Matt 27:51), making the formerly lethal 'look' into the holy place the confident 'drawing near' of Heb 10:22."}
    ]
  },
  "5": {
    "2": [
      {"type": "allusion", "target": "Heb 13:11", "note": "YHWH commands the removal of everyone unclean from the camp — anyone with a skin disease, a discharge, or who is defiled by the dead must be put outside the camp. 'For the bodies of those animals whose blood is brought into the holy places by the high priest as a sacrifice for sin are burned outside the camp. So Jesus also suffered outside the gate in order to sanctify the people through his own blood' (Heb 13:11-12). Christ bears the outside-the-camp status of the unclean, identifying with the excluded in order to transform their exclusion into sanctification."}
    ],
    "7": [
      {"type": "allusion", "target": "Col 2:14", "note": "The confession of sin and restitution with the one-fifth (chomesh) surcharge — the verbal acknowledgment followed by payment that exceeds the original debt. Paul describes Christ's atonement as 'canceling the record of debt that stood against us with its legal demands. This he set aside, nailing it to the cross' (Col 2:14). The debt acknowledged in the restitution formula (the 'record of debt' that requires confession and payment) is blotted out through Christ's cross rather than paid by the offender's own chomesh — the surplus is absorbed in Christ rather than extracted from the debtor."}
    ],
    "17": [
      {"type": "type", "target": "Gal 3:13", "note": "The priest takes holy water and mixes dust from the tabernacle floor into it to create the bitter water of cursing for the suspected adulteress — the curse is literally dissolved into water and drunk. The book of curses is washed into the water (v.23); the curse becomes the drink. Christ 'became a curse for us — for it is written, &ldquo;Cursed is everyone who is hanged on a tree&rdquo;' (Gal 3:13): he drinks the cup of cursing in the place of those who deserve it. The sotah's bitter curse-water drunk by the (possibly guilty) woman is the type of the curse-cup Christ drinks at Gethsemane ('let this cup pass from me,' Matt 26:39) and on the cross."}
    ],
    "23": [
      {"type": "allusion", "target": "Rev 10:10", "note": "The priest writes the curses in a scroll and washes them off into the bitter water; the woman drinks the curse-laden water. In Rev 10:8-10, John is commanded to eat the scroll: 'it was sweet as honey in my mouth, but when I had eaten it my stomach was made bitter.' The scroll-curse absorbed into liquid and consumed is the structure both share. The prophetic vocation of bearing the word of judgment — sweet in receiving, bitter in delivering — echoes the sotah's bitter water that reveals guilt or innocence when internalized."}
    ],
    "28": [
      {"type": "type", "target": "Rom 8:1", "note": "If the woman is clean and has not defiled herself, she is free (nivtah) and will conceive children — the acquittal of the innocent woman under the sotah ordeal. Christ undergoes the ultimate sotah ordeal — drinking the cup of God's wrath — as the one who is innocent, so that the guilty may receive the verdict of the innocent: 'there is therefore now no condemnation for those who are in Christ Jesus' (Rom 8:1). The acquitted woman who conceives children is the type of the redeemed community, found not guilty through Christ's bearing of the curse, now bearing the fruit of new life."}
    ]
  }
}

def main():
    e = load_echo('numbers')
    merge_echo(e, ECHO)
    save_echo('numbers', e)
    print('Numbers 4-5 echo written.')

if __name__ == '__main__':
    main()
