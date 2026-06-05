"""
MKT Echo Layer — Romans chapters 1–3
Run: python3 scripts/zc-echo-romans-1-3.py

Source data used:
- data/interlinear/romans.json
- data/translation/glossary-greek.json (πίστις disp=3, δικαιοσύνη disp=4, νόμος disp=3)
- data/translation/notes/romans.json
- data/translation/draft/mediating/romans.json
- data/parallels/romans.json (absorbed: 1:17 Hab 2:4; 3:4 Ps 51:4; 3:10 Ps 14:1-3;
  3:13 Ps 5:9 + Ps 140:3; 3:14 Ps 10:7; 3:15-17 Isa 59:7-8; 3:18 Ps 36:1)

Key decisions in this range:
- Rom 1:4 "appointed Son of God in power" — Ps 2:7 is allusion not fulfillment;
  the NT explicit declaration is Acts 13:33 / Heb 1:5. Echo classified allusion.
- Rom 1:17 Hab 2:4 — Paul cites LXX ("the righteous will live by faith"), absorbing
  as quote (parallels had prophecy-source → fulfillment, but Paul uses it as a proof-
  text about the principle of faith, not messianic prediction per se; classified quote).
- Rom 2:15 "law written on hearts" — Jer 31:33 is the background text Paul expects
  readers to know; the internalized law in Gentiles is a shadow of new covenant realities.
- Rom 2:24 Isaiah 52:5 — Paul is quoting LXX Isaiah with "as it is written"; classified quote.
- Rom 3:4 Ps 51:4 — direct quotation from LXX Ps 50:6; classified quote (absorbed from parallels).
- Rom 3:10-12 Ps 14:1-3 — direct composite quotation; classified quote (absorbed).
- Rom 3:13-18 — six quotations from Ps 5:9, Ps 140:3, Ps 10:7, Isa 59:7-8, Ps 36:1;
  all absorbed from parallels as quotes.
- Rom 3:25 ἱλαστήριον — the mercy seat (kapporeth/LXX hilastērion) of Exod 25:17 and
  Lev 16 is the primary type; classified type because the structural correspondence
  (atoning blood, presence of God, covering of sin) is what Paul is invoking.
- Rom 1:21-23 exchange-of-glory motif — Ps 106:20 ("exchanged their glory") is the
  most verbally close OT text; Jer 2:11 parallels it; both classified allusion.
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

ROMANS_ECHOES = {
  "1": {
    "1": [
      {"type": "allusion", "target": "Isa 49:1", "note": "The Servant called from birth and set apart — Paul's language of being 'called' and 'set apart' (aphōrismenos) echoes the Isaianic Servant's commission before birth, activating the mission-to-Gentiles register that runs through 1:5."}
    ],
    "2": [
      {"type": "theme", "target": "Amos 3:7", "note": "God revealing his purposes through his servants the prophets — Paul's claim that the gospel was 'promised beforehand through his prophets in the Holy Scriptures' participates in this prophetic self-understanding of Israel's Scripture as advance disclosure of redemptive history."}
    ],
    "3": [
      {"type": "fulfillment", "target": "2 Sam 7:12-13", "note": "The Davidic covenant promised a descendant of David who would establish an enduring kingdom — Paul explicitly grounds Christ's Davidic descent here as the fulfillment of this dynastic promise, the 'seed' language of 2 Sam 7:12 now arriving."},
      {"type": "allusion", "target": "Isa 11:1", "note": "The Branch from Jesse's stump — Isaiah's 'shoot from the stump of Jesse' anticipates a Davidic heir after dynastic collapse; Paul's 'descended from David according to the flesh' stands in this trajectory."}
    ],
    "4": [
      {"type": "allusion", "target": "Ps 2:7", "note": "The royal decree 'You are my Son; today I have begotten you' — Paul's declaration that Christ was 'appointed (horisthentos) Son of God in power by his resurrection' echoes the enthronement language of Ps 2:7, which Acts 13:33 and Heb 1:5 cite explicitly as resurrection-fulfillment; Paul assumes the same frame."},
      {"type": "allusion", "target": "Ps 110:1", "note": "The Lord's declaration to the Davidic king — the resurrection vindicating Christ as 'Son of God in power' draws on the Davidic enthronement complex of Ps 110, which the early church consistently applied to resurrection-exaltation."}
    ],
    "5": [
      {"type": "fulfillment", "target": "Isa 49:6", "note": "The Servant commissioned as 'a light to the Gentiles, that my salvation may reach the ends of the earth' — Paul's call to bring 'all the Gentiles to the obedience that comes from faith' is the realized mission of the Isaianic Servant, now mediated through the apostle of the risen Christ."}
    ],
    "7": [
      {"type": "theme", "target": "Exod 19:6", "note": "Israel called to be a 'holy nation' (gōy qādōsh) at Sinai — Paul addresses the Roman believers as 'called to be his holy people' (klētois hagiois), applying to the new covenant assembly the election-and-calling language originally marking Israel at Sinai."}
    ],
    "16": [
      {"type": "allusion", "target": "Ps 98:2-3", "note": "The Lord 'has made known his salvation; his righteousness he has revealed openly to the nations' — the psalm anticipates a universal disclosure of divine righteousness to all peoples, precisely the theological claim Paul makes for the gospel in v.16–17."},
      {"type": "theme", "target": "Isa 46:13", "note": "God's salvation and righteousness arriving together — Isaiah repeatedly links God's tsedaqah (righteousness) and yeshuah (salvation) as simultaneous divine acts; Paul's gospel announcement in v.16 is the arrival of this promised conjunction."}
    ],
    "17": [
      {"type": "quote", "target": "Hab 2:4", "note": "Paul cites the LXX of Habakkuk ('the righteous will live by faith') as the scriptural warrant for his thesis that righteousness is by faith. Habakkuk's original context speaks of trusting God through the Babylonian crisis; Paul reads the principle as the universal structure of covenant life before God, fulfilled in Christ."}
    ],
    "18": [
      {"type": "theme", "target": "Ps 2:5", "note": "The Lord speaking in his wrath against nations that rebel — Paul's 'wrath of God is being revealed from heaven' picks up the theophanic wrath-language of Ps 2 and the prophets, presenting the present revelation of judgment as continuation of this biblical pattern."},
      {"type": "allusion", "target": "Nah 1:2-3", "note": "God's wrath against those who oppose him, not abating — Nahum's portrait of divine wrath as a present reality revealed in history against unrepentant wickedness is the OT frame Paul assumes for his anthropological argument in 1:18–32."}
    ],
    "19": [
      {"type": "theme", "target": "Ps 19:1-4", "note": "The heavens declaring God's glory, the skies proclaiming his handiwork — Paul's claim that 'what may be known about God is plain to them, because God has made it plain to them' through created things directly inhabits the world of Ps 19:1-4, which declares that creation's witness reaches all the earth."}
    ],
    "20": [
      {"type": "allusion", "target": "Wis 13:1-9", "note": "The Wisdom of Solomon argues that Gentiles who failed to recognize God from the beauty of creation are 'without excuse' (anapologētos) — Paul uses the identical term and the same logic, indicating he is engaging with a known Jewish apologetic tradition about natural revelation and pagan culpability."}
    ],
    "21": [
      {"type": "allusion", "target": "Jer 2:5", "note": "Israel 'walked after worthless things and became worthless' (LXX: emataiōthēsan) — Paul's 'their thinking became futile (emataiōthēsan)' echoes this Jeremianic indictment, extending Israel's covenant failure to the entire human race."},
      {"type": "theme", "target": "Deut 4:19", "note": "Moses warns Israel not to be drawn into astral worship, the idolatry of the nations — Paul's portrait of humanity suppressing knowledge of God and turning to creature-worship stands in the shadow of this Deuteronomic warning about the corruption that follows from turning away from the Creator."}
    ],
    "22": [
      {"type": "allusion", "target": "Jer 10:14", "note": "Every goldsmith is shamed by his idols — the fool-motif (claiming wisdom while practicing folly) in Jeremiah's polemic against idol-makers is the OT background for Paul's 'although they claimed to be wise, they became fools.'"}
    ],
    "23": [
      {"type": "allusion", "target": "Ps 106:20", "note": "Israel 'exchanged their glory for an image of an ox' — Paul's language ('exchanged the glory of the immortal God for images') is a near-verbal echo of this psalm verse describing Israel's golden calf sin, which Paul broadens to describe the universal human turn from Creator to creature."},
      {"type": "allusion", "target": "Jer 2:11", "note": "The nations exchanged their gods, but Israel exchanged its glory for 'what does not profit' — Jeremiah's indictment of Israel's apostasy uses the same exchange-structure; Paul universalizes it as the defining act of fallen humanity."}
    ],
    "24": [
      {"type": "theme", "target": "Ps 81:12", "note": "God 'gave them over to their stubborn hearts to follow their own devices' — the divine act of abandonment as judgment is already an OT pattern in Ps 81:12, where Israel's persistent rebellion results in God releasing them to the consequences of their own choices; Paul's triple 'gave them over' (vv.24, 26, 28) intensifies this structure."}
    ],
    "25": [
      {"type": "allusion", "target": "Isa 44:20", "note": "The idol-worshiper 'feeds on ashes; a deluded heart has led him astray' — Isaiah's satirical analysis of idolatry (choosing created wood for both fire and god) is the prophetic background for Paul's 'worshiped and served created things rather than the Creator.'"}
    ],
    "28": [
      {"type": "theme", "target": "Ezek 20:25", "note": "God gave Israel 'statutes that were not good and ordinances by which they could not live' as judicial hardening — the Ezekielian concept of divine giving-over to corrupted thinking as covenant judgment illuminates Paul's 'God gave them over to a depraved mind,' presenting this not as divine abandonment of responsibility but as the judicial dimension of human rebellion."}
    ],
    "32": [
      {"type": "allusion", "target": "Ps 50:18", "note": "God rebukes those who 'see a thief and are pleased with him' — the motif of approving what God condemns as itself a form of condemnation is anticipated in Ps 50's indictment of those who consent to wickedness; Paul concludes his list with this communal dimension of guilt."}
    ]
  },
  "2": {
    "1": [
      {"type": "allusion", "target": "Ps 50:16-21", "note": "God's rebuke to the one who recites the law but hates discipline and casts his words behind him — Paul's 'you who pass judgment do the same things' inhabits the world of Ps 50:16-21, where the liturgically observant person stands equally condemned for the same underlying failures."}
    ],
    "4": [
      {"type": "allusion", "target": "Joel 2:13", "note": "The Lord is 'gracious and compassionate, slow to anger and abounding in love' and relents from sending calamity — Paul's appeal to the 'kindness, forbearance and patience' of God that leads to repentance is grounded in this classic OT characterization of divine patience (cf. Exod 34:6-7), well-known through Joel and the prophetic tradition."},
      {"type": "allusion", "target": "Ps 103:8", "note": "The Lord is 'slow to anger and abounding in love' — the divine patience Paul invokes as itself a summons to repentance draws on the deep reservoir of psalmic praise for God's covenantal forbearance toward his people."}
    ],
    "5": [
      {"type": "allusion", "target": "Zeph 1:14-18", "note": "The day of the Lord's wrath, a day of distress and anguish — Paul's 'day of God's wrath, when his righteous judgment will be revealed' imports the prophetic Day-of-the-Lord tradition, which Zephaniah presents as a universal day of reckoning for all who have hardened themselves."}
    ],
    "6": [
      {"type": "allusion", "target": "Ps 62:12", "note": "You, O Lord, are loving; surely you will reward each person according to what he has done — Paul's principle that God 'will repay each person according to what they have done' cites this psalmist claim, grounding impartial judgment in the character of the covenant God."},
      {"type": "allusion", "target": "Prov 24:12", "note": "God 'who weighs hearts, does he not know? He will repay each person according to what they have done' — the proverb Paul alludes to confirms that individual moral accountability before the all-seeing God is a consistent OT axiom, not a Pauline innovation."}
    ],
    "11": [
      {"type": "allusion", "target": "Deut 10:17", "note": "The Lord 'shows no partiality and accepts no bribes' — Paul's 'God does not show favoritism' (prosōpolēmpsia ouk estin para tō theō) applies this Deuteronomic principle of divine impartiality, originally stated about God's dealings with Israel, to the universal frame of Jew-Gentile judgment."}
    ],
    "12": [
      {"type": "theme", "target": "Amos 1:3-2:3", "note": "God's judgment on nations that 'do not have the law' — Amos's oracles against surrounding nations for moral violations they committed without Sinai's covenant demonstrate that moral accountability exists apart from Mosaic legislation, the OT precedent for Paul's argument in 2:12."}
    ],
    "13": [
      {"type": "allusion", "target": "Lev 18:5", "note": "Moses commands that whoever 'does these things will live by them' — the principle that doing the law (not merely hearing it) brings life is already embedded in Lev 18:5 (cf. Deut 4:1); Paul's 'doers of the law will be declared righteous' restates this, though his larger argument (3:20) will show that no one in fact does it."}
    ],
    "15": [
      {"type": "allusion", "target": "Jer 31:33", "note": "God's new covenant promise to write the law 'on their hearts' — Paul's observation that Gentiles 'show that the requirements of the law are written on their hearts' holds up the natural moral sense as a shadow of what Jeremiah prophesied as the new covenant reality; Paul's point is the universality of moral knowledge, while the new covenant fulfillment awaits his later argument."}
    ],
    "17": [
      {"type": "theme", "target": "Mic 3:11", "note": "Micah condemns the leaders who 'lean upon the Lord' and say 'Is not the Lord among us?' while practicing injustice — Paul's portrait of the Jew who boasts in God and relies on the law while breaking it reprises this prophetic critique of confident covenant identity unmatched by covenant obedience."}
    ],
    "19": [
      {"type": "allusion", "target": "Isa 42:6-7", "note": "The Servant called to be 'a light for the Gentiles, to open eyes that are blind' — Paul's ironic portrait of the law-confident Jew as 'a light for those who are in the dark' echoes the Isaianic Servant's mission language, here applied to the self-understanding of teachers of the law; the irony is that they claim the Servant's role while failing the Servant's character."}
    ],
    "24": [
      {"type": "quote", "target": "Isa 52:5", "note": "Paul quotes the LXX: 'God's name is blasphemed among the Gentiles because of you' — in Isaiah this indicts Israel in exile whose suffering caused the nations to mock Israel's God; Paul applies it to Torah-breaking Jews whose conduct dishonors God's name in the diaspora context, preserving the original connection between covenant behavior and divine reputation among the Gentiles."},
      {"type": "allusion", "target": "Ezek 36:20-23", "note": "Israel profaned God's name among the nations by its conduct in exile — Ezekiel's charge that Israel's behavior 'profaned my holy name' among the Gentiles provides the second stream of this tradition Paul draws on, confirming that the connection between covenant failure and Gentile contempt for God's name was a known prophetic theme."}
    ],
    "25": [
      {"type": "theme", "target": "Gen 17:10-14", "note": "The circumcision covenant established between God and Abraham — Paul's argument that circumcision 'has value if you observe the law' engages the foundational covenant sign of Gen 17; his point is not to abolish but to expose the conditionality embedded in the covenant structure itself (Gen 17:14: the uncircumcised who breaks the covenant is 'cut off')."}
    ],
    "28": [
      {"type": "allusion", "target": "Deut 30:6", "note": "Moses prophesies that God himself will 'circumcise your hearts and the hearts of your descendants' — Paul's distinction between outward and inward circumcision (2:28-29) is anticipated in Deuteronomy's own internalization of the covenant sign; the argument is not an innovation over against Moses but the fulfillment of what Moses already foresaw."}
    ],
    "29": [
      {"type": "allusion", "target": "Jer 4:4", "note": "Jeremiah commands Israel to 'circumcise yourselves to the Lord, circumcise your hearts' and not merely the flesh — Paul's 'circumcision is circumcision of the heart, by the Spirit' is the fulfillment of Jeremiah's prophetic demand; the prophetic critique that Israel's external sign needed to become an inner reality is now resolved by Spirit-work."},
      {"type": "allusion", "target": "Deut 10:16", "note": "Moses commands Israel to 'circumcise your hearts' and stop being stiff-necked — the Deuteronomic demand for heart-circumcision as the inner corollary of the physical sign is the OT foundation Paul builds on when he redefines the true Jew as one circumcised 'inwardly, by the Spirit.'"}
    ]
  },
  "3": {
    "2": [
      {"type": "theme", "target": "Ps 147:19-20", "note": "God 'has revealed his word to Jacob, his laws and decrees to Israel; he has done this for no other nation' — Paul's 'the Jews have been entrusted with the very words of God' affirms this distinctive covenantal gift; the argument builds toward 3:1-2 being an asset whose abuse is the real indictment."}
    ],
    "3": [
      {"type": "theme", "target": "Num 23:19", "note": "God is 'not a man, that he should lie' — Paul's 'will their unfaithfulness nullify God's faithfulness?' presupposes the OT axiom of divine reliability that Balaam's oracle states plainly; the possibility of covenant nullification based on human failure is excluded by God's own character."}
    ],
    "4": [
      {"type": "quote", "target": "Ps 51:4", "note": "David's penitential confession: 'so that you are proved right in your words and justified when you judge' — Paul quotes the LXX (Ps 50:6 LXX) to demonstrate that Scripture itself recognizes human guilt and divine vindication as the baseline reality; David's confession of universal human fallibility before God's righteous judgment becomes Paul's proof-text for God's truthfulness against all human challenge."}
    ],
    "9": [
      {"type": "allusion", "target": "Ps 14:1-3", "note": "The psalm's diagnosis that 'all have turned away, all have become corrupt; there is no one who does good, not even one' — Paul's charge that 'Jews and Gentiles alike are all under the power of sin' prepares for the catena of quotations beginning at v.10; the universal scope Paul asserts is already the universal scope Ps 14 describes."}
    ],
    "10": [
      {"type": "quote", "target": "Ps 14:1-3", "note": "Paul opens his catena with a composite quotation from Ps 14:1-3 (cf. Ps 53:1-3): 'There is no one righteous, not even one; no one who understands, no one who seeks God.' The psalm describes the corrupt conditions the Lord surveys from heaven; Paul quotes it as Scripture's own declaration of the universal condition of sin, closing off any Jewish exemption from the indictment."}
    ],
    "11": [
      {"type": "quote", "target": "Ps 53:1-3", "note": "The parallel psalm to Ps 14, surveying universal human corruption — vv.11-12 continue the composite quotation drawing on both psalms, reinforcing that the diagnosis of no righteous person, no seeker of God, is not an isolated text but a repeated scriptural witness."}
    ],
    "12": [
      {"type": "allusion", "target": "Eccl 7:20", "note": "Qohelet's observation that 'there is not a righteous man on earth who does what is right and never sins' — while Paul's catena draws primarily on Psalms, Ecclesiastes provides a wisdom-literature parallel confirming that the universal verdict is found across multiple Old Testament genres, not only in the lament psalms."}
    ],
    "13": [
      {"type": "quote", "target": "Ps 5:9", "note": "Paul quotes LXX: 'Their throats are open graves; with their tongues they practice deceit' — Ps 5:9 is David's description of his enemies' speech as corrupt at its source; Paul deploys it as part of the scriptural proof that human sinfulness extends to the organs of speech and social life."},
      {"type": "quote", "target": "Ps 140:3", "note": "'The poison of vipers is on their lips' — Paul's second quotation in v.13 is from Ps 140:3 (LXX 139:4), where the psalmist describes violent enemies whose words are lethal; Paul extends this description from enemies to the universal human condition before God."}
    ],
    "14": [
      {"type": "quote", "target": "Ps 10:7", "note": "Paul quotes: 'Their mouths are full of cursing and bitterness' — Ps 10:7 describes the wicked man's speech; Paul continues his catena to demonstrate that the corruption of speech catalogued in these psalms is Scripture's testimony against all people, not merely David's enemies."}
    ],
    "15": [
      {"type": "quote", "target": "Isa 59:7-8", "note": "Paul quotes Isa 59:7-8 LXX: 'Their feet are swift to shed blood; ruin and misery mark their paths, and the way of peace they do not know.' Isaiah's indictment of Israel's corporate moral failure — feet, paths, blood, peace — becomes Paul's next proof that scriptural testimony to human corruption is found in the prophets as well as the psalms, and applied originally to God's own covenant people."}
    ],
    "18": [
      {"type": "quote", "target": "Ps 36:1", "note": "Paul closes his catena with Ps 36:1: 'There is no fear of God before their eyes' — the psalmist identifies the root of wickedness as the absence of the fear of God; Paul positions this as the theological summary of the preceding six quotations, the foundational condition from which all the specific corruptions flow."}
    ],
    "19": [
      {"type": "allusion", "target": "Ps 107:42", "note": "All wickedness stops its mouth before God's justice — Paul's 'every mouth may be silenced and the whole world held accountable to God' echoes the psalmist's picture of universal accountability; the courtroom metaphor of silencing is already present in the psalmic tradition."}
    ],
    "20": [
      {"type": "allusion", "target": "Ps 143:2", "note": "David's plea: 'Do not bring your servant into judgment, for no one living is righteous before you' — Paul's 'no one will be declared righteous in God's sight by the works of the law' is the forensic generalization of David's own penitential acknowledgment; the psalmist's recognition that all flesh falls short before God becomes Paul's doctrinal axiom."},
      {"type": "allusion", "target": "Lev 18:5", "note": "The promise that 'the man who does them will live by them' — Paul's argument that the law produces 'consciousness of sin' rather than righteousness stands in deliberate tension with Lev 18:5's life-promise; the law's function as sin-revealer is the flip side of its life-promise, a point Paul will develop in ch. 7."}
    ],
    "21": [
      {"type": "allusion", "target": "Isa 53:11", "note": "The Servant who 'will justify many, and he will bear their iniquities' — Paul's 'righteousness of God has been made known, to which the Law and the Prophets testify' has the Isaianic Servant's justifying work as its most specific prophetic anticipation; the righteousness-through-substitution structure of Isa 53 is precisely what Paul will elaborate in 3:24-26."},
      {"type": "allusion", "target": "Isa 51:5-6", "note": "God's righteousness is 'near,' his salvation 'on the way,' and 'my righteousness will never end' — Isaiah's declaration that God's tsedaqah arrives as saving action for his people is the prophetic basis for Paul's claim that the righteousness of God 'has been made known' now, in the gospel event."}
    ],
    "22": [
      {"type": "allusion", "target": "Isa 45:22-23", "note": "'Turn to me and be saved, all the ends of the earth' — the universal scope of God's saving righteousness Paul announces in v.22 ('to all who believe, there is no difference between Jew and Gentile') realizes the Isaianic invitation to all nations, rooted in the one God confessed in the Shema."}
    ],
    "23": [
      {"type": "allusion", "target": "Gen 3:23", "note": "Adam and Eve expelled from the garden, cut off from God's presence — 'all have sinned and fall short of the glory of God' names the post-Fall condition of humanity: the glory of intimate presence with God, forfeited at the Fall, is what sin structurally bars human beings from recovering."},
      {"type": "theme", "target": "Ps 14:3", "note": "'All have turned away, all have together become corrupt' — Paul's universal verdict ('all have sinned') is not rhetorical overstatement but the psalmist's own conclusion about the human condition when viewed from God's perspective; the catena of 3:10-18 has established the scriptural basis for this summary."}
    ],
    "24": [
      {"type": "allusion", "target": "Isa 44:22-23", "note": "God redeems Israel ('I have swept away your offenses like a cloud') and calls the heavens and earth to shout for joy at this redemption — Paul's 'justified freely by his grace through the redemption (apolytrōsis)' locates Christ's work in the trajectory of the divine redemptive acts for which Isaiah's second half calls all creation to rejoice."},
      {"type": "allusion", "target": "Exod 6:6", "note": "God promises to 'redeem' Israel from Egypt with an outstretched arm — the apolytrōsis (redemption) language Paul uses was the standing term in Jewish Scripture for the Exodus liberation; Paul presents Christ's atoning work as the definitive new-exodus redemption, the event to which Israel's foundational liberation pointed."}
    ],
    "25": [
      {"type": "type", "target": "Exod 25:17-22", "note": "The kapporeth — the gold cover of the ark (LXX: hilastērion) — is the locus where God meets Israel and atones for sin on the Day of Atonement. Paul uses the identical term (hilastērion) for Christ, identifying him as the new mercy seat: the place where God and humanity meet, where blood is presented, where sin is covered. The structural correspondence (atoning blood, divine presence, covering of transgression) is the type Paul is explicitly invoking."},
      {"type": "type", "target": "Lev 16:14-16", "note": "The high priest sprinkles blood on the mercy seat to make atonement for the sins of Israel — Paul's 'through the shedding of his blood' activates the Day of Atonement ritual as the type that Christ's death fulfills: the blood, the presentation before God, and the covering of sins previously 'left unpunished' all map directly onto the Yom Kippur structure."},
      {"type": "allusion", "target": "Isa 53:10", "note": "God making the Servant's life 'an offering for sin' (asham) — the Isaianic guilt-offering provides the prophetic counterpart to the Levitical type; the Servant's death as expiatory offering is the prophetic register Paul's language of 'sacrifice of atonement' also draws from."}
    ],
    "26": [
      {"type": "allusion", "target": "Isa 45:21", "note": "God declares himself 'a righteous God and a Savior; there is none but me' — Paul's climactic claim that God is both 'just and the one who justifies' (dikaion kai dikaiounta) is the Christological fulfillment of this Isaianic paradox, which posed how the one righteous God could also be a Savior; the Cross resolves the tension Isa 45:21 poses."}
    ],
    "27": [
      {"type": "theme", "target": "Jer 9:23-24", "note": "Let not the wise boast in wisdom, but let the one who boasts 'boast in this: that he understands and knows me' — Paul's 'where then is boasting? it is excluded' echoes the Jeremianic exclusion of all human-capacity boasting in favor of knowing God; Paul's point is that faith-righteousness eliminates self-achievement as the ground of standing before God."}
    ],
    "29": [
      {"type": "allusion", "target": "Deut 4:7-8", "note": "Moses asks what great nation has a god so near to them as the Lord — Paul's 'or is God the God of Jews only? Is he not the God of Gentiles too?' inverts the Deuteronomic question: the nearness-of-God privilege Israel claimed is now exposed as a privilege misread if it implies exclusivity, since the Creator is God of all."}
    ],
    "30": [
      {"type": "allusion", "target": "Deut 6:4", "note": "The Shema: 'Hear, O Israel: The Lord our God, the Lord is one' — Paul's argument that 'there is only one God' grounds the equality of Jew and Gentile before him; monotheism is not merely a theological claim but the logical basis for the universal scope of the gospel, a point Paul makes explicit that the Shema already implied."}
    ],
    "31": [
      {"type": "allusion", "target": "Ps 119:89", "note": "The law of the Lord standing firm forever — Paul's insistence that faith 'upholds' (histanomen) the law rather than nullifying it responds to the charge that grace-apart-from-law makes Torah irrelevant; the law's permanent validity is not abolished but rightly established as witness and preparatory teacher (as 3:21 already stated: 'the Law and the Prophets testify' to this righteousness)."}
    ]
  }
}

def main():
    existing = load_echo('romans')
    merge_echo(existing, ROMANS_ECHOES)
    save_echo('romans', existing)
    print('Romans 1–3 echoes written.')

if __name__ == '__main__':
    main()
