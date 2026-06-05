"""
MKT Christ Commentary — John chapters 1–2
Run: python3 scripts/zc-christ-john-1-2.py

Source data used:
- data/interlinear/john.json
- data/translation/glossary-greek.json (λόγος, μονογενής, ἀμνός, σάρξ)
- data/translation/notes/john.json
- data/translation/draft/mediating/john.json (MKT text for quoting)
- data/echoes/john.json (echoes already established for ch 1–2)
- data/commentary/mkt-original/john.json (terminology: "the Evangelist")
- data/commentary/mkt-context/john.json (terminology carried forward)

Key decisions in this range:
- "The Evangelist" consistently used (matching mkt-original register)
- Directness levels stated in prose even when not using the exact term
- John 1:1–18 (the Prologue) treated as the densest Christological unit in the NT
- John 1:6–8 / 19–28 (Baptist passages): each verse gets an entry even where
  Christological content is indirect — they function as negative definition
- John 2:1–11 (Cana): the sign reveals glory (v11); each verse reads in light of that
- John 2:13–22 (Temple cleansing): body-as-temple is the explicit interpretive key (v21)
- "Hour" language (2:4) treated as pointing forward to the passion/glorification,
  consistent with how the Evangelist uses it across the Gospel
- Nathanael's twin acclamation (1:49) — both titles treated; Son of God = Ps 2:7
  royal-divine, King of Israel = Davidic-messianic
- 1:51 (Jacob's ladder) treated as a type: Son of Man = new Bethel
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
  "1": {
    "1": '<p>The most direct Christological claim in the NT: the Word who "was God" and who "was with God" is not a creature or an emanation but the divine Son in eternal existence before all created things. The Evangelist does not begin with Jesus\' birth or ministry but with what precedes it by eternity — establishing that the one who becomes flesh in v14 is the one through whom all things were made and who shares the divine nature fully.</p>',

    "2": '<p>The compressed restatement anchors the distinction: there is one God, and the Word is with him — not identical in a collapsing sense, not separate in a divided sense. This distinction between Father and Son is the foundation on which the Incarnation is intelligible: the one who is "with God" can be sent into the world precisely because he is distinct from the Father while sharing the divine nature.</p>',

    "3": '<p>A revelation of God: the one who becomes flesh in v14 is the agent of creation of every existing thing. Paul makes the same claim (Col 1:16), as does the author of Hebrews (Heb 1:2). The Christological weight is enormous — the carpenter from Nazareth is the one through whom every atom came into existence. No gap exists between Creator and Redeemer.</p>',

    "4": '<p>Life and light are not abstract qualities here; they are names the Evangelist will unfold as Christ\'s own self-designations: "I am the light of the world" (8:12; 9:5), "I am the resurrection and the life" (11:25), "I am the way, the truth, and the life" (14:6). The Prologue establishes in principle what the Gospel narratives demonstrate in event: these realities exist in Christ and nowhere else.</p>',

    "5": '<p>The present tense "shines" — not "shone" — asserts that the light is still active. The darkness\'s failure to overcome it is the Prologue\'s anticipation of the cross: darkness appeared to have the final word on Good Friday, but the resurrection proved it could not. This is a shadow of Christ\'s death and resurrection — the cosmic conflict between light and dark resolved by the one who embodies the light.</p>',

    "6": '<p>John the Baptist enters as a sent witness, not the Light himself. The Christological function of this verse is definitional by contrast: the one who is "not the Light" is being contrasted with the one who is. Every attribute withheld from John in vv6–8 belongs to Christ alone — he is the origin, the Light, the one to whom witness is borne, not the one who bears it.</p>',

    "7": '<p>John\'s entire ministry is oriented toward Christ — witness, testimony, belief "through him." The Evangelist structures the Baptist passages to point the reader\'s attention away from John and toward Christ at every turn. The purpose clause ("so that through him all might believe") makes the soteriological goal explicit: Christ, not John, is the object of saving faith.</p>',

    "8": '<p>The explicit denial — "he was not the Light" — is a Christological protection. The Fourth Gospel is alert to any confusion between the forerunner and the one he announces. Christ alone is the true Light; John is the lamp that points to it. The theme is revelation of God: only the Son, not any human agent however anointed, is the source of divine illumination.</p>',

    "9": '<p>The "true Light" (<em>alēthinós</em>) — not false but the original, the reality of which all other lights are shadows. The universal scope ("every man") anticipates the mission to the nations that the Evangelist traces through the Gospel: Greeks come seeking Jesus (12:20–21); the Samaritan woman receives him (ch. 4); the world itself is the scope of the Father\'s sending (3:16). Christ is the light that no ethnicity, culture, or era has lacked access to in principle.</p>',

    "10": '<p>The triple <em>kosmos</em> — the world was made through him, he was in it, the world did not know him — sets up the great paradox of the Incarnation. The Creator entering his own creation and going unrecognized is the precondition of the rejection that culminates at the cross. The theme of non-recognition runs through the Gospel: the world, the religious establishment, and even the disciples struggle to see who stands before them.</p>',

    "11": '<p>The coming to "his own" — Israel, the covenant people to whom the Messiah was promised — and their failure to receive him is the Evangelist\'s compressed account of what the synoptic narratives unfold at length. It echoes Isa 53:3 (the Suffering Servant "despised and rejected") and sets the pattern: the one sent to his own is sent ultimately to all who will receive him (v12). The rejection does not defeat the mission; it redirects it.</p>',

    "12": '<p>The authority to "become children of God" is Christ\'s unique gift — not granted by any OT figure, institution, or covenant. The new birth (spelled out in ch. 3) is received "in his name," meaning through the whole person and work of Christ. The Christological claim is that sonship is not a natural human condition but a gift from the Son, who shares the Father\'s nature and can therefore bestow that relationship.</p>',

    "13": '<p>The triple negation — not of blood, not of human will, not of a husband\'s will — clears away every natural mechanism for entering God\'s family. The rebirth is purely of God. This anticipates the new birth discourse of ch. 3 (3:3–8), where Jesus explains to Nicodemus that only the Spirit generates genuine children of God. The theme is that participation in Christ\'s sonship is entirely God\'s initiative, not human achievement.</p>',

    "14": '<p>The Incarnation compressed into one verse: the divine Word takes on full, mortal human flesh (<em>sarx</em>) and pitches his tent (<em>eskēnōsen</em>) among us. The tabernacle allusion is direct: the Shekinah glory that filled the Mosaic Tabernacle and Solomon\'s Temple now dwells in the body of the Son. When the disciples behold his glory, they are seeing in a human face what Israel saw in the cloud-filled sanctuary. Christ is the true and permanent Tabernacle.</p>',

    "15": '<p>John\'s testimony reverses the expected logic: the one who comes after me has surpassed me because he existed before me. The chronological inversion — later in earthly sequence, earlier in eternal existence — is the argument for Christ\'s supreme authority. The forerunner cannot surpass the eternal one; his role is precisely to point away from himself toward the one whose eternal pre-existence his own later birth acknowledges.</p>',

    "16": '<p>The fullness from which all grace flows is Christ\'s own fullness — his divine-human plenitude. "Grace upon grace" (<em>charin anti charitos</em>) is sometimes rendered as the new covenant grace succeeding the Mosaic covenant grace. The Christological point is that all grace in every age comes from the same source: the Word who contains life in himself (v4). There is no grace available to anyone that does not flow from him.</p>',

    "17": '<p>The Law was given through Moses as instrument; grace and truth "came to be" through Jesus Christ as person. The contrast is not between a good gift and a bad one but between mediation through an agent and arrival through the one who is himself the reality. This is also the first full naming of "Jesus Christ" in the Gospel — the complete messianic title introduced at the moment of announcing what surpasses every previous form of divine self-disclosure.</p>',

    "18": '<p>Christ as the exegete of God: the Greek <em>exēgēsato</em> ("has made known") is the verb from which "exegesis" derives — a thorough, unfolding declaration. No one has seen God (cf. Exod 33:20; 1 John 4:12), but the only-begotten Son who is in the Father\'s bosom has made him fully known. The claim is exclusive: the knowledge of God that humanity requires is available only through the Son. The entire Gospel is the unfolding of this "exegesis."</p>',

    "19": '<p>The institutional interrogation begins: Jerusalem sends priests and Levites to establish John\'s credentials. The Christological function is preparatory — the questioners are assembling the categories (Messiah, Elijah, the Prophet) that John will deny, clearing the field for the one who fulfills them all. The negative definition of John\'s identity is a positive definition of Jesus\'s.</p>',

    "20": '<p>"I am not the Messiah" — the clearest possible negation. John\'s explicit disavowal of the title he most visibly resembled opens the space for the one who will claim it. The Christological logic: the Baptist\'s "I am not" prepares for Christ\'s "I am" — the great series of self-identifications that the Evangelist unfolds through the Gospel.</p>',

    "21": '<p>The two titles John also refuses — Elijah (Mal 4:5) and the Prophet (Deut 18:15) — are titles that belong to Christ\'s mission: Jesus is the embodiment of the Elijah-like prophetic confrontation and the prophet like Moses of Deut 18:15 (see John 6:14; 7:40; Acts 3:22). John\'s refusals point the reader toward the one who fulfills all three expectation-categories simultaneously and in a higher sense.</p>',

    "22": '<p>The question "Who are you?" directed at John is the question the whole Gospel directs at Jesus. John deflects to Isaiah 40:3, identifying himself as a voice — not the word. The Christological structure: the forerunner exists only to answer the question about someone else; John\'s identity is entirely derivative from Christ\'s.</p>',

    "23": '<p>John identifies himself with Isa 40:3 — the herald preparing the way of the Lord. The "Lord" in Isaiah is YHWH; the Evangelist, following Mark\'s use of this text, places it as the preparation for Jesus. The implication is that Jesus is the Lord whose way is being prepared — a direct Christological identification of Jesus with the divine name.</p>',

    "24": '<p>The Pharisees among the questioners anticipate the institutional conflict that frames Jesus\'s entire ministry in the Fourth Gospel. The theme here is revelation of God: the gatekeepers of covenant identity are present from the very beginning, and their sustained inability to recognize Christ will define the narrative arc through ch. 12.</p>',

    "25": '<p>The Pharisees\' question implies that baptism is a messianic act — "Why baptize if you are not the Messiah?" — which inadvertently defines what the Messiah would do. The one who baptizes with the Holy Spirit (v33) is already present but unrecognized. The irony the Evangelist builds is that the very act they are interrogating points to the one who will fulfill what they are looking for.</p>',

    "26": '<p>Christ stands among them unrecognized — present but hidden, known only to the one God sent to announce him. "Among you stands one you do not know" is the Gospel\'s governing irony in miniature: throughout the narrative, Jesus will be among those who cannot perceive what is before them. The revelation is hidden not in absence but in presence.</p>',

    "27": '<p>John places himself below the slave level relative to Christ — in rabbinic tradition, a disciple did every task for his teacher except remove sandals (that was a slave\'s work). The Christological point is the absolute disproportion between the greatest of human prophetic figures and the one he announces. No human dignity or calling, however high, is commensurate with Christ\'s.</p>',

    "28": '<p>Bethany beyond the Jordan — the eastern side of the river, where Joshua crossed into the Promised Land and where Elijah was taken up in the whirlwind. The geography carries typological weight: the place of entry into the land and of prophetic succession is the place where the new Elijah identifies the one who surpasses him. The spatial setting reinforces the transition from the Mosaic-prophetic era to the messianic.</p>',

    "29": '<p>The title "Lamb of God who takes away the sin of the world" is the Christological apex of chapter 1. As a type: multiple OT strands converge — the Passover lamb of Exod 12:3 (blood averts judgment), the Servant of Isa 53:7 (led like a lamb to slaughter), the ram in Gen 22:8 ("God will provide the lamb"). The present participle "taking away" (<em>airōn</em>) signals an ongoing, not merely punctiliar, removal of the world\'s sin-condition.</p>',

    "30": '<p>John\'s testimony restates the inversion: "he comes after me but was before me." Each repetition of this logic deepens the Christological claim — not merely that Jesus is wiser or holier, but that his eternal priority over John (and over every created thing) is the basis of his supremacy. The forerunner\'s logic only works if the coming one pre-exists time.</p>',

    "31": '<p>The purpose of John\'s water baptism is the revealing of Christ to Israel — not the cleansing of individuals but the unveiling of the Messianic identity. The Evangelist consistently subordinates John\'s activity to its Christological function: every element of John\'s ministry exists as scaffolding for the recognition of Jesus.</p>',

    "32": '<p>The Spirit\'s descent and remaining on Jesus fulfills the anointing prophesied in Isa 42:1 ("I will put my Spirit on him") and Isa 61:1 ("The Spirit of the Lord is on me, because the LORD has anointed me"). The word "remained" (<em>emeinen</em>) — the Spirit stays, does not depart — distinguishes Jesus from Saul (on whom the Spirit came and left) and marks him as the permanent bearer of the divine anointing.</p>',

    "33": '<p>Christ\'s distinctive act — baptizing with the Holy Spirit — marks the transition from the age of anticipation to the age of fulfillment. The Baptist administers a baptism of repentance and preparation; Christ administers the Spirit that regenerates and indwells. This is the difference between forerunner and the one he heralds: John points toward the gift; Jesus gives it.</p>',

    "34": '<p>The formal Christological conclusion of the Baptist\'s testimony: "This is the Son of God." The title in the Fourth Gospel carries both the royal Davidic register (Ps 2:7, the king enthroned as Son) and the deeper Johannine sense of ontological divine relationship. The eyewitness formula "I have seen and I testify" positions this as legal testimony — the forerunner\'s sworn witness to the identity of Christ.</p>',

    "35": '<p>The transition from John to Jesus as the center of gravity: John is present again with his disciples, but the scene is designed for them to transfer their following. The Christological movement of the passage — from witness to the witnessed-to — enacts at the narrative level what the Prologue stated theologically: John\'s role is to point, and Christ is the destination pointed to.</p>',

    "36": '<p>The repeated title "Lamb of God" — here spoken to John\'s own disciples as Christ passes — functions as a second, private commissioning of the Isaiah 53 / Passover register. The Evangelist frames the discipleship call as a response to the Lamb-title, not to a miracle or an argument. Those who follow Christ do so because they have heard the Christological announcement: the Lamb who takes away the world\'s sin is passing.</p>',

    "37": '<p>The two disciples hear the Lamb-title and follow Jesus. This is the pattern the Evangelist establishes for the entire Gospel: hearing the true word about Christ generates following. The theme of believing and abiding — both rooted in the verb "follow" (<em>akoloutheō</em>) — begins here. The response to a correct Christological announcement is discipleship.</p>',

    "38": '<p>Christ\'s first words in the Gospel — "What do you want?" — are not a rebuff but an invitation to articulate desire. "Rabbi, where are you staying?" is the question that yields "Come and see" (v39), the invitation to abide with Christ. The Christological pattern: the knowledge of Christ is not abstract information but relational, participatory — one comes and sees by being with him.</p>',

    "39": '<p>"Come and see" — the discipleship invitation that will recur (1:46; 4:29). The disciples spend the day with Jesus; the Evangelist notes the tenth hour. The theme of abiding (<em>menō</em>) — staying with Christ — is introduced here and will develop into one of the Johannine themes of union with Christ (chs. 14–15). The Christological point: knowing Christ begins with coming and staying.</p>',

    "40": '<p>Andrew as a historical anchor: one of the two disciples is named, establishing continuity with the apostolic tradition. The narrative focus is on what Andrew does with what he has received — he immediately seeks his brother, demonstrating that Christological discovery is inherently missionary. Encountering Christ creates the impulse to bring others to him.</p>',

    "41": '<p>Andrew\'s announcement — "We have found the Messiah!" — is the first explicit messianic claim by a disciple in the Gospel. The Christological movement of vv19–41: the Baptist denies he is the Messiah, and the disciples discover that Jesus is. The whole of Israel\'s messianic hope, focused in the Davidic promise, converges in Andrew\'s single sentence.</p>',

    "42": '<p>Christ renames Simon as Cephas (Peter — "rock"). The renaming is a divine prerogative in scripture: God renamed Abram (Gen 17:5) and Jacob (Gen 32:28), marking a new identity and calling. That Jesus exercises this prerogative from the moment of meeting establishes his sovereign authority over persons. The name Peter will carry the weight of the confession in Matt 16 and the restoration in John 21.</p>',

    "43": '<p>The direct call "Follow me" — issued to Philip — is Christ\'s sovereign summons that requires no prior relationship, no explanation, no negotiation. The Christological authority here is royal-prophetic: as Elijah called Elisha (1 Kgs 19:19), so Christ calls his disciples, but with a directness that exceeds any human prophetic call. The disciples do not choose him; he chooses them (15:16).</p>',

    "44": '<p>Bethsaida is identified as the hometown of Philip, Andrew, and Peter — a Galilean fishing town near the northern shore of the lake. The Christological significance is geographical: the first disciples are Galileans, fulfilling the pattern of Isa 9:1–2 ("the people walking in darkness in the land of Zebulun and Naphtali have seen a great light"). The light dawns in the margins, not the center.</p>',

    "45": '<p>Philip\'s testimony to Nathanael: "We have found the one Moses wrote about in the Law, and about whom the prophets also wrote." The Christological claim is canonical — the whole OT points to Jesus. "Moses wrote" invokes Deut 18:15 (the Prophet like Moses), and "the prophets also wrote" covers the breadth of prophetic anticipation from Isaiah\'s Servant to Zechariah\'s King. Every scripture-strand converges in the man from Nazareth.</p>',

    "46": '<p>"Can anything good come from Nazareth?" — Nathanael\'s skepticism mirrors the despised origin theme of Isa 53:2 ("He had no beauty or majesty to attract us to him, nothing in his appearance that we should desire him"). Nazareth had no prophetic cachet. The Christological pattern: God\'s Messiah arrives in lowly, unexpected form, confounding the assumption that divine endorsement comes with visible prestige.</p>',

    "47": '<p>Jesus sees Nathanael and immediately declares him "a true Israelite in whom there is nothing false" — <em>dolos</em> (deceit, the word used of Jacob\'s trickery in Gen 27:35). Christ recognizes the genuine seeker before Nathanael has spoken or demonstrated faith. The Christological point is omniscience rooted in divine perception: he knows what is in each person (2:25), and this knowledge precedes human testimony.</p>',

    "48": '<p>"I saw you while you were still under the fig tree before Philip called you" — Christ\'s supernatural knowledge of a private moment is the ground of Nathanael\'s faith. The fig tree under which a pious Jew sat in contemplation and study is an eschatological image (Mic 4:4; Zech 3:10). That Christ saw Nathanael there is not merely a display of omniscience but an intimate divine regard for private devotion.</p>',

    "49": '<p>Nathanael\'s twin acclamation — "You are the Son of God! You are the King of Israel!" — maps the two primary Christological registers of the Gospel: divine sonship (Ps 2:7; the ontological relationship to the Father that the Evangelist traces) and royal-messianic identity (the Davidic king for whom Israel waited). The response to a single sign of divine knowledge is a full Christological confession, demonstrating that genuine encounter with Christ produces recognition.</p>',

    "50": '<p>Christ accepts the confession and promises greater revelation: "you will see greater things than that." The Christological trajectory points forward to the signs (2:11; 6:14; 11:45), the passion (12:23–32), and the resurrection appearances (20:8; 20:28). The discipleship of the Fourth Gospel is a progression of increasing Christological perception — each encounter revealing more of who Jesus is.</p>',

    "51": '<p>Jacob\'s dream at Bethel — angels ascending and descending on a ladder between heaven and earth (Gen 28:12) — is transferred to the Son of Man: the angels ascend and descend on him, not on a place. As a type: Christ is the new Bethel ("house of God"), the true meeting point of heaven and earth. The title "Son of Man" — used here for the first time in the Gospel — carries the heavenly freight of Dan 7:13, the one who comes with the clouds. The gate of heaven is a person.</p>'
  },
  "2": {
    "1": '<p>The third day carries deliberate resonance: in Jewish idiom it is the day of divine action and theophany (Exod 19:16; Hos 6:2). The Evangelist places the first sign on the third day, and the post-resurrection faith of the disciples (v22) will retrospectively illuminate this. The wedding at Cana is not incidental to the Gospel\'s Christological arc — it opens on resurrection-day timing and closes with the disclosure of glory.</p>',

    "2": '<p>Jesus and his disciples are present at a wedding as guests — Christ participates in ordinary human festivity and social life. The theme of revelation of God: God in the flesh is not a solitary contemplative but a participant in the community life of Galilean villages. The Incarnation encompasses celebration, not only sacrifice.</p>',

    "3": '<p>The wine runs out — the provision of the old order reaches its limit. The Christological movement of the sign turns on this deficiency: the vessels of purification (v6) are filled with water only to be transformed into the best wine (v10). The pattern anticipates the broader theme: whatever sufficiency the old covenant provided, Christ\'s arrival introduces a fullness that surpasses it (1:16).</p>',

    "4": '<p>"My hour has not yet come" — the language of "hour" (<em>hōra</em>) recurs in the Gospel as a technical term for the passion and glorification of Christ (7:30; 8:20; 12:23; 13:1; 17:1). Even when performing a gracious act, the Evangelist frames Christ\'s action in light of its ultimate destination. Every sign occurs in the interval before the hour; every sign points toward it. The Christological trajectory runs through Cana toward Calvary and Easter.</p>',

    "5": '<p>Mary\'s instruction — "Do whatever he tells you" — is the appropriate response to divine authority. The Christological pattern: Mary\'s role is not to direct Christ\'s power but to direct others toward it. The formula echoes Pharaoh\'s instruction about Joseph (Gen 41:55, "Go to Joseph and do whatever he tells you"), transferring that paradigm of mediating authority to Christ\'s servants. Obedience to Christ\'s word is the channel through which his power operates.</p>',

    "6": '<p>Six stone water jars for Jewish purification — the entire apparatus of ritual cleansing is about to be overtaken. The vessels that held the water of legal washing are filled with water and produce the wine of messianic celebration. As a shadow: the Mosaic purification system pointed forward to the cleansing Christ himself would accomplish. His arrival does not merely augment the old system; he fills its vessels with something new.</p>',

    "7": '<p>The servants obey — they fill the jars to the brim. The Christological pattern of the signs: obedience to Christ\'s command precedes the transformation. No explanation is given; no mechanism is described. The full filling leaves no room for partial solutions. The theme of abundance — the jars are filled to the brim, not partially — anticipates the "fullness" language of the Prologue (1:16) and the "abundant life" of 10:10.</p>',

    "8": '<p>The command to draw and take to the master of the banquet requires trust from the servants — they know what they put in, not what they will deliver. The Christological pattern: those who serve Christ act on his word alone, carrying to others what he has transformed. The servants who drew the water knew (v9); the miracle is hidden from the master but known to those who obeyed. Discipleship is enacted before the miracle is recognized.</p>',

    "9": '<p>The master of the banquet does not know the source of the wine; the servants who drew the water do. This distribution of knowledge is structurally significant: the one with authority does not perceive the miracle, while the obedient servants do. The Christological theme of hidden revelation — present but unrecognized (1:10) — runs through Cana: the source of transformation is Christ, and only those who obey his word know it.</p>',

    "10": '<p>"You have saved the best till now" — the unwitting testimony of the master to the pattern of the Gospel. Everyone else exhausts good wine and produces inferior; Christ reverses the direction. As a shadow: the eschatological banquet of Isa 25:6 promises "the best of meats and the finest of wines." The Evangelist presents the Cana wine as a foretaste of the messianic abundance — the best comes last, with Christ\'s arrival.</p>',

    "11": '<p>"The first of the signs through which he revealed his glory" — the Christological function of all the signs in the Gospel is stated explicitly: they reveal the glory of the divine Son. The word for "signs" (<em>sēmeia</em>) distinguishes the Johannine miracles from raw demonstrations of power — each sign points beyond itself to the identity of Christ. The disciples\' belief in response to the sign is the intended outcome: the sign creates the Christological perception that the narrative cultivates.</p>',

    "12": '<p>A narrative transition — Christ moves with family and disciples to Capernaum. The Christological significance is low; the Evangelist notes it briefly before the theologically loaded Jerusalem sequence. The theme of Christ as the center of a gathered community — mother, brothers, disciples — is present: from the beginning of his ministry he is not a solitary figure but one who creates community around himself.</p>',

    "13": '<p>The first of three Passovers in the Fourth Gospel marks the Gospel\'s Christological calendar: Christ is aligned with Passover from the beginning of his public ministry to the end (19:14, 31, 42). The Passover connection is not incidental — Christ is the Passover lamb (1:29), and his death at Passover time is the fulfillment of what the feast anticipated. The temple visit at Passover places him immediately in the space where that fulfillment will eventually be enacted.</p>',

    "14": '<p>The temple courts filled with commerce — the space designated for prayer and the presence of God has become a market. The Christological significance: Christ arrives in the Father\'s house and finds it corrupted. Mal 3:1 ("the Lord you are seeking will suddenly come to his temple") is being enacted. His clearing of the temple is a messianic act — the arrival of the one who has authority over the house that bears his Father\'s name.</p>',

    "15": '<p>Christ drives out the animals and overturns the tables with a whip he makes on the spot. As a shadow of the eschatological purification: Mal 3:2–3 describes the coming Lord as a "refiner\'s fire," purifying the temple and its servants. The physical force of the cleansing is a sign of the authority Christ exercises — not the authority of office (he holds no priestly or royal position by human appointment) but the authority inherent in divine sonship.</p>',

    "16": '<p>"My Father\'s house" — the first use of this phrase in the Gospel, and an implicit Christological claim: the temple is not merely God\'s house but his Father\'s house, establishing the sonship relationship that will define the entire Gospel\'s Christology. The buyers of doves (the poor\'s offering, Lev 5:7) are addressed, not the bankers — the commerce has penetrated even the most accessible sacrifice. The Father\'s house has been turned into a marketplace.</p>',

    "17": '<p>The disciples recall Ps 69:9 — "Zeal for your house will consume me" — as a fulfillment. The psalm is a Davidic lament of suffering unjust reproach; the NT applies it repeatedly to Christ\'s passion (Rom 15:3; John 19:29). That the disciples connect the temple cleansing with this text suggests they perceive the Christological stakes: the zeal that drives Christ to cleanse the temple is the same zeal that will lead to his death. The house consumes the one devoted to it.</p>',

    "18": '<p>The authorities demand a legitimating sign: "What sign can you show us to prove your authority?" The Christological irony is dense — the demand for a sign comes immediately after the greatest messianic sign they could have asked for (the prophesied Lord arriving suddenly at his temple). They demand proof of the authority they have just witnessed. The Gospel\'s pattern: those who require external validation from Christ have already failed to perceive the revelation that stands before them.</p>',

    "19": '<p>"Destroy this temple, and I will raise it again in three days" — the most concentrated Christological prophecy of the chapter. The Evangelist provides the interpretation in v21 (his body), but the saying functions on multiple levels: it announces the resurrection, claims authority over the ultimate divine symbol, and redefines the location of God\'s presence as the Son\'s own body. The saying will return at the trial (Mark 14:58; Matt 26:61) as a charge against him.</p>',

    "20": '<p>The authorities take the statement literally — Herod\'s temple, begun 46 BCE, under construction for decades. The Christological irony: they cannot hear the saying on any level except the architectural. The inability to hear Christ\'s words on their deeper register is one of the Gospel\'s recurring patterns: Nicodemus hears "born again" as re-entry into the womb; the Samaritan woman hears "living water" as water that saves a trip to the well. Literal hearing blocks Christological perception.</p>',

    "21": '<p>The Evangelist provides the interpretive key: the temple he spoke of was his body. As a shadow fulfilled: the temple was always the dwelling-place of God with his people — the theme running from Tabernacle through Solomon\'s temple to Ezekiel\'s vision of the restored temple (Ezek 37:26–27). Christ\'s body is the true and permanent fulfillment of that trajectory — the place where God and humanity are united, which cannot be permanently destroyed (John 2:19; 10:18).</p>',

    "22": '<p>After the resurrection, the disciples remember and believe "the scripture and the words that Jesus had spoken." The Christological epistemology: the resurrection retroactively illuminates both scripture and Christ\'s own teaching. Before Easter, much of what Jesus said is opaque; after Easter, it is transparent. The Evangelist writes from the post-resurrection vantage point throughout — the commentary of the Spirit (14:26; 16:13) enables the understanding that the disciples lacked during the ministry.</p>',

    "23": '<p>Many in Jerusalem believe on seeing the signs — the seed-faith generated by visible miracles. The Christological qualification of v24 distinguishes sign-faith from genuine faith: sign-faith responds to what Christ does; genuine faith responds to who Christ is. The signs are not the goal but the means by which the Evangelist hopes to lead readers from initial belief to the deeper Christological perception that the Gospel cultivates (20:30–31).</p>',

    "24": '<p>Christ does not entrust himself to them — he does not place his confidence (<em>episteusen</em>, same root as "believe") in the belief of those who believe in him on the basis of signs. The Christological insight into human hearts is itself a divine attribute: only God fully knows what is in a person. The same omniscience that saw Nathanael under the fig tree (1:48) perceives the limits of the crowd\'s faith.</p>',

    "25": '<p>He "knew what was in each person" — the final verse of ch. 2 states what the Prologue implied: Christ\'s knowledge of humanity is not derived from testimony but intrinsic. He needs no one to tell him what people are like; he made them. The Christological claim draws on the creation theology of vv1–3: the Creator knows his creation from the inside. This knowledge is not surveillance but the omniscience of the one who formed each human being.</p>'
  }
}


def main():
    existing = load_comm('mkt-christ', 'john')
    merge_comm(existing, JOHN)
    save_comm('mkt-christ', 'john', existing)
    print('John 1–2 mkt-christ written.')

if __name__ == '__main__':
    main()
