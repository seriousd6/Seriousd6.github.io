"""
MKT Context Commentary -- John chapters 3-4
Run: python3 scripts/zc-context-john-3-4.py

Source data used:
- data/interlinear/john.json
- data/translation/draft/mediating/john.json (MKT text)
- data/commentary/ellicott/john.json (philological and historical notes)
- data/commentary/mkt-original/john.json (terminology continuity)

Key decisions in this range:
- "the Evangelist" for the author throughout (matching mkt-original)
- "the Baptist" for John the Baptist
- Samaritan context: treated as historically grounded, not allegorical
  (five husbands = literal, not symbolic of 2 Kgs 17 nations)
- Taheb vs. Messiah: Samaritan expectation distinguished from Jewish Davidic Messiah
- sothr tou kosmou (4:42): imperial-cult resonance noted
- 3:31-36 treated as the Evangelist's commentary, not the Baptist's speech
- "Living water" dual sense: Jewish purity law + prophetic/eschatological register
- Ezek 36:25-27 as primary background for John 3:5 (over baptism or natural birth)
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
    """Merge new_data into existing without overwriting present entries."""
    for ch, verses in new_data.items():
        if ch not in existing:
            existing[ch] = {}
        for v, html in verses.items():
            if v not in existing[ch]:
                existing[ch][v] = html


JOHN = {
  "3": {
    "1": "<p>Nicodemus is introduced with two institutional markers: <strong>Pharisee</strong> and <strong>member of the Jewish ruling council</strong> (the Sanhedrin). The Pharisees were the dominant sect in late Second Temple Judaism, distinguished by strict Torah observance and adherence to the oral law (the \"tradition of the elders\"). The Sanhedrin was a 71-member body with judicial, legislative, and administrative authority -- operating under Roman oversight but retaining broad internal jurisdiction. Being both Pharisee and Sanhedrin member placed Nicodemus near the apex of Jewish institutional life, the opposite social position from the fishermen Jesus had already called.</p>",

    "2": "<p>The nocturnal visit has generated debate. Several explanations coexist: fear of peer disapproval among Sanhedrin colleagues; the rabbinic value placed on Torah study at night; or simply the desire for an extended private conversation without a crowd. In the Evangelist's narrative pattern, darkness is also a theological register -- Nicodemus comes \"in the night\" before he fully comes into the light (cf. 19:39, where he appears again at the burial, no longer hidden by night).</p><p>The \"signs\" (<em>semeia</em>) language is significant: in Second Temple expectation, authentic divine agents were recognized by wonder-works. The acknowledgment that \"God must be with him\" echoes OT language for authenticated prophets (cf. God \"with\" Moses in Exod 3:12, Joshua in Josh 1:5).</p>",

    "3": "<p>The concept of new birth would not have been entirely alien to Nicodemus. Ezekiel 36:25-27 promised that God would pour clean water on Israel and put a new spirit within them -- an eschatological transformation of the inner person. Proselyte conversion in Jewish practice was sometimes described using birth language: a Gentile who fully converted was considered \"like a newborn child,\" legally starting fresh. Nicodemus, as Israel's leading teacher (see v.10), is expected to know the Ezekiel background; his incomprehension makes the rebuke of v.10 pointed.</p>",

    "4": "<p>Nicodemus's literalistic response (re-entering the mother's womb) is an instance of the Evangelist's recurring misunderstanding pattern -- a device that exposes the gap between earthly comprehension and Jesus's meaning. The question is not absurd; Nicodemus is reasoning carefully from a physical frame. His failure is not stupidity but the limit of a perspective anchored in the natural order.</p>",

    "5": "<p>The primary OT background for \"born of water and Spirit\" is Ezekiel 36:25-27, which pairs the promise of cleansing water-sprinkling with the gift of a new spirit placed within Israel. This eschatological oracle was well known in Second Temple Judaism and was associated with the age of renewal that God would inaugurate. Some Qumran texts (1QS 4:20-21) echo the same pairing of purifying water and Spirit for the end-time community.</p><p>The rebuke in v.10 makes the Ezekiel background almost certain: a teacher of Israel who knew his Scriptures should have recognized what Jesus was describing. Water as baptism is a possible secondary resonance, but Ezekiel provides the structural fit.</p>",

    "6": "<p>The contrast between flesh and Spirit in Second Temple Judaism was not primarily a moral contrast (evil vs. holy) but an ontological one: flesh (<em>sarx</em>) marks creaturely limitation and natural origin; Spirit marks divine transformative power and heavenly origin. Nicodemus is reasoning within the category of flesh -- natural birth produces natural offspring. Jesus's point is that entry into God's kingdom requires an origin the flesh cannot provide.</p>",

    "7": "<p>The command \"you must not marvel\" addresses Nicodemus but uses the plural \"you\" -- likely extending the statement to his generation or to Israel as a whole. The use of the plural here may signal that Jesus's rebuke reaches beyond the individual Nicodemus to the broader failure of Israel's teachers to recognize what their own Scriptures promised.</p>",

    "8": "<p>The wind-Spirit double meaning of <em>pneuma</em> was available in both Greek and Hebrew (where <em>ruach</em> means both wind and Spirit). The image of divine wind as unpredictable, sovereign, and life-giving runs from Genesis 1:2 (the Spirit hovering over the waters) through Ezekiel 37 (the breath summoned to animate the valley of dry bones). The point is divine initiative: the Spirit acts where it will; humans do not command it or trace its paths. This would resonate with prophetic traditions in which the Spirit \"fell upon\" individuals unexpectedly.</p>",

    "9": "<p>Nicodemus's \"how can this be?\" is the last thing he says in this chapter. The Evangelist does not resolve his journey here; it is completed in 19:39, when Nicodemus appears with 75 pounds of myrrh and aloes to anoint Jesus's body -- a servant's act by one who has finally come into the open. The night-to-light trajectory is complete only at the burial.</p>",

    "10": "<p>The definite article in \"the teacher of Israel\" (<em>ho didaskalos tou Israel</em>) suggests Nicodemus was not merely a teacher among many but a notable or foremost one. The rebuke is proportional to his position: one so well versed in Israel's Scriptures -- including Ezekiel's new-spirit promise and Jeremiah's new covenant -- should not be mystified by the concept of spiritual new birth. The institutional insider who should understand is outrun by those with less formation.</p>",

    "11": "<p>The shift to the plural \"we speak... we testify\" is unexplained within the narrative. It may extend Jesus's testimony to include the disciples as a community of witness, or it may reflect the Evangelist's own authorial voice including himself among those who testify. The plural \"you do not accept our testimony\" widens the indictment to the Jewish leadership broadly, not only Nicodemus.</p>",

    "12": "<p>The earthly things / heavenly things distinction resonates with Jewish apocalyptic literature. 4 Ezra and 2 Baruch distinguish things of this age from those of the age to come, and distinguish earthly-accessible mysteries from those requiring heavenly revelation. The argument is a fortiori: if Jesus's earthly-register teaching (the new birth) has not been received, how will the higher register (his identity and origin) be believed?</p>",

    "13": "<p>Heavenly ascents were a recognized feature of Second Temple Jewish apocalypticism: Enoch ascends (1 Enoch 70-71), Elijah is taken up (2 Kgs 2:11), various seers receive heavenly visions (4 Ezra, 2 Baruch, the Apocalypse of Abraham). Jesus's claim cuts through this tradition: no one has actually gone up and returned as an authoritative reporter of heavenly realities except the one who descended from there. The claim is not that ascents did not happen but that only the Son of Man has the unique origin that qualifies him to speak from firsthand knowledge.</p>",

    "14": "<p>The bronze serpent episode (Num 21:4-9) was widely known and interpretively contested. When Israel was bitten by snakes in the wilderness, God commanded Moses to make a bronze serpent on a pole; those who looked at it lived. The episode troubled later interpreters: was gazing at a bronze image an act of idolatry? Hezekiah eventually destroyed it because Israel had been burning incense to it (2 Kgs 18:4). The Wisdom of Solomon (16:6-7) offered a reinterpretation: the serpent was \"a reminder of the commandment of your law\" -- it was not the object but the divine word that healed. Jesus's application redirects entirely: what the serpent-on-a-pole pointed to is the Son of Man lifted up.</p>",

    "15": "<p>\"Eternal life\" (<em>zoe aionios</em>) in Second Temple usage designated the life of the age to come -- the resurrection life of God's restored creation. It is qualitative (the kind of life that belongs to God's new age) as much as quantitative (unending). The phrase does not simply mean \"life that goes on forever\" but \"the life of the new world,\" which Jesus presents as already accessible through the Son.</p>",

    "16": "<p>The verse continues the pattern of Jewish covenant theology: God's love expressed in saving acts on behalf of his people. What is unprecedented is the extension to \"the world\" (<em>kosmos</em>) -- not merely Israel but all nations. The gift of the Son breaks the ethnic frame of the covenant while fulfilling its deepest logic: the blessing of Abraham was always to reach all nations (Gen 12:3).</p>",

    "17": "<p>Jewish expectation included divine judgment as the primary mode of God's end-time intervention -- sorting the righteous from the wicked, vindicating Israel, punishing nations. Jesus's announcement inverts the expected order: the primary mission is rescue, not condemnation. Condemnation remains real (v.18) but is not the purpose of the sending.</p><p>The \"sending\" language (<em>apesteilen</em>) evokes the Jewish <em>shaliach</em> principle: an authorized representative acts with the full authority of the one who sent him. The Father's agent acts as the Father acts.</p>",

    "18": "<p>The logic of condemnation as a pre-existing state -- not a new sentence imposed by the Son's arrival -- would resonate with Jewish covenant theology. Outside the covenant, one already stood under divine judgment; what the covenant offered was shelter. The Evangelist applies this structure to belief in the Son: the default condition is judgment; belief is the movement into life, not a work that earns it.</p>",

    "19": "<p>Light-darkness dualism was pervasive in Second Temple literature, especially at Qumran. The Community Rule (1QS) frames history as a battle between the sons of light and the sons of darkness, governed by the Spirit of truth and the spirit of deceit. The Evangelist uses similar language but shifts the moral content: the issue is not cosmic warfare between predetermined groups but the individual's response to the revelation of God in Christ. People \"prefer darkness\" because their deeds are evil -- a moral choice, not a cosmic determination.</p>",

    "20": "<p>The fear of exposure is an honor-shame dynamic: in a culture where reputation was a primary social currency, having one's deeds \"exposed\" (<em>elenchthe</em>) was a form of public shaming. Coming to the light required willingness to have one's actual life seen -- a high social cost in a world where reputation was carefully managed and public face was paramount.</p>",

    "21": "<p>\"Lives by the truth\" (<em>poion ten aletheian</em>, literally \"doing the truth\") -- the phrase appears in the Dead Sea Scrolls (1QS 1:5; 5:3) and reflects a Hebraic understanding of truth as something enacted, not merely believed. Truth in this usage is covenant fidelity expressed in action. The one who lives this way welcomes the light rather than fleeing it, because there is nothing hidden that the light will expose.</p>",

    "22": "<p>The Judean baptizing ministry (vv. 22-24) is unique to the Fourth Gospel. The Synoptics present Jesus's ministry as beginning after the Baptist's arrest; the Evangelist shows an overlap period in which both operate simultaneously in Judea. This sets up the question of v.26 (people are going to Jesus rather than the Baptist) and frames the Baptist's final testimony as a deliberate, clear-eyed act -- not a fading away.</p>",

    "23": "<p>Aenon near Salim -- the location remains debated; the name \"Aenon\" derives from the Aramaic <em>ayin</em> (spring, eye of water), suggesting a place of springs. The detail \"plenty of water\" is a practical note: immersion baptism required enough water for full-body submersion. Cisterns and pools could work, but flowing spring water was preferred both for practical reasons and because Jewish purity law valued <em>mayim chayyim</em> (living water) for ritual washing. The Baptist's site selection reflects these requirements.</p>",

    "24": "<p>The parenthetical note that the Baptist had not yet been imprisoned is the Evangelist's chronological marker, aligning this account with the Synoptic sequence without reproducing it. The arrest of John (Mark 1:14) would later trigger Jesus's withdrawal northward and the shift to Galilean ministry as the primary theater.</p>",

    "25": "<p>The \"dispute over purification\" (<em>peri katharismou</em>) points to live debates in Second Temple Judaism about which ablutions were valid, what water sources counted for ritual purity, and how the Baptist's baptism related to established Jewish practice. John's baptism was a once-for-all act of repentance; Jewish purity washings were repeated and governed by complex rules. The dispute appears to have spilled into a comparison between the Baptist's practice and Jesus's disciples' baptizing -- a rivalry the Baptist will firmly refuse.</p>",

    "26": "<p>The disciples' report frames the situation in honor-shame terms: \"everyone is going to him\" means Jesus is accumulating followers at the Baptist's expense. In a patronage society where a teacher's honor was measured by his following, this represented a competitive challenge -- at least from the disciples' perspective. Their expectation that the Baptist will be alarmed reveals their inability to grasp their teacher's self-understanding.</p>",

    "27": "<p>\"A person can receive only what is given from heaven\" echoes a strand of Jewish thought about divine sovereignty over vocation and calling. A teacher's following and role are not self-constructed achievements; they are divinely ordered. The Baptist refuses to operate within the competitive frame his disciples have imposed and relocates the question to divine assignment.</p>",

    "28": "<p>The Baptist restates his earlier testimony (cf. 1:20-23) -- \"I am not the Messiah, but I am sent ahead of him.\" In Jewish expectation shaped by Malachi 3:1 and 4:5, the Messiah's forerunner was a recognized preparatory role. The Baptist has already defined himself within this role; his disciples' alarm at Jesus's growing following misreads the Baptist's entire self-understanding.</p>",

    "29": "<p>The \"friend of the bridegroom\" (<em>shoshben</em> in Hebrew; <em>paranymph</em> in Greek) was a formal role in Jewish wedding custom. He arranged the betrothal negotiations, led the bride to the groom, stood with the groom under the wedding canopy, and received the first cup at the feast. His role was defined entirely by service to the groom -- his success was the groom's success. The bridegroom's voice was the signal of fulfillment. The Baptist maps himself precisely onto this role: his joy is complete not when he himself is celebrated but when he hears the bridegroom arrive.</p>",

    "30": "<p>This is the Baptist's last spoken word in the Gospel. The principle \"he must increase, I must decrease\" functions almost as a liturgical axiom. The narrative enacts it: from this point the Baptist recedes (imprisoned and eventually executed in the Synoptic accounts) while Jesus's ministry expands through Samaria, Galilee, and ultimately the entire world. The Baptist's self-diminishment is not resignation but the logical completion of his assigned role.</p>",

    "31": "<p>Verses 31-36 are widely regarded as the Evangelist's theological commentary rather than the Baptist's continuing speech -- the language closely parallels the Prologue (1:1-18) and the Farewell Discourse (chs. 13-17). The contrast between the one \"from above\" and the one \"from the earth\" maps Jewish cosmological categories: heavenly origin conferred supreme authority to speak about heavenly realities, a principle well established in apocalyptic tradition.</p>",

    "32": "<p>\"No one accepts his testimony\" is a rhetorical overstatement for emphasis (contrast v.26 -- \"everyone is going to him\"). The Evangelist uses this pattern elsewhere (1:11 \"his own did not receive him\") to signal the tragic pattern of rejection before noting the exceptions. The context indicates widespread non-reception among the Jewish leadership, not literal universal rejection.</p>",

    "33": "<p>\"Certified that God is truthful\" -- the verb <em>esphragisen</em> (sealed) is commercial and legal language: to seal a document was to authenticate it officially in the ancient world. Accepting Jesus's testimony is framed as a legal attestation of divine truthfulness -- a weighty act in a culture where formal witness-bearing carried serious covenantal and social weight.</p>",

    "34": "<p>\"The Spirit without limit\" draws on eschatological expectation. In OT tradition, the Spirit was given selectively and often temporarily (to prophets, judges, and kings for specific tasks). The eschatological promise was for an unlimited, universal Spirit-outpouring (Joel 2:28-29; Isa 44:3; Ezek 39:29). The Baptist received the Spirit from birth (Luke 1:15); Jesus is the one to whom the Spirit is given without measure -- and the one through whom it will be distributed to all who believe.</p>",

    "35": "<p>The Father's love for the Son and the entrusting of \"all things\" echoes royal-son language in the OT (Ps 2:7-8; 8:6; Dan 7:13-14). The Davidic king was constituted as \"Son of God\" at coronation; divine Wisdom received all things (Prov 8:22-31). These registers converge in the Evangelist's presentation of Jesus as the unique Son who inherits the full scope of divine authority.</p>",

    "36": "<p>The \"wrath of God\" (<em>orge tou theou</em>) in Jewish apocalyptic thought is not a temperamental reaction but God's settled covenantal opposition to what violates righteousness. \"Remains on them\" signals a present condition -- divine wrath is not a future sentence to be announced at judgment but the current state of those outside the shelter the Son provides. This framing places urgency on response to Jesus: the issue is decided in the present, not deferred to a future reckoning.</p>"
  },
  "4": {
    "1": "<p>The Pharisees' attention to Jesus's growing baptizing ministry signals that he is entering the radar of Jerusalem's power structures -- the same surveillance that will eventually engineer his arrest. Jesus's withdrawal is strategic, not reactive. In the Evangelist's framing, Jesus consistently acts on his own timing: he departs when his presence would trigger premature confrontation, not when others want him to.</p>",

    "2": "<p>The parenthetical clarification that Jesus himself did not baptize, only his disciples, is unique to the Fourth Gospel. It distinguishes Jesus's role from the Baptist's and may address a concern in the Evangelist's community about whether being baptized by Jesus himself conferred special status. The clarification is inserted without elaboration -- the tone suggests the Evangelist is correcting a known misunderstanding in circulation.</p>",

    "3": "<p>The departure to Galilee follows a pattern in the Gospel: Jerusalem and Judea represent confrontation with institutional authority; Galilee represents relative openness to Jesus's ministry. The movement northward also sets up the Samaritan encounter as something Jesus passes through intentionally, not as an accidental detour on the way to somewhere else.</p>",

    "4": "<p>\"He had to go through Samaria\" -- the verb <em>dei</em> (necessity) in the Fourth Gospel consistently signals theological compulsion, not mere geographic convenience. Geographically, the route through Samaria was the direct road (about 3 days' travel), while many Jews took the longer Perea route (east of the Jordan) specifically to avoid Samaritan territory. According to Josephus, Galilean pilgrims sometimes used the Samaritan route for Passover, occasionally facing harassment. The Evangelist's \"had to\" points to mission-necessity: the Samaritan encounter is not incidental but planned by divine ordering.</p>",

    "5": "<p>Sychar was located near ancient Shechem, at the entrance to the valley between Mount Ebal and Mount Gerizim. Shechem carried deep patriarchal memory: it was where Abraham built his first altar in Canaan (Gen 12:6-7), where Jacob purchased land (Gen 33:18-20), where Joseph's bones were eventually buried (Josh 24:32), and where the tribal assembly gathered under Joshua (Josh 24). The \"plot of ground Jacob gave to Joseph\" refers to the field at Shechem (Gen 48:22). For Samaritans, who traced their heritage through the Joseph tribes (Ephraim and Manasseh), this location carried the same weight of patriarchal identity that Jerusalem carried for Jews.</p>",

    "6": "<p>Jacob's well is not mentioned in the OT but is attested by unbroken tradition and archaeology (a well exists at this site today, still in use). Wells in the ancient Near East were more than water sources -- they were community gathering points where legal transactions, betrothals, and covenantal encounters took place. The Evangelist likely invokes the well-betrothal type-scene: Jacob met Rachel at a well (Gen 29:1-12), Moses met Zipporah at a well (Exod 2:15-17). In this type-scene, the well marks the beginning of a relationship with lasting significance.</p><p>The sixth hour (noon) was the hottest part of the day -- an unusual time for water-drawing, when women typically came in the cooler morning or evening, often in groups. The woman's solitary midday appearance is an early signal that her social situation is irregular.</p>",

    "7": "<p>A Jewish man addressing an unaccompanied Samaritan woman in public was a double social violation. Jewish men were expected to avoid extended public conversation with women they did not know (Pirke Avot 1:5 explicitly warns against talking much with women, \"even with your own wife\"). Stricter Pharisaic interpretation regarded Samaritan women as perpetually ritually unclean (m. Niddah 4:1), making shared vessels ritually problematic. Jesus initiates the conversation -- an act that would have been startling to any observant Jewish observer.</p>",

    "8": "<p>The disciples' absence buying food in the village is a narrative convenience that explains why Jesus is alone at the well. It also sets up the dramatic irony of their return in v.27 and their puzzlement at finding him in conversation with a woman. The purchase of food in a Samaritan village itself reflected a pragmatic engagement that more scrupulous Jews might have avoided.</p>",

    "9": "<p>The woman's surprise is socially and religiously grounded. The parenthetical \"Jews do not associate with Samaritans\" -- more precisely, \"do not use [shared] vessels\" -- reflects a specific halakhic concern that made contact with Samaritans and their belongings ritually problematic. The history of hostility between Jews and Samaritans ran deep: the Assyrian resettlement of the Northern Kingdom (2 Kgs 17), the Samaritan opposition to Ezra's rebuilding efforts (Ezra 4), and the Hasmonean destruction of the Samaritan temple on Gerizim around 128 BC all layered the antagonism. A Jewish man asking to share a Samaritan woman's vessel compounded multiple layers of social and ritual concern.</p>",

    "10": "<p>\"Living water\" (<em>hydor zon</em>) carried a technical meaning in Jewish purity law: flowing spring or river water, as opposed to collected cistern water. Jewish law required \"living water\" for certain purifications, including the mikveh. The woman hears this physical meaning and responds accordingly (v.11). In prophetic tradition, \"living water\" was also a metaphor for divine teaching and the life of the new age: Jeremiah 2:13 calls God the \"fountain of living waters\"; Zechariah 14:8 speaks of living waters flowing from Jerusalem in the eschatological age. Jesus deploys both registers simultaneously.</p>",

    "11": "<p>The woman's response is practically grounded: the well was deep (archaeological evidence confirms approximately 30 meters) and required a rope and bucket not carried by a traveling stranger. Her question \"where can you get this living water?\" is entirely reasonable given the physical situation. The Evangelist uses her practical reasoning to set up the contrast between what she understands Jesus to be offering and what he actually means.</p>",

    "12": "<p>The appeal to \"our father Jacob\" is a standard honor-challenge in patron-client idiom: the revered ancestor who gave the well is being implicitly set against this stranger who claims to offer something better. Samaritans traced their patriarchal lineage through Joseph (Ephraim and Manasseh), making Jacob genuinely \"their father.\" The implicit question -- \"are you greater than Jacob?\" -- echoes similar challenges in the Gospel (cf. 8:53, \"are you greater than our father Abraham?\") and will receive a positive answer in each case.</p>",

    "13": "<p>The well's limitation -- that its water satisfies temporarily and requires repeated return -- is not a criticism of Jacob's gift but a natural property of physical water that Jesus uses to establish the contrast. Jewish wisdom literature used similar contrasts between recurring physical need and the sustaining quality of divine instruction: \"Come, eat my food and drink the wine I have mixed\" (Prov 9:5); \"all who thirst, come to the waters\" (Isa 55:1).</p>",

    "14": "<p>\"A spring of water welling up to eternal life\" -- the image draws on the prophetic stream from Isaiah 58:11 (God will make you like a well-watered garden), Jeremiah 2:13 (God as the fountain of living waters), and Zechariah 14:8 (living waters flowing from Jerusalem in the eschatological age). Jesus locates this eschatological wellspring not in sacred geography but in himself. The verb \"welling up\" (<em>hallomenou</em>, literally leaping or bubbling up) is unusually vivid for an internal spiritual reality.</p>",

    "15": "<p>The woman's request for this water is again practical: she hears \"living spring water that quenches thirst permanently\" and wants to avoid the daily labor of drawing from a deep well. Her misunderstanding is not obtuse -- she is reasoning consistently from what Jesus has said. The Evangelist uses her literal-minded request to pivot the conversation from abstract spiritual offer to the personal exposure that will open her eyes to who Jesus actually is.</p>",

    "16": "<p>The command to call her husband shifts the conversation from abstract request to personal exposure. In a culture where a woman's social standing was mediated through male kinship (father, husband, brother), the question about her husband was simultaneously a question about her place in the social order -- and a probe into the place where her life diverged from its expected pattern.</p>",

    "17": "<p>The woman's honest answer -- \"I have no husband\" -- invites Jesus's disclosure of her fuller situation. Her candor is notable: she could have deflected with a partial truth or changed the subject. Jesus affirms her truthfulness before expanding on it -- a pattern of gracious confrontation rather than shaming accusation.</p>",

    "18": "<p>Five previous husbands and a current live-in arrangement were not automatically scandalous in the ancient world -- high mortality rates, serial widowhood, divorce, and remarriage were common. What marks the situation as irregular is the current man being \"not your husband.\" Some allegorical interpreters have read the five husbands as the five foreign peoples the Assyrians settled in Samaria (2 Kgs 17:24-34), each bringing their own gods and representing false worship. This reading imports symbolic complexity the text does not require; the primary force of the disclosure is that Jesus knows her actual history without having been told -- which is what marks him as a prophet in her eyes (v.19).</p>",

    "19": "<p>The recognition of Jesus as a prophet follows naturally from the capacity to reveal hidden things. In Second Temple expectation, authentic prophets could \"see\" what was concealed from normal perception -- this is why the testing of a prophet's claims mattered, and why false prophets were detected by failed predictions (Deut 18:21-22). The woman's perception is accurate but incomplete; prophet is not the fullest category for who Jesus is.</p>",

    "20": "<p>Mount Gerizim -- visible from the well site -- was where the Samaritans had built their temple (erected in the 5th or 4th century BC, destroyed by the Hasmonean ruler John Hyrcanus around 128 BC). The Samaritans justified Gerizim as the true worship site based on their Pentateuch, where Deuteronomy 27:4 in the Samaritan text reads \"Gerizim\" where the Hebrew MT reads \"Ebal.\" The dispute between Samaritan Gerizim-worship and Jewish Jerusalem-worship was historically bitter and still live in Jesus's day. Even without a standing temple, Samaritans continued to regard Gerizim as the sacred place. The woman's pivot to this topic may partly be a deflection from personal exposure, but it is also a genuine theological question that a prophet could answer.</p>",

    "21": "<p>Jesus's answer transcends the geographic dispute rather than adjudicating it in favor of either party. \"The Father\" as the object of worship reframes the question away from sacred mountains entirely. In Jewish theological development during the Exile, prayer and Torah study had already begun to function as substitutes for Temple worship; Jesus anticipates a more fundamental shift in which the entire sacred-geography framework becomes obsolete.</p>",

    "22": "<p>\"Salvation is from the Jews\" is an explicit acknowledgment of Israel's custodianship of the covenant, the Scriptures, and the messianic promise. The Samaritans accepted only the Pentateuch and rejected the Prophets and Writings -- thus, in Jesus's framing, they worshiped with less than the full scope of the revelation God had given. This is not ethnic triumphalism but historical-covenantal accuracy: the promise of salvation was channeled through Israel, and the Messiah comes from that covenant line.</p>",

    "23": "<p>\"In Spirit and in truth\" is not an abstraction about interior sincerity versus outward ritual. In the Evangelist's framework, it means worship enabled by the Spirit whom the Son will give (cf. 7:38-39; 14:16-17) and structured around the truth that Jesus himself embodies (14:6). The Evangelist draws on the eschatological promise of Spirit-endowment (Ezek 36:27; Joel 2:28) -- the \"true worshipers\" are those who participate in the new-age realities Jesus inaugurates, regardless of their geographic location.</p>",

    "24": "<p>\"God is Spirit\" -- not that God is a spiritual substance in a Greek metaphysical sense, but that God is not spatially confined or accessed through a particular geographic medium. The statement dismantles both Gerizim and Jerusalem as necessary locales while not denying their historical significance in salvation history. Worship \"in Spirit\" means worship empowered by the divine Spirit, not merely sincere interior intention.</p>",

    "25": "<p>The Samaritan expectation differed significantly from Jewish messianism. Samaritans accepted only the Pentateuch and did not share Jewish hopes for a Davidic warrior-king. Their expectation was for the \"Taheb\" (the Restorer, from Hebrew <em>shub</em>, \"to return\" or \"to restore\"), based primarily on Deuteronomy 18:18: a prophet like Moses who would restore true worship and interpret the law definitively. The Taheb's expected role of explaining \"everything\" matches the woman's description precisely. She uses the term \"Messiah\" (Jewish vocabulary the Evangelist's audience would recognize), but her actual expectation is closer to the Mosaic prophetic figure of her own tradition.</p>",

    "26": "<p>\"I am he\" (<em>ego eimi</em>) -- the first explicit self-disclosure as Messiah in the Gospel, and it comes not in Jerusalem to religious authorities but at a well to a Samaritan woman. The phrasing resonates with the divine self-declaration of Exodus 3:14, though in context the primary meaning is \"I am the Messiah/Taheb you are expecting.\" The disclosure to a Samaritan outsider before any formal announcement to Israel is a characteristic reversal in the Evangelist's narrative: the margins receive the revelation before the center.</p>",

    "27": "<p>The disciples' surprise at Jesus \"speaking with a woman\" reflects Rabbinic norms explicitly documented in Pirke Avot 1:5: \"Do not talk much with women. They said this even about a man's own wife; how much more so about another man's wife. Hence the sages said: He who talks much with women brings evil upon himself.\" A leading teacher who spoke publicly with a strange woman would be subject to social censure. The disciples' restraint in not questioning him shows the reverence already developing.</p>",

    "28": "<p>The abandoned water jar is a small but telling narrative detail. The woman came for water; she leaves without it because something more urgent now occupies her. The jar's abandonment signals the same displacement of ordinary priority that Jesus's calls prompted in the fishermen (who left their nets) and the tax collector (who left his booth). She becomes an ad hoc evangelist, using the same invitation Jesus used: \"come and see\" (cf. 1:39, 1:46).</p>",

    "29": "<p>The woman's testimony to the townspeople centers on prophetic knowledge -- \"he told me everything I ever did\" -- and invites them to form their own verdict through a question rather than a claim: \"Could this be the Messiah?\" This is shrewd honor-shame rhetoric: making an outright assertion that could be disputed would expose her to challenge. A question invites the community to invest in the inquiry and arrive at its own conclusion, reducing the social risk of a contested claim from a woman of irregular standing.</p>",

    "30": "<p>The movement of the Samaritans toward Jesus (\"they came out of the town and made their way toward him\") is the visible harvest that Jesus will describe in v.35 -- the fields already white. Their streaming toward him creates the visual backdrop for his teaching to the disciples about a harvest that does not wait four months.</p>",

    "31": "<p>The disciples' concern to feed Jesus (\"Rabbi, eat something\") is appropriate pastoral care but also a sign of their continued earthly-register thinking. They have returned from the village with food and expect the conversation to resume normal traveling logistics. What they walk into is a conversation about a dimension of sustenance they have not yet experienced.</p>",

    "32": "<p>\"Food you know nothing about\" -- the Evangelist's misunderstanding device again: the disciples reason horizontally (has someone brought him food while we were gone?). Jesus has been sustained through the encounter with the woman in a way that bypasses physical hunger -- not a mystical claim but a description of what it is like to do God's work with complete absorption. The mission itself is nourishment.</p>",

    "33": "<p>The disciples' question to each other (\"could someone have brought him food?\") is a brief moment of communal puzzlement. It mirrors similar moments of incomprehension throughout the Gospel (cf. 2:22; 12:16, where the disciples understand \"afterward\"). The Evangelist uses these moments to mark the gap between present perception and future clarity -- a gap that the Spirit's coming will close.</p>",

    "34": "<p>\"My food is to do the will of him who sent me\" -- the <em>shaliach</em> language again: one sent to complete a task finds sustenance in the task itself. The verb \"to finish\" (<em>teleioo</em>) is notable: it uses the same root as Jesus's final word from the cross (19:30, <em>tetelestai</em>, \"it is finished\"). The mission at the well is not a detour in the larger narrative; it is the work itself, already carrying the weight of the cross's completion.</p>",

    "35": "<p>\"Don't you have a saying, 'It's still four months until harvest'?\" -- this was likely a real seasonal proverb. The grain harvest in Samaria and Galilee (barley, then wheat) fell in April-May; if the encounter is set in late winter or early spring, the proverb would have been literally accurate. Jesus inverts the temporal logic: the spiritual harvest is not future but present. The Samaritans streaming from the village are the visible field, already ripe. The \"lifting of eyes\" to see the fields is literal and figurative simultaneously.</p>",

    "36": "<p>The wage for the reaper and the harvest gathered \"for eternal life\" places the mission in eschatological terms. In Jewish agricultural law, the reaper was entitled to wages by day's end (Deut 24:15). The image of eschatological harvest appears in Amos 9:13 (the reaper overtaken by the plowman in the new age) and Joel 3:13. The unusual feature is that sower and reaper rejoice together -- in normal agriculture they work in different seasons. The eschatological harvest collapses that temporal gap.</p>",

    "37": "<p>\"One sows and another reaps\" -- in normal agricultural life, the sower planted in autumn and the reaper harvested months later; they rarely worked side by side. The proverb appeared in Greek literature to express disparity (one person does the work, another gets the credit). Jesus deploys it positively: the spiritual harvest is the joint work of all who have sown across time -- the prophets, the Baptist, Jesus himself -- and all who now reap. The credit is shared across the whole history of witness.</p>",

    "38": "<p>\"Others have done the hard work; you have reaped the benefits of their labor\" -- the \"others\" who sowed include the OT prophets (who cultivated Israel's hope), the Baptist (who prepared the immediate audience), and Jesus himself in his Judean ministry. The disciples are entering a harvest field prepared long before them. This reverses the usual logic of labor and reward: they reap what they did not sow, which means the fruit of the mission is not primarily their achievement and cannot become grounds for pride.</p>",

    "39": "<p>The Samaritans' initial belief \"because of the woman's testimony\" is the first instance in the Gospel of faith coming through witness rather than through direct encounter or signs. The Evangelist will return to this pattern explicitly in 17:20 (\"those who will believe through their message\"). The woman becomes the first evangelist figure in the Gospel, doubly stigmatized by Jewish standards: a Samaritan and a woman with an irregular personal history.</p>",

    "40": "<p>The two-day stay responds to the Samaritans' invitation -- they \"urged him\" to remain. In John, Jesus generally controls his movements and timing (cf. 2:4; 7:6-8). The willingness here to accept Samaritan hospitality (eating their food, staying under their roofs) was itself a social statement cutting against established Jewish-Samaritan practice. Hospitality received creates bonds of mutual recognition that the normal ethnic barriers denied.</p>",

    "41": "<p>The progression from v.39 (believe because of the woman's testimony) to v.41 (believe because of his own words) is the two-stage faith-development pattern the Evangelist maps throughout: testimony opens the door; direct encounter deepens and grounds the faith on a more secure foundation. The same pattern appears in 1:40-42 (Andrew believes through John's witness, brings Peter to direct encounter).</p>",

    "42": "<p>\"Savior of the world\" (<em>soter tou kosmou</em>) -- this title was widely used in Hellenistic culture for gods (Zeus Soter, Asclepius the healer-savior) and for emperors. Augustus Caesar was hailed as <em>soter</em> in Greek inscriptions across the empire; the Roman poet Virgil's Fourth Eclogue was read in some circles as heralding a universal savior-figure. The Samaritans' acclamation of Jesus with this imperial-cult title carries deliberate subversive weight: the Savior of the world is not Caesar but this Jewish teacher who sat at a Samaritan well and offered living water.</p>",

    "43": "<p>The departure to Galilee after two days follows the pattern of Jesus moving along his own timeline. The movement northward resumes the journey that the Samaritan encounter interrupted -- though \"interrupted\" is the wrong word, since the Evangelist's <em>dei</em> (\"had to go,\" v.4) framed it as the purpose of the route, not a detour from it.</p>",

    "44": "<p>\"A prophet has no honor in his own country\" -- the saying appears in all four Gospels (Mark 6:4; Matt 13:57; Luke 4:24). In the Evangelist's placement, the saying creates a mild tension: Galilee will welcome him (v.45), which seems to contradict the proverb. The tension is part of the point: even the welcome that follows is qualified (v.45 -- they welcomed him \"because\" of Jerusalem signs, i.e., sign-based faith). The proverb prepares the reader for rejection patterns that will intensify as the Gospel proceeds toward Jerusalem.</p>",

    "45": "<p>The Galileans' welcome was sign-based -- they had seen what Jesus did in Jerusalem at Passover. This is exactly the kind of faith Jesus questions in v.48. Their welcome has a conditional, observational quality: they received him because they had seen signs. The Evangelist implicitly contrasts this with the Samaritans, who had no signs and yet believed \"because of his word\" (v.41) -- a pointed juxtaposition of two very different modes of reception.</p>",

    "46": "<p>The return to Cana, \"where he had turned the water into wine,\" explicitly recalls the first sign (2:1-11). The Evangelist numbers the signs (v.54 calls this \"the second sign\"), with Cana serving as a repeated site of revelation.</p><p>The \"royal official\" (<em>basilikos</em>) was almost certainly a Herodian functionary -- an official in the court of Herod Antipas, tetrarch of Galilee. Capernaum was a significant administrative and commercial center on the western shore of the Sea of Galilee, about 20 miles from Cana. The official's willingness to travel 20 miles and personally plead with an itinerant Galilean teacher reflects both his desperation and his perception that Jesus had power to help.</p>",

    "47": "<p>The official \"begged\" Jesus -- the verb <em>parekalei</em> is imperfect, indicating persistent, repeated pleading. The social inversion is deliberate: a man of official status in Herod's court approaches Jesus as a suppliant. In honor-shame terms, this required setting aside the dignity his office conferred. Parental desperation overrides social calculation.</p>",

    "48": "<p>\"Unless you see signs and wonders\" (<em>semeia kai terata</em>) -- the pairing is the standard OT phrase for Exodus miracles (Deut 4:34; 6:22; Ps 78:43) and carries prophetic resonance. Paul notes in 1 Corinthians 1:22 that \"Jews demand signs and Greeks seek wisdom.\" Jesus's rebuke challenges faith conditioned on spectacular proof -- a pattern he encountered in Jerusalem (2:23-25) and will continue to address. The plural \"you\" extends the critique beyond the official to his generation. His response in v.50 (believing on Jesus's word alone and departing) is the faith Jesus is looking for.</p>",

    "49": "<p>\"Come down before my child dies\" -- the official is not deterred by the rebuke; his desperation bypasses pride. The diminutive \"child\" (<em>paidion</em>, my little child) humanizes the official beyond his institutional role. The Evangelist keeps the story relational and personal even while making large theological points about the nature of faith.</p>",

    "50": "<p>Jesus's response is simply \"Go, your son will live\" -- no physical presence, no touch, no dramatic sign-performance. The healing is accomplished at a distance by word alone. The official \"believed the word Jesus spoke\" and departed without verification. This is the faith Jesus had just called for in v.48: trust in the word before any confirming sign. The structural irony is immediate: the man challenged about sign-demanding faith provides the example of word-trusting faith within the same encounter.</p>",

    "51": "<p>Servants meeting the official on the road with news of recovery recalls similar patterns in OT narrative -- messengers bringing news that reframes a traveler's situation (cf. the runners reporting to David in 2 Sam 18). The detail that they met him while he was \"still on the way\" -- before he could reach Capernaum to verify personally -- confirms that he traveled on trust, not on sight.</p>",

    "52": "<p>The inquiry about the precise hour of recovery is a verification step -- not disbelief but the responsible confirmation of a remarkable claim. \"Yesterday at one in the afternoon\" (the seventh hour) corresponds exactly to the moment Jesus spoke (the text implies the sixth-to-seventh hour). The precision of the match -- not \"around the same time\" but the exact hour -- is the Evangelist's way of marking the event as unmistakably coordinated, not coincidental.</p>",

    "53": "<p>The father's retrospective recognition (\"he realized this was the exact time\") triggers full household faith. The detail that \"he and his whole household believed\" echoes a pattern significant in early Christian mission literature: household conversions in Acts (Cornelius's household, Lydia's household, the Philippian jailer's household) reflect the ancient world's organization around household units. The head of household's decision typically shaped the entire domestic community's practice and commitments.</p>",

    "54": "<p>The \"second sign\" notation counts from the first Cana sign (water to wine, 2:11), establishing a deliberate numerical sequence. Cana thus brackets a unit: the first sign opened the disciples' faith; the second comes at the same location and deepens the pattern. The numbering suggests the Evangelist is working with a structured tradition of signs, deliberately arranged to mark each one as part of cumulative, purposeful revelation -- not miracle for its own sake but disclosure of who Jesus is.</p>"
  }
}


def main():
    existing = load_comm('mkt-context', 'john')
    merge_comm(existing, JOHN)
    save_comm('mkt-context', 'john', existing)
    print('John 3-4 mkt-context written.')

if __name__ == '__main__':
    main()
