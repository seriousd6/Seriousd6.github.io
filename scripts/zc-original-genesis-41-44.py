"""
Genesis — all four layers (echo + original + context + christ)
Output: data/echoes/genesis.json + mkt-original/genesis.json + mkt-context/genesis.json + mkt-christ/genesis.json

Genesis is the OT's foundational book of origins — of creation, of humanity,
of sin, of promise, and of the Abrahamic covenant that structures all subsequent
OT and NT theology. Its echo patterns run through the entire canon.
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

GEN_ECHO = {
  "1": {
    "1": [
      {"type": "allusion", "target": "John 1:1", "note": "In the beginning God created — John 1:1 deliberately echoes Gen 1:1 (en arche = bereshit); what God did in Gen 1:1 through the word, the Word (Logos) was present to do; the new creation of the gospel is narrated in the same opening cadence as the first creation"},
      {"type": "allusion", "target": "Rev 21:1", "note": "The first heaven and earth (Gen 1:1) will pass away and be replaced by new heavens and new earth; Revelation's new creation is the eschatological bookend to Genesis's original creation"}
    ],
    "26": [
      {"type": "allusion", "target": "Col 3:10", "note": "Made in the image of God (imago Dei) — humanity's creation in the divine image is the basis for the new-creation renewal in Colossians: the new self is being renewed in knowledge after the image of its creator; the image lost in the Fall is restored in Christ"},
      {"type": "allusion", "target": "Rom 8:29", "note": "Predestined to be conformed to the image of his Son — God's original purpose in creating humanity in his image (Gen 1:26) is eschatologically completed in conformity to the image of Christ, the perfect image-bearer"}
    ]
  },
  "2": {
    "7": [
      {"type": "allusion", "target": "1 Cor 15:45", "note": "YHWH formed man from the dust and breathed into his nostrils the breath of life, and man became a living being — Paul quotes Gen 2:7 LXX exactly (psuche zosa) to contrast the first Adam (living soul) with the last Adam (life-giving spirit); the first creation's humanity is the baseline against which the new creation's humanity is measured"},
      {"type": "allusion", "target": "John 20:22", "note": "The risen Christ breathed on them and said Receive the Holy Spirit — the post-resurrection breathing echoes YHWH's breath into Adam; the new creation community receives the same life-giving breath that animated the first humanity, now as the Spirit of the risen Lord"}
    ],
    "24": [
      {"type": "allusion", "target": "Eph 5:31-32", "note": "A man shall leave his father and mother and hold fast to his wife and they shall become one flesh — Paul quotes Gen 2:24 and calls it a profound mystery (<em>mysterion mega</em>) referring to Christ and the church; the one-flesh union of marriage is the type of Christ's union with the church"}
    ]
  },
  "3": {
    "15": [
      {"type": "fulfillment", "target": "Gal 4:4", "note": "I will put enmity between you and the woman, and between your offspring and her offspring — the seed of the woman who crushes the serpent's head is fulfilled when God sent his Son, born of woman, born under the law; the protoevangelium's promised offspring is Christ"},
      {"type": "fulfillment", "target": "Rev 12:9", "note": "That ancient serpent, who is called the devil and Satan, who deceives the whole world — Revelation's identification of the serpent as Satan retroactively clarifies who the Gen 3 serpent was; the Gen 3:15 enmity reaches its climax in Rev 12's cosmic conflict"},
      {"type": "fulfillment", "target": "Rom 16:20", "note": "The God of peace will soon crush Satan under your feet — Paul's benediction applies Gen 3:15 to the Roman church: the bruising of the serpent's head promised in the protoevangelium will be accomplished by the God of peace through the community of Christ; the curse is being reversed"}
    ]
  },
  "4": {
    "4": [
      {"type": "allusion", "target": "Heb 11:4", "note": "By faith Abel offered to God a more acceptable sacrifice than Cain — Genesis's narrative of YHWH's regard for Abel's offering is interpreted in Hebrews as a faith-action; Abel's blood speaks (Heb 12:24), and Jesus's blood speaks better than Abel's"},
      {"type": "allusion", "target": "1 John 3:12", "note": "Not like Cain who was of the evil one and murdered his brother — Cain becomes the NT type of the world's murderous hatred of the righteous; the community that faces hatred for righteousness stands where Abel stood"}
    ]
  },
  "12": {
    "1": [
      {"type": "fulfillment", "target": "Heb 11:8", "note": "By faith Abraham obeyed when he was called to go out to a place that he was to receive as an inheritance — the Abrahamic call and response (lekh-lekha) is interpreted in Hebrews as the paradigmatic faith-obedience: he went out, not knowing where he was going"},
      {"type": "fulfillment", "target": "Acts 7:2-4", "note": "Stephen's speech begins with the God of glory appearing to Abraham in Mesopotamia before he lived in Haran; the Abrahamic call inaugurates salvation history and is the foundational moment Stephen uses to show Israel's God as the God who works outside the land"}
    ],
    "3": [
      {"type": "fulfillment", "target": "Gal 3:8", "note": "In you all the families of the earth shall be blessed — Paul reads the Abrahamic promise as the preaching of the gospel in advance: the Scripture foresaw that God would justify the Gentiles by faith and preached the gospel beforehand to Abraham; the blessing to all nations is fulfilled in the Gentile mission of Christ"}
    ]
  },
  "15": {
    "6": [
      {"type": "fulfillment", "target": "Rom 4:3", "note": "Abraham believed God and it was counted to him as righteousness — Paul's foundational text for justification by faith; Gen 15:6 is cited as the decisive proof that righteousness before God has always been by faith, not by works (since circumcision came later in ch. 17)"},
      {"type": "fulfillment", "target": "Gal 3:6", "note": "Abraham believed God and it was counted to him as righteousness — Paul cites Gen 15:6 to show that the blessing of Abraham comes to the Gentiles through faith, not through Torah-observance; the Galatian churches participate in the Abrahamic faith-righteousness"}
    ]
  },
  "22": {
    "8": [
      {"type": "type", "target": "John 3:16", "note": "God will provide for himself the lamb — the Aqedah (binding of Isaac): Abraham's willingness to sacrifice his only son is the OT type of God the Father giving his Son; 'God himself will provide the lamb' is fulfilled when God provides Christ as the Passover Lamb"},
      {"type": "allusion", "target": "Heb 11:17-19", "note": "By faith Abraham, when he was tested, offered up Isaac, and he who had received the promises was in the act of offering up his only son, of whom it was said: Through Isaac shall your offspring be named — he considered that God was able even to raise him from the dead; the Aqedah is interpreted as a resurrection-typology: Isaac's deliverance from death prefigured Christ's resurrection"}
    ]
  },
  "28": {
    "12": [
      {"type": "fulfillment", "target": "John 1:51", "note": "Jacob's ladder with angels ascending and descending — Jesus applies the Jacob's ladder vision to himself: you will see heaven opened and the angels of God ascending and descending on the Son of Man; Christ is the ladder/stairway between heaven and earth, the meeting point of divine and human"}
    ]
  },
  "37": {
    "28": [
      {"type": "type", "target": "Acts 7:9", "note": "Joseph sold by his brothers for twenty pieces of silver — Stephen's speech identifies the Joseph narrative as a type of the rejection of Christ by his own people; as the patriarchs were jealous of Joseph and sold him, so they rejected Christ"}
    ]
  },
  "49": {
    "10": [
      {"type": "fulfillment", "target": "Rev 5:5", "note": "The scepter shall not depart from Judah nor the ruler's staff from between his feet, until tribute comes to him — the Lion of the tribe of Judah in Revelation is the fulfillment of Jacob's blessing on Judah; the royal authority of Gen 49:10 is Christ's eschatological sovereignty"}
    ]
  }
}

GEN_ORIGINAL = {
  "1": {
    "1": "<p><strong>bereshit bara elohim</strong> (<em>bĕrēʾšît bārāʾ ʾĕlōhîm</em>): 'In the beginning God created.' Three initial philological observations: (1) <em>bereshit</em> (in the beginning) is in construct state — the absolute beginning, not 'in a beginning of'; (2) <em>bara</em> (created) is used in the OT exclusively with God as subject and without specification of material — implying creation from nothing (<em>ex nihilo</em>), not merely formation from pre-existing chaos; (3) <em>Elohim</em> is grammatically plural but takes a singular verb (<em>bara</em>) — the plural of majesty, or early evidence of the complexity that later theology would develop as Trinity. The first word of Scripture establishes the fundamental theological axiom: God, not chaos, not a pantheon, not nature, is the origin of all things.</p>",

    "26": "<p><strong>naase adam betsalmenu kidmutenu</strong> (<em>naʿăśeh ʾādām bĕṣalmēnû kidmûtēnû</em>): 'Let us make humanity in our image, after our likeness.' The divine plural (<em>naase</em>, let us; <em>tsalmenu</em>, our image) has generated three interpretive traditions: (1) a plural of majesty; (2) God consulting the heavenly court of angels (cf. Job 1:6; Isa 6:8); (3) an early intra-divine address (Trinitarian foreshadowing, as the Church Fathers read it). <em>Tselem</em> (image) is the word used for cult-statues representing a deity — in ancient Near Eastern thought, the king was the <em>tselem</em> of the gods, their representative and regent. By applying this to all humanity, Genesis democratizes the royal-priestly image: every human, not just the king, represents the divine presence on earth and exercises dominion on behalf of the divine.</p>"
  },
  "2": {
    "7": "<p><strong>wayyitser YHWH Elohim et-haadam afar min-haadam wayyipach beapav nishmat hayyim wayyehi haadam lenefesh hayyah</strong>: 'YHWH God formed the man of dust from the ground and breathed into his nostrils the breath of life, and the man became a living creature (<em>nefesh hayyah</em>).' Two observations: (1) <em>wayyitser</em> (formed) uses the imagery of the potter (<em>yatsar</em>) — human embodiment is the result of divine craftsmanship, not accident; (2) <em>nishmat hayyim</em> (breath of life) — the identical phrase is used for all animals in 7:22; what distinguishes humanity is not the breath but the preceding formation in the divine image (1:26-27) and the naming task (2:19-20). <em>Nefesh hayyah</em> (living being/soul) is not a Platonic immortal soul but the whole animated creature — biblical anthropology is holistic: the person is the ensouled body, not a soul housed in a body.</p>",

    "24": "<p><strong>al-ken yaazov ish et-aviv veimmo vedavak beishto vehayyu levasar echad</strong> (<em>ʿal-kēn yaʿăzŏv ʾîš ʾet-ʾābîw wĕʾimmô wĕdābaq bĕʾištô wĕhāyû lĕbāśār ʾeḥād</em>): 'Therefore a man shall leave his father and his mother and hold fast to his wife, and they shall become one flesh.' The narrative aside (<em>al-ken</em>, therefore/for this reason) signals a foundational principle being derived from the narrative. <em>Davak</em> (hold fast/cleave) is the same word used for Israel's covenant-commitment to YHWH (Deut 10:20; Josh 23:8) — marital union is described in covenant-fidelity language. <em>Basar echad</em> (one flesh): not merely physical union but a comprehensive sharing of life, identity, and destiny — which is why Paul calls it a 'profound mystery' (<em>mysterion mega</em>) of the Christ-church relationship.</p>"
  },
  "3": {
    "15": "<p><strong>veevah asit beincha uvein haisha uvein zaracha uvein zarah tshuv yeshuphenu rosh veata teshuphenu akev</strong>: 'I will put enmity between you and the woman, and between your offspring and her offspring; he shall bruise your head, and you shall bruise his heel.' The <em>protoevangelium</em> (first gospel). Key philological issues: (1) The singular <em>zarah</em> (offspring) combined with the masculine singular pronoun <em>hu</em> (he) in the LXX translated as masculine singular <em>autos</em> — a masculine seed of the woman — though the Hebrew <em>zera</em> is collectively singular and the pronoun could be collective. Jewish midrash and Church Fathers both recognized the Messianic potential; (2) <em>shuph</em> (bruise/strike): used for both the heel-strike and the head-strike with the same verb — the same action, different targets, different outcomes. The serpent's strike is temporary (heel); the seed's strike is fatal (head).</p>"
  },
  "15": {
    "6": "<p><strong>vehemin baYHWH wayyachsheveha lo tsedaqah</strong> (<em>wĕheʾĕmīn bY̌HWH wayyaḥšĕbehā lô ṣĕdāqāh</em>): 'And he believed YHWH, and he counted it to him as righteousness.' The most theologically dense sentence in Genesis. <em>Heamin</em> (believed/trusted): Hiphil of <em>aman</em> — not merely intellectual assent but the full posture of reliable trust, the same root as <em>amen</em>. <em>Wayachsheveha</em> (counted/reckoned/credited): the accounting verb used in financial and legal contexts — credit assigned. <em>Tsedaqah</em> (righteousness): the right-relational standing before God that Abraham receives not by doing but by trusting. Paul (Rom 4:3; Gal 3:6) and James (2:23) both cite this verse as definitional for faith-righteousness; their different emphases (Paul: before circumcision, therefore not by works; James: completed by the Aqedah of ch. 22, therefore enacted by obedience) are both grounded in the canonical shape of Genesis.</p>"
  },
  "22": {
    "14": "<p><strong>YHWH yireh asher yeamer hayom behar YHWH yeraeh</strong> (<em>Yhwh yirʾeh ... ʾăšer yēʾāmēr hayyôm bĕhar Yhwh yērāʾeh</em>): 'YHWH will provide / YHWH will be seen.' The name <em>YHWH-Yireh</em> (<em>YHWH will see/provide</em>) is a word-play: <em>raah</em> means both 'see' and 'provide' (to see to it = to provide). The place-name combines both meanings: on this mountain YHWH sees and is seen. The site is identified with Jerusalem and eventually Mount Moriah (2 Chr 3:1), where Solomon built the temple. The Aqedah's theology: the provision of the ram in place of Isaac establishes the substitution-pattern that the entire sacrificial system develops and that Christ fulfills finally.</p>"
  },
  "49": {
    "10": "<p><strong>lo yasur shevet miYehudah umechokek mibein raglav ad ki yavo shiloh velo yiqqehat amim</strong>: 'The scepter shall not depart from Judah, nor the ruler's staff from between his feet, until tribute comes to him; and to him shall be the obedience of the peoples.' <em>Shiloh</em>: the most debated word in Jacob's blessing. Major interpretations: (1) a place name (Shiloh in Ephraim — problematic geographically); (2) a form of <em>sheloh</em> = 'whose it is' (Ezek 21:27 uses similar language); (3) a Messianic title derived from <em>shalom</em> (peace). The LXX reads 'until what is reserved for him comes' — pointing toward a coming ruler. Christian and early Jewish messianic readings consistently identified this as a promise of a coming king who would gather the nations.</p>"
  }
}

GEN_CONTEXT = {
  "1": {
    "1": "<p>Genesis was composed in a world where Babylonian and Canaanite creation myths provided the dominant cosmological framework. The <em>Enuma Elish</em> (Babylonian creation epic, ca. 18th century BCE or earlier in its oral form) portrays creation as emerging from conflict between Marduk and Tiamat (the chaos-water), with humans created from the blood of a slain god to serve the gods. The <em>Atra-hasis</em> similarly portrays humanity as created to do menial labor for gods. Genesis's polemic: creation comes not from divine conflict but from divine speech; creation is not chaotic violence but ordered goodness; humanity is not divine labor-fodder but the image-bearing vice-regent of YHWH. The literary parallels (waters, light, land, creatures, rest) show cultural contact; the theological inversions show deliberate counter-testimony.</p>"
  },
  "6": {
    "5": "<p>The Flood narrative (Gen 6-9) has its closest literary parallel in the <em>Epic of Gilgamesh</em> (Tablet XI), in which Utnapishtim survives a flood sent by the gods, builds a boat, releases birds, offers sacrifice on the mountain. Earlier, the <em>Atra-hasis</em> epic provides an even closer parallel to the Genesis flood. The similarities (flood, boat, birds, sacrifice, rainbow-equivalent) are real and have generated both 'common source' theories (shared Mesopotamian memory of a regional catastrophe) and 'polemical adaptation' theories (Israel renarrates the flood with YHWH as the sole sovereign actor, eliminating the capricious divine conflict of the Babylonian originals). Key theological differences: in Genesis the flood has a clear moral rationale (human wickedness, v. 5) and is followed by a covenant (ch. 9), not arbitrary divine caprice.</p>"
  },
  "12": {
    "1": "<p>The patriarchal age (Abraham ca. 2000-1700 BCE in traditional dating) corresponds archaeologically to the Middle Bronze Age, when semi-nomadic herder-farmers ('Amorites' in Mesopotamian records) moved through the Fertile Crescent. Texts from Nuzi (Hurrian city, 15th century BCE) and Mari (on the Euphrates, 18th century BCE) illuminate social customs in Genesis: adoption of slaves as heirs (Gen 15:2-4 paralleled in Nuzi adoption texts), the levirate custom, and treaty-covenant forms that match the patriarchal covenant narratives. While no extrabiblical text names Abraham, Isaac, or Jacob, the social-legal background of Genesis 12-50 is consistent with the Middle Bronze Age rather than the Iron Age context in which later OT books were written.</p>"
  },
  "15": {
    "17": "<p>The covenant-making ceremony of Genesis 15 — animals cut in half, a smoking firepot and flaming torch passing between the pieces — follows a well-documented ancient Near Eastern covenant ritual (cf. Jer 34:18-19 where covenant-breakers are threatened with the fate of the divided animal). The typical ritual required both parties to walk between the pieces, committing themselves to the same fate if they broke the covenant. In Gen 15, only YHWH passes through (the smoking firepot and torch = divine theophanic manifestation): the Abrahamic covenant is unilateral — God alone binds himself, making the promise unconditional on Abraham's performance. The covenant is YHWH's oath to Abraham, not a bilateral contract requiring Abraham's sustained compliance.</p>"
  },
  "22": {
    "1": "<p>The Aqedah (binding of Isaac, Gen 22) has been the most interpreted passage in Jewish history. The Mishnah, Talmud, and rabbinic midrash developed elaborate theologies around Isaac's willingness (not just Abraham's obedience): the <em>Mekhilta</em> and <em>Pirke de-Rabbi Eliezer</em> describe Isaac as a willing adult (identified as 37 years old by some traditions) who offered himself. The merit of the Aqedah (<em>zekhut Aqedah</em>) became in some rabbinic traditions an intercessory resource for Israel. Early Christian typology (Paul, Hebrews, John) saw the Aqedah as the supreme OT type of the Father giving his Son and the Son willingly going to death. The ram caught in the thicket provided the substitutionary sacrifice that Isaac's deliverance required — the pattern for the atonement.</p>"
  },
  "37": {
    "1": "<p>The Joseph narrative (Gen 37-50) is widely recognized as the most literarily sophisticated narrative in the Hebrew Bible — a novella with psychological depth, ironic plot reversals, and careful narrative control. Its Egyptian setting (Gen 39-47) is consistent with the Second Intermediate Period (ca. 1650-1550 BCE, Hyksos rule) when Semitic people could attain positions of influence in Egypt. The Potiphar's wife episode (ch. 39) has a literary parallel in the Egyptian 'Tale of Two Brothers,' though the theological emphasis on Joseph's integrity and YHWH's providential presence (<em>YHWH was with Joseph</em>, 39:2, 21, 23) is distinctively Israelite. The entire narrative is framed as the theodicy of providence: what the brothers meant for evil, God meant for good (50:20).</p>"
  }
}

GEN_CHRIST = {
  "1": {
    "26": "<p>A shadow: 'Let us make humanity in our image, after our likeness.' The imago Dei in Genesis is the first shadow of the ultimate image of God, who is Christ (2 Cor 4:4; Col 1:15). Humanity was created to bear God's image — to represent God in the world. The Fall distorted the image without destroying it (Gen 9:6 still assumes the image as the basis for human dignity). Christ is the image that humanity was always meant to embody: perfectly representing the Father, exercising dominion over creation, fulfilling the cultural mandate. The redemption of humanity is therefore the restoration of the image in and through the one who is himself the image — conformity to Christ is the telos of creation.</p>"
  },
  "2": {
    "17": "<p>A shadow: 'But of the tree of the knowledge of good and evil you shall not eat, for in the day that you eat of it you shall surely die.' The death-warning is the first statement of the law-death nexus that Paul develops in Romans 5-6 and 1 Corinthians 15: sin brings death, death reigns through Adam. The prohibition is not arbitrary but reflects the order of creation: the creature's flourishing depends on remaining within the Creator's boundaries. The shadow: as Adam's transgression brought death, Christ's obedience brings life (Rom 5:18-19). The new tree — the cross — reverses the curse of the old tree.</p>"
  },
  "3": {
    "15": "<p>A fulfillment (first promise, final fulfillment): 'He shall bruise your head and you shall bruise his heel.' The protoevangelium is the most foundational Christological promise in Scripture — the first statement that the serpent's work will be undone by a coming seed of the woman. The bruising of the heel (the crucifixion, the apparent defeat of Christ) and the crushing of the head (the resurrection that undoes the devil's power over death, Heb 2:14) are both within the scope of the single promise. Christ's entire work — Incarnation (born of woman), crucifixion (heel-bruise), and resurrection (head-crushing) — fulfills what Gen 3:15 compressed into one prophetic sentence.</p>"
  },
  "15": {
    "6": "<p>A direct revelation: 'He believed YHWH, and he counted it to him as righteousness.' The reckoning of faith as righteousness — credited by grace before circumcision, before the law, before any works — is the OT's own testimony that justification has always been by faith. Paul's argument in Romans 4 and Galatians 3 is not that the NT overturns the OT but that the NT has always been true: Abraham, the father of the faithful, received righteousness as a gift of trust. The revelation of righteousness through faith in Christ is the full disclosure of what God was doing in Gen 15:6 when he credited Abraham's faith as righteousness.</p>"
  },
  "22": {
    "13": "<p>A type: 'Abraham lifted up his eyes and looked, and behold, behind him was a ram, caught in a thicket by his horns. And Abraham went and took the ram and offered it up as a burnt offering instead of his son.' The substitutionary ram is the most explicit type of substitutionary atonement in the OT. The ram dies in Isaac's place: the innocent substituted for the guilty who was also the beloved son. The location (Moriah, later Jerusalem) and the typological pattern (father giving son, son willingly going, ram substituted) form the OT's clearest foreshadowing of the cross. The Aqedah is the type; Calvary is the antitype — where the Father did not withhold his only Son (Rom 8:32 deliberately echoes Gen 22:16), and no ram was provided.</p>"
  },
  "37": {
    "28": "<p>A type: Joseph was sold by his brothers for twenty pieces of silver into slavery in Egypt, rejected by his own, yet rose to save the world and his brothers who betrayed him. Joseph is the OT's most fully developed type of Christ: rejected by his own → suffering servant → exalted to the right hand of power → reconciling the very ones who betrayed him → saving many alive. The pattern is so close that Stephen devotes the Joseph narrative's typological center of his Acts 7 speech to it. Unlike Christ, Joseph is not a sinless substitute — but the career-pattern of rejection → exaltation → salvation is the Christological trajectory the Joseph narrative enshrines.</p>"
  },
  "49": {
    "10": "<p>A fulfillment: 'The scepter shall not depart from Judah, nor the ruler's staff from between his feet, until tribute comes to him; and to him shall be the obedience of the peoples.' Jacob's blessing on Judah is the foundational Messianic oracle: from Judah's line will come the ultimate ruler to whom all nations submit. The historical sequence: David (from Judah, 2 Sam 7); David's greater Son promised (Ps 2; Isa 11); Christ as 'Lion of the tribe of Judah, Root of David' (Rev 5:5). The scepter finally rests permanently with the risen and enthroned Christ whose kingdom is without end (Luke 1:32-33).</p>"
  }
}

def main():
    e = load_echo('genesis')
    merge_echo(e, GEN_ECHO)
    save_echo('genesis', e)
    print(f'Genesis echo: {len(e)} chapters, {sum(len(v) for v in e.values())} verses')

    c = load_comm('mkt-original', 'genesis')
    merge_comm(c, GEN_ORIGINAL)
    save_comm('mkt-original', 'genesis', c)
    print(f'Genesis original: {len(c)} chapters, {sum(len(v) for v in c.values())} verses')

    c = load_comm('mkt-context', 'genesis')
    merge_comm(c, GEN_CONTEXT)
    save_comm('mkt-context', 'genesis', c)
    print(f'Genesis context: {len(c)} chapters, {sum(len(v) for v in c.values())} verses')

    c = load_comm('mkt-christ', 'genesis')
    merge_comm(c, GEN_CHRIST)
    save_comm('mkt-christ', 'genesis', c)
    print(f'Genesis christ: {len(c)} chapters, {sum(len(v) for v in c.values())} verses')

if __name__ == '__main__':
    main()
