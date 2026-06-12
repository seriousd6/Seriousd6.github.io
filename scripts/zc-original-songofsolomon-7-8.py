"""
Job + Proverbs + Ecclesiastes + Song of Solomon — all four layers.
Wisdom books: suffering and theodicy (Job), practical wisdom as Christ (Prov 8),
vanity and meaning (Eccl), the love of Christ and the church (Song).
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
# JOB
# ============================

JOB_ECHO = {
  "1": {
    "21": [
      {"type": "allusion", "target": "Phil 4:11-12", "note": "The LORD gave, and the LORD has taken away; blessed be the name of the LORD — Job's response to total loss; Paul's 'I have learned, in whatever state I am, to be content' echoes the Job pattern of accepting both abundance and loss from the hand of God"}
    ]
  },
  "9": {
    "33": [
      {"type": "allusion", "target": "1 Tim 2:5", "note": "There is no arbiter between us who might lay his hand on both of us — Job's longing for a mediator who can bridge the gap between the holy God and the accused human; Paul's 'there is one mediator between God and men, the man Christ Jesus' is the direct answer to Job's longing: the mediator Job needed exists"}
    ]
  },
  "19": {
    "25": [
      {"type": "allusion", "target": "1 Cor 15:20", "note": "I know that my Redeemer lives, and at the last he will stand upon the earth — Job's confession of faith in a living Redeemer who will vindicate him after death; the resurrection of Christ is the answer to Job's hope: the Redeemer who lives has stood upon the earth, and because he lives Job will live also"}
    ]
  },
  "38": {
    "4": [
      {"type": "allusion", "target": "John 1:1", "note": "Where were you when I laid the foundation of the earth? — the divine speech from the whirlwind (chs. 38-41) confronts Job with the Creator's incomprehensible majesty; John 1:1 grounds Christ as the one who was present at that foundation: in the beginning was the Word, and the Word was with God — the one speaking from the whirlwind and the one who became flesh are the same person"}
    ]
  }
}

JOB_ORIGINAL = {
  "19": {
    "25": "<p><strong>vaani yadati goa'li chai ve'acharon al afar yaqum</strong>: 'For I know that my Redeemer [<em>go'el</em>] lives, and at the last he will stand upon the earth' (or 'upon the dust'). This is one of the OT's most disputed verses — the text is difficult (the next verse, 19:26, is even more so: 'after my skin has thus been destroyed, yet in my flesh I shall see God'). The term <em>go'el</em> (kinsman-redeemer) in the context of Job's suffering suggests: the one who will vindicate Job after death, who will see to it that justice is done. Whether Job envisions a bodily resurrection (as 19:26 suggests in the MT) or a post-mortem vindication, the theological content is the same: a personal Redeemer who is alive, who will act at the last, who will secure Job's vindication. The NT identifies this Redeemer as Christ (1 Cor 15:20: Christ has been raised from the dead, the firstfruits of those who have fallen asleep).</p>"
  },
  "38": {
    "4": "<p>The divine speech from the whirlwind (Job 38-41) is the OT's most extended meditation on the incomprehensibility and majesty of God. YHWH's questions ('Where were you when I laid the foundation of the earth? Tell me, if you have understanding') do not answer Job's question about suffering — they reframe it by confronting Job with the Creator's perspective. The response to theodicy is not a logical explanation but a theophanic encounter: when Job sees YHWH, his questions are transformed, not answered (42:5: 'my eye sees you'; he is satisfied). This pattern — suffering resolved not by explanation but by encounter with God — points to the incarnation: the answer to the problem of suffering is not a theodicy argument but the Son of God entering the suffering and going through it.</p>"
  }
}

JOB_CONTEXT = {
  "1": {
    "1": "<p>Job is the OT's most direct engagement with the problem of innocent suffering. Its genre combines a prose frame (the prologue and epilogue) with a poetic center (the dialogues, Job 3-41). The prologue reveals what Job does not know: that his suffering is the result of a cosmic test. The dialogues work out the human perspective on suffering without that hidden knowledge. The friends defend the retributive justice principle (you suffer, therefore you sinned); Job insists on his innocence. Both are partially right: the friends are correct that suffering is related to sin in general (the cosmic fall), but wrong that Job's specific suffering is punishment for specific sin. YHWH's verdict (42:7-8: Job's friends 'have not spoken of me what is right, as my servant Job has') vindicates Job's complaint against easy theodicy.</p>"
  }
}

JOB_CHRIST = {
  "9": {
    "33": "<p>A type: 'There is no arbiter between us who might lay his hand on us both, who would remove his rod from me, and let not dread of him terrify me.' Job's longing for a mediator is one of the Bible's most poignant anticipations of Christ. What Job needs is someone who can stand between the holy God and the accused human — with one hand on God and one hand on the human — securing Job's access to God without the terror. The incarnation is the answer: Jesus Christ 'laid his hand' on both realities, being fully God and fully human, so that 'there is one mediator between God and men, the man Christ Jesus' (1 Tim 2:5). The mediator Job could only wish for, the NT declares has come.</p>"
  },
  "19": {
    "25": "<p>A direct revelation: 'I know that my Redeemer lives, and at the last he will stand upon the earth.' Job's confession cuts through the fog of his suffering to affirm what cannot be seen or felt: a living Redeemer who will vindicate. The confession has multiple levels of fulfillment in Christ: (1) the Redeemer lives — Christ's resurrection is the demonstration; (2) he will stand upon the earth at the last — the parousia; (3) 'in my flesh I shall see God' (v. 26) — the bodily resurrection of the righteous. Job, in the depths of suffering and loss, speaks one of Scripture's clearest affirmations of resurrection-hope and the personal Redeemer who makes it possible.</p>"
  }
}

# ============================
# PROVERBS
# ============================

PROV_ECHO = {
  "1": {
    "7": [
      {"type": "allusion", "target": "Col 2:3", "note": "The fear of the LORD is the beginning of wisdom — Proverbs' foundational maxim; Paul says in Christ are hidden all the treasures of wisdom and knowledge (Col 2:3): Christ is where the 'fear of the LORD leads, the source from whom all wisdom flows"}
    ]
  },
  "8": {
    "22": [
      {"type": "allusion", "target": "John 1:1", "note": "The LORD possessed me at the beginning of his work, the first of his acts of old — Wisdom speaking in Proverbs 8:22-31; personified Wisdom present at creation, delighting in the inhabited world; the Logos-Wisdom identification (John 1:1-3; Col 1:15-16; Heb 1:2-3) applies the Prov 8 Wisdom-portrait to the pre-incarnate Christ"},
      {"type": "allusion", "target": "Col 1:15", "note": "I was beside him like a master workman, rejoicing before him always — Wisdom as God's artisan in creation (Prov 8:30); Paul describes Christ as the one in whom all things were created (Col 1:16) and through whom all things were made (John 1:3); the Wisdom-Creator becomes the Christ-Creator"}
    ]
  },
  "3": {
    "11": [
      {"type": "allusion", "target": "Heb 12:5-6", "note": "My son, do not despise the LORD's discipline or be weary of his reproof, for the LORD reproves him whom he loves — Hebrews quotes Prov 3:11-12 to explain suffering as divine discipline: God treats believers as sons (Heb 12:7); the wisdom perspective on suffering as fatherly training is the theological framework for the Christian endurance of hardship"}
    ]
  }
}

PROV_ORIGINAL = {
  "8": {
    "22": "<p><strong>YHWH qanani reshit darko qedem mifalav meaz</strong>: 'The LORD possessed/created me at the beginning of his work, the first of his acts of old.' The verb <em>qanah</em> is disputed: it can mean 'to acquire/possess' (so most LXX manuscripts, Aquila, Theodotion) or 'to create' (so the Arian controversy reading, applied to prove the Son was a created being). The Nicene theology responded: even if <em>qanah</em> means 'created', Proverbs 8 is personified Wisdom literature — a poetic device, not a literal description of a divine person's ontology. The NT applies Prov 8's Wisdom-portrait to the eternal Son (Col 1:15-17; Heb 1:2-3; John 1:1-3) not to prove the Son is created, but to show that the pre-existent Son is the referent of the Wisdom-personification: the figure the wisdom tradition was groping toward in poetic imagery became flesh in Christ.</p>"
  }
}

PROV_CONTEXT = {
  "1": {
    "1": "<p>Proverbs is the OT's primary wisdom text — a collection of moral instruction, practical guidance, and theological reflection on the nature of a well-ordered life in YHWH's world. It is attributed to Solomon (1:1; 10:1; 25:1) with additions from other wise men (Agur, 30:1; Lemuel's mother, 31:1). Its theological foundation is the fear of YHWH (1:7; 9:10; 15:33): wisdom is not abstract intellectual skill but a disposition toward God and the moral order of creation. The longest section (chs. 1-9) frames the rest with the personification of Wisdom as a woman calling in the streets, building her house, offering her feast — while her counterpart, Folly, seduces the simple to death. The NT's identification of Christ as divine Wisdom (1 Cor 1:24, 30; Col 2:3) is the claim that the personification in Proverbs 8 was, in the fullness of time, made literal and personal.</p>"
  }
}

PROV_CHRIST = {
  "8": {
    "30": "<p>A revelation of God: 'Then I was beside him, like a master workman, and I was daily his delight, rejoicing before him always, rejoicing in his inhabited world and delighting in the children of man.' Wisdom's delight in creation and in humanity (Prov 8:30-31) is the OT's most personal statement of the divine affection for the created order. The NT applies this portrait to the eternal Son: 'by him all things were created' (Col 1:16); 'all things were made through him' (John 1:3); 'through whom also he created the world' (Heb 1:2). The Wisdom who rejoiced at creation is the Word who entered creation (John 1:14), and the delight Wisdom expressed for the children of man is the love that sent the Son into the world (John 3:16). Proverbs 8's Wisdom-portrait is the poetic anticipation of the incarnate Logos who is himself divine wisdom in person (1 Cor 1:24: Christ the wisdom of God).</p>"
  }
}

# ============================
# ECCLESIASTES
# ============================

ECCL_ECHO = {
  "1": {
    "2": [
      {"type": "allusion", "target": "Rom 8:20", "note": "Vanity of vanities, all is vanity — the Preacher's diagnosis of the futility of all earthly striving; Paul's 'the creation was subjected to futility [mataiotes = the LXX word for hevel/vanity]' applies Ecclesiastes' diagnosis to the whole created order: the vanity is not merely human experience but creation-wide, awaiting the liberation of the resurrection"}
    ]
  },
  "12": {
    "13": [
      {"type": "allusion", "target": "Matt 22:37-40", "note": "Fear God and keep his commandments, for this is the whole duty of man — the Preacher's final summary of the human vocation: the fear of YHWH and covenant obedience are the answer to the vanity of all other human projects; Jesus's summary (love God and love neighbor) is the new covenant distillation of the same conclusion"}
    ]
  }
}

ECCL_ORIGINAL = {
  "1": {
    "2": "<p><strong>havel havalim amar qohelet havel havalim hakol havel</strong>: 'Vanity of vanities, says the Preacher, vanity of vanities! All is vanity.' The Hebrew <em>hevel</em> (vapor, breath, vanity) is used 38 times in Ecclesiastes — more than in any other biblical book. It literally means a breath of air that passes immediately: something that exists momentarily and then is gone. The LXX translates <em>hevel</em> as <em>mataiotes</em> (futility, vanity), and Paul uses this word in Romans 8:20: 'the creation was subjected to futility [<em>mataiotes</em>].' The Ecclesiastes diagnosis is therefore not pessimism but realism about the post-fall condition of creation: all earthly striving that does not account for God and eternity is, sub specie aeternitatis, vapor. The NT's response is the resurrection, which gives permanence to what was formerly vapor: 'your labor in the Lord is not in vain' (1 Cor 15:58).</p>"
  }
}

ECCL_CONTEXT = {
  "1": {
    "1": "<p>Ecclesiastes (Hebrew <em>Qohelet</em>, 'the Preacher/Assembler') is the most theologically challenging book of the wisdom literature — it appears to endorse cynicism (2:24: 'there is nothing better for a person than to eat and drink'), relativism (3:1-8: a time for everything), and even doubt (9:5: the dead know nothing). Its canonical function is the 'foil' in the wisdom dialogue: if Proverbs gives the optimistic wisdom perspective, Ecclesiastes gives the honest reckoning with what happens when wisdom is pursued 'under the sun' — that is, within the frame of mortal, fallen human existence. The recurring phrase 'under the sun' (29 occurrences) marks the book's self-conscious limitation: it is wisdom from the earthly perspective, without the resurrection. The NT provides what Ecclesiastes lacks: the 'not in vain' of labor done in the Lord (1 Cor 15:58) and the hope that breaks the <em>hevel</em>-cycle.</p>"
  }
}

ECCL_CHRIST = {
  "12": {
    "13": "<p>A shadow: 'Fear God and keep his commandments, for this is the whole duty of man.' Ecclesiastes' closing verdict after surveying all human wisdom is the simplest possible statement of the human vocation: the fear of God and covenant obedience. This is the wisdom tradition's answer to vanity — not a philosophical system but a personal relationship with the Creator. Jesus's summary of the law (love God, love neighbor) is the new covenant's positive restatement of what Ecclesiastes reaches as its final conclusion. But Christ does more than restate: he embodies the fear of God and covenant obedience perfectly (Heb 5:7-8: in the days of his flesh, Jesus offered up prayers and supplications with loud cries and tears ... and was heard because of his reverence; although he was a son, he learned obedience through what he suffered), and in his resurrection he breaks the <em>hevel</em>-cycle, proving that labor in the Lord — unlike all labor 'under the sun' — is not in vain (1 Cor 15:58).</p>"
  }
}

# ============================
# SONG OF SOLOMON
# ============================

SONG_ECHO = {
  "2": {
    "16": [
      {"type": "allusion", "target": "John 10:14", "note": "My beloved is mine and I am his — the mutual possession of the beloved and the lover; I know my sheep and my sheep know me (John 10:14) is the new covenant expression of the same mutual-knowing/belonging that the Song celebrates; Christ's love for the church is the fulfillment of the Song's bridegroom love"}
    ]
  },
  "8": {
    "6": [
      {"type": "allusion", "target": "Rom 8:35-39", "note": "Love is strong as death, jealousy is fierce as the grave; its flashes are flashes of fire, the very flame of the LORD — the Song's declaration of love's unconquerable strength; Paul's conviction that nothing can separate us from the love of God in Christ Jesus is the new covenant answer to the Song's vision of love stronger than death: Christ's love has defeated death itself and remains unbreakable"}
    ]
  }
}

SONG_ORIGINAL = {
  "1": {
    "1": "<p>The Song of Songs (<em>shir hashirim</em>) is the OT's wisdom-meditation on human love and sexuality. Its literal level — a celebration of erotic love between a man and a woman — is taken seriously by responsible interpreters as a canonical affirmation of marriage and the goodness of sexual love within covenant. The allegorical level — YHWH's love for Israel (the Jewish interpretation) or Christ's love for the church (the dominant Christian interpretation) — has been the dominant hermeneutical approach through most of church history (Origen's commentary and Bernard of Clairvaux's 86 sermons on Song 1-2 are the most extensive examples). The allegorical reading is supported by the OT's consistent use of the husband-wife metaphor for YHWH-Israel (Isa 54:5; Jer 2:2; Ezek 16; Hos 1-3) and the NT's application of the bride-bridegroom image to Christ-church (Eph 5:25-32; Rev 19:7-9; 21:2). The two readings are not mutually exclusive: the literal is the foundation that gives the allegorical its force.</p>"
  },
  "7": {
    "1": "<p><strong>hassulammit / machola ha-machanayim</strong>: The beloved is here called <em>hassulammit</em> — the only named character in the Song (H7759, appearing only in 6:13 and here). The name is debated: most likely the feminine form of <em>shlomo</em> (Solomon, H8010), meaning she is the feminine counterpart to the king — <em>shlomit</em>, the peaceful/complete one. The LXX reads <em>Soulamitis</em> (the Shunammite), connecting her to Abishag the Shunammite (1 Kings 1:3; 2:17), the young woman brought to comfort David in his old age. <em>Machola ha-machanayim</em> (the dance of two camps/armies, H4246 + H4264) is a hapax; <em>machanayim</em> (two camps, H4264) is the place name where Jacob saw the angel army and called the place Mahanaim (Gen 32:2 — &ldquo;this is God&rsquo;s camp&rdquo;, hence two camps). Whether the dance takes place at Mahanaim, or the beloved dances before two groups, or the descriptor invokes the theophanic camp-vision, the military vocabulary (<em>machaneh</em> = army/camp) applied to the beloved&rsquo;s dance connects to the &ldquo;awesome as an army with banners&rdquo; (6:4, 10) portrait. The <em>wasf</em> (Arabic term for this body-description form) of ch7 ascends from feet upward, unlike ch4&rsquo;s descending wasf — a structural inversion that creates variety in the book&rsquo;s praise-poetry.</p>",
    "2": "<p><strong>shorer / 'aggan</strong>: <em>Shorer</em> (H8326, navel/umbilical cord) is a hapax legomenon — appearing only here in the Hebrew Bible. The term refers to the navel or the umbilical region. The comparison to an <em>'aggan</em> (H101, a bowl or basin) that never lacks mixed wine (<em>mezeg</em>, H4197, spiced/mixed wine, also a hapax) is the most anatomically specific metaphor in the <em>wasf</em> sequence. The <em>'aggan</em> is used for the bronze basins of the sanctuary (Exod 24:6); its application here to the navel invests a bodily feature with the dignity of sacred craftsmanship. The belly (<em>beten</em>, H990) as a mound of wheat (<em>'orem chitta</em>, H6194 + H2406) fenced with lilies (<em>shushanim</em>, H7799) repeats the wheat-fenced-with-lilies image from 7:3 and 4:5, suggesting the beauty of the abundant harvest protected by delicate beauty. The mound-of-wheat image may also echo the harvest-thanksgiving fertility symbolism of Canaanite and broader ANE ceremonial contexts where the body was celebrated as a site of agricultural abundance.</p>",
    "3": "<p>The two-fawns twin-gazelle simile for the breasts, repeated nearly verbatim from 4:5, creates a deliberate internal echo within the Song. The repetition is not carelessness but the deliberate intensification of the praise-pattern: the same beautiful image heard again in a new context deepens the picture. The <em>teomei tzeviyyah</em> (H8380 + H6646, twins of a gazelle) describes the symmetry, delicacy, and vitality of the beloved&rsquo;s body — matching paired features that move together with the elegant coordination of young animals at play.</p>",
    "4": "<p><strong>bat-rabbim / hachat-ha-bat-rabbim</strong>: The pools of Heshbon at the gate of <em>Bat-Rabbim</em> (H1337, daughter of many) are likely archaeological. Heshbon (modern Tell Hesban in Jordan) was the capital of the Amorite king Sihon and subsequently a Reubenite city (Num 21:25-26; Josh 13:17); excavations have revealed large stone-cut water cisterns near the city. The <em>bat-rabbim</em> gate may be a topographic name for a specific entrance to the city. Eyes as pools emphasize their depth, reflectivity, and stillness — the quality that makes one want to gaze into them. <em>Miqvei cheshbon</em> (H4798 + H2809, the pools of Heshbon) — the <em>miqveh</em> (H4723, gathering of water) root is related to the Jewish ritual bath; the word carries the sense of gathered, standing, clear water. The nose like the tower of Lebanon (<em>migdal hallevano</em>) looking toward Damascus — the great mountain range as the image of a prominent, regal facial feature facing the direction of a powerful city.</p>",
    "5": "<p><strong>ha-karmel</strong>: The head like Carmel (<em>karmel</em>, H3760) is both a place name (the prominent coastal promontory where Elijah confronted the prophets of Baal, 1 Kings 18) and a common noun meaning a garden-land or fruitful field (used in Isa 10:18, 2 Kings 19:23 for garden-lands; in 2 Kings 4:42 for fresh ears of grain). The double meaning — majestic landmark and fruitful garden — makes the comparison to the beloved&rsquo;s head capture both her regal bearing and her vitality. The flowing locks described as <em>'arugah ba-t&rsquo;chumorot</em> (wavy/bound with purple) — the word <em>arugah</em> or the root behind the translated &ldquo;dyed/bound with purple&rdquo; — purple dye was the luxury color of the ancient world, produced from the murex snail by the Phoenician craftsmen. The king captured (<em>asur</em>, H631, bound/held) by the tresses inverts the power dynamic: the king who holds everything is held by the beloved&rsquo;s hair.</p>",
    "6": "<p>The direct address of appreciation — <em>mah-yafet umah-na'amt ahavah bata'anugim</em> (how fair and how pleasant you are, O love, with delights/pleasures) — steps back from the detailed <em>wasf</em> inventory to offer the holistic impression. <em>Ta'anugim</em> (H8588, delights/luxuries) is the noun used in Eccl 2:8 for the sensory pleasures Solomon accumulated; here it is the label for the beloved herself as the embodiment of all delight. The paired adjectives <em>yafeh</em> (beautiful) and <em>na'im</em> (pleasant/agreeable, the root of Jonathan&rsquo;s <em>no'am</em> and Naomi&rsquo;s name) describe both visual beauty and the quality of being agreeable, delightful, or at ease — the word that describes Jonathan&rsquo;s love for David in 2 Sam 1:26 (&ldquo;your love was wonderful to me&rdquo;, <em>nifle'ta ahavatkha</em>).</p>",
    "7": "<p><strong>tamar</strong>: The comparison of the beloved&rsquo;s stature to a date palm (<em>tamar</em>, H8558) is one of the most evocative images in the Song. The <em>tamar</em> is the date palm — the tree of the ancient Near East most closely associated with royal dignity, fertility, and beauty. Date palms were cultivated throughout Mesopotamia and Canaan; the palm branch is the symbol of victory and majesty (cf. the triumphal palm branches of John 12:13). The name <em>Tamar</em> (given to Judah&rsquo;s daughter-in-law in Gen 38 and to David&rsquo;s daughter in 2 Sam 13) means &ldquo;date palm&rdquo; — a name of beauty and dignity. The clusters (<em>'eshkolot</em>, H811) of the date palm for the beloved&rsquo;s breasts use the same word used for the enormous grape cluster brought from the Valley of Eshcol in Num 13:23, suggesting abundance and sweetness.</p>",
    "8": "<p>The bridegroom&rsquo;s declaration that he will climb the palm tree (<em>e'eleh b&rsquo;tamar</em>, I will ascend the palm tree) and take hold of its branches/clusters (<em>sansinav</em>, H5577, its boughs/date-branches, a hapax in this form) is the boldest statement of intentional pursuit in the Song. <em>E'eleh</em> (I will go up/ascend) is the verb used for going up to Jerusalem, to the temple, and to the high places — it carries connotations of purposeful, upward movement toward something honored or holy. The vine branches whose smell is like an apple (<em>appe-ha-gefen ka-tappuchim</em>) — the fragrance of the vine at close range compared to the apple tree (used elsewhere in the Song as the beloved&rsquo;s sheltering image, 2:3, 8:5).</p>",
    "9": "<p><strong>yayin ha-tov / meyashar ledodi</strong>: The mouth of the beloved compared to <em>yayin ha-tov</em> (the best wine, H2896 + H3196) transitions into the beloved&rsquo;s own voice in mid-verse: &ldquo;going down smoothly for my beloved&rdquo; (<em>meyashar ledodi</em>, moving smoothly/pleasantly to my beloved) and &ldquo;gliding over lips and teeth&rdquo; (<em>dovev sifatei yeshenim</em>, causing the lips of sleeping ones to speak, or &ldquo;gliding over the lips of those who sleep&rdquo;). The <em>yeshanim</em> (H3463, sleeping ones) is interpretively difficult — some understand &ldquo;the lips of the sleeping&rdquo; as the wine&rsquo;s quality of loosening speech even in drowsiness; others (following the LXX <em>lips and teeth</em>) read the mouth imagery as the wine&rsquo;s pleasant movement across the palate. The transition from bridegroom speaking about the wine-mouth to the beloved taking up the wine image for herself is a grammatical intimacy — the beloved enters the speech as its continuation.</p>",
    "10": "<p><strong>teshuqah</strong>: <em>Ani ledodi ve'alai teshuqato</em> (I am my beloved&rsquo;s and his desire is for me) — the mutual-possession formula of 2:16 and 6:3 recurs here with a crucial variation: where 2:16 says &ldquo;he pastures among the lilies&rdquo; and 6:3 simply mirrors possession, 7:10 adds <em>teshuqah</em> (H8669, desire/longing). This word occurs only three times in the Hebrew Bible: Gen 3:16 (the woman&rsquo;s desire for her husband, in the context of the curse — &ldquo;your desire will be for your husband and he will rule over you&rdquo;), Gen 4:7 (sin&rsquo;s desire crouching at the door, waiting for Cain), and here. The theological contrast is profound: in Genesis the <em>teshuqah</em> is bound up with the curse (the distortion of the man-woman relationship through the fall) and with the threat of sin (the appetite that destroys). Here in the Song the same word names the beloved&rsquo;s desire for the beloved in the context of covenantal love that echoes the pre-fall garden: the <em>teshuqah</em> of the Song is the restoration of the desire that Genesis describes as distorted. The Song does not use the word innocently — it reaches into the curse-vocabulary and redeems it.</p>",
    "11": "<p>The beloved&rsquo;s invitation to go out into the fields (<em>sadeh</em>, H7704) and lodge in the villages (<em>kefar</em>, H3723, villages/hamlets) is the rural-pastoral invitation that runs through the Song as its primary landscape. The word <em>kefar</em> (also the root of Capernaum, <em>kefar nachum</em>, the village of Nahum) describes the smaller settlements around the walled city — the agrarian life of vineyards, flocks, and harvests. The invitation to leave the city and enter the village is the beloved&rsquo;s initiative — she is the one who leads in this verse, calling the bridegroom into her world rather than waiting for him to call her out.</p>",
    "12": "<p>The springtime inventory of the vineyard — <em>nistrah hagefen pitach hasemadar</em> (whether the vine has sprouted, the tender grape blossom has opened) and the pomegranates flowering (<em>heniczu ha-rimmonim</em>) — repeats the spring-survey vocabulary of 2:11-13 in compressed form. The <em>semadar</em> (H5563, the tender grape blossom or grape-bud, appearing in the Song at 2:13, 2:15, and here) is the earliest indicator of the vine&rsquo;s productive season. <em>Sham 'eten et-dodai lakh</em> (there I will give my love to you) — the beloved&rsquo;s self-gift offered in the productive landscape of the vineyard; the place of abundance is also the place of self-donation.</p>",
    "13": "<p><strong>duda'im</strong>: The mandrakes (<em>duda'im</em>, H1736) appear only in two other biblical passages: Gen 30:14-16, where Rachel trades Jacob&rsquo;s company for Leah&rsquo;s mandrakes (mandrakes were believed in the ANE to promote fertility and desire, the word related to <em>dod</em>, beloved/uncle/love), and Prov 7:18 (possibly). The Song&rsquo;s beloved offers the fragrant mandrakes without the competitive anxiety of the Genesis scene — what Leah and Rachel fought over becomes the abundant gift of the beloved who freely gives all her precious fruits. <em>Chadashim gam yeshanim</em> (new and old/new and stored ones) — the image of the beloved who has laid away, over time, all good things for her beloved. The past savings and the fresh harvest, the stored and the new — the comprehensive abundance of a love that has been accumulating its gifts.</p>"
  },
  "8": {
    "1": "<p><strong>mi yittencha ke'ach li</strong>: &lsquo;Who will give you to me as a brother&rsquo; — the use of <em>mi yitten</em> (who will give, the Hebrew idiom for &ldquo;would that!&rdquo; or &ldquo;if only&rdquo;) expresses wish for something currently impossible. The social context: in the ancient Near East, a woman could kiss a brother in public without social reproach, but kissing a non-family male in the street would result in her being <em>buz</em>-ed (contemned, despised, H936) — subjected to the social shame of breaking the honor code governing public male-female contact. The beloved&rsquo;s wish is not that the beloved were literally her sibling but that the intimacy of sibling affection could be publicly expressed without social jeopardy. The verse is a precise social observation: love creates longings for a freedom of expression that social conventions restrict.</p>",
    "2": "<p><strong>'avi-me</strong>: The mother&rsquo;s house (<em>beit immi</em>, H517, my mother&rsquo;s house) appears three times in the Song (3:4, 8:2) as the primary social sanctuary for the beloved — the place of legitimate reception of the beloved. The instruction the beloved would receive from her mother — in the context of the spiced wine and pomegranate nectar she would serve — reflects the role of the mother in the ancient Near East as the transmitter of domestic wisdom, particularly regarding the preparation of the household for the relationship of marriage. <em>Rimmon</em> (H7416, pomegranate) is a recurring image in the Song for the beloved&rsquo;s beauty (4:3, 6:7, 7:12) and here for the gift she would offer the beloved. The pomegranate was the ANE symbol of fertility and abundance; its juice as the gift of the beloved&rsquo;s hospitality elevates the natural fruit to the level of love-gift.</p>",
    "3": "<p>The left-hand/right-hand embrace — <em>semalo tachat roshi ve-yamino techabbakeni</em> (his left hand under my head and his right hand embraces me) — repeats 2:6 verbatim. The repetition within the Song functions as a structural echo: the reclining tenderness of 2:6 and 8:3 frames the entire middle section of the book (chs. 3-7) with the same image of covenantal closeness. The left hand under the head is the posture of the protective reclining embrace — the protective cradle; the right hand embracing is the encircling hold. Together they describe the full-body embrace of the beloved by the one who holds her.</p>",
    "4": "<p>The daughters of Jerusalem adjuration (<em>hishba'ti etkem&hellip; mah-ta'iru umah-te'oreru et-ha'ahavah</em>, I adjure you&hellip; why would you stir up and awaken love) is the Song&rsquo;s recurring refrain (2:7, 3:5). The gazelle/deer invocation present in 2:7 and 3:5 is absent here, making this the more compressed form of the adjuration. The refrain&rsquo;s placement at the beginning of the final chapter functions as a summary: having traced the entire arc of love&rsquo;s seeking, finding, losing, and re-finding, the beloved reissues the counsel of patient waiting. Love that is authentic cannot be forced, manufactured, or artificially stirred up; it arrives in its own time and must be awaited rather than provoked.</p>",
    "5": "<p><strong>mecholeliteka</strong>: <em>Mi zo't olah min-hamidbar mitrapeket al-dodah</em> (who is this coming up from the wilderness, leaning on her beloved?) — the procession image (cf. 3:6) recurs here, but now the figure is identified by her intimacy: she leans on (<em>mitrapeket</em>, clinging, leaning upon) her beloved. The final wilderness-to-Zion procession image of the Song has been transformed from the perfumed-smoke procession of ch3 (which featured Solomon&rsquo;s couch, cedar wood, and sixty warriors) into an intimate pair. <em>Mecholeliteka</em> (H2342, gave birth to you, from <em>chul</em>, to writhe/dance/give birth) — the same root used for birth pangs throughout the prophets (Isa 26:17, Jer 4:31, Mic 4:10) and for the trembling of creation. The apple tree (cf. 2:3 where the bridegroom is an apple tree for the beloved) as the birthplace creates a structural inclusion: the tree under which the beloved rested (2:3) is now the tree under which the beloved was born. Love has the quality of rebirth at its origin point.</p>",
    "6": "<p><strong>shalhevetyah</strong>: <em>Simeini kachotam al libecha kachotam al zeroa'echa ki azza kamavet ahavah qasha kishol qina'ah reshefeyha reshefei esh shalhevetyah</strong>: The seal (<em>chotam</em>, H2368, a signet ring or impression seal, used in Gen 38:18 for Judah&rsquo;s identifying seal) is the most intimate possessory object in the ancient world — it was the authorized mark of one&rsquo;s identity on legal documents. To ask to be placed as a seal upon the beloved&rsquo;s heart and arm is to ask for incorporation into the beloved&rsquo;s very identity and authority. The climactic declaration of love&rsquo;s strength: <em>azza kamavet ahavah</em> (fierce as death is love) and <em>qasha kishol qina'ah</em> (hard as Sheol is jealousy). <em>Qina'ah</em> (H7068, jealousy/zeal) — the same root used for divine jealousy (<em>el qanna</em>, jealous God, Exod 20:5) — the love that cannot share its beloved is the mirror of the divine jealousy that cannot share its people. <em>Shalhevetyah</em> (H7957 + H3050) — the word uniquely compounds <em>shalhebet</em> (flame) with the divine name suffix <em>-yah</em> (the shortened form of YHWH). The KJV renders this as &ldquo;a most vehement flame&rdquo; (taking the <em>-yah</em> as a grammatical intensifier); the theological reading takes it as the literal identification of the love-flame with the divine fire. Given the theophanic associations of divine fire throughout the OT (burning bush, Sinai, pillar of fire), the &ldquo;flame of Yah&rdquo; reading is theologically weighted: love&rsquo;s fire participates in the nature of YHWH&rsquo;s own fire.</p>",
    "7": "<p><strong>buz yevuzu lo</strong>: The continuation of v6&rsquo;s declaration — <em>mayim rabbim lo yukelu lechabbot et-ha'ahavah</em> (many waters are not able to quench the love) and rivers (<em>neharot</em>) cannot drown it. The many waters and rivers are images of the ANE flood-chaos (cf. Ps 93:3-4 where the floods/rivers roar against YHWH&rsquo;s throne; Ps 46:2-3 where mountains fall into the sea and waters rage). Love that the chaos-waters cannot extinguish is love that participates in YHWH&rsquo;s own stability against the chaotic deep. The wealth-contempt coda: <em>im yitten ish et-kol-hon beito ba'ahavah boz yevuzu lo</em> (if a man were to give all the wealth of his house for love, he would be utterly despised). <em>Buz</em> (H936, contempt/treating with contempt) — the social shaming of the one who attempts to commodify love through commercial exchange. The attempt to purchase what can only be freely given is not merely unsuccessful but self-disgracing: it places the buyer in the position of the one who fundamentally misunderstands the nature of the thing he seeks.</p>",
    "8": "<p>The brothers&rsquo; deliberation about the little sister (<em>achot lanu qetannah</em>, we have a little sister) who does not yet have breasts — a younger sibling not yet at marriageable age. The brothers&rsquo; question: what will we do for our sister on the day she is spoken for? The protective role of the brothers toward their sister&rsquo;s honor was a social norm in ancient Israel (cf. Gen 34:25-29 where Simeon and Levi avenge Dinah&rsquo;s honor). The question shows that the beloved&rsquo;s brothers have been thinking about her future: the two possibilities (wall or door) represent two different assessments of her character and two corresponding responses.</p>",
    "9": "<p>The wall/door alternatives: <em>im chomah hi</em> (if she is a wall, H2346) the brothers would build upon her a turret of silver (<em>tira'at kesef</em>, H2918 + H3701); <em>ve-im delet hi</em> (if she is a door, H1817) they would enclose her with cedar boards (<em>luch erez</em>, H3871 + H730). The wall represents the impenetrable — a woman whose character is like a fortified wall, whose integrity needs only to be adorned and honored; the door represents the open passage that needs to be secured. The distinction is not judgmental but architectural: the brothers respond to what the beloved is with the appropriate protection. Silver turrets ornament what is already strong; cedar boards secure what is vulnerable. The verse anticipates the beloved&rsquo;s own declaration in v10.</p>",
    "10": "<p><strong>shalom / shlomoh</strong>: <em>Ani chomah u-shadai kamigdalot az hayiti be'einav kemotze'et shalom</em> (I am a wall, and my breasts are like towers; thus I have become in his eyes as one who finds peace). The beloved answers the brothers&rsquo; hypothetical with a declaration: she is the wall, not the door — her integrity is the fortress. The towers of her body adorning what was already strong confirms the silver-turret scenario of v9. <em>Shalom</em> (H7965, peace/wholeness/completeness) as the beloved&rsquo;s self-description creates a deliberate wordplay with <em>shlomoh</em> (Solomon, H8010, the peaceful one). The beloved who is a wall becomes in the bridegroom&rsquo;s eyes the one who finds/gives <em>shalom</em> — she mirrors the Solomon-quality that the Song has associated with the bridegroom throughout. The verse&rsquo;s wordplay: the beloved-as-wall achieves in her integrity the <em>shalom</em> that the Solomon-figure embodies.</p>",
    "11": "<p><strong>ba'al hamon / kerem</strong>: Solomon&rsquo;s vineyard at <em>Ba'al Hamon</em> (H1174, master of abundance or Baal-Hamon, an unidentified location) follows the vineyard-ownership theme from 1:6. The vineyard lets out to keepers (<em>notrim</em>, H5201, watchmen/guardians — the same root used for keeping the law and for the vineyard-keepers in Isa 5:1-7) for a rent of a thousand silver pieces (<em>elef kesef</em>). The commercial vineyard, rented and productive for profit, is the literary backdrop against which the beloved makes her declaration in v12.</p>",
    "12": "<p><strong>karmi shelli lefanai</strong>: <em>Karmi shelli lefanai</em> (my own vineyard is before me, belonging to me) — the emphatic <em>shelli</em> (mine, my own) is the rhetorical climax of the vineyard imagery that has run through the Song from 1:6 (where the beloved lamented she had not kept her own vineyard while keeping others&rsquo;). Here the beloved asserts that her vineyard — her own self and her love — is hers to give, not to rent for silver. The thousand pieces for Solomon and the two hundred for the keepers (<em>la-notrim</em>) contrast with the priceless self-gift the beloved offers freely. The commercial transaction of the vineyard-rent is implicitly contrasted with v7&rsquo;s statement that love cannot be purchased: the beloved&rsquo;s vineyard is free in the sense of both liberty (it is hers to give) and of freely given (it is offered without price).</p>",
    "13": "<p><strong>chomeret / yashvu / hashme'ini</strong>: The companions (<em>chaverim</em>, H2270) listening for the beloved&rsquo;s voice creates a scene of communal anticipation: the beloved&rsquo;s speech is sought not only by the bridegroom but by the surrounding community. The <em>chaverim</em> (friends/companions) are a presupposed community of listeners, the circle of relationship that the love-pair exists within. <em>Hashme'ini et-qolekh</em> (let me hear your voice) — the same formula as 2:14 where the bridegroom in the cleft of the rock begs to hear the beloved&rsquo;s voice. The voice of the beloved that the companions gather to hear and that the bridegroom specifically requests is the most intimate gift of the whole person: the beloved&rsquo;s words are what she gives most fully, beyond the gifts of the vineyard and the mandrakes.</p>",
    "14": "<p><strong>berach dodi</strong>: The Song&rsquo;s final line — <em>berach dodi vedameh lekha litsvi o le'ofer ha'ayyalim al-harim vessamim</em> (flee, my beloved, and be like a gazelle or a young stag on the mountains of spices) — is not a permanent farewell but the invitation to return. <em>Berach</em> (H1272, to flee/move through quickly) is the verb for the swift movement of animals through landscape — the same root used for the patriarchs&rsquo; flight and for the movement of the divine spirit. The gazelle/stag imagery (repeated from 2:9, 2:17) frames the ending as open, dynamic movement rather than static arrival: the Song ends with the beloved in motion, racing over the fragrant mountains, with the beloved calling after him. The mountains of spices (<em>harim vessamim</em>) — not a specific location but the entire fragrant landscape of the Song — are where the beloved runs. The ending is the beginning of the next seeking.</p>"
  }
}

SONG_CONTEXT = {
  "1": {
    "1": "<p>The Song of Solomon's place in the canon was debated in rabbinic Judaism (Rabbi Akiva defended it: 'all the ages are not worth the day on which the Song of Songs was given to Israel; for all the writings are holy, but the Song of Songs is the Holy of Holies'); it was included in the Hebrew canon and subsequently in the Christian canon. The bride-bridegroom image is the OT's primary metaphor for the YHWH-Israel covenant relationship: Hosea (chs. 1-3) uses the marriage metaphor for covenant and its violation; Isaiah 54:5 calls YHWH Israel's husband; Jeremiah 2:2 recalls the honeymoon period of the wilderness. The NT develops the bridegroom imagery specifically for Jesus (Mark 2:20: the bridegroom is taken away; John 3:29: the friend of the bridegroom rejoices; Eph 5:25-32: husbands love your wives as Christ loved the church; Rev 19:7: the marriage of the Lamb has come).</p>"
  }
}

SONG_CHRIST = {
  "2": {
    "16": "<p>A revelation of God: 'My beloved is mine, and I am his.' The Song's vision of mutual possession between lover and beloved is the OT's most intimate description of the covenant relationship. In the NT, this mutual possession is fulfilled in the Christ-church relationship: 'You are not your own, for you were bought with a price' (1 Cor 6:19-20); 'I am my beloved's and my beloved is mine' becomes 'I live, and yet not I, but Christ lives in me' (Gal 2:20). The mutual knowing of bride and groom (I know my sheep and my sheep know me, John 10:14) is the new covenant's personal form of the Song's mutual possession. The eschatological fulfillment is the marriage of the Lamb (Rev 19:7-9; 21:2): the Song's vision of complete love is consummated in the new creation when the Bride has made herself ready.</p>"
  },
  "8": {
    "6": "<p>A direct revelation: 'Love is strong as death, jealousy is fierce as the grave; its flashes are flashes of fire, the very flame of the LORD.' The Song declares love's unconquerable strength in the face of the two most formidable opponents — death and sheol. The NT's claim is that this declaration is literally, not merely poetically, true in Christ: his love has conquered death (1 Cor 15:54-57: Death is swallowed up in victory; thanks be to God who gives us the victory through our Lord Jesus Christ) and the love of God in Christ is literally unconquerable (Rom 8:38-39: neither death nor life ... shall be able to separate us from the love of God in Christ Jesus our Lord). What the Song celebrates as love's aspiration, the resurrection announces as love's accomplished fact.</p>"
  }
}

def main():
    books = [
        ('job', JOB_ECHO, JOB_ORIGINAL, JOB_CONTEXT, JOB_CHRIST),
        ('proverbs', PROV_ECHO, PROV_ORIGINAL, PROV_CONTEXT, PROV_CHRIST),
        ('ecclesiastes', ECCL_ECHO, ECCL_ORIGINAL, ECCL_CONTEXT, ECCL_CHRIST),
        ('songofsolomon', SONG_ECHO, SONG_ORIGINAL, SONG_CONTEXT, SONG_CHRIST),
    ]
    for book, echo_d, orig_d, ctx_d, chr_d in books:
        e = load_echo(book); merge_echo(e, echo_d); save_echo(book, e)
        c = load_comm('mkt-original', book); merge_comm(c, orig_d); save_comm('mkt-original', book, c)
        c = load_comm('mkt-context', book); merge_comm(c, ctx_d); save_comm('mkt-context', book, c)
        c = load_comm('mkt-christ', book); merge_comm(c, chr_d); save_comm('mkt-christ', book, c)
        print(f'{book}: all 4 layers written')

if __name__ == '__main__':
    main()
