"""
MKT Revelation chapter 13 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-revelation-13-13.py

Translation decisions (carrying forward from mkt-revelation-3-6.py and mkt-revelation-7-12.py):

- G2342 (θηρίον): "beast" (L/M); "the Beast" as a proper antagonist title in T when used of
    the first beast (sea-beast) as a political-eschatological power. The second beast (earth-
    beast) is "the second beast" or "false prophet" in T (Revelation names it false prophet at
    16:13, 19:20). Consistent with mkt-revelation-7-12.py convention.
- G1404 (δράκων): "dragon" (L/M/T) — always. The Dragon's identity is declared at 12:9.
- G721 (ἀρνίον): "Lamb" (capitalized) when referring to Christ; lowercase "lamb" in 13:11
    where the second beast wears the appearance of a lamb — that is the false prophet
    counterfeiting the Lamb. The lowercase makes the distinction audible.
- G1504 (εἰκών): "image" (L/M/T) — a sculpted likeness/statue, as in imperial cult.
- G5480 (χάραγμα): "mark" (L/M/T) — the branded or stamped mark; used for ownership marks
    on slaves and animals in antiquity. T surfaces the ownership/allegiance dimension.
- G4151 (πνεῦμα) in 13:15: lowercase "spirit/breath" — this is the animating force granted
    to the image, not the Holy Spirit. L: "spirit"; M: "breath"; T: "breath and voice."
- G5281 (ὑπομονή): "endurance" (L/M); "patient endurance" (T) in 13:10. Consistent with
    chs. 2–3 (ὑπομονή as active perseverance, not passive waiting).
- G4102 (πίστις): "faith" in 13:10 — the active trust/allegiance the saints maintain
    through suffering.
- G1849 (ἐξουσία): "authority" (L/M/T) — consistently. The repeated use of ἐδόθη (it was
    given) in ch.13 (vv.5, 7, 14, 15) signals that the beast's power is derivative and
    divinely permitted, not autonomous. This theological point is surfaced in T.
- G2602 (καταβολή) + G2889 (κόσμος) in 13:8: "from the foundation of the world" modifies
    "slain" (ἐσφαγμένου) in Greek word order, not "written." L preserves the source word
    order. This is the Greek reading supported by KJV; modern versions split; the Greek
    syntax favors this reading. T surfaces the implication: the Lamb's sacrifice was planned
    before creation.
- G706 (ἀριθμός): "number" (L/M/T) — the number of the beast. In 13:18 this is six hundred
    and sixty-six (χξϛ in some MSS, the full spelling ἑξακόσιοι ἑξήκοντα ἕξ in others).
    Rendered as "six hundred and sixty-six" in L/M; T notes it is a gematria cipher pointing
    to a historical figure (most likely Nero Caesar in Hebrew gematria).
- G4678 (σοφία): "wisdom" (L/M/T) in 13:18 — the same word used for the wisdom needed to
    interpret the divine mysteries (compare 17:9). Not casual cleverness but theological
    discernment.
- Textual note v1: The Greek has a disputed variant — ἐστάθη ("he stood," 3rd person,
    subject = dragon from 12:17-18) in NA28/critical text vs. ἐστάθην ("I stood," 1st
    person = John). Most English translations read "I stood" following TR. Rendered "I stood"
    to maintain narrative consistency with the rest of Revelation's first-person vision style.
- OT intertextuality:
    vv.1-2: The beast from the sea combines features of Daniel's four beasts (Dan 7:3-7):
        leopard (Dan 7:6), bear (Dan 7:5), lion (Dan 7:4), and the ten-horned beast (Dan 7:7).
        T surfaces this explicitly — the sea-beast is a composite of all earthly empires.
    v4: "Who is like the beast?" — a dark parody of "Who is like you, O LORD?" (Exod 15:11;
        Mic 7:18; Ps 35:10). T surfaces the blasphemous inversion.
    v8: "Lamb slain from the foundation of the world" — echoes 1 Pet 1:19-20; Eph 1:4.
    v10: "He who leads into captivity goes into captivity" echoes Jer 15:2 and 43:11. T
        frames this as a call to faithful acceptance of the appointed path, not fatalism.
    v13: Fire from heaven — deliberate parallel to Elijah's fire at Carmel (1 Kgs 18:38).
        The false prophet counterfeits the prophet's power in service of idolatry. T notes this.
- Aspect notes:
    v8 ἐσφαγμένου (perfect passive participle): the Lamb bears the lasting marks of slaughter
        — "having been slain." Perfect aspect: past act with permanent present effect.
    v5 ἐδόθη (aorist passive): "was given" — a divine passive; God grants the beast's platform.
    v3 ἐθαύμασεν (aorist): the world's wonder was a single past event, not ongoing.
    v15 δοθῆναι (aorist infinitive): the giving of spirit/breath to the image is a single act.
"""
import json, pathlib

ROOT  = pathlib.Path(__file__).parent.parent
DRAFT = ROOT / 'data' / 'translation' / 'draft'

