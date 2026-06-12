"""
MKT Context Commentary — 1 Kings chapters 15–17
Run: python3 scripts/zc-context-1kings-15-17.py

Ch15: gᵉḇîrāh — queen-mother institution; Maacah's deposition; ANE parallels (Ugarit)
Ch16: Samaria founded — Omride archaeology; Mesha Stele; Assyrian 'house of Omri'
Ch17: Elijah's drought as challenge to Baal's rain domain — Ugaritic Baal Cycle (KTU 1);
      Zarephath in Sidon — Elijah in Baal's heartland; Luke 4:26 reception

ANE/historical context:
- gᵉḇîrāh (15:13): queen-mother as official court position, not merely familial role
- Mesha Stele (16:24): only contemporaneous non-biblical attestation of an Israelite king
- Baal Cycle (17:1): Baal as rain/storm god; drought = direct challenge to his domain
- Zarephath / Sidon (17:9): Sidonian territory = heartland of Jezebel's Baal religion
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
  "15": {
    "13": "<p>Asa&rsquo;s deposition of his mother Maacah from the position of <em>gᵉḇîrāh</em> — <em>wayyasirāh ʾet maʿăḵāh ʾimmô mig gᵉḇîrāh</em> — involves the most politically significant female office in the Judahite monarchy. The <em>gᵉḇîrāh</em> (literally &lsquo;great lady,&rsquo; from <em>gāḇar</em>, to be strong/great) was a formal court position, not merely a familial designation: the queen mother had official standing, was present at accession ceremonies, and could intercede with the king as a recognized court actor (1 Kgs 2:19-20: Bathsheba as <em>gᵉḇîrāh</em> approaches Solomon, who rises, bows, and seats her at his right hand with a throne of her own). The Ugaritic texts document a comparable institution (<em>rbtn</em>, &lsquo;great lady&rsquo;) at the Ugaritic court, and Hittite records show a formal &lsquo;Great Queen&rsquo; (<em>MUNUS.LUGAL-uš</em>) position. The <em>gᵉḇîrāh</em> was particularly significant in Judah because the king had multiple wives but only one queen mother — making her the most stable senior female figure across reigns. Maacah&rsquo;s deposition is simultaneously a formal political act and a religious one: she is removed because she made &lsquo;a horrifying thing (<em>mipleset</em>) for Asherah,&rsquo; and Asa burns the object in the Kidron. The Kuntillet Ajrud inscriptions (ca. 800 BCE) mentioning &lsquo;YHWH and his Asherah&rsquo; document the popular syncretism that allowed an Asherah object in the court of YHWH&rsquo;s appointed king&rsquo;s mother — the precise situation Asa&rsquo;s reform addresses.</p>"
  },
  "16": {
    "24": "<p>Omri&rsquo;s purchase of the hill of Samaria for two talents of silver and construction of his capital — <em>wayyiqen ʾet hāhār šōmᵉrôn bᵉkikkar keseep mēʾet šemer</em> — is archaeologically and extrabiblically documented at an exceptional level. The excavations at Samaria (Tell es-Sāmireh, directed by Harvard expeditions and Kathleen Kenyon) revealed Omride palace architecture with massive ashlar masonry characteristic of Phoenician building technique — confirming the Phoenician-Israelite collaboration that Solomon had initiated and the Omrides continued (Jezebel is a Sidonian princess). The Samaria Ivories (ca. 9th-8th century BCE), carved ivory furniture decorations excavated at Samaria, represent some of the finest ANE art found in the region, consistent with the luxury against which Amos 6:4 prophesies (&lsquo;those who lie on beds of ivory&rsquo;). Most significantly, the Mesha Stele (ca. 840 BCE, the Moabite Stone, found at Dhiban in 1868) — one of the most important epigraphic finds in biblical archaeology — records in Moabite that &lsquo;Omri king of Israel humbled Moab for many years,&rsquo; providing the only contemporaneous non-biblical attestation of an Israelite king by name at this period. The Assyrian annals continued to call Israel <em>bît-ḥumrî</em> (&lsquo;the house of Omri&rsquo;) even after the Jehu dynasty replaced the Omrides — a testament to Omri&rsquo;s regional impact. The Kings narrative (v25: &lsquo;Omri did more evil than all who were before him&rsquo;) stands in deliberate tension with his historical achievement: the most effective king in Israel&rsquo;s history by external standards is the Deuteronomistic historian&rsquo;s most negatively evaluated.</p>"
  },
  "17": {
    "1": "<p>Elijah&rsquo;s drought announcement — <em>ḥay YHWH ʾelōhê yiśrāʾēl... ʾim yihyeh haššānîm hāʾēlleh ṭal ûmāṭār kî ʾim lᵉpî dᵉḇārî</em> — &lsquo;as YHWH the God of Israel lives, there shall be neither dew nor rain these years, except by my word&rsquo; — is a direct challenge to Baal&rsquo;s claimed domain. In Canaanite religious cosmology, Baal (<em>baʿal</em>, &lsquo;lord&rsquo;) was the storm deity who controlled rain, thunder, and agricultural fertility. The Ugaritic Baal Cycle (tablets from Ras Shamra, ancient Ugarit, ca. 14th-13th century BCE; KTU 1.1-6) depicts Baal&rsquo;s ongoing contest with Mot (death) for control of the rain: when Mot defeats Baal, the land dries; when Baal defeats Mot, the rains return. Baal&rsquo;s enemies taunt him in the Cycle: &lsquo;Baal has no house like the other gods.&rsquo; The drought announced by Elijah strips Baal of his one undisputed domain and assigns control of the rain to YHWH through his prophet&rsquo;s spoken word alone — without the elaborate ritual combat of the Baal Cycle. The irony is compounded: the announcement is made to Ahab, whose wife Jezebel is the daughter of Ethbaal king of Sidon (<em>ʾeṯbaʿal</em>, &lsquo;with Baal&rsquo;) — the king whose very name declares Baal devotion. The drought is YHWH&rsquo;s challenge delivered to Baal&rsquo;s champion in Baal&rsquo;s heartland.</p>",
    "9": "<p>YHWH&rsquo;s command sending Elijah to Zarephath — <em>qûm lēḵ ṣārᵉpatāh ʾăšer lᵉṣîḏôn</em>, &lsquo;arise, go to Zarephath, which belongs to Sidon&rsquo; — is geographically and theologically loaded. Zarephath (<em>ṣārᵉpat</em>, modern Sarafand in Lebanon) is a Phoenician coastal town between Tyre and Sidon, explicitly identified as Sidonian territory. Sidon was the home city of Jezebel&rsquo;s father Ethbaal, the center of Phoenician Baal religion, and the source of the Baal/Asherah worship that the Omride-Jezebel axis had imported into Israel. Elijah is sent not to an Israelite widow but to a Gentile widow in the heartland of Baal worship — in the territory of the very deity whose rain-domain he had challenged, and whose leading human patron had married into the Israelite royal house. This mission embodies the theological principle that YHWH&rsquo;s provision and presence are not bounded by covenant geography. Luke 4:26 applies this location explicitly in Jesus&rsquo;s Nazareth sermon: &lsquo;there were many widows in Israel in the days of Elijah... and Elijah was sent to none of them but only to Zarephath, in the land of Sidon, to a woman who was a widow&rsquo; — identifying Elijah&rsquo;s Zarephath mission as the OT precedent for divine grace operating outside Israel&rsquo;s borders, and provoking the congregation&rsquo;s rejection of Jesus by the same logic: the grace that went to a Sidonian widow is now going to those outside the Nazareth congregation&rsquo;s expectation.</p>"
  }
}

def main():
    c = load_comm('mkt-context', '1kings')
    merge_comm(c, CONTEXT)
    save_comm('mkt-context', '1kings', c)
    count = sum(len(v) for v in CONTEXT.values())
    print(f'1kings mkt-context: wrote {count} verses across ch 15-17')

if __name__ == '__main__':
    main()
