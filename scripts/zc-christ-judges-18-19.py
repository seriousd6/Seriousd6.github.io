"""
MKT Christ Commentary — Judges chapters 18–19
Run: python3 scripts/zc-christ-judges-18-19.py

Every verse receives an entry connecting it to the trajectory toward Christ.

Ch18: Danite migration and idolatry — the tribe that lost its inheritance;
      stolen sacred objects; Jonathan son of Moses as the idolatrous priest;
      the persistence of false worship alongside true; anticipates the need for
      a permanent king who establishes righteous worship

Ch19: The Levite's concubine — the Gibeah atrocity; the Sodom parallel within
      Israel; the concubine as the most vulnerable person sacrificed by those
      who should protect her; the 12-piece summons as covenant lawsuit;
      anticipates the need for a true king who protects the vulnerable

Christological keys:
- Dan's lost inheritance: Christ as the one who secures the inheritance that
  human failure cannot (Heb 9:15 — an eternal inheritance)
- Stolen idols → Jonathan's corrupt priesthood: Christ as the true high priest
  who cannot be bought or corrupted (Heb 7:26 — holy, innocent, unstained)
- "All the days the house of God was at Shiloh" (18:31): the end of Shiloh
  (1 Sam 4) points toward the one who will build the permanent house (2 Sam 7;
  John 2:19-21 — the temple of his body)
- The concubine as the silenced victim: Christ as the one who speaks for the
  voiceless; Isa 53:7 — he was oppressed, yet he opened not his mouth;
  the voiceless victim whose death summons a response
- The 12-piece summons: covenant justice demands a response; Christ's death
  is the ultimate covenant summons — 'What will you do with Jesus?' (Matt 27:22)
- Gibeah/Sodom parallel within Israel: the depth of human sin requiring not
  just a judge or a king but a savior from outside the cycle
"""

import json, pathlib

ROOT = pathlib.Path(__file__).parent.parent

def load_comm(layer, book):
    p = ROOT / 'data' / 'commentary' / layer / f'{book}.json'
    return json.loads(p.read_text()) if p.exists() else {}

def save_comm(layer, book, data):
    p = ROOT / 'data' / 'commentary' / layer / f'{book}.json'
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=None))
    print(f'  wrote {p.relative_to(ROOT)}')

def merge_comm(existing, new_data):
    for ch, verses in new_data.items():
        if ch not in existing:
            existing[ch] = {}
        for v, html in verses.items():
            if v not in existing[ch]:
                existing[ch][v] = html

