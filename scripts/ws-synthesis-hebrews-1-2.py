"""
Wide Source Synthesis — Hebrews chapters 1–2
bookId: hebrews
Run: python3 scripts/ws-synthesis-hebrews-1-2.py

Sources used: calvin, ellicott, clarke, wesley, barnes, rwp
Chapter range: 1–2  (32 verses approx.)
Note: mhcc not available for hebrews; jfb data corrupted (2 Corinthians content loaded in error)

Key synthesis decisions:
- 1:4  "having become" vs. "being made" — Ellicott reads as post-resurrection exaltation;
       Calvin/Barnes read as the Son's inherent superior rank. Set consensus: mixed.
- 1:6  "again" (πάλιν) — Ellicott/Robertson read as second coming;
       Calvin/Barnes read as introducing another quotation. Set consensus: mixed.
- 1:7  "spirits" vs. "winds" — Ellicott prefers "winds" from the Greek/Hebrew;
       traditional English rendering is "spirits." Set consensus: mixed.
- 2:7  "a little lower" — whether the Psalm refers to Adam (Clarke/Wesley)
       or directly to Christ (author of Hebrews); and whether "little" = degree or time. Set: mixed.
- 2:11 "of one" (ἐξ ἑνός) — Ellicott, Clarke, Wesley prefer "of one Father";
       some read "of one kind/nature." Set consensus: mixed.
- 2:15 Fear of death as universal vs. particularly Gentile bondage — Clarke vs. Calvin/Wesley. Set: mixed.
- 2:16 ἐπιλαμβάνεται — "takes hold of to help" vs. KJV "took on him the nature of." Set: mixed.
"""

import json, pathlib

ROOT = pathlib.Path(__file__).parent.parent

def load_synthesis(book):
    p = ROOT / 'data' / 'commentary' / 'synthesis' / f'{book}.json'
    if p.exists():
        return json.loads(p.read_text())
    return {}

def save_synthesis(book, data):
    p = ROOT / 'data' / 'commentary' / 'synthesis' / f'{book}.json'
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=None))
    print(f'  wrote {p.relative_to(ROOT)}')

def merge_synthesis(existing, new_data):
    """Merge new chapter/verse entries without overwriting existing ones."""
    for ch, verses in new_data.items():
        if ch not in existing:
            existing[ch] = {}
        for v, entry in verses.items():
            if v not in existing[ch]:
                existing[ch][v] = entry

