import json, pathlib

ROOT = pathlib.Path(__file__).parent.parent

def load_echo(book):
    p = ROOT / 'data' / 'echoes' / f'{book}.json'
    if p.exists():
        return json.loads(p.read_text())
    return {}

def save_echo(book, data):
    p = ROOT / 'data' / 'echoes' / f'{book}.json'
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

JUDGES_ECHOES = {
    "18": {
        "1": [
            {
                "type": "allusion",
                "target": "Heb 11:8",
                "note": "In those days the tribe of Dan was seeking an inheritance to settle in — 'for until then no inheritance had fallen to them among the tribes of Israel.' The tribe without an inheritance types the person without a heavenly country. Hebrews 11:8-10 contrasts Abraham's model: he 'went out, not knowing where he was going,' seeking 'the city that has foundations, whose designer and builder is God.' The Danites sought their own solution to the inheritance problem; Abraham trusted YHWH. The tribe's self-directed search for territory contrasts with the faith-directed seeking of those who 'desire a better country, that is, a heavenly one' (Heb 11:16)."
            }
        ],
        "2": [
            {
                "type": "allusion",
                "target": "Num 13:17",
                "note": "Dan sent five men to spy out the land — an echo of Moses's twelve spies (Num 13:17). But where Moses's spies were sent by divine command to the land YHWH had promised, Dan's spies are sent by tribal initiative to find land YHWH had not designated for them. The unauthorized spy mission produces unauthorized settlement. The NT pattern is similar: 'the one who enters by the door is the shepherd of the sheep' (John 10:2) — those who climb in another way are not legitimate. Dan's self-directed search produces a stolen inheritance; Christ's disciples receive an inheritance through the door."
            }
        ],
        "5": [
            {
                "type": "allusion",
                "target": "Jer 6:14",
                "note": "The Danite spies ask Micah's Levite priest whether their journey will succeed, and he answers 'Go in peace. The journey on which you go is under the eye of the LORD' (v.6). This is a false oracle of peace — the Levite speaks peace without knowing YHWH's will. Jeremiah's indictment of false prophets captures the pattern: 'They have healed the wound of my people lightly, saying \"Peace, peace,\" when there is no peace' (Jer 6:14; 8:11). The hireling-priest who pronounces peace over a mission YHWH never authorized is the prototypical false prophet — a pattern Jesus warns against: 'Beware of false prophets' (Matt 7:15)."
            }
        ],
        "6": [
            {
                "type": "allusion",
                "target": "Matt 7:15",
                "note": "The Levite's oracle — 'The journey on which you go is under the eye of the LORD' — is unverified and self-interested, given to travelers who have simply asked his favor. This types the false prophet who tells people what they want to hear without genuine divine commission. Jesus warns: 'Beware of false prophets, who come to you in sheep's clothing but inwardly are ravenous wolves' (Matt 7:15). The Levite is not malicious but opportunistic — and opportunistic religious authority is exactly the 'sheep's clothing' under which false teaching operates. The oracle that pleased the Danites led them to steal and conquer, confirming the oracle's falseness by its fruits (Matt 7:16-20)."
            }
        ],
        "14": [
            {
                "type": "allusion",
                "target": "John 10:12",
                "note": "The six hundred armed Danites stop at Micah's house and take the ephod, household gods, and carved image — then invite the Levite-priest to come with them: 'Is it better for you to be priest to the house of one man, or to be priest to a tribe and clan in Israel?' (v.19). The priest whose heart was glad and who went willingly (v.20) is the hireling shepherd: 'He who is a hired hand and not a shepherd, who does not own the sheep, sees the wolf coming and leaves the sheep and flees' (John 10:12). The Levite follows the larger salary, abandoning his original employer. The Good Shepherd, by contrast, lays down his life for the sheep rather than abandoning them for a better offer."
            }
        ],
        "20": [
            {
                "type": "allusion",
                "target": "John 10:12",
                "note": "'The priest's heart was glad. He took the ephod and household gods and the carved image and went along with the people.' The eager compliance of the hireling-priest types the ease with which religious authority becomes institutionally compliant rather than prophetically faithful. The Levite's gladness at the promotion types the temptation Jesus warns against: those who serve for professional advantage rather than divine calling will abandon their post when tested. The NT's 'false teachers' (2 Pet 2:1-3) are characterized by the same motif: 'In their greed they will exploit you with false words.'"
            }
        ],
        "24": [
            {
                "type": "allusion",
                "target": "Matt 16:26",
                "note": "Micah's lament — 'You have taken away my gods that I made and the priest, and gone away, and what have I left?' — is the cry of a man whose entire spiritual identity consisted of self-constructed religion. His 'gods that I made' are his whole inheritance; when they are taken, he has nothing. Jesus's question cuts to the same point: 'For what will it profit a man if he gains the whole world and forfeits his soul?' (Matt 16:26). Micah's carved gods were his soul's false foundation; their theft revealed the emptiness that had always been there. The gods we make cannot save us when the Danites (or death) come."
            }
        ],
        "27": [
            {
                "type": "allusion",
                "target": "Luke 21:20",
                "note": "The tribe of Dan took Micah's gods and his priest, came to Laish, and struck the city with the sword and burned it. Laish was 'quiet and unsuspecting' — a city dwelling in security that had no warning of coming destruction (v.7,27). Jesus warns of exactly this complacency before judgment: 'When you see Jerusalem surrounded by armies, then know that its desolation has come near' (Luke 21:20). The peaceful, unsuspecting Laish burning without warning types the judgment that comes on those who dwell in false security. 'People were eating, drinking, marrying and being given in marriage... and the flood came' (Matt 24:38-39)."
            }
        ],
        "28": [
            {
                "type": "allusion",
                "target": "1 Cor 10:7",
                "note": "Dan set up the carved image and the stolen priesthood in their conquered city, 'and Dan was the name of the city to the day of the captivity of the land' (v.29). The entire tribal settlement was built on stolen idols and an unqualified priest — a foundation that lasted until the exile. Paul uses the wilderness generation's idolatry as a warning: 'Do not be idolaters as some of them were; as it is written, \"The people sat down to eat and drink and rose up to play\"' (1 Cor 10:7). Dan's founding of a city on idolatry is the same pattern: a people settling into comfortable worship of what they have constructed rather than YHWH."
            }
        ],
        "30": [
            {
                "type": "allusion",
                "target": "Acts 7:43",
                "note": "Jonathan the son of Gershom, son of Moses, served as priest to Dan until the day of the captivity — Moses's own grandson operating an idolatrous shrine. Stephen's speech in Acts 7 quotes Amos 5:26 regarding Israel's wilderness idolatry: 'You took up the tent of Moloch and the star of your god Rephan.' The corruption of Israel's worship from within, through people with impeccable pedigrees (Moses's grandson!), illustrates the NT warning that false teaching comes from within the community (Acts 20:30: 'from among your own selves will arise men speaking twisted things'). Lineage does not protect against apostasy."
            }
        ],
    },
    "19": {
        "1": [
            {
                "type": "type",
                "target": "John 19:15",
                "note": "'In those days, when there was no king in Israel' — the refrain of Judges 17-21 frames the entire final section as a diagnosis of kinglessness. The darkest chapters of Judges (idol-theft, Gibeah's outrage, civil war) occur in the absence of YHWH's king. The NT counter-refrain is Israel's cry at the trial of Jesus: 'We have no king but Caesar' (John 19:15). Both statements are acts of royal rejection: the Judges narrative describes the chaos of no king; the Passion narrative describes the explicit rejection of the true King. In both cases, the absence/rejection of the true king produces catastrophe."
            }
        ],
        "3": [
            {
                "type": "allusion",
                "target": "Luke 15:20",
                "note": "The Levite went to Bethlehem of Judah 'to speak tenderly to her and bring her back' — the phrase <em>ledaber al-libah</em> (to speak to her heart) is the language of covenant restoration (Hos 2:14: 'I will... speak tenderly to her'). The husband seeking the estranged wife types the Father running to receive the prodigal: 'But while he was still a long way off, his father saw him and felt compassion, and ran and embraced him' (Luke 15:20). YHWH's covenant love in the OT prophets is precisely this pattern of going to recover the estranged — what the husband in Judges 19 intends to do. The narrative then darkens, showing what humans do with covenant recovery attempts."
            }
        ],
        "10": [
            {
                "type": "allusion",
                "target": "Luke 10:31",
                "note": "The Levite refuses to lodge in Jebus (pre-Israelite Jerusalem) because it is 'a city of foreigners, who do not belong to the people of Israel' (v.12) — and insists on stopping among 'the people of Israel' at Gibeah of Benjamin. The irony is the Samaritan-parable inversion: those expected to be dangerous (foreigners) would have been safer; those expected to be hospitable (Israelites, Benjaminites) prove more violent than Sodom. The priest and Levite who passed by the man beaten on the Jericho road (Luke 10:31-32) parallel the Gibeahites who passed by on the other side of hospitality. The expected insiders fail; the unexpected outsiders (like the Samaritan) act with true covenant love."
            }
        ],
        "15": [
            {
                "type": "type",
                "target": "Gen 19:2",
                "note": "No one in Gibeah took the Levite and his party in — they sat in the open square. This near-exact parallel to Lot's situation in Sodom (Gen 19:1-2) announces what is coming. The men of Gibeah who surround the house (v.22) replicate the men of Sodom (Gen 19:4-5) in type and language. Jesus invokes both Sodom and the 'cities of Israel' as parallel judgments: 'I tell you, it will be more tolerable on that day for Sodom than for that town' (Luke 10:12). Gibeah-of-Benjamin was worse than Sodom: the covenant people had become what their supposed enemies were. The elect's failure of hospitality is more culpable than the outsiders'."
            }
        ],
        "16": [
            {
                "type": "allusion",
                "target": "Gen 18:2",
                "note": "The old man from the hill country of Ephraim — not a Benjaminite — sees the travelers in the square and runs to meet them and bring them in (vv.16-21). He is the Gibeah-narrative's equivalent of Abraham at Mamre: the one who breaks ranks with the surrounding community's inhospitality to welcome strangers. 'Do not neglect to show hospitality to strangers, for thereby some have entertained angels unawares' (Heb 13:2, citing Abraham and Lot). In a city of Israelites who failed the hospitality test, one man acted with covenant faithfulness — the remnant pattern that runs through Scripture alongside the apostasy narrative."
            }
        ],
        "22": [
            {
                "type": "type",
                "target": "Gen 19:4",
                "note": "The men of Gibeah surround the house and demand the Levite for sexual violence — an exact structural echo of Sodom (Gen 19:4-5). The NT returns to Sodom as a type of end-time judgment: 'Likewise, just as it was in the days of Lot... fire and sulfur rained from heaven and destroyed them all — so will it be on the day when the Son of Man is revealed' (Luke 17:28-30). Gibeah's repetition of Sodom's crime within the covenant people intensifies the warning: judgment falls not only on Sodom's open wickedness but on Gibeah's internal corruption of covenant identity. The church is warned: 'You also must be ready' (Luke 12:40)."
            }
        ],
        "25": [
            {
                "type": "allusion",
                "target": "Isa 53:7",
                "note": "The concubine thrust out and 'abused all night until the morning' (v.25) is among the OT's most harrowing images of innocent suffering. The suffering servant of Isaiah 53 is 'oppressed and afflicted, yet he opened not his mouth' (Isa 53:7) — crushed under the full weight of human violence without protest. The concubine's passive suffering at the hands of those who should have protected her types the silent endurance of the one who 'when he was reviled, did not revile in return; when he suffered, he did not threaten, but continued entrusting himself to him who judges justly' (1 Pet 2:23). The darkness of Judges 19 is the darkness that the cross entered."
            }
        ],
        "26": [
            {
                "type": "type",
                "target": "Luke 13:34",
                "note": "The concubine fell at the door of the house 'with her hands on the threshold' — the image of collapse at the very door of the shelter she could not enter. Jesus's lament over Jerusalem captures the same image: 'O Jerusalem, Jerusalem, the city that kills the prophets and stones those who are sent to it! How often would I have gathered your children together as a hen gathers her brood under her wings, and you were not willing!' (Luke 13:34). Those who fall at the threshold of the house types those who sought refuge in Jerusalem but found only death — and the concubine's stretched-out hands on the threshold type the hands stretched out on the cross."
            }
        ],
        "28": [
            {
                "type": "allusion",
                "target": "Matt 27:46",
                "note": "'Get up, let us be going.' But there was no answer — she was dead. The Levite's words to the silent concubine echo the silence of death itself. The silence of the dead who cannot respond types the silence of the entombed Christ — the 'no answer' of the hours between crucifixion and resurrection. The Father's apparent silence in those hours ('My God, my God, why have you forsaken me?' Matt 27:46) is the divine entry into the 'no answer' that the concubine suffered. Christ descended into the full reality of Judges 19's darkness — the silence of death — and broke it from within by resurrection."
            }
        ],
        "29": [
            {
                "type": "allusion",
                "target": "1 Cor 1:18",
                "note": "The Levite cuts the concubine's body into twelve pieces and sends them throughout Israel. This extreme, shocking act was designed to force Israel to reckon with what Gibeah had done — to make the invisible violence visible and inescapable. Paul's proclamation of the cross operates similarly: 'The word of the cross is folly to those who are perishing, but to us who are being saved it is the power of God' (1 Cor 1:18). The cross is YHWH's twelve-piece message to the world: this is what your sin has done; this is what human violence looks like when it meets the innocent. The body broken and distributed as testimony is a type of the broken body of Christ proclaimed in the gospel."
            }
        ],
        "30": [
            {
                "type": "allusion",
                "target": "Mark 13:19",
                "note": "'Has such a thing ever happened since the day that the people of Israel came up out of Egypt until this day? Consider it, take counsel, and speak.' The assembled response recognizes Gibeah as uniquely unprecedented — a benchmark of depravity that Israel had never reached before. Jesus's discourse on the end times uses the same framing: 'For in those days there will be such tribulation as has not been from the beginning of the creation that God created until now, and never will be' (Mark 13:19). Both statements mark a moment of judgment so severe that nothing comparable has preceded it. The unprecedented is coming; the question is not whether to reckon with it but how."
            }
        ],
    },
}

def main():
    existing = load_echo('judges')
    merge_echo(existing, JUDGES_ECHOES)
    save_echo('judges', existing)
    count_18 = len(existing.get('18', {}))
    count_19 = len(existing.get('19', {}))
    print(f'ch18: {count_18} verses with echoes; ch19: {count_19} verses with echoes')
    print('Judges 18-19 echo written.')

if __name__ == '__main__':
    main()
