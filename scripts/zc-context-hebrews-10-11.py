"""
MKT Context Commentary — Hebrews chapters 10–11
Run: python3 scripts/zc-context-hebrews-10-11.py

Key decisions:
- 10:1 Platonic shadow/image: Hebrews' use of Platonic phenomenology without Platonic metaphysics
- 10:5 Ps 40 LXX variant: the textual critical situation and its significance
- 10:25 not neglecting assembly: the historical situation of Christians withdrawing from community
- 10:26-31 willful sin warning: comparison with Jewish apostasy and covenant violation
- 11: faith heroes list: Jewish martyrology tradition (2 Macc, 4 Macc, Wisdom of Solomon)
- 11:37 sawn asunder: rabbinic tradition of Isaiah's martyrdom
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

HEBREWS = {
  "10": {
    "1": '<p>Hebrews\' description of the law as having "a shadow of the good things to come" and "not the image (<em>eikōn</em>) itself" uses conceptual categories found in Platonic philosophy. Plato\'s theory of forms described the visible world as a shadow of the intelligible world of Forms — what we see are shadows on the cave wall, not the realities themselves (Republic 514a-520e). Philo of Alexandria extensively applied this framework to interpret the Jewish Torah and temple: the earthly sanctuary is the image of the heavenly archetype (On the Life of Moses 2.71-76). However, Hebrews does not adopt the Platonic framework wholesale — it does not make the Jewish institutions merely imperfect shadows of eternal realities, but rather provisional historical realities that pointed forward to a historical fulfillment. The "shadow/image" language is Platonic vocabulary deployed for a historical-eschatological argument.</p>',
    "5": '<p>The textual variant between Psalm 40:6\'s Hebrew ("ears you have dug/opened for me") and the LXX ("a body you have prepared for me") reflects an important text-critical situation. The Masoretic Text reads <em>ōzen karitha li</em> (ears you have bored/dug for me) — the idiom "opening the ears" for giving the capacity to hear and obey (used in Isa 50:5 of the Servant). The LXX Greek reads <em>sōma de katērtisō moi</em> (a body you have prepared for me) — either a different Hebrew text (reading <em>guf</em> [body] rather than <em>ōzen</em> [ear]) or an interpretive translation understanding the opened ear as a synecdoche for the receptive body. The LXX reading enables Hebrews\' Christological application: the incarnate body prepared for the Son is the instrument of the will-doing that replaces sacrifice. The textual difference is thus theologically productive in Hebrews.</p>',
    "19": '<p>The description of the community\'s access to the holy places "by the blood of Jesus, by the new and living way that he opened for us through the curtain, that is, through his flesh" (10:19-20) reflects the theological significance of the temple curtain\'s tearing at the crucifixion (Matt 27:51; Mark 15:38; Luke 23:45). In the Second Temple period, the <em>paroket</em> (the great veil) that separated the Holy Place from the Most Holy Place was an elaborate woven tapestry described in Josephus (Jewish War 5.212-214) as depicting the heavens — a cosmic hanging that represented the boundary between the divine and human spheres. Its destruction at the crucifixion was understood by the evangelists as a sign; Hebrews\' "through the curtain, that is, through his flesh" identifies the curtain typologically with Christ\'s flesh, making his death the literal tearing that opens the way to God.</p>',
    "25": '<p>"Not neglecting to meet together, as is the habit of some" refers to an actual pattern of withdrawal from the community assembly that was occurring in the Hebrews\' community. The reasons for withdrawal could include: (a) fear of public identification as a Christian community in a context of persecution; (b) gradual drift back toward Jewish synagogue worship, which offered legal protection; (c) the spiritual fatigue and disillusionment that persecution produces; (d) the loss of eschatological urgency as the parousia was delayed. The instruction to assemble more rather than less as the Day approaches places community assembly in an explicitly eschatological frame — the assembly is both the present foretaste of the heavenly assembly (12:22-24) and the mutual support structure for surviving until the Day.</p>',
    "26": '<p>The category of "willful sin" (<em>hekousiōs hamartanein</em>) after receiving the knowledge of the truth echoes the OT distinction between inadvertent sins (for which the Levitical system provided atonement, Lev 4-5; Num 15:22-29) and "high-handed" or presumptuous sins (Num 15:30-31) for which no Levitical atonement was provided — the person who acted presumptuously was "cut off from among his people." The Qumran Rule of the Community (1QS 8:20-9:2) distinguishes between inadvertent transgressions and deliberate sins, providing different community responses to each. Hebrews\' "no longer any sacrifice for sins" applies the OT no-atonement principle for high-handed sins to the specific case of post-conversion deliberate apostasy from Christ.</p>'
  },
  "11": {
    "1": '<p>The placement of Hebrews 11\'s "faith definition" (hypostasis... elenchos) in the context of the Habakkuk citation (10:37-38) situates it within the prophetic tradition of the righteous remnant who trusts in God against visible evidence. The Second Temple Jewish wisdom tradition had developed the concept of faith-despite-circumstances: 4 Maccabees (1st century CE) celebrates the Maccabean martyrs as examples of reason and piety overcoming bodily suffering — a form of faith-endurance. Wisdom of Solomon 3:1-9 describes the righteous whose apparent suffering is actually their testing and glorification. The Habakkuk pesher from Qumran (1QpHab 8:1-3) interprets "the righteous shall live by his faith" as referring to the community that trusts in the Teacher of Righteousness\'s interpretation — a different application of the same text that Paul and Hebrews use.</p>',
    "4": '<p>Abel\'s story (Gen 4:1-10) had been developed in Second Temple Jewish tradition as the paradigmatic martyrdom. The Testament of Abel (embedded in the Testaments of the Twelve Patriarchs) and the Martyrdom of Isaiah develop the martyr-tradition. Philo (Questions on Genesis 1.59-68) allegorizes Abel and Cain as representing piety vs. self-love. In the Targum Neofiti (early tradition preserved in later texts), Abel\'s blood cries out and his spirit testifies before God. Hebrews\' comment that "through his faith, though he died, he still speaks" (11:4) draws on this tradition of the martyr\'s continuing testimony. The rabbinic tradition (later crystallized in the b. Sanhedrin 37b) on the blood of Abel crying from the ground reinforces the ongoing-testimony motif.</p>',
    "13": '<p>The patriarchs\' self-description as "strangers and exiles on the earth" (11:13) participates in the Hellenistic-Jewish philosophical tradition of the soul\'s alienation from its true heavenly home. Philo developed the idea of the soul as a pilgrim (<em>parepidēmos</em>) separated from its divine origin and journeying toward return (On the Cherubim 120-121; On the Confusion of Tongues 77-78). The terminology of <em>xenoi kai parepidēmoi</em> (strangers and sojourners) was also used legally in the Hellenistic world for resident aliens who lacked full citizen rights. 1 Peter 2:11 uses identical language for the Christian community. In Hebrews, the patriarchal pilgrim-identity is the model for the community: they are citizens of the heavenly city who live as aliens in the present order.</p>',
    "37": '<p>"Sawn in two" (<em>epristhēsan</em>) is a reference that early Christian tradition universally applied to Isaiah\'s martyrdom under King Manasseh. The Martyrdom of Isaiah (a Jewish text from the 2nd century BCE or earlier, surviving in the pseudepigraphical Ascension of Isaiah) describes Isaiah as being sawn in two with a wood saw while being held in a hollow tree — a tradition already established in Jewish circles before Hebrews was written. Justin Martyr (Dialogue with Trypho 120) confirms the tradition\'s early currency. This tradition explains the otherwise puzzling reference: the prophet Isaiah, whose book is extensively quoted throughout Hebrews, was understood to have been martyred in the very manner that his faith led to. The "sawn in two" martyr is thus the tradition\'s own most authoritative witness to the faith-under-persecution theme.</p>',
    "38": '<p>"Of whom the world was not worthy" reflects the apocalyptic inversion of worldly judgment: the wandering, cave-dwelling martyrs who appear rejected by the world are actually those by whose presence the world is honored — or rather, whose presence reveals the world\'s unworthiness of them. This inversion language appears in Jewish apocalyptic: 4 Ezra 7:86-87 describes how the righteous who suffered in the present age will be vindicated; 2 Baruch 52:6-7 describes how the righteous who were unknown in this age will be revealed in the next. The Wisdom of Solomon 3:1-9 makes the same inversion explicit: the righteous whose suffering appeared to be destruction was actually their honor. Hebrews situates the faith-heroes in this tradition of the world\'s failure to recognize its greatest treasures.</p>'
  }
}

def main():
    existing = load_comm('mkt-context', 'hebrews')
    merge_comm(existing, HEBREWS)
    save_comm('mkt-context', 'hebrews', existing)
    total = sum(len(v) for v in existing.values())
    print(f'Hebrews mkt-context: {len(existing)} chapters, {total} verses written.')

if __name__ == '__main__':
    main()
