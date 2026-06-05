"""
MKT Context — Luke all 24 chapters
Output: data/commentary/mkt-context/luke.json
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
    "1": '<p>Luke-Acts is a two-volume work addressed to Theophilus (a Greek name meaning friend of God or beloved of God), probably a Roman Gentile patron of high standing (the title most excellent / kratiste is used for Roman officials, cf. Acts 23:26, 24:3). The prologue (1:1-4) follows the conventions of Hellenistic historical writing, establishing Luke as a careful researcher who investigated the traditions. The Gospel was written ca. 80-90 CE, after Mark (which Luke uses as a source) but before the Pastorals assume a settled Pauline legacy. Luke-Acts together constitute the longest contribution by a single author to the NT canon.</p>',
    "5": '<p>The opening chapters of Luke (1-2) are saturated with Semitic style (Hebraisms, parallelisms, Greek that translates Hebrew idioms), suggesting Luke is either using Hebrew/Aramaic sources or deliberately writing in a Septuagint style to evoke the OT narrative. Zechariah is introduced as a Levitical priest of the division of Abijah — one of the 24 priestly divisions established by David (1 Chr 24:10). Each division served two one-week periods per year; the incense offering was assigned by lot among the many priests of each division, making it a once-in-a-lifetime honor. The setting of the angel\'s appearance at the altar of incense (the holy place, just outside the holy of holies) is the spatial marker of the narrative\'s sacred beginning.</p>'
  },
  "2": {
    "1": '<p>The census of Caesar Augustus (63 BCE - 14 CE) raises the most discussed historical question in Luke\'s infancy narrative. Luke places the birth during a worldwide census while Quirinius was governing Syria (v.2). The known Quirinius census occurred in 6-7 CE, which conflicts with the Herodian birth-dating (Herod died 4 BCE). Scholars have proposed that an earlier census or registration during an earlier Quirinius governorship may explain the discrepancy; others read prote as before (before Quirinius was governor); others identify a scribal error. Whatever the resolution, Luke\'s historical-anchoring intention is clear: the birth of Jesus is embedded in universal history (Caesar Augustus, the Roman census system), not merely in Jewish sacred time.</p>',
    "41": '<p>The Passover pilgrimage to Jerusalem was required of all Jewish adult males who lived within 15 miles of Jerusalem (m. Hagigah 1:1), though by the first century many diaspora Jews and pious Galileans made the pilgrimage annually. The family caravan from Galilee to Jerusalem took approximately 4-5 days on foot. The social structure of the pilgrimage is key to understanding the story of the lost boy (v.43): extended families and neighbors traveled together in large groups; it was natural to assume a child was with relatives in the caravan before noticing his absence at nightfall. The three-day search (journey back one day, search one day, find on the third day) has been noticed as a resurrection-echo in Luke\'s typological pattern.</p>'
  },
  "3": {
    "1": '<p>Luke\'s sixfold dating of John\'s ministry (v.1-2) is the most precisely anchored historical introduction in the Gospels: the 15th year of Tiberius Caesar (28-29 CE by most reckonings, possibly 26 CE if counted from Tiberius\'s co-regency), with Pilate as Judean prefect (26-36 CE), Herod Antipas as Galilean tetrarch (4 BCE - 39 CE), Philip as Iturean tetrarch (4 BCE - 34 CE), Lysanias as Abilene tetrarch (dates uncertain), and Annas and Caiaphas as high priests (Annas served 6-15 CE; Caiaphas 18-36 CE). Luke\'s secular-historical anchoring reflects his apologetic purpose: Christianity is a public, datable, geographically specific event, not a mystery cult with hidden origins.</p>'
  },
  "4": {
    "16": '<p>The Nazareth synagogue scene is both Luke\'s inauguration narrative and his programmatic Christological-social summary. Synagogue worship in the first century included Torah readings, Prophets readings (<em>haftarah</em>), prayer, and exposition; there was no fixed lectionary for the Prophets readings, allowing Jesus to select Isa 61:1-2. The Jubilee language of Isa 61 (release to captives, year of the Lord\'s favor = the year of Jubilee from Lev 25) would have evoked economic liberation for the impoverished Galilean audience. The crowd\'s initial favorable response (v.22) followed by fury (v.28) when Jesus cites the Gentile precedents (Zarephath, Naaman) is the reception pattern that the whole Gospel will repeat: initial receptivity followed by rejection at the universal-mission implication.</p>'
  },
  "6": {
    "20": '<p>The Sermon on the Plain (6:17-49) is Luke\'s parallel to Matthew\'s Sermon on the Mount — shorter, more economically concrete, and delivered at a level place (v.17) rather than a mountain. The four beatitudes and four woes reflect the Jubilee-reversal theology of Isa 61: the poor are blessed (and the rich are denounced), the hungry are satisfied (and the full are left empty), the mourners are comforted (and those who laugh are warned). Luke\'s social emphasis (actual poverty, actual hunger) alongside Matthew\'s more spiritualized version (poor in spirit, hunger for righteousness) reflects different community contexts: Luke\'s mixed Gentile-Jewish audience includes the economically marginalized; Matthew\'s Jewish-Christian community reads poverty through the anawim tradition.</p>'
  },
  "7": {
    "1": '<p>The healing of the centurion\'s servant (7:1-10) appears in both Luke and Matthew (8:5-13), with Luke adding details that reflect a Gentile patron-client relationship: the centurion sends Jewish elders first (respected intermediaries) and then friends (personal representatives), never approaching Jesus directly. This distance-protocol reflects Mediterranean honor-shame culture: the centurion recognizes that direct approach would obligate Jesus and risk social boundary-violation. His own statement (I am not worthy for you to come under my roof) is a precise formulation of the patron-client inequality. Jesus\'s wonder at his faith (v.9) — the only time in the Synoptics Jesus marvels at faith — singles out the Gentile as the paradigm believer.</p>'
  },
  "10": {
    "25": '<p>The parable of the Good Samaritan (10:25-37) is Luke\'s unique contribution to the NT. The lawyer\'s question (who is my neighbor?) is a genuine Second Temple debate: some interpretations limited neighbor to fellow Jews or even only to Pharisees; others extended it to proselytes. The Samaritan as hero is the most provocative element: Samaritans and Jews had long-standing mutual hostility (John 4:9, Josephus Ant. 18.30 describes violent incidents). The parable does not define who counts as a neighbor (the expected answer) but asks which of the three acted as a neighbor — shifting the question from classification (who is in my neighbor-category?) to disposition (how do I neighbor?). The priest and Levite\'s failure is probably a purity concern: contact with a potentially dead body would render them unclean for temple service.</p>'
  },
  "15": {
    "1": '<p>The three parables of Luke 15 (lost sheep, lost coin, lost son) are unique to Luke and form a unified trilogy on the divine initiative in seeking and finding the lost. The social context of v.1-2 is critical: the Pharisees and scribes murmur because Jesus receives (accepts, welcomes, eats with) sinners. Table fellowship was a community boundary marker in first-century Judaism: with whom you ate defined who you included. The parable trilogy is Jesus\'s theological defense of his boundary-transgressing practice: God himself seeks the lost (lost sheep, lost coin) and runs to embrace the returning prodigal — therefore the community formed around this God should reflect the same excess of seeking, welcoming love.</p>'
  },
  "16": {
    "19": '<p>The parable of the Rich Man and Lazarus (16:19-31) is Luke\'s unique social-reversal parable with an afterlife scene. The rich man\'s clothing (purple and fine linen) are the markers of extreme wealth in antiquity (purple dye was extraordinarily expensive; fine linen was the priestly and royal cloth). Lazarus (the only named character in a Jesus parable) is a name meaning God has helped — the divine help he received was absent in life but present in death. The parable concludes with the theological point that Abraham\'s bosom (the Jewish term for the blessed state of the righteous after death) is not available to those who ignore the Law and the Prophets (v.29,31) — reinforcing Luke\'s consistent theme of wealth as a spiritual danger.</p>'
  },
  "19": {
    "1": '<p>Jericho (19:1-10, Zacchaeus) is the last stop before Jerusalem on the road up from the Jordan Valley. Zacchaeus as chief tax collector (architelones) — a title not found elsewhere in the NT — suggests he was the head contractor for the Jericho district, which would have been profitable: Jericho was a wealthy oasis city with balsam groves, a major product of the region. His height problem and the sycamore tree (ficus sycomorus, a low-branching tree common in the Jordan Valley) are vivid geographic details. Zacchaeus\'s offer of fourfold restitution and 50% distribution to the poor exceeds what repentance required: the Mosaic law required 20% addition (Lev 6:5, Num 5:7) and fourfold only for stolen animals (Exod 22:1).</p>'
  },
  "22": {
    "3": '<p>The Last Supper\'s Passover context (22:7-13) is thoroughly Lukan: Luke adds the preparatory detail (Peter and John sent to find the room), the eschatological-earnest longing (I have earnestly desired to eat this Passover with you, v.15), and the unique covenant-cup sequence (some manuscripts give two cups in Luke — a feature that may reflect the four Passover cups). The argument about greatness at the table (vv.24-27, unique to Luke) is placed immediately after the institution, as if the disciples misunderstand the service-Christology just enacted. Luke\'s passion narrative contains significant unique material: the Agony (v.43-44, in some manuscripts), the arrest crowd with clubs and swords, and the healing of the high priest\'s servant\'s ear (v.51).</p>'
  },
  "23": {
    "1": '<p>Luke\'s passion narrative adds several unique elements that serve his apologetic purpose: Pilate\'s triple declaration of Jesus\'s innocence (23:4, 14, 22 — I find no guilt in this man), the Herod Antipas episode (23:7-12, unique to Luke), the mourning daughters of Jerusalem (23:27-31), the repentant criminal (23:39-43), and the Lukan last word (23:46, quoting Ps 31:5). The triple Pilate-innocence formula is Luke\'s most explicit apologetic point: the Roman governor found Jesus not guilty, therefore Roman law and Roman Christians need not regard Jesus as a criminal. The political authorities\' guilt lies in capitulation to Jewish pressure, not in their own judgment.</p>'
  },
  "24": {
    "13": '<p>The Emmaus road appearance (24:13-35) is Luke\'s unique and most extended resurrection narrative. Emmaus has been tentatively identified with modern Motza or Abu Ghosh, approximately 11 km from Jerusalem. The disciples\' unrecognized conversation with the risen Jesus (the recognition-delayed pattern echoes Gen 42:7-8, Joseph unrecognized by his brothers) culminates in the breaking of bread — the Eucharistic gesture that opens their eyes. Luke\'s narrative implies that the Lord\'s Supper is one of the primary contexts for recognition of the risen Christ; the post-Easter community encounters the risen one in the sharing of bread, as in the Upper Room. The Emmaus account grounds the Eucharistic practice of the early church in a resurrection-recognition event.</p>'
  }
}

def main():
    existing = load_comm('mkt-context', 'luke')
    merge_comm(existing, DATA)
    save_comm('mkt-context', 'luke', existing)
    total = sum(len(v) for v in existing.values())
    print(f'Luke mkt-context: {len(existing)} chapters, {total} verses written.')

if __name__ == '__main__':
    main()
