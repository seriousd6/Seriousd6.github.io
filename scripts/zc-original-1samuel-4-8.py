"""
MKT Original Commentary — 1 Samuel chapters 4–8
Run: python3 scripts/zc-original-1samuel-4-8.py

The Ark Narrative (chs 4-7) and the demand for a king (ch8):
philological commentary on Hebrew vocabulary, ANE background,
theological vocabulary, and key terms.

Book-level keys for this section:
- kabod (כָּבוֹד) — glory: the Ichabod naming (4:21) is the book's most concentrated
  theology of divine presence; the departure of the glory anticipates Ezek 10
- Dagon's fall (ch5): the toppling of the Philistine grain-god before the Ark
  demonstrates YHWH's supremacy over all rival deities
- Ebenezer (7:12): eben ha-ezer = stone of help — the geographical marker of
  covenant memory; YHWH's faithful provision marked in the landscape
- mišpat hammelek (8:9,11): the "manner of the king" — Samuel's warning list;
  the constitutional description of royal excess
- "they have rejected me from being king" (8:7): YHWH's theological interpretation
  of the request for kingship
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

ORIGINAL = {
  "4": {
    "3": "<p>The elders' proposal — 'Let us bring the ark of the covenant of YHWH from Shiloh to us, so it may come among us and save us from the power of our enemies' — treats the Ark as a divine weapon that can be deployed independently of covenant faithfulness. The Ark is <em>ʾărôn bərît YHWH</em> (ark of the covenant of YHWH), the physical locus of divine presence between the cherubim. The elders' logic inverts the relationship: the Ark is to be brought to the army, not the army brought into covenant alignment with YHWH. The same magical theology of religious objects — use the right apparatus, get the right result — is the root error of every subsequent Israelite cult failure (Micah's shrine, Jeroboam's calves, the bronze serpent, Nehushtan). What cannot be manipulated is YHWH's sovereign presence; the Ark is not a talisman but a covenant sign.</p>",
    "4": "<p>The Ark is identified here as <em>ʾărôn bərît YHWH ṣəḇāʾôt yōšēḇ hakkərūḇîm</em> — 'the ark of the covenant of YHWH of armies who is enthroned upon the cherubim.' The title <em>YHWH ṣəḇāʾôt</em> (YHWH of armies/hosts) appears here for one of its first occurrences in the narrative corpus (also 1:3, 11; it is rare in the Pentateuch). The divine warrior epithet marks YHWH as the commander of cosmic and terrestrial armies — precisely the character that Israel is invoking when it brings the Ark into battle. The enthroned-upon-cherubim epithet identifies YHWH's throne-presence as the reality the Ark represents: the portable throne of the cosmic king. The irony is devastating — Israel attempts to manipulate into battle the throne of the One who cannot be manipulated.</p>",
    "21": "<p>The naming of the child <em>ʾîḵāḇôḏ</em> — 'Where is the glory?' or 'No glory' — is the Ark Narrative's theological center. <em>Kāḇôḏ</em> (כָּבוֹד) is the most comprehensive Hebrew term for YHWH's weighty, substantial, self-manifesting presence — the cloud-and-fire glory of Exod 16:10; 24:16; 40:34-35. The mother's explanation: <em>gālāh kāḇôḏ miyyiśrāʾēl</em> — 'the glory has gone into exile (<em>gālāh</em>) from Israel.' The verb <em>gālāh</em> is the exile verb — the same word used for Israel's deportation to Babylon. The glory departing is the beginning of the exile trajectory that will culminate in Ezekiel's vision of the divine chariot-throne rising from the temple and departing eastward (Ezek 10:18-19; 11:22-23). <em>Ichabod</em> is the OT's single most concentrated naming of divine absence.</p>"
  },
  "5": {
    "3": "<p>Dagon falls on his face before the Ark: <em>wayyipōl dāgôn lᵉpānāyw ʾarṣāh</em> — 'Dagon fell on his face to the ground' in the classic prostration posture of a vassal before a superior. <em>Dāgôn</em> is the chief deity of the Philistine cities, attested in texts from Ugarit (as Baal's father), Mari, and the Tell Dan stele context. The name is disputed — possibly from <em>dāg</em> (fish) or <em>dāgān</em> (grain). The prostration of the Philistine deity before YHWH's Ark is the text's argument: YHWH's sovereign presence does not require Israelite compliance to dominate rival deities; even in captivity, the covenant God of Israel reduces the most powerful Philistine god to prostration. The theme recurs in Acts 5 (Ananias and Sapphira falling before the Spirit's judgment) and Phil 2:10 (every knee bowing at the name of Jesus).</p>",
    "4": "<p>The second morning: Dagon's head and both hands are severed and lie on the threshold — only <em>dāgôn dāgôn</em>, his torso, remains. The amputation of head and hands is the fate of defeated warriors (cf. 1 Sam 17:51 — David cuts off Goliath's head; 31:9 — the Philistines cut off Saul's head). Dagon is thus treated as a defeated enemy-soldier, his power symbolically neutralized. The word <em>miptān</em> (threshold) marks the place as the boundary where the Dagon cult's authority ended; the narrator notes that the Philistine priests 'do not tread on the threshold of Dagon in Ashdod to this day' — a surviving cultic taboo preserving the memory of this defeat embedded in Philistine practice itself.</p>",
    "6": "<p>The <em>yāḏ YHWH</em> — 'hand of YHWH' — is the theological category for direct divine action. The phrase appears six times in the Ark Narrative (5:6, 7, 9, 11; 6:3, 5), transforming the entire Philistine ordeal into a demonstration of YHWH's sovereign intervention without Israelite agency. <em>Yāḏ YHWH</em> is the Exodus vocabulary: the ten plagues are the work of YHWH's 'mighty hand and outstretched arm' (Deut 26:8). The Philistine ordeal is a mini-Exodus in reverse — YHWH operates in Philistine territory with the same plagues-and-forced-release pattern: tumors and mice parallel the Exodus plagues; the gold offerings parallel the despoliation of Egypt; the Ark's return on a cart parallels Israel's departure from Egypt. The Philistine priests make this explicit in 6:6: 'Why should you harden your hearts as the Egyptians and Pharaoh hardened their hearts?'</p>"
  },
  "6": {
    "6": "<p>The Philistine priests' reference to Egypt: <em>lāmmāh tᵉḵabbəḏû ʾet lᵉḇaḇḵem kaʾăšer kibbəḏû miṣrayim wəparʿōh ʾet libbām</em> — 'Why do you harden your hearts (<em>kāḇad</em> = to make heavy) as Egypt and Pharaoh hardened their hearts?' The Exodus vocabulary is deliberately employed: the verb for 'harden' here is <em>kāḇad</em> (to be heavy), the same root as <em>kāḇôḏ</em> (glory). The Philistine priests have theological knowledge of the Exodus — a remarkable detail that positions the Ark Narrative as an extension of YHWH's sovereignty beyond Israel's borders. Pharaoh hardened his heart (<em>kāḇad</em>) and was destroyed; the Philistines are urged to learn from that precedent rather than repeat it. The same vocabulary of 'hardening' recurs in Mark 6:52 (the disciples' hardened hearts after the feeding) and Heb 3:8 (the warning not to harden hearts as in the wilderness).</p>",
    "19": "<p>YHWH strikes the men of Beth-shemesh for looking into the Ark — <em>kî rāʾû bǎʾărôn YHWH</em>, 'for they looked into the ark of YHWH.' Beth-shemesh (<em>bêt šemeš</em>, 'house of the sun') is a sun-cult city; the men treat the Ark with the same casual curiosity appropriate to a cult object that could be inspected. The holiness of the Ark is absolute — it cannot be looked into any more than YHWH's face can be seen directly (Exod 33:20). The number struck (50,070 in the MT, probably a textual corruption) is less important than the theological point: proximity to divine holiness without covenant preparation is lethal. This is the theological ground of the NT's 'our God is a consuming fire' (Heb 12:29) and of the NT's emphasis on Christ as the mediator who makes approach to the holy God possible (Heb 10:19-22 — 'we have confidence to enter the holy places by the blood of Jesus').</p>"
  },
  "7": {
    "3": "<p>Samuel's call to national repentance uses the technical vocabulary of covenant renewal: <em>hāšîḇû ʾet lᵉḇaḇḵem ʾel YHWH wəʿiḇdûhû lᵉḇaḏô</em> — 'Return your hearts to YHWH and serve him alone.' The verbs <em>šûḇ</em> (return/repent) and <em>ʿāḇaḏ</em> (serve/worship) are the covenant's core demands. The call to remove the <em>bəʿālîm</em> and <em>ʿaštārôt</em> — the plural of Baal and Astarte, the dominant Canaanite male and female deities — is the standard formula for covenant renewal (cf. Josh 24:14; Judg 10:16). <em>Lᵉḇaḏô</em> (him alone) is the exclusivity principle of the Shema: YHWH's covenant requires singular devotion, not mere priority. Jesus cites the Shema's <em>lᵉḇaḏô</em> principle directly: 'Worship the Lord your God and serve him only' (Matt 4:10, citing Deut 6:13).</p>",
    "12": "<p>Samuel erects the memorial stone and names it <em>ʾeḇen hāʿēzer</em> — 'stone of help': <em>wayyiqrāʾ ʾet šəmāh ʾeḇen hāʿēzer lēʾmōr ʿad hēnnāh ʿăzārānû YHWH</em> — 'he called its name Stone of Help, saying, &ldquo;Until now YHWH has helped us.&rdquo;' This is a counter-naming: in 4:1 Israel was defeated at a place that would become Ebenezer (named before the battle), a name that now takes on a new meaning. Samuel plants a covenant-memory marker in the landscape — YHWH's faithfulness made permanent in geography. The <em>ʿad hēnnāh</em> ('until now') phrase is the covenant retrospect formula: all of YHWH's past faithfulness concentrates in this moment. The stone of help is the OT equivalent of the NT's 'He who began a good work in you will bring it to completion' (Phil 1:6) — divine faithfulness marked and remembered.</p>"
  },
  "8": {
    "5": "<p>Israel's demand: <em>śîmāh lānû melek lᵉšāpəṭēnû kəḵol haggôyim</em> — 'give us a king to judge us like all the nations.' The phrase <em>kəḵol haggôyim</em> (like all the nations) is the demand's theological indictment: Israel's covenant identity is precisely its differentiation from the nations. Deut 17:14-20 anticipated this moment and regulated kingship — kings were permitted but must not multiply horses (military alliance with Egypt), wives (foreign treaties), or silver and gold (autonomous wealth). The demand here goes beyond the Deuteronomic provision: they want a king not to embody covenant rule but to replace YHWH as the source of security and governance. <em>Lᵉšāpəṭēnû</em> (to judge us) — the same verb <em>šāpaṭ</em> used for the judges — signals that they want a permanent institutional judge, not the crisis-charismatic judges YHWH has been providing.</p>",
    "7": "<p>YHWH's verdict to Samuel: <em>kî lōʾ ʾōtəḵā māʾāsû kî ʾōtî māʾāsû mimᵉlōḵ ʿălêhem</em> — 'for it is not you they have rejected, but me they have rejected from being king over them.' The verb <em>māʾas</em> (to reject, despise) is the same word used in 15:23 and 15:26 when YHWH rejects Saul. The rejection is mutual and sequential: Israel rejects YHWH as king; YHWH will later reject Saul as the king Israel chose. The theological structure is precise: <em>melek ʿălêhem</em> (king over them) — YHWH's kingship is the real category at stake. The entire book of 1 Samuel is framed by two rejections: Israel rejects YHWH's kingship in ch8; YHWH rejects Saul's kingship in ch15. Between them is the question of what kind of king YHWH will provide — which chs 16-31 and the entire Davidic tradition answer.</p>",
    "9": "<p>Samuel is commanded to warn Israel of the <em>mišpaṭ hammelek</em> — 'the manner/justice of the king.' The word <em>mišpaṭ</em> normally refers to covenant justice — YHWH's justice, the standard by which leaders are to be measured. Its use here for royal taxation and conscription is ironic: the 'justice' of a human king is coercive extraction, the opposite of the <em>mišpaṭ</em> YHWH's covenant produces. The list (vv11-17): sons taken for the chariot corps and harvest work, daughters for perfumers and cooks, fields and vineyards taken, a ten-percent tithe to royal servants — is the exact catalog of Solomonic administrative excess documented in 1 Kgs 4-5. The warning Samuel gives is the structural analysis of kingship that will be precisely fulfilled in the Solomonic monarchy.</p>"
  }
}

def main():
    c = load_comm('mkt-original', '1samuel')
    merge_comm(c, ORIGINAL)
    save_comm('mkt-original', '1samuel', c)
    count = sum(len(v) for v in ORIGINAL.values())
    print(f'1samuel mkt-original: wrote {count} verses across ch 4-8')

if __name__ == '__main__':
    main()