HEBREWS = {
    "1": {
        "1": {
            "synthesis": "<p>The epistle opens with a sentence architecturally designed to set old and new revelation side by side. On one side: God speaking to the fathers through the prophets, in many portions (<em>πολυμερῶς</em>) and many manners (<em>πολυτρόπως</em>); on the other: that same God speaking through his Son, a disclosure both complete and final. Calvin identifies three contrasts compressed into the opening: Son versus prophets, the present generation versus the fathers, one perfect revelation versus its many fragmentary predecessors. Ellicott presses the Greek further, noting the artistic arrangement—multiplicity over against singularity—and renders the verse: \"In many portions and in many ways God having of old spoken unto the fathers in the prophets, at the end of these days did speak unto us in a Son.\" Wesley catalogs the specific times God spoke (creation to Adam, judgment to Enoch) and observes that the very number of the prophets betrayed the partial character of each. Barnes reflects that the \"last days\" idiom signals not the imminent end of history, but the finality of this dispensation—no further one follows. Robertson notes the epistle opens like Genesis and John's Gospel: with God as subject, author of both covenants. All voices agree: the old revelation was trustworthy; the new is supremely authoritative precisely because it comes through the Son rather than through servants.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>This beginning is for the purpose of commending the doctrine taught by Christ; it shows that we ought not only reverently to receive it, but also to be satisfied with it alone. The Son of God is set in opposition to the prophets; then we to the fathers; and thirdly, the various and manifold modes of speaking which God had adopted as to the fathers, to the last revelation brought to us by Christ.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>The writer's object is to place the former revelation over against that which has now been given. If we imitate the artistic arrangement of the Greek: <em>In many portions and in many ways God having of old spoken unto the fathers in the prophets, at the end of these days did speak unto us in a Son.</em> The manifold successive partial disclosures of God's will have given place to one revelation, complete and final.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "John Wesley's Notes",
                    "html": "<p>God, who at sundry times—The creation was revealed in the time of Adam; the last judgment, in the time of Enoch. In divers manners—In visions, in dreams, and by revelations of various kinds. Both these are opposed to the one entire and perfect revelation which he has made to us by Jesus Christ. The very number of the prophets showed that they prophesied only <em>in part.</em></p>"
                },
                {
                    "src": "rwp",
                    "attr": "Robertson's Word Pictures",
                    "html": "<p>This Epistle begins like Genesis and the Fourth Gospel with God, who is the Author of the old revelation in the prophets and of the new in his Son. The periodic structure of the sentence (vv. 1–4) serves as an introduction to the whole Epistle. <em>Of old time</em> (<em>πάλαι</em>)—\"long ago\"—stands in sharp contrast to <em>at the end of these days</em> in verse 2.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "2": {
            "synthesis": "<p>The single sentence that opens Hebrews extends through verse 2, naming the Son's twofold dignity: he is the appointed heir of all things, and the one through whom God made the worlds. Calvin draws out the practical weight of both—since all things belong to the Son, no good is found apart from him; since creation itself was made through him, his dominion is not a later grant but an original right. Ellicott insists on the translation \"in a Son\" rather than \"in his Son,\" since the Greek lacks both article and pronoun; what matters is not which Son but what the Son is—God's own adequate and final revealer. Clarke confirms the point from the Greek text: <em>ἐν Υἱῷ</em>, without pronoun, carries the absolute sense, so that God's revelation through him stands as categorically different from revelation through any creature. Wesley links appointment as heir to the name Son: the inheritance was settled before the worlds were made, the Son being the firstborn who holds all rights of primogeniture. Barnes places this in the language of \"last days\"—the final dispensation under which all history will close—which makes the Son's role as both creator and heir the ground for the epistle's entire argument about finality and sufficiency. Robertson notes that the Son is not merely the channel of the revelation but its content: \"the very counterpart of God.\"</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>He honors Christ with high commendations, in order to lead us to show him reverence; for since the Father has subjected all things to him, we are all under his authority. No good can be found apart from him, as he is the heir of all things. This honor of possessing all things belongs by right to the Son, because by him have all things been created.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>Better, <em>at the end of these days spake unto us in a Son.</em> The thought common to both verses is \"God hath spoken to man.\" The manifold successive partial disclosures of God's will have given place to one revelation, complete and final; for He who spake in the prophets hath now spoken \"in a Son\"—not, who is the Revealer? but, what is he? The whole stress lies on these last words.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "John Wesley's Notes",
                    "html": "<p>Whom he hath appointed heir of all things—After the name of Son, his inheritance is mentioned. God appointed him the heir long before he made the worlds. The Son is the firstborn, born before all things: the heir is a term relating to the creation which followed. By whom he also made the worlds—therefore the Son was before all worlds. His glory reaches from everlasting to everlasting.</p>"
                },
                {
                    "src": "rwp",
                    "attr": "Robertson's Word Pictures",
                    "html": "<p><em>In his Son</em> (<em>ἐν υἱῷ</em>)—no article or pronoun, giving the absolute sense of \"Son.\" Here the idea is not merely what Jesus said, but what he is (Dods), God's Son who reveals the Father. <em>The Old Testament slopes upward to Christ.</em> The revelation was not a word merely, but a Person.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "3": {
            "synthesis": "<p>Verse 3 is the theological summit of the epistle's opening sentence, piling seven affirmations onto the Son before the main verb arrives. He is the <em>ἀπαύγασμα</em>—the effulgence or outbeaming—of God's glory, and the <em>χαρακτήρ</em>—the exact impression, the stamp—of his substance; he upholds all things by the word of his power; having purged sins, he sat down at the right hand. Ellicott notes that <em>ἀπαύγασμα</em> became the source-text for the Nicene Creed's \"God of God, Light of Light, Very God of Very God,\" and that both \"effulgence\" and \"exact image\" had parallel uses in Philo and in Wisdom 7:26, showing the author deploying conceptual language his readers already knew. Clarke's analysis of <em>ἀπαύγασμα</em> is precise: it is the splendor emitted from the source, not the source itself, so that what shines from the Son is the same divine glory that resides in the Father. Calvin cautions against pressing the analogies too far—they are similitudes borrowed from nature—but affirms that the verse speaks of both Christ's divine essence and his human nature as mediator. Robertson fastens on the word <em>ὤν</em>, the present participle of absolute, timeless existence, set in deliberate contrast to <em>γενόμενος</em> in verse 4, just as John 1:1 uses <em>ἦν</em> over against <em>ἐγένετο</em>. Wesley reads the \"express image\" as saying: whatever the Father is, is exhibited in the Son, as a seal in the stamp on wax.</p>",
            "voices": [
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>Who being the effulgence of His glory and the exact image of His substance. The first figure is familiar in the words of the Nicene Creed (derived from this verse), \"God of God, Light of Light, Very God of Very God.\" Striking parallels present themselves in Philo and in the Book of Wisdom: \"She is the effulgence of the everlasting light, the unsullied mirror of the energy of God.\"</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p>The resplendent outbeaming of the essential glory of God. <em>Αὐγασμα</em> is that which has splendor in itself; <em>ἀπαύγασμα</em> is the splendor emitted from it. But the inherent splendor and the emitted splendor are both from the same source, and the emitted is of the same nature as the inherent. The same expression is used in Wisdom 7:26 of the uncreated Wisdom: \"she is the splendor of eternal light.\"</p>"
                },
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>These things are said of Christ partly as to his divine essence, and partly as a partaker of our flesh. Nothing can be said of things so great and so profound but by similitudes taken from created things. There is therefore no need to press the analogies too far. The whole is stated in order to set forth the dignity of Christ—that his glory is the very glory of God, not a derived imitation.</p>"
                },
                {
                    "src": "rwp",
                    "attr": "Robertson's Word Pictures",
                    "html": "<p><em>Being</em> (<em>ὤν</em>)—absolute and timeless existence (present active participle of εἰμί) in contrast with <em>γενόμενος</em> in verse 4, like <em>ἦν</em> in John 1:1 (in contrast with <em>ἐγένετο</em> in 1:14) and like <em>ὑπάρχων</em> and <em>γενόμενος</em> in Philippians 2:6f. The effulgence (<em>ἀπαύγασμα</em>)—can mean either reflected brightness or effulgence, ray from an original light body; the Greek Fathers hold the latter. Both senses are true of Christ.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "4": {
            "synthesis": "<p>The long opening sentence closes with a comparison: the Son \"having become\" so much greater than the angels as he has by inheritance obtained a more excellent name. The word the author uses—<em>γενόμενος</em>, \"having become\"—is the same one Robertson noted as a deliberate contrast to the timeless <em>ὤν</em> of verse 3; and Ellicott insists on the translation, arguing that the verse speaks not of the eternal glory that was always the Son's, but of the exaltation that became his after he had \"made purification of sins.\" On this reading the comparison looks to the resurrection and session—his post-humiliation enthronement—as the specific event establishing his superiority over angels. Calvin, reading with the grain of the whole argument, sees the comparison as addressed to Jewish readers who held angels in extraordinary esteem (believing, as Clarke documents, that angels participated in the creation of the world and served as God's privy council); the point is simply that the Son is categorically above them. Barnes reads \"better\" as a ranking of dignity, not of moral character: as Mediator, as the Son of God in our nature, Christ holds a rank that no angel shares. The \"more excellent name\" that sets him apart will be identified in the next verses as \"Son.\"</p>",
            "voices": [
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>Better, <em>having become.</em> These words must be closely joined with the last clause of verse 3; they speak, not of the glory which was ever His, but of that which became His after He had \"made purification of sins.\" Having become \"greater than the angels,\" on the one hand the argument of chapter 1 is opened; on the other, the theme of his humiliation and exaltation through suffering is laid down for chapter 2.</p>"
                },
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>After having raised Christ above Moses and all others, he now amplifies His glory by a comparison with angels. It was a common notion among the Jews that the Law was given by angels; they attentively considered the honorable things spoken of them everywhere in Scripture; and as the world is strangely inclined to superstition, they were disposed to regard angels with excessive veneration.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes",
                    "html": "<p>Being made so much better—being exalted so much above the angels. The word \"better\" here does not refer to moral character, but to exaltation of rank. As Mediator; as the Son of God in our nature, he is exalted far above the angels. The inheritance of a more excellent name points forward to what is established in the quotations that follow: the name \"Son,\" which no angel receives.</p>"
                }
            ],
            "consensus": "mixed",
            "key_tension": "Ellicott reads 'having become' as pointing specifically to the post-resurrection exaltation earned through the Son's finished work of purification, while Calvin and Barnes read the comparison as the Son's general and inherent superiority over angels that the whole chapter is designed to demonstrate."
        },
        "5": {
            "synthesis": "<p>Having named the \"more excellent name,\" the author now proves it with two Old Testament quotations. The first—\"Thou art my Son; this day have I begotten thee\" (Ps 2:7)—and the second—\"I will be to him a Father, and he shall be to me a Son\" (2 Sam 7:14)—are joined by the question: \"For unto which of the angels said he at any time...?\" The rhetorical force is absolute: while \"sons of God\" may be used of angels as a class, no individual angel was ever addressed in this singular, personal way. Ellicott notes the distinction carefully—the plural \"sons of God\" applied collectively to angels carries a different weight than the singular address to the Messiah. Calvin reads both quotations as originally spoken of David and Solomon respectively, but sustaining their fuller meaning in Christ as the one who uniquely fulfills what was said of them in type. Clarke agrees that Psalm 2:7 was consistently understood by the rabbis and Paul himself (Acts 13:33) as referring to the Messiah. Wesley reads \"this day\" as pointing not to a moment in history but to eternity itself—one continuing \"today\" in which the Son stands begotten. Barnes observes that the whole argument requires the Messiah's unique sonship: no angel was ever offered this relationship, so the Son stands incomparably above the entire angelic order.</p>",
            "voices": [
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>\"God has spoken of the Messiah as His Son, a title which no angel ever receives from Him.\" The appellation \"sons of God\" may be used in a wider sense of the members of the heavenly host, but even so it is a collective and general description, never the singular personal address which these two quotations establish as belonging uniquely to the Messiah.</p>"
                },
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>It cannot be denied but that this was spoken of David, that is, as he sustained the person of Christ. The things found in this Psalm must have been shadowed forth in David; but since he was only a type, the full meaning is not to be sought in him. The Apostle, then, rightly applies to Christ what David said of himself, inasmuch as David was a type of Christ.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "John Wesley's Notes",
                    "html": "<p>Thou art my Son—God of God, Light of Light. This day have I begotten thee—I have begotten thee from eternity, which, by its unalterable permanency of duration, is one continued, never-beginning, never-ceasing day. I will be to him a Father—so implying his right to the inheritance; and he shall be to me a Son—so implying his participation of my nature.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes",
                    "html": "<p>The object of this is to prove that the Son of God, who has spoken to men in these last days, is superior to the angels. The apostle goes to the Old Testament to show that a name was given to the Messiah which was never given to the angels—the name of Son, conveying a relationship entirely unique. To which of the angels was such a word ever addressed? To none.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "6": {
            "synthesis": "<p>The author adds a third Old Testament witness: \"Let all the angels of God worship him\" (Psalm 97:7 / Deut 32:43 LXX). The logic is straightforward—if angels are commanded to worship the Son, he must be superior to them. The crux of the verse is the phrase \"and again, when he bringeth in the firstbegotten into the world,\" where the word <em>πάλιν</em> (\"again\") is genuinely ambiguous. Ellicott reads the clause as referring to the Parousia, the second coming: when God shall again lead the Firstborn into the inhabited world, all angels will worship him. Robertson agrees that if <em>πάλιν</em> governs the verb, the reference is to Christ's return. Calvin, by contrast, reads \"again\" as a simple transitional particle introducing another quotation from Scripture—\"and again [it is said]\"—with no reference to the second advent. Barnes follows the same reading. Wesley's brief note focuses on \"firstbegotten,\" connecting it to the rights of primogeniture already mentioned in verse 2. Clarke distinguishes carefully between \"firstbegotten\" as the ground of Christ's rights and the command to angels as proof of his supremacy over them.</p>",
            "voices": [
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>There seems little doubt that the true translation is: <em>And when He again leadeth the Firstborn into the world He saith, Let all the angels of God worship him.</em> If <em>πάλιν</em> is taken with the verb, the reference to the Second Advent is clear—when God shall again introduce his Son into the world, all angels are commanded to worship him.</p>"
                },
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>He now proves by another argument that Christ is above the angels, and that is because the angels are bidden to worship him. It hence follows that he is Lord of angels, and therefore above them. The word <em>again</em> is a transitional particle—\"and again [Scripture] saith\"—and does not point to a second coming, but to a further proof-text for the Son's supremacy.</p>"
                },
                {
                    "src": "rwp",
                    "attr": "Robertson's Word Pictures",
                    "html": "<p>If <em>πάλιν</em> is taken with <em>εἰσαγάγῃ</em>, it refers to the second coming; if <em>πάλιν</em> goes with <em>λέγει</em> it simply means \"again he saith.\" The indefinite temporal clause with <em>ὅταν</em> and the aorist subjunctive of <em>εἰσάγω</em> leaves the timing deliberately open. The command to angels—<em>Let all the angels of God worship him</em>—is the essential point in either case.</p>"
                }
            ],
            "consensus": "mixed",
            "key_tension": "Ellicott and Robertson read 'again' (πάλιν) as modifying 'bringeth in,' making the verse a reference to Christ's second advent; Calvin and Barnes read 'again' as simply introducing another quotation, with no temporal reference to the Parousia."
        },
        "7": {
            "synthesis": "<p>The contrast sharpens: \"of the angels he saith\" (quoting Psalm 104:4) versus \"of the Son he saith\" (verse 8). Angels are described as <em>πνεύματα</em> and a \"flame of fire\"—created, variable, serving God's sovereign will. Calvin reads the Psalm as originally describing how God works through natural forces (winds, fire) and only secondarily applies to angels as his ministers, who are like those forces: swift, powerful, but wholly at the divine disposal. Ellicott challenges the traditional English rendering and argues that <em>πνεύματα</em> here means \"winds\" rather than \"spirits\"—angels are as transient as winds, as changeable as flames—while the Son is eternal (verse 8). Clarke reads the verse as showing that angels are servants, not sons: \"They are no more than his servants, as tempests and lightning are his servants.\" Wesley picks up the contrast with verse 8 as the key: by calling angels mere creatures, the author prepares the reader to receive the Son as the eternal Creator. Barnes summarizes: angels are assigned an inferior name and a more humble office—they are ministers, the Son is sovereign.</p>",
            "voices": [
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>Better, <em>winds</em>. The verse establishes a deliberate contrast: of the angels—who are as variable and transient as winds and flames, wholly instruments of the divine will—over against the Son, who is addressed as God and whose throne is forever. The point is not the dignity of angels but their creatureliness, which makes the Son's eternal sovereignty stand out the more.</p>"
                },
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>The passage quoted seems to describe the manner in which God works in this world by his ministers; but the design of the Apostle is to show the condition of angels. As David is describing the manner in which God employs the elements of this world as his servants, the Apostle takes occasion to say that angels are not above that condition—they too are merely servants, employed according to the sovereign pleasure of God.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "John Wesley's Notes",
                    "html": "<p>Who maketh his angels spirits—This implies they are only creatures, whereas the Son is eternal (verse 8) and the Creator himself (verse 10). Spirits and a flame of fire—which intimates both their excellency and their ministry; executing God's commands with the utmost swiftness and fervency. But this creaturely dignity is entirely different from the Son's eternal, uncreated majesty.</p>"
                }
            ],
            "consensus": "mixed",
            "key_tension": "Ellicott argues that πνεύματα should be rendered 'winds' (variable, transient elements that serve God's purposes), emphasizing the angels' mutability and dependence; the traditional rendering 'spirits' emphasizes their immaterial nature, though both readings agree on the main point of their creatureliness and servitude."
        },
        "8": {
            "synthesis": "<p>Now the contrast reaches its apex: \"But of the Son he saith, Thy throne, O God, is for ever and ever\" (Ps 45:6–7). The author addresses the Son directly as God—<em>ὁ θεός</em>—citing a Psalm originally composed as a royal wedding ode for a Davidic king. All the commentators treat this as one of the most direct New Testament affirmations of Christ's deity. Calvin acknowledges the Psalm was composed for Solomon's marriage but argues that what is written is \"much too high to be applied to Solomon\"—the Psalm therefore points through the type to its antitype. Clarke makes the argument explicit: if Jesus Christ is here called God, then Jesus Christ is God, and the design of the whole passage is to prove this. Wesley reads \"O God\" as bearing its full singular weight—\"God, in the singular number, is never in Scripture used absolutely of any but the supreme God\"—and connects the eternal throne to the eternal sceptre of righteousness. Robertson notes a textual question: whether <em>ὁ θεός</em> is vocative (\"O God\") or nominative with \"is\" implied (\"God is thy throne\"), but he concludes that either reading affirms Christ's deity. Barnes records that both Jewish and Christian interpreters applied the Psalm to the Messiah.</p>",
            "voices": [
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p>Thy throne, O God, is for ever and ever—If this be said of the Son of God, i.e. Jesus Christ, then Jesus Christ must be God; and indeed the design of the apostle is to prove this. The words here quoted are taken from Psalm 45:6, which the ancient Chaldee paraphrast and the most intelligent rabbins refer to the Messiah.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "John Wesley's Notes",
                    "html": "<p>O God—God, in the singular number, is never in scripture used absolutely of any but the supreme God. Thy reign, of which the sceptre is the ensign, is full of justice and equity. The eternal throne and the righteous sceptre together show that what is addressed to the Son is no mere honorific: he is the sovereign God whose rule is everlasting.</p>"
                },
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>It must indeed be allowed that this Psalm was composed as a wedding song; but what is here related is much too high to be applied to Solomon. The Jews, that they may not be forced to own Christ to be called God, make the word in the vocative case to mean a kind of inferior deity; but this is a vain evasion. The Son is here addressed as God with a plain and unambiguous predication.</p>"
                },
                {
                    "src": "rwp",
                    "attr": "Robertson's Word Pictures",
                    "html": "<p>It is not certain whether <em>ὁ θεός</em> is here the vocative—\"O God\"—with the Messiah termed <em>θεός</em>, as in John 20:28, or whether <em>ὁ θεός</em> is nominative with <em>ἐστιν</em> understood: \"God is thy throne\" or \"Thy throne is God.\" Either makes good sense. Both senses affirm the Son's deity and the eternal, righteous character of his reign.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "9": {
            "synthesis": "<p>The citation from Psalm 45 continues: the king has loved righteousness and hated iniquity, and therefore God—\"even thy God\"—has anointed him with the oil of gladness above his fellows. Calvin observes that all this was said of Solomon first, and that Solomon's exaltation above his brothers after David's death was a type of Christ's anointing above all his companions. Ellicott reads the verse as showing both divine election and divine reward: the Son was appointed by God and exalted by God, the one who reigns by right and the one who is crowned as reward for righteousness. Clarke reads \"loved righteousness and hated iniquity\" as the characteristic of the perfectly just Governor—the one who suppresses iniquity and upholds truth—and sees in the anointing the royal and priestly investiture of the Messiah. Wesley notes that the anointing is as Mediator: \"thy God\" means the one who is God to him in his mediatorial capacity. Robertson supplies the etymological link: the verb here is <em>ἔχρισέν</em>, the first aorist of <em>χρίω</em>, the very root from which <em>Χριστός</em> (\"the Anointed One\") derives—so the Psalm names the Messiah in the act of his anointing.</p>",
            "voices": [
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>The King by divine election has been exalted by divine reward. It is possible that the words \"therefore God, even thy God\" could be addressed either to the Father or to the Son, but the plain sense is that the eternal Son, having loved righteousness in his earthly obedience, receives from the Father the anointing of exaltation above all his companions.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "John Wesley's Notes",
                    "html": "<p>Thou hast loved righteousness and hated iniquity—Thou art infinitely pure and holy. Therefore God—Who, as thou art Mediator, is thy God—hath anointed thee with the oil of gladness above thy fellows. The anointing above his companions points to his unique mediatorial rank: no other king, prophet, or priest receives so full an anointing.</p>"
                },
                {
                    "src": "rwp",
                    "attr": "Robertson's Word Pictures",
                    "html": "<p>Hath anointed thee (<em>ἔχρισέν σε</em>)—first aorist active indicative of <em>χρίω</em>, to anoint, from which verbal <em>Χριστός</em>, the Anointed One, comes. The Psalm thus names the Messiah in the act of his anointing, connecting the royal title to the perfect moral character from which the exaltation flows: he is anointed <em>because</em> he has loved righteousness.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "10": {
            "synthesis": "<p>The author now reaches back to Psalm 102:25–27 for his third address to the Son: \"Thou, Lord, in the beginning hast laid the foundation of the earth; and the heavens are the works of thine hands.\" The move is significant—Psalm 102 is a lament of a creature under affliction, yet the author reads its closing doxology as a divine address to the Son, showing that the Son who \"made purification of sins\" (v. 3) and who \"became\" superior to angels (v. 4) is also the original Creator. Clarke identifies this as an address to the Son as Creator, consistent with verse 2 where God made the worlds \"through him.\" Calvin, anticipating the objection that the Psalm is about Yahweh and not obviously about Christ, argues that the point in dispute requires attributing creative power to the one whose authority is being established—and since the Son is the one through whom all things were made, the Psalm fits perfectly. Ellicott connects the passage to verse 8, treating verses 10–12 as the second part of the contrast between angels and the Son: in verse 8 the Son has an eternal throne; here he is the Creator whose creation will perish while he endures. Robertson notes the emphatic <em>σύ</em> (\"thou\") that opens the quotation in the LXX—the personal, direct address to the Son as Lord and Maker.</p>",
            "voices": [
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p>This is an address to the Son as the Creator; for this is implied in laying the foundation of the earth. The heavens, which are the work of his hands, declare his power and Godhead. Consistent with the argument of verse 2, where God made the worlds through him, this quotation from Psalm 102 establishes that the one addressed as \"Lord\" and \"Creator\" is none other than the Son.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>Verses 10–12 are linked with verse 8 as presenting the second part of the contrast between angels and the Son. As there we read of a divine sovereign reign—\"thy throne... for ever and ever\"—here we read of the Creator who made the heavens and earth and who will outlast them. The eternal Son is both sovereign and Creator; the contrast with angels, who are merely creatures, could not be sharper.</p>"
                },
                {
                    "src": "rwp",
                    "attr": "Robertson's Word Pictures",
                    "html": "<p>Quotation from Psalm 102:26–28. Note the emphatic position of <em>σύ</em> (\"thou\") here at the beginning, as in verses 11–12—a direct, personal address to the Son as Lord. The LXX has <em>Κύριε</em> where the Hebrew has no such vocative; the author uses the LXX form to establish the Son as the divine Lord addressed in the Psalm.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "11": {
            "synthesis": "<p>The Creator-Son's permanence is set over against the transience of his creation: \"They shall perish; but thou remainest.\" The heavens and earth—the very things he made—shall wax old like a garment; he shall outlast them all. Ellicott points to Isaiah 34:4 and 51:6 as the background: the created order that seems so fixed and permanent is actually contingent. Clarke draws out an important precision: the heavens and earth shall be \"changed,\" not annihilated—the same matter and the same structure will pass through transformation into the new creation, but the Son who made them is exempt from any such change. Barnes reads the verse as asserting something important changes about the created order, without claiming absolute annihilation—the language of \"perishing\" describes the passing of the present form. Wesley is covered by his note on verse 10, which extends through the quotation. Robertson observes, with characteristic interest in scientific fact, that modern science itself has come to acknowledge the non-eternity of the physical universe—the heat death problem was already recognized in Robertson's day—so the writer of Hebrews makes a claim no longer contested even on naturalistic grounds.</p>",
            "voices": [
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>Both the earth and the heavens: see Isaiah 34:4, \"The heavens shall be rolled together as a scroll\"; and Isaiah 51:6, \"The earth shall wax old like a garment.\" The language of the Psalm is not the hyperbole of despair but the sober recognition that all created things are contingent—only the Son, who made them, stands above their decay.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p>They shall perish—permanently fixed as they seem to be, a time shall come when they shall be dissolved, and afterward new heavens and a new earth be formed, in which righteousness shall dwell. Not annihilation but transformation: the created order will change, but the Son who made it is the same yesterday, today, and forever.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes",
                    "html": "<p>They shall perish—that is, the heavens and the earth. They shall pass away; or they shall be destroyed. Probably no more is meant than that important changes will occur in them, or that they will undergo great revolutions; they shall not exist always in their present form. The contrast is with the Son, who remains entirely unchanged through all that the created order undergoes.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "12": {
            "synthesis": "<p>The garment metaphor completes the contrast: \"As a vesture shalt thou fold them up, and they shall be changed: but thou art the same, and thy years shall not fail.\" The created heavens are as a cloak the Son rolls up—an image of casual, effortless sovereignty over what he made. Ellicott renders the verb sharply: \"as a mantle shalt Thou roll them up\"—the universe is changed with no more difficulty than folding a garment. The affirmation \"thou art the same\" is, Clarke insists, a predicate that can be said of no being but God: it is the divine immutability, the very quality expressed in the \"I am\" of Exodus 3. Clarke continues: the years of the Son shall not fail—a direct refusal of any temporal limit on his existence. Wesley's note is brief but telling: they shall be \"changed into new heavens and a new earth\"—the dissolution is not destruction but renewal—but the Son is eternally the same through and beyond all such renewal. Barnes rounds out the imagery: the outer garment (<em>περιβόλαιον</em>), thrown around and rolled up, pictures complete, unforced mastery over the created order.</p>",
            "voices": [
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>And as a mantle shalt Thou roll them up; as a garment shall they also be changed. The course of thought is easily traced: as a cloak is rolled up at the end of a journey, so the present form of the heavens and earth will be rolled up when their purpose is served. The ease and mastery of the action is part of the image—no labor, no resistance, only sovereign disposal.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p>But thou art the same—These words can be said of no being but God: they assert the absolute, unchanging self-existence of him who is addressed. Thy years shall not fail—there is no limit, no end, to his duration. He who made all things stands outside their transience; he is the same before they existed, through their changes, and beyond their dissolution.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "John Wesley's Notes",
                    "html": "<p>As a mantle—with all ease. They shall be changed—into new heavens and a new earth. But thou art eternally the same. The dissolution of the present order is not destruction but transformation; but the Son undergoes no such transformation—he is the immutable ground on which all change rests.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "13": {
            "synthesis": "<p>The final quotation seals the argument: \"But to which of the angels said he at any time, Sit on my right hand, until I make thine enemies thy footstool?\" (Ps 110:1). No angel was ever so addressed; the Son alone received this invitation. Calvin notes the theological importance of Psalm 110 beyond the session: the Psalm establishes Christ as both king and priest in one person, since it was not lawful for kings in Israel to touch the priesthood—the Psalm therefore introduces a new and unique office that no angelic being shares. Ellicott calls Psalm 110 \"that Psalm\"—the Messianic psalm quoted in the New Testament more frequently than any other—and observes that the session at God's right hand is the single image that recurs throughout the New Testament as the summary of the Son's exaltation. Clarke connects the point to the cumulative argument: the Jews conceded that if Christ could be shown greater than the angels, his divinity was established—these seven quotations together accomplish precisely that. Barnes emphasizes the specific honor implied by the invitation: no angel was ever asked to sit; they all stand in service. The verb \"until\" projects the Son's reign forward toward the final subjugation of all enemies, completing the Christological picture.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>He again by another testimony extols the excellency of Christ. The passage is taken from Psalm 110:1, and it cannot be explained of any but of Christ. As it was not lawful for kings to touch the priesthood, and as neither David nor any of his successors was ordained a priest, it follows that a new kingdom and a new priesthood are here introduced—the same person made both king and priest, which no angel is.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>The final appeal is made to that Psalm which more frequently than any other is quoted in reference to Christ, and which is the source of all New Testament references to the Saviour's session at the right hand of God. That it was regularly understood by the Jews of our Lord's time to be a Messianic Psalm is clear both from Matthew 22:43–44 and from the independent notices we possess.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes",
                    "html": "<p>The apostle adduces one other proof of the exaltation of the Son of God above the angels. He asks where there is an instance in which God had addressed any one of the angels, and asked him to sit at his right hand until he should subdue his enemies under him? No such invitation was ever given to any angel—they stand and serve; the Son alone sits and reigns.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "14": {
            "synthesis": "<p>The chapter closes with a rhetorical question that functions as an affirmative declaration: \"Are they not all ministering spirits, sent forth to minister for them who shall be heirs of salvation?\" Angels are <em>λειτουργικὰ πνεύματα</em>—ministering spirits—dispatched to serve the very people for whose salvation the Son has just been shown to be incomparably superior. Calvin draws the contrast cleanly: the eminence implied in \"ministering\" is real, but it is the eminence of a servant, not of a lord. Ellicott notes the rhetorical inversion: verses 7–9 contrasted angel-servants with the Son-God, and now verses 13–14 repeat the contrast in reverse order, closing the ring—the Son reigns, the angels minister for those who will inherit what the Son has secured. Clarke reads the interrogative as the Hebrew idiom of the strongest affirmative: \"They are all ministering spirits\"—there is not one exception, however exalted. Wesley adds that the angels serve \"in numerous offices of protection, care, and guidance\" for the heirs of salvation. Barnes concludes: not one angel is elevated to the high rank of the Redeemer—even the most exalted angel is employed in the comparatively humble office of serving those whom the Son has redeemed.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>That the comparison might appear more clearly, he now mentions what the condition of angels is. For calling them ministering spirits he denotes their eminence; but in this respect they are superior to us only that they may minister to our salvation. The dignity of angels is real; but it is the dignity of servants sent to serve the heirs of salvation, not of lords seated at the right hand.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>In this verse and the preceding is repeated the contrast of verses 7–9, in reversed order. The words \"ministering spirits\" at once recall verse 7; the \"heirs of salvation\" are the \"many sons\" whom the Son will bring to glory (2:10). Angels are sent to serve those who will inherit what the Son has secured—their ministry is in behalf of the redeemed, not above them.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p>Are they not all ministering spirits?—The Hebrews often express the strongest affirmative by an interrogation. All the angels, of whatever order, are no more than ministering spirits—they are all employed in the service of God for the benefit of mankind, and particularly for the heirs of salvation. Not one is exempted from this service, however exalted in rank.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes",
                    "html": "<p>There is not one of them that is elevated to the high rank of the Redeemer. Even the most exalted angel is employed in the comparatively humble office of ministering to those who shall be heirs of salvation. They are sent forth—commissioned, dispatched—to serve in behalf of those for whom the Son has obtained eternal redemption.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        }
    },
    "2": {
        "1": {
            "synthesis": "<p>Chapter 2 opens with the first of several pastoral pauses in the epistle's argument. Having established the Son's incomparable superiority to angels, the author draws the practical inference: \"Therefore we ought to give the more earnest heed to the things which we have heard, lest at any time we should let them slip.\" The <em>therefore</em> is weight-bearing—the greater the revealer, the greater the obligation to attend. Calvin states the logic with precision: if the Law given through angels was inviolable and demanded compliance, the Gospel given through the Son demands immeasurably more. Ellicott notes that the object of attention is \"the things heard\"—<em>τοῖς ἀκουσθεῖσιν</em>, the word itself—not merely \"what we have heard\" as a past event, but the ongoing content of the revelation. Wesley offers the sharpest rendering of the danger: \"let them slip\" translates a Greek word (<em>παραρρυῶμεν</em>) that literally means to flow past, as water out of a leaky vessel—the gospel may not be actively rejected, but simply allowed to drain away through neglect. Barnes identifies the \"things heard\" as the great salvation that Christ has brought, and calls neglect of it the specific sin the epistle is warning against—not apostasy in the sense of renunciation, but the fatal drift of inattention.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>He now declares what he had before in view, by comparing Christ with angels, even to secure the highest authority to his doctrine. For if the Law given through angels could not have been received without being obeyed—and transgression was visited with just punishment—how much more must the Gospel command our obedience, since it comes through the Son himself?</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>Better, <em>to the things heard</em>; for this expression contains the complement of the thought of 1:1. Both \"spoken\" and \"heard\" carry the weight of the argument: the God who spoke through prophets and finally through his Son has addressed men, and men have heard; the danger is not active rejection but passive drift—allowing what was heard to flow past unheeded.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "John Wesley's Notes",
                    "html": "<p>Lest we should let them slip—as water out of a leaky vessel. So the Greek word properly signifies. The image is not of deliberate rejection but of gradual loss: the gospel, if not received and held with earnest attention, drains quietly away, leaving nothing behind.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "2": {
            "synthesis": "<p>The comparison that drives the warning is stated plainly: if the word spoken \"through angels\"—the Mosaic law—was firm (<em>βέβαιος</em>), and every transgression and disobedience received a just recompense, then how much more does the greater revelation demand compliance? Ellicott clarifies the preposition: the law was not spoken \"by\" angels as its authors but \"through\" angels as the medium—the word remained God's word, delivered via angelic intermediaries. Clarke documents this as established Jewish tradition, citing Acts 7:53 and Galatians 3:19 alongside Josephus, who explicitly records the Jewish understanding that the law came through angelic mediation. Wesley sharpens the vocabulary: \"transgression\" is the commission of sin, \"disobedience\" is the omission of duty—the penalty attached to both. Barnes adds that the Mosaic law's inviolability was the premise everyone accepted; the author is not arguing for it but reasoning from it. Robertson notes the verse states a first-class conditional (assumed true): the stability of the law under angelic administration is the established ground from which the a fortiori argument to the gospel proceeds.</p>",
            "voices": [
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>The word spoken <em>through</em> angels—the word was God's, but angels were the medium through which it was given to men. In accordance with the tone of the whole Epistle, the divine origin of both revelations is assumed; what distinguishes them is the dignity of the mediators through whom they came: angels for the Law, the Son for the Gospel.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p>The law, according to some, was delivered by the mediation of angels, God frequently employing these to communicate his will to men. See Acts 7:53 and Galatians 3:19, where this tradition is explicitly cited. Josephus records that the Jews had their most excellent doctrines and the holiest part of their law delivered to them through angels. This premise grounds the whole comparative argument.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "John Wesley's Notes",
                    "html": "<p>In giving the law, God spoke by angels; but in proclaiming the gospel, by his Son. Steadfast—firm and valid. Every transgression—commission of sin. Every disobedience—omission of duty. Both received a just recompense: the law's sanctions were exact and comprehensive, touching both what was done and what was left undone.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "3": {
            "synthesis": "<p>The comparative logic is now pressed to its conclusion in a rhetorical question: \"How shall we escape, if we neglect so great a salvation?\" Calvin draws the sharpest possible edge: it is not only the rejection of the gospel that incurs the heaviest punishment, but even its neglect—inattention to saving grace is itself a gravity-defying act, given the magnitude of what is offered. Wesley unpacks \"so great a salvation\" as deliverance from so great a wickedness and misery, into so great a holiness and happiness—the adjective \"great\" carries the full weight of the gospel's scope. Ellicott notes that the question here is not how transgressors of the law shall escape, which was the concern of chapter 1's quotations; it is how those who simply let this salvation pass without attention shall escape—the reference is specifically to neglect, not to dramatic apostasy. Barnes reads the question as practically unanswerable: there is no alternative refuge, no other mediator, no second gospel. The author also anchors the salvation in its historical origin: first spoken by the Lord himself, then confirmed to his hearers, the message has an unbroken chain of attestation that neglect cannot survive.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>Not only the rejection of the Gospel, but also its neglect, deserves the heaviest punishment, and that on account of the greatness of the grace which it offers. God would indeed leave unpunished no one who violated the law; much less will he suffer unpunished those who tread underfoot the blood of the covenant. The argument moves from the lesser to the greater with inexorable logic.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "John Wesley's Notes",
                    "html": "<p>So great a salvation—a deliverance from so great wickedness and misery, into so great holiness and happiness. This was first spoken of—before he came it was not known—by him who is the Lord of all, angels and men; and was confirmed to us by them that heard him—the apostles and original eyewitnesses who could verify what they had personally received from Christ.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes",
                    "html": "<p>How shall we escape? What way is there of being saved from punishment, if we suffer the great salvation to be neglected, and do not embrace it? There is no alternative. If there were some other way of salvation—some other gospel, some second opportunity—the question could be answered; but there is none. The force of the question lies in the absolute absence of any escape route outside of this salvation.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "4": {
            "synthesis": "<p>The divine authentication of the gospel is specified: God himself bore witness to the apostolic message \"with signs and wonders, and with divers miracles, and gifts of the Holy Ghost, according to his own will.\" Calvin reads this as God's solemn subscription to the preaching of the apostles: the miracles were not the apostles' own credentials but God's endorsement of their message. Ellicott cites Mark 16:20 as a close parallel—\"they went out and preached everywhere, the Lord working with them and confirming the word with signs following\"—and emphasizes that the attestation was given not to the messengers as individuals but to the truth they proclaimed. Clarke reads the verse as God refusing to leave the confirmation of these great truths to human testimony alone: he added his own testimony through signs, wonders, miracles, and the distribution of the Spirit. Wesley distinguishes the timing: signs were given while Christ himself lived; the diverse gifts of the Holy Spirit were distributed after his exaltation. Barnes makes the theological point: miracles are inherently impossible for a human being acting by his own power; when the dead are raised or nature is interrupted, God alone can be the cause—miracles therefore constitute divine certification of the message.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>The Lord proved his approbation of the apostolic preaching by miracles, as by a solemn subscription. Then they who will not obey the Gospel have no excuse, because God himself has confirmed it. The miracles were not the apostles' own works but God's own endorsement, making the word not merely credible but divinely authenticated.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>God also bearing witness with them—bearing witness together with the apostles—to the truth they preached. Mark 16:20 is a striking parallel. The divine attestation was given by miracles and gifts of the Holy Ghost—not as signs of the messengers' authority, but as confirmations of the message itself. \"According to his own will\"—the distribution was sovereign, not automatic.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes",
                    "html": "<p>God bearing them witness by miracles—giving them the sanction of his authority, showing that they were sent by him. No man can work a miracle by his own power. When the dead are raised or the blind receive sight, God alone can be the cause; miracles therefore bear the divine seal upon the message they accompany. The verse closes the argument: the gospel is attested by the Son, by eyewitnesses, and by God himself.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "5": {
            "synthesis": "<p>Having completed the first pastoral application (vv. 1–4), the author returns to the argument of chapter 1: not to angels has God subjected the world to come. The phrase \"world to come\" (<em>οἰκουμένη μέλλουσα</em>) is the key. Clarke documents that among the Jews <em>olam habba</em>, \"the world to come,\" consistently denoted the Messianic age—the era inaugurated by the Messiah's coming, not merely the afterlife. Ellicott connects the verse directly to 1:14: angels are ministering spirits who serve the heirs of salvation; dominion over the new age was never entrusted to them. Calvin makes the point from the Father's side: it is the Father who has conferred the sovereignty of the whole world on Christ, while angels are wholly destitute of such honor; this is another argument—additional to the seven scriptural proofs—that the Son is superior. Barnes notes that this verse explicitly resumes the superiority theme from chapter 1, making clear that the pastoral warning of verses 1–4 was a parenthesis and that the argument about Christ's supremacy now continues at a deeper level. The author will now prove that the Son's temporary humiliation below the angels (Ps 8) does not contradict but confirms this sovereignty.</p>",
            "voices": [
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p>The world to come—that <em>עולם הבא olam habba</em>, the world to come, meant the days of the Messiah among the Jews is most evident and has been often pointed out. This world to come, this Messianic age, God has not put in subjection to the angels but to the Messiah himself—another proof, from sovereignty over the new creation, of the Son's supremacy over all angelic powers.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>There is a very clear connection between this verse and 1:14. \"Angels are but ministering spirits, serving God in the cause of those who shall inherit salvation; for not to angels is the world to come subjected.\" Their ministry is for heirs, not as rulers; the dominion over the coming age belongs to another—to the one who is both Son and Heir of all things.</p>"
                },
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>He again proves by another argument that Christ ought to be obeyed; for the Father has conferred on him the sovereignty of the whole world, while the angels are wholly destitute of such an honor. It was a mark of singular honor to be made the Lord of all. This honor was given to Christ and to Christ alone; not one of the angels was ever admitted to share it.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "6": {
            "synthesis": "<p>The author introduces Psalm 8 with characteristic vagueness: \"But one in a certain place testified.\" Ellicott notes this \"somewhere\" construction as a deliberate literary mannerism—the author trusts his readers to know the Scriptures and does not need to cite chapter and verse. Clarke identifies the \"one\" as David and the \"certain place\" as Psalm 8:4–6. The quotation asks: \"What is man, that thou art mindful of him? or the son of man, that thou visitest him?\" Wesley reads the Psalm as composed on a clear, moonlit night as David contemplated the vastness of the heavens over against the smallness of humanity—the contrast between cosmic grandeur and human dignity that the Psalm then surprisingly resolves in favor of human significance. Barnes notes that writing to readers steeped in the Hebrew Scriptures, the author needed only to gesture at a familiar passage; they would supply the context. Robertson identifies the verb form as the perfect tense used by the author throughout for Scripture quotations—<em>διεμαρτύρατο</em>, \"has testified,\" with the permanent authority of divine witness.</p>",
            "voices": [
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>Better, <em>somewhere.</em> The expression is perfectly indefinite; the author assumes his readers know the Scriptures and requires only a gesture toward the familiar text. As a rule, the words of Scripture are in this Epistle quoted as God's own utterances, and here David's words in Psalm 8 are brought forward as a divine testimony about the dignity and destiny of man—and ultimately of the Son of Man.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p>But one in a certain place—this one is David; and the certain place is Psalm 8:4, 5, 6. The apostle uses this indeterminate mode of quotation because it was common thus to cite Scripture among the Jews when the reference was obvious; the readers were assumed to be thoroughly familiar with the text and its Messianic implications.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "John Wesley's Notes",
                    "html": "<p>What is man—to the vast expanse of heaven, to the moon and the stars which thou hast ordained? This Psalm seems to have been composed by David, in a clear moonshiny and starlight night, while he was contemplating the glorious works of God. The smallness of man contrasted with the grandeur of creation makes the divine attention to him all the more astonishing—and the promised dominion all the more remarkable.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "7": {
            "synthesis": "<p>The Psalm's first clause—\"Thou madest him a little lower than the angels\"—raises both a textual and an interpretive question. The Hebrew reads <em>meelohim</em>, \"lower than God\" (or \"the divine beings\"), while the LXX renders it \"lower than the angels.\" Clarke notes this divergence: if the Psalm is about Adam, the Hebrew may mean God himself; if about the Messiah, it anticipates the incarnation's lowering below the angels. Wesley reads the Psalm first as about Adam, who was made \"next to God, the highest of all creatures,\" then as applied by the author to Christ in his incarnation. Calvin argues that in the Psalm itself \"a little lower\" denotes degree of dignity, while the author of Hebrews interprets the phrase temporally when applying it to Christ—as a brief period of humiliation during his earthly life and death. Ellicott connects the verse directly to 2:9, where \"a little\" is more naturally read as degree. Barnes sees the phrase as indicating both a slight diminution in rank (the incarnate Son below angels in dignity) and an enduring description of Christ's assumption of human nature. Robertson notes the LXX Septuagint's substitution of \"angels\" for \"God\" (<em>Elohim</em>) and regards it as divinely providential for this application.</p>",
            "voices": [
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p>We must have recourse to the original: <em>vattechasserehu meat meelohim</em>. If this be spoken of Adam, and <em>elohim</em> be God, then the meaning is that man was made but a little inferior to God himself—the highest of all God's earthly creatures. If applied to Christ, the LXX rendering \"angels\" fits the argument: he took on human nature and was thereby placed, in his state of humiliation, below the angelic order.</p>"
                },
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>The meaning of <em>βραχύ τι</em> is ambiguous—it can mean \"little\" in degree or \"little\" in time. In the Psalm the former meaning is evident; but the Apostle applies it to Christ's incarnation, where the temporal sense also fits: for a little while he took on a nature inferior to that of angels. The inferiority is real, not merely nominal—he truly descended below them in condition.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes",
                    "html": "<p>Thou madest him a little lower than the angels—a little inferior in rank, or inferior for a little time. The Greek may mean either. The probable meaning in the Psalm is \"a little in degree\"; but the application in verse 9 shows the author takes it also as temporal—Christ was made lower than the angels for a brief period, in order to suffer death, and is now exalted above them.</p>"
                }
            ],
            "consensus": "mixed",
            "key_tension": "The Psalm can be read as primarily about Adam/humanity, with Christ as the ultimate fulfillment (Clarke, Wesley), or as directly Messianic (Calvin, the author of Hebrews); and 'a little lower' can mean a small degree of inferiority (Calvin in the Psalm) or a brief duration of humiliation (the author's application to Christ's incarnation and passion)."
        },
        "8": {
            "synthesis": "<p>The Psalm continues: \"Thou hast put all things in subjection under his feet.\" The claim is total—nothing is excluded from the promise. But the author immediately notes the gap between promise and present reality: \"But now we see not yet all things put under him.\" This tension between the promise's comprehensiveness and the visible incompleteness of its fulfillment is the rhetorical engine of the paragraph. Calvin's exegetical argument is sharp: the Psalm says \"all things\" are subjected to \"man,\" but universal dominion is obviously not given to the human race as such—it must therefore refer to one specific man in whom the whole promise is gathered. Ellicott notes the author's studious repetition of the key word \"subjected\" (<em>ὑπέταξας</em>) three times in the verse, underlining the completeness of the divine intention. Barnes reads the verse as acknowledging honestly that the fulfillment is not yet visible in human experience—the world does not appear to be under human dominion—but the \"not yet\" implies a coming fulfillment. Robertson observes that the aorist <em>ἀφῆκεν</em>, \"he left nothing unsubjected,\" is a decisive word: the grant was total; the incompleteness is in the visible realization, not in the original appointment.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>One might think the argument to be this—\"To the man whom David speaks, all things are subjected; but to mankind all things are not made subject; then it is some one man of whom the Psalmist speaks.\" This is indeed the Apostle's argument. The universal promise of the Psalm cannot fit the human race in general; it must point to one person who truly holds all things under him.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>There is in the Greek a studious repetition of the leading word, which should not be lost: \"Thou didst subject all things under his feet. For in subjecting all things to him, He left nothing unsubjected to him. But now we see not yet all things subjected to him.\" The repetition underlines the total scope of the divine intention—even though the realization in history is as yet incomplete.</p>"
                },
                {
                    "src": "rwp",
                    "attr": "Robertson's Word Pictures",
                    "html": "<p>He left nothing unsubjected (<em>ἀφῆκεν</em>)—first aorist active indicative; the grant was total. The contrast between the comprehensiveness of the promise and the incompleteness of its present realization sets up the argument of verse 9: we do not see man triumphant, but we do see Jesus, in whom the promise has already been fulfilled in principle through his death and exaltation.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "9": {
            "synthesis": "<p>\"But we see Jesus\"—these three words are the theological pivot of the chapter. The promised dominion is not yet visible in humanity generally, but it is visible in one man: Jesus, who was made a little lower than the angels for the suffering of death, and has now been crowned with glory and honor. The author makes explicit what the Psalm implies: Christ's temporary humiliation was not a defeat but the path to his crowning. Calvin insists that \"a little lower\" here denotes degree—Christ took on a nature genuinely inferior to the angels in order to suffer and die, since angels cannot die. Wesley reads the crown as specifically a reward for the suffering of death—Christ is crowned with glory and honor as the recompense for his cross. Ellicott carefully notes that the purpose clause \"that he might taste death for every man\" is better connected to \"crowned\" than to \"made lower\"—God's grace ordained the cross as the means to the crown, and the crown vindicates the cross. Barnes focuses the exegesis: the point is not that he suffered, but that on account of suffering, he was crowned—the Psalm's promise of dominion is fulfilled precisely in the one who went lowest. Robertson adds the existential sharpness: \"death has defeated man, but Jesus has conquered death.\"</p>",
            "voices": [
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>But we see Him who has been made a little lower than angels, Jesus, because of the suffering of death crowned with glory and honour. There is One in whom the divine purpose is fulfilled in all its parts. He was made a little lower than angels, and He is crowned with glory. In one point we note an apparent departure from the Psalm: words which there denote dignity here denote humiliation—yet in each case it is the position of the Son of Man that is described.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "John Wesley's Notes",
                    "html": "<p>It is done only with regard to Jesus, God-Man, who is now crowned with glory and honour—as a reward for his having suffered death. He was made a little lower than the angels, who cannot either suffer or die. That by the grace of God he might taste death—an expression denoting both the reality of his death, and the shortness of its continuance. For every man—that ever was or will be born into the world.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes",
                    "html": "<p>\"We do not see that man elsewhere has the extended dominion of which the Psalmist speaks. But we see the fulfillment of it in Jesus, who was crowned with glory and honour.\" The object of the apostle is to show that Jesus has received a dominion superior to that of the angels—and he received it through the suffering of death. The crown came by the cross; the exaltation came through humiliation.</p>"
                },
                {
                    "src": "rwp",
                    "attr": "Robertson's Word Pictures",
                    "html": "<p>We do not see man triumphant, but we do see Jesus, realizing man's destiny—\"the very one who has been made a little lower than the angels.\" Death has defeated man, but Jesus has conquered death. Because of the suffering of death (<em>διὰ τὸ πάθημα τοῦ θανάτου</em>)—the causal sense; it was precisely the suffering of death that led to the crown of glory.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "10": {
            "synthesis": "<p>The author now steps back and affirms the fitness of the whole arrangement: \"For it became him, for whom are all things, and by whom are all things, in bringing many sons unto glory, to make the captain of their salvation perfect through sufferings.\" The word <em>ἔπρεπεν</em>—\"it was becoming, fitting, seemly\"—is a strong word of divine propriety: God's own character required this path. Calvin opens with the pastoral intention behind the verse: he writes to make Christ's humiliation appear glorious, not shameful, to the godly. The cross could seem to disqualify the Savior from his office; the author shows it is in fact his credential. Ellicott reads the verse as answering the Jewish incredulity at a suffering Messiah: what seemed unthinkable was divinely ordained, and the fitness of the ordination is shown by the character of the one who ordained it—God himself, for whom and through whom all things exist. Clarke distills the logic: without suffering there is no death; without death there is no atonement; without atonement there is no completed priestly work. Wesley connects the verse to the language of Psalm 8: he is bringing many adopted sons to glory—the very dominion promised in the Psalm is being fulfilled in the Captain who precedes his people to the promised destination.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>His object is to make Christ's humiliation appear glorious to the godly; for when he is said to have been clothed with our flesh, he seems to be classed with the common order of men; and the cross brought him lower than all men. The Apostle shows that this very thing ought to be deemed honorable: it was the means by which he was consecrated the Captain of our salvation, and no other path would serve.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>What seemed to Jews incredible—that the Christ should die—was ordained by the grace of God. For thus to make sufferings the path to His kingdom was worthy of God, for whose glory and through whose power all things exist. God cannot but do that which will subserve His glory; and a suffering, dying Savior, perfected through suffering, subserves it supremely.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p>For it became him—it was suitable to the Divine wisdom, the requisitions of justice, and the economy of grace, to offer Jesus as a sacrifice in order to bring many sons and daughters to glory. Without suffering he could not have died, and without dying he could not have made an atonement for sin. The sacrifice must be consummated before the Captain could lead his people home.</p>"
                },
                {
                    "src": "rwp",
                    "attr": "Robertson's Word Pictures",
                    "html": "<p>It became him (<em>ἔπρεπεν αὐτῷ</em>)—imperfect active of <em>πρέπω</em>, to be becoming or seemly; impersonal here. The voluntary humiliation or incarnation of the Son—made a little lower than angels—was a seemly thing to God the Father. One has only to recall John 3:16 to get the idea. This great passage (2:10–18) is worthy to stand beside Philippians 2:5–11.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "11": {
            "synthesis": "<p>\"For both he that sanctifieth and they who are sanctified are all of one: for which cause he is not ashamed to call them brethren.\" The verse asserts a profound unity between the Son and those he came to save—a unity so deep that he publicly acknowledges them as his own family. The crux is the phrase \"of one\" (<em>ἐξ ἑνός</em>): one what? Ellicott, Clarke, and Wesley all read this as \"of one Father\"—the unity that makes the Son unashamed is not primarily shared human nature but the divine family relationship under God as Father of all. Calvin, while not contradicting this, emphasizes the connection between Christ and his members as the reason why the incarnation was necessary: Christ is bound to those he sanctifies by the deepest unity, which required that he take their condition upon himself. Clarke notes that <em>ὁ ἁγιάζων</em> (\"the one who sanctifies\") carries not only the meaning of making holy but also of making atonement, so that the verse encompasses both Christ's priestly and sanctifying work. Barnes reads the verse as establishing the union between Christ and his people that grounds the whole chapter's argument about the incarnation: because of this union, he was obligated by love and by the nature of the redemption to become what his people are.</p>",
            "voices": [
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>The special meaning of \"sanctify\" in this Epistle seems to be bringing into fellowship with God—being reconciled and consecrated to him. \"Of one\"—not of one common humanity, but of one Father; the unity that underlies Christ's willingness to call them brethren is ultimately the divine family bond, God's fatherhood over both the Son and the redeemed.</p>"
                },
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>He proves that it was necessary that what he had said should be fulfilled in the person of Christ on account of his connection with his members; and he also teaches that it was a remarkable evidence of divine grace, that the Son of God was not ashamed to call us his brethren. For it is a remarkable instance of condescension that he who excels all the angels calls us brethren.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p>The word <em>ὁ ἁγιάζων</em> does not merely signify one who sanctifies or makes holy, but one who makes atonement or reconciliation to God. And they who are sanctified—that are brought to God; that draw near or come to him. They are all of one—of one Father; this is the most natural and consistent sense. He is not ashamed to call them brethren—so intimate and real is the family bond he has entered.</p>"
                }
            ],
            "consensus": "mixed",
            "key_tension": "The phrase 'of one' (ἐξ ἑνός) is read by Ellicott, Clarke, and Wesley as 'of one Father'—emphasizing the divine family relationship—while Calvin emphasizes the connection as grounded in the unity between Christ and his members, which required their shared humanity and condition."
        },
        "12": {
            "synthesis": "<p>To prove that the Son calls his people brethren, the author cites Psalm 22:22: \"I will declare thy name unto my brethren, in the midst of the church will I sing praise unto thee.\" The Psalm is one of the most directly Messianic in the Psalter—it opens with the cry of dereliction (\"My God, my God, why hast thou forsaken me?\") that Jesus quoted from the cross, and it closes with praise in the midst of the assembly. Calvin notes that the Apostle changes the Septuagint verb from <em>διηγήσομαι</em> to <em>ἀπαγγελῶ</em>—a synonym, but one that includes the idea of announcement; the Psalm words are placed in the mouth of Christ speaking to the Father about what he will do among his redeemed community. Ellicott reads the citation as choosing the verse that clinches the argument: Christ himself, in the Messianic Psalm that describes his suffering, already anticipates his work of declaring the Father's name to those he will call brethren. Clarke identifies this as Christ speaking to the Father in reference to his incarnation and ongoing ministry. Barnes notes that Psalm 22's Messianic reference is among the least disputed in the Old Testament and that <em>ἐκκλησία</em>—here translated \"church\"—is the congregation of the redeemed in which Christ himself sings.</p>",
            "voices": [
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>The quotation is taken from the 22nd verse of Psalm 22—a Psalm remarkable for its close connection with the narrative of the crucifixion and resurrection. The Messiah is presented as speaking to his brethren in the midst of the congregation, declaring the Father's name and leading the praise. This confirms that he who suffered is the same who now leads the worship of the redeemed family.</p>"
                },
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>This quotation is made from Psalm 22:22, from the Septuagint, except that the Apostle changes <em>διηγήσομαι</em> into <em>ἀπαγγελῶ</em>. The words are placed in the mouth of Christ speaking to the Father: I will declare thy name to my brethren—those united to me—in the midst of the church will I sing praise. The risen Christ is not ashamed of his family; he leads their worship.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes",
                    "html": "<p>This passage is found in Psalm 22:22. The whole of that Psalm has been commonly referred to the Messiah, and in regard to such a reference there is less difficulty than attends most OT quotations. The word <em>ἐκκλησία</em>—\"congregation\" or \"church\"—is the gathering of all those who have been brought into the family of God through the one who both suffered and now sings.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "13": {
            "synthesis": "<p>Two further scriptural quotations are added to demonstrate the Son's solidarity with his people. The first—\"I will put my trust in him\"—is drawn from Psalm 18:2 or its parallel in 2 Samuel 22:3 (or possibly Isaiah 8:17). The second—\"Behold I and the children which God hath given me\"—is explicitly from Isaiah 8:18, where the prophet and his children were themselves signs pointing forward to the Messiah. Calvin reads the first quotation as placing Christ in the company of those who trust God through suffering—he took on not only human flesh but the whole experience of human dependence and faith. Wesley reads both quotations together as expressing the Messiah's communion with his brethren: he trusts in God alongside them and presents them to the Father as those given to him. Ellicott notes that the second citation (Isa 8:18) is the more certain of the two—the prophet and his children as living signs of God's word—and that applied to Christ it shows him presenting his redeemed family to the Father as those who are given to him as the completion of his mediatorial work. Barnes observes that both quotations show Christ partaking of the feelings of humanity: the trust that he exercised, the family that he gathered, belong to the incarnate experience of the Son who was made like his brethren in all things.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>As this sentence is found in Psalm 18:2 or 2 Samuel 22:3, it was probably taken from one of those places. The words are placed in the mouth of Christ as the head together with his members; he shows that he partook of the same condition of trust and dependence, and suffered through the same experiences, in order that he might be in all things made like unto his brethren.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>Of the two passages cited, the latter is certainly from Isaiah 8:18; the former might be derived from 2 Samuel 22:3 or Psalm 18:2. The prophet and his children were themselves signs and wonders in Israel—living embodiments of God's word. Applied to Christ, the words present him before the Father with those given to him: <em>Behold I and the children which God hath given me.</em></p>"
                },
                {
                    "src": "wesley",
                    "attr": "John Wesley's Notes",
                    "html": "<p>And again—as one that has communion with his brethren in sufferings as well as in nature, he says, I will put my trust in him—to carry me through them all. And again—with a like acknowledgment of his close union with his brethren, he says, Behold I and the children which God hath given me—presenting them all to the Father as those entrusted to his keeping.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "14": {
            "synthesis": "<p>With the solidarity now established by Scripture, the author draws the conclusion: since the children share in flesh and blood, he himself likewise took part of the same—and he did so for a specific purpose: that through death he might destroy him who had the power of death, that is, the devil, and deliver those who through fear of death were subject to lifelong bondage. Calvin notes the inference from the foregoing: the Son of God became man so that he might partake the same nature and condition as his people, and that by undergoing death he might redeem them from it. The argument is tight: only a being who can die can conquer death; since the children are mortal, the savior must be mortal; so he became mortal in order to destroy mortality's lord. Ellicott sees verses 14–15 as directly recalling 2:9 and 2:10: the grace of God ordained the cross as the means to dominion, and the specific target of that cross was the power behind death—the devil. Wesley reads \"destroy\" as destroying the <em>tyranny</em> of the devil—not annihilating the devil as a being, but stripping him of his power over those who are reconciled to God. Robertson supplies the Greek: <em>καταργήσῃ</em>—to render powerless, to put out of commission—rather than to annihilate; the devil's power over death has been broken, not his existence ended.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>\"The Son of God became man that he might partake of the same condition and nature with us.\" What could be more fitted to confirm our faith? He who is the Lord of death undertook death in order to destroy it. The passage deserves especial notice, for it not only confirms the reality of the human nature of Christ, but also shows the benefit which flows to us from his taking that nature.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>The two members of this verse directly recall 2:10 and 2:9. It was the will of God that salvation should be won by the Son for sons; and this salvation could only be won by means of death. The children share flesh and blood; the Savior must therefore share flesh and blood—and his death, by destroying the one who wielded death as a weapon, becomes the instrument of their liberation.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "John Wesley's Notes",
                    "html": "<p>He also in like manner took part of the same; that through his own death he might destroy the tyranny of him that had, by God's permission, the power of death with regard to the ungodly. Death is the devil's servant and sergeant, delivering to him those whom he seizes in sin. By dying, Christ overthrew the officer and broke the chain.</p>"
                },
                {
                    "src": "rwp",
                    "attr": "Robertson's Word Pictures",
                    "html": "<p>That he might bring to nought (<em>ἵνα καταργήσῃ</em>)—first aorist active subjunctive of <em>καταργέω</em>, to render inactive, to put out of commission. This is not annihilation but the breaking of power. The devil's authority over death has been stripped away by the one who passed through death and came out the other side as Lord of both the living and the dead.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "15": {
            "synthesis": "<p>The deliverance won through Christ's death has a specific object: those who through fear of death were all their lifetime subject to bondage. The universality of that bondage, and its precise nature, is read differently by the commentators. Calvin presses the sharpest application: those who fear death look at it apart from Christ, and what they see is a terrible abyss—nothing but a harbinger of divine judgment. The fear is rational, given the fallen condition, and the slavery is total: every aspect of life is shadowed by what lies at its end. Wesley agrees with the universal scope—\"every man who fears death is in a slavish, uncomfortable state\"—and holds that this describes the universal pre-Christian human condition. Clarke, however, places the primary reference with the Gentiles: lacking revelation and any certainty of resurrection or immortality, they were trapped in a bondage to death that the Jews, with their Scriptures, did not fully share. Ellicott reads the verse with pastoral sympathy, suggesting that the author's words were prompted by intimate knowledge of what this fear actually feels like. Barnes draws out both dimensions of the deliverance: Christ frees his people from the dread of death as a present experience, and from death itself in the final sense.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>This passage expresses in a striking manner how miserable is the life of those who fear death, as they must feel it to be dreadful because they look on it apart from Christ; for then nothing but a terrible abyss is open before them. The fear of death is not irrational in the unconverted; it is the recognition of a real and unresolved debt. Christ comes to break that bondage by paying what is owed.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "John Wesley's Notes",
                    "html": "<p>And deliver them, as many as through fear of death were all their lifetime, till then, subject to bondage—every man who fears death is subject to bondage; is in a slavish, uncomfortable state. And every man, who is not delivered therefrom, has this fear more or less, though he may not be sensible of it.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p>It is very likely that the apostle has the Gentiles here principally in view. As they had no revelation, and no certainty of immortality, they were in bondage through fear of death all their life. The Epicureans tried to reason away this fear; the Stoics tried to suppress it; but neither school could break the bondage that only the resurrection of Christ dissolves.</p>"
                }
            ],
            "consensus": "mixed",
            "key_tension": "Clarke reads the lifelong bondage to the fear of death as primarily describing the Gentiles who lacked the light of revelation and had no certainty of resurrection, while Calvin and Wesley see it as the universal condition of all who have not yet grasped Christ's victory over death."
        },
        "16": {
            "synthesis": "<p>\"For verily he took not on him the nature of angels; but he took on him the seed of Abraham.\" This familiar rendering of the KJV actually obscures the Greek, as Ellicott, Clarke, and Barnes all point out. The verb <em>ἐπιλαμβάνεται</em> does not mean \"to take on a nature\" but \"to take hold of, to lay hold of, to help or rescue.\" The verse is not about the mode of the incarnation but about its beneficiaries: Christ does not extend his rescuing hand to angels but to the seed of Abraham. Calvin, reading with the traditional sense, sees the verse as enhancing the honor of the incarnation: Christ never stooped so low for angels as he stooped for fallen humanity. Clarke quotes the Greek directly: <em>οὐ γὰρ δήπου ἀγγέλων ἐπιλαμβάνεται, ἀλλὰ σπέρματος Ἀβραὰμ ἐπιλαμβάνεται</em>—\"He does not at all take hold of angels; but of the seed of Abraham he takes hold.\" Barnes agrees: the metaphor is of a rescuer stretching out a hand to save someone who is in danger, and the point is that Christ reached out for the seed of Abraham, not for fallen angels. Robertson connects the verb to <em>βοηθῆσαι</em> in verse 18—to help, to succor—confirming the sense of active assistance rather than assumption of nature.</p>",
            "voices": [
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>He took not on him the nature of angels—the rendering of the margin approaches the true meaning far more closely: <em>He taketh not hold of angels, but of the seed of Abraham he taketh hold.</em> The verb means to take hold of in order to help; the sentence is not about which nature Christ assumed but about whom he came to rescue. He came for Abraham's seed, not for fallen angels.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p><em>Οὐ γὰρ δήπου ἀγγέλων ἐπιλαμβάνεται, ἀλλὰ σπέρματος Ἀβραὰμ ἐπιλαμβάνεται</em>—Moreover, he doth not at all take hold of angels; but of the seed of Abraham he taketh hold. The image is of a rescuer seizing the hand of one in danger. Christ stretched out his saving hand not to fallen angels but to the heirs of the Abrahamic promise.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes",
                    "html": "<p>The word here used—<em>ἐπιλαμβάνεται</em>—means to take hold of, to lay hold upon for help, rescue, or support. The figure is that of a rescuer stretching out a hand; not of someone putting on another's clothing. The verse declares that Christ's rescuing work is directed toward the seed of Abraham—the heirs of the promise—and not toward fallen angels.</p>"
                }
            ],
            "consensus": "mixed",
            "key_tension": "The KJV 'took not on him the nature of angels' reads ἐπιλαμβάνεται as incarnation language, while Ellicott, Clarke, and Barnes argue that the verb means 'to take hold of in order to help'—making the verse about the beneficiaries of Christ's rescue (Abraham's seed) rather than the mode of the incarnation."
        },
        "17": {
            "synthesis": "<p>The chapter reaches its first climax with the explicit naming of Christ's office: \"Wherefore in all things it behoved him to be made like unto his brethren, that he might be a merciful and faithful high priest in things pertaining to God, to make reconciliation for the sins of the people.\" This is the first explicit mention of the high-priestly theme that will dominate chapters 4–10 of the epistle. The logic of the verse ties together everything that has been argued: the incarnation, the humiliation, the solidarity with human suffering—all of it was obligatory because the work of a high priest requires that he stand fully in the place of those he represents. Ellicott identifies the governing phrase: \"in all things\" goes with \"made like,\" not with \"behoved him,\" and the single exception (sin) does not need to be named here. Calvin distinguishes two elements of the likeness: not only real flesh, but all the affections and feelings proper to humanity. Clarke unpacks \"merciful\" and \"faithful\": merciful means feeling the infirmities of his people, moved by their suffering; faithful means toward God—he performs his priestly office with entire faithfulness to the One he represents before. Wesley reads the verse as a recapitulation of the whole chapter: \"merciful toward sinners; faithful toward God\"—both aspects require the incarnation, and both aspects complete the picture of the perfect high priest.</p>",
            "voices": [
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>Since it is \"the seed of Abraham,\" his brethren, that he would help, he must be made like them in all things—in all respects the single exception is sin (see 4:15). He must be liable to, and must suffer, temptation, sorrow, pain, death. That he might prove—or become—a compassionate and faithful High Priest: merciful in that he has felt what the people feel; faithful in that he serves the God he represents without wavering.</p>"
                },
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>In Christ's human nature there are two things to be considered: the real flesh and the affections or feelings. The Apostle teaches that he had not only put on the real flesh of man, but also all those feelings which belong to man. He shows the benefit that hence proceeds: it is true teaching of faith when we find in Christ the very reason why the Son of God undertook our infirmities.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p>That he might be merciful—<em>ἵνα ἐλεήμων γένηται</em>—that he might be affected with a feeling of our infirmities, that, partaking of our nature with all its innocent afflictions, he might know how to compassionate poor, suffering man. And that he might be a faithful high priest—faithful toward God, doing everything that God required; faithful toward man, interceding for them according to their real need.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "John Wesley's Notes",
                    "html": "<p>Wherefore it behoved him—it was highly fit and proper, yea necessary, in order to his design of redeeming them. To be made in all things like his brethren—this is a recapitulation of all that goes before. That he might be a merciful and faithful High Priest—merciful toward sinners; faithful toward God. Both properties of the perfect high priest require the full incarnation.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "18": {
            "synthesis": "<p>The chapter ends by drawing out the pastoral consequence of the high priest's likeness to his people: \"For in that he himself hath suffered being tempted, he is able to succour them that are tempted.\" The argument is from experience: because Christ has genuinely suffered under the same pressures that bear on his people, he is qualified—not merely willing—to help them. Calvin reads \"being tempted\" as meaning \"being tried by our evils\"—the word <em>πειρασθείς</em> denotes experience, probation, the real encounter with what tests and presses. Ellicott unpacks the chain: through the temptations Christ faced arose opportunities for sin; in resisting them and suffering through them he gained not only sympathy but also knowledge—he knows exactly what help is needed and has the priestly position to provide it. Clarke, appealing to classical sentiment, cites the maxim that those who have endured most affliction feel most for others; Christ's suffering was not incidental to his compassion but constitutive of it. Wesley cuts to the proof: Christ's ability to succor the tempted is a \"manifest, demonstrative proof\"—the fact itself, once grasped, needs no further argument. Robertson notes the perfect tense of <em>πέπονθεν</em> (\"hath suffered\"): the experience of suffering is a permanent part of Christ's history as the exalted Lord, not a past event that has faded. The empathy is not remembered; it is retained.</p>",
            "voices": [
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>The necessity of being \"in all things made like to His brethren\" is now illustrated from the result. Through the temptations arose those conditions which required a High Priest's intercession; and in his having been tempted lies his special ability to help the tempted—by his sympathy, by his knowledge of what help is needed, and by the position of High Priest which he has gained through suffering.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p>A state of suffering disposes persons to be compassionate, and those who endure most afflictions are they who feel most for others. The apostle argues that it was necessary that Jesus Christ should partake of human nature exposed to trials, persecutions, and various sufferings, that he might the better feel for and be led to succour those who are afflicted and sorely tried.</p>"
                },
                {
                    "src": "rwp",
                    "attr": "Robertson's Word Pictures",
                    "html": "<p>Hath suffered (<em>πέπονθεν</em>)—second perfect active indicative; the suffering is a permanent part of Christ's experience. Being tempted (<em>πειρασθείς</em>)—the temptation to escape the Cross was early and repeatedly presented: in the wilderness, through Peter, in Gethsemane. He is able to help (<em>δύναται βοηθῆσαι</em>)—the present tense of ability grounds the ongoing intercession of the exalted High Priest.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "John Wesley's Notes",
                    "html": "<p>For in that he hath suffered being tempted himself, he is able to succour them that are tempted—that is, he has given a manifest, demonstrative proof that he is able so to do. The suffering and the succouring are not two separate things: the suffering through temptation is precisely what equips him to be the helper of the tempted.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        }
    }
}

def main():
    existing = load_synthesis('hebrews')
    merge_synthesis(existing, HEBREWS)
    save_synthesis('hebrews', existing)
    print('Hebrews 1–2 synthesis complete.')

if __name__ == '__main__':
    main()
