"""
MKT Christ — Luke all 24 chapters
Output: data/commentary/mkt-christ/luke.json
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
    "46": '<p>A type: the Magnificat. Mary\'s song is shaped by Hannah\'s prayer (1 Sam 2:1-10) — Hannah as the type of the Spirit-filled woman through whom the Lord\'s anointed enters the world. But the Magnificat exceeds Hannah\'s song: where Hannah praised for her personal vindication, Mary praises for the eschatological reversal that the incarnation initiates for all the humble and hungry of Israel and the world. The type (Hannah/Samuel) points to the antitype (Mary/Jesus) not as mere parallel but as fulfillment: what Hannah\'s prayer anticipated (the exaltation of the humble, the strength of the LORD\'s anointed) is now the content of the incarnation itself.</p>',
    "68": '<p>A fulfillment: blessed be the Lord God of Israel, for he has visited and redeemed his people. Zechariah\'s Benedictus identifies the births of John and Jesus as the visitation (episkope) of YHWH that all the prophets promised. The OT motif of divine visitation (YHWH visiting his people in mercy or judgment) reaches its fulfillment in the incarnation: God personally visits his people not through a prophet or angel but in the person of his Son. The redemption (lytrosis, v.68; lytrosan, v.74) is the Exodus-liberation pattern now applied to redemption from enemies (political) and from sin (spiritual), with both dimensions present.</p>'
  },
  "2": {
    "11": '<p>A direct revelation: a Savior, who is Christ the Lord, has been born for you in the city of David. The angelic announcement at the shepherds concentrates Luke\'s Christology in a single sentence. The Savior born in David\'s city is the fulfillment of the Davidic covenant, the messianic hope, and the divine rescue promised throughout the OT. Luke\'s characteristic soter (Savior) title connects Jesus to the salvation history of Israel (YHWH as Israel\'s only savior, Isa 43:11) while the details of the manger, the shepherds, and the town of Bethlehem anchor the salvation in the most ordinary and humble circumstances — the divine Savior in a feeding trough.</p>',
    "32": '<p>A fulfillment: a light for revelation to the Gentiles and for glory to your people Israel. Simeon\'s Nunc Dimittis applies the Isaianic Servant vocation (Isa 49:6) to the infant Jesus: he is the Servant who is a light to the nations. Luke\'s Gospel will be the narrative of this dual fulfillment — the glory of Israel (through the Jewish mission) and the light to the Gentiles (through the Gentile mission that Acts continues). The infant who cannot yet speak is already identified as the one in whom the universal Servant mission will be embodied and accomplished.</p>'
  },
  "4": {
    "18": '<p>A direct revelation: the Spirit of the Lord is upon me, because he has anointed me to proclaim good news to the poor. The Nazareth synagogue scene is Luke\'s programmatic statement of the Christological mission. Jesus reads Isa 61:1-2 and declares today this scripture has been fulfilled in your hearing (v.21) — the most explicit self-identification with the Isaianic Servant in the Synoptic Gospels. Luke presents the Christ\'s mission as the Jubilee: release to captives (from sin and from evil powers), sight to the blind, freedom for the oppressed, the year of the Lord\'s favor. The entire Gospel is the unfolding of this Jubilee-mission.</p>',
    "43": '<p>A direct revelation: I must preach the good news of the kingdom of God to the other towns as well; for I was sent for this purpose. The dei (it is necessary) of v.43 is one of Luke\'s most important theological terms — divine necessity shapes the mission at every point. Jesus was sent (apestalen) — the mission is not self-chosen but given by the Father. The kingdom of God that Jesus preaches is the reign of God becoming present in his own person; to hear Jesus is to encounter the kingdom\'s arrival.</p>'
  },
  "7": {
    "22": '<p>A fulfillment: go and tell John what you have seen and heard — the blind receive their sight, the lame walk, lepers are cleansed, the deaf hear, the dead are raised, the poor have good news proclaimed. Jesus\'s answer to the imprisoned John is the definitive self-identification from Isaiah: the signs that he lists are precisely the signs that Isaiah promised when YHWH comes to save (Isa 35:5-6, 61:1). Christ\'s identity is proven not by Messianic title-claim but by Isaianic sign-fulfillment; the question is not what do you claim to be? but what do you see happening? The works are the revelation.</p>'
  },
  "9": {
    "51": '<p>A direct revelation: when the days drew near for him to be taken up, he set his face to go to Jerusalem. Luke\'s travel-narrative framing (9:51-19:44) presents the entire journey to Jerusalem as a deliberate movement toward the passion, resurrection, and ascension. Jesus does not drift toward Jerusalem; he sets his face (Isa 50:7, the Servant who sets his face like flint to face opposition). Every parable and teaching in the travel narrative is colored by this deliberate journey toward the cross. The Christological claim is implicit: the one who moves with this resolve toward his own death is the one who has freely accepted the Father\'s mission from eternity.</p>'
  },
  "15": {
    "20": '<p>A revelation of God: the father of the prodigal son runs, embraces, and restores without condition. The father in the parable is transparently the image of God — no other first-century Jewish father would run (an undignified act) to embrace a disgraced son before any apology had been given. The parable is Jesus\'s defense of his own practice (receiving sinners) by revealing the Father\'s character: God himself is the running father who hosts the party for the found son and pleads with the older brother. Every feature of the father\'s excess (running, robe, ring, sandals, feast, self-humiliation at the party\'s edge) is a portrait of divine grace preceding, enabling, and exceeding human repentance.</p>'
  },
  "19": {
    "10": '<p>A direct revelation: the Son of Man came to seek and to save the lost. Luke\'s mission-statement frames the Zacchaeus encounter as the paradigmatic instance of the Son of Man\'s seeking-saving mission. The three parables of Luke 15 and the Zacchaeus narrative are the lived theology of Luke 19:10: the lost sheep sought by the shepherd, the lost coin sought by the woman, the lost son welcomed by the father, and now the lost Zacchaeus sought-and-found by the Son of Man himself. The mission of Luke\'s Gospel is the living-out of this one sentence, fulfilled supremely in the cross (where the Son of Man gives himself to save the utterly lost).</p>'
  },
  "22": {
    "20": '<p>A fulfillment: this cup that is poured out for you is the new covenant in my blood. Luke\'s cup-word (with the new covenant language from Jer 31:31-34) is the most explicit Jeremianic citation in the passion narratives. The new covenant — written on the heart, bringing forgiveness of sins, creating universal knowledge of YHWH — is inaugurated in the cup of Jesus\'s blood. The Passover context connects the new covenant blood to the Exodus blood (the lamb\'s blood that protected from the destroying angel): Christ\'s blood is simultaneously the final Passover (ending the old covenant\'s provisional atonement) and the new covenant\'s ratifying sacrifice.</p>',
    "37": '<p>A fulfillment: this scripture must be fulfilled in me: And he was numbered with the transgressors. Jesus\'s citation of Isa 53:12 before his arrest is the clearest evidence in the Synoptics that Jesus explicitly understood his death as the fulfillment of the Servant\'s vicarious suffering. The verb dei (must be fulfilled) indicates divine necessity: the Servant\'s path of bearing sin for the many was not merely predictive of his death but constitutive of the divine plan from which the cross received its saving power. The numbered-with-transgressors (arrested as a criminal) is the humiliation that precedes the Servant\'s exaltation.</p>'
  },
  "23": {
    "43": '<p>A direct revelation: today you will be with me in paradise. The word to the penitent criminal is the most compressed eschatological promise in the Gospels: today (the dying day, no purgatorial delay), with me (personal presence with Christ, not merely a blessed state), in paradise (the garden-restored, the original Eden-with-God now restored). The dying Christ who is in the process of bearing sin for the many simultaneously promises the thief immediate eschatological fellowship. The promise grounds the community\'s confidence: if even the dying criminal is welcomed today, the resurrection-hope of all who trust Christ is secured.</p>',
    "46": '<p>A direct revelation: Father, into your hands I commit my spirit. Luke\'s Christ dies with Ps 31:5 as his final prayer — the trust-language of the righteous sufferer who commits himself to the faithful Father at death. The Father-address maintains the intimate relationship that defined the whole of Luke\'s Christological portrayal (Abba in Gethsemane, 22:42; this prayer at death). The Spirit commended to the Father\'s hands is the Spirit that will be poured out at Pentecost (Acts 2) — even in death the Son\'s Spirit remains in the Father\'s keeping, to be given back in the resurrection and then poured out on the community.</p>'
  },
  "24": {
    "27": '<p>A direct revelation: beginning with Moses and all the Prophets he interpreted to them in all the Scriptures the things concerning himself. The risen Christ\'s Emmaus hermeneutic is the epistemological key to Luke\'s entire Gospel: the OT is about Christ, and only the risen Christ can unlock its true meaning. The burning hearts (v.32) indicate that proper reading of Scripture is simultaneously encounter with the risen Christ — not merely information about him but the experience of his presence through the word. Luke\'s Gospel has been narrating what the risen Christ explained: the whole story of Israel (from Genesis through the Prophets) was the long preparation for and anticipation of what Jesus accomplished in Jerusalem.</p>',
    "46": '<p>A direct revelation: it is necessary that the Christ should suffer and on the third day rise from the dead, and that repentance for the forgiveness of sins should be proclaimed in his name to all nations. The risen Christ\'s final hermeneutical statement to the disciples declares the canonical shape of the Christological narrative: suffering → resurrection is the divinely necessary arc (dei), and the worldwide mission to proclaim forgiveness in his name is its equally necessary consequence. Luke 24:46-47 is the theological thesis of Acts, which will narrate exactly this proclamation going from Jerusalem to the ends of the earth. The Christ\'s mission is complete; the community\'s mission is just beginning.'
  }
}

def main():
    existing = load_comm('mkt-christ', 'luke')
    merge_comm(existing, DATA)
    save_comm('mkt-christ', 'luke', existing)
    total = sum(len(v) for v in existing.values())
    print(f'Luke mkt-christ: {len(existing)} chapters, {total} verses written.')

if __name__ == '__main__':
    main()
