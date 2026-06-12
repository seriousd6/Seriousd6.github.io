"""
Lamentations + all 12 Minor Prophets — all four layers.
These complete the OT portion of the Z Commentary Suite.
Key NT: Hosea (son called out of Egypt; Lo-ammi/Ammi), Joel 2 (Pentecost),
        Amos (Day of the LORD, Amos 9:11 Davidic restoration),
        Jonah (sign of Jonah), Micah 5:2 (Bethlehem), Zech 9:9 (triumphal entry),
        Zech 12:10 (pierced one), Mal 3:1 (messenger), Mal 4:5 (Elijah).
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

def load_comm(layer, book):
    p = ROOT / 'data' / 'commentary' / layer / f'{book}.json'
    return json.loads(p.read_text()) if p.exists() else {}

def save_comm(layer, book, data):
    p = ROOT / 'data' / 'commentary' / layer / f'{book}.json'
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

def merge_comm(existing, new_data):
    for ch, verses in new_data.items():
        if ch not in existing:
            existing[ch] = {}
        for v, html in verses.items():
            if v not in existing[ch]:
                existing[ch][v] = html

# ============================
# LAMENTATIONS
# ============================

LAM_ECHO = {
  "3": {
    "22": [
      {"type": "allusion", "target": "Heb 13:8", "note": "The steadfast love of the LORD never ceases; his mercies never come to an end — the great confession of YHWH's faithfulness in the midst of Jerusalem's total destruction; Jesus Christ is the same yesterday and today and forever (Heb 13:8) is the new covenant form of the same confession: divine steadfast love, permanent and unending"},
      {"type": "allusion", "target": "Lam 3:26", "note": "It is good that one should wait quietly for the salvation of the LORD — the sufferer's renewed hope after total collapse; the salvation (yeshuah) that Lamentations awaits is the name of Jesus"}
    ]
  }
}

LAM_ORIGINAL = {
  "3": {
    "22": "<p><strong>chasde YHWH ki lo tamnu ki lo chalu rachamav</strong>: 'The steadfast love [<em>chesed</em>] of the LORD never ceases; his mercies [<em>rachamim</em>] never come to an end.' This confession (Lam 3:22-24) is the theological center of Lamentations — placed at the exact midpoint of the book (the acrostic structure of ch. 3 is 22×3 = 66 verses, and v. 22 is the centerpiece). Its context makes it remarkable: Lamentations is the most sustained expression of grief and lamentation in Scripture, written in the immediate aftermath of Jerusalem's destruction, yet its center is a confession of divine steadfast love. The structure embodies the theology: suffering and praise, grief and faith, can coexist — and at the center of the darkest book is the brightest confession.</p>"
  }
}

LAM_CONTEXT = {
  "1": {
    "1": "<p>Lamentations is a collection of five poems mourning the destruction of Jerusalem in 586 BCE. Four are acrostics (following the Hebrew alphabet), reflecting the artistic discipline of theological grief: the structure provides form for what might otherwise be formless pain. Traditionally attributed to Jeremiah (who is associated with Lamentations in 2 Chr 35:25 and the LXX introduction), the poems articulate Israel's grief, confession, and ongoing hope in YHWH's steadfast love. The book is read in Jewish tradition on Tisha B&rsquo;Av, the fast commemorating the temple&rsquo;s destruction. Its influence on the NT&rsquo;s passion narrative is significant: the description of Jerusalem&rsquo;s suffering (1:12: &lsquo;Is it nothing to you, all you who pass by?&rsquo;) is echoed in the passion accounts; Christ&rsquo;s passion is interpreted through the Lamentations framework of righteous suffering.</p>",
    "2": "<p>The threefold social web of <strong>allies</strong>, <strong>friends</strong>, and <strong>lovers</strong> represents the political relationships Jerusalem cultivated &mdash; Egypt, Assyria, and surrounding nations who made diplomatic treaties (<em>&rsquo;ohavim</em>, lit. &ldquo;those who love her,&rdquo; a common ancient Near Eastern treaty term for covenant partners). Egypt&rsquo;s failure to intervene when Nebuchadnezzar besieged Jerusalem is documented in Jeremiah 37:7 &mdash; Pharaoh&rsquo;s army turned back without engaging the Babylonians. The term <strong>menahem</strong> (&ldquo;comforter&rdquo;) echoes through the entire first chapter as a theological refrain: there is no human agent who can provide the consolation only YHWH can give.</p>",
    "3": "<p>The <strong>exile</strong> refers to the mass deportations of Jerusalem&rsquo;s population in 597 BCE (when the young king Jehoiachin and the elite were taken; 2 Kgs 24:14&ndash;16) and again in 586 BCE after the city fell. The language of &ldquo;finding no resting place&rdquo; (<em>lo matsa manoach</em>) echoes Deuteronomy 28:65, part of the covenant-curse catalogue predicting that Israel in exile would &ldquo;find no resting place among those nations, and the LORD will give you a trembling heart, failing eyes, and a languishing spirit.&rdquo; The exile is thus both historical catastrophe and fulfilled covenant word.</p>",
    "4": "<p>The <strong>roads to Zion mourning</strong> reflects the cessation of the three annual pilgrimage festivals (<em>mo&rsquo;adim</em>) &mdash; Passover, Weeks (Shavuot), and Tabernacles (Sukkot) &mdash; which required male Israelites to &ldquo;appear before the LORD&rdquo; in Jerusalem (Deut 16:16). The city&rsquo;s life was organized around these festival cycles; their interruption means the collapse of Israel&rsquo;s entire calendrical and liturgical world. The image of <strong>desolate gates</strong> is also archaeologically apt: city gates were the social and commercial hubs of ancient cities, bustling with trade, legal proceedings, and communal life (Ruth 4:1; Amos 5:15). Empty gates signal civic death.</p>",
    "5": "<p>The theological interpretation &mdash; <strong>the LORD afflicted her for the multitude of her transgressions</strong> &mdash; situates the disaster within Deuteronomic covenant theology (Deut 28:15&ndash;68). The enemies are not autonomous victors but instruments of divine judgment. This is the same theological framework Jeremiah himself used (Jer 25:8&ndash;9), calling Nebuchadnezzar &ldquo;my servant&rdquo; whom YHWH sent against Judah. <strong>Her children went captive before the adversary</strong> reflects the specific trauma of watching families separated during deportation &mdash; a detail corroborated by ancient Near Eastern deportation records documenting the relocation of entire communities to rebuild Babylonian infrastructure.</p>",
    "6": "<p>The image of princes as <strong>deer that find no pasture</strong> evokes exhausted animals unable to sustain themselves &mdash; an apt picture of the ruling class stripped of power, wealth, and the social networks that sustained them. The historical background is Zedekiah&rsquo;s flight from Jerusalem as it fell: &ldquo;the king went out by night by the way of the gate between the two walls&hellip; and the army fled before the Chaldeans&rdquo; (2 Kgs 25:4). Captured near Jericho, Zedekiah watched his sons executed before his own eyes were put out (2 Kgs 25:6&ndash;7) &mdash; the ultimate image of collapsing royal majesty.</p>",
    "7": "<p><strong>Precious things she once possessed in former days</strong> refers to the temple treasury, which was systematically stripped in multiple stages. In 597 BCE Nebuchadnezzar &ldquo;carried out all the treasures of the house of the LORD and the treasures of the king&rsquo;s house; he cut in pieces all the vessels of gold in the temple of the LORD&rdquo; (2 Kgs 24:13). In 586 BCE the Babylonians took the bronze pillars, the sea, and the stands that Solomon had made (2 Kgs 25:13&ndash;17). The <strong>enemy who saw her and laughed at her downfall</strong> reflects ancient Near Eastern victor&rsquo;s gloating &mdash; Babylonian royal inscriptions commonly boast of looting foreign temple goods as proof of the conqueror&rsquo;s god outranking the defeated nation&rsquo;s deity.</p>",
    "8": "<p>The term <em>niddah</em> &mdash; rendered <strong>unclean</strong> &mdash; is technically the state of ritual impurity associated with menstruation (Lev 15:19&ndash;24), the most intimate and unavoidable form of impurity in Israelite law. Applying this status to Jerusalem is a rhetorically devastating move: the holy city, which was to be a source of consecration and YHWH&rsquo;s presence, is now in a state of maximum ritual pollution. Those who once &ldquo;honored her&rdquo; &mdash; her political allies and her own citizens &mdash; have become those who despise and avoid her, just as society required separation from one who was <em>niddah</em>.</p>",
    "9": "<p><strong>Her uncleanness clung to her skirts</strong> continues the <em>niddah</em> metaphor: the impurity that should have been dealt with privately has become visible, clinging to her garments. &ldquo;She did not consider her future&rdquo; (<em>lo zakrah &rsquo;achritah</em>) is a wisdom critique &mdash; the failure of foresight that Proverbs and the prophets consistently warned against. The city&rsquo;s first-person cry &mdash; <em>re&rsquo;eh YHWH</em>, &ldquo;See, O LORD, my affliction&rdquo; &mdash; marks the shift from third-person description to direct prayer, a movement that characterizes the lament genre across the Psalter and Mesopotamian city laments alike.</p>",
    "10": "<p><strong>Nations entering the sanctuary</strong> represents the ultimate desecration. Deuteronomy 23:3 barred certain foreign peoples from &ldquo;entering the assembly of the LORD,&rdquo; and the inner courts of the temple had increasingly restricted access &mdash; the outer courts admitted Gentiles, but the inner courts required Israelite status, and the holy of holies was accessible only to the high priest once a year. The Babylonian soldiers ransacking and then burning the temple (2 Kgs 25:9; Jer 52:13) violated every boundary of sacred space simultaneously. The ANE parallel is Mesopotamian city lament literature, where the gods are described as abandoning their sanctuaries before the enemy enters &mdash; YHWH&rsquo;s departure precedes the desecration.</p>",
    "11": "<p>The <strong>search for bread</strong> reflects the documented conditions of the Babylonian siege, which lasted approximately 18 months (2 Kgs 25:1&ndash;3 records that by the fourth month of Zedekiah&rsquo;s eleventh year &ldquo;the famine was severe in the city, so that there was no food for the people of the land&rdquo;). <strong>Traded their treasures for food</strong> is a vivid collapse of value &mdash; the temple&rsquo;s gold and silver, accumulated over centuries as YHWH&rsquo;s wealth, is now exchanged for basic survival. The city&rsquo;s second direct address to YHWH &mdash; &ldquo;Look, O LORD&rdquo; &mdash; builds the pattern of appeal that reaches its fullest expression in chapter 3.</p>",
    "12": "<p><strong>Is it nothing to you, all who pass by?</strong> (<em>lo &rsquo;aleykhem kol &rsquo;ovrey derekh</em>) is one of the most-cited lines in Lamentations, appealing to passersby as witnesses to the city&rsquo;s suffering. In ancient Near Eastern mourning practice, public lamentation required witnesses; grief was performed in visible, communal ways &mdash; tearing clothes, throwing dust, professional mourners wailing at the city gates. The question appeals to that social obligation: suffering demands acknowledgment. The verse compares the city&rsquo;s sorrow to YHWH&rsquo;s own affliction of her on &ldquo;the day of his fierce anger&rdquo; &mdash; the <em>yom &rsquo;aph</em>, a phrase associated with the eschatological day of divine wrath.</p>",
    "13": "<p><strong>He sent fire into my bones</strong> and <strong>spread a net for my feet</strong> are images drawn from the arsenal of divine warrior imagery: fire as the divine weapon (as in Amos 1&ndash;2, where YHWH sends fire upon nations), and the net as divine entrapment (Ezek 12:13, where YHWH spreads his net over Zedekiah). These images position YHWH not merely as permitting the disaster but as its active agent &mdash; a theological claim far more difficult than saying &ldquo;God allowed this.&rdquo; The <strong>desolation and faintness all day long</strong> uses the same root (<em>shomemah</em>) applied to the destroyed temple and land throughout the prophets (Jer 44:6; Ezek 33:28).</p>",
    "14": "<p>The <strong>yoke of my transgressions</strong> is a deliberate echo of the yoke symbolism at the center of Jeremiah&rsquo;s conflict with the false prophet Hananiah (Jer 27&ndash;28). Jeremiah wore a wooden yoke to symbolize submission to Babylon as YHWH&rsquo;s judgment; Hananiah broke it, declaring the exile would end in two years (Jer 28:10&ndash;11). Lamentations&rsquo; yoke is woven from the city&rsquo;s own transgressions &mdash; the sins themselves become the instrument of judgment. <strong>Braided by his hand</strong> emphasizes YHWH&rsquo;s active construction of the punishment, not merely passive permission.</p>",
    "15": "<p><strong>He trampled the virgin daughter of Judah in the wine press</strong> connects to the prophetic wine-press image for divine judgment (Isa 63:3, where the divine warrior treads the winepress of his wrath; Joel 3:13). &ldquo;Virgin daughter&rdquo; (<em>betulat bat</em>) is a stock phrase for a nation or city in its prime &mdash; young, previously unviolated. The military imagery of the &ldquo;set time&rdquo; (<em>mo&rsquo;ed</em>) deliberately inverts the festival calendar: the same word used for YHWH&rsquo;s appointed feasts (v. 4) now describes an appointed time of destruction.</p>",
    "16": "<p>The third occurrence of <strong>no comforter</strong> (<em>menahem</em>) in the chapter (cf. vv. 2, 9) functions as a theological refrain making a cumulative claim: the international political order cannot provide what Jerusalem needs; only YHWH&rsquo;s restoration can serve as true comfort. The image of <strong>children desolate</strong> because &ldquo;the enemy prevailed&rdquo; gestures toward the deportation of the younger generation who represented Jerusalem&rsquo;s future.</p>",
    "17": "<p><strong>Zion stretches out her hands</strong> is the gesture of supplication &mdash; both in prayer (as in Ps 88:9; Isa 1:15) and as a signal of distress. The command attributed to YHWH &mdash; that <strong>Jacob&rsquo;s adversaries surround him</strong> &mdash; again frames the enemy assault as divinely ordered. <strong>Jerusalem has become a niddah among them</strong> returns to the ritual-impurity metaphor of vv. 8&ndash;9, now framing the city&rsquo;s political isolation as enforced separation: all neighboring peoples keep their distance, as one required distance from a menstruant.</p>",
    "18": "<p><strong>The LORD is in the right, for I rebelled against his command</strong> is one of the most theologically remarkable confessions in the Hebrew Bible: the suffering community explicitly vindicates YHWH while acknowledging its own culpability. This is the same confession Nehemiah voices in post-exilic prayer (Neh 9:33: &ldquo;You are just in all that has come upon us, for you have acted faithfully and we have done wickedly&rdquo;). The willingness to confess rather than protest the divine justice reflects the Deuteronomic theological framework that structures all five poems: the catastrophe is not divine arbitrariness but covenantal consequence.</p>",
    "19": "<p><strong>I called to my allies but they deceived me</strong> has a specific historical referent: the alliance with Egypt that Zedekiah sought when he withheld tribute from Babylon. Jeremiah 37:7 records that &ldquo;Pharaoh&rsquo;s army which came out to help you is about to return to Egypt, to its own land.&rdquo; Ezekiel 29:6&ndash;7 uses similar language of Egypt as a &ldquo;broken reed&rdquo; that pierces the hand of those who lean on it. <strong>My priests and elders perished in the city</strong> as they searched for food reflects the horror of siege conditions consuming even the religious leadership &mdash; those who should intercede before YHWH are themselves dying of starvation.</p>",
    "20": "<p><strong>My insides churn</strong> (<em>me&rsquo;ay hamaru</em>) uses visceral language for anguish &mdash; the churning of the bowels that Hebrew literature consistently associates with deep emotion (Gen 43:30; Jer 31:20). The contrast of <strong>sword outside, death inside</strong> captures the impossible situation of siege: those who venture into the streets risk the sword; those who stay inside face famine and pestilence. This double horror &mdash; plague within, sword without &mdash; is catalogued in the Deuteronomic curse (Deut 28:22) and repeatedly described by Jeremiah (Jer 14:18; 21:9).</p>",
    "21": "<p><strong>They heard my sighing; there is no one to comfort me</strong> reprises the refrain while noting that the nations are passive witnesses who rejoice rather than help. <strong>Bring on the day you announced</strong> invokes the prophetic announcements of coming judgment on Babylon (Jer 50&ndash;51; Isa 47). The &ldquo;day you announced&rdquo; is the Day of the LORD, which has a double edge: judgment for Israel first, then for the nations who served as YHWH&rsquo;s instrument.</p>",
    "22": "<p>The final verse of chapter 1 is a formal imprecatory prayer &mdash; <strong>let all their wickedness come before you</strong> &mdash; using the same standard of justice applied to Jerusalem to call for equivalent judgment on her enemies. The prayer does not ask for revenge beyond justice; it asks for theological consistency: YHWH acted against Jerusalem for its transgressions, and the enemy nations are also transgressors. This use of YHWH&rsquo;s own justice as the ground for prayer is characteristic of biblical lament (Ps 79:10&ndash;12; Jer 11:20).</p>"
  },
  "2": {
    "1": "<p>Chapter 2 is the most theologically intense of the five poems: YHWH appears as the active agent of destruction in virtually every verse, a sustained reversal of the holy-war traditions where YHWH fought <em>for</em> Israel against her enemies. The opening <em>&rsquo;ekhah</em> (&ldquo;How!&rdquo;) repeats the incipit of chapter 1, marking this as a parallel poem. <strong>The footstool of his feet</strong> refers to the ark of the covenant or the temple in Jerusalem (1 Chr 28:2; Ps 99:5; 132:7) &mdash; the physical locus of YHWH&rsquo;s presence on earth. That YHWH himself cast the &ldquo;splendor of Israel&rdquo; from heaven to earth means the divine glory has reversed its direction of movement: instead of descending to fill the temple (1 Kgs 8:11), it is hurled down in judgment.</p>",
    "2": "<p><strong>Without pity</strong> (<em>lo chamal</em>) occurs three times in chapter 2 (vv. 2, 17, 21), functioning as a dark refrain &mdash; the quality of divine mercy that Lamentations 3:22 will later celebrate as the ground of hope is conspicuously absent in the divine warrior&rsquo;s assault. The destruction of <strong>strongholds</strong> (<em>mivtsarot</em>) &mdash; fortified cities &mdash; reflects the Babylonian military strategy of systematic destruction of Judean fortifications documented in the Lachish ostraca (c. 589 BCE), letters from a Judean military officer describing the fall of outlying cities before Jerusalem.</p>",
    "3": "<p><strong>He cut off every horn of Israel</strong> &mdash; the horn (<em>qeren</em>) is a consistent symbol of strength and royal power throughout the Hebrew Bible (1 Sam 2:1; Ps 75:10). Its cutting off signals not merely military defeat but the complete erasure of Israel&rsquo;s political vitality. <strong>He withdrew his right hand</strong> in the face of the enemy: the right hand of YHWH is the instrument of salvation in exodus traditions (Exod 15:6, 12). Here YHWH deliberately pulls back the very hand that delivered Israel from Egypt, allowing the enemy to advance unopposed &mdash; the theological nightmare of holy war reversed.</p>",
    "4": "<p><strong>He bent his bow like an enemy</strong> inverts the tradition of YHWH as Israel&rsquo;s divine warrior: in Habakkuk 3:9 YHWH&rsquo;s bow is drawn against the nations; here it is drawn against the &ldquo;tent of the daughter of Zion.&rdquo; YHWH standing as <strong>adversary</strong> against his own city is as theologically provocative as any statement in the Hebrew Bible. <strong>All who were pleasing to the eye</strong> likely refers to the young men of Jerusalem &mdash; the best of the military-age population &mdash; whose deaths were most visually devastating to the city&rsquo;s sense of future.</p>",
    "5": "<p><strong>The Lord has acted like an enemy</strong> (<em>hayah YHWH ke-oyev</em>) is the theological climax of chapter 2&rsquo;s first movement &mdash; a statement that would have been nearly unthinkable in earlier Israelite theology, where YHWH&rsquo;s enmity was always directed outward at Israel&rsquo;s enemies. The Mesopotamian city lament parallels are instructive: in the &ldquo;Lament for the Destruction of Ur&rdquo; (c. 2000 BCE), the goddess Ningal pleads with the divine assembly to spare Ur but ultimately cannot prevent its destruction by divine decree. In Lamentations the theological framework is stricter: YHWH has no restraining council; he acts as sole agent of destruction because the covenant demands it.</p>",
    "6": "<p><strong>He broke down his tabernacle like a garden shelter</strong> &mdash; the word <em>sukkah</em> (garden shelter, temporary booth) deliberately evokes the Feast of Tabernacles (<em>Sukkot</em>), where Israel annually built temporary shelters as memorial of wilderness wandering. That YHWH&rsquo;s own temple-dwelling is reduced to a <em>sukkah</em> is a devastating irony: the permanent dwelling YHWH chose (1 Kgs 8:13) is destroyed to the level of the temporary. <strong>The LORD made the appointed feasts and sabbaths in Zion to be forgotten</strong> &mdash; the entire liturgical calendar is erased. Second Kings 25:9 records that the Babylonians burned the temple in the fifth month; the rabbinic tradition fixed the commemoration on the 9th of Av (Tisha B&rsquo;Av), the major fast of the Jewish calendar to this day.</p>",
    "7": "<p><strong>The Lord rejected his altar and disowned his sanctuary</strong> &mdash; YHWH has undone the act of choosing (<em>bachor</em>) that established the temple. First Kings 8 and 9 record YHWH&rsquo;s choice of Jerusalem and his warning that rejection of the covenant would mean the temple&rsquo;s destruction (1 Kgs 9:6&ndash;9). Archaeological evidence from the 586 BCE destruction layer shows widespread burning across Jerusalem&rsquo;s residential quarters; the City of David excavations have uncovered a destruction level with arrowheads, charred timbers, and the &ldquo;House of Ahiel&rdquo; abandoned in haste. <strong>They raised a shout in the house of the LORD as on a feast day</strong> &mdash; the enemy&rsquo;s victorious shout in the sanctuary is the dark inversion of Israel&rsquo;s festival worship.</p>",
    "8": "<p><strong>The LORD planned the destruction of Zion&rsquo;s wall</strong> &mdash; the verb <em>chashav</em> (planned, devised) is typically used of divine planning for salvation (Jer 29:11, &ldquo;plans for welfare&rdquo;). Here it is turned to destruction. <strong>He stretched out the measuring line</strong> (<em>qaw</em>) &mdash; the architect&rsquo;s tool, used for laying out a building&rsquo;s dimensions, is here applied to demolition. Amos 7:7&ndash;8 uses the plumb line (<em>&rsquo;anak</em>) as a measurement of judgment; Isaiah 34:11 speaks of YHWH stretching a &ldquo;line of confusion&rdquo; over Edom. The measuring line used for destruction rather than construction is a bitter architectural irony.</p>",
    "9": "<p><strong>Her gates have sunk into the ground; he shattered and broke their bars</strong> &mdash; gates were both defensive structures and the seat of civic authority (Deut 16:18; 21:19; Ruth 4:1&ndash;2); their collapse means the end of both military defense and social order. <strong>Her king and princes are among the nations; the law is no more</strong> &mdash; three simultaneous losses: the monarchy (Zedekiah captured and blinded), the legal-administrative structure (the Torah as national constitution), and prophetic guidance (&ldquo;her prophets find no vision from the LORD&rdquo;). The cessation of prophetic vision signals divine withdrawal: in the pre-exilic period, prophecy was a continuous communication channel between YHWH and Israel (Amos 3:7).</p>",
    "10": "<p><strong>The elders of Zion&rsquo;s daughter sit on the ground in silence</strong> &mdash; sitting on the ground (<em>yashvu la&rsquo;arets</em>) is the posture of extreme mourning in the ancient Near East, attested in Mesopotamian mourning texts and throughout the Hebrew Bible (Job 2:13; Isa 47:1; Ezek 26:16). <strong>Thrown dust on their heads and put on sackcloth</strong> &mdash; the dual sign of mourning: dust from the ground (returning to mortality) and sackcloth (goat-hair garment associated with penitential mourning; 1 Kgs 21:27; Joel 1:8). Both the social leadership (elders) and the young women represent the two ends of the social spectrum reduced to the same posture of grief.</p>",
    "11": "<p><strong>My eyes are spent with weeping; my insides churn</strong> &mdash; the poet shifts from third-person description (vv. 1&ndash;10) to first-person participation in the city&rsquo;s grief, mirroring the tradition of the prophets who lamented as participants (Jer 9:1; 14:17). <strong>My bile spills on the ground</strong> (<em>nishpakh la&rsquo;arets kevedi</em>) &mdash; the Hebrew <em>kaved</em> (liver) was considered in ancient Near Eastern thought the body&rsquo;s center of vitality, used in divination and associated with deep emotion. <strong>Infants and nursing babies faint in the streets</strong> &mdash; the starvation of the most vulnerable; ancient siege warfare routinely produced famine among civilians, documented in both Mesopotamian and Egyptian records of siege conditions.</p>",
    "12": "<p><strong>They cry to their mothers, &lsquo;Where is grain and wine?&rsquo;</strong> &mdash; children asking for the basics of the Israelite diet (grain for bread, wine for drink) and receiving nothing. <strong>As they collapse like the mortally wounded in the city streets</strong> &mdash; the children are dying of starvation as violently as soldiers die of wounds; the city&rsquo;s streets, which should be full of commercial and social life, are littered with the dying. <strong>Their breath ebbing away on their mothers&rsquo; bosoms</strong> &mdash; the most intimate image of helpless death: the child dying in the place of greatest security.</p>",
    "13": "<p><strong>What can I say to you? To what can I compare you?</strong> &mdash; the incomparability formula (<em>mah &rsquo;ashveh lakh</em>) is a rhetorical device affirming that the suffering exceeds all analogies. ANE royal inscriptions use incomparability formulas for praise (&ldquo;no king like you&rdquo;); Lamentations applies the same formula to suffering &mdash; Jerusalem&rsquo;s wound is as unmatched as a great king&rsquo;s glory. <strong>Your wound is as deep as the sea</strong> &mdash; the sea (<em>yam</em>) in Hebrew cosmology represents primal, immeasurable chaos (Gen 1:2; Ps 46:3). <strong>Who can heal you?</strong> &mdash; a question with only one possible answer, which Jeremiah 30:17 will provide: &ldquo;I will restore health to you, and your wounds I will heal, declares the LORD.&rdquo;</p>",
    "14": "<p><strong>Your prophets gave you empty and deceptive visions</strong> &mdash; the failure of false prophecy is a major theme in the pre-fall period. Jeremiah spent decades warning of destruction while prophets like Hananiah promised peace and a quick return of the exiles (Jer 28). <strong>They did not expose your sin to restore you</strong> &mdash; the diagnostic function of true prophecy (Mic 3:8; Isa 58:1) was to name sin in order to enable repentance; false prophets, by promising peace, removed the motivation for repentance. <strong>The oracles they proclaimed were false and misleading</strong> &mdash; the false prophets&rsquo; oracles did not merely fail but actively contributed to the city&rsquo;s destruction by preventing the confession that might have delayed judgment.</p>",
    "15": "<p><strong>All who pass by clap their hands at you</strong> &mdash; handclapping as a gesture of mockery and contempt (Job 27:23; Nah 3:19); the gesture of scorn from passersby inverts the gathering of pilgrims who once came to Jerusalem&rsquo;s festivals. <strong>They hiss and wag their heads</strong> &mdash; both gestures of derision; hissing (<em>sharaq</em>) appears in the prophetic announcements of Jerusalem&rsquo;s desolation (Jer 19:8; 49:17). <strong>&lsquo;Is this the city that was called the perfection of beauty, the joy of all the earth?&rsquo;</strong> &mdash; quoting Psalm 50:2 (&ldquo;out of Zion, the perfection of beauty, God shines forth&rdquo;) and Psalm 48:2; the mockers use Jerusalem&rsquo;s own liturgical self-description as the instrument of mockery.</p>",
    "16": "<p><strong>All your enemies open wide their mouths against you; they hiss and gnash their teeth</strong> &mdash; the gnashing of teeth (<em>charaqu shinayim</em>) is a gesture of aggressive hostility in the Psalms (Ps 35:16; 37:12). <strong>&lsquo;This is the day we waited for! We have found it, we have seen it!&rsquo;</strong> &mdash; the enemies&rsquo; triumph is experienced as the fulfillment of their longing. But the text implies a theological counter-claim: YHWH has his own &ldquo;day he announced&rdquo; (1:21) for the enemies; the enemy&rsquo;s day of triumph is not the last word in the divine calendar.</p>",
    "17": "<p><strong>The LORD has done what he planned; he fulfilled the word he decreed in days of old</strong> &mdash; this verse explicitly connects the disaster to YHWH&rsquo;s pre-announced covenantal warnings (Deut 28; Lev 26; Jer 1:14&ndash;16). The destruction is not accident or divine absence but covenant fidelity in its most terrible mode &mdash; YHWH keeping his word of judgment as faithfully as he would later keep his word of restoration. <strong>He raised the horn of your adversaries</strong> &mdash; the imagery of raised horn (strength, triumph) ironically inverts v. 3 where Israel&rsquo;s horn was cut off.</p>",
    "18": "<p><strong>Their heart cried out to the Lord; O wall of Zion&rsquo;s daughter, let tears flow like a river day and night!</strong> &mdash; an exhortation to continued lamentation addressed directly to the wall itself, a vivid personification. The <strong>night watches</strong> (<em>ashmurot</em>) refers to the three divisions of the night in ancient Israelite military practice (Exod 14:24; Judg 7:19) &mdash; weeping through every watch, without a break of sleep. The command to continuous weeping reflects sustained mourning practices: seven days of mourning for the dead (Job 2:13; cf. Deut 34:8).</p>",
    "19": "<p><strong>Arise, cry out in the night! At the start of the night watches pour out your heart like water before the Lord</strong> &mdash; the liquid metaphor for prayer &mdash; pouring out the heart as one pours water &mdash; appears in Hannah&rsquo;s prayer (1 Sam 1:15). The urgency of night prayer connects to the Psalter&rsquo;s night-cry tradition (Ps 22:2; 63:6; 77:2). <strong>Lift your hands to him for the lives of your children who faint from hunger at the head of every street</strong> &mdash; lifting hands is the classic posture of petition in ancient Near Eastern iconography and biblical prayer (Ps 28:2; 1 Kgs 8:22). The specificity of &ldquo;at the head of every street&rdquo; returns to the brutal visual of chapter 2: the city&rsquo;s children dying publicly.</p>",
    "20": "<p><strong>Should women eat the fruit of their own wombs, their newborn children?</strong> &mdash; cannibalism during siege is explicitly predicted in the Deuteronomic curse (Deut 28:53&ndash;57: &ldquo;Because of the desperate straits to which your enemy will reduce you, you will eat the fruit of your womb, the flesh of your own sons and daughters&rdquo;) and historically attested: 2 Kings 6:28&ndash;29 records two women who agreed to eat their children during the siege of Samaria. <strong>Should priest and prophet be killed in the sanctuary of the Lord?</strong> &mdash; the killing of religious officials in the sacred precinct represents the ultimate collapse of the distinction between sacred and profane.</p>",
    "21": "<p><strong>Young and old lie on the ground in the streets</strong> &mdash; both the very young and the very old killed or left to die; the total breadth of the destruction. In ancient Near Eastern warfare, killing the elderly and children signaled a policy of annihilation rather than conquest for tribute. <strong>You killed them in the day of your anger; you slaughtered without pity</strong> &mdash; the repetition of &ldquo;without pity&rdquo; (<em>lo chamal</em>, cf. vv. 2, 17) drives home the chapter&rsquo;s darkest theological claim: the divine quality most associated with Israel&rsquo;s covenant hope &mdash; compassion, the <em>rachamim</em> celebrated in Exodus 34:6 &mdash; was entirely withheld on this day.</p>",
    "22": "<p><strong>You called my terrors from every side as though summoning people to a feast day</strong> &mdash; the word for &ldquo;feast day&rdquo; is <em>mo&rsquo;ed</em>, the same term used for Israel&rsquo;s pilgrimage festivals (v. 6; cf. 1:4). YHWH summoned the Babylonian terrors with the same authority with which he summoned Israel to Passover, Weeks, and Tabernacles. <strong>On the day of the LORD&rsquo;s anger, none escaped or survived</strong> &mdash; the absolute totality of the disaster. <strong>Those I had swaddled and reared, my enemy destroyed</strong> &mdash; the final image returns to the children of vv. 19&ndash;20, now described as YHWH&rsquo;s own swaddled infants &mdash; the most intimate image of divine parental care (cf. Hos 11:1&ndash;4) &mdash; delivered to the enemy. The chapter ends at the most extreme point of theological abandonment, setting the stage for chapter 3&rsquo;s turn toward hope.</p>"
  }
}

LAM_CHRIST = {
  "1": {
    "12": "<p>A type: 'Is it nothing to you, all you who pass by? Look and see if there is any sorrow like my sorrow, which was brought upon me, which the LORD inflicted on the day of his fierce anger.' The suffering of Jerusalem — the Daughter of Zion who has suffered at YHWH's hand for her sins — is one of the OT's primary types of Christ's passion. The NT passion accounts use the Lamentations framework: the mockers who wag their heads at the crucified Jesus echo Lamentations (Lam 2:15: 'all who pass by clap their hands at you; they hiss and wag their heads at the daughter of Jerusalem'; Matt 27:39). But the typological inversion is crucial: Jerusalem suffers for her own sins; Christ suffers for ours. The language of innocent suffering that Lamentations applies to the city becomes, in the NT, applicable to the one who is truly innocent.</p>"
  },
  "3": {
    "22": "<p>A direct revelation: 'The steadfast love of the LORD never ceases; his mercies never come to an end; they are new every morning; great is your faithfulness.' This confession — the OT's most concentrated statement of divine covenantal faithfulness — is the foundation of NT assurance. Paul says 'neither death nor life ... shall be able to separate us from the love of God in Christ Jesus our Lord' (Rom 8:38-39): the love the Preacher of Lamentations confessed in the ruins of Jerusalem is the love that cannot be severed by anything. Christ's resurrection is the supreme demonstration of the <em>chesed</em> that Lamentations confesses: even through the cross — the ultimate expression of divine wrath — the steadfast love did not fail.</p>"
  }
}

# ============================
# HOSEA
# ============================

HOSEA_ECHO = {
  "1": {
    "10": [
      {"type": "fulfillment", "target": "Rom 9:25-26", "note": "And in the place where it was said to them You are not my people it shall be said to them Children of the living God — Paul cites Hos 1:10 and 2:23 as OT support for Gentile inclusion: what YHWH said about restoring estranged Israel is applied to the calling of the Gentiles into the people of God; the not-my-people becoming my-people is the inclusive dynamic of the new covenant"}
    ]
  },
  "2": {
    "23": [
      {"type": "fulfillment", "target": "1 Pet 2:10", "note": "I will say to Lo-ammi You are my people; and he shall say You are my God — Peter applies Hosea's restoration promise to the church: once you were not a people, but now you are God's people; the covenant formula's restoration (you are my people/I am your God) is fulfilled in Christ's reconciling work"}
    ]
  },
  "6": {
    "6": [
      {"type": "fulfillment", "target": "Matt 9:13", "note": "For I desire steadfast love and not sacrifice, the knowledge of God rather than burnt offerings — Jesus quotes Hos 6:6 twice (Matt 9:13; 12:7) in defense of his association with sinners and his disciples' plucking grain on the Sabbath; the priority of covenant love over ritual is Jesus's critique of Pharisaic misapplication of the law"}
    ]
  },
  "11": {
    "1": [
      {"type": "fulfillment", "target": "Matt 2:15", "note": "Out of Egypt I called my son — Matthew cites Hos 11:1 as fulfilled in the flight to Egypt and the return: as YHWH called Israel (his son) out of Egypt in the Exodus, so Jesus (the true Son) recapitulates Israel's history; Jesus is the new Israel who succeeds where Israel failed"}
    ]
  }
}

HOSEA_ORIGINAL = {
  "11": {
    "1": "<p><strong>ki naar Yisrael vaehavuhu umimitzraim qarati livni</strong>: 'When Israel was a child, I loved him, and out of Egypt I called my son.' Matthew's citation of Hos 11:1 in Matt 2:15 is one of the NT's most discussed typological uses of the OT — because Hosea 11:1 in its original context is clearly not a predictive prophecy but a historical statement about the Exodus. Matthew's method is typological recapitulation: Jesus is the new Israel, the true Son of God who goes down to Egypt and is called out again; what happened to the nation in type is fulfilled in the person of the Messiah in antitype. This reading was not arbitrary: it was grounded in the OT's identification of Israel as YHWH's 'son' (Exod 4:22-23) and the expectation that the Messiah would recapitulate and fulfill Israel's story.</p>"
  }
}

HOSEA_CONTEXT = {
  "1": {
    "1": "<p>Hosea prophesied in the northern kingdom of Israel ca. 755-725 BCE, the final decades before Assyria destroyed Samaria (722 BCE). His marriage to Gomer — a woman who proved unfaithful — is the enacted metaphor of YHWH's relationship with Israel: YHWH's faithful covenant love (hesed) in the face of Israel's persistent idolatry (harlotry). The marriage metaphor for the YHWH-Israel covenant (developed also in Jeremiah 2-3, Ezekiel 16, and Isaiah 54) is Hosea's central theological contribution: covenant violation is not merely law-breaking but adultery, a betrayal of the intimate covenant-love relationship. The NT develops the bridegroom-bride metaphor for Christ-church (Eph 5:25-32; Rev 19:7-9) directly in line with Hosea's framework.</p>"
  }
}

HOSEA_CHRIST = {
  "11": {
    "1": "<p>A type: 'Out of Egypt I called my son.' The Hosea 11:1 citation in Matthew 2:15 reveals the NT's typological method: the Exodus — YHWH calling Israel his son out of Egypt — is recapitulated in miniature by the holy family's flight to Egypt and return. Jesus is the true Son of God where Israel was the representative son; Jesus is the true Israel who succeeds where Israel repeatedly failed. The NT development of this recapitulation: Israel spent 40 years in the wilderness and failed (Num 14); Jesus spent 40 days in the wilderness and prevailed (Matt 4). Israel crossed the Jordan under Joshua and conquered imperfectly; Jesus was baptized in the Jordan and accomplished the complete conquest of sin and death. The Exodus story is not just a historical event that Jesus parallels — it is the template YHWH designed to interpret what his Son would do.</p>"
  }
}

# ============================
# JOEL
# ============================

JOEL_ECHO = {
  "2": {
    "28": [
      {"type": "fulfillment", "target": "Acts 2:16-21", "note": "I will pour out my Spirit on all flesh — Peter on the Day of Pentecost cites Joel 2:28-32 as fulfilled in the Spirit's outpouring: this is what was uttered through the prophet Joel; the universal Spirit-gift (all flesh, sons and daughters, young and old, male and female, servant and free) is the new covenant's democratization of prophetic access to God"},
      {"type": "fulfillment", "target": "Acts 2:21", "note": "And it shall come to pass that everyone who calls on the name of the LORD shall be saved — Joel's salvation promise is cited by Peter (Acts 2:21) and Paul (Rom 10:13) as the OT basis for universal gospel accessibility: the LORD whose name saves is identified with Jesus, Lord and Christ (Acts 2:36)"}
    ]
  }
}

JOEL_ORIGINAL = {
  "2": {
    "28": "<p><strong>vehaya acharei chen eshpoch et ruchi al kol basar venivve'u bneichem uvnotechem ziknechem chalomot yachalomun bachureichem cheziyonot yiru</strong>: 'And it shall come to pass afterward, that I will pour out my Spirit on all flesh; your sons and your daughters shall prophesy, your old men shall dream dreams, and your young men shall see visions.' The universal Spirit-outpouring prophesied in Joel 2:28-32 is the most significant single prophecy cited in the NT's account of Pentecost. The key phrase is <em>kol basar</em> (all flesh): unlike the selective, temporary Spirit-anointing of specific judges, prophets, and kings in the OT, the new covenant Spirit will be given to all — removing the mediatorial hierarchy that required prophets and priests to relay YHWH's word to the people. This is Jeremiah 31:34 ('no longer will each person teach his neighbor, for they will all know me') from the pneumatological angle.</p>"
  }
}

JOEL_CONTEXT = {
  "1": {
    "1": "<p>Joel is undated — no contemporary king is mentioned — but it is typically placed in the post-exilic period (late 5th-early 4th century BCE) based on its references to the temple cult and its post-exilic vocabulary. The book's structure: a devastating locust plague (chs. 1-2:11) serves as the occasion for a call to repentance (2:12-17), followed by YHWH's promise of restoration (2:18-3:21). The locust plague is both a literal agricultural disaster and the harbinger of the Day of the LORD — the pattern of divine judgment working through historical events that will culminate in the final eschatological judgment. Joel is the OT prophet most cited in the NT on the Day of Pentecost, making his prophecy of the Spirit's universal outpouring the bridge between the Old and New covenant eras.</p>"
  }
}

JOEL_CHRIST = {
  "2": {
    "32": "<p>A fulfillment: 'And it shall come to pass that everyone who calls on the name of the LORD shall be saved.' Peter (Acts 2:21) and Paul (Rom 10:13) both cite Joel 2:32 as fulfilled in the gospel proclamation: the 'name of the LORD' whose invocation brings salvation is now identified as Jesus, whom God has made both Lord and Christ (Acts 2:36). The typological identification is clear: YHWH's name in the OT = Jesus's name in the NT. This is not a revision of the OT but the NT's claim that YHWH's name and Jesus's name are the same divine identity now disclosed fully in the incarnation. The universal accessibility of salvation ('everyone who calls') removes the national and ethnic boundaries that had characterized the OT covenant community.</p>"
  }
}

# ============================
# AMOS
# ============================

AMOS_ECHO = {
  "5": {
    "18": [
      {"type": "allusion", "target": "1 Thess 5:2", "note": "Woe to you who desire the day of the LORD — Amos warns that the Day of the LORD will be darkness not light for the presumptuous; Paul says the day of the Lord comes like a thief in the night; both challenge the assumption that the Day of the LORD is automatically good news for those who consider themselves God's people"}
    ]
  },
  "9": {
    "11": [
      {"type": "fulfillment", "target": "Acts 15:16-17", "note": "I will raise up the booth of David that is fallen — James cites Amos 9:11-12 at the Jerusalem Council as the OT justification for Gentile inclusion without circumcision; the restoration of the Davidic dynasty (the fallen booth) is being fulfilled in the Messiah Jesus, and the nations seeking the LORD follows from this restoration"}
    ]
  }
}

AMOS_ORIGINAL = {
  "9": {
    "11": "<p><strong>bayom hahu aqim et sukat David hanofelet vegadarta et pirzeihen vaharisotyav aqim uvenituha keyeme olam</strong>: 'In that day I will raise up the booth of David that is fallen and repair its breaches, and raise up its ruins and rebuild it as in the days of old.' The 'fallen booth of David' is an image of the Davidic dynasty in ruins — either the northern kingdom's secession (931 BCE) or the Babylonian destruction of the Davidic throne (586 BCE). James's citation at the Jerusalem Council (Acts 15:16-17) reads the restoration as the messianic reign of Jesus: the booth is raised; now the Gentiles ('all the nations who are called by my name', v. 12 in the LXX, which differs from the MT) stream in. The LXX variant makes the Gentile-inclusion application cleaner; James uses the LXX version. This is not a mistaken quotation but a deliberate use of the LXX rendering that the Spirit has superintended to carry the intended typological meaning.</p>"
  }
}

AMOS_CONTEXT = {
  "1": {
    "1": "<p>Amos prophesied ca. 760-750 BCE in the northern kingdom under Jeroboam II, a period of remarkable prosperity and military success — and of corresponding social injustice and covenant neglect. Amos is the first of the classical writing prophets and the OT's most sustained advocate for social justice: the Day of the LORD will expose the oppression of the poor (5:11-12), the corruption of the courts (5:12), the religious hypocrisy of the sanctuaries (5:21-24: I hate, I despise your feasts ... let justice roll down like waters). His social critique is grounded in covenant theology: YHWH's covenant with Israel demands covenant justice in the community; religious observance without ethical faithfulness is an abomination.</p>"
  }
}

AMOS_CHRIST = {
  "9": {
    "11": "<p>A fulfillment: 'In that day I will raise up the booth of David that is fallen.' James's application of Amos 9:11-12 at the Jerusalem Council (Acts 15:16-17) identifies the fulfillment: the resurrection of Christ is the raising of the fallen Davidic dynasty in its ultimate form. The 'booth of David' — the Davidic covenant and its dynastic promise — lay in ruins from 586 BCE onward; no Davidic king sat on an independent throne. The risen Jesus, enthroned at the Father's right hand (Acts 2:34-36), is the restored Davidic ruler whose reign brings in the nations. The Gentile mission is therefore not a deviation from the OT prophetic program but its very fulfillment: 'the remnant of mankind and all the nations who are called by my name' (Acts 15:17, citing Amos 9:12 LXX) stream into the reestablished Davidic kingdom.</p>"
  }
}

# ============================
# OBADIAH
# ============================

OBAD_ECHO = {
  "1": {
    "4": [
      {"type": "allusion", "target": "Luke 1:52", "note": "Though you soar aloft like the eagle, though your nest is set among the stars, from there I will bring you down — YHWH's judgment of Edom's pride; Mary's Magnificat: he has brought down the mighty from their thrones; the pride-and-fall pattern of Obadiah is the structure of divine reversal that the Magnificat celebrates"}
    ],
    "15": [
      {"type": "allusion", "target": "Rev 16:19", "note": "The day of the LORD is near upon all the nations. As you have done it shall be done to you — the lex talionis principle applied to the Day of the LORD; the great city was split and the nations drank from the cup of YHWH's wrath; Obadiah's principle of nations receiving what they did to Israel reaches its ultimate form in Revelation's final judgment"}
    ]
  }
}

OBAD_ORIGINAL = {
  "1": {
    "21": "<p><strong>vealu moshim behar tziyon lishpot et har Esav vehaitah lADONAI hamelukah</strong>: 'Saviors shall go up to Mount Zion to rule Mount Esau, and the kingdom shall be the LORD's.' Obadiah's final verse is the OT's shortest prophetic book's most expansive declaration: the kingdom belongs to YHWH. Edom (the persistent enemy of Israel, descended from Esau) will be judged; the deliverers (<em>moshim</em>, saviors/deliverers) will ascend Zion; the kingdom is YHWH's alone. The NT takes the <em>moshim</em> (saviors/deliverers) as the saints who reign with Christ (Rev 20:4-6) and the kingdom as Christ's eternal reign (Rev 11:15).</p>"
  }
}

OBAD_CONTEXT = {
  "1": {
    "1": "<p>Obadiah is the shortest book in the OT (21 verses) and is addressed entirely to Edom — the nation descended from Esau, the brother of Jacob/Israel. The oracle condemns Edom for standing aloof (v. 11) or actively participating in Jerusalem's destruction (the context is almost certainly the Babylonian destruction of 586 BCE, when Edomites reportedly aided the attackers and blocked Jewish refugees, Obad 12-14). The Edom-Israel enmity runs throughout the OT from Genesis (Esau-Jacob) through Numbers (Edom refuses passage to Moses), 1 Samuel (David's wars), and the post-exilic period. Edom becomes in the Prophets a symbol for the hostile nations in general (Isa 34; Ezek 35; Mal 1:2-5), and its final judgment is the type of all anti-God hostility that will be judged on the eschatological Day of the LORD.</p>"
  }
}

OBAD_CHRIST = {
  "1": {
    "21": "<p>A shadow: 'Saviors shall go up to Mount Zion to rule Mount Esau, and the kingdom shall be the LORD's.' Obadiah's closing declaration — the kingdom belongs to YHWH — is the OT's most compact eschatological statement. The NT's fulfillment: 'The kingdom of the world has become the kingdom of our Lord and of his Christ, and he shall reign forever and ever' (Rev 11:15). The deliverers who ascend Zion are the saints who reign with Christ in the new creation (Rev 20:6: they will be priests of God and of Christ and will reign with him). Edom — the hostile brother, the nation of Esau who despised his birthright — represents all who reject the covenant birthright; their ultimate defeat is not a tribal victory for Israel but the vindication of YHWH's justice over all who oppose his reign.</p>"
  }
}

# ============================
# JONAH
# ============================

JONAH_ECHO = {
  "1": {
    "17": [
      {"type": "fulfillment", "target": "Matt 12:40", "note": "And Jonah was in the belly of the fish three days and three nights — Jesus cites this as the sign of Jonah: the Son of Man will be three days and three nights in the heart of the earth; Jonah's entombment in the fish and his emergence is the type of Jesus's death and resurrection"}
    ]
  },
  "3": {
    "5": [
      {"type": "fulfillment", "target": "Matt 12:41", "note": "The men of Nineveh repented at the preaching of Jonah, and behold something greater than Jonah is here — Jesus contrasts Nineveh's repentance at Jonah's preaching with the Jewish generation's refusal to repent at Jesus's preaching; Nineveh is a Gentile city that responded; this generation has responded to a greater preacher with less"}
    ]
  }
}

JONAH_ORIGINAL = {
  "1": {
    "17": "<p><strong>vayeman YHWH dag gadol livlo et Yonah vayehi Yonah bime'ei haddag shlosha yamim ushlosha leilot</strong>: 'And the LORD appointed a great fish to swallow up Jonah. And Jonah was in the belly of the fish three days and three nights.' The historicity of Jonah has been debated throughout church history — a man surviving inside a large sea creature is extraordinary. Jesus's citation of Jonah in Matt 12:40 takes the narrative as historical: 'just as Jonah was three days and three nights in the belly of the great fish, so will the Son of Man be three days and three nights in the heart of the earth.' If Jonah is a parable, Jesus is drawing a parable-to-reality comparison, which is unusual. The orthodox reading: both Jonah's experience and Jesus's resurrection are historical events in which the later was the greater antitype of the earlier.</p>"
  }
}

JONAH_CONTEXT = {
  "1": {
    "1": "<p>Jonah is unique among the writing prophets: instead of a prophetic oracle, it is a narrative about a prophet. Jonah ben Amittai is mentioned in 2 Kings 14:25 as a historical figure who prophesied during the reign of Jeroboam II (ca. 793-753 BCE). The book narrates his mission to Nineveh, the capital of the Assyrian Empire — Israel's most formidable enemy. His initial flight from the mission (not from fear but, the book reveals in ch. 4, from a reluctance to see Gentile enemies repent and be spared) is the book's theological problem: the prophet opposes the very grace that characterizes YHWH. The book's final question (4:11: should I not be concerned about Nineveh?) is deliberately unanswered — forcing the reader to answer it. Jesus's use of the 'sign of Jonah' (Matt 12:39-41) makes Jonah's historical experience the type of his own death and resurrection.</p>"
  }
}

JONAH_CHRIST = {
  "1": {
    "17": "<p>A type: 'Jonah was in the belly of the fish three days and three nights.' Jesus himself identifies this as the OT's appointed sign for his resurrection: 'For just as Jonah was three days and three nights in the belly of the great fish, so will the Son of Man be three days and three nights in the heart of the earth' (Matt 12:40). The typological elements: Jonah goes into the deep as a substitute (the sailors are saved from the storm by throwing Jonah overboard; 1:12-15) → Jonah is entombed in the fish → Jonah emerges to complete his mission to the Gentiles. The antitype: Christ goes to the cross as the world's substitute → Christ is entombed → Christ rises and commissions the mission to all Gentiles (Matt 28:19). Jonah's Gentile mission to Nineveh is the shadow; the apostolic mission to all nations is the substance.</p>"
  }
}

# ============================
# MICAH
# ============================

MICAH_ECHO = {
  "5": {
    "2": [
      {"type": "fulfillment", "target": "Matt 2:6", "note": "But you O Bethlehem Ephrathah who are too little to be among the clans of Judah from you shall come forth for me one who is to be ruler in Israel — the Magi and Herod's scribes cite Micah 5:2 as the birthplace of the Messiah; Matthew cites it as fulfilled in Jesus's birth at Bethlehem; the ruler whose origin is from of old, from ancient days, is the pre-existent Christ born in the city of David"}
    ]
  },
  "6": {
    "8": [
      {"type": "allusion", "target": "Matt 23:23", "note": "He has told you, O man, what is good; and what does the LORD require of you but to do justice and to love kindness and to walk humbly with your God — the ethical summary of Micah; Jesus's woe against the Pharisees who tithe mint but neglect the weightier matters of the law: justice and mercy and faithfulness (Matt 23:23); Micah 6:8 is Jesus's standard for what constitutes the law's weightier matters"}
    ]
  }
}

MICAH_ORIGINAL = {
  "5": {
    "2": "<p><strong>veatta Beit-Lechem Efrata tzair lihyot be'alfei Yehudah mimcha li yetze lihyot moshel beYisrael umotza'otav mikedem miyemei olam</strong>: 'But you, O Bethlehem Ephrathah, who are too little to be among the clans of Judah, from you shall come forth for me one who is to be ruler in Israel, whose coming forth is from of old, from ancient days.' <em>Motza'otav mikedem miyemei olam</em> (whose coming forth is from of old, from ancient days/from ancient times/from everlasting): the preposition and nouns can point to either the antiquity of the Davidic dynasty (David's line goes back to ancient Bethlehem) or to the eternal pre-existence of the coming ruler. The NT reading (John 8:58; John 1:1) takes it in the latter, stronger sense: the one born in Bethlehem has his 'goings forth' from eternity.</p>"
  }
}

MICAH_CONTEXT = {
  "1": {
    "1": "<p>Micah prophesied ca. 735-700 BCE, contemporary with Isaiah in the southern kingdom, during the Assyrian crisis that destroyed Samaria (722 BCE) and threatened Jerusalem (701 BCE). He was a rural prophet from Moresheth-Gath (a village in the Judean foothills), which gives his oracles a social-justice perspective: he speaks for the peasant farmers whose land is being seized by the powerful (2:1-2; 3:1-3). His prophecy of Jerusalem's destruction (3:12: Zion shall be plowed as a field; Jerusalem shall become a heap of ruins) was so striking that it was cited a century later as a precedent for not killing Jeremiah when he prophesied similarly (Jer 26:18-19). Micah 6:8 is the OT's most compact ethical summary and one of the most frequently cited prophetic verses.</p>"
  }
}

MICAH_CHRIST = {
  "5": {
    "2": "<p>A direct revelation: 'But you, O Bethlehem Ephrathah, who are too little to be among the clans of Judah, from you shall come forth for me one who is to be ruler in Israel, whose coming forth is from of old, from ancient days.' The theological precision of this prophecy is remarkable: (1) the specific town — Bethlehem, not Jerusalem; (2) the paradox — too small to be a clan-city, yet the birthplace of the supreme ruler; (3) the pre-existence — his 'coming forth' predates his birth in Bethlehem, reaching back to 'ancient days' (or in the stronger reading, eternity). Matthew 2:6 cites it as fulfilled with a slight adaptation that applies Micah's 'ruler' language to the one who will 'shepherd my people Israel' — combining Micah's political and pastoral imagery into the Christ who is both king and shepherd (John 10:11; Rev 7:17).</p>"
  }
}

# ============================
# NAHUM
# ============================

NAHUM_ECHO = {
  "1": {
    "15": [
      {"type": "allusion", "target": "Rom 10:15", "note": "Behold upon the mountains the feet of him who brings good news, who publishes peace — Nahum announces the fall of Nineveh as good news (the oppressor is destroyed); Isaiah 52:7 uses the same image (how beautiful upon the mountains are the feet of him who brings good news); Paul cites Isaiah in Romans 10:15 for the gospel proclamation: the good news of peace is the gospel of Christ, and the messenger's feet are the apostles'"}
    ]
  }
}

NAHUM_ORIGINAL = {
  "1": {
    "3": "<p><strong>YHWH erech apayim ugedol koach venakeh lo yenakeh YHWH besufa uvishara darko veanan afar raglav</strong>: 'The LORD is slow to anger and great in power, and the LORD will by no means clear the guilty. His way is in whirlwind and storm, and the clouds are the dust of his feet.' Nahum opens with an acrostic poem (1:2-8, partial alphabet) on the character of YHWH — combining the divine attributes of mercy and judgment that Exod 34:6-7 announced: merciful and slow to anger (Exod 34:6; Nahum 1:3a) but will not leave the guilty unpunished (Exod 34:7b; Nahum 1:3a). Jonah announced repentance and YHWH relented; Nahum announces the final judgment because Nineveh did not permanently repent. The same divine character — patient mercy but ultimate justice — is the framework for the NT: God overlooked past sins (Acts 17:30; Rom 3:25) but now commands repentance in light of the coming judgment.</p>"
  }
}

NAHUM_CONTEXT = {
  "1": {
    "1": "<p>Nahum prophesied ca. 663-612 BCE — after the fall of Thebes (663 BCE, mentioned in 3:8) and before the fall of Nineveh (612 BCE, which Nahum predicts). He is the companion prophecy to Jonah: Jonah brought Nineveh to repentance (ca. 760 BCE) and YHWH relented; Nahum announces that Nineveh's subsequent return to violence and oppression means its final destruction is now inevitable. The contrast is instructive: divine patience has a limit; the same attributes of mercy and justice that led YHWH to spare Nineveh in Jonah's day lead him to destroy it in Nahum's day. Nineveh was destroyed in 612 BCE by a coalition of Babylonians and Medes, exactly as Nahum predicted.</p>"
  }
}

NAHUM_CHRIST = {
  "1": {
    "7": "<p>A revelation of God: 'The LORD is good, a stronghold in the day of trouble; he knows those who take refuge in him.' Set in the context of Nineveh's coming destruction, this verse identifies the flip-side of divine wrath: the same YHWH who destroys his enemies is the stronghold for those who trust him. The NT's form of this double-truth: 'It is a fearful thing to fall into the hands of the living God' (Heb 10:31) for those who reject Christ; but 'There is therefore now no condemnation for those who are in Christ Jesus' (Rom 8:1) for those who are in him. The refuge (<em>maoz</em>, stronghold/fortress) that Nahum declares is the God who is also Christ: 'the name of the LORD is a strong tower; the righteous man runs into it and is safe' (Prov 18:10).</p>"
  }
}

# ============================
# HABAKKUK
# ============================

HAB_ECHO = {
  "2": {
    "4": [
      {"type": "fulfillment", "target": "Rom 1:17", "note": "The righteous shall live by his faith — Paul quotes Hab 2:4 in Romans 1:17, Galatians 3:11, and Hebrews 10:38 as the OT summary of justification by faith: the just/righteous person lives by faithfulness/faith; Paul applies it to the righteousness of God revealed in the gospel"},
      {"type": "fulfillment", "target": "Gal 3:11", "note": "It is evident that no one is justified before God by the law, for the righteous shall live by faith — Paul cites Hab 2:4 as proof that the OT already knew that justification was by faith, not law-keeping; the law (Lev 18:5: he who does them shall live by them) and the prophet (Hab 2:4: the righteous shall live by faith) are placed in contrast"}
    ]
  }
}

HAB_ORIGINAL = {
  "2": {
    "4": "<p><strong>hineh afela lo yoshra nafsho bo vetzaddik beemunato yichyeh</strong>: 'Behold, his soul is puffed up; it is not upright within him, but the righteous shall live by his faith [or faithfulness, <em>emunah</em>].' This verse is the most quoted OT text in the NT letters. The Hebrew <em>emunah</em> covers a semantic range from 'faithfulness' (reliability, steadfastness) to 'faith' (trust, belief). Paul's use in Romans and Galatians emphasizes the trust/belief aspect; the Habakkuk context emphasizes endurance and faithfulness during the Babylonian crisis. Both senses are present: the righteous person is characterized by trust in YHWH's promise that sustains them through the crisis (both the original Babylonian threat and the ongoing existential challenge of life under divine wrath deferred). The Reformers' rediscovery of this verse (Luther: the just shall live by faith, not by works of the law) was the theological engine of the Protestant Reformation.</p>"
  }
}

HAB_CONTEXT = {
  "1": {
    "1": "<p>Habakkuk's dialogue with YHWH (ca. 605-598 BCE) is the OT's most direct expression of prophetic complaint about divine justice: Why do you tolerate wrong? (1:3); Why are you silent while the wicked swallow up the more righteous? (1:13). YHWH's answer — he is raising up the Babylonians as the instrument of judgment — only deepens the question: how can a holy God use a more wicked nation to judge a less wicked one? The book's resolution is the three-chapter arc of complaint → divine response → prophetic praise (ch. 3): the righteous will live by faith in YHWH's promises even when the present situation appears to contradict those promises. The book models the theodicy of faith: not a logical resolution of the problem of evil, but a trust in the character of YHWH that sustains through crisis.</p>"
  }
}

HAB_CHRIST = {
  "2": {
    "4": "<p>A direct revelation: 'The righteous shall live by his faithfulness/faith.' This verse, quoted three times in the NT, is the OT's most concentrated statement of the principle of justification by faith. Paul reads it as the OT's own principle against works-righteousness: 'it is evident that no one is justified before God by the law, for the righteous shall live by faith' (Gal 3:11). The christological dimension: the 'righteous one' who lives by faith in its ultimate form is Jesus himself, who trusted the Father through the cross and was vindicated in the resurrection (Heb 10:38-39 applies the verse to perseverance under persecution, contextualizing it with the author's own reflection on Christ's faithfulness). The Reformation's recovery of this verse as the summary of the gospel ('the just shall live by faith') was the recovery of the Christological center of the OT's own prophetic witness.</p>"
  }
}

# ============================
# ZEPHANIAH
# ============================

ZEPH_ECHO = {
  "3": {
    "14": [
      {"type": "allusion", "target": "Luke 1:28", "note": "Sing aloud O daughter of Zion; shout O Israel! Rejoice and exult with all your heart O daughter of Jerusalem — the call to rejoice because YHWH is among you (3:17); the angel's greeting to Mary (Rejoice, highly favored one, the Lord is with you) echoes the Zephaniah joy-announcement: the presence of YHWH is the reason for rejoicing, and in the incarnation, YHWH is present in the most intimate way imaginable"},
      {"type": "allusion", "target": "John 1:14", "note": "The LORD your God is in your midst — Zeph 3:17 (the LORD is in your midst) is the OT's joyful proclamation of divine presence; John 1:14 (the Word became flesh and dwelt in our midst) is the ultimate fulfillment: YHWH's presence in the tabernacle-tent and in the midst of his people now means the incarnate Son tabernacling among humanity"}
    ]
  }
}

ZEPH_ORIGINAL = {
  "3": {
    "17": "<p><strong>YHWH eloheicha bekirbecha gibbor yoshi'a yasis alayich besimcha yacharish be'ahavato yagel alayich berinah</strong>: 'The LORD your God is in your midst, a mighty one who will save; he will rejoice over you with gladness; he will quiet you by his love; he will exult over you with loud singing.' This verse is the OT's most intimate statement of divine delight in his people: YHWH not merely tolerating but actively rejoicing over Israel, singing over her. The father-over-child image (quieting, singing) is the most tender description of YHWH's covenant love. The NT fulfillment: 'The Father himself loves you' (John 16:27); 'God is love' (1 John 4:8); 'rejoice in the Lord always' (Phil 4:4) — the joy is mutual, as Zephaniah's vision shows: YHWH singing over his people is the grounding for the people's own joy.</p>"
  }
}

ZEPH_CONTEXT = {
  "1": {
    "1": "<p>Zephaniah prophesied ca. 640-609 BCE during the reign of Josiah (640-609 BCE), before or during Josiah's reform (621 BCE). He was a member of the royal family (his genealogy goes back four generations to Hezekiah, 1:1) — one of the few prophets with clear royal connections. His primary theme is the Day of the LORD (using the phrase more than any other prophet): a comprehensive divine judgment on Judah (ch. 1), the nations (2), and Jerusalem (3:1-8), followed by the promise of a purified remnant and YHWH's presence among them (3:9-20). Zephaniah 3:14-20's closing vision of joy and restoration is one of the OT's most beautiful eschatological passages and the probable background for the angel's greeting to Mary at the Annunciation.</p>"
  }
}

ZEPH_CHRIST = {
  "3": {
    "14": "<p>A fulfillment: 'Sing aloud, O daughter of Zion; shout, O Israel! Rejoice and exult with all your heart, O daughter of Jerusalem! The LORD has taken away the judgments against you ... The King of Israel, the LORD, is in your midst; you shall never again fear evil.' This call to rejoice because YHWH is in the midst of his people reaches its fulfillment in the incarnation. Luke's Annunciation (1:28-33) and the angels' song at the Nativity (2:10-14: I bring you good news of great joy) are the NT's recasting of Zephaniah's joy-cry: rejoice, for the Lord is with you. The movement from Zephaniah to Luke is the movement from prophetic announcement to historical fulfillment: the divine King who was to come 'in your midst' comes as the infant in Bethlehem, and then the risen Lord who sends the Spirit so that YHWH is 'in the midst' of the church (Matt 18:20; John 14:23).</p>"
  }
}

# ============================
# HAGGAI
# ============================

HAG_ECHO = {
  "2": {
    "6": [
      {"type": "fulfillment", "target": "Heb 12:26-27", "note": "Yet once more, in a little while, I will shake the heavens and the earth and the sea and the dry land — Hebrews cites Haggai 2:6 as pointing to the definitive eschatological shaking: the removal of created things that are shakeable, so that only the unshakeable kingdom remains; the new creation will be established through a shaking that removes the old"}
    ],
    "9": [
      {"type": "allusion", "target": "John 2:21", "note": "The latter glory of this house shall be greater than the former — Haggai promises that the second temple will surpass Solomon's in glory; this is fulfilled not in the physical Herodian temple but in Jesus entering the temple (John 2:19-21: destroy this temple, and in three days I will raise it up; the temple was his body); the presence of Christ in the second temple makes its latter glory exceed its former"}
    ]
  }
}

HAG_ORIGINAL = {
  "2": {
    "9": "<p><strong>gadol yihyeh kevod habayit haze ha-acharon min harishon amar YHWH tzvaot uvamaqom haze etten shalom neum YHWH tzvaot</strong>: 'The latter glory of this house shall be greater than the former, says the LORD of hosts. And in this place I will give peace, declares the LORD of hosts.' Haggai's promise was puzzling to the post-exilic community: the second temple was visibly inferior to Solomon's (Ezra 3:12: the elders who had seen the first temple wept when the second was founded). The fulfillment required an unexpected reading: the greater glory came not through architectural improvement (Herod's renovation made it physically grander) but through the presence of the messianic King who entered it (Matt 21:12-17; John 2:13-22). Jesus is the glory that made the second temple greater — the Shekinah presence in person, which the first temple never contained.</p>"
  }
}

HAG_CONTEXT = {
  "1": {
    "1": "<p>Haggai prophesied in 520 BCE, the second year of Darius I of Persia — 16 years after the first returnees arrived in Jerusalem. The temple reconstruction had stalled: the returning exiles had built their own houses while the temple remained unfinished (1:4). Haggai's four oracles (1:1-11; 2:1-9; 2:10-19; 2:20-23) call the community to prioritize the temple and promise divine blessing as a result. His contemporary was Zechariah, whose visions (chs. 1-8) addressed the same restoration community. Together they provide the theological framework for the post-exilic community's task: rebuilding the worship center through which YHWH's presence among his people would be maintained until the coming of the one greater than the temple.</p>"
  }
}

HAG_CHRIST = {
  "2": {
    "7": "<p>A type: 'And I will shake all nations, so that the treasures of all nations shall come in, and I will fill this house with glory, says the LORD of hosts.' The 'treasures/desired things of all nations' (<em>chemdah</em>) coming to the temple has been read messianically (the Vulgate translates it 'veniet Desideratus cunctis gentibus', 'the one desired by all nations will come'). Whether or not this is the primary meaning, the pattern is clear: the nations streaming to the temple with their wealth is the OT vision of the eschatological gathering of all peoples to YHWH's dwelling. In the NT: the Magi (Gentile wise men) coming to the Christ-child with their treasures (Matt 2:11) is one fulfillment; the nations bringing their glory into the new Jerusalem (Rev 21:24-26) is the final fulfillment. The temple's latter glory exceeds the former because it is the glory of the incarnate Son and ultimately the new creation temple where God dwells with his people forever.</p>"
  }
}

# ============================
# ZECHARIAH
# ============================

ZECH_ECHO = {
  "9": {
    "9": [
      {"type": "fulfillment", "target": "Matt 21:5", "note": "Rejoice greatly O daughter of Zion! Shout O daughter of Jerusalem! Behold your king is coming to you; righteous and having salvation is he, humble and mounted on a donkey on a colt the foal of a donkey — Matthew and John both cite Zechariah 9:9 as fulfilled in the triumphal entry; the King of peace entering on a donkey (not a war horse) is the messianic sign"}
    ]
  },
  "11": {
    "12": [
      {"type": "fulfillment", "target": "Matt 26:15", "note": "And they weighed out as my wages thirty pieces of silver — the shepherd's wages in Zechariah 11:12 are applied to Judas's price for betraying Jesus; Matthew explicitly cites this as fulfillment (using Jeremiah's name by prophetic attribution of the scripture) in Matt 27:9-10"}
    ]
  },
  "12": {
    "10": [
      {"type": "fulfillment", "target": "John 19:37", "note": "They shall look on me whom they have pierced — Zechariah's oracle about the pierced one whom Jerusalem will mourn; John cites it at the crucifixion (they will look on the one they have pierced, John 19:37); Revelation applies it to the parousia (Rev 1:7: every eye will see him, even those who pierced him)"}
    ]
  },
  "13": {
    "7": [
      {"type": "fulfillment", "target": "Matt 26:31", "note": "Strike the shepherd, and the sheep will be scattered — Jesus quotes Zechariah 13:7 in Gethsemane as what will be fulfilled when he is arrested: strike the shepherd and the sheep of the flock will be scattered; the disciples' abandonment is the fulfillment of the Zechariah oracle about the smitten shepherd"}
    ]
  }
}

ZECH_ORIGINAL = {
  "12": {
    "10": "<p><strong>veshafachti al beit David veal yoshev Yerushalayim ruach chen vetachanunin vehibitu elai et asher daqaru vesafdu alav kemisped al hayachid vehamer alav kemispod al habechor</strong>: 'And I will pour out on the house of David and the inhabitants of Jerusalem a spirit of grace and pleas for mercy, so that, when they look on me, on him whom they have pierced, they shall mourn for him, as one mourns for an only child, and weep bitterly over him, as one weeps over a firstborn.' The grammatical anomaly is striking: 'they shall look on me [YHWH speaking] whom they have pierced' — the divine speaker identifies himself as the one pierced. The transition from 'me' to 'him' within the verse is unexplained in the OT but is resolved in the NT: YHWH and the one who was pierced are identified — the one pierced at the crucifixion is YHWH in the person of the Son.</p>"
  }
}

ZECH_CONTEXT = {
  "1": {
    "1": "<p>Zechariah prophesied ca. 520-518 BCE (chs. 1-8, with the dated oracles) and possibly into the 5th or 4th century BCE (chs. 9-14, the 'Second Zechariah', are undated and stylistically different — many scholars treat them as later additions). His eight night visions (chs. 1-6) address the post-exilic restoration community with complex symbolic imagery; his oracle-collections (chs. 7-8, 9-11, 12-14) look further into the eschatological future. Zechariah is the most extensively quoted OT book in the Gospel passion narratives — his oracles about the triumphal entry (9:9), the thirty pieces of silver (11:12-13), the smitten shepherd (13:7), the pierced one (12:10), and the cosmic mourning (12:10-14) all find explicit NT citations in the passion story. The passion narrative is Zechariah 9-14 in fulfillment.</p>"
  }
}

ZECH_CHRIST = {
  "9": {
    "9": "<p>A direct revelation: 'Rejoice greatly, O daughter of Zion! Shout aloud, O daughter of Jerusalem! Behold, your king is coming to you; righteous and having salvation is he, humble and mounted on a donkey, on a colt, the foal of a donkey.' The triumphal entry is one of the most deliberately staged Christological events in the Gospels: Jesus specifically arranges for the donkey (Luke 19:30-34), enters Jerusalem in a way that fulfills Zechariah's vision exactly, and Matthew and John both cite the fulfillment (Matt 21:5; John 12:15). The theological content of the sign: a king on a war horse signals military conquest; a king on a donkey signals peace and humility. The Messiah comes not to destroy enemies with military power but to bring salvation through the humble, peaceable means of his own sacrifice. The crowds' hosannas (Ps 118:26, 'Blessed is he who comes in the name of the LORD') are their recognition of the sign, even if they misread its implications.</p>"
  },
  "12": {
    "10": "<p>A direct revelation: 'They shall look on me, on him whom they have pierced, and they shall mourn for him, as one mourns for an only child, and weep bitterly over him, as one weeps over a firstborn.' The shift from 'me' (YHWH speaking) to 'him' (the one pierced) within the verse is the OT's most striking grammatical prolepsis of the incarnation: the one pierced is YHWH, yet YHWH speaks of him in the third person. John cites it at the crucifixion (19:37: these things took place that the Scripture might be fulfilled: they will look on him whom they have pierced), and Revelation applies it to the parousia (1:7: every eye will see him, even those who pierced him, and all tribes of the earth will wail on account of him). The mourning is both repentance (Acts 2:37: they were cut to the heart and said, Brothers, what shall we do?) and eschatological recognition (Rev 1:7: all tribes will wail).</p>"
  }
}

# ============================
# MALACHI
# ============================

MAL_ECHO = {
  "3": {
    "1": [
      {"type": "fulfillment", "target": "Matt 11:10", "note": "Behold I send my messenger and he will prepare the way before me — the messenger of the covenant is announced; Jesus quotes Malachi 3:1 (in combination with Exod 23:20) as fulfilled in John the Baptist: this is the one about whom it is written, Behold I send my messenger before your face who will prepare your way before you"},
      {"type": "fulfillment", "target": "Mark 1:2", "note": "Behold I send my messenger before your face — Mark opens his Gospel by combining Malachi 3:1 and Isaiah 40:3 as fulfilled in John the Baptist's ministry in the wilderness"}
    ]
  },
  "4": {
    "5": [
      {"type": "fulfillment", "target": "Matt 11:14", "note": "Behold I will send you Elijah the prophet before the great and awesome day of the LORD comes — Jesus identifies John the Baptist as the Elijah who was to come (Matt 11:14; 17:12): if you are willing to accept it, he is Elijah who is to come; the angel's announcement (Luke 1:17: he will go before him in the spirit and power of Elijah) grounds John's identity in Malachi's prophecy"}
    ],
    "6": [
      {"type": "allusion", "target": "Luke 1:17", "note": "He will turn the hearts of fathers to their children and the hearts of children to their fathers — the Elijah-prophecy of Malachi 4:6 is applied to John the Baptist's ministry; Luke 1:17 applies it directly: he will turn the hearts of the fathers to the children, and the disobedient to the wisdom of the just"}
    ]
  }
}

MAL_ORIGINAL = {
  "3": {
    "1": "<p><strong>hineni sholech malachi ufinah derekh lefanai ufitom yavo el heikhalov haAdon asher atem mevaksim umalach haberit asher atem chafetzim hineh ba amar YHWH tzvaot</strong>: 'Behold, I send my messenger [<em>malachi</em>], and he will prepare the way before me. And the Lord whom you seek will suddenly come to his temple; and the messenger of the covenant in whom you delight, behold, he is coming, says the LORD of hosts.' The word <em>malachi</em> means 'my messenger' — the book's title is this very word. YHWH promises two figures: the forerunner messenger (= John the Baptist) and the Lord who suddenly comes to his temple (= Jesus). The Lord's coming to his temple is the incarnation and the temple-cleansings (John 2:13-22; Mark 11:15-17). The 'messenger of the covenant' combines the forerunner and the Lord in a way that the NT separates: John is the messenger of Mal 3:1a; Jesus is the Lord of Mal 3:1b.</p>"
  },
  "4": {
    "5": "<p>The closing oracle of Malachi (4:5-6) is also the closing oracle of the OT: 'Behold, I will send you Elijah the prophet before the great and awesome day of the LORD comes. And he will turn the hearts of fathers to their children and hearts of children to their fathers, lest I come and strike the land with a decree of utter destruction.' The Hebrew canon ends here — with a promise of Elijah's return and a warning of cursing if he is rejected. The NT opens with John the Baptist filling this role (Luke 1:17; Matt 11:14; 17:10-13). The OT ends in expectation; the NT opens in fulfillment. The 400-year inter-testamental silence is the space between Malachi's promise and Matthew's fulfillment — the waiting for the forerunner who will announce the Lord's coming.</p>"
  }
}

MAL_CONTEXT = {
  "1": {
    "1": "<p>Malachi is the last book of the OT in both the Hebrew canon's traditional order and the Christian canon. It was written ca. 450-430 BCE, after the return from exile, during a period of post-exilic religious laxness. The prophet addresses: priests who offer defiled offerings (1:6-2:9), men who divorce their wives (2:14-16), the community's failure to tithe (3:10), and the skepticism of those who question YHWH's justice (3:13-15). Its six disputation speeches (each opening with a divine claim, then an objection, then YHWH's response) address the demoralization of the restored community. Malachi is the bridge between the OT and the NT: its final oracles (3:1; 4:5-6) are the OT's last prophetic words, pointing directly to John the Baptist and Jesus, so that the NT's opening (Matt 1-3; Mark 1; Luke 1-3) is the direct fulfillment of Malachi's closing.</p>"
  }
}

MAL_CHRIST = {
  "3": {
    "1": "<p>A direct revelation: 'Behold, I send my messenger, and he will prepare the way before me. And the Lord whom you seek will suddenly come to his temple.' This oracle ends the OT's prophetic program: the next thing to happen is the forerunner's preparation and the Lord's arrival. Four hundred years of prophetic silence follow — and then John the Baptist appears in the wilderness (Matt 3:1-3; Mark 1:2-4), fulfilling Malachi 3:1 (combined with Isaiah 40:3). Jesus's entry into the temple (John 2:13-22; Mark 11:15-17) is the Lord's sudden coming to his temple. The NT's opening chapters are Malachi's oracle in motion. The closing words of the OT (Mal 4:5-6) and the opening words of the NT (Matt 1:1) are not separated by 400 years of divine absence but by the divine patience that was preparing the fullness of time (Gal 4:4: when the fullness of time had come, God sent forth his Son).</p>"
  },
  "4": {
    "5": "<p>A fulfillment: 'Behold, I will send you Elijah the prophet before the great and awesome day of the LORD comes.' The OT ends with a promise; the NT opens with its fulfillment. John the Baptist comes 'in the spirit and power of Elijah' (Luke 1:17) — not literally Elijah reincarnated (John explicitly denies being Elijah, John 1:21) but fulfilling Elijah's eschatological role as the forerunner who prepares the way. Jesus confirms: 'if you are willing to accept it, he is Elijah who is to come' (Matt 11:14). The Transfiguration scene (Matt 17:3) brings the literal Elijah alongside the literal Moses alongside the literal Christ — the forerunner and the law flanking the fulfillment. Malachi's final word (the turning of fathers' and children's hearts, lest the land be struck with a curse) is the new covenant's mission: the gospel brings family reconciliation within the covenant community and protects from the ultimate curse, which Christ has absorbed (Gal 3:13).</p>"
  }
}

def main():
    books_data = [
        ('lamentations', LAM_ECHO, LAM_ORIGINAL, LAM_CONTEXT, LAM_CHRIST),
        ('hosea', HOSEA_ECHO, HOSEA_ORIGINAL, HOSEA_CONTEXT, HOSEA_CHRIST),
        ('joel', JOEL_ECHO, JOEL_ORIGINAL, JOEL_CONTEXT, JOEL_CHRIST),
        ('amos', AMOS_ECHO, AMOS_ORIGINAL, AMOS_CONTEXT, AMOS_CHRIST),
        ('obadiah', OBAD_ECHO, OBAD_ORIGINAL, OBAD_CONTEXT, OBAD_CHRIST),
        ('jonah', JONAH_ECHO, JONAH_ORIGINAL, JONAH_CONTEXT, JONAH_CHRIST),
        ('micah', MICAH_ECHO, MICAH_ORIGINAL, MICAH_CONTEXT, MICAH_CHRIST),
        ('nahum', NAHUM_ECHO, NAHUM_ORIGINAL, NAHUM_CONTEXT, NAHUM_CHRIST),
        ('habakkuk', HAB_ECHO, HAB_ORIGINAL, HAB_CONTEXT, HAB_CHRIST),
        ('zephaniah', ZEPH_ECHO, ZEPH_ORIGINAL, ZEPH_CONTEXT, ZEPH_CHRIST),
        ('haggai', HAG_ECHO, HAG_ORIGINAL, HAG_CONTEXT, HAG_CHRIST),
        ('zechariah', ZECH_ECHO, ZECH_ORIGINAL, ZECH_CONTEXT, ZECH_CHRIST),
        ('malachi', MAL_ECHO, MAL_ORIGINAL, MAL_CONTEXT, MAL_CHRIST),
    ]
    for book, echo_d, orig_d, ctx_d, chr_d in books_data:
        e = load_echo(book); merge_echo(e, echo_d); save_echo(book, e)
        c = load_comm('mkt-original', book); merge_comm(c, orig_d); save_comm('mkt-original', book, c)
        c = load_comm('mkt-context', book); merge_comm(c, ctx_d); save_comm('mkt-context', book, c)
        c = load_comm('mkt-christ', book); merge_comm(c, chr_d); save_comm('mkt-christ', book, c)
        print(f'{book}: all 4 layers written')

if __name__ == '__main__':
    main()
