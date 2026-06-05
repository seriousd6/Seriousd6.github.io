"""
MKT Echo Layer — 1 John chapter 5
Run: python3 scripts/zc-echo-1john-5-5.py

Source data used:
- data/interlinear/1john.json
- data/translation/draft/mediating/1john.json (MKT text)
- data/parallels/1john.json (empty — no prototype entries)

Key decisions in this range:
- v7 (Comma Johanneum): The KJV/TR reading adds "the Father, the Word, and the Holy Ghost"
  as heavenly witnesses. This text is absent from all early Greek manuscripts and is widely
  regarded as a later Latin gloss. Echo entry notes Deut 19:15 (legal witness frame) which
  the earthly witnesses of v8 actualize; no Trinitarian echo fabricated from the interpolation.
- "born of God" (vv 1, 4, 18): echoes divine sonship language from Ps 2:7 and 2 Sam 7:14
  rather than OT birth imagery; the connection is through the begetting/sonship register.
- "overcomes the world" (vv 4-5): primary OT register is Dan 7 (saints receiving kingdom)
  plus Ps 2 (the Son's universal dominion) rather than military conquest.
- "sin leading to death" (v 16): Num 15:30-31 (defiant/high-hand sin = cut off from community)
  is the clearest OT parallel; the Johannine category maps onto covenant-exclusion rather
  than capital punishment.
- v 20 identification "He is the true God": direct allusion to the Shema (Deut 6:4) -- the
  author applies Israel's confession of the one true God to Jesus Christ; classified as
  allusion (intentional but not an explicit quote).
"""

import json, pathlib

ROOT = pathlib.Path(__file__).parent.parent

def load_echo(book):
    p = ROOT / 'data' / 'echoes' / f'{book}.json'
    if p.exists():
        return json.loads(p.read_text())
    return {}

def save_echo(book, data):
    p = ROOT / 'data' / 'echoes' / f'{book}.json'
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=None))
    print(f'  wrote {p.relative_to(ROOT)}')

def merge_echo(existing, new_data):
    """Merge echo entries; deduplicate by (type, target) within each verse."""
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