CHRIST = {
  "18": {
    "1": "<p>Dan's failure to inherit its allotment is a corporate version of the individual failure that runs through Judges: the covenant gift requires covenant faithfulness to receive and hold. The tribe that refuses to fight for its God-given territory mirrors the servant who buries his talent (Matt 25:18) rather than risking it. Christ comes as the one who secures the inheritance that human failure cannot secure: 'He is the mediator of a new covenant, so that those who are called may receive the promised eternal inheritance' (Heb 9:15). Where Dan loses its earthly allotment through spiritual failure, Christ purchases an eternal inheritance for his people through his own blood — an inheritance that cannot be taken, cannot be lost, 'kept in heaven for you' (1 Pet 1:4).</p>",
    "14": "<p>The Danites' practical logic — take the sacred objects for the new city — reflects the human tendency to substitute religious apparatus for covenant relationship. The graven image, the ephod, the teraphim are devices for accessing divine power without covenant submission. Jesus confronts this instinct in every encounter with those who want miracle without discipleship, sign without faith, bread without the bread of life (John 6:26-27 — 'You are seeking me not because you saw signs, but because you ate your fill of the loaves. Do not labor for the food that perishes'). The Danites carry idols northward; they will not carry YHWH's presence, because YHWH's presence cannot be stolen or relocated — it follows covenant faithfulness.</p>",
    "19": "<p>'Come with us and be to us a father and a priest. Is it better for you to be priest to the house of one man, or to be priest to a tribe and clan in Israel?' The promotion offered to the hired Levite is a temptation to exchange authentic vocation for status and security. The temptation of Christ in the wilderness echoes this pattern: the devil offers 'all the kingdoms of the world and their glory' (Matt 4:8-9) in exchange for a shortcut to authority. The Levite's 'heart was glad' at the promotion (v20); Jesus responds 'Be gone, Satan' (Matt 4:10). The corruption of priestly ministry by institutional advancement anticipates Christ who 'did not count equality with God a thing to be grasped, but emptied himself, taking the form of a servant' (Phil 2:6-7).</p>",
    "30": "<p>'Jonathan son of Gershom, son of Moses' — Moses's own grandson as the founding priest of Israel's idolatrous northern shrine. The revelation is a type of every generation's capacity for covenant apostasy: no genealogy protects against it. Yet it also points to the one whose faithfulness is not genealogical but intrinsic — Christ 'the same yesterday and today and forever' (Heb 13:8), whose priesthood is not inherited from fallible ancestors but constituted by 'the power of an indestructible life' (Heb 7:16). Jonathan's priesthood continues until exile; Christ's priesthood continues forever: 'He holds his priesthood permanently, because he continues forever. Consequently, he is able to save to the uttermost those who draw near to God through him' (Heb 7:24-25).</p>",
    "31": "<p>'All the days that the house of God was at Shiloh.' The bracket around the Dan cult — from its founding to the fall of Shiloh (1 Sam 4, ca. 1050 BCE) — marks the entire pre-monarchic period as a time of compromised worship. The destruction of Shiloh clears the ground for the question 2 Sam 7 will answer: where will YHWH's permanent dwelling be? David asks to build a house for God; God promises to build a house (dynasty) for David. Christ is the ultimate answer: 'Destroy this temple, and in three days I will raise it up' (John 2:19). The true Shiloh — the one to whom the gathering of the peoples belongs (Gen 49:10) — is not a building or a city but a person: 'the Word became flesh and tabernacled among us' (John 1:14).</p>"
  },
  "19": {
    "1": "<p>The Levite's concubine is the most vulnerable person in Israel's social system: a secondary wife with no inheritance rights, no legal recourse, dependent entirely on the protection of her household. The entire narrative of ch19 is the story of that protection failing at every level — her husband, the host, the citizens of Gibeah. Christ's ministry is defined by the reversal of exactly this pattern: 'The Spirit of the Lord... has anointed me to proclaim good news to the poor... to set at liberty those who are oppressed' (Luke 4:18, citing Isa 61:1). The concubine's story — her abandonment and death — is a type of every silenced victim; Christ is the one who 'does not break a bruised reed or quench a smoldering wick' (Matt 12:20, citing Isa 42:3).</p>",
    "2": "<p>The concubine's departure — whatever its cause (infidelity or anger) — and the Levite's going to 'speak to her heart' to bring her back is a type of the divine pursuit of the straying covenant partner. Hosea uses exactly this imagery: Israel has played the harlot, yet YHWH goes after her: 'Therefore I will hedge up her way with thorns... And there I will speak tenderly to her' (Hos 2:6,14). Christ's parable of the lost sheep — the shepherd leaving the ninety-nine to find the one (Luke 15:4-7) — is the ultimate expression of this pursuit. The Levite's journey to Bethlehem to 'speak to her heart' is a pale reflection of the lengths to which the divine husband goes to reclaim his people.</p>",
    "14": "<p>'The sun went down on them near Gibeah, which belongs to Benjamin.' The geographical irony is the text's theological verdict: the Levite chose the Israelite city over the foreign Jebus, trusting covenant kinship over ethnic difference — and found Gibeah of Benjamin more dangerous than any Canaanite city. The cross reveals the same irony at cosmic scale: 'He came to his own, and his own people did not receive him' (John 1:11). The covenant people crucified their covenant Lord. Gibeah of Benjamin is the geographical preview of Jerusalem's rejection of its king — the most protected people being the source of the greatest covenant violation.</p>",
    "22": "<p>The men of Gibeah demand the Levite for sexual violation — the Sodom scene replayed within Israel (Gen 19:4-5). This is the text's structural argument: Israel, with the covenant and the tabernacle and the law, has reproduced the worst act of the cities destroyed by divine fire. Paul makes the same argument about the universality of human sinfulness: 'All have sinned and fall short of the glory of God' (Rom 3:23). The covenant does not produce righteousness automatically; it requires the Spirit writing the law on the heart (Jer 31:33). The Gibeah horror demonstrates that external covenant membership is insufficient — what is needed is the new birth (John 3:3) and the new covenant (Jer 31:31-34), which Christ establishes through his death.</p>",
    "25": "<p>The Levite seizes his concubine and thrusts her out to the mob — the most devastating act of a man who came to win her back with tender words. He who came to 'speak to her heart' abandons her when it costs him. This is the anti-type of Christ who, when faced with the choice of saving himself or his people, chose his people: 'For our sake he made him to be sin who knew no sin, so that in him we might become the righteousness of God' (2 Cor 5:21). The Levite saves himself by sacrificing her; Christ saves his people by sacrificing himself. The contrast is total: the one who should have protected her delivers her to death; the one who owed nothing to sinners 'gave himself as a ransom for all' (1 Tim 2:6).</p>",
    "28": "<p>'There was no answer.' The concubine is dead at the threshold. Her silence echoes through the prophetic tradition: 'He was oppressed, and he was afflicted, yet he opened not his mouth; like a lamb that is led to the slaughter, and like a sheep that before its shearers is silent, so he opened not his mouth' (Isa 53:7). The voiceless victim whose death cannot speak for itself — Christ's death, like the concubine's, is the death that should have been prevented by those who should have protected. Yet Christ's silence at his trial is not powerlessness but sovereign submission: 'Do you think that I cannot appeal to my Father, and he will at once send me more than twelve legions of angels?' (Matt 26:53). The silenced one is also the one who 'always lives to make intercession' (Heb 7:25).</p>",
    "29": "<p>The 12-piece summons — the concubine's body distributed to all Israel's territories — is a covenant lawsuit in action: the covenant people are confronted with the evidence of covenant violation and summoned to respond. The 12 pieces for 12 tribes invoke the covenant-animal-cutting of Gen 15 and Jer 34. At the cross, the ultimate covenant lawsuit is issued: 'He was pierced for our transgressions; he was crushed for our iniquities' (Isa 53:5). The death that demands a response. 'What shall I do with Jesus who is called Christ?' (Matt 27:22) is Pilate's form of the same question the Levite's summons asks: you have seen what was done; what will you do? The concubine's death demands tribal accountability; Christ's death demands cosmic accountability.</p>",
    "30": "<p>'Nothing like this has happened or been seen from the day the children of Israel came up from the land of Egypt until this day.' The historical maximum — the worst thing since the Exodus — is the narrator's verdict. It also points forward: the book's descent into depravity reaches a nadir that cannot be resolved by another judge. Only a king can restore covenant order; only the ultimate King can restore the covenant itself. The Gibeah horror is the OT's way of saying what Rom 7:24 says: 'Wretched man that I am! Who will deliver me from this body of death?' The question has no human answer. The answer comes from outside the cycle: 'Thanks be to God through Jesus Christ our Lord!' (Rom 7:25). Judges ends with a cry that can only be answered by the King who comes.</p>"
  }
}

def main():
    c = load_comm('mkt-christ', 'judges')
    merge_comm(c, CHRIST)
    save_comm('mkt-christ', 'judges', c)
    print(f'judges mkt-christ: wrote {sum(len(v) for v in CHRIST.values())} verses across ch 18-19')

if __name__ == '__main__':
    main()
