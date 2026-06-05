"""
MKT Context Commentary — Hebrews chapters 6–9
Run: python3 scripts/zc-context-hebrews-6-9.py

Key decisions:
- 6:13-18 oath-taking: Jewish legal and covenantal background of oath formulas
- 7:1-10 Melchizedek: Gen 14 in Second Temple Jewish interpretation (11QMelchizedek, Philo)
- 7:11 Levitical priesthood imperfection: historical corruption context
- 8:1-5 heavenly sanctuary: apocalyptic heavenly temple traditions
- 8:8-13 new covenant Jeremiah: Jeremiah's historical context, Qumran new covenant self-understanding
- 9:1-10 tabernacle furnishings: Exodus/Leviticus cultic descriptions
- 9:11-14 Day of Atonement: Leviticus 16 as the central ritual background
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
  "6": {
    "4": '<p>The warning of 6:4-6 has been debated across church history because of its severity. In its historical context, it addressed a specific situation: those who had converted from Judaism (or Gentile God-fearers with deep synagogue formation) to the Christian community, who were now considering returning to the synagogue and the Jewish community to avoid persecution. The Domitian persecution (81-96 CE) and earlier Neronian persecution (64 CE) created enormous social pressure on Jewish Christians: the Jewish community had certain legal protections (<em>religio licita</em>) under Roman law that Christians who separated from the synagogue lost. The warning against apostasy addresses this specific crisis of faith under social-political pressure rather than the general question of whether any sin is beyond forgiveness.</p>',
    "13": '<p>The oath formula "by myself I have sworn" (Gen 22:16) reflects the ancient Near Eastern and Jewish legal practice of oath-taking by invoking a greater authority. In Israelite practice, oaths were sworn by the LORD (Deut 6:13; 10:20); in Hellenistic culture, by the gods or by the emperor. The Mishnah (tractate Shevu\'ot) devotes significant attention to the legal obligations created by oaths and the consequences of false oaths. The Essenes at Qumran reportedly refused to take oaths (Josephus, Jewish War 2.135), understanding the community covenant as sufficiently binding without additional oath-swearing. In this context of oath-law, God\'s self-swearing is the maximum possible legal guarantee — the divine oath creates an obligation that God\'s own character upholds.</p>',
    "19": '<p>The anchor metaphor for hope was common in Hellenistic culture. The anchor (<em>ankura</em>) was the sailor\'s most essential equipment for security; it appears frequently in inscriptions, papyri, and early Christian art as a symbol of hope and security. The catacombs use the anchor as a Christian symbol. In Jewish apocalyptic, the heavenly sanctuary was understood as the source of stability for the earthly order; the Hebrews metaphor of hope as an anchor entering the heavenly sanctuary behind the curtain is a specifically Jewish-Christian synthesis: the Hellenistic anchor image combined with the priestly sanctuary theology.</p>'
  },
  "7": {
    "1": '<p>Genesis 14:18-20\'s Melchizedek passage generated extensive Jewish interpretation. The Qumran text 11QMelchizedek (11Q13) portrays Melchizedek as a heavenly figure of divine judgment who will declare atonement for the Sons of Light at the end of the tenth Jubilee period. In this text, Melchizedek appears as a semi-divine being executing eschatological judgment — far beyond the Genesis narrative\'s brief mention. Philo of Alexandria allegorizes Melchizedek as the Logos (Word/Reason) — the divine rational principle that is "king of peace" and "priest of God Most High" by nature rather than appointment (On Allegory 3.79-82). The Genesis Apocryphon from Qumran (1QapGen) simply retells the Genesis narrative without allegorization. Hebrews differs from all these: Melchizedek is a type (shadow), not a divine figure in himself, and the correspondence is to the Son as the antitype.</p>',
    "11": '<p>The historical corruption of the Levitical high priesthood created real anxiety about whether the temple cult could accomplish its atoning purpose. The Qumran community withdrew from Jerusalem temple worship entirely, establishing its own community worship as the true priestly service until the eschatological restoration of the legitimate Zadokite priesthood. The Psalms of Solomon (1st century BCE) reflect intense concern about the defilement of the Jerusalem priesthood. Philo discusses the high priest\'s qualifications extensively in On Special Laws 1.113-131, emphasizing the moral and physical perfection required — and implying awareness that current high priests did not always meet these requirements. Hebrews\' claim that the Levitical system could not achieve "perfection" addresses a community that had genuine reasons to doubt its effectiveness.</p>',
    "22": '<p>The legal concept of the surety or guarantor (<em>engyos</em>) was a standard institution in Hellenistic commercial law. A guarantor made themselves legally liable for another\'s obligations — if the principal defaulted, the guarantor paid. Papyri from Egypt and the Greco-Roman world contain numerous examples of surety agreements. Philo uses the concept in discussing Abraham\'s covenantal relationship with God (On Abraham 273). The identification of Jesus as the covenant\'s guarantor in legal terms grounds the theological claim in a familiar legal institution: the community\'s covenant standing is secured by Jesus\'s personal assumption of liability.</p>'
  },
  "8": {
    "5": '<p>The concept of the earthly tabernacle as a copy of the heavenly original appears explicitly in Exodus 25:40 (the pattern shown to Moses on the mountain) and is developed in multiple Second Temple Jewish texts. Philo of Alexandria interprets the tabernacle allegorically as representing the entire cosmos, with the Most Holy Place representing the divine world and the Holy Place representing the visible creation (Questions on Exodus 2.85-86; On the Life of Moses 2.71-108). In the Dead Sea Scrolls, the Songs of the Sabbath Sacrifice describe the heavenly sanctuary and its angelic liturgy as the model for the Qumran community\'s own worship — earthly worship as participation in the heavenly original. The Targums identify the heavenly sanctuary as the archetype (e.g., Targum Pseudo-Jonathan on Exod 25:9). Hebrews draws on this widely shared tradition of heavenly-earthly correspondence.</p>',
    "8": '<p>Jeremiah\'s new covenant oracle (Jer 31:31-34) was written in the context of the Babylonian exile — the first covenant had failed (Israel had broken it through persistent idolatry and injustice) and Jeremiah promises a future covenant in which God will write his law on hearts rather than stone tablets. By the first century, multiple Jewish communities understood themselves as the inheritors of this new covenant promise. The Qumran Damascus Document explicitly identifies the community as those who "entered the new covenant in the land of Damascus" — the Qumranites understood their community covenant as the Jeremianic new covenant. Early Christianity (cf. Luke 22:20; 1 Cor 11:25; 2 Cor 3:6) made the same claim in relation to Jesus\'s death. Hebrews\' use of Jer 31 in ch8 is the most extensive NT exposition of the new covenant oracle.</p>',
    "13": '<p>The language of covenant obsolescence and imminence of passing away ("ready to vanish away") may reflect the actual historical situation of the Jerusalem temple still standing at the time of Hebrews\' writing. If Hebrews was written before 70 CE (when the Romans destroyed the temple and ended the Levitical sacrificial system), the author could see the temple system as theologically obsolete (because of the new covenant) while still physically present. The community may have included former priests (Acts 6:7 mentions "a great company of priests" who joined the Jerusalem community); Josephus records the continuing temple worship up to 70 CE. The "growing old and aging" language anticipates the temple\'s physical end as the visible completion of what the new covenant has already accomplished theologically.</p>'
  },
  "9": {
    "1": '<p>The tabernacle furnishings that Hebrews 9:1-5 inventories correspond to the Exodus descriptions: the lampstand (Exod 25:31-40; Num 8:1-4), the table of showbread (Exod 25:23-30; Lev 24:5-9), the golden altar of incense (Exod 30:1-10; placed either in front of the curtain [Exod 30:6] or associated with the inner sanctuary in Hebrews\' account), the Ark of the Covenant with its gold jar of manna (Exod 16:33-34), Aaron\'s budded staff (Num 17:10), the stone tablets (Exod 25:21; Deut 10:1-5), and the cherubim of glory overshadowing the mercy seat (Exod 25:17-22). The Mishnah tractate Middot and Yoma describe the Second Temple\'s actual arrangement, which differed somewhat from the desert tabernacle. Hebrews appears to describe the Mosaic tabernacle rather than the Herodian temple.</p>',
    "7": '<p>The Day of Atonement (Yom Kippur) ritual is described in detail in Leviticus 16 and elaborated extensively in the Mishnah tractate Yoma. The elaborate preparations: the high priest separated from his family and household seven days before; he immersed in the mikveh (ritual bath) five times on the day itself; he offered the bull for himself, then selected one of two goats for the LORD (the other becoming the scapegoat for Azazel); he entered the Most Holy Place three times — with the incense pan, then with the bull\'s blood, then with the goat\'s blood — sprinkling seven times on the mercy seat and seven times in front of it. The elaborate preparation for a single annual entry underscored the difficulty of access to the divine presence that Hebrews argues Christ\'s death permanently resolves.</p>',
    "11": '<p>The Hebrews statement that Christ is "a high priest of the good things that have come" (or "that are coming," depending on the manuscript) places him in the context of the eschatological good that Jewish apocalyptic anticipated. 4 Ezra 7:26-44 describes the revelation of the age to come with its messianic kingdom and final judgment. 2 Baruch 29:3-8 describes the eschatological abundance (manna from heaven again, wine from vines) that will accompany the Messiah\'s arrival. The "greater and more perfect tent not made with hands" uses <em>cheiropoiētos</em> (made by human hands) — a term the Hebrew prophets used to describe idols (Isa 2:18; 10:11) and that Acts 7:48 uses to argue that God does not dwell in a human-made temple. The heavenly sanctuary transcends the category of human religious construction.</p>',
    "13": '<p>The red heifer ritual (Num 19) was among the most puzzling of the Torah\'s purity laws — even King Solomon, tradition said, could not explain it (Numbers Rabbah 19:3; Pesikta de-Rav Kahana 4.2). The ashes of the red heifer, mixed with water, purified those who had become unclean through contact with a corpse. The ritual required that the officiating priest himself became unclean in the process of purifying others — a paradox that the Mishnah (Parah) acknowledges without resolving. The rabbis treated it as a <em>chok</em> (divine decree beyond human understanding). Hebrews reads the ritual\'s very paradoxicality as part of its typological function: the shadow of purification through the death of the unblemished animal, which itself defiled the purifier, points forward to the blood of Christ that purifies without defiling its source.</p>'
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
