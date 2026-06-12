#!/usr/bin/env python3
"""
mkt-christ commentary — Proverbs 31 (31 verses)
Two sections:
  vv.1–9  — Oracle of King Lemuel (Massa): queen mother's instruction on kingly virtue
  vv.10–31 — Eshet Chayil / ʾēšet ḥayil acrostic: the valiant woman (aleph–taw)

Christological classification decisions:
  31:5  = 'theme'  (perverting justice for the poor → Christ as just judge, Rev 19:11)
  31:8  = 'direct' (speak for the mute/perishing → Christ's advocacy, Heb 7:25; Isa 53:7 contrast)
  31:9  = 'direct' (defend poor and needy → Luke 4:18; Matt 25:40)
  31:10 = 'type'   (ʾēšet ḥayil as type: Church as bride of Christ, Eph 5:25-27; Rev 19:7-8)
  31:11 = 'type'   (husband's heart trusts her → Christ's trust in his redeemed people)
  31:20 = 'theme'  (she opens hand to poor → Christ's generosity embodied in his body)
  31:23 = 'type'   (husband known at the gates → Christ exalted, Phil 2:9-11)
  31:25 = 'theme'  (strength and dignity her clothing → arrayed in righteousness, Rev 19:8)
  31:26 = 'type'   (law of kindness on her tongue → Christ the living Word, John 1:14)
  31:30 = 'theme'  (fear of the LORD praised → Christ the fullness of wisdom, Col 2:3)
  31:31 = 'theme'  (her works praise her in the gates → deeds known at judgment, Matt 7:20)
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

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

PROVERBS = {
    "31": {
        "1": "<p>The oracle of King Lemuel — words his mother taught him. This royal figure shaped by maternal wisdom anticipates Christ, the Son taught by the Father (John 8:28), who came not to be served but to serve (Mark 10:45). The king under instruction mirrors the incarnate Son who learned obedience through what he suffered (Heb 5:8).</p>",
        "2": "<p>The triple address 'O my son … son of my womb … son of my vows' expresses the depth of a mother's covenant investment in her child. The intensity of this love foreshadows the Father's declaration over Christ: 'This is my beloved Son, in whom I am well pleased' (Matt 3:17) — a voice from heaven investing the Son for his royal mission.</p>",
        "3": "<p>The queen mother warns against wasting strength on women who destroy kings — a warning against power dissipated in folly rather than deployed for the vulnerable. Christ, the true king, never diverted his strength to self-serving ends; he 'did not please himself' (Rom 15:3) but spent every resource on the redemption of his people.</p>",
        "4": "<p>'It is not for kings to drink wine … lest they forget what is decreed and pervert the rights of all the afflicted.' The king must remain clear-minded to execute justice. Christ, the King of kings, never clouded his judgment; even at Gethsemane he refused the wine mingled with myrrh that would have dulled his suffering (Mark 15:23), maintaining full conscious submission to the Father's will.</p>",
        "5": "<p class='christ-theme'>Drunkenness causes rulers to 'forget what is decreed and pervert the rights of all the afflicted.' This inversion of justice — the law weaponized against the needy — stands in stark contrast to Christ the righteous judge. Revelation 19:11 pictures him returning to 'judge and make war' in righteousness; Isaiah 42:3 promises he will not break the bruised reed nor quench the smoldering wick. His throne is established on justice and righteousness (Ps 89:14).</p>",
        "6": "<p>The counsel to give strong drink to the dying and wine to the bitter in soul reflects ancient palliative practice — numbing the pain of the perishing. This mercy toward the suffering anticipates Christ, who gave himself as the true comfort for those in mortal anguish. He is the 'Father of mercies and God of all comfort' (2 Cor 1:3), and at the Last Supper he took the cup that spoke of his own suffering poured out for many (Matt 26:27-28).</p>",
        "7": "<p>Let those in poverty and misery drink and forget their need — a compassionate concession to the desperate. Christ's mercy toward the suffering was not merely palliative but transformative: he came to announce release to the captives and liberty to the oppressed (Luke 4:18), not simply numbing their pain but removing the cause. He is the physician who heals rather than only sedates.</p>",
        "8": "<p class='christ-direct'>The king is commanded: 'Open your mouth for the mute, for the rights of all who are destitute.' Isaiah 53:7 shows Christ as the Servant who 'opened not his mouth' at his own trial — but this silence was in his own defense, not in defense of the needy. As the exalted intercessor, Christ fulfills this command permanently: he 'always lives to make intercession' for his people (Heb 7:25). He is the advocate who speaks for those who cannot speak for themselves (1 John 2:1).</p>",
        "9": "<p class='christ-direct'>The climax of Lemuel's instruction: 'Open your mouth, judge righteously, defend the poor and needy.' This triple imperative defines the messianic king. Luke 4:18-19 is Jesus' programmatic announcement that he came to bring good news to the poor, release to the captive, sight to the blind. Matthew 25:40 identifies the poor and needy as the very face of Christ himself — so to serve the needy is to serve the King who commands it.</p>",
        "10": "<p class='christ-type'>The opening question — 'An excellent wife who can find? She is far more precious than jewels' — launches a 22-verse acrostic (aleph to taw) celebrating the ʾēšet ḥayil, the valiant woman. The rarity and preciousness of this figure, impossible by human effort alone, positions her as a type of the Church as the bride of Christ: 'a glorious church, not having spot or wrinkle … holy and without blemish' (Eph 5:27). Just as the virtuous woman must be found rather than fabricated, the Church is Christ's finding and making — chosen before the foundation of the world (Eph 1:4).</p>",
        "11": "<p class='christ-type'>Her husband's heart trusts safely in her, and he lacks nothing of value. In the typology of bride and bridegroom, Christ the husband entrusts himself to his Church — his body, his mission, his name in the world. This is the astonishing condescension of the covenant: Christ 'gave himself up for her' (Eph 5:25) and then entrusts his ongoing work to the community he has redeemed and sent (John 20:21; Matt 28:18-20).</p>",
        "12": "<p>She does him good and not harm all the days of her life — a portrait of covenant faithfulness across a lifetime. The Church's calling is to do good to Christ's name and purposes in the world, bearing fruit in every season. This echoes Paul's prayer that believers be 'filled with the fruit of righteousness that comes through Jesus Christ, to the glory and praise of God' (Phil 1:11).</p>",
        "13": "<p>She seeks wool and flax and works with willing hands. The valiant woman's industriousness — raw material gathered and transformed — prefigures the Spirit-empowered ministry of the Church, gathering the materials of human need and transforming them through the gospel. The willingness of her hands recalls Christ's own willing sacrifice: 'Not my will, but yours, be done' (Luke 22:42).</p>",
        "14": "<p>She is like merchant ships bringing food from afar — resource gathering at great distance and cost. The Church, like her Lord, reaches to the far ends of the earth (Acts 1:8), bringing the bread of life that Christ himself provides. Christ is the true bread that comes down from heaven (John 6:35), and the Church is the vessel that carries him to those who have not yet tasted.</p>",
        "15": "<p>She rises while it is yet night to provide food for her household and portions for her maidens. The pre-dawn rising evokes sacrificial dedication — giving before others are awake. Christ's resurrection took place 'early on the first day of the week, while it was still dark' (John 20:1); he rose to provide new life for his household. The Church rises early in the world's night to distribute the bread he has provided.</p>",
        "16": "<p>She considers a field and buys it; from her fruit she plants a vineyard. Deliberate investment, calculated risk, and productive stewardship characterize the valiant woman. Jesus' parables of the kingdom describe similar investment strategies: the man who found a treasure in a field 'sold all that he had and bought that field' (Matt 13:44). The Church exercises the same discernment, investing gospel resources where fruit will grow.</p>",
        "17": "<p>She dresses herself with strength and makes her arms strong. The garment of strength recalls Isaiah's call to 'put on strength' as divine invitation (Isa 52:1) and Paul's armor of God (Eph 6:10-17). The Church's strength is not her own — it is the 'strength that God supplies' (1 Pet 4:11), the power of Christ's resurrection at work in his people (Phil 3:10; Eph 1:19-20).</p>",
        "18": "<p>She perceives that her merchandise is profitable; her lamp does not go out at night. The lamp burning through the night recalls the parable of the ten virgins (Matt 25:1-13): those with oil whose lamps remain lit are ready for the bridegroom. The Church is called to be a city on a hill, a lamp not hidden under a basket (Matt 5:14-16), keeping the light of the gospel burning until the dawn of the Lord's return.</p>",
        "19": "<p>Her hands reach to the distaff and her fingers grasp the spindle — patient, skilled, repetitive labor sustaining the household. The quiet faithfulness of her craft parallels the hidden work of the Spirit in the Church: not spectacular, but steady and life-giving. Paul describes the Church being knit together in love, growing with a growth that is from God (Col 2:2, 19).</p>",
        "20": "<p class='christ-theme'>She opens her hand to the poor and reaches out her hands to the needy. The outstretched hands of generosity take on profound resonance in Christ, whose hands were stretched out on the cross — the ultimate act of giving to the needy. The Church participates in this gesture whenever she extends mercy: 'You did it to me' (Matt 25:40). Christ's generosity becomes the Church's generosity, her hands becoming his hands in the world.</p>",
        "21": "<p>She is not afraid of snow for her household, for all her household are clothed in scarlet. She has prepared her household against the cold — the crisis does not catch her unready. Christ has prepared his Church for the world's opposition: 'In the world you will have tribulation. But take heart; I have overcome the world' (John 16:33). The scarlet clothing suggests both warmth and the blood of the covenant that covers and protects the redeemed community.</p>",
        "22": "<p>She makes bed coverings for herself; her clothing is fine linen and purple. Fine linen and purple are the vestments of dignity and royalty — she dresses herself in accordance with her identity. The Church is clothed by Christ: Revelation 19:8 describes the Bride's 'fine linen, bright and pure' as 'the righteous deeds of the saints,' the garment of her sanctification given by grace and expressed in action.</p>",
        "23": "<p class='christ-type'>Her husband is known in the gates when he sits among the elders of the land. The gates were the place of authority, legal transaction, and public honor. The valiant woman's husband is publicly recognized and honored. In the Christological typology, this points to the exaltation of Christ: God 'highly exalted him and bestowed on him the name that is above every name' (Phil 2:9). The Church's faithfulness serves her Lord's public honor — his name is magnified when his people live uprightly.</p>",
        "24": "<p>She makes linen garments and sells them; she delivers sashes to the merchant. Her commercial activity extends her provision beyond the household into the marketplace, sustaining relationships of exchange and mutual benefit. The Church operates in the world's marketplace — not extracting from it but contributing to it, demonstrating the justice and generosity of the kingdom. Paul worked as a tentmaker precisely to model self-giving service (Acts 18:3; 1 Thess 2:9).</p>",
        "25": "<p class='christ-theme'>Strength and dignity are her clothing, and she laughs at the time to come. The eschatological confidence — laughing at the future rather than fearing it — is grounded in her preparation and character. The Church's laughter at what is to come is grounded not in her own resources but in the resurrection of Christ: 'Where, O death, is your victory? Where, O death, is your sting?' (1 Cor 15:55). She is clothed in the righteousness of Christ (2 Cor 5:21), which no future threat can strip away.</p>",
        "26": "<p class='christ-type'>She opens her mouth with wisdom, and the teaching of kindness is on her tongue. The valiant woman is a speaking figure — her words carry wisdom and covenant love (ḥesed). This anticipates the Church as the continuing presence of Christ the living Word (John 1:14) in the world. The Church speaks Christ when she speaks truly, and the 'law of kindness' on her tongue reflects the love-command of Jesus: 'Love one another as I have loved you' (John 15:12).</p>",
        "27": "<p>She looks well to the ways of her household and does not eat the bread of idleness. Vigilant oversight of the household recalls Christ's own watchfulness over his Church: 'I will build my church, and the gates of hell shall not prevail against it' (Matt 16:18). The elders of the Church are similarly called to shepherd the flock with vigilance, not lording it over them but as examples (1 Pet 5:2-3) — following the pattern of the Chief Shepherd.</p>",
        "28": "<p>Her children rise up and call her blessed; her husband also, and he praises her. The blessing pronounced by children and husband is the testimony of those who have experienced her faithfulness most intimately. The Church's ultimate validation is the testimony of those transformed by her ministry — and the voice of the Lord himself who says, 'Well done, good and faithful servant' (Matt 25:21). To be praised by Christ is the Church's highest aspiration.</p>",
        "29": "<p>'Many women have done excellently, but you surpass them all.' The superlative praise distinguishes the valiant woman from all predecessors. In typological terms, Christ is the fulfillment who surpasses all types: 'The law has but a shadow of the good things to come' (Heb 10:1). The Church, as his Bride, participates in this surpassing excellence — not by her own virtue but by union with the one who is 'better' and 'more excellent' than all that came before (Heb 1:4; 8:6).</p>",
        "30": "<p class='christ-theme'>Charm is deceitful and beauty is vain, but a woman who fears the LORD is to be praised. The fear of the LORD — the beginning and summit of Proverbs' whole wisdom project (1:7; 9:10) — is the true excellence. In Christ, this principle is perfectly embodied: he is the one 'in whom are hidden all the treasures of wisdom and knowledge' (Col 2:3), the one whose life was constituted by perfect reverence toward the Father (Heb 5:7-8). The Church is called to this same fear — not as terror but as loving awe before the one who redeemed her.</p>",
        "31": "<p class='christ-theme'>Give her the fruit of her hands, and let her works praise her in the gates. The final verse is a call to public acknowledgment of the valiant woman's deeds. The gates — the place of honor and judgment — will tell the truth about her. At the last judgment, Christ will make public what was done in secret: 'Then the King will say to those on his right, Come, you who are blessed by my Father' (Matt 25:34). The Church's faithful works, done in the name of Christ, will be made visible by him who sees in secret (Matt 6:4) and rewards openly.</p>"
    }
}

def main():
    existing = load_comm('mkt-christ', 'proverbs')
    merge_comm(existing, PROVERBS)
    save_comm('mkt-christ', 'proverbs', existing)
    print('Proverbs 31 mkt-christ written.')

if __name__ == '__main__':
    main()
