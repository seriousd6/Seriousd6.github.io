"""
MKT Original Commentary — 1 Samuel chapters 25–27
Run: python3 scripts/zc-original-1samuel-25-27.py

Ch25: Nabal and Abigail — nabal-as-fool wordplay; Abigail's intercession;
      the bundle of the living (tsrôr haḥayyîm); David restrained from bloodguilt
Ch26: David spares Saul second time — YHWH's deep sleep (tardēmāh); the anointed's
      inviolability; David's confidence in divine recompense
Ch27: David's exile in Philistia — sojourner theology; the double-dealing deception;
      Achish and Ziklag

Key Hebrew terms:
- nāḇāl / nəḇālāh (25:25): fool / folly — the man's name = his character
- ṣᵉrôr haḥayyîm (25:29): bundle of the living — unique divine-preservation metaphor
- tardēmāh YHWH (26:12): the deep sleep from YHWH — theophanic protection
- māšîaḥ YHWH (26:9,11,23): YHWH's anointed — the covenant term for the chosen king
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
  "25": {
    "25": "<p>Abigail's etymology of her husband's name is the book's most explicit wordplay: <em>nāḇāl šəmô ûnəḇālāh ʿimmô</em> — 'Nabal is his name and folly (<em>nəḇālāh</em>) is with him.' The noun <em>nāḇāl</em> and the abstract noun <em>nəḇālāh</em> share the same root and are placed in immediate sequence — the man is his name. In biblical thought names both reveal and shape character; Nabal's name is not incidental but definitional. The root <em>nāḇal</em> (to be senseless, to wither) describes the fool who operates with no regard for covenant relationship — Ps 14:1's <em>nāḇāl</em> says 'there is no God,' not as formal atheism but as practical denial of YHWH's claims. Nabal's refusal of David is precisely this: the practical denial that YHWH's anointed has any claim on his resources. His folly is not stupidity but willful covenant-blindness.</p>",
    "28": "<p>Abigail's intercession speech is a theological oracle in the form of a petition. She employs the phrase <em>ḥerpat pešaʿ</em> — 'guilt of transgression' — using <em>pešaʿ</em>, the Hebrew word for deliberate revolt against a superior (the strongest of the three main sin-words: <em>ḥēṭ</em> = missing the mark, <em>ʿāwōn</em> = iniquity, <em>pešaʿ</em> = rebellion against a sovereign). She asks David not to incur bloodguilt (<em>dām ḥinnām</em>, blood for nothing) and not to take personal vengeance — offering herself as the target of David's anger. The structure of her intercession is mediatorial: she stands between the guilty party (her household) and the righteous king's wrath, taking the penalty onto herself. This is the mediatorial structure that the NT theology of atonement employs: Christ stands between guilty humanity and the Father's righteous judgment, taking the consequence onto himself (2 Cor 5:21).</p>",
    "29": "<p>Abigail's oracle about David's future contains the most beautiful metaphor of divine preservation in the Samuel narratives: <em>wᵉhāyᵉṯāh nepeš ʾăḏōnî ṣᵉrûrāh biṣrôr haḥayyîm ʾēt YHWH ʾelōhêḵā</em> — 'the soul (<em>nepeš</em>) of my lord shall be bound (<em>ṣᵉrûrāh</em>) in the bundle (<em>ṣrôr</em>) of the living (<em>haḥayyîm</em>) with YHWH your God.' The word <em>ṣrôr</em> (bundle/pouch) is the small leather pouch used to carry valuables — precious stones, coins, documents. YHWH holds David's <em>nepeš</em> as a precious object in a sealed pouch: secured, protected, carried close. The image draws on the ANE custom of binding something valuable in a cloth or leather bundle to keep it safe during travel. The contrast is immediate: the enemies' lives are flung away 'as from the hollow of a sling' (<em>qelaʿ</em>) — the same weapon David used against Goliath. The bundle vs. the sling is the image of covenant security vs. covenant exposure.</p>",
    "32": "<p>David's response to Abigail begins with a theological recognition: <em>bārûḵ YHWH ʾelōhê yiśrāʾēl ʾăšer šᵉlaḥēḵ hayyôm hazzeh liqrāʾtî</em> — 'Blessed is YHWH the God of Israel who sent you today to meet me.' The divine agency in Abigail's interception is explicit: David identifies her arrival as YHWH's providential dispatch. The baruch-formula (blessed be YHWH) is the standard OT acclamation of divine action in history (cf. Exod 18:10 — Jethro's baruch when he hears of the Exodus; 1 Sam 25:32,39 — David says it twice in this chapter). David is learning the pattern that will define his psalms: divine provision arrives through human agents, and the proper response is to bless YHWH rather than praise the human instrument.</p>"
  },
  "26": {
    "9": "<p>David's restraint of Abishai: <em>ʾal tašḥîtēhû kî mî šālaḥ yāḏô bimšîaḥ YHWH wᵉniqqāh</em> — 'Do not destroy him, for who has sent his hand against YHWH's anointed and been innocent?' The title <em>māšîaḥ YHWH</em> (YHWH's anointed) is the covenant title that designates the king chosen and empowered by YHWH. <em>Māšîaḥ</em> derives from <em>māšaḥ</em> (to anoint with oil) — the ritual that marks covenant appointment. Saul received this title at his anointing (10:1); David will receive it at his (16:13). The inviolability David asserts for Saul-as-<em>māšîaḥ</em> applies equally to himself as the coming <em>māšîaḥ</em>. The word <em>māšîaḥ</em> in its later development becomes the formal title for the expected deliverer-king whose anointing transcends any individual (Dan 9:25-26), ultimately pointing to Jesus who is <em>christos</em> (the Greek translation of <em>māšîaḥ</em>) par excellence.</p>",
    "12": "<p>The deep sleep at the Philistine camp: <em>kî kullām yəšēnîm kî tardēmāh YHWH nāpᵉlāh ʿălêhem</em> — 'for they were all sleeping because a deep sleep from YHWH had fallen upon them.' The noun <em>tardēmāh</em> is used sparingly in the OT but always for divinely-caused unconsciousness: Gen 2:21 (the deep sleep that falls on Adam at Eve's creation), Gen 15:12 (Abram's deep sleep at the covenant-cutting ceremony), and here. The term marks YHWH's active, protective intervention — this is not ordinary sleep but theophanic suspension. David can walk through the sleeping camp as YHWH's representative because YHWH has prepared the way. The <em>tardēmāh</em> connects the Michmash protection of Jonathan (14:15, the theophanic panic) to the same divine-warrior sovereignty that clears the path for the anointed.</p>",
    "23": "<p>David's theological statement of confidence: <em>wᵉYHWH yāšîḇ lᵉʾîš ʾet ṣiḏqātô wᵉʾet ʾĕmûnātô</em> — 'YHWH returns to each man his righteousness (<em>ṣeḏāqāh</em>) and his faithfulness (<em>ʾĕmûnāh</em>).' The two covenant-virtue terms are significant: <em>ṣeḏāqāh</em> (righteousness) is right covenant conduct; <em>ʾĕmûnāh</em> (faithfulness/steadfastness) is the covenant virtue par excellence — the same root as <em>ʾāmēn</em>. David is asserting that covenant faithfulness will be divinely recognized and rewarded — YHWH is the eschatological judge who sees conduct no human witness can observe (he spared Saul in the dark camp; YHWH saw). This is the OT ground for the NT principle that God rewards the hidden righteous act (Matt 6:4 — 'your Father who sees in secret will reward you').</p>"
  },
  "27": {
    "1": "<p>David's interior monologue opens ch27: <em>wayyōʾmer dāwiḏ ʾel libbô</em> — 'David said in his heart.' The expression <em>ʾāmar ʾel lēb</em> (to say to one's heart) is the formula for inner deliberation or self-counsel — it appears in Gen 8:21 (YHWH's inner resolve after the flood), Ps 14:1 (the fool's inner denial of God), and frequently in Ecclesiastes for Qohelet's self-directed inquiry. David's inner speech is not prayer (he does not speak to YHWH) but a pragmatic calculation under pressure. That the man who just twice relied on YHWH's protection now calculates survival without mentioning YHWH is the narrative's signal of spiritual fatigue — the same exhaustion that appears in Elijah under the juniper tree (1 Kgs 19:4). The <em>ʾāmar ʾel lēb</em> without a divine address marks the moment when covenant confidence gives way to human calculation.</p>",
    "6": "<p>Achish gives David <em>ṣiqlag</em> (Ziklag): <em>wayyitēn lô ʾāḵîš bayyôm hahûʾ ʾet ṣiqlag</em>. Ziklag (<em>ṣiqlag</em>) is an unknown etymology — a Philistine city name with no clear Semitic derivation. The verse adds: <em>lāḵēn hāyᵉṯāh ṣiqlag lᵉmalᵉḵê yᵉhûḏāh ʿad hayyôm hazzeh</em> — 'therefore Ziklag has belonged to the kings of Judah until this day.' This is the narrator's anachronism that confirms the later monarchic horizon of the account: the Philistine gift becomes a Judahite royal possession, and the comment 'to this day' marks it as a living geographical memory. Ziklag is thus a type of the exile-period pattern: the anointed king receives territory in unexpected circumstances, from unexpected sources, during the period of his rejection — preparation for the throne he will eventually occupy.</p>"
  }
}

def main():
    c = load_comm('mkt-original', '1samuel')
    merge_comm(c, ORIGINAL)
    save_comm('mkt-original', '1samuel', c)
    count = sum(len(v) for v in ORIGINAL.values())
    print(f'1samuel mkt-original: wrote {count} verses across ch 25-27')

if __name__ == '__main__':
    main()
