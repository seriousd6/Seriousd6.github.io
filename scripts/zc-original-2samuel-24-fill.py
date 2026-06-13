"""
mkt-original fill — 2 Samuel ch24
Covers: 21 missing verses (2–13, 15–17, 19–23, 25)
Run: python3 scripts/zc-original-2samuel-24-fill.py

Key decisions:
- v13: "7 years" (MT) vs. "3 years" (1 Chr 21:12, LXX of 2 Sam) — text-critical discrepancy noted
- v16: wayyinnāḥem — divine Niphal of nāḥam; YHWH genuinely relents, not mere anthropomorphism
- v17: ḥāṭāʾtî wᵉʾānōkî — emphatic personal pronoun; David takes full individual responsibility
- v25: wayyēʿāter — Niphal of ʿātar ("be entreated"); same root as Gen 25:21 Isaac/Rebekah intercession
"""

import json
import pathlib

def load_comm(path):
    p = pathlib.Path(path)
    return json.loads(p.read_text()) if p.exists() else {}

def save_comm(path, data):
    pathlib.Path(path).write_text(json.dumps(data, ensure_ascii=False, indent=2))

def merge_comm(existing, new_data):
    # INTENT: Merge new commentary entries without overwriting existing ones — safe to re-run
    for ch, verses in new_data.items():
        if ch not in existing:
            existing[ch] = {}
        for v, html in verses.items():
            if v not in existing[ch]:
                existing[ch][v] = html