def load(tier, book):
    p = DRAFT / tier / f'{book}.json'
    if p.exists():
        return json.loads(p.read_text())
    return {}

def save(tier, book, data):
    p = DRAFT / tier / f'{book}.json'
    p.write_text(json.dumps(data, ensure_ascii=False, indent=None))
    print(f'  wrote {p.relative_to(ROOT)}')

def merge_tier(existing, new_data, tier_key):
    for ch, verses in new_data.items():
        if ch not in existing:
            existing[ch] = {}
        for v, tiers in verses.items():
            existing[ch][v] = tiers[tier_key]

REVELATION = {
  "13": {
    "1": {
      "L": "And I stood on the sand of the sea. And I saw a beast rising up out of the sea, having ten horns and seven heads, and on his horns ten crowns, and on his heads a name of blasphemy.",
      "M": "And I stood on the sand of the sea. And I saw a beast rising out of the sea, with ten horns and seven heads, with ten crowns on its horns and a blasphemous name on its heads.",
      "T": "I took my stand on the shore. A beast came surging up out of the sea — ten horns and seven heads, a royal crown on every horn, and inscribed across each head a name that was an act of defiance against God."
    },
    "2": {
      "L": "And the beast which I saw was like a leopard, and his feet like the feet of a bear, and his mouth like the mouth of a lion; and the dragon gave him his power and his throne and great authority.",
      "M": "The beast I saw was like a leopard; its feet were like a bear's, and its mouth was like a lion's mouth. And the dragon gave it his power and his throne and great authority.",
      "T": "The beast before me combined every predatory feature of Daniel's vision: the spotted body of a leopard, the crushing feet of a bear, the devouring mouth of a lion — all four terrible empires merged into one. And the dragon transferred to it his own power, his own throne, and his sweeping authority."
    },
    "3": {
      "L": "And one of his heads was as if slain to death, and his deadly wound was healed. And all the earth wondered after the beast.",
      "M": "One of its heads seemed to have a mortal wound, but the mortal wound was healed. The whole earth marveled and followed the beast.",
      "T": "One of the seven heads bore what looked like a fatal wound — and yet it had healed. The whole world stared in astonishment and fell in behind the beast. It was a dark imitation of resurrection, and the world was taken in."
    },
    "4": {
      "L": "And they worshipped the dragon because he gave authority to the beast, and they worshipped the beast, saying, 'Who is like the beast? Who is able to make war with him?'",
      "M": "And they worshipped the dragon, because he had given authority to the beast, and they worshipped the beast, saying, 'Who is like the beast, and who can make war against it?'",
      "T": "They bowed before the dragon for empowering the beast, and they bowed before the beast itself, chanting: 'Who could ever match it? Who would dare fight it?' The ancient hymn of Israel — 'Who is like you, LORD?' — was turned inside out, offered to the Beast as a substitute god."
    },
    "5": {
      "L": "And there was given to him a mouth speaking great things and blasphemies, and authority was given to him to act for forty-two months.",
      "M": "And the beast was given a mouth uttering haughty words and blasphemies, and it was given authority to exercise power for forty-two months.",
      "T": "The beast was given a mouth — a platform for boasting and for blasphemy against God. And it was given authority to operate for forty-two months. Both the mouth and the time were granted, not seized. Everything the beast has, it holds on borrowed terms."
    },
    "6": {
      "L": "And he opened his mouth in blasphemies against God, to blaspheme his name and his tabernacle, those dwelling in heaven.",
      "M": "It opened its mouth to utter blasphemies against God, blaspheming his name and his dwelling — those who dwell in heaven.",
      "T": "With the voice it had been given, the beast launched its assault — against God himself, against his name, against his sanctuary, against every heavenly being who belongs to him. Every word was an attack on the holy."
    },
    "7": {
      "L": "And it was given to him to make war with the saints and to overcome them; and authority was given to him over every tribe and people and tongue and nation.",
      "M": "Also it was given authority to make war on the saints and to conquer them. And authority was given it over every tribe and people and language and nation.",
      "T": "It was granted power to wage war against God's people and to prevail — for a season. The reach was global: every tribe, every people, every language, every nation. And yet: the verb 'given' keeps appearing. The beast does not act on its own authority; it acts within limits set by one greater than itself."
    },
    "8": {
      "L": "And all who dwell on the earth will worship him — everyone whose name has not been written in the book of life of the Lamb slain from the foundation of the world.",
      "M": "And all who dwell on earth will worship it — everyone whose name has not been written in the book of life of the Lamb who was slain from the foundation of the world.",
      "T": "Everyone whose home is in this present age will worship it — all whose names were never inscribed in the book of life belonging to the Lamb who was slaughtered from before the foundation of the world. The Lamb's sacrifice was no late correction. It was part of the plan before creation began."
    },
    "9": {
      "L": "If anyone has an ear, let him hear.",
      "M": "If anyone has an ear, let him hear.",
      "T": "If you have ears, use them now. This vision is speaking directly to you."
    },
    "10": {
      "L": "If anyone is for captivity, into captivity he goes; if anyone kills with the sword, with the sword he must be killed. Here is the endurance and the faith of the saints.",
      "M": "If anyone is to go into captivity, into captivity he will go; if anyone is to be killed with the sword, with the sword he must be killed. Here is a call for the endurance and faith of the saints.",
      "T": "Some of God's people will be taken captive — that is the path appointed for them. Some will fall to the sword — that too is the appointed path. This is not defeat; this is the moment when the saints demonstrate who they are: a people who endure without collapsing and keep faith without flinching. The call echoes Jeremiah: accept the appointed way, for the LORD governs even this."
    },
    "11": {
      "L": "And I saw another beast rising up out of the earth. And it had two horns like a lamb and spoke like a dragon.",
      "M": "Then I saw another beast rising out of the earth. It had two horns like a lamb, but it spoke like a dragon.",
      "T": "Then a second beast appeared — rising not from the sea but from the earth itself. It wore the appearance of gentleness: two horns like a young lamb. But when it opened its mouth, what came out was the dragon's voice. The face deceives; the speech reveals."
    },
    "12": {
      "L": "And it exercises all the authority of the first beast in its presence, and it causes the earth and those who dwell in it to worship the first beast, whose deadly wound was healed.",
      "M": "It exercises all the authority of the first beast in its presence, and makes the earth and those who dwell in it worship the first beast, whose mortal wound was healed.",
      "T": "This second beast wields the full authority of the first beast, always operating in its presence and acting as its agent. Its single driving purpose: to direct every person on earth to bow before the first beast — the one who appeared to die and lived again."
    },
    "13": {
      "L": "And it performs great signs, so that it even makes fire come down from heaven to earth in the sight of people.",
      "M": "It performs great signs, even making fire come down from heaven to earth in front of everyone.",
      "T": "To enforce this worship, the second beast performs spectacular signs — fire drawn down from the sky before the watching crowds. This is a deliberate echo of the prophet Elijah at Mount Carmel. But Elijah called fire to prove the LORD was God; the false prophet calls fire to prove the Beast deserves worship."
    },
    "14": {
      "L": "And it deceives those who dwell on the earth by the signs which were given to it to do before the beast, telling those who dwell on the earth to make an image to the beast who has the wound of the sword and yet lived.",
      "M": "And by the signs it was allowed to perform in the presence of the beast, it deceives those who dwell on earth, telling them to make an image for the beast that was wounded by the sword and yet lived.",
      "T": "Using those performed signs as its leverage, the second beast deceives the inhabitants of the earth — signs that were granted to it, not generated from its own power. Its command to the nations: construct an image honoring the beast that survived the sword, the one who appeared dead and returned."
    },
    "15": {
      "L": "And it was given to it to give spirit to the image of the beast, so that the image of the beast might speak, and cause as many as would not worship the image of the beast to be killed.",
      "M": "And it was allowed to give breath to the image of the beast, so that the image of the beast could speak and could cause those who would not worship the image to be killed.",
      "T": "The false prophet was granted the power to animate the image — to breathe voice into it, so that it could speak and issue decrees. The decree it issued was this: anyone who refused to bow before the image would be put to death. Worship the image, or die."
    },
    "16": {
      "L": "And it causes all, both small and great, both rich and poor, both free and slave, to be given a mark on their right hand or on their forehead,",
      "M": "It also caused all, both small and great, both rich and poor, both free and slave, to be marked on the right hand or the forehead,",
      "T": "The second beast imposed a mark on the entire population — no exemptions across any social rank: small or great, wealthy or destitute, free person or slave. The mark was placed on the right hand or the forehead: the places of action and identity."
    },
    "17": {
      "L": "and that no one might buy or sell except the one who has the mark, the name of the beast, or the number of its name.",
      "M": "so that no one could buy or sell unless he had the mark, that is, the name of the beast or the number of its name.",
      "T": "Without the mark — which meant accepting the beast's name or the numerical cipher of its name — no one could trade. No buying, no selling, no economic participation. Survival itself required allegiance. This is the system at full extension: total economic dependence on the Beast's approval to eat, to work, to live."
    },
    "18": {
      "L": "Here is wisdom: let the one who has understanding calculate the number of the beast, for it is the number of a man, and his number is six hundred and sixty-six.",
      "M": "This calls for wisdom: let the one who has understanding calculate the number of the beast, for it is the number of a man, and his number is six hundred and sixty-six.",
      "T": "This requires the kind of wisdom that can read the signs of the age — not casual cleverness but discernment. The number of the beast is a human number, the gematria cipher of a specific person. That number is six hundred and sixty-six. Those with ears attuned to the first century would have decoded the name this cipher concealed."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'revelation')
        merge_tier(existing, REVELATION, tier_key)
        save(tier_dir, 'revelation', existing)
    print('Revelation 13 written.')

if __name__ == '__main__':
    main()
