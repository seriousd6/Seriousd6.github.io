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
  "8": {
    "6": "<p><strong>simeini kachotam al libecha kachotam al zeroa'echa ki azza kamavet ahavah qasha kishol qina'ah reshefeyha reshefei esh shalhevetyah</strong>: 'Set me as a seal upon your heart, as a seal upon your arm, for love is strong as death, jealousy is fierce as the grave. Its flashes are flashes of fire, the very flame of the LORD.' The climax of the Song's celebration of love: it is as strong as death and as fierce as <em>sheol</em> — the two most powerful forces in human experience. <em>Shalhevetyah</em> (the very flame of the LORD) — uniquely, this is one of the few places in the Song where the divine name appears, even embedded in a word. The NT's fulfillment: the love of Christ has defeated death (1 Cor 15:54-57) and nothing can separate us from that love (Rom 8:38-39); what the Song claimed about love's unconquerability is literally true in Christ's resurrection.</p>"
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
  "7": {
    "1": "<p>A type: the Shulammite is called out of her dancing to be seen — the invitation to appear before the bridegroom who celebrates her. Christ calls his church out of hiddenness and shame into the visibility of his own approval: 'You are the light of the world. A city set on a hill cannot be hidden' (Matt 5:14). The <em>machola ha-machanayim</em> (dance of two camps) invokes the Mahanaim of Gen 32 — the site of Jacob&rsquo;s encounter with the angel-army of God. The beloved who dances between two heavenly camps is the church who belongs to two worlds — she dances at the intersection of earth and heaven, already held by the one who crossed from heaven to earth to find her.</p>",
    "2": "<p>A type: the bridegroom&rsquo;s detailed description of the beloved&rsquo;s body as the site of abundance — the navel like a bowl of wine, the belly like a mound of wheat — speaks to his delight in the whole person God has made. Christ&rsquo;s love for the church is not a spiritual abstraction that ignores her embodied existence; it is the love of the Creator for what he made and declared good (Gen 1:31). The body is the temple of the Holy Spirit (1 Cor 6:19), and Christ&rsquo;s declaration of the body&rsquo;s beauty is the theological ground for bodily resurrection: the same body he declares beautiful, he will raise.</p>",
    "3": "<p>A type: the repeated twin-fawns image (cf. 4:5) is the Song&rsquo;s characteristic repetition — the same praise spoken again with fresh delight. Christ&rsquo;s love for the church does not diminish through familiarity; it speaks the same declarations of beauty from generation to generation. The pastoral imagery (gazelle, twins, fawns) places the beloved in the created order that Christ made and entered: the Good Shepherd who knows his own (John 10:14) delights in them with the same fresh attentiveness as a shepherd delights in young animals in the spring.</p>",
    "4": "<p>A type: the church&rsquo;s neck like an ivory tower speaks to the unyielding faithfulness of the church&rsquo;s witness — the community that does not bend to cultural pressure. The eyes like the pools of Heshbon describe the depth and clarity of faith that sees clearly. Christ commissions this quality in his church: &lsquo;let your eyes be healthy so that your whole body is full of light&rsquo; (Matt 6:22). The nose facing Damascus — the city of Paul&rsquo;s conversion and of the Gentile mission — is the prophetic posture of the church directed outward toward the world she is called to serve.</p>",
    "5": "<p>A type: the head like Carmel (the majestic promontory) and the flowing locks that capture the king speak to the church&rsquo;s dignity and the paradoxical power of faith over Christ: he who &lsquo;holds all things together&rsquo; (Col 1:17) is &lsquo;captured&rsquo; by the church&rsquo;s beauty — a beauty he himself gave her (Eph 5:26-27). This is the kenosis reversed: the one who emptied himself and humbled himself (Phil 2:7-8) is now, from his position of exaltation, captivated by the church he redeemed. The purple locks (the royal color) placed on the beloved by the bridegroom&rsquo;s love are the royal priesthood that Christ confers on the church (1 Pet 2:9).</p>",
    "6": "<p>A type: &lsquo;How fair and pleasant you are, O love, with all your delights!&rsquo; is the summary declaration of the bridegroom&rsquo;s delight in the beloved. Christ&rsquo;s delight in the church is the love that preceded the cross — he endured the cross &lsquo;for the joy set before him&rsquo; (Heb 12:2), and the church is part of that joy. Zeph 3:17 provides the fullest OT statement of this divine delight: &lsquo;The LORD your God is in your midst, a mighty one who will save; he will rejoice over you with gladness; he will quiet you by his love; he will exult over you with loud singing.&rsquo; The Song&rsquo;s bridegroom-delight is the experiential image of the divine rejoicing-over that Zephaniah proclaims.</p>",
    "7": "<p>A type: the beloved&rsquo;s stature like a date palm is the image of the church planted, rooted, and bearing fruit. Ps 92:12 declares: &lsquo;the righteous flourish like the palm tree.&rsquo; The church is the community of the righteous planted by Christ; her fruit clusters (Eph 5:9, the fruit of light) are what the Bridegroom comes to taste. The palm tree is also the tree of victory — the palm branches of the triumphal entry (John 12:13) and of the great multitude who stand before the throne (Rev 7:9). The beloved-as-palm-tree is the church whose dignity Christ proclaims.</p>",
    "8": "<p>A type: &lsquo;I say I will climb the palm tree and lay hold of its fruit-clusters.&rsquo; The bridegroom&rsquo;s declaration of intentional pursuit is the Incarnation-movement translated into the language of love: Christ came to &lsquo;lay hold&rsquo; of the church (Heb 2:16: &lsquo;he does not lay hold of angels but of the offspring of Abraham&rsquo;). The same Greek verb <em>epilambanomai</em> (to take hold of) appears in Heb 2:16 and describes precisely the incarnational reaching: God extended his hand into creation and took hold of human flesh in order to take hold of human persons. The climbing and reaching of Song 7:8 is the poetry that Hebrews makes literal.</p>",
    "9": "<p>A type: the mouth of the beloved like the best wine going down smoothly — the reciprocity of love in which the church&rsquo;s prayer is heard as the most exquisite speech by Christ, who desires to hear her voice (cf. 2:14, &lsquo;let me hear your voice, for your voice is sweet&rsquo;). Christ invites the church into the communication of prayer: &lsquo;ask, and it will be given to you&rsquo; (Matt 7:7); &lsquo;abide in me, and ask whatever you wish&rsquo; (John 15:7). The beloved&rsquo;s voice that the bridegroom savors as wine is the church&rsquo;s prayer received by Christ as the most precious thing she offers.</p>",
    "10": "<p>A direct revelation: &lsquo;I am my beloved&rsquo;s, and his desire is for me.&rsquo; The word <em>teshuqah</em> (desire/longing) here reverses Gen 3:16&rsquo;s distorted desire: where the fall introduced a desire entangled with domination, the Song restores the desire that is pure self-giving love. Christ&rsquo;s desire for the church is the redemptive desire that is enacted in the cross: he desired to redeem what was lost, and &lsquo;for the joy set before him he endured the cross&rsquo; (Heb 12:2). His desire brought him through death for the church. The beloved&rsquo;s declaration &lsquo;his desire is for me&rsquo; is the church&rsquo;s assurance that she is the specific object of Christ&rsquo;s redemptive longing — not an afterthought but the goal of the Incarnation.</p>",
    "11": "<p>A type: &lsquo;Come, my beloved, let us go out into the fields.&rsquo; The beloved&rsquo;s invitation to Christ to go with her into the world is the church&rsquo;s missionary movement. The fields (<em>sadeh</em>) in the parable of the sower (Matt 13:38) are the world; the church goes into that world not alone but with the Bridegroom: &lsquo;Go therefore and make disciples of all nations&hellip; and behold, I am with you always&rsquo; (Matt 28:19-20). The church&rsquo;s invitation to Christ to come with her into the harvest-field is the prayer that precedes mission. The Lord of the harvest goes with the laborers he sends.</p>",
    "12": "<p>A type: the vineyard inspection — checking whether the vine has sprouted, the blossoms opened, the pomegranates flowered — is the church&rsquo;s examination of her own fruitfulness before the return of the Bridegroom. Christ inspects the churches (Rev 2-3, the letters to the seven churches) with the same care the bridegroom brings to the vineyard: what is bearing fruit, what needs pruning, what has not yet bloomed. The beloved&rsquo;s declaration &lsquo;there I will give you my love&rsquo; is the church&rsquo;s self-offering in the place of productive service — she gives herself most fully in the context of fruitfulness.</p>",
    "13": "<p>A type: the mandrakes giving fragrance and the precious fruits stored up — new and old — for the beloved represent the church&rsquo;s accumulated offering to Christ. The early church leader who brings &lsquo;out of his treasure what is new and what is old&rsquo; (Matt 13:52) is the steward of the household of God who has stored both the ancient Scriptures and the new revelation of Christ. The church&rsquo;s all-things-for-you is the participation in the Spirit&rsquo;s work of preparing the Bride: &lsquo;the Spirit and the Bride say, &ldquo;Come&rdquo;&rsquo; (Rev 22:17) — and the Bride comes with her hands full of gifts for the Bridegroom.</p>"
  },
  "8": {
    "1": "<p>A direct revelation: &lsquo;O that you were like a brother to me.&rsquo; The Incarnation is the answer to the exact longing of this verse: Christ became the church&rsquo;s &lsquo;brother&rsquo; in the most complete sense, so that she could embrace him publicly without shame. Heb 2:11-12 is the fulfillment: &lsquo;he is not ashamed to call them brothers, saying, &ldquo;I will tell of your name to my brothers; in the midst of the congregation I will sing your praise.&rdquo;&rsquo; The social shame that the beloved feared (being looked down upon for public embrace) is precisely what Christ absorbs in the crucifixion: &lsquo;despised and rejected by men, a man of sorrows&rsquo; (Isa 53:3). The shame that social convention threatened, Christ took; the brotherhood the beloved longed for, Christ became.</p>",
    "2": "<p>A type: &lsquo;I would bring you into my mother&rsquo;s house&rsquo; — the deepest hospitality, offering the most intimate domestic space to the beloved. The Lord&rsquo;s Supper is the church&rsquo;s bringing of Christ into her house — the table set with the spiced wine and the bread that Christ provided. &lsquo;Behold, I stand at the door and knock. If anyone opens the door, I will come in to him and eat with him, and he with me&rsquo; (Rev 3:20). The beloved&rsquo;s offering of pomegranate nectar and spiced wine to the one she brings into her house is the church&rsquo;s eucharistic act — she receives the Bridegroom&rsquo;s gift and offers her own thanksgiving in return.</p>",
    "3": "<p>A type: the left-hand-under-the-head and right-hand embrace — the total protective posture — is the church&rsquo;s experience of Christ&rsquo;s holding of her. Deut 33:27: &lsquo;the eternal God is your dwelling place, and underneath are the everlasting arms.&rsquo; John 10:28-29: &lsquo;I give them eternal life, and they will never perish, and no one will snatch them out of my hand. My Father, who has given them to me, is greater than all, and no one is able to snatch them out of the Father&rsquo;s hand.&rsquo; The Song&rsquo;s intimate embrace is the physical image of the theological guarantee of perseverance: the church is held from below (the left hand) and surrounded (the right hand).</p>",
    "4": "<p>A type: the adjuration not to stir up love until it pleases is the church&rsquo;s posture of waiting for the parousia. Jas 5:7-8: &lsquo;Be patient, therefore, brothers, until the coming of the Lord. See how the farmer waits for the precious fruit of the earth, being patient about it, until it receives the early and the late rains. You also, be patient. Establish your hearts, for the coming of the Lord is at hand.&rsquo; The love that &lsquo;cannot be forced&rsquo; is the eschatological love that arrives in its own time — and the church that has experienced its fullness knows not to try to manufacture what only God can give. The patience of the refrain is the patience of the eschatological people.</p>",
    "5": "<p>A type: &lsquo;Who is this coming up from the wilderness, leaning on her beloved?&rsquo; The Incarnation is God coming &lsquo;up from the wilderness&rsquo; of human history, and the church who leans on him is already being carried by his strength. Isa 40:31: &lsquo;they who wait for the LORD shall renew their strength; they shall mount up with wings like eagles.&rsquo; The apple tree under which the beloved was born — and under which his mother bore him — is the specific place of new life; Christ was born in the lowliest of places (the manger, like a hidden apple tree in the wilderness) so that the church could find her beginning under his shade. The one who comes up from the wilderness is also the one who was tempted in the wilderness (Matt 4:1-11) and came through it to begin his public ministry of love.</p>",
    "6": "<p>A direct revelation: &lsquo;Love is strong as death, jealousy is fierce as the grave; its flashes are flashes of fire, the very flame of the LORD.&rsquo; The Song declares love&rsquo;s unconquerable strength in the face of the two most formidable opponents — death and sheol. The NT&rsquo;s claim is that this declaration is literally, not merely poetically, true in Christ: his love has conquered death (1 Cor 15:54-57: Death is swallowed up in victory; thanks be to God who gives us the victory through our Lord Jesus Christ) and the love of God in Christ is literally unconquerable (Rom 8:38-39: neither death nor life shall be able to separate us from the love of God in Christ Jesus our Lord). What the Song celebrates as love&rsquo;s aspiration, the resurrection announces as love&rsquo;s accomplished fact.</p>",
    "7": "<p>A direct revelation: &lsquo;Many waters cannot quench love, neither can floods drown it. If a man offered all the wealth of his house for love, it would be utterly scorned.&rsquo; The flood-chaos imagery (many waters, rivers) represents the full force of opposition — persecution, death, the powers arrayed against the church. Christ&rsquo;s love for the church has passed through the flood-chaos of the cross and emerged unquenched: &lsquo;neither death nor life, nor angels nor rulers, nor things present nor things to come, nor powers, nor height nor depth, nor anything else in all creation, will be able to separate us from the love of God in Christ Jesus our Lord&rsquo; (Rom 8:38-39). The contempt for the man who tries to buy love with wealth is the Song&rsquo;s rejection of the commercial model of salvation — grace cannot be purchased, only received.</p>",
    "8": "<p>A type: the brothers&rsquo; care for the little sister not yet developed anticipates Christ&rsquo;s protection of the immature and small in his kingdom. &lsquo;See that you do not despise one of these little ones. For I tell you that in heaven their angels always see the face of my Father who is in heaven&rsquo; (Matt 18:10). The brothers who deliberate about what to do for their sister before she is marriageable represent the care of the community for the young and vulnerable — a care that Christ himself models: he rebukes the disciples for turning away children (Matt 19:14) and declares that the kingdom belongs to such. The church&rsquo;s care for her little ones is the echo of the brothers&rsquo; protective love.</p>",
    "9": "<p>A type: the wall/door discernment — responding to what the beloved is with appropriate care — is the pattern of Christ&rsquo;s pastoral knowledge of the church. Rev 2-3 (the letters to the seven churches) shows Christ applying exactly this discernment: to Smyrna (strong under persecution) he gives honor; to Laodicea (lukewarm) he offers the correction that secures. Christ&rsquo;s knowledge of his church is complete and particular: he does not apply the same pastoral response to every situation but responds to what each church actually is. The grace that fortifies the wall and secures the door is the grace of the divine Physician who knows the condition of each patient.</p>",
    "10": "<p>A direct revelation: &lsquo;I am a wall, and my breasts are like towers; thus I have become in his eyes as one who finds <em>shalom</em>.&rsquo; The church that is a wall — firm in faith, not dissolved by pressure — becomes in Christ&rsquo;s eyes the bearer of his own peace. Christ is the Prince of Peace (<em>sar shalom</em>, Isa 9:6); the church that embodies his character of integrity becomes the instrument of his <em>shalom</em>. Phil 4:7: &lsquo;the peace of God, which surpasses all understanding, will guard your hearts and your minds in Christ Jesus.&rsquo; The guarding-peace of God is the tower that the church becomes in Christ&rsquo;s eyes when she stands firm. The <em>shalom</em>/<em>shlomoh</em> wordplay is christological: the beloved who finds <em>shalom</em> finds it through her union with the Solomon-Bridegroom who is himself Peace.</p>",
    "11": "<p>A type: Solomon&rsquo;s vineyard at Baal-Hamon, leased to keepers for silver, is the image of the world-vineyard managed by imperfect stewards — the parable of the wicked tenants (Matt 21:33-41). Christ is the owner of the vineyard (John 15:1: &lsquo;I am the true vine, and my Father is the vinedresser&rsquo;) who has entrusted the care of his vineyard to the church. The thousand silver pieces due to Solomon anticipate the accountability that the parable foregrounds: the servants who were given the vineyard must account for what it produced. The church is the faithful tenant who returns not just the rent but the fruit itself.</p>",
    "12": "<p>A type: &lsquo;My own vineyard is before me; the thousand are for you, O Solomon.&rsquo; The church&rsquo;s free self-gift — &lsquo;my vineyard is mine to give, and I give it to you&rsquo; — is the mirror of Christ&rsquo;s own free self-giving: &lsquo;No one takes [my life] from me, but I lay it down of my own accord&rsquo; (John 10:18). The reciprocity is the heart of the covenant: Christ gives himself freely for the church (Eph 5:25), and the church responds by freely giving herself to Christ (2 Cor 8:5: &lsquo;they gave themselves first to the Lord&rsquo;). The vineyard that is freely given anticipates the New Jerusalem where all things are freely given: &lsquo;to the thirsty I will give from the spring of the water of life without payment&rsquo; (Rev 21:6).</p>",
    "13": "<p>A type: &lsquo;O you who dwell in the gardens, with companions listening for your voice — let me hear it.&rsquo; Christ&rsquo;s desire to hear the church&rsquo;s voice is the motive for prayer: he invites, even requests, the voice of the one he loves. The companions listening are the cosmic witnesses — the angels who &lsquo;long to look&rsquo; into the gospel (1 Pet 1:12) and gather around the worship of the church to hear the voice of the people God has redeemed. The church&rsquo;s worship is a cosmic event heard by the heavenly assembly: &lsquo;you have come to Mount Zion and to the city of the living God, the heavenly Jerusalem, and to innumerable angels in festal gathering&rsquo; (Heb 12:22). Every time the church gathers to pray, her voice goes out to a gallery that extends beyond what she can see.</p>",
    "14": "<p>A direct revelation: &lsquo;Flee, my beloved, and be like a gazelle or a young stag on the mountains of spices.&rsquo; The Song&rsquo;s final line is the church&rsquo;s cry for the parousia. The beloved running swiftly over the fragrant mountains is the return of Christ that the whole NT ends with: &lsquo;Amen. Come, Lord Jesus!&rsquo; (Rev 22:20). The invitation to flight/swift return — <em>berach dodi</em> (flee, my beloved) — is not dismissal but the urgency of longing: come quickly. The Song that began with &lsquo;let him kiss me with the kisses of his mouth&rsquo; (1:2) ends with the beloved in motion, still coming. The incompleteness of the ending is the &lsquo;not yet&rsquo; of the eschatological kingdom: the Bridegroom is on his way, and the Bride waits and calls for his coming.</p>"
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