JOHN1 = {
  "5": {
    "1": [
      {
        "type": "allusion",
        "target": "Ps 2:7",
        "note": "\"You are my Son; today I have begotten you\" -- the Psalm establishes the divine begetting of the royal Son; 1 John's phrase \"born of God\" draws on the same register, extending Ps 2's royal sonship to every believer who confesses Jesus as that Son."
      },
      {
        "type": "theme",
        "target": "Deut 6:5",
        "note": "The love of the Father and the love of his children are intertwined: Deuteronomy grounds the whole covenant in loving the LORD your God, and 1 John argues that love for the Father necessarily includes love for his offspring -- the family logic of covenant loyalty."
      }
    ],
    "2": [
      {
        "type": "allusion",
        "target": "Deut 6:5",
        "note": "Deuteronomy places love for God and obedience to his commandments as inseparably paired obligations; 1 John reproduces this exact pairing -- knowing that we love God's children is confirmed by loving God and keeping his commands, collapsing the two great commandments into a single test."
      },
      {
        "type": "theme",
        "target": "Lev 19:18",
        "note": "\"Love your neighbor as yourself\" -- the horizontal dimension of covenant love; 1 John argues that the vertical (love of God) and horizontal (love of his children) are mutually confirming, so that either dimension verifies the other."
      }
    ],
    "3": [
      {
        "type": "allusion",
        "target": "Deut 30:11",
        "note": "\"This commandment I give you today is not too difficult for you\" -- Moses uses the same logic: obedience to God's commands is genuinely achievable, not an impossible burden. 1 John's \"his commands are not burdensome\" is a deliberate echo; the new covenant context (Jer 31:33 -- law written on the heart) explains how what external law could not achieve the indwelling Spirit enables."
      }
    ],
    "4": [
      {
        "type": "theme",
        "target": "Dan 7:18",
        "note": "\"The saints of the Most High will receive the kingdom and will possess it forever\" -- Daniel's vision of the saints overcoming and receiving dominion provides the framework for 1 John's \"victory that overcomes the world\"; the conquest is not military but through faithful endurance, and the outcome is eternal possession."
      },
      {
        "type": "allusion",
        "target": "Ps 44:3",
        "note": "\"It was not by their sword that they won the land... it was your right hand\" -- the Psalm establishes that decisive victory belongs to God, not human effort; 1 John names faith as the instrument of victory, placing the agency with God's gift rather than the believer's achievement."
      }
    ],
    "5": [
      {
        "type": "allusion",
        "target": "Ps 2:12",
        "note": "\"Blessed are all who take refuge in him [the Son]\" -- Ps 2 ends by pointing toward the Son as the locus of safety and blessing; 1 John's question \"Who is it that overcomes the world?\" and answer \"only the one who believes that Jesus is the Son of God\" echoes this Psalm's climax: the one who confesses the Son and takes refuge in him is the one who stands."
      },
      {
        "type": "type",
        "target": "Ps 2:7",
        "note": "The divine declaration \"You are my Son\" in Ps 2 anticipates the confession 1 John names as the ground of victory -- \"Jesus is the Son of God.\" The Davidic king as God's son is a type that finds its substance in Jesus; faith in this identity is what overcomes the world."
      }
    ],
    "6": [
      {
        "type": "allusion",
        "target": "Zech 13:1",
        "note": "\"On that day a fountain will be opened for the house of David... to cleanse them from sin and impurity\" -- Zechariah's eschatological fountain of cleansing (water) and purification from death (blood) prepares the imagery John uses: Jesus came by water and blood, and the Spirit testifies, fulfilling this opening of a cleansing fountain."
      },
      {
        "type": "type",
        "target": "Exod 24:8",
        "note": "\"This is the blood of the covenant that the LORD has made with you\" -- Moses sprinkled blood to ratify the Sinai covenant; 1 John's emphasis that Jesus came by blood (not water only) points to the covenant-ratifying function of Christ's death, the blood that establishes the new covenant (Jer 31:31)."
      }
    ],
    "7": [
      {
        "type": "allusion",
        "target": "Deut 19:15",
        "note": "\"A matter must be established by the testimony of two or three witnesses\" -- the Mosaic legal requirement for verified testimony provides the framework for 1 John's argument: the divine testimony about the Son is established by multiple witnesses, meeting and exceeding the Torah standard for reliable witness."
      }
    ],
    "8": [
      {
        "type": "allusion",
        "target": "Deut 19:15",
        "note": "The three earthly witnesses -- Spirit, water, blood -- fulfill and surpass the two-or-three-witness legal requirement; their agreement (\"the three are in agreement\") establishes the legal sufficiency of God's case for his Son. The Torah's evidentiary standard is not merely met but tripled."
      },
      {
        "type": "type",
        "target": "Exod 12:7",
        "note": "The blood applied to the doorposts served as a protective sign -- a type of the blood of Christ that now testifies to his sacrifice. The blood in 1 John 5:8 carries this protective-testimony function: it speaks (cf. Heb 12:24) of the covenant made through the Passover Lamb."
      }
    ],
    "9": [
      {
        "type": "theme",
        "target": "Isa 43:10",
        "note": "\"You are my witnesses, declares the LORD\" -- Isaiah establishes the pattern of God authenticating his own witnesses; 1 John inverts the frame: if we accept human witness, how much more must we accept God's own testimony about his Son. The reliability of divine witness is already a major theme in Isa 40-55."
      },
      {
        "type": "type",
        "target": "Isa 55:4",
        "note": "\"I have made him a witness to the peoples\" -- the servant-David figure is appointed as God's designated witness; this type reaches its fullness in the Son of God to whom the Father testifies in 1 John 5:9. The testimony flows downward from the Father through his appointed witness."
      }
    ],
    "10": [
      {
        "type": "allusion",
        "target": "Deut 32:4",
        "note": "\"He is the Rock; his works are perfect; all his ways are just. A faithful God who does no wrong\" -- Moses's Song establishes God's utter truthfulness as his character; to disbelieve God's testimony about his Son is therefore to call this God a liar, inverting everything Deut 32 declares about him."
      },
      {
        "type": "allusion",
        "target": "Ps 2:7",
        "note": "The testimony God has given about his Son echoes the Ps 2 declaration (\"You are my Son\"); to reject the Son is to reject the Father's own sworn word. The Psalm's royal decree is the foundation on which God's testimony in 1 John 5:10 rests."
      }
    ],
    "11": [
      {
        "type": "type",
        "target": "Dan 12:2",
        "note": "\"Many who sleep in the dust of the earth will awake -- some to everlasting life\" -- the clearest OT anticipation of individual resurrection to eternal life; 1 John's declaration that \"God has given us eternal life\" presents this OT hope as a present possession given to those in the Son, not merely a future event to be awaited."
      },
      {
        "type": "shadow",
        "target": "Gen 2:7",
        "note": "God breathing life into Adam -- the original act of divine life-giving -- casts the shadow that 1 John fills: eternal life is not a human achievement but a gift given by God. \"This life is in his Son\" updates the pattern: where Adam received creaturely life, believers receive eschatological life through the second Adam."
      }
    ],
    "12": [
      {
        "type": "theme",
        "target": "Deut 30:15",
        "note": "\"See, I set before you today life and prosperity, death and destruction\" -- Moses's binary framing of the covenant choice provides the structural precedent for 1 John's stark division: whoever has the Son has life; whoever does not, does not. The covenant has always been structured around this binary; now it crystallizes in relation to the Son."
      },
      {
        "type": "shadow",
        "target": "Prov 8:35",
        "note": "\"Whoever finds wisdom finds life, and receives favor from the LORD\" -- personified Wisdom declares that life comes through her; 1 John replaces Wisdom with the Son (a move prepared by the Wisdom Christology of the NT), so that life is now explicitly located in the Son as God's wisdom incarnate."
      }
    ],
    "13": [
      {
        "type": "fulfillment",
        "target": "Jer 31:34",
        "note": "\"They will all know me\" -- the new covenant's central promise of direct, assured knowledge of God; 1 John writes precisely to give believers this assurance (\"so that you may know that you have eternal life\"), presenting the letter itself as a covenant document delivering the new-covenant knowledge Jeremiah promised."
      }
    ],
    "14": [
      {
        "type": "allusion",
        "target": "Ps 34:15",
        "note": "\"The eyes of the LORD are on the righteous, and his ears are attentive to their cry\" -- the Psalm grounds the confidence that God hears his people; 1 John's \"confidence we have in approaching God\" that \"he hears us\" is built on this covenant-established pattern of divine attentiveness to those who belong to him."
      },
      {
        "type": "allusion",
        "target": "2 Chr 7:14",
        "note": "\"If my people... humble themselves and pray and seek my face... then I will hear from heaven\" -- the Solomonic promise of a hearing God conditions that hearing on covenant posture; 1 John's condition \"if we ask anything according to his will\" echoes this framing: prayer according to God's will is the new-covenant equivalent of seeking his face."
      }
    ],
    "15": [
      {
        "type": "allusion",
        "target": "Isa 65:24",
        "note": "\"Before they call I will answer; while they are still speaking I will hear\" -- Isaiah's eschatological vision of a God who hears before the request is complete; 1 John's certainty that \"we have what we asked\" extends this promise to the present experience of those in the Son."
      },
      {
        "type": "allusion",
        "target": "1 Kgs 18:37",
        "note": "\"Answer me, LORD, answer me\" -- Elijah's bold petition and its immediate answer is the paradigmatic OT example of God hearing and granting what is asked; 1 John's confidence in being heard builds on this pattern of a God who responds to his servants."
      }
    ],
    "16": [
      {
        "type": "allusion",
        "target": "Num 15:30",
        "note": "\"But anyone who sins defiantly... blasphemes the LORD and must be cut off from their people\" -- the distinction between unintentional sin (atoneable by offering) and defiant/high-hand sin (resulting in being cut off from the covenant community) is the closest OT parallel to 1 John's \"sin leading to death.\" The covenant-exclusion function maps onto the Johannine category."
      },
      {
        "type": "theme",
        "target": "Ezek 18:4",
        "note": "\"The soul who sins is the one who will die\" -- Ezekiel's individual accountability principle establishes death as the covenant consequence of sin; 1 John's distinction acknowledges this while carving out a category of sin that remains within the reach of intercession, implying that not all sin has exhausted the possibility of repentance and life."
      }
    ],
    "17": [
      {
        "type": "theme",
        "target": "Lev 4:2",
        "note": "Leviticus distinguishes classes of sin -- unintentional violations -- and provides offerings for each class; 1 John's affirmation that \"all wrongdoing is sin\" clarifies rather than flattens: the variety of sin types the Torah catalogued are all genuine sin, yet not all are beyond intercession and remediation."
      }
    ],
    "18": [
      {
        "type": "allusion",
        "target": "Ps 121:3",
        "note": "\"He who watches over you will not slumber... the LORD watches over you\" -- the Psalm's repeated \"keep/watch\" language (shaman) maps onto 1 John's \"the One who was born of God keeps them safe\"; the Psalmist promises divine protection from all harm, and 1 John confirms this protection extends to keeping the evil one at bay."
      },
      {
        "type": "type",
        "target": "Zech 3:2",
        "note": "\"The LORD rebuke you, Satan!\" -- Zechariah's vision of the adversary being silenced by divine authority anticipates 1 John's assurance that the evil one \"cannot harm\" those whom the Son keeps; the rebuking of the accuser is a type of Christ's decisive victory over the evil one."
      }
    ],
    "19": [
      {
        "type": "type",
        "target": "Gen 3:1",
        "note": "The serpent's deception of Adam and Eve is the entry point of the evil one's dominion over creation; 1 John's statement that \"the whole world lies in the power of the evil one\" traces back to this originary act. The contrast -- \"we are of God\" -- maps the same division that began in Eden between those who listen to God and those who follow the deceiver."
      },
      {
        "type": "theme",
        "target": "Dan 10:13",
        "note": "The angelic prince of Persia opposing God's messenger reveals the cosmic dimension of conflict behind earthly events; Daniel's vision provides the theological backdrop for 1 John's claim that the world system lies under an evil governing power -- not chaos, but organized opposition with a personal ruler."
      }
    ],
    "20": [
      {
        "type": "fulfillment",
        "target": "Jer 31:34",
        "note": "\"They will all know me\" -- the new covenant's central promise of universal, direct knowledge of God is explicitly fulfilled in the Son's coming: \"the Son of God has come and has given us understanding, so that we may know him who is true.\" The understanding given by the Son is the new-covenant faculty Jeremiah said God would inscribe."
      },
      {
        "type": "allusion",
        "target": "Deut 6:4",
        "note": "\"Hear, O Israel: the LORD our God, the LORD is one\" -- the Shema's declaration of the one true God is in view when 1 John identifies Jesus Christ as \"the true God and eternal life\"; the author applies Israel's foundational monotheistic confession to the Son, claiming for Christ the identity the Shema reserves for YHWH alone."
      }
    ],
    "21": [
      {
        "type": "allusion",
        "target": "Deut 4:15",
        "note": "\"You saw no form of any kind... Therefore watch yourselves carefully so that you do not become corrupt and make an idol\" -- Moses's prohibition against idolatry grounds the warning in the invisibility of God; 1 John closes with the same imperative in a Greco-Roman context where idols were omnipresent in civic and domestic life."
      },
      {
        "type": "allusion",
        "target": "Isa 44:9",
        "note": "\"All who make idols are nothing, and the things they treasure are worthless\" -- Isaiah's extended polemic against idolatry (Isa 44:9-20) establishes the theological absurdity of worshiping what the craftsman made; 1 John's closing \"keep yourselves from idols\" resonates with this Isaianic tradition: having known the true God, to turn to idols is an act of epistemological inversion."
      }
    ]
  }
}


def main():
    existing = load_echo('1john')
    merge_echo(existing, JOHN1)
    save_echo('1john', existing)
    print('1 John 5 echoes written.')

if __name__ == '__main__':
    main()
