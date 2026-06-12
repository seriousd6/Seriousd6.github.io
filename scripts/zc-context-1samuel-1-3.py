"""
MKT Context Commentary — 1 Samuel chapters 1–3
Run: python3 scripts/zc-context-1samuel-1-3.py

Historical/ANE context, canonical function, Second Temple reception:

Ch1: Hannah and Elkanah at Shiloh — barren-woman motif in covenant history;
     Shiloh as central sanctuary; Samuel's vow and birth
Ch2: Hannah's prayer — the reversal-of-fortunes theology; Eli's sons and
     institutional corruption of the priesthood; the oracle against the house of Eli
Ch3: YHWH's call to Samuel — the new prophetic mediation; the transition from
     the priestly-tabernacle era to the prophetic era
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

CONTEXT = {
  "1": {
    "3": "<p>Elkanah's annual pilgrimage to Shiloh situates the narrative in the final phase of the tabernacle period. Shiloh (<em>šîlōh</em>, modern Khirbet Seilun, in the hill country of Ephraim) was the central sanctuary from after the conquest (Josh 18:1, when the tabernacle was erected there) through the end of the judges period, a span of roughly 300 years (ca. 1400-1050 BCE). Archaeological excavations at Khirbet Seilun by Israel Finkelstein (1981-84) revealed substantial Iron Age I occupation consistent with a cultic center, including large quantities of imported pottery and faunal remains suggesting sacrificial feasting. The annual pilgrimage pattern (Elkanah going 'year by year') reflects the Pentateuchal requirements of Exod 23:14-17 and Deut 16:16 — the three annual pilgrim festivals (Passover, Weeks, Booths). The mention of YHWH of armies (<em>YHWH ṣᵉḇāʾôt</em>) in v3 and v11 is significant: this is the first occurrence of this specific divine title in the narrative books, and it becomes the dominant epithet in the Ark Narrative that follows in chs 4-6.</p>",
    "9": "<p>The Shiloh sanctuary has a 'doorpost of the temple of YHWH' (<em>mᵉzûzōt hêḵal YHWH</em>) — the Hebrew <em>hêḵal</em> here refers to the tabernacle's tent structure rather than a permanent building (which is not yet built). The term <em>hêḵal</em> (palace/temple) applied to the tabernacle is unusual; it anticipates the transition that will occur in 2 Sam 7 when David proposes to build a permanent <em>bêt</em> (house/temple) for YHWH. That the Shiloh tabernacle is called a <em>hêḵal</em> suggests either that the original tent had been supplemented with more permanent structures by this period, or that the narrator is using the term proleptically. The Priestly legislation of Num 3-4 describes the Levites dismantling and transporting the tabernacle; the use of <em>hêḵal</em> here suggests a period of relative stability at Shiloh where the tabernacle had taken on more permanent character.</p>",
    "20": "<p>Hannah names her son <em>šᵉmûʾēl</em> (Samuel) with the explanation: <em>kî mēYHWH šᵉʾiltîw</em> — 'for from YHWH I asked him.' The etymology offered is from the root <em>šāʾal</em> (to ask/request), making the name mean 'name of God' or 'heard of God' — though the Semitic derivation of <em>šᵉmûʾēl</em> more naturally yields 'his name is El' or 'heard of God' (combining <em>šēm</em> + <em>ʾēl</em> or <em>šāmaʿ</em> + <em>ʾēl</em>). The narrative etymology — connecting the name to Saul's being asked/lent — actually fits Saul's name (<em>šāʾûl</em>, asked for) better than Samuel's. Scholars have noted this as a possible narrative telescoping or theologically motivated name-giving. Whatever the historical-linguistic analysis, the narrative point is clear: Samuel is the answered prayer, the gift-child, the one whose life belongs to YHWH because he was received from YHWH's hand.</p>"
  },
  "2": {
    "1": "<p>Hannah's prayer (the Magnificat of the OT) is dated to ca. 1100 BCE in the narrative framework and represents one of the oldest poetic compositions preserved in Samuel. Its closest structural parallel is Psalm 113 (the praise of YHWH who raises the poor from the dust). The prayer's theological structure — YHWH reverses human fortunes by humbling the proud and exalting the lowly — is the dominant theological pattern of the Samuel books: Saul is humbled, David is exalted; the priest Eli's house falls, Samuel rises. Mary's Magnificat (Luke 1:46-55) is a conscious typological expansion of Hannah's prayer: the same reversal theology, the same vocabulary of the hungry being filled and the rich sent empty away, the same divine agent (YHWH/the Lord) as the initiator of the reversal. Placing Hannah's prayer in its canonical context shows it as the theological overture to both the Samuel books and the NT Advent narratives.</p>",
    "12": "<p>Eli's sons Hophni and Phinehas are described as <em>bənê bəliyyaʿal</em> — 'sons of worthlessness/Belial' — the same phrase used for the men of Gibeah (Judg 19:22) and for Nabal (1 Sam 25:17, 25). The compound <em>bəliyyaʿal</em> (<em>bəlî</em> = without + <em>yōʿal</em> = profit/worth) designates persons who operate entirely outside covenant norms — those from whom no positive covenant contribution can be expected. The specific sins enumerated: taking the meat by force before the fat has been offered to YHWH (vv13-16), and lying with the women who served at the entrance of the tent of meeting (v22). Both sins are direct inversions of priestly vocation: the priest is to burn the fat first (Lev 3:16-17), and the sanctuary is to be protected from sexual defilement (cf. the Zimri-Cozbi incident, Num 25). The Shiloh priesthood's corruption is the institutional background that makes Samuel's emergence and eventually the royal institution both necessary and theologically justified.</p>",
    "27": "<p>The oracle of the 'man of God' (ʾîš hāʾelōhîm) against Eli's house introduces a motif that will recur throughout the DH: the prophetic word that announces the end of a dynasty or institution, followed by the fulfillment in the narrative. The formula <em>hinnēh yāmîm bāʾîm</em> ('behold, days are coming') is the standard prophetic announcement formula for future judgment (it appears 16 times in Jeremiah alone). The judgment oracle against the house of Eli (vv31-36) announces: (1) cutting off (<em>kārat</em>) the strength of Eli's father's house; (2) no old man in his house forever; (3) a faithful priest (<em>kōhēn neʾĕmān</em>) to replace him, 'who will do according to what is in my heart and in my soul.' The 'faithful priest' of v35 is variously identified as Samuel, Zadok (who replaces Abiathar/Eli's line, 1 Kgs 2:27,35), or eschatologically as Christ. The oracle's immediate fulfillment in the deaths of Hophni and Phinehas (ch4) and its long fulfillment in Zadok's appointment makes this a paradigmatic example of prophetic word-and-fulfillment theology.</p>",
    "35": "<p>The 'faithful priest' (<em>kōhēn neʾĕmān</em>) oracle is the pivot of the Shiloh narrative. The terms <em>neʾĕmān</em> (faithful, reliable, established — from the <em>ʾāmēn</em> root) echo the Davidic covenant vocabulary of 2 Sam 7:16 (<em>wᵉneʾĕman bêtəḵā</em>, 'your house shall be established/faithful forever'). The phrase 'a sure (<em>neʾĕmān</em>) house' appears in both the Eli oracle (v35) and the Nathan oracle (2 Sam 7:16), creating a structural parallel: what is denied to Eli's house (a sure/faithful house) is granted to David's house. The theological logic: the priestly failure at Shiloh clears the ground for the Davidic institution — Eli's corruption is not merely personal but institutional, requiring not just a better priest but a new covenantal arrangement whose embodiment will eventually be the priestly-royal Messiah.</p>"
  },
  "3": {
    "1": "<p>The narrative's temporal marker: <em>ûdəḇar YHWH hāyāh yāqār bayyāmîm hahēm ʾên ḥāzôn niphrāṣ</em> — 'the word of YHWH was rare in those days; there was no frequent vision.' The rarity of prophetic vision at the end of the Eli period marks a nadir of covenant communication — YHWH had gone silent. This silence is the negative background against which Samuel's emergence as prophet is the more dramatic. The pattern of divine silence followed by renewed prophetic word is a recurrent OT structure: the centuries between Malachi and John the Baptist, the silence between Elijah and Elisha's ministry. Amos 8:11-12 describes a coming 'famine of hearing the words of YHWH' — the absence of prophetic word as divine judgment. The silence at Shiloh is not YHWH's absence but his withholding of the word that Eli's priesthood has made itself unworthy to receive.</p>",
    "3": "<p>Samuel sleeps 'in the temple of YHWH where the ark of God was.' The physical arrangement of the Shiloh sanctuary described here — the Ark, the lamp of God, the sleeping quarters for the priestly attendant — places Samuel in the position of the ideal sanctuary-keeper: present, attentive, in the posture of availability. The lamp of God (<em>nēr ʾelōhîm</em>) burning through the night is the <em>mənōrāh</em>'s lamp (Exod 27:20-21 — the priests are to keep the lamp burning from evening to morning). Samuel's nighttime vigil at the Ark, hearing the divine voice while Eli's sight is failing (v2 — 'his eyes had begun to grow dim'), is a visual narrative of the transition: the old, dimming priestly order yields to the attentive young servant who hears what Eli can no longer see or receive.</p>",
    "19": "<p>Samuel's prophetic authentication: <em>wayyiḡdal šᵉmûʾēl wᵉYHWH hāyāh ʿimmô wəlōʾ hippîl mikkol dᵉḇārāyw ʾārṣāh</em> — 'Samuel grew and YHWH was with him and did not let any of his words fall to the ground.' The phrase 'words falling to the ground' (<em>hippîl dāḇār ʾārṣāh</em>) is the idiom for prophetic failure — a word that does not come to pass. The canonical criterion for true prophecy in Deut 18:22 is precisely this: if the word does not come to pass, the prophet has spoken presumptuously. Samuel's authentication is the inverse: all his words come true. This is the foundational credential that makes Samuel the paradigmatic OT prophet and the institutional anchor for what will be called the 'school of the prophets' (<em>bᵉnê hannəḇîʾîm</em>) in the Elijah-Elisha narratives (2 Kgs 2-4). Second Temple Judaism's high regard for Samuel is reflected in Sir 46:13-20 and 1 Macc 2:57 — his intercession at Mizpah was remembered as paradigmatic covenant prayer.</p>"
  }
}

def main():
    c = load_comm('mkt-context', '1samuel')
    merge_comm(c, CONTEXT)
    save_comm('mkt-context', '1samuel', c)
    count = sum(len(v) for v in CONTEXT.values())
    print(f'1samuel mkt-context: wrote {count} verses across ch 1-3')

if __name__ == '__main__':
    main()
