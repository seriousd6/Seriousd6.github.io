"""
Isaiah — all four layers (echo + original + context + christ)
Output: data/echoes/isaiah.json + mkt-original + mkt-context + mkt-christ

Isaiah is the NT's most cited OT prophet — roughly 419 citations or allusions.
The book divides into two major sections (1-39: judgment; 40-66: comfort/servant)
with the Servant Songs (42:1-4; 49:1-6; 50:4-9; 52:13-53:12) as the NT's
most foundational OT Christological resource.
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

ISA_ECHO = {
  "6": {
    "1": [
      {"type": "fulfillment", "target": "John 12:41", "note": "Isaiah saw his glory and spoke of him — John identifies the YHWH whose glory Isaiah saw in the throne-vision (Isa 6:1-4) with the pre-incarnate Christ; the seraphim's Trisagion is the worship of the Son before the Incarnation"}
    ],
    "9": [
      {"type": "fulfillment", "target": "Matt 13:14-15", "note": "You will indeed hear but never understand — Jesus cites Isa 6:9-10 to explain his parable-methodology; the hardening effect of his teaching on the religious leaders fulfills the Isaianic commission to preach to those who will not understand"},
      {"type": "fulfillment", "target": "Acts 28:26-27", "note": "Paul's final quotation of Isa 6:9-10 to the Roman Jews who reject the gospel closes the book of Acts — the Isaianic hardening frames the entire mission narrative from Jesus's parable-ministry to Paul's Roman imprisonment"}
    ]
  },
  "7": {
    "14": [
      {"type": "fulfillment", "target": "Matt 1:23", "note": "Behold the virgin shall conceive and bear a son and shall call his name Immanuel — Matthew cites Isa 7:14 LXX (parthenos = virgin) as fulfilled in the virginal conception of Jesus; the Immanuel sign given to Ahaz in the Assyrian crisis reaches its ultimate fulfillment in the one who is literally God-with-us"}
    ]
  },
  "9": {
    "2": [
      {"type": "fulfillment", "target": "Matt 4:15-16", "note": "The people dwelling in darkness have seen a great light — Matthew applies Isa 9:1-2 to Jesus's Galilean ministry; the light in Zebulun and Naphtali is the gospel's arrival in the darkened region; Jesus is the great light"}
    ]
  },
  "11": {
    "1": [
      {"type": "fulfillment", "target": "Rom 15:12", "note": "The root of Jesse who rises to rule the Gentiles — Paul cites Isa 11:10 (the root of Jesse as a signal for the nations) as fulfilled in Christ's universal lordship over Gentiles"},
      {"type": "fulfillment", "target": "Rev 5:5", "note": "The Root of David has conquered — Revelation applies the Root of Jesse/David imagery of Isa 11:1 to the risen Christ who has conquered; the shoot from the stump of Jesse is the crucified-and-risen Messiah"}
    ],
    "2": [
      {"type": "fulfillment", "target": "John 1:32-33", "note": "The Spirit of the LORD shall rest upon him — the anointing Spirit of Isa 11:2 is visibly manifest when the Spirit descends as a dove at Jesus's baptism; the Spirit resting on Christ at baptism marks the beginning of the Isaianic messianic anointing"}
    ]
  },
  "40": {
    "3": [
      {"type": "fulfillment", "target": "Mark 1:2-4", "note": "The voice of one crying in the wilderness: Prepare the way of the LORD — all four Gospels cite Isa 40:3 as fulfilled in John the Baptist; the voice calling for the preparation of YHWH's way is the one who announces the arrival of Jesus, whose way John prepares"}
    ]
  },
  "42": {
    "1": [
      {"type": "fulfillment", "target": "Matt 12:18-21", "note": "Behold my servant whom I have chosen, my beloved in whom my soul delights — Matthew cites the first Servant Song (Isa 42:1-4) at length as fulfilled in Jesus's withdrawal from controversy and gentle healing ministry; the bruised reed he would not break is his treatment of the vulnerable"}
    ]
  },
  "49": {
    "6": [
      {"type": "fulfillment", "target": "Acts 13:47", "note": "I have made you a light for the Gentiles, that you may bring salvation to the ends of the earth — Paul and Barnabas cite Isa 49:6 as their scriptural warrant for turning to the Gentiles; the Servant's mission to be a light to the nations is the apostolic commission"},
      {"type": "fulfillment", "target": "Luke 2:32", "note": "A light for revelation to the Gentiles and for glory to your people Israel — Simeon's Nunc Dimittis applies Isa 49:6 to the infant Jesus; the Servant's mission as light-to-nations is announced over Jesus at the temple presentation"}
    ]
  },
  "52": {
    "15": [
      {"type": "fulfillment", "target": "Rom 15:21", "note": "Those who were never told about him will see, and those who have never heard will understand — Paul cites Isa 52:15 as his apostolic principle for pioneer mission: to proclaim where Christ has not been named, fulfilling the Servant's revelation to nations who never heard"}
    ]
  },
  "53": {
    "1": [
      {"type": "fulfillment", "target": "John 12:38", "note": "Who has believed what he heard from us? — John cites Isa 53:1 to explain Israel's unbelief despite Jesus's signs; the question of Isa 53 (who believed the Servant-report?) is the question that frames the rejection of Jesus"},
      {"type": "fulfillment", "target": "Rom 10:16", "note": "Lord, who has believed what he heard from us? — Paul cites Isa 53:1 to explain Israel's failure to embrace the gospel; the Servant's rejected message is the gospel that Israel stumbles over"}
    ],
    "4": [
      {"type": "fulfillment", "target": "Matt 8:17", "note": "He took our illnesses and bore our diseases — Matthew cites Isa 53:4 in connection with Jesus's healing ministry; the Servant's bearing of human disease and suffering is enacted in Jesus's healings, not only in his atoning death"}
    ],
    "7": [
      {"type": "fulfillment", "target": "Acts 8:32-33", "note": "He was led like a sheep to the slaughter and like a lamb before its shearer is silent — Philip reads Isa 53:7-8 to the Ethiopian eunuch and proclaims Jesus as the fulfillment; the silent suffering of the Servant is Jesus's silent submission to his accusers and executioners"}
    ],
    "12": [
      {"type": "fulfillment", "target": "Luke 22:37", "note": "And he was numbered with the transgressors — Jesus at the Last Supper applies Isa 53:12 to himself: this must be fulfilled in me; the Servant's identification with sinners is Jesus's crucifixion between two criminals"}
    ]
  },
  "61": {
    "1": [
      {"type": "fulfillment", "target": "Luke 4:18-19", "note": "The Spirit of the Lord is upon me, because he has anointed me to proclaim good news to the poor — Jesus reads Isa 61:1-2 in the Nazareth synagogue and says: Today this Scripture has been fulfilled in your hearing; his entire ministry is the proclamation of the Jubilee-anointing of Isa 61"}
    ]
  },
  "65": {
    "17": [
      {"type": "fulfillment", "target": "2 Cor 5:17", "note": "I create new heavens and a new earth — Paul's new creation language in 2 Cor 5:17 (if anyone is in Christ, new creation) draws from Isa 65:17's eschatological promise; the new creation is already present in Christ"},
      {"type": "fulfillment", "target": "Rev 21:1", "note": "Then I saw a new heaven and a new earth — Revelation's new creation vision fulfills Isa 65:17 and 66:22 literally; John sees the eschatological reality that Isaiah prophesied in the vision of the New Jerusalem"}
    ]
  }
}

ISA_ORIGINAL = {
  "6": {
    "3": "<p><strong>kadosh kadosh kadosh YHWH tsvaot melo kol-haaretz kevodo</strong> (<em>qādôš qādôš qādôš Yhwh ṣĕbāʾôt, mĕlōʾ kāl-hāʾāreṣ kĕbôdô</em>): 'Holy, holy, holy is the LORD of hosts; the whole earth is full of his glory.' The Trisagion is the foundational liturgical text of Jewish and Christian worship. <em>Kadosh</em> (holy) in Hebrew means primarily 'set apart, other, distinct' — YHWH is wholly other from creation. The threefold repetition (<em>shalosh</em>) conveys absolute superlative in Hebrew (cf. Gen 14:10: 'many/many/many pits' = full of pits; Jer 22:29: 'O earth, earth, earth') — not a Trinitarian formula in context, but available for Trinitarian appropriation given its threefold address. <em>Tsvaot</em> (of hosts/armies): YHWH as commander of the heavenly armies — the most frequent divine title in Isaiah (62 occurrences in the book).</p>"
  },
  "7": {
    "14": "<p><strong>hinei haalmah harah veyoledet ben veqarat shemo immanuel</strong> (<em>hinnēh hāʿalmāh hārāh wĕyōledet bēn wĕqārāt šĕmô ʿimmānûʾēl</em>): 'Behold the young woman is with child and shall bear a son and shall call his name Immanuel.' The philological crux: <em>almah</em> (young woman) vs. the LXX <em>parthenos</em> (virgin). <em>Almah</em> means 'young woman of marriageable age' — not a technical term for biological virginity (which is <em>betulah</em>). However, in context an unmarried <em>almah</em> would normally be a virgin; Matthew's use of LXX <em>parthenos</em> sees the deeper Christological fulfillment where the historical sign (birth within a year to a young woman in Ahaz's time) is transcended by the ultimate Immanuel born without a human father — the literal 'God with us.'</p>"
  },
  "40": {
    "3": "<p><strong>qol qore bamidbar panu derek YHWH yasheru baaravah mesillah lelohenu</strong> (<em>qôl qôrēʾ bammidbar pannû derek Yhwh yašĕrû bāʿărābāh mĕsillāh lēʾlōhênû</em>): 'A voice crying in the wilderness: Prepare the way of the LORD; make straight in the desert a highway for our God.' The four Gospels unanimously apply this voice to John the Baptist. Critically, the original syntax is ambiguous: is the voice 'in the wilderness' (most translations) or does the voice cry 'Prepare the way of the LORD in the wilderness' (Mark 1:3 seems to read the wilderness phrase with the road-preparation)? The Qumran community (1QS 8:14) cited this same verse for their own desert withdrawal — interpreting 'preparing the way' as Torah-study. The NT's application to John is the contested alternative: the way is prepared through proclamation, not desert community-formation.</p>"
  },
  "52": {
    "13": "<p><strong>hinneh yaskil avdi yarum venissa vegavah meod</strong> (<em>hinnēh yašĕkîl ʿabdî yārûm wĕniśśāʾ wĕgābahh mĕʾōd</em>): 'Behold, my servant shall act wisely; he shall be high and lifted up and shall be exalted.' The fourth Servant Song (52:13-53:12) opens with the Servant's triumph — <em>yarum venissa vegavah</em> (high, lifted up, exalted) — three verbs used for YHWH's own majesty in Isa 6:1 and 33:10. The Servant shares the divine exaltation-vocabulary. The shock of the Song: the path to this exaltation is through disfigurement so severe that people were appalled (52:14), and the means of exaltation is vicarious suffering (53:4-6). The Hebrew <em>nasa</em> (to bear/lift) runs through the Song: 52:13 (be lifted up), 53:4 (bore our griefs), 53:11 (bear their iniquities), 53:12 (bore the sin of many) — the lifting of the Servant and his bearing of sin are different sides of the same word.</p>",

    "7": "<p><strong>noogesh vehu naaneh velo yiptach piv kesh latabach yuval vekrachel lifnei gozezeiha nelamah velo yiftach piv</strong>: 'He was oppressed and he was afflicted, yet he opened not his mouth; like a lamb that is led to the slaughter, and like a sheep that before its shearers is silent, so he opened not his mouth.' The lamb-image combines the Passover lamb (Exod 12) and the Day of Atonement offering — an intentional fusion of Israel's two great atoning sacrifices. The silence contrasts with every protest of innocence in biblical lament-psalms: the Servant has no claim to make, no defense to offer — or rather, his silence is itself the defense, the refusal to protect himself from the death that will accomplish others' salvation. Peter applies this silence to Christ's non-retaliation (1 Pet 2:23) and Luke applies the lamb-image to the Ethiopian eunuch's question about Isa 53:7 (Acts 8:32-33).</p>"
  }
}

ISA_CONTEXT = {
  "1": {
    "1": "<p>Isaiah ben Amoz prophesied under four Judean kings: Uzziah, Jotham, Ahaz, and Hezekiah (ca. 740-686 BCE), spanning the Assyrian crisis and its aftermath. His call-vision (ch. 6) was in the year Uzziah died — a political transition when the nation faced the rising Assyrian threat under Tiglath-Pileser III. Isaiah's ministry context: the Northern Kingdom fell to Assyria in 722 BCE (referenced in Isa 7-8; 28); Jerusalem survived the siege of Sennacherib in 701 BCE (ch. 36-39). The 'Deutero-Isaiah' debate: many critical scholars argue that chs. 40-66 come from a later author writing during the Babylonian exile (ca. 550-530 BCE), given the specific naming of Cyrus (44:28; 45:1) and the Babylonian setting of chs. 40-55. Conservative scholars hold single Isaianic authorship under divine foreknowledge. The canonical unity of the book is supported by the NT's consistent attribution of both halves to 'Isaiah.'</p>"
  },
  "53": {
    "1": "<p>The fourth Servant Song (Isa 52:13-53:12) has been interpreted in Jewish tradition as: (1) collective Israel suffering in exile and ultimately vindicated; (2) the righteous remnant of Israel; (3) an individual historical figure (Jeremiah, Moses, Hezekiah, or a suffering prophet). Early Jewish sources (1QIs, Targum Jonathan, b. Sanhedrin 98b where some rabbis applied it to the Messiah) show a live debate. The NT unanimously applies the Servant to Jesus (Matt 8:17; Luke 22:37; John 12:38; Acts 8:32; Rom 10:16; 1 Pet 2:22-24; Rev 5:6). The linguistic data: the Servant suffers vicariously ('for our sins', 'for our transgressions', 'the LORD laid on him the iniquity of us all'), is innocent ('no violence or deceit'), is exalted after suffering ('he shall see his offspring, he shall prolong his days'), and his suffering is efficacious ('by his knowledge shall the righteous one, my servant, make many to be accounted righteous').</p>"
  },
  "61": {
    "1": "<p>The Spirit-anointing oracle of Isa 61:1-3 in its original context speaks of a prophetic figure commissioned to announce the Year of Jubilee (Lev 25) — the release of captives, the year of divine favor, the comfort of mourners. Whether Isa 61 belongs to 'Deutero-Isaiah' or 'Trito-Isaiah' (chs. 56-66), its Jubilee-economics for the poor were already a live text in Second Temple Judaism — Qumran's Melchizedek Scroll (11QMelch) applies Isa 61 to the eschatological release in the final Jubilee under Melchizedek. Jesus's Nazareth reading (Luke 4:18-21) claims to be this eschatological Jubilee-fulfillment: his ministry is the Year of the Lord's favor enacted in person.</p>"
  }
}

ISA_CHRIST = {
  "7": {
    "14": "<p>A fulfillment: 'Behold the virgin shall conceive and bear a son, and they shall call his name Immanuel.' The historical sign (birth to a young woman in Ahaz's time) is the type; the antitype is Jesus's virginal conception by the Holy Spirit, which makes the 'God with us' name literal for the first time in history. Every previous 'Immanuel' moment (YHWH dwelling in the tabernacle, in the temple, with Israel) was mediated through materials and institutions; in Christ, God is with us in person, in flesh, without mediation. The Immanuel bookend that Matthew establishes (1:23 = Isa 7:14; 28:20 = 'I am with you always') frames the entire Gospel as the Immanuel narrative.</p>"
  },
  "42": {
    "1": "<p>A direct revelation: 'Behold my servant whom I uphold, my chosen, in whom my soul delights; I have put my Spirit upon him; he will bring forth justice to the nations.' The first Servant Song is the OT's portrait of the Messiah as servant rather than conqueror. The divine delight in the Servant echoes at the baptism (Matt 3:17: 'my beloved Son, with whom I am well pleased') — the Father's Psalm 2 / Servant-declaration. The Spirit's endowment (v. 1) is the anointing that Luke 4:18 identifies with Jesus's public ministry. The justice-to-the-nations mission is the mandate for the Gentile mission of Acts. The first Servant Song defines Christ's method: gentle, persistent, non-violent, Spirit-empowered, globally-oriented justice.</p>"
  },
  "52": {
    "13": "<p>A direct revelation: 'Behold, my servant shall act wisely; he shall be high and lifted up, and shall be exalted.' The Servant Songs reach their climax in the fourth song: the exaltation begins the song (52:13) and ends it (53:12: 'I will divide him a portion among the many, and he shall divide the spoil with the strong'). The Christological movement: wisdom → humiliation (disfigurement, rejection, death) → exaltation (he shall see his offspring, he shall prolong his days). The resurrection is implicit in 'he shall prolong his days' after 'he was cut off out of the land of the living' (53:8-10). The fourth Servant Song is the OT's clearest pre-figuration of the entire Christological narrative: incarnation, rejection, crucifixion, resurrection, and universal reign.</p>"
  },
  "53": {
    "5": "<p>A direct revelation: 'He was pierced for our transgressions; he was crushed for our iniquities; upon him was the chastisement that brought us peace, and with his wounds we are healed.' The substitutionary suffering of the Servant expressed in four parallel lines: (1) pierced for our transgressions; (2) crushed for our iniquities; (3) chastisement for our peace; (4) wounds for our healing. The preposition <em>lemaan</em>/<em>min</em> in Hebrew (for/because of/from our transgressions) carries causal weight — the Servant suffers not for his own sins but for others'. Peter cites v. 5b-c in 1 Pet 2:24 (by his wounds you have been healed) as the foundational text for Christ's atoning death. The fourfold parallelism is the OT's most precise statement of what the cross accomplishes.</p>",

    "11": "<p>A direct revelation: 'Out of the anguish of his soul he shall see and be satisfied; by his knowledge shall the righteous one, my servant, make many to be accounted righteous, and he shall bear their iniquities.' The justification-language of Isa 53:11 — <em>yatsdiq</em> (make righteous/justify) + the many — is Paul's foundation for Pauline justification theology. The righteous Servant making many righteous by bearing their iniquities is the atonement-justification nexus that Romans 3-5 develops: Christ's obedient death (bearing iniquities) is the ground of the justified status of many. Isaiah 53:11 is the OT's closest approximation to Paul's 'he made him to be sin so that in him we might become the righteousness of God' (2 Cor 5:21).</p>"
  },
  "61": {
    "1": "<p>A direct revelation: 'The Spirit of the Lord GOD is upon me, because the LORD has anointed me to bring good news to the poor; he has sent me to bind up the brokenhearted, to proclaim liberty to the captives and the opening of the prison to those who are bound; to proclaim the year of the LORD's favor.' Jesus's Nazareth declaration — 'Today this Scripture has been fulfilled in your hearing' (Luke 4:21) — is the most explicit Christological self-application of an OT text in the Gospels. Jesus is not a prophet announcing a future event; he is himself the eschatological year of favor. The Jubilee of Isa 61 (release from debt-slavery, return of land, restoration of community) is enacted wherever Christ's reign extends — in healing, exorcism, forgiveness, community inclusion.</p>"
  }
}

def main():
    e = load_echo('isaiah')
    merge_echo(e, ISA_ECHO)
    save_echo('isaiah', e)
    print(f'Isaiah echo: {len(e)} chapters, {sum(len(v) for v in e.values())} verses')

    c = load_comm('mkt-original', 'isaiah')
    merge_comm(c, ISA_ORIGINAL)
    save_comm('mkt-original', 'isaiah', c)
    print(f'Isaiah original: {len(c)} chapters, {sum(len(v) for v in c.values())} verses')

    c = load_comm('mkt-context', 'isaiah')
    merge_comm(c, ISA_CONTEXT)
    save_comm('mkt-context', 'isaiah', c)
    print(f'Isaiah context: {len(c)} chapters, {sum(len(v) for v in c.values())} verses')

    c = load_comm('mkt-christ', 'isaiah')
    merge_comm(c, ISA_CHRIST)
    save_comm('mkt-christ', 'isaiah', c)
    print(f'Isaiah christ: {len(c)} chapters, {sum(len(v) for v in c.values())} verses')

if __name__ == '__main__':
    main()
