"""
MKT Context — Matthew all chapters (historical/cultural background)
Output: data/commentary/mkt-context/matthew.json
One batch covering key context verses across all 28 chapters.
"""

import json, pathlib

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

DATA = {
  "1": {
    "1": '<p>Matthew\'s genealogy addresses a Jewish-Christian community likely in Syrian Antioch (ca. 80-90 CE), navigating the post-70 CE crisis in which the Temple was destroyed and Pharisaic Judaism was reconstituting itself at Jamnia. The three sections of the genealogy (Abraham to David; David to the Babylonian exile; exile to Christ) encode the three great epochs of Israel\'s story: election, kingdom, and exile awaiting restoration. Matthew presents Jesus as the one in whom Israel\'s story reaches its resolution — the community\'s claim that Jesus is the fulfillment of Jewish hope, made against the rising dominance of rabbinic Judaism that rejected this claim.</p>',
    "18": '<p>The betrothal system in first-century Jewish law created a legally binding covenant between families; unfaithfulness during betrothal was legally adultery (Deut 22:23-24). Joseph\'s plan to divorce Mary quietly (v.19) rather than publicly expose her reflects the Mishnaic debate (later codified in m. Sotah) about how to handle a wife suspected of adultery — the quiet get (certificate of divorce) vs. the public sotah-ordeal. The angel\'s intervention reframes what appeared to be a shame situation (pregnancy before cohabitation) as divine action. The entire social machinery of honor-shame culture is present in the background.</p>'
  },
  "2": {
    "1": '<p>Herod the Great (37-4 BCE) was an Idumean (Edomite) installed by Rome as client king over Judea. His reign was characterized by massive building projects (including the Temple\'s expansion) and paranoid purges of potential rivals, including members of his own family. The historical record of Herod\'s murders of his wife, mother-in-law, and sons (Josephus, Ant. 15-17) makes the Bethlehem massacre (a small village of perhaps 10-20 infant boys) entirely consistent with his character, though it goes unmentioned in Josephus — probably too small an event in the scale of Herodian atrocity to be recorded.</p>',
    "11": '<p>The Magi\'s gifts have specific cultural resonance: gold (the gift for kings, associated with tribute payments in the ancient Near East), frankincense (the incense of the temple cult, associated with priestly service), and myrrh (used for anointing and for embalming the dead). Early Christian interpretation (Origen, Contra Celsum 1.60) read the three gifts as royal, priestly, and mortal (prophesying the death) — a typological reading of the gifts as Christological symbols. The gifts also recall the tribute brought to Solomon by the queen of Sheba (1 Kgs 10:2), grounding the Magi\'s visit in the tradition of Gentile recognition of Israel\'s king.</p>'
  },
  "3": {
    "1": '<p>John the Baptist\'s wilderness ministry evokes the Qumran community\'s self-understanding: the Dead Sea Scroll community (1QS 8:14) explicitly cited Isa 40:3 (prepare the way of the LORD in the wilderness) as their charter — they withdrew to the Judean desert to prepare the way by studying Torah. John\'s baptism similarly draws on Jewish purification practices (the Qumran community\'s frequent ritual washings, the proselyte baptism for Gentile converts to Judaism) but radically applies the immersion to born Jews as a sign of repentance, treating them as if they were Gentiles needing to enter the covenant for the first time.</p>',
    "7": '<p>The Pharisees emerged as a renewal movement in Hasmonean-period Judaism (2nd century BCE), committed to applying Torah to everyday life through the oral tradition (the tradition of the elders). By the 1st century they were the most influential popular religious group in Judea, though they had no formal political power under Herod and Roman rule. The Sadducees were the priestly aristocracy who controlled the Temple and collaborated with Rome; they accepted only the written Torah and rejected resurrection, angels, and oral tradition. The tension between John/Jesus and both groups reflects the broader contest over who represented authentic Israel in the crisis of Roman occupation.</p>'
  },
  "4": {
    "1": '<p>The Judean wilderness (today\'s West Bank desert) where Jesus was tempted is a stark limestone desert with dramatic temperature swings — scorchingly hot by day, frigid at night. The forty-day fast has both Moses (Exod 34:28) and Elijah (1 Kgs 19:8) as precedents, situating Jesus in the prophetic tradition of wilderness encounter with God. The three temptations correspond to Israel\'s three great wilderness failures (bread/manna, testing God at Massah, and idolatry at the golden calf), which Jesus reverses by quoting Deuteronomy — the book of covenant renewal that summarized those failures.</p>'
  },
  "5": {
    "1": '<p>The Sermon on the Mount\'s setting (mountain, seated teacher, disciples gathered around) deliberately evokes Sinai but also the normal rabbinic teaching posture: rabbis sat to teach with authority (the cathedra, the seat of authority, from which our English word cathedral derives). The Sermon is the first of Matthew\'s five great discourses (chs. 5-7, 10, 13, 18, 24-25) — a fivefold structure that has often been seen as a parallel to the five books of Moses. The community Matthew addresses needed a coherent Torah-fulfillment that could defend its Jewish heritage against the charge of antinomianism while simultaneously distinguishing itself from Pharisaic Judaism.</p>',
    "17": '<p>The accusation that Jesus abrogated the Torah was a live controversy in Matthew\'s community. The community\'s separation from the synagogue (implied by 23:34, where synagogues are called your synagogues, implying external perspective) meant they needed a coherent account of their relationship to Jewish scripture. Matthew\'s Jesus emphatically asserts Torah-continuity (not abolition but fulfillment) while his practice (eating with sinners, Sabbath flexibility, temple-action) required explanation. The five antitheses that follow are not contrasts with the Torah but with inadequate interpretations, demonstrating Torah-intensification rather than abrogation.</p>'
  },
  "6": {
    "1": '<p>The Sermon on the Mount\'s instructions on almsgiving, prayer, and fasting (ch.6) address the three central pillars of Jewish piety. The critique of doing these things to be seen by men targets a practice that was genuinely common in Greco-Roman and Jewish civic culture: public benefactions by wealthy patrons were carved in stone and announced publicly, creating honor-capital for the donor. Synagogue donors would have their contributions acknowledged; fasting was sometimes externalized through disheveled appearance. Jesus does not reject the practices but strips them of the honor-exchange economy in which they were embedded.</p>',
    "9": '<p>The Lord\'s Prayer (Matt 6:9-13) exists in two versions (Matthew\'s liturgical version and Luke\'s shorter catechetical version, Luke 11:2-4) and was likely used as a regular prayer in Matthean communities (the Didache 8:2-3, ca. 100 CE, quotes the Matthean form and instructs prayer three times daily, in contrast to the Jewish practice of Amidah three times daily). The doxology (thine is the kingdom, the power, and the glory, forever, amen) appears in later manuscripts and the Didache — it was added liturgically. The structure reflects Jewish prayer patterns: address, petitions concerning God\'s honor, petitions for human need, final acknowledgment of dependence.</p>'
  },
  "7": {
    "28": '<p>The formula etelesen ho Iesous tous logous toutous (when Jesus had finished these words) appears at the end of each of the five Matthean discourses (7:28, 11:1, 13:53, 19:1, 26:1), structuring the Gospel as five blocks of teaching. The crowd\'s astonishment at the authority (exousia) vs. the scribes is a key social observation: the scribes taught by citation of authorities (as Rabbi X said, interpreting Rabbi Y); Jesus taught in his own name (ego de lego hymin), which was either presumptuous or authoritative depending on one\'s perspective. The crowd perceived something categorically different.</p>'
  },
  "8": {
    "5": '<p>A Roman centurion commanded approximately 80-100 soldiers (a centuria) within a cohort; the centurion at Capernaum represents the Roman military presence in Galilee. Herod Antipas\'s Galilee was not under direct Roman military command, so this centurion may have been in Herod\'s service (as a mercenary officer) rather than the Roman legions directly. His approach to Jesus — a Gentile approaching a Jewish healer with humility and faith — is presented by Matthew as the paradigm case of the Gentile inclusion that the Gospel will consummate at 28:19 (make disciples of all nations). Luke adds that he had built the local synagogue (Luke 7:5), making the irony of his humility even sharper.</p>'
  },
  "9": {
    "11": '<p>The Pharisees\' question about Jesus eating with tax collectors and sinners reflects the purity-code concerns of Second Temple Judaism. Tax collectors (telonai) collected duties for Herod or Rome and were despised for both their collaboration with the occupying power and their regular cheating (overcharging to keep the difference). They were considered as unclean as Gentiles by many Jewish groups. Sharing a meal in antiquity was not a casual social act but a declaration of covenant-solidarity; one ate with family, equals, and those one honored. The Pharisees\' objection is sociologically precise: table-fellowship with sinners communicated acceptance of their status.</p>'
  },
  "10": {
    "1": '<p>The appointment of twelve disciples mirrors the twelve tribes of Israel, presenting the renewed Israel as the nucleus of the kingdom community. In Second Temple Judaism, the number twelve had strong eschatological resonance: several Jewish restoration movements anticipated a renewed twelve-tribe Israel at the end of the age (the Qumran community had a council of twelve, 1QS 8:1). Jesus\'s appointment of twelve is a symbolic reconstitution of Israel around himself as its center — the community of the new exodus, organized as the covenant people heading toward the eschatological inheritance.</p>'
  },
  "11": {
    "2": '<p>John the Baptist in prison (Machaerus fortress, east of the Dead Sea, according to Josephus, Ant. 18.119) raises a question that reflects the hermeneutical difficulty of matching messianic expectation to actual events. The Qumran community expected two messiahs (a priestly messiah of Aaron and a royal messiah of Israel, 1QS 9:11); other Jewish traditions expected a single Davidic warrior-king who would defeat Rome and rebuild the temple. Jesus\'s answer (listing Isaianic healing signs) redirects the question from political-military categories to the prophetic-servant categories of Isaiah, redefining what messianic success looks like.</p>'
  },
  "12": {
    "1": '<p>The Sabbath controversies of ch.12 reflect real halakic disputes of first-century Judaism. The question of what constituted forbidden work on the Sabbath was the subject of extensive rabbinic debate: Mishnah Shabbat lists 39 categories of forbidden work, and gleaning was the 3rd of the 11 agricultural categories. The disciples\' plucking grain was probably permissible under Torah (Deut 23:25 allows plucking by hand in another\'s field) but was debated as a form of reaping (one of the 39) on the Sabbath. Jesus\'s appeal to David and to the priests demonstrates not Sabbath-abolition but a different hermeneutical principle: mercy and need as legitimate Sabbath criteria.</p>'
  },
  "13": {
    "1": '<p>The parable discourse (ch.13) occurs immediately after the Beelzebul controversy and the request for a sign — in the context of official rejection. The shift to parabolic teaching at this point (v.13: because seeing they do not see) is a narrative turning point: the kingdom\'s mysteries are now disclosed selectively, revealed to those who receive Jesus and concealed from those who reject him. In rabbinic tradition, parables (meshalim) were a standard teaching form for making abstract truths accessible — Ezekiel, Hosea, and Nathan used mashal-forms. But Jesus\'s parables function simultaneously as revelation (for disciples) and concealment (for hardened hearers), a dual function unprecedented in the tradition.</p>'
  },
  "14": {
    "6": '<p>Herod Antipas\'s birthday banquet (the tetrarch of Galilee, not Herod the Great\'s son Herod Agrippa) was a Hellenistic royal celebration; birthday banquets were associated in Greco-Roman culture with elaborate entertainment and gifts. The dancing girl (identified in Josephus, Ant. 18.136, as Salome, daughter of Herodias) and the rash oath (up to half my kingdom, echoing Esth 5:3) belong to the royal-court scene-setting. Josephus confirms that John was imprisoned at Machaerus and executed by Herod, though his account gives a different motivation (Herod feared John\'s political influence); Matthew emphasizes the personal vendetta of Herodias.</p>'
  },
  "15": {
    "1": '<p>The tradition of the elders (paradosis ton presbyteron) refers to the oral Torah — the Pharisaic tradition of applying written Torah to daily life through accumulated rabbinic interpretation. This tradition was later codified in the Mishnah (ca. 200 CE) and Talmud. The specific dispute about handwashing (v.2) was not a Decalogue commandment but a purity extension developed from the Levitical washings required of priests; the Pharisees extended this priestly requirement to all Jews as an expression of the priestly-people theology. Jesus disputes not Torah itself but the tradition\'s authority to override Torah (citing corban as the example where tradition nullified the fifth commandment).</p>'
  },
  "16": {
    "21": '<p>The first passion prediction (16:21) is Matthew\'s structural pivot: from here Matthew uses apo tote erxato (from that time he began) to mark the shift to the passion-oriented portion of the Gospel. The prediction names three groups (elders, chief priests, scribes) — the three constituent bodies of the Sanhedrin (the supreme Jewish council that had jurisdiction over religious law). The geography is also significant: this is Jesus\'s first explicit prediction of going to Jerusalem, which from Galilee was a deliberate journey toward the center of power that would produce the confrontation the Sanhedrin leaders feared (21:46).</p>'
  },
  "17": {
    "2": '<p>The Transfiguration\'s mountain has traditionally been identified as Mount Tabor (in Galilee) or Mount Hermon (on the northern border). The six-day interval (17:1) after Peter\'s confession echoes the six days before Moses\'s ascent of Sinai (Exod 24:16). Peter\'s suggestion to build three booths (skenai) reflects the Feast of Tabernacles (Sukkot), the festival of dwelling in booths, which in Second Temple Judaism had strong eschatological associations — the time when YHWH would dwell with his people in the messianic era. Peter instinctively reaches for the Sukkot-framework to interpret the theophanic dwelling-in-glory he is witnessing.</p>'
  },
  "18": {
    "15": '<p>The community discipline procedure of 18:15-18 (personal confrontation → two or three witnesses → community) follows a procedure similar to the Qumran community\'s discipline rules (1QS 5:25-6:1, CD 9:2-4). Both communities drew on Lev 19:17-18 (rebuke your neighbor) and Deut 19:15 (two or three witnesses). The Matthean community\'s procedure presupposes a structured assembly (ekklesia, v.17) with the authority to bind and loose — a community governance function that reflects the early church\'s development of internal discipline before and alongside synagogue structures.</p>'
  },
  "19": {
    "1": '<p>The divorce controversy (19:1-12) engages the well-known debate between the schools of Shammai and Hillel on the interpretation of Deut 24:1 (the ground for divorce: some unseemly thing, erva dabar). Shammai\'s school restricted divorce to sexual infidelity; Hillel\'s school permitted divorce for any reason (even if a wife spoiled the cooking). Matthew\'s Jesus takes a stricter position than both schools: divorce is permitted only for porneia (sexual immorality), consistent with Shammai but grounded not in Shammai\'s halakic reasoning but in the creation order (Gen 1:27, 2:24).</p>'
  },
  "20": {
    "1": '<p>The Parable of the Laborers in the Vineyard (20:1-16) is anchored in the daily wage-labor economy of first-century Galilee. Day laborers (agricultural workers without land) gathered in village marketplaces early in the morning hoping to be hired for the day; the denarius (a day\'s wage) was the survival wage for a laborer\'s family. The parable\'s surprise is not in the payment (a denarius each is generous for the latecomers) but in the employer\'s refusal to pay proportionally more to those who worked longer — the grace-logic of the kingdom reverses the labor-economy\'s logic of merit-based reward.</p>'
  },
  "21": {
    "1": '<p>The triumphal entry into Jerusalem from the Mount of Olives follows the route of Zechariah\'s eschatological scenario: the LORD stands on the Mount of Olives (Zech 14:4); the king comes to Zion (Zech 9:9). The Mount of Olives had strong messianic associations in Second Temple Judaism — Josephus (Ant. 20.169-170) mentions a Judean prophet who led followers from the Mount of Olives, expecting walls to fall at his command (Theudas; another such movement in 20.167). Jesus\'s deliberate staging of the entry — sending for the specific animal, the specific route — performs the prophetic script of Zech 9:9 before the Passover pilgrimage crowds.</p>',
    "12": '<p>The temple cleansing takes place in the Court of the Gentiles — the outer court of Herod\'s expanded temple complex where Gentiles were permitted (Jews only were allowed further in, on pain of death; the Greek inscription warning Gentiles was found in excavations and is now in the Istanbul Archaeological Museum). The money-changers and dove-sellers provided an essential service: pilgrims needed to exchange their Roman/Gentile coins (which bore idolatrous images) for the Tyrian shekel (the approved temple currency) to pay the annual half-shekel tax. Jesus\'s objection is not to the service itself but to its location in the only space designated for Gentile prayer.</p>'
  },
  "22": {
    "15": '<p>The three controversy dialogues of ch.22 (taxes to Caesar, resurrection, the great commandment) represent the three main Jewish factions confronting Jesus: the Pharisees with Herodians (political collaboration question), the Sadducees (resurrection), and a scribe/Pharisee (Torah interpretation). The Caesar question is politically lethal: Yes endorses Roman taxation and alienates Jewish nationalists; No risks arrest for sedition. The denarius Jesus asks for already answers the question: carrying Caesar\'s coin means operating within his economic system; render to each what belongs to each is a shrewd escape from the either/or trap.</p>'
  },
  "23": {
    "1": '<p>The Seven Woes of ch.23 address leaders of the synagogue system Matthew\'s community has separated from. The Pharisees\' authority is acknowledged (sit in Moses\'s seat, v.2) while their hypocrisy is indicted — a complex posture that suggests Matthew\'s community still respected Pharisaic Torah-knowledge while rejecting their leadership as exemplary. The specific practices targeted (phylacteries, tassels, titles of honor like Rabbi, Father, Teacher) are precisely the status-markers of the emerging rabbinic class. The woes function as a prophetic indictment speech, modeled on the OT prophetic woe-oracles (Isa 5:8-23, Amos 5-6).</p>'
  },
  "24": {
    "1": '<p>The Olivet Discourse (chs. 24-25) was delivered on the Mount of Olives overlooking the temple complex. The prediction of the temple\'s destruction (not one stone will be left on another, v.2) is either a genuine prophecy or (in critical readings) vaticinium ex eventu (prophecy after the fact, written after 70 CE). The temple was destroyed by Titus in August 70 CE; Josephus describes the systematic dismantling of the walls and burning of the colonnades (War 6.4-6). The discourse addresses the disciples\' conflation of Jerusalem\'s destruction with the parousia; Jesus distinguishes the two events (this generation for Jerusalem; the day and hour unknown for the parousia).</p>'
  },
  "26": {
    "3": '<p>Caiaphas (high priest ca. 18-36 CE) was the longest-serving high priest under Roman rule, which required annual reappointment by the prefect. His position depended on political maneuvering with Rome; his calculation that it is better for one man to die than for the whole nation to perish (John 11:50) reflects the political realism of a man who had survived by accommodation. The plot to arrest Jesus before Passover (v.5, not during the feast, lest there be an uproar) is historically coherent: Passover in Jerusalem brought 100,000+ pilgrims, nationalist tensions ran high, and the Roman governor (Pilate) increased his military presence from Caesarea Maritima specifically to prevent revolts.</p>',
    "17": '<p>The Last Supper is explicitly a Passover meal in Matthew, Mark, and Luke. The Passover seder in the first century was simpler than the later rabbinic seder codified in the Mishnah (m. Pesahim), but included the essential elements: the lamb slaughtered at the temple on Nisan 14, the bitter herbs, the unleavened bread, the Hallel Psalms (Ps 113-118), and four cups of wine. Jesus reinterprets the bread and the cup within this Passover framework, connecting his death to the Exodus event: as the lamb\'s blood protected Israel in Egypt, so his blood inaugurates the new covenant (Jer 31:31-34) for the forgiveness of sins.</p>'
  },
  "27": {
    "11": '<p>Pontius Pilate served as prefect of Judea (26-36 CE), the fifth Roman prefect, residing at Caesarea Maritima and coming to Jerusalem for major festivals. The Pilate Stone (discovered at Caesarea in 1961) confirms his title as prefect and his dedication of a building to Tiberius. Philo (Embassy to Gaius 301-302) and Josephus (Ant. 18.55-62, 18.85-89) describe Pilate as obstinate, corrupt, and brutal — but also politically vulnerable after the fall of his patron Sejanus in 31 CE, which may explain his reluctance to release Jesus against the Sanhedrin\'s pressure (risking another complaint to Rome).</p>'
  },
  "28": {
    "1": '<p>The resurrection appearances take place in Galilee (Matthew\'s primary location, 28:7,16) rather than Jerusalem (Luke\'s primary focus), reflecting Matthew\'s Galilean-community orientation. The Great Commission (28:18-20) is delivered on a mountain (the mountain in Galilee, v.16), continuing the Sermon on the Mount mountain-theology: the place of Torah-giving is now the place of mission-commissioning. The universal mission to all nations (panta ta ethne) is the fulfillment of the Abrahamic promise (Gen 12:3) and the Isaianic servant vision (Isa 49:6) that Matthew has traced throughout the Gospel.</p>'
  }
}

def main():
    existing = load_comm('mkt-context', 'matthew')
    merge_comm(existing, DATA)
    save_comm('mkt-context', 'matthew', existing)
    total = sum(len(v) for v in existing.values())
    print(f'Matthew mkt-context: {len(existing)} chapters, {total} verses written.')

if __name__ == '__main__':
    main()
