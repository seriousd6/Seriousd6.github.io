"""
MKT Echo Layer — Esther chapters 6–10
Run: python3 scripts/zc-echo-esther-6-10.py

Ch6:  Providential insomnia — the king cannot sleep; the hidden divine hand (6:1) — Ps 121:4; Rom 8:28
      Haman forced to honor Mordecai — the enemy serves the one he planned to destroy (6:11) — Phil 2:10-11
Ch7:  Esther's intercession before the king — asking for her life and her people's (7:3-4) — Rom 8:34; Heb 7:25
      Haman hanged on his own gallows — falls into the pit he dug (7:10) — Ps 7:15-16; Gal 6:7
Ch8:  Esther given Haman's house — spoils of the enemy to the redeemed (8:1) — Col 2:15; Luke 11:22
      Esther: I cannot bear to see destruction of my kindred (8:6) — Rom 9:3; 2 Cor 5:14
      The irrevocable first decree countered by a second decree of life (8:8-11) — 2 Cor 1:20; Rom 8:1-2
Ch9:  On the day enemies expected to prevail, the reverse occurred (9:1) — 1 Cor 1:25-27; 1 Pet 2:9
      Days of feasting, giving portions, gifts to the poor (9:22) — 1 Cor 11:26; 2 Cor 9:7
      These days shall never pass away — the permanent commemoration (9:28) — Luke 22:19
Ch10: Mordecai great among Jews, seeking welfare and speaking peace (10:3) — Rom 8:29; Eph 2:14-17
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

ECHOES = {
  "6": {
    "1": [
      {"type": "allusion", "target": "Ps 121:4", "note": "On that night the king could not sleep — the providential insomnia that sets in motion the entire reversal of Haman's plot. Psalm 121:4: 'He who keeps Israel will neither slumber nor sleep.' The king's sleeplessness is the narrative's most explicit moment of hidden divine activity: an apparently random occurrence (the insomniac king calling for the royal records) becomes the pivot on which Mordecai's deliverance turns. The God who never sleeps uses the king's inability to sleep as the instrument of his covenant protection. The irony is theologically dense: the human king sleeps when he should be waking; the divine King never sleeps — and it is the divine wakefulness operating through human insomnia that preserves the covenant people."},
      {"type": "allusion", "target": "Rom 8:28", "note": "The king cannot sleep; his servants read the chronicles aloud; the record of Mordecai's unrewarded service happens to be the text they reach. The chain of coincidences — insomnia, records, specific passage, Haman's arrival — is the narrative form of what Paul articulates theologically in Romans 8:28: 'we know that in all things God works for the good of those who love him, who have been called according to his purpose.' Esther 6:1 is the OT's most concentrated illustration of this principle: God works through what appears accidental to accomplish what is purposed. The author of Esther never names God, but the invisible hand behind the king's sleeplessness is unmistakable."}
    ],
    "3": [
      {"type": "allusion", "target": "Luke 18:7", "note": "The king asks: what honor or distinction has been bestowed on Mordecai for this? — and finds that nothing has been done. The delayed reward, the unrecompensed service, the deferred honor that suddenly arrives — this is the structure of Luke 18:7-8: 'will not God give justice to his elect who cry to him day and night? Will he delay long over them? I tell you, he will give justice to them speedily.' Mordecai waited years for the recognition of his service; the elect wait through the age for the vindication that appears to be delayed. In both cases, the moment of vindication when it comes is decisive and comprehensive."}
    ],
    "11": [
      {"type": "allusion", "target": "Phil 2:10", "note": "Haman leads Mordecai on horseback through the city square proclaiming: thus shall it be done to the man whom the king delights to honor. The man who planned Mordecai's execution is compelled to be the instrument of his public honor — the ultimate irony of reversal. Philippians 2:10-11: 'at the name of Jesus every knee should bow, in heaven and on earth and under the earth, and every tongue acknowledge that Jesus Christ is Lord.' The one whom the powers crucified will be publicly honored by every tongue that condemned him — including those who plotted his destruction. Haman's compelled proclamation of Mordecai's honor is the OT figure of the compelled universal confession of Christ's lordship."}
    ]
  },
  "7": {
    "3": [
      {"type": "allusion", "target": "Heb 7:25", "note": "Esther's petition before the king: if I have found favor in your sight, O king, and if it pleases the king, let my life be granted me at my petition, and my people at my request. The intercessor standing before the throne, asking for her own life and the lives of her people, is the structural type of Christ's high-priestly intercession. Hebrews 7:25: 'he is able to save to the uttermost those who draw near to God through him, since he always lives to make intercession for them.' Esther stands once at the Persian throne to plead for her people; Christ stands always at the heavenly throne to intercede for his. Where Esther risked death to enter the king's presence, Christ's intercession rests on his completed sacrifice — he has already paid the price that secures the ongoing access."},
      {"type": "allusion", "target": "Rom 8:34", "note": "Esther's plea — let my life be given me, and my people at my request — is the form of intercessory identification: the mediator is so bound up with the fate of those she represents that her own life is at stake with theirs. Romans 8:34: 'who is to condemn? Christ Jesus is the one who died — more than that, who was raised — who is at the right hand of God, who indeed is interceding for us.' Paul grounds the impossibility of condemnation in the living intercession of the one who has already died in our place. Esther's plea on behalf of her people is the OT form of the intercession that the NT grounds in the completed sacrifice."}
    ],
    "6": [
      {"type": "allusion", "target": "1 Pet 5:8", "note": "Esther names the enemy explicitly before the king: a foe and enemy — this wicked Haman! The unmasking of the adversary, the public identification of the one who has been plotting destruction behind the scenes, is the structural parallel to 1 Peter 5:8-9: 'your adversary the devil prowls around like a roaring lion, seeking someone to devour. Resist him, firm in your faith.' Esther's naming of Haman before the king is the act of resistance — bringing the enemy's plot into the light of the king's court. The gospel likewise unmasks the adversary: Christ came to destroy the works of the devil (1 John 3:8), which requires first identifying them for what they are."}
    ],
    "10": [
      {"type": "allusion", "target": "Gal 6:7", "note": "Haman is hanged on the very gallows he built for Mordecai — fifty cubits high, the conspicuous instrument of intended shame turned into the instrument of the conspirator's own destruction. Galatians 6:7: 'whatever one sows, that will he also reap.' The gallows-reversal is the most vivid OT instantiation of the sowing-and-reaping principle. Christ's resurrection applies this principle in its ultimate form: the cross — the instrument the powers used to destroy him — becomes the instrument of their defeat. The gallows Haman built for another became his own; the cross the powers built for Christ became the instrument of their disarmament (Col 2:15)."},
      {"type": "allusion", "target": "Ps 7:15", "note": "Haman fell into the pit he had dug. Psalm 7:15-16: 'He makes a pit, digging it out, and falls into the hole that he has made. His mischief returns upon his own head.' The Psalm describes as a general principle what Esther 7:10 narrates as a specific event: the wicked man's plot becomes his own destruction. The Esther narrative is the Psalm's most complete narrative enactment in the OT. The cross takes the principle to its ultimate expression: the powers that conspired to kill the Son of God found themselves defeated by the very act they thought was their victory."}
    ]
  },
  "8": {
    "1": [
      {"type": "allusion", "target": "Col 2:15", "note": "On that day King Ahasuerus gave to Queen Esther the house of Haman, the enemy of the Jews. The plundering of the enemy's household and the transfer of his property to the redeemed is the covenant-reversal pattern. Colossians 2:15: 'he disarmed the rulers and authorities and put them to open shame, by triumphing over them in him.' The cross achieved the ultimate property-transfer: what belonged to the powers — death's dominion, sin's mastery, the accusation against us — was disarmed and transferred. Esther's inheritance of Haman's house is the figure of the church's inheritance of what Christ's victory secured from the enemy."},
      {"type": "allusion", "target": "Luke 11:22", "note": "Esther is given the house of Haman — the enemy's property transferred to those he sought to destroy. Luke 11:22: 'when one stronger than he attacks him and overcomes him, he takes away his armor in which he trusted and divides his spoil.' The strong man (Haman) is overcome; his house is given to those he oppressed. Christ as the stronger man overcomes the strong man of sin and death (1 John 4:4: 'he who is in you is greater than he who is in the world'), and the plunder — freedom, righteousness, eternal life — is distributed to those who were held captive."}
    ],
    "6": [
      {"type": "allusion", "target": "Rom 9:3", "note": "Esther's anguished appeal: how can I endure to see the calamity that is coming to my people? Or how can I endure to see the destruction of my kindred? The intercessor who cannot emotionally or morally detach from the fate of those she represents — whose own wellbeing is inextricable from theirs — is the type of Christ's identification with his people. Romans 9:3: 'For I could wish that I myself were accursed and cut off from Christ for the sake of my brothers, my kinsmen according to the flesh.' Paul expresses the same intercessor's anguish: unable to bear the destruction of those he loves, he would sacrifice himself if it could help them. Christ actually made this sacrifice — not merely wishing it but accomplishing it."}
    ],
    "8": [
      {"type": "allusion", "target": "2 Cor 1:20", "note": "The first decree sealed with the king's ring cannot be revoked — but the king authorizes a second decree that gives the Jews the right to defend themselves. The two-decree structure illuminates the relationship between law and gospel: the first decree (death) cannot simply be cancelled — it was sealed with the king's seal. But a second decree can be written that creates a new reality within the first decree's framework. 2 Corinthians 1:20: 'all the promises of God find their Yes in him.' The law's death-decree is not cancelled in the gospel but fulfilled — Christ bears the curse of the first decree (Gal 3:13) so that those under it can live under the terms of the second."},
      {"type": "allusion", "target": "Rom 8:1", "note": "The first decree against the Jews cannot be revoked, but the second decree gives them the right to live. The two decrees co-exist: death is legally in force but life has been authorized by the king's own new decree. Romans 8:1: 'There is therefore now no condemnation for those who are in Christ Jesus. For the law of the Spirit of life has set you free in Christ Jesus from the law of sin and death.' The first law (condemnation) has not been erased from the record — it was enacted on Christ. But the second law (the Spirit of life) operates in Christ to give freedom to those who were condemned. The Esther two-decree structure is the OT narrative form of Paul's theological statement."}
    ],
    "16": [
      {"type": "allusion", "target": "1 Pet 2:9", "note": "For the Jews there was light and gladness and joy and honor — the fourfold description of the reversal experienced by the covenant people when the death-decree is countered by the life-decree. 1 Peter 2:9: 'you are a chosen race, a royal priesthood, a holy nation, a people for his own possession, that you may proclaim the excellencies of him who called you out of darkness into his marvelous light.' Peter's description of the church's new identity echoes the Esther vocabulary of light and honor: the people under the sentence of death, brought into light and gladness by the king's second decree, are the OT figure of the church brought from darkness into marvelous light."}
    ]
  },
  "9": {
    "1": [
      {"type": "allusion", "target": "1 Cor 1:27", "note": "On the very day that the enemies of the Jews had hoped to overpower them, the reverse occurred — the Jews gained mastery over those who hated them. The reversal at the moment of expected defeat is the structural heart of the Esther narrative and the pattern of the cross. 1 Corinthians 1:27: 'God chose what is foolish in the world to shame the wise; God chose what is weak in the world to shame the strong.' The cross was the moment the powers expected complete victory — and it was the moment of their defeat. The reversal on the appointed day of destruction is the Esther narrative's typological core: the day of death becomes the day of life."}
    ],
    "22": [
      {"type": "allusion", "target": "1 Cor 11:26", "note": "The Purim institution: days of feasting and gladness and sending portions to one another and giving gifts to the poor — the annual commemoration of deliverance through communal eating, sharing, and remembering. 1 Corinthians 11:26: 'for as often as you eat this bread and drink the cup, you proclaim the Lord's death until he comes.' Both Purim and the Lord's Supper are commemorative meals that enact the community's identity as those who have been delivered from death. Purim celebrates deliverance from Haman's death-decree; the Lord's Supper celebrates deliverance from sin's death-sentence. Both are annual/recurring acts of communal memory that constitute the community's identity as the saved."},
      {"type": "allusion", "target": "2 Cor 9:7", "note": "The Purim instructions include giving gifts to the poor — the deliverance of the community becomes the occasion for generosity toward those in need. 2 Corinthians 9:7: 'Each one must give as he has decided in his heart, not reluctantly or under compulsion, for God loves a cheerful giver.' Paul's theology of cheerful giving is rooted in the same gratitude-logic as the Purim gift-giving: those who have received deliverance give freely from the overflow of their received grace. The joy of Purim — a community celebrating its escape from death — generates the giving that the NT connects to the gospel's own generosity (2 Cor 9:15: 'thanks be to God for his inexpressible gift')."}
    ],
    "28": [
      {"type": "allusion", "target": "Luke 22:19", "note": "These days of Purim should never fall into disuse among the Jews — the permanent institutionalization of the commemorative celebration. Luke 22:19: 'do this in remembrance of me.' Both Purim and the Lord's Supper are perpetual commemorations instituted by those who experienced deliverance. The Esther narrative establishes a covenant of remembrance — the community binds itself never to forget — and the NT establishes the new-covenant counterpart: the regular breaking of bread in remembrance of Christ's body given and blood poured out. Both institutions create communities defined by their memory of a decisive deliverance from death."}
    ]
  },
  "10": {
    "3": [
      {"type": "allusion", "target": "Rom 8:29", "note": "Mordecai was great among the Jews and popular with the multitude of his brothers, for he sought the welfare of his people and spoke peace to all his descendants. The great man among his brothers who speaks peace and seeks the community's welfare is the figure of Christ, the firstborn among many brothers (Rom 8:29: 'for those whom he foreknew he also predestined to be conformed to the image of his Son, in order that he might be the firstborn among many brothers'). Mordecai's greatness is exercised in service to the community's welfare and peace; Christ's greatness is expressed in his complete self-giving for the life and peace of those who are his brothers by adoption."},
      {"type": "allusion", "target": "Eph 2:14", "note": "Mordecai spoke peace to all his descendants — the great man of the Persian court uses his position and influence to speak shalom over the covenant community. Ephesians 2:14: 'For he himself is our peace, who has made us both one and has broken down in his flesh the dividing wall of hostility.' Mordecai's peace-speaking is the shadow; Christ's peace-making is the substance. Where Mordecai speaks peace to one community from a position of political influence, Christ makes peace between humanity and God and between Jew and Gentile through the sacrifice of himself. The book of Esther ends with a man who speaks peace; the gospel ends with the one who is peace."}
    ]
  }
}

def main():
    e = load_echo('esther')
    merge_echo(e, ECHOES)
    save_echo('esther', e)
    count = sum(len(v) for v in ECHOES.values())
    print(f'esther echo: wrote entries for {count} verses across ch 6-10')

if __name__ == '__main__':
    main()
