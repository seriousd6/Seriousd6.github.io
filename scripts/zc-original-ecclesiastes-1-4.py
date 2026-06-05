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
