"""
MKT Echo — 1 Samuel chapters 4–8
Run: python3 scripts/zc-echo-1samuel-4-8.py

Ch 4: Philistines capture the ark — Hophni and Phinehas die, Eli dies, Ichabod born.
      Echo anchors: ark theology, glory-departure (Ichabod), presumptuous use of the sacred.
Ch 5: Ark in Philistia — Dagon prostrated, plagues on Ashdod/Gath/Ekron.
      Echo anchors: YHWH's sovereignty over false gods, divine holiness.
Ch 6: Ark returned — golden guilt offerings, Beth-shemesh struck for looking inside.
      Echo anchors: return of divine presence, awe before YHWH's holiness.
Ch 7: Samuel at Mizpah — national repentance, Philistine defeat, Ebenezer stone.
      Echo anchors: intercession, repentance-and-deliverance, covenant memory.
Ch 8: Israel demands a king — Samuel's warning, YHWH's concession.
      Echo anchors: rejection of YHWH as king, warning about human kingship.
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

ECHOES = {
  "4": {
    "3": [
      {"type": "theme", "target": "1 Cor 10:7-8", "note": "Israel brings the ark of the covenant from Shiloh, assuming its physical presence will guarantee military victory — 'Let it come among us, that it may save us.' The presumptuous use of the sacred as a talisman is the same failure Paul warns against in 1 Cor 10:7-8: Israel's sacramental participation (cloud, sea, manna) did not protect those who acted presumptuously. Presence of the covenant sign does not guarantee blessing when covenant faithfulness is absent."}
    ],
    "11": [
      {"type": "allusion", "target": "Ezek 10:18", "note": "The ark of God was captured and Hophni and Phinehas died — YHWH surrenders the ark, the visible symbol of his presence, to Philistine hands. This is the first step in the glory-departure that reaches its fullest expression in Ezekiel 10:18 ('Then the glory of YHWH departed from over the threshold of the house') and anticipates the Shekinah withdrawal that precedes Jerusalem's fall in 586. The ark's capture is the enacted departure of YHWH's covenant presence from a covenant-violating people."}
    ],
    "21": [
      {"type": "type", "target": "John 17:11", "note": "Ichabod — 'the glory has departed from Israel' (<em>gālāh kāḇôḏ</em>) — the name given by Phinehas's dying wife encapsulates the theological catastrophe of the ark's capture. The departure of the glory from Israel in 1 Samuel 4 sets up the entire arc of YHWH's returning glory: Ezekiel's vision of the returning glory (43:1-5), the glory filling the second temple (Hag 2:9), and the incarnation — 'the Word became flesh and dwelt among us, and we have seen his glory' (John 1:14). Jesus's prayer that the Father's name be kept holy among his disciples (John 17:11) is the NT expression of the Ichabod reversal."}
    ]
  },
  "5": {
    "3": [
      {"type": "type", "target": "Rev 19:20", "note": "Dagon fell face down before the ark of YHWH — the Philistine deity prostrated before YHWH's covenant sign. The next day Dagon's head and hands were cut off, leaving only the torso. The humiliation of a false deity by YHWH's presence is the OT pattern of divine sovereignty over all pretenders that reaches its climax in Revelation 19:20 where the beast and false prophet are thrown alive into the lake of fire at Christ's appearing. YHWH's victory over Dagon is the preliminary type of the eschatological defeat of all false gods."}
    ],
    "6": [
      {"type": "theme", "target": "Acts 5:11", "note": "YHWH's hand was heavy upon the Ashdodites and he ravaged them — the divine judgment on those who presume to possess YHWH's sacred presence without covenant relationship. The heavy hand of YHWH on Philistia mirrors the 'great fear' that fell on the entire church after Ananias and Sapphira's deaths (Acts 5:11). Both incidents demonstrate that proximity to the divine presence without reverence produces judgment rather than blessing."}
    ]
  },
  "6": {
    "7": [
      {"type": "allusion", "target": "Num 19:2", "note": "The Philistines send the ark back on a new cart drawn by two nursing cows — the 'new cart' (<em>ʿăgālāh ḥăḏāšāh</em>) and the ritually unused cows echo the red heifer legislation (Num 19:2: 'a red heifer without defect, on which a yoke has never come'). The Philistines intuitively apply a principle of ritual purity — unused vessels for holy things — that mirrors Israel's own Torah. Even pagan recognition of holiness's demands points toward the NT's call for a holy and consecrated body as the dwelling place of God's Spirit (1 Cor 6:19-20)."}
    ],
    "19": [
      {"type": "theme", "target": "Heb 12:28-29", "note": "YHWH struck the men of Beth-shemesh because they looked into the ark — 70 men died. The severity of the judgment for irreverent curiosity about the holy demonstrates that YHWH's holiness is not an abstraction but an active reality that destroys what approaches it without proper covenant standing. Hebrews 12:28-29 draws on this pattern: 'let us offer to God acceptable worship, with reverence and awe, for our God is a consuming fire.' The NT does not soften the OT's holy-fire theology; it grounds it in Christ's mediation."}
    ]
  },
  "7": {
    "12": [
      {"type": "allusion", "target": "Rom 8:31", "note": "Samuel sets up the Ebenezer stone and says: 'Thus far YHWH has helped us' (<em>ʿaḏ-hēnnāh ʿăzārānû YHWH</em>). The memorial stone marking accumulated divine faithfulness is the OT basis for Paul's confident assertion: 'If God is for us, who can be against us?' (Rom 8:31). The Ebenezer ('stone of help') is covenant memory made material: the past deliverances are the ground of present confidence. Christian assurance is built on the same logic: the cross and resurrection are the Ebenezer stone of the new covenant."}
    ],
    "5": [
      {"type": "type", "target": "Heb 7:25", "note": "Samuel said: 'I will pray to YHWH for you' — Samuel's intercessory prayer at Mizpah is accompanied by a burnt offering that YHWH answers with thunder that routs the Philistines (vv9-11). Samuel as prophet-intercessor whose prayer is tied to sacrifice is a structural type of Christ's high-priestly intercession: 'He always lives to make intercession for them' (Heb 7:25). The sacrifice-plus-intercession that brings covenant deliverance is the pattern fulfilled once for all at the cross, where sacrifice and intercession coincide."}
    ]
  },
  "8": {
    "7": [
      {"type": "allusion", "target": "John 19:15", "note": "YHWH says to Samuel: 'They have not rejected you, but they have rejected me from being king over them' (<em>ʾōtî māʾăsû mimleḵ ʿălêhem</em>). Israel's demand for a human king over against YHWH's kingship is the OT prototype of John 19:15: 'We have no king but Caesar' — the explicit rejection of YHWH's kingship by his covenant people before Pilate. Both rejections take the same form: choosing human political power over divine sovereignty. Both produce catastrophic consequences: Saul's failed dynasty; the cross that becomes YHWH's ultimate vindication."}
    ],
    "20": [
      {"type": "theme", "target": "Matt 20:25-26", "note": "Israel says: 'We want to be like all the nations, and our king shall govern us and go out before us and fight our battles.' The desire to be like the nations (<em>kəḵol-haggôyim</em>) is the rejection of Israel's distinctive covenant identity as a kingdom of priests and a holy nation (Exod 19:6). Jesus inverts this explicitly: 'The rulers of the Gentiles lord it over them... it shall not be so among you' (Matt 20:25-26). The NT community's distinctiveness from 'all the nations' is grounded in the same theological principle that Israel violated in 1 Sam 8 — YHWH's sovereignty over worldly power structures."}
    ]
  }
}

def main():
    existing = load_echo('1samuel')
    merge_echo(existing, ECHOES)
    save_echo('1samuel', existing)
    print('1samuel ch 4-8: echoes written')

if __name__ == '__main__':
    main()
