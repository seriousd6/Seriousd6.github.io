"""
MKT Original Commentary — 1 Samuel chapters 17–18
Run: python3 scripts/zc-original-1samuel-17-18.py

Ch17: David and Goliath — the definitive narrative of the anointed underdog;
      the champion-combat structure (ish habênayim); the name of YHWH;
      YHWH's war; the head-crushing blow
Ch18: Jonathan's covenant with David; Saul's jealousy; David's wisdom-success
      (sakal); the souls knit together (nepeš qāšar)

Key Hebrew terms:
- ish habênayim (17:4): man of the between-two-spaces — the dueling champion
- ḥerpāh (17:26): reproach/defiance — the theological charge in the battle
- shem YHWH tseva'ot (17:45): the name invoked against Goliath's armor
- milḥemet YHWH (17:47): YHWH's battle — the war belongs to YHWH
- nepeš qāšar (18:1): soul-knitting — Jonathan and David's bond
- śākal (18:5,14,15): act wisely and succeed — David's Spirit-empowered wisdom
"""

import json, pathlib

ROOT = pathlib.Path(__file__).parent.parent

def load_comm(layer, book):
    p = ROOT / 'data' / 'commentary' / layer / f'{book}.json'
    return json.loads(p.read_text()) if p.exists() else {}

def save_comm(layer, book, data):
    p = ROOT / 'data' / 'commentary' / layer / f'{book}.json'
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

