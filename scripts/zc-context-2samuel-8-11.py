"""
mkt-context | 2 Samuel 8-11
Run: python3 scripts/zc-context-2samuel-8-11.py

Key context themes:
- Ch 8: ANE imperial administration; David's officer roster includes Philistine mercenaries
- Ch 9: Covenant loyalty (hesed) in ANE suzerain-vassal treaty tradition; Lo-debar geography
- Ch 10: Honor-shame dynamics of the beard-shaving insult; spring warfare season (yēṣēʾ hammelek)
- Ch 11: "Time when kings go to war" — David's absence from battle as the crack in the armor;
         Uriah the Hittite as the loyal foreigner; the cover-up mechanics; the evil reported
         tersely in v27b as the theological verdict
"""

import json
import pathlib

ROOT = pathlib.Path(__file__).parent.parent


def load_comm(source, book):
    p = ROOT / 'data' / 'commentary' / source / f'{book}.json'
    if p.exists():
        return json.loads(p.read_text())
    return {}


def save_comm(source, book, data):
    p = ROOT / 'data' / 'commentary' / source / f'{book}.json'
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


SAMUEL = {
    "8": {
        "1": "<p>The summary of David's military campaigns opens a new literary unit: the annals of the Davidic empire. Chapter 8 is structured as a royal summary — a genre familiar from Egyptian and Mesopotamian royal inscriptions that enumerate the king's victories and tribute-recipients. 'Metheg-ammah' is a toponym of disputed meaning; 1 Chr 18:1 reads 'Gath and its dependencies,' suggesting this was the Philistine heartland. David completing what Saul could never accomplish — subduing the Philistines — is the symbolic closure of the Samuel narrative.</p>",

        "2": "<p>The treatment of Moab after defeating them — measuring with a cord, executing two-thirds, sparing one-third — is unusually harsh compared to David's other campaigns. Moab had earlier sheltered David's parents (1 Sam 22:3-4); the reason for this severity is not stated. ANE context: the measuring-and-selecting of prisoners for death was a known practice in ancient warfare, used to reduce the fighting population while creating a subject state. The Moabite subjection fits the pattern of treaty-vassal relationships: tribute, service, subject status.</p>",

        "3": "<p>Hadadezer king of Zobah was attempting to reassert control at the Euphrates (<em>hayyāḏ binhār-pĕrāṯ</em>) — the phrase is debated (whether he was going to restore his stele/monument or his power at the river). Zobah was an Aramaean kingdom in modern Syria, one of the strongest powers in the Levant at this time. David's defeat of Zobah extends Israelite influence far beyond the traditional borders, fulfilling the territorial promises of Gen 15:18 ('from the river of Egypt to the great river, the Euphrates').</p>",

        "4": "<p>The hamstringing of chariot horses (<em>wayyĕʿaqqēr dāwîḏ ʾeṯ-kol-hāreḵeš</em>) except for enough for a hundred chariots follows the command of Deut 17:16: 'he must not acquire many horses for himself.' David is complying with the Torah prohibition on royal horse-accumulation — a check on the militaristic excess the law anticipated. Solomon will violate this (1 Kgs 10:26-29) with 1,400 chariots; the contrast is built into the canonical sequence.</p>",

        "5": "<p>The Aramaeans of Damascus intervene to help Hadadezer; David defeats twenty-two thousand of them as well. Damascus — later the capital of Aram — first appears here as a significant regional power. The defeat of Damascus establishes a sphere of influence that will later contract when Solomon's compromises allow Rezon of Damascus to become an adversary (1 Kgs 11:23-25). What David captures militarily, Solomon loses diplomatically.</p>",

        "6": "<p>Garrisons placed throughout Damascus-Aram; the Syrians bring tribute (<em>minḥâ</em>). The vocabulary here is vassal-treaty vocabulary: the defeated king becomes a tribute-paying subject. This is Israel's widest imperial extent — David controls from the Euphrates to the border with Egypt, a territory no later Israelite king would match. The narrator's theological verdict: 'The LORD preserved David wherever he went' (<em>wayyōšaʿ YHWH ʾeṯ-dāwîḏ bĕkōl ʾăšer hālāk</em>) — the victories are attributed to divine preservation, not merely military skill.</p>",

        "7": "<p>The gold shields (or quivers — <em>šilṭê hazzāhāḇ</em>, possibly round shields or decorative quivers) taken from Hadadezer's officers are brought to Jerusalem. This begins the treasure-accumulation that will fund the Temple's construction. The dedicatory chain — David captures → brings to Jerusalem → Solomon uses for the Temple — is explicit in 1 Kgs 7:51. The spoils of empire become the furnishings of worship.</p>",

        "8": "<p>Bronze from the captured Aramaean cities — bronze was the industrial material of the age, essential for weapons, tools, and sacred objects. The narrator notes 'a very large quantity' (<em>nĕḥōšeṯ harbēh mĕʾōḏ</em>). Solomon's bronze works (the pillars Jachin and Boaz, the bronze sea, the altar) will be made from this captured material (1 Kgs 7:47). Military victory in the ANE routinely included the stripping of metals; David's campaigns are simultaneously territorial and material preparation for the Temple.</p>",

        "9": "<p>Toi king of Hamath was Hadadezer's enemy — my enemy's enemy becomes my ally. Hamath is located in central Syria, modern Hama. It sat on the Orontes River and controlled major trade routes. Its mention here confirms the geographical scope of David's influence: a king from 200 miles north is tracking Israeli military movements carefully enough to respond diplomatically to Hadadezer's defeat.</p>",

        "10": "<p>Joram (or Hadoram, 1 Chr 18:10) brings gifts of silver, gold, and bronze — diplomatic tribute in the form of precious metals. The NT equivalent of this gift-bearing of nations is the Magi's gold, frankincense, and myrrh (Matt 2:11), and the eschatological vision of nations bringing their wealth into the New Jerusalem (Rev 21:24-26). The Davidic king attracting tribute from foreign nations is an OT archetype of the universal kingship Christ exercises.</p>",

        "11": "<p>David dedicates the captured materials 'to the LORD' (<em>qiddēš dāwîḏ laYHWH</em>). The verb <em>qiddēš</em> (consecrate, make holy) takes on particular significance: all the silver, gold, and bronze from the subjugated nations is set apart for divine use, not personal accumulation. This is the theological discipline of the ḥērem principle applied to imperial spoils: the fruits of conquest belong to YHWH. The list of nations — Edom, Moab, Ammon, Philistines, Amalek — are the traditional enemies of Israel.</p>",

        "12": "<p>The list includes Amalek — completing the arc from 1 Samuel 15 where Saul failed to destroy Amalek. What Saul left undone, David accomplishes — not in a single ḥērem campaign but through accumulative military dominance. The canonical lesson is not that David finished Saul's specific campaign but that under righteous kingship the enemies of YHWH's people are eventually subdued.</p>",

        "13": "<p>David makes a name (<em>wayyaʿaś dāwîḏ šēm</em>) after the Valley of Salt victory over Edom. 'Making a name' is empire-building language — the same ambition the tower-builders at Babel had (Gen 11:4 'let us make a name for ourselves'). The difference: David's name is made through YHWH's victories (v6, 14), not through human construction. Yet the phrase itself signals the dangerous proximity of genuine achievement and pride — an edge David will step over in 2 Samuel 24's census.</p>",

        "14": "<p>Garrisons throughout Edom; all Edomites become David's subjects. The reference to Ps 60 (superscription) connects this campaign to a psalm of lament: even this era of victory included setbacks. The theological refrain returns: 'The LORD preserved David wherever he went.' The repetition of this phrase (also in v6) frames the entire military summary as a theological statement about YHWH's faithfulness rather than David's ability.</p>",

        "15": "<p>'David reigned over all Israel, administering justice and equity (<em>mišpāṭ ûṣĕḏāqâ</em>) to all his people.' This paired phrase — justice and righteousness — is the OT's standard for ideal kingship. It appears in Isaiah's descriptions of the coming messianic king (Isa 9:7 'justice and righteousness from this time forth'; Isa 32:1 'a king will reign in righteousness'). David at his apex embodies this ideal; the chapters that follow (11-12) show his catastrophic failure to maintain it in his personal life.</p>",

        "16": "<p>The administrative roster begins. Joab son of Zeruiah over the army — the military commander whose loyalty to David is fierce but whose methods are consistently brutal. Jehoshaphat son of Ahilud as mazkîr (recorder/herald) — a royal official who kept records and managed the king's public communications. The emergence of a formal bureaucratic structure marks Israel's transition from tribal confederation to territorial state, paralleling developments in Egypt, Assyria, and Mesopotamia.</p>",

        "17": "<p>Zadok and Ahimelech (or Abiathar — the textual tradition is confused here; cf. 1 Chr 24:3-6) as priests. The dual-priesthood reflects the dual-lineage of Aaron's sons: Zadok is associated with Eleazar's line, Abiathar with Ithamar's. This priestly division will crystallize at Solomon's coronation when Abiathar is exiled and Zadok becomes the sole Solomonic priest (1 Kgs 2:35). Seraiah as secretary completes the triad of royal officials that appears in parallel form in later Israelite administrations.</p>",

        "18": "<p>Benaiah over the Cherethites and Pelethites — Philistine-origin mercenary troops who served as the royal bodyguard. The Cherethites (Cretans) and Pelethites (possibly 'Philistines') were professional soldiers operating outside Israelite tribal structures, loyal directly to the king rather than to tribal commanders. The use of foreign mercenaries as a royal guard is an ANE royal institution (Egyptian pharaohs used Nubian guards; Mesopotamian kings used similarly non-native troops) providing protection not subject to tribal politics. David's sons as kōhănîm (priests) reflects early monarchy practice before the priestly office was strictly Levitical in practice.</p>",
    },

    "9": {
        "1": "<p>David's question — 'Is there anyone still left of the house of Saul to whom I can show <em>hesed</em> for Jonathan's sake?' — is a formal covenant-loyalty inquiry. The word <em>hesed</em> (H2617, steadfast love, covenant loyalty) is the key term: it refers to the covenant relationship David and Jonathan made (1 Sam 20:14-17) when Jonathan explicitly asked David to show hesed to his descendants. This is ANE suzerain-vassal treaty language: the new king is obligated to honor the covenant commitments of the previous covenant partner. Ancient Near Eastern treaties routinely included clauses protecting the families of treaty partners.</p>",

        "2": "<p>Ziba is a <em>naʿar</em> (servant) of the house of Saul — a household manager or major-domo who would know the estate's affairs. His summoning is the first step of the administrative investigation required to fulfill the covenant obligation. Ziba will reappear in the Absalom narrative (chs 16, 19) as an ambiguous figure whose loyalties are contested.</p>",

        "3": "<p>'To show the <em>hesed</em> of God (<em>ḥesed ʾĕlōhîm</em>)' — a stronger formulation than 'my <em>hesed</em>': it is the loyalty that mirrors YHWH's own covenant love. The phrase elevates David's kindness from personal sentiment to covenantal obligation patterned on divine character. This is the key theological move: human covenant loyalty is to mirror and enact the divine <em>hesed</em> that YHWH shows his covenant people.</p>",

        "4": "<p>Lo-debar (<em>lōʾ-dĕḇar</em>) — likely means 'no pasture' or 'no word/thing'; a place-name conveying remoteness and poverty. Mephibosheth has been hiding in a backwater east of the Jordan, presumably afraid that the new dynasty would eliminate any surviving Saulide claimant (as was common ANE practice). His fear of David is grounded in political realism: in the ancient world, new dynasties typically executed potential rival claimants.</p>",

        "5": "<p>David summons Mephibosheth from Lo-debar — from 'no thing' to the royal table. The spatial movement from the margins to the center is the gospel pattern in miniature: those who live in obscurity, fear, and poverty are brought into the presence of the king not by their own merit but by prior covenant commitment. The NT counterpart is the parable of the great banquet (Luke 14:21) where the host sends servants to bring in those from the highways and hedges.</p>",

        "6": "<p>Mephibosheth falls on his face (<em>wayyipōl ʿal-pānāyw wayyiščāḥu</em>). The physical posture is the standard approach before a king — prostration as acknowledgment of absolute power differential. David's response — 'Do not fear' (<em>ʾal-tîrāʾ</em>) — is the word of grace spoken precisely when fear is justified by circumstances. In the NT, 'do not fear' (mē phobeisthe) is the angel's greeting at both the nativity and the resurrection: grace speaks first to fear.</p>",

        "7": "<p>'I will certainly show you <em>hesed</em> for the sake of your father Jonathan' — the threefold structure of the covenant fulfillment: (1) restoration of Saul's land; (2) a permanent place at the king's table; (3) all of this 'for Jonathan's sake' (<em>bĕʿăḇûr yĕhônāṯān ʾāḇîkā</em>). Mephibosheth receives what he could not earn because of the covenant another made. Salvation by grace through another's covenant-relationship is the theological structure of the gospel: we receive what we did not earn because of what Christ has done.</p>",

        "8": "<p>Mephibosheth calls himself 'a dead dog' (<em>keleb mēṯ</em>) — the most demeaning self-description in the Hebrew idiom. In ANE contexts, 'dog' was the lowest social status (cf. 1 Sam 17:43; 24:14). His self-deprecation is not mere politeness but an accurate assessment of his social vulnerability: crippled, from a defeated dynasty, hiding in the east, he has no claim on royal favor. The grace extended to him is the more striking for his explicit sense of unworthiness.</p>",

        "9": "<p>Ziba is appointed as the estate manager for Mephibosheth — all of Saul's land is restored, and Ziba's household (15 sons, 20 servants, v10) becomes the agricultural workforce. The economic restoration is substantial: Saul's estate in Benjamin would have been considerable. The king giving back what he could legitimately have kept (all royal property typically reverted to the new dynasty) demonstrates the radicality of covenant loyalty over political convention.</p>",

        "10": "<p>Mephibosheth will 'eat bread at the king's table always' (<em>ʾākal leḥem ʿal-šulḥānî tāmîḏ</em>). The table as the symbol of covenant belonging is central to the OT — the shared meal seals covenants (Gen 31:54), celebrates redemption (Exod 24:11), and expresses ongoing relationship. The Eucharist inherits this table-fellowship tradition: Christ invites the broken and undeserving to eat at his table perpetually (Rev 3:20; Luke 22:30).</p>",

        "11": "<p>Ziba confirms his compliance; Mephibosheth eats at David's table 'like one of the king's sons.' The simile is remarkable: the enemy dynasty's disabled survivor is treated as a royal family member. This is adoption language — a non-son treated as a son. The NT's language of adoption into the family of God (Rom 8:15-17; Gal 4:5-7; Eph 1:5) draws on exactly this royal adoption pattern: those who are not sons by nature are made sons by covenant grace.</p>",

        "12": "<p>Mephibosheth has a young son, Micha — so the Saul dynasty continues. The genealogy is important: Ziba's household becomes service to a continuing line. In 2 Sam 21:7, Mephibosheth is protected when seven of Saul's descendants are handed over to the Gibeonites — because of the oath between David and Jonathan. The covenant keeps protecting even when its cost is high.</p>",

        "13": "<p>'Mephibosheth lived in Jerusalem, eating at the king's table always. And he was lame in both feet.' The chapter closes with the physical reminder of his disability and the social reality of his restoration held together. His lameness did not disqualify him from the table; his poverty did not make him unwelcome; his lineage did not make him a threat. He lives in the city of the king, at the king's table, always — a picture of what YHWH offers to all those who come to him through covenant: presence, provision, and permanence despite their brokenness.</p>",
    },

    "10": {
        "1": "<p>The death of Nahash king of the Ammonites sets up the diplomatic test. Nahash had shown some kindness to David — possibly during David's outlawry (1 Sam 11:2 shows Nahash as Israel's enemy under Saul, but David's relationship with him may have developed during the fugitive years). The specific nature of Nahash's <em>hesed</em> to David is not stated, but David's intention to reciprocate it with his son Hanun demonstrates the covenant-loyalty principle of ch 9 extending to international relations.</p>",

        "2": "<p>David's diplomatic mission — sending <em>mĕnaḥămîm</em> (comforters) to Hanun — is standard ANE mourning protocol. When a vassal king died, suzerain states would send condolence embassies. The act communicated recognition of the new king's legitimacy and continuity of the relationship. David's initiative here positions him as the senior partner, offering to continue the relationship his predecessor had with Hanun's father.</p>",

        "3": "<p>The Ammonite commanders' suspicion — 'Do you really think David is honoring your father? Has he not sent his servants to you to explore and spy out the city and overthrow it?' — reflects the pervasive distrust of diplomatic overtures in an era of frequent conquest. In the ANE, diplomatic embassies could function as intelligence-gathering missions. The commanders' reading of David's motives is wrong, but not paranoid — it reflects genuine historical experience of how embassies sometimes functioned.</p>",

        "4": "<p>The insult is precise and calculated: shaving half the beard and cutting garments at the buttock-line. In ANE honor-shame cultures, the beard was the primary marker of a man's dignity and social status. Egyptian reliefs show Semitic prisoners with distinctive beards; Assyrian annals describe the cutting of beards as a specific humiliation. To shave half a beard was to expose a man to public ridicule — he could not function in society until it grew back. The garment-cutting exposed the body in a similar way. This was not accidental rudeness but a deliberate diplomatic communication: David's ambassadors are being treated as slaves and fools.</p>",

        "5": "<p>David's compassionate response — 'Stay in Jericho until your beards have grown back' — is itself a culturally informed act of dignity. He does not minimize the shame or demand they return regardless; he gives the men the time to restore their honor before re-entering public life. The act of waiting for the beard to regrow was the only socially available remedy in a culture where honor was visible and bodily. David's instruction protects his servants from further exposure to public shame.</p>",

        "6": "<p>The Ammonites realize they have become 'a stench' (<em>nib'āšû</em>) to David — the idiom for having made oneself an irreconcilable enemy. Now they must mobilize: they hire Aramaean mercenaries from Beth-rehob, Zobah, Tob, and Maacah — a coalition of northern Aramaean kingdoms. The total forces hired (twenty thousand Aramaean infantry plus additional forces from Maacah and Tob) indicates the Ammonites understand they cannot face David's forces alone. The coalition-against-Israel pattern here anticipates the Psalms' descriptions of nations conspiring against YHWH's anointed (Ps 2:1-3).</p>",

        "7": "<p>David sends Joab with 'the entire army of the mighty men' (<em>kōl-haṣṣāḇāʾ haggibbōrîm</em>). The gibbōrîm are David's elite warriors — the thirty, the three (2 Sam 23:8-39). Deploying the full force immediately signals the seriousness of the offense and the thoroughness of the planned response.</p>",

        "8": "<p>The tactical problem: Ammonites at the city gate entrance, Aramaean mercenaries in the open field. Joab faces a two-front situation. The 'entrance of the gate' (<em>peṯaḥ haššaʿar</em>) is a strategic defensive position — the city's fortifications provide a strong anchor for the Ammonite position. The Aramaeans in the open field are the mobile threat that must be defeated before the city itself can be addressed.</p>",

        "9": "<p>Joab's tactical solution: split his forces, personally take the best troops against the Aramaean field army, assign his brother Abishai to face the Ammonites at the gate. The decision to personally lead the harder engagement against the coalition mercenaries shows Joab's military confidence — and the trust between the brothers that a divided command requires.</p>",

        "10": "<p>The coordination between Joab and Abishai — 'if the Aramaeans are too strong for me, come to my rescue; if the Ammonites are too strong for you, I will come' — is a mutual aid pact within the battle itself. The tactical flexibility preserved in the command structure, allowing either commander to reinforce the other, is sophisticated warfare adapted to the two-front problem.</p>",

        "11": "<p>Joab's battle-eve speech to Abishai anticipates the challenge ahead. The conditional structure ('if X, you come; if Y, I come') models covenant mutual-aid language — the same structure as ANE alliance treaties where each party commits to the other's defense. Military covenant language and theological covenant language use the same grammatical forms because they emerge from the same social institutions.</p>",

        "12": "<p>'Be strong (<em>ḥăzaq</em>) and let us fight bravely for our people and for the cities of our God (<em>ʿārê ʾĕlōhênû</em>).' Joab's battle cry is the most explicitly theological utterance in his otherwise pragmatic career. The phrase 'cities of our God' is unique — it identifies the Israelite urban landscape as divinely claimed territory. The Davidic kingdom is not merely a political entity; its cities are YHWH's cities. The second half of the speech is a statement of divine sovereignty: 'The LORD will do what is good in his eyes' — Joab does not claim victory, but submits the outcome to YHWH's judgment. This is rare wisdom from a man who usually acts on his own judgment.</p>",

        "13": "<p>The Aramaeans flee before Joab. The narrative is terse — the entire battle is reported in two verbs: Joab advanced, Syrians fled. The swiftness of the collapse suggests either that the mercenaries were not fully committed to the Ammonite cause, or that Joab's force was overwhelming. ANE mercenaries who lost in initial contact often retreated rather than fight to the last man for a foreign employer.</p>",

        "14": "<p>The Ammonites see the Aramaeans flee and themselves retreat into the city. The domino effect — one front's collapse causing the other to break — is a standard tactical vulnerability of coalition forces with different national interests. Joab does not press the siege; he returns to Jerusalem. The chapter's first phase ends without full resolution, setting up the larger coalition mobilization in vv 15-19.</p>",

        "15": "<p>The Aramaean coalition regroups — Hadadezer (defeated in ch 8) now mobilizes a larger Aramaean force from beyond the Euphrates. This is the second round: the initial defeat triggered a escalation rather than submission. The pattern is familiar from the Exodus: each plague leads Pharaoh to a brief submission followed by renewed resistance. Military humiliation and diplomatic humiliation both can produce escalation before capitulation.</p>",

        "16": "<p>Shobach, Hadadezer's army commander, leads the augmented Aramaean forces to Helam. Helam is probably east of the Jordan, somewhere in Transjordan. The mobilization from 'beyond the Euphrates' indicates the full reach of the Aramaean coalition — and thus the significance of David's response, which requires crossing the Jordan personally.</p>",

        "17": "<p>David himself crosses the Jordan and marches to Helam — unlike his delegation of command to Joab in the first phase. The king's personal presence in the decisive engagement contrasts sharply with his absence from battle in 11:1. Here, at the height of his power, David goes; after Bathsheba, he sends others. The contrast sets up the theological analysis of ch 11's opening verse.</p>",

        "18": "<p>The Aramaean defeat: 700 chariot crews (or 7,000 according to 1 Chr 19:18) and 40,000 horsemen (or footsoldiers in Chronicles). The textual discrepancy between 2 Sam and 1 Chr is well-known; the numbers in both represent decisive destruction. Shobach the commander dies in the battle — the decapitation of the enemy's military leadership marks the completeness of the victory.</p>",

        "19": "<p>All the vassal kings of Hadadezer make peace with Israel and become subject (<em>wayyaʿaḇĕḏûm</em>). The Aramaean coalition collapses; the northern tier of potential threats is neutralized. The Ammonites, now without their Aramaean allies, will remain to be dealt with (ch 11-12). The verse closes with the phrase 'and the Syrians feared to help the Ammonites anymore' — a diplomatic and military isolation of Israel's eastern enemy achieved through the defeat of their sponsor.</p>",
    },

    "11": {
        "1": "<p>'At the return of the year (<em>lĕtĕšûḇaṯ haššānâ</em>), at the time when kings typically march out to war (<em>lēṯ ṣēʾṯ hamĕlāḵîm</em>).' The temporal formula marks a seasonal and professional expectation: spring campaigns began after the winter rains ended (roughly March-April), when roads dried and foraging was possible. Egyptian, Assyrian, and Babylonian annals all record spring as the standard campaign season. Joab goes; David stays. The narrative's implicit judgment is embedded in the contrast: the king who should be leading his armies is instead at home in Jerusalem. This is not an administrative decision — it is a structural departure from the king's vocational role.</p>",

        "2": "<p>David's walk on the palace roof in the evening (<em>lĕʿēṯ hāʿereḇ</em>) — flat rooftop terraces were standard domestic architecture in the ancient Levant, used for sleeping in summer and evening relaxation. The palace roof would have overlooked lower residential areas. The woman bathing is not identified as behaving improperly — ritual purification baths (mikveh) were taken in private domestic spaces, and Bathsheba had no expectation of being observed from the palace roof. The power differential is entirely David's: he sees, he inquires, he sends. She is passive throughout the sequence.</p>",

        "3": "<p>'She is Bathsheba daughter of Eliam, the wife of Uriah the Hittite.' The identification provided to David contains all the information needed to stop: she is another man's wife (adultery), and her husband is named — not an anonymous soldier but a known man in David's own elite guard (23:39, Uriah appears in the list of the Thirty). The informant may have intended the identification as a caution; David proceeds anyway. The additional genealogical note — Eliam is possibly the son of Ahithophel (23:34) — means the Bathsheba affair may have contributed to Ahithophel's decision to join Absalom's rebellion.</p>",

        "4": "<p>'She came to him (<em>waṯāḇōʾ ʾēlāyw</em>), and he lay with her.' The syntax is clinical. Bathsheba 'had just completed her ritual purification from her monthly uncleanness' — this note establishes three things: (1) she was observing Torah (Lev 15:19-30); (2) she could not have been pregnant before this encounter; (3) the pregnancy reported in v5 is unambiguously David's. The legal implication is carefully built into the narrative.</p>",

        "5": "<p>'I am pregnant' — two words in Hebrew (<em>hārâ ʾānōḵî</em>). The message's brevity conveys its weight. The entire subsequent narrative — the summons of Uriah, the attempted cover-up, the calculated murder, the marriage — unfolds from this two-word report. David's response to crisis will be concealment rather than confession, and each step of the cover-up compounds the sin.</p>",

        "6": "<p>David's first attempt at cover-up: send for Uriah, who is with the army besieging Rabbah. The plan is to have Uriah sleep with his wife so the pregnancy appears legitimate. The mechanics require Uriah's willing cooperation — specifically his going home to his wife. David asks about the war (v7) as if the summons were routine — a military debriefing rather than an operation in domestic deception.</p>",

        "7": "<p>The casual inquiry about Joab and the troops is the cover for the real purpose: send Uriah home. Joab's welfare, the troops' welfare, the war's progress — David asks about these things as if concerned for the campaign he chose not to lead. The irony is dark: the king who should be at the siege is interrogating a soldier about how the siege he abandoned is going.</p>",

        "8": "<p>'Go down to your house and wash your feet' (<em>rĕd lĕḇêṯĕkā ûrḥaṣ raglêykā</em>). 'Wash your feet' is a common idiom for domestic rest after travel — and possibly a euphemism for sexual intercourse (cf. Ruth 3:4). The present David sends after Uriah (<em>maśʾeṯ</em>) is a generous gift from the king — sweetening the invitation. Everything is being done to make the domestic visit natural and attractive.</p>",

        "9": "<p>Uriah does not go home. He sleeps at the palace entrance with the servants. His act of solidarity with the army is entirely voluntary — he is not commanded to abstain. His explanation (v11) invokes the ark, Israel, Judah, and the troops in the field. Uriah the Hittite, a foreigner, demonstrates a level of covenantal faithfulness that the Israelite king is conspicuously failing to exhibit.</p>",

        "10": "<p>David's incredulous question — 'You have just come from a journey; why did you not go home?' — exposes his own frame of reference. He assumed comfort would override solidarity; Uriah's choice confounds him. David cannot comprehend why a man would choose tent-solidarity with the troops over the domestic pleasures of a homecoming.</p>",

        "11": "<p>Uriah's speech is one of the most remarkable in the David narrative: 'The ark and Israel and Judah are staying in tents (<em>ʾōhālîm</em>), and my lord Joab and your servants are camping in the open field. Shall I then go to my house, to eat and drink, and to lie with my wife? As YHWH lives and as you live, I will not do this thing.' A Hittite invokes YHWH's name and refuses to violate the code of military solidarity. The mention of the ark is particularly pointed: the ark's presence with the army consecrates the campaign as holy war, during which sexual abstinence was required (cf. 1 Sam 21:5). Uriah knows the rules of holy war better than the king who should be leading it.</p>",

        "12": "<p>David extends Uriah's stay by one day — buying time to try the drunkenness strategy (v13). The delay does not change Uriah's commitment; it only prolongs David's exposure to a man whose integrity is a standing rebuke.</p>",

        "13": "<p>David makes Uriah drunk. Even intoxicated, Uriah does not go home. The third attempt at cover-up fails as completely as the first two. Uriah's moral commitment survives even impaired judgment. This is the narrative's sharpest irony: the sober king cannot match the drunk soldier's integrity.</p>",

        "14": "<p>David writes a letter to Joab — sent by Uriah's own hand. The letter contains Uriah's death warrant. The horror of the act is intensified by its mechanism: Uriah carries the document that orders his own execution, trusting the king's seal. This is a perversion of the messenger institution — the man who trusted the king's communication is killed by it.</p>",

        "15": "<p>'Put Uriah in the front of the fiercest fighting, then pull back from him so that he is struck down and dies.' The order requires Joab's complicity — it is not an order that can be followed without understanding its purpose. Joab is asked to commit judicial murder by military proxy. His compliance without recorded objection (contrast his later refusal to kill the king's son, 18:5) indicates his acceptance of the king's authority even in moral extremity.</p>",

        "16": "<p>Joab executes the plan, stationing Uriah where the strongest defenders would be. The siege of Rabbah — the military operation David should have been leading — becomes the instrument of his cover-up. The war he avoided attending is now accomplishing his private crime.</p>",

        "17": "<p>Uriah dies in the sortie, along with other unnamed soldiers. The collateral death of unnamed men to cover one man's sin is one of the narrative's darkest notes. David's private moral failure costs multiple lives — Uriah is the target, but soldiers who happened to be stationed with him die as well. Private sin has public casualties.</p>",

        "18": "<p>Joab sends a battle report — covering the bad news of the sortie's losses with the embedded good news that Uriah is dead. The report is structured as a test: Joab instructs the messenger (v19-21) on how to handle the king's predictable anger at the tactical mistake of approaching the wall.</p>",

        "19": "<p>Joab's instruction to the messenger anticipates David's anger at the tactical misjudgment. Joab knows David well enough to predict his first response will be military criticism before he processes the personal news. The pre-scripted answer (v21b) is designed to defuse that anger by revealing that Uriah is dead.</p>",

        "20": "<p>The anticipated rebuke references Abimelech and the woman of Thebez (Judges 9:52-54) — a precedent from Israel's own history where a commander was killed approaching a city wall. Joab is inviting David to critique him exactly as any competent commander would be criticized for the tactical mistake, knowing the criticism will be interrupted by the death-news.</p>",

        "21": "<p>The citation of Abimelech's death serves a double function: it is the exemplar Joab expects David to invoke, and it is an ironic comparison — Abimelech was killed while pursuing illegitimate power and was struck down by a woman. David is also pursuing an illegitimate goal (concealment of adultery) and will also be destroyed — not by a woman but by a prophet.</p>",

        "22": "<p>The messenger delivers the full account of the battle. The narrative compression here (v22 summarizes what vv 19-21 prepared us for) moves quickly to the crucial exchange.</p>",

        "23": "<p>The messenger recounts the battle, including the enemy sortie that caused the casualties. He is giving David the military context before the personal news — following Joab's script.</p>",

        "24": "<p>The archers' role in the casualties is detailed. The messenger lists David's fallen servants, ending with 'and your servant Uriah the Hittite is also dead.' The 'also' is devastating in its casualness: Uriah is listed among the fallen soldiers as if his death were incidental, not engineered.</p>",

        "25": "<p>David's response — 'Do not let this distress you; the sword is no respecter of persons (<em>ʾāḵĕlâ ḥereḇ gam-zeh gam-zeh</em>, lit. the sword devours this one as well as that one)' — is the language of military fatalism deployed to cover moral atrocity. His instruction to 'strengthen the attack against the city' redirects everyone's attention to the military task. The king sounds like a commander managing casualties; he is actually managing a crime scene.</p>",

        "26": "<p>Bathsheba mourns her husband. The mourning is real — whatever the power dynamics of her earlier summons, she has lost her husband. The mourning period (<em>wattispad</em>, wayyitammu, the formal stages of grief) is observed. Narrative space is given to her loss even in a chapter about David's crime.</p>",

        "27": "<p>'When the mourning was over, David sent for her and brought her to his palace. She became his wife and bore him a son. But the thing David had done was evil in the LORD's eyes (<em>wayyēraʿ hadāḇār ʾăšer-ʿāśâ dāwîḏ bĕʿênê YHWH</em>).' The chapter ends with the marriage accomplished and the child born — and then the theological verdict. The narrator holds the entire sequence together: the cover-up worked, the child came, the marriage happened — and YHWH noticed. The final clause of ch 11 is the final clause of the tragedy: not a human observer catching David, but YHWH's own assessment delivered in the text itself before Nathan speaks a word. Divine judgment is not announced by a prophet but embedded in the narrative's final sentence.</p>",
    }
}


def main():
    existing = load_comm('mkt-context', '2samuel')
    merge_comm(existing, SAMUEL)
    save_comm('mkt-context', '2samuel', existing)

    import json as _json
    il = _json.loads((ROOT / 'data/interlinear/2samuel.json').read_text())
    all_ok = True
    for ch in range(8, 12):
        ck = str(ch)
        missing = set(il.get(ck, {}).keys()) - set(existing.get(ck, {}).keys())
        if missing:
            print(f'ch {ch} STILL MISSING: {sorted(missing, key=int)}')
            all_ok = False
        else:
            print(f'ch {ch}: complete ({len(existing.get(ck, {}))} verses)')
    if all_ok:
        print('All verses present ✓')
    print(f'Total chapters in file: {len(existing)}')


if __name__ == '__main__':
    main()