DATA = {
"24": {
"2": "<p>David commands Joab and the army commanders to census <em>kol-šiḇṭê yiśrāʾēl</em> (all the tribes of Israel) from Dan in the north to Beer-sheba in the south — the standard formula marking the full extent of the unified monarchy. The phrase <em>piqḏû ʾet-hāʿām</em> uses <em>pāqaḏ</em> (to muster, number, oversee), the same root used for census-taking in Numbers; its use here signals the act's cultic-administrative weight. The purpose clause <em>wᵉʾēḏᵉʿāh ʾet-mispar hāʿām</em> (that I may know the number of the people) encapsulates the problem: David wants actuarial knowledge of Israel's fighting strength, implicitly substituting demographic confidence for dependence on YHWH. Compare the Mosaic census in Numbers 1, which included an atonement half-shekel per person precisely because numbering the people without such provision brought divine judgment.</p>",

"3": "<p>Joab's objection carries both political and theological weight. <em>yōsēp YHWH ʾelōhêḵā ʾel-hāʿām kahem wᵉḵāhem mēʾāh pᵉʿāmîm</em> — May YHWH your God add to the people a hundredfold as many as they are — frames Joab's protest as a petition for divine multiplication rather than human calculation. The final question <em>ûlᵉʾadōnî hammelek lāmmāh ḥāpēṣ baddāḇār hazzeh</em> (and why does my lord the king desire this thing?) indicts the census as a desire born of royal ambition, not necessity. This is the only place in the narrative where Joab acts as the moral check on David; the reversal is ironic — the general who killed Abner and Absalom without compunction balks at a census. His objection anticipates the divine judgment that follows.</p>",

"4": "<p>The king's word (<em>daḇar haMelek</em>) prevails against Joab and the army commanders. The verb <em>wayyeḥĕzaq</em> (was strong/prevailed) from <em>ḥāzaq</em> signals royal authority overriding wise counsel — a pattern of fatal decision-making in Samuel (cf. Saul overriding Samuel, Rehoboam overriding the elders). That Joab <em>went out</em> despite his objection shows the institutional hierarchy; he is loyal even when he disagrees. The phrase <em>śārê haḥayil</em> (commanders of the army) underscores that the census is a military initiative rather than a civic one — its purpose is enumeration of fighting strength.</p>",

"5": "<p>The census route begins at Aroer on the Arnon gorge (southern Transjordan), proceeding north through the Gadite valley. <em>wayyaḥănû bāʿărōʿēr yᵉmîn hāʿîr ʾăšer bᵉtôk-hannāḥal hāgāḏ</em> specifies both topographic precision and tribal territory. Aroer (modern Arāʿir) marked the traditional southern limit of Israelite Transjordanian control; beginning here signals a comprehensive count from the margins inward. The term <em>haḥayil</em> applied to the city (<em>yᵉmîn hāʿîr</em>) may read as &#8220;to the right of the city&#8221; — the scribe tracks the military route with cartographic attention, which itself reflects the census&#8217;s military purpose.</p>",

"6": "<p>The route continues north through Gilead, Kadesh (possibly Kadesh Naphtali; some read <em>taḥtîm-ḥoḏšî</em> as a place name, though the text is uncertain), and to Dan in the far north. <em>ʾereṣ haḥittîm</em> (land of the Hittites) appears in a northern context, likely referring to Hittite communities in the Beqa&#8217; valley or the territory around Abel-beth-maacah. The inclusion of non-Israelite territories within the enumerated zone reflects the census&#8217;s imperial scope — David is numbering the population under his effective control, not merely Israelite tribal rolls.</p>",

"7": "<p>The circuit reaches Tyre (<em>mibṣar-ṣōr</em>, fortified Tyre), the Hivite and Canaanite cities, and concludes at Beer-sheba in the Negev — the southern terminus corresponding to the opening &#8220;Dan to Beer-sheba&#8221; formula. The exhaustive geographic scope (Transjordan, Galilee, Phoenician coast, Canaanite enclaves, Negev) shows the census covering the entire Davidic empire, not just tribal Israel. This comprehensiveness heightens the offense: David is cataloguing the full extent of his military resources, precisely the kind of self-reliant accounting that Deuteronomy warns against (Deut 17:16–17 — the king must not multiply horses or return to Egypt; the census&#8217;s logic parallels this accumulative temptation).</p>",

"8": "<p>The census required nine months and twenty days to complete — a duration reflecting both the geographic scope and the administrative complexity of the operation. <em>wayyāšuḇû ʾel-yᵉrûšālayim</em> marks the return to the royal center. The LXX adds detail about the route not found in MT; MT&#8217;s brevity here shifts focus immediately to the numbers. The duration also implies significant resource expenditure: the army commanders are occupied for nearly a year in non-military administration, a cost in readiness that itself represents misallocation of Israel&#8217;s defense posture.</p>",

"9": "<p>Joab reports the totals to David: <em>wayyitten yōʾāḇ ʾet-mispar mipqad-hāʿām ʾel-hammelek</em>. The numbers — 800,000 sword-bearing men in Israel (<em>yiśrāʾēl</em>) and 500,000 in Judah — differ substantially from the parallel in 1 Chronicles 21:5 (1,100,000 + 470,000). The discrepancy is a classic text-critical problem; possible explanations include different counting criteria (whether standing army vs. general conscript pool, whether Levi and Benjamin were counted), different source traditions, or scribal adjustment. The Chronicles text may represent a separate administrative record. Neither figure should be harmonized artificially; both reflect real data disputes in the ancient transmission. The scale — 1.3 million fighting men — signals David&#8217;s peak imperial power, which is precisely the moment divine judgment arrives.</p>",

"10": "<p>David&#8217;s conscience strikes him (<em>wayyak lēḇ dāwid ʾōtô</em>) after the census is complete — the verb <em>nāḵāh</em> used reflexively of the heart conveys the inner blow of conviction (cf. 1 Sam 24:6 where David&#8217;s heart smites him for cutting Saul&#8217;s robe). His confession is terse and direct: <em>ḥāṭāʾtî mᵉʾōḏ ʾăšer ʿāśîtî</em> (I have sinned greatly in what I have done). Crucially, the prayer that follows — <em>wᵉʿattāh YHWH haʿăḇer nāʾ ʾet-ʿăwōn ʿaḇdᵉḵā</em> (and now YHWH, pass over the iniquity of your servant) — uses <em>ʿāḇar</em> (to pass over/away) rather than <em>sālaḥ</em> (to forgive). The distinction is subtle: <em>ʿāḇar</em> asks for removal of consequence; <em>sālaḥ</em> asks for forgiveness of guilt. Both together would constitute full restoration.</p>",

"11": "<p>The word of YHWH reaches David through <em>Gāḏ hānāḇîʾ ḥōzeh dāwid</em> — Gad the prophet, the seer of David. <em>Ḥōzeh</em> (seer, from <em>ḥāzāh</em> to perceive/vision) is the earlier term for the prophetic office; its pairing with <em>nāḇîʾ</em> here demonstrates that both designations applied to the same figure in David&#8217;s court. Gad first appears in 1 Samuel 22:5 directing David&#8217;s movements during Saul&#8217;s persecution; he is mentioned in 1 Chronicles 29:29 among those who wrote David&#8217;s history. His role as court prophet ensures that divine communication comes through an established mediator, not a direct theophany — YHWH&#8217;s judgment is announced prophetically rather than enacted silently.</p>",

"12": "<p>YHWH offers David three options through Gad: <em>šālōš ʾānōḵî nōṭeh ʿāleḵā</em> (three things I am stretching out against you). The verb <em>nāṭāh</em> (to stretch out, extend) normally applies to YHWH&#8217;s outstretched arm in salvation contexts (Exod 6:6; 7:5); here it is turned toward judgment. This is a remarkable forensic structure — the sovereign grants the condemned a choice among penalties, a practice attested in ANE treaty documents where suzerain-initiated punishment options signal controlled divine justice rather than arbitrary retribution. David is not passive under judgment but is given moral agency in his own punishment, which the narrative will use to reveal his theology of divine mercy (v14).</p>",

"13": "<p>Gad presents the three options: three years of famine, three months of flight from enemies, or three days of plague. A critical text variant appears here: the MT reads <em>šeḇaʿ šānîm</em> (seven years) of famine, while 1 Chronicles 21:12 and the LXX of this verse read <em>šālōš šānîm</em> (three years). The LXX of 2 Samuel explicitly supports the three-year reading, strongly suggesting the MT&#8217;s &#8220;seven&#8221; is a later expansion, possibly influenced by the seven-year famine motifs in Genesis 41 or 2 Kings 8:1. The three-year reading makes the triadic symmetry (3 years / 3 months / 3 days) explicit and fits the rhetorical structure of the offer. The Masoretic &#8220;seven&#8221; may reflect a copyist&#8217;s assimilation to other famine traditions in the corpus.</p>",

"15": "<p>YHWH sends the plague (<em>deber</em>) from that morning until the appointed time (<em>mōʿēd</em>). The term <em>mōʿēd</em> carries liturgical weight — the same word used for sacred assembly times and the tabernacle of meeting; its appearance here may signal that YHWH appoints even the duration of judgment with precision, not capriciously. Seventy thousand die from Dan to Beer-sheba — the same geographic formula that bounded the census, creating a literary irony: the numbers David sought to know are now numbers of the dead. The plague thus answers the census measure for measure: David counted lives; YHWH removes them in the same territorial scope.</p>",

"16": "<p>The narrative&#8217;s theological climax: the angel of YHWH stretches his hand toward Jerusalem to destroy it, but <em>wayyinnāḥem YHWH ʾel-hārāʿāh</em> — YHWH relented concerning the disaster. The Niphal of <em>nāḥam</em> denotes genuine divine emotional movement — the same term used in Genesis 6:6 when YHWH was grieved he made humanity, and in Jeremiah 18:8 when YHWH relents from threatened judgment upon repentant nations. Theology cannot explain this away as mere anthropomorphism; the narrative insists YHWH is genuinely moved. The command to stop (<em>rab haref yādᵉḵā</em> — &#8220;Enough, stay your hand&#8221;) is issued at the precise geographic point that the entire narrative has been building toward: the threshing floor of Araunah the Jebusite, which becomes the site of the Temple altar (2 Chr 3:1).</p>",

"17": "<p>David&#8217;s intercession before the angel uses emphatic personal language: <em>ʾānōḵî ḥāṭāʾtî wᵉʾānōḵî hārēʿōtî</em> — I am the one who sinned and I am the one who acted wickedly. The doubled <em>ʾānōḵî</em> (emphatic personal pronoun) is maximally self-implicating; David takes sole individual responsibility, excluding the people. The pastoral image that follows — <em>wᵉʾēlleh haṣṣōn meh ʿāśû</em> (and these sheep, what have they done?) — frames David as shepherd-king interceding for his flock (cf. Ps 23; Ezek 34), even as he acknowledges they suffer for his decision. The request that divine hand fall on him and his household (<em>bêt ʾāḇî</em>) rather than on the people echoes Moses&#8217;s willingness to be blotted from the book (Exod 32:32) and foreshadows the Servant who bears others&#8217; iniquity (Isa 53:6).</p>",

"19": "<p>David goes up to Araunah as Gad had commanded and as YHWH had ordered (<em>kaʾăšer ṣiwwāh YHWH</em>). The verb <em>wayyaʿal dāwid</em> (David went up) echoes the language of temple ascent; the journey to the threshing floor anticipates the processional theology of the Psalms of Ascent (Pss 120–134). That YHWH directly commanded Gad, who in turn commanded David, establishes a clear prophetic chain of authority — the purchase of the threshing floor is not David&#8217;s autonomous initiative but a divinely directed act of worship that transforms a site of judgment into a site of atonement.</p>",

"20": "<p>Araunah (<em>ʾărawnāh</em>; also spelled Ornan in Chronicles) sees the king approaching and his servants, prostrates himself face to the ground (<em>wayyiššataḥû ʾappāyw ʾarṣāh</em>). The depth of the bow — face to the earth — is the most complete prostration gesture in the Hebrew posture vocabulary, used before kings and deities. His question <em>maddûaʿ bāʾ ʾăḏōnî hammelek ʾel-ʿaḇdô</em> (why has my lord the king come to his servant?) uses the language of servitude that frames the entire transaction: Araunah defines himself as David&#8217;s servant even while his threshing floor possesses something the king needs. The irony of a Jebusite landowner holding the future Temple Mount underscores the theological point that YHWH&#8217;s choice of location transcends ethnic boundaries.</p>",

"21": "<p>David&#8217;s stated purpose — <em>liqnôt mēʿimmᵉḵā ʾet-haGōren</em> (to buy from you the threshing floor) — uses <em>qānāh</em>, the standard commercial term for acquisition by purchase (cf. Gen 23 Abraham&#8217;s purchase of Machpelah from Ephron; Ruth 4:4–5 Boaz&#8217;s redemption purchase). The stated reason is <em>liḇnôt mizḇēaḥ laYHWH</em> (to build an altar to YHWH) so that the plague on the people will be stopped (<em>wᵉtiʿăṣar hammaggēpāh</em>). The commercial acquisition of sacred space follows a pattern in Genesis and here: the founding sites of Israelite worship are purchased legitimately from non-Israelites (Machpelah, Shechem, and now Araunah&#8217;s threshing floor), establishing ownership claims that transcend conquest.</p>",

"22": "<p>Araunah&#8217;s generous offer — take the threshing sledges (<em>hammōrāgōt</em>) for firewood and the oxen for a burnt offering — uses the tools of his agricultural livelihood as sacrificial material. <em>Hammōrāgōt</em> are heavy threshing sledges dragged by animals over grain; their use as firewood for an altar sacrifice is a fitting conversion: implements of agricultural labor become instruments of worship. The word <em>kōl</em> (everything) emphasizes Araunah&#8217;s total generosity — he offers implements, animals, and land without reservation. The narrative carefully records this offer to make David&#8217;s refusal the more deliberate and the more theologically weighted.</p>",

"23": "<p>Araunah repeats the gift formally: <em>hakkōl nātan ʾărawnāh hammelek lammelek</em> — all this Araunah the king gives to the king. The unusual self-designation <em>ʾărawnāh hammelek</em> (Araunah the king) is debated: some read it as a respectful address to David, others as a title Araunah held as the last Jebusite ruler of pre-Davidic Jerusalem. If the latter, the scene carries extraordinary subtext: the former Jebusite king grants the Israelite king sacred ground, and YHWH accepts the worship. The closing blessing — <em>yereḵā YHWH ʾelōhêḵā</em> — shows Araunah invoking Israel&#8217;s God for David, a Gentile aligning himself with YHWH&#8217;s blessing even as the transaction is completed.</p>",

"25": "<p>David builds the altar and offers both <em>ʿōlôt</em> (burnt offerings, wholly consumed) and <em>šᵉlāmîm</em> (fellowship/peace offerings, shared between worshipper and deity). The combination signals both total consecration to YHWH and the restoration of covenant communion that had been broken by the census. The result: <em>wayyēʿāter YHWH lāʾāreṣ</em> — YHWH was moved by entreaty for the land. The Niphal of <em>ʿātar</em> (to be entreated, to allow oneself to be moved by prayer) appears only six times in the Hebrew Bible, including Isaac&#8217;s prayer for Rebekah (Gen 25:21) and Manasseh&#8217;s humbling (2 Chr 33:13). It denotes YHWH&#8217;s willingness to be affected by human petition — not divine weakness, but divine relational responsiveness. The plague stops. The book of 2 Samuel closes on this site: the ground where judgment was arrested becomes the ground where the Temple will stand, and where sacrifice will continually meet divine mercy.</p>"
}
}

def main():
    out_path = "data/commentary/mkt-original/2samuel.json"
    existing = load_comm(out_path)
    before = sum(len(existing.get(c, {})) for c in DATA)
    merge_comm(existing, DATA)
    after = sum(len(existing.get(c, {})) for c in DATA)
    save_comm(out_path, existing)
    print(f"  wrote {out_path}")
    print(f"2samuel mkt-original: added up to {after - before} verses across ch24")

if __name__ == "__main__":
    main()