ORIGINAL = {
  "17": {
    "4": "<p>Goliath is introduced as <em>ʾîš habênayim</em> — 'man of the between-two-spaces' — the technical term for a single combat champion who stands between the two armies to settle the battle by representative duel. The <em>bênayim</em> (the space between) is the no-man's land where the champions meet; the champion's defeat ends the battle. This is the ANE institution of <em>monomachia</em> — individual combat as proxy warfare. The irony of the narrative is that Israel has a champion — YHWH — who dwells in the <em>bênayim</em> between heaven and earth, whose representative David will enter the space as YHWH's proxy. Goliath is the embodiment of all that looks like an unsurmountable adversary: six cubits and a span tall, armored in bronze, with a spear like a weaver's beam. The narrative establishes the appearance of insurmountability before the reversal.</p>",
    "26": "<p>David's first question — <em>mî haʿārēl happəlištî hazzeh kî ḥērēp maʿarəḵôt ʾelōhîm ḥayyîm</em> — 'Who is this uncircumcised Philistine that he should defy the armies of the living God?' — introduces the key theological term <em>ḥerpāh</em> (reproach, defiance, shame). Goliath's challenge is not merely military; it is a covenant-theological defiance: he stands against <em>ʾelōhîm ḥayyîm</em> (the living God), which David will address directly in v45-46. The term <em>ḥerpāh</em> (shame/reproach) appears in Ps 22:6 — 'I am a reproach (<em>ḥerpāh</em>) to men' — where the Davidic king takes on the shame that Goliath levied. The one who defeats the shame-levying giant in ch17 will himself bear shame in Ps 22 — the trajectory from victorious champion to suffering servant in the Davidic typology.</p>",
    "45": "<p>David's declaration of battle terms is a liturgical counter to Goliath's military credentials: <em>ʾattāh bāʾ ʾēlay bəḥereḇ ûḇaḥănît ûḇəḵîḏôn wəʾānōḵî bāʾ ʾēleyḵā bəšēm YHWH ṣəḇāʾôt</em> — 'You come to me with sword and spear and javelin, but I come to you in the name of YHWH of armies.' The contrast is between weaponry (<em>ḥereḇ, ḥănît, kîḏôn</em> = sword, spear, javelin — three weapons for Goliath's three-fold armament) and the <em>šēm YHWH ṣəḇāʾôt</em> (the name of YHWH of armies). The name (<em>šēm</em>) is the representative presence of YHWH — invoked in battle as the living divine warrior (cf. Ps 20:5 — 'in the name of our God we will set up our banners'). <em>YHWH ṣəḇāʾôt</em> (YHWH of armies) is the divine warrior title par excellence; David is fighting as YHWH's champion, and the <em>šēm</em> is his weapon.</p>",
    "47": "<p>David's theological summary of the battle: <em>wəyēḏᵉʿû kol haqqāhāl hazzeh kî lōʾ bəḥereḇ ûḇaḥănît yôšîaʿ YHWH kî laYHWH hammilḥāmāh</em> — 'all this assembly will know that not by sword or spear does YHWH save; for the battle belongs to YHWH.' The phrase <em>laYHWH hammilḥāmāh</em> (to YHWH belongs the battle) is the most compressed statement of holy war theology in the Samuel narratives. It echoes Moses at the Red Sea (Exod 14:13-14 — 'Stand firm and see the salvation of YHWH... YHWH will fight for you') and Jehoshaphat's battle prayer (2 Chr 20:15 — 'the battle is not yours but God's'). The purpose of the victory is explicitly missional: 'that all the earth may know that there is a God in Israel' (v46) — YHWH's glory among the nations as the goal of the anointed's battle.</p>",
    "49": "<p>The sling-stone strikes Goliath in the forehead (<em>miṣḥô</em>): <em>wayyitbāʿ hāʾeḇen bᵉmiṣḥô wayyipōl ʿal pānāyw ʾārṣāh</em> — 'the stone sank into his forehead, and he fell on his face to the ground.' The blow to the head is the Gen 3:15 vocabulary enacted: <em>rōʾš</em> (head) — 'he shall crush your head' (<em>yəšûpəḵā rōʾš</em>). The serpent's-head-crushing prophecy finds one of its clearest pre-Christ actualizations here: the seed of the woman (the young shepherd, the least expected champion) strikes the representative of all forces arrayed against YHWH's people through the head. The forehead strike is not incidental but structurally significant — it is the narrative's way of gesturing toward Gen 3:15 while pointing beyond all human champion-combatants to the one who will finally crush the serpent.</p>",
    "51": "<p>David takes Goliath's own sword and cuts off his head: <em>wayyiqaḥ dāwiḏ ʾet ḥarbô wayyišlᵉpāh mittaʿrāh wayyᵉmōtəṯēhû wayyiḵrat bāh ʾet rōʾšô</em> — 'David took his sword and drew it from its sheath and killed him and cut off his head with it.' The use of the enemy's own weapon to execute the final blow is the book's ironic statement: the armament that was supposed to terrify Israel becomes the instrument of Goliath's destruction. This is the NT pattern for Christ's victory over death: 'that through death he might destroy the one who has the power of death' (Heb 2:14) — the weapon of the adversary (death) becomes the mechanism of the adversary's defeat. David takes the giant's head to Jerusalem (v54), presaging the future capital where the Davidic line will reign and ultimately where the serpent's head will be crushed once for all.</p>"
  },
  "18": {
    "1": "<p>The soul-binding between Jonathan and David: <em>wᵉnepeš yôhônātān niqšərāh bᵉnepeš dāwiḏ wayyeʾĕhāḇēhû yôhônātān kᵉnapšô</em> — 'and the soul (<em>nepeš</em>) of Jonathan was knit (<em>niqšərāh</em>) to the soul of David, and Jonathan loved him as his own soul.' The verb <em>qāšar</em> (to bind, knit, tie) is the construction-verb: what happens is an ontological binding of two <em>napšôt</em>. The <em>nepeš</em> in Hebrew is not merely the 'soul' in a Platonic sense but the whole animated person — the breathing, feeling, willing self. Jonathan's self-gift to David (stripping his robe, armor, sword, bow, belt in v4) enacts in action what the soul-binding describes in ontological terms. The love standard — 'as his own soul' (<em>kənapšô</em>) — is the Lev 19:18 standard that Jesus cites as the second great commandment.</p>",
    "3": "<p>The covenant between Jonathan and David: <em>wayyiḵrot yôhônātān wəḏāwiḏ bərît bəʾahăḇātô ʾōtô kənapšô</em> — 'Jonathan cut a covenant with David, in his love for him as his own soul.' The <em>kārat bərît</em> (cutting a covenant) formula marks this as a formal covenant transaction, not merely friendship. The covenant is motivated by love (<em>ʾahăḇāh</em>) — the word used for covenant-loyalty love throughout the OT (Deut 6:5; 7:9; 1 Kgs 3:3). Jonathan's enactment of covenant love toward David — the crown prince stripping himself of his royal insignia to clothe the shepherd — is the OT's most vivid picture of kenotic self-emptying in covenant: rank, privilege, and weapon transferred to the beloved. The NT pattern is explicit: 'He who had equality with God did not count it a thing to be grasped but emptied himself' (Phil 2:6-7).</p>",
    "5": "<p>David succeeds everywhere: <em>wayyaśkēl dāwiḏ bᵉḵōl ʾăšer yišlāḥēhû šāʾûl</em> — 'David acted wisely (<em>śākal</em>) in everything Saul sent him to do.' The verb <em>śākal</em> (in the <em>hiph'il</em>: to act wisely, to prosper through prudent action) is the vocabulary of covenant wisdom — the same root as <em>haśkîl</em> in Ps 101:2 and <em>maśkîl</em> in the Psalm superscriptions. The verb combines wisdom, insight, and the resulting success: to act with discernment that leads to divine favor and practical effectiveness. The pattern — the Spirit-anointed son who succeeds in everything — runs from Joseph (Gen 39:3 — 'YHWH caused all he did to succeed') through David to the messianic portrayal of the Servant who 'acts wisely' (<em>yaśkîl</em>) before his suffering (Isa 52:13 — 'my servant shall act wisely / be high and lifted up').</p>",
    "12": "<p>Saul's fear of David: <em>wayyirāʾ šāʾûl mippənê dāwiḏ kî hāyāh YHWH ʿimmô ûmēʿim šāʾûl sār</em> — 'Saul was afraid of David because YHWH was with him but had departed from Saul.' The structure is a covenant-reversal: <em>YHWH ʿimmô</em> (YHWH was with him) has transferred from Saul to David. The divine presence-formula (<em>YHWH ʿim X</em>) tracks covenant election: it is with Abraham (Gen 21:22), Isaac (Gen 26:28), Jacob (Gen 28:15), Joseph (Gen 39:2), Moses (Exod 3:12), Joshua (Josh 1:5), Gideon (Judg 6:12), and now David. Saul's fear is the inverse of covenant confidence — he sees that the divine presence that underwrites success has left him and rests on his rival. Saul's <em>yārēʾ</em> (fear) of David is the fear that comes from recognizing that YHWH has chosen another.</p>"
  }
}

def main():
    c = load_comm('mkt-original', '1samuel')
    merge_comm(c, ORIGINAL)
    save_comm('mkt-original', '1samuel', c)
    count = sum(len(v) for v in ORIGINAL.values())
    print(f'1samuel mkt-original: wrote {count} verses across ch 17-18')

if __name__ == '__main__':
    main()
