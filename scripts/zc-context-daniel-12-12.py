"""
MKT Context Commentary — Daniel chapter 12
Run: python3 scripts/zc-context-daniel-12-12.py

Ch 12: The book's eschatological climax — Michael's arising, the general resurrection
       (the OT's clearest statement), the sealing of the book, 1,290/1,335-day
       chronologies, and Daniel's personal resurrection promise.

Key context decisions:
- v2 is treated as a genuine general resurrection text (not merely metaphorical),
  in contrast to Ezek 37 (national restoration as resurrection metaphor).
- "Time, times and half a time" (v7) = 3.5 years = the recurring prophetic period
  of tribulation shared across Daniel 7:25, 9:27, Rev 12:14, Rev 13:5.
- The 1,290 and 1,335 days (vv. 11-12) are acknowledged as the most debated
  numbers in Scripture; their interpretation is held open.
- The "abomination of desolation" (v11) is treated as having a near-historical
  referent (Antiochus IV Epiphanes, 167 BCE) and an eschatological referent
  (Jesus applies the term in Matt 24:15).
- Daniel's personal resurrection promise (v13) closes the book with individual
  eschatological hope, not only cosmic resolution.
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

DANIEL = {
  "12": {
    "1": "<p>'At that time Michael, the great prince who watches over your people, will arise' — Michael (Hebrew: <em>mîkāʾēl</em>, 'who is like God?') is the angelic guardian of Israel, named here and in Dan 10:13, 21 as the celestial counterpart to the human conflict being described. The concept of guardian angels for nations appears in Deut 32:8 (LXX/DSS reading: 'according to the number of the sons of God') and is developed in Second Temple literature (1 Enoch 20; Jubilees 15:31-32). 'A time of distress unlike any since nations first existed' (<em>et tzarah asher lo nihetah mihiyot goy</em>) echoes the phrase of Joel 2:2 and is applied by Jesus to the eschatological tribulation in Matt 24:21, connecting Daniel's language directly to the discourse on the last things. 'Every one who is found written in the book' (<em>kol-asher yimmatze katuv basefer</em>) — the heavenly register of the righteous is attested in Ex 32:32-33, Ps 69:28, and developed in Second Temple and NT apocalyptic as the 'book of life' (Rev 20:12).</p>",
    "2": "<p>'Multitudes who sleep in the dust of the earth will awake: some to everlasting life, others to shame and everlasting contempt' — this is the OT's clearest statement of a general resurrection with two outcomes, and the only OT text that explicitly names 'everlasting life' (<em>lehayye olam</em>). Earlier resurrection language in the OT is either corporate/metaphorical (Ezek 37:1-14: the dry bones as a symbol of national restoration) or ambiguous (Job 19:25-27; Ps 16:10; Hos 6:2; Isa 26:19). Daniel 12:2 states individual bodily resurrection unambiguously. The two-outcome structure ('everlasting life' vs. 'shame and everlasting contempt,' <em>lederaon olam</em>) is cited by Jesus in John 5:28-29 ('all who are in the tombs will hear his voice and come out — those who have done good to the resurrection of life, those who have done evil to the resurrection of judgment'). Josephus reports that the Pharisees believed in the resurrection of the righteous based on passages like this (Ant. 18.14; War 2.163).</p>",
    "3": "<p>'Those who are wise will shine like the brightness of the heavens, and those who lead many to righteousness, like the stars forever and ever' — the <em>maskilim</em> (wise ones, from <em>hizkil</em>, to be wise, to have insight) appear throughout Daniel 11-12 as the group who endure the Antiochene persecution, 'fall by sword and flame, by captivity and plunder, for some days' (11:33) but are refined by it (11:35; 12:10). Their stellar glory (<em>kezohar haraqia</em>, 'like the brightness of the firmament') echoes the language of Gen 1:14-17 (the lights in the firmament) and is developed in 1 Enoch 104:2-6 (the righteous will shine like the stars). Paul applies the language of Dan 12:3 to the final resurrection body in 1 Cor 15:40-43 ('star differs from star in glory') and to the Philippian community in Phil 2:15 ('shine like stars in the universe'). 'Those who lead many to righteousness' (<em>umatzdikim harabbim</em>) is a phrase shared with Isa 53:11 ('my servant will justify many, and he will bear their iniquities').</p>",
    "4": "<p>'Roll up and seal the words of this scroll until the time of the end' (<em>sethom hadevarim veḥatom hasefer ʿad-et qetz</em>) — Daniel is instructed to seal his revelations, contrasting sharply with Revelation 22:10 ('Do not seal up the words of the prophecy of this scroll, because the time is near'). The sealing is not suppression but preservation for a future generation: the book is sealed <em>until</em> the time of the end. 'Many will go here and there to increase knowledge' (<em>yeshotu rabbim vetirbe hadaat</em>) — the phrase is debated: some read 'go here and there' (<em>shotet</em>, to roam) as intellectual searching through the text (cf. Amos 8:12, 'stagger from sea to sea seeking YHWH's word'), others read it as physical travel. The LXX tradition reads it as 'many will be taught and knowledge will abound,' pointing to eschatological increase of understanding rather than physical movement.</p>",
    "5": "<p>'Then I, Daniel, looked and saw two others standing there, one on this side of the river and one on the opposite bank' — the two angelic figures flanking the river provide witnesses to the oath of vv. 6-7, following the principle of two-witness validation (Deut 19:15). The Ulai/Tigris river as the setting of the vision (cf. 10:4) locates the vision in Babylonian geography. The dual-witness structure reappears in Revelation 11:3-12 (the two witnesses) and John 20:12 (the two angels at the tomb), though each context serves different purposes. The heavenly court structure — celestial beings flanking a central figure above the waters — echoes the divine council imagery of 1 Kings 22:19 and Isa 6:1-3.</p>",
    "6": "<p>'How long will it be before these astonishing things are fulfilled?' (<em>matay ketz haniflaot</em>) — the question from one of the riverside figures voices the reader's own question, which has accumulated through the visions of chapters 7-12. 'The astonishing things' (<em>haniflaot</em>, wonders) refers to the distress and redemption of 12:1 and the entire sequence of visions. The question-answer structure (celestial messenger asks, the figure above the waters answers) is a standard apocalyptic convention establishing the authoritative source of the following disclosure (cf. Zech 1:12-13; Rev 7:13-14). The urgency of the question reflects the pastoral concern underlying the whole book: for the community enduring persecution, the timing of divine intervention is the most pressing question.</p>",
    "7": "<p>'A time, times and half a time' (<em>lemoed moedim vahetzt</em>) — the mysterious time-period, first stated in Dan 7:25 for the Little Horn's dominion over the saints, here receives its climactic restatement. The formula 1 + 2 + ½ = 3½ is widely interpreted as a half-week of years (3½ years = 42 months = 1,260 days), a period that recurs in Revelation (Rev 11:2, 3; 12:6, 14; 13:5) as the duration of eschatological tribulation. Historical near-fulfillment: Antiochus IV's desecration of the temple lasted roughly 3 years (168-165 BCE). The oath 'by him who lives forever' (<em>beḥei haolam</em>) is the strongest possible form of affirmation — swearing by the eternal God rather than by any creature (cf. Heb 6:13 on God swearing by himself). 'When the power of the holy people has been finally broken' (<em>kekhallot nappetz yad am-qodesh</em>) — complete vulnerability precedes deliverance, the pattern of the Exodus.</p>",
    "8": "<p>'I heard, but I did not understand' — Daniel's incomprehension is programmatic: the visions are not fully intelligible to their recipient, which is part of what 'sealing' means. The prophet does not require full comprehension to be faithful — his task is to record and preserve the revelation, not to master it. This honest admission distinguishes authentic prophecy from pseudo-prophetic claims of complete understanding. Cf. 1 Pet 1:10-12: the prophets 'searched intently and with the greatest care, trying to find out the time and circumstances to which the Spirit of Christ in them was pointing when he predicted the sufferings of the Messiah and the glories that would follow.' Not even the prophets fully understood their own prophecies.</p>",
    "9": "<p>'The words are rolled up and sealed until the time of the end' — the repetition of the sealing command (cf. v. 4) emphasizes that Daniel's non-understanding is not a failure of intelligence but the appropriate condition of a sealed revelation. The 'time of the end' (<em>et qetz</em>) is the repeated technical term of Daniel's eschatology (Dan 8:17; 11:35, 40; 12:4, 9), consistently pointing to a future moment when YHWH's intervention will resolve the crisis. The book of Daniel closes in a posture of patient, non-understanding trust — which is precisely the disposition commended to the saints who will endure the tribulation.</p>",
    "10": "<p>'Many will be purified, made spotless and refined, but the wicked will continue to be wicked' (<em>yitbarreru veyitlabenu veyitzarafu rabbim vehirshiu resha'im</em>) — the refining language (purified, spotless, refined) uses the vocabulary of metallurgical testing applied to covenant faithfulness (cf. Ps 12:6; Jer 9:7; Zech 13:9; Mal 3:3). The eschatological period is one of moral bifurcation: those who are refined become more pure; those who are wicked become more deeply wicked — the hardening effect that appears in Ex 7-11 (Pharaoh's hardening) and Rom 1:28 (God giving people over to further sin). 'None of the wicked will understand, but those who are wise will understand' — wisdom (<em>maskil</em>) is both the prerequisite for and the consequence of covenant faithfulness; the wicked are cognitively disabled from understanding the revelation their rebellion has rejected.</p>",
    "11": "<p>'From the time that the daily sacrifice is abolished and the abomination that causes desolation is set up, there will be 1,290 days' — the 'abomination of desolation' (<em>shiqqutz meshomem</em>) first appeared in Dan 9:27 and 11:31. Near-historical fulfillment: Antiochus IV Epiphanes abolished the tamid (daily sacrifice) and set up a Zeus altar on the Jerusalem altar (1 Macc 1:54; 2 Macc 6:2) ca. December 167 BCE, desecrating the temple until its rededication by Judas Maccabaeus on 25 Kislev 164 BCE — approximately three years (1,095 days), not 1,290 days. The gap between 1,260 (3.5 years), 1,290, and 1,335 days has generated extensive debate. Jesus applies 'abomination of desolation' to a future event in Matt 24:15 ('when you see the abomination of desolation spoken of by Daniel, standing in the holy place'), treating the Antiochene fulfillment as a type rather than the final referent. The 1,290 days may represent 30 additional days of continued crisis before final resolution.</p>",
    "12": "<p>'Blessed is the one who waits for and reaches the end of the 1,335 days' — one of two beatitudes in Daniel (cf. 12:1's implicit blessing on those written in the book). The 1,335 days exceeds the 1,290 by 45 more days — a further extension beyond the 1,260 days of the tribulation period. The exact significance of the 45-day interval (1,335 − 1,290) and the 75-day interval (1,335 − 1,260) from the start of the tribulation has generated speculation about preparation periods for judgment, temple rededication, or the regathering of the scattered. What is clear is the pastoral intent: the blessing is for those who persevere and endure beyond what seems to be the final moment. Endurance beyond the expected endpoint — not giving up when the tribulation outlasts the initial estimate — is the specific virtue commended.</p>",
    "13": "<p>'As for you, go your way till the end. You will rest, and then at the end of the days you will rise to receive your allotted inheritance' (<em>telekh leqetz vetinaḥ vetamod legoral laqetz hayamin</em>) — the book closes with a personal resurrection promise to Daniel himself: he will 'rest' (die) and then 'rise' (<em>amad</em>, stand up) to receive his 'allotted inheritance' (<em>goral</em>, portion, lot — the term for one's share of the Promised Land in the division of Canaan, Josh 14-19). The cosmic resolution of empires (chs. 2, 7-12) comes home to a personal promise: Daniel will participate in the resurrection he has seen prophesied (v. 2) and receive the covenant inheritance that exile deferred. The book that began with the despoliation of the temple vessels ends with a promise that Daniel's personal <em>goral</em> is secure in the hands of the God who revealed these mysteries — a fitting conclusion to a book written for a community that had lost everything except the hope of resurrection.</p>"
  }
}

def main():
    existing = load_comm('mkt-context', 'daniel')
    merge_comm(existing, DANIEL)
    save_comm('mkt-context', 'daniel', existing)
    print('Daniel 12 mkt-context written.')

if __name__ == '__main__':
    main()
