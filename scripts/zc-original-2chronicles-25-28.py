"""
MKT Original Commentary — 2 Chronicles chapters 25–28
Run: python3 scripts/zc-original-2chronicles-25-28.py

Ch25: ʾîš bᵉḥeṭʾô — Deut 24:16 cited verbatim; individual moral accountability (25:4)
      futility argument: gods who could not deliver their own people (25:15)
Ch26: dārash ʾĕlōhîm — Chronicler's seeking-vocabulary; prospered formula (26:5)
      wayyigbah libbô — pride-of-heart idiom; strength-to-pride pattern (26:16)
      lōʾ-lᵉkā ʿuzzîyāhû — name irony; priestly prerogative rebuked (26:18)
Ch27: ûbᵉal-bāʾ ʾel-hêkal — Jotham's restraint clause; contrast with Uzziah (27:2)
      wayyithazzēq — self-strengthening formula; covenant faithfulness (27:6)
Ch28: gêʾ ben-hinnōm — historical site; origin of NT Gehenna (28:3)
      ʿōḏēḏ — northern prophet's cross-kingdom intercession (28:9)
      action-chain verbs — clothing, feeding, anointing, transport (28:15)
      wayyōsep lim'ōl — compounding-treachery formula (28:22)
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

DATA = {
  "25": {
    "4": "<p><span class='term'>ʾîš bᵉḥeṭʾô</span> — 'each person for his own sin' (25:4). The Chronicler does not paraphrase but quotes Deut 24:16 verbatim as the legal ground for Amaziah's refusal to execute the sons of his father's killers. The formula establishes individual moral accountability as a statutory principle rooted in the Torah: fathers shall not die for children, children shall not die for fathers. The Aramaic cognate tradition preserves this non-transference principle in Targum as well. Ezekiel 18 develops the same formula into a full theology; the NT picks it up in Rom 14:12 ('each of us will give an account of himself to God'). The Chronicler's explicit citation — unusual in the historical narratives — signals that the legal basis mattered to the story's meaning, not merely the outcome.</p>",
    "15": "<p><span class='term'>ʾăšer lōʾ-hiṣṣîlû ʾet-ʿammām</span> — 'who did not deliver their own people from your hand' (25:15). The divine messenger's rhetorical question deploys the futility-of-idolatry argument in its sharpest form: you are seeking gods who demonstrably failed their own worshippers when you defeated them. The argument appears in Isa 10:10-11, 37:12, and elsewhere — defeated gods are gods who cannot save. The Chronicler uses military outcome as theological verdict: divine power is measured by actual capacity to deliver. The irony is structural — Amaziah, who just won a battle (vv. 11-12), immediately adopts the gods of the losers.</p>",
    "16": "<p><span class='term'>hᵃyōʾēṣ lammeleḵ nᵉtanûkā</span> — 'have they appointed you as the king's counselor?' (25:16). The prophet's sharp counter-question when Amaziah silences him. The <span class='term'>yāʾaṣ</span> / counselor vocabulary is significant: 1 Chr 27:32 catalogs David's counselors; the Chronicler regards unsolicited prophetic counsel as divinely mandated, not an imposition. Amaziah's refusal to receive the word — and his mocking it — triggers the Chronicler's editorial formula: 'God has determined to destroy you, because you have done this and have not listened to my counsel.' The prophet's withdrawal from the conversation does not withdraw the divine verdict.</p>"
  },
  "26": {
    "5": "<p><span class='term'>wayyiḏrōš ʾĕlōhîm</span> — 'he sought God' (26:5). The <span class='term'>dārash</span> root is the Chronicler's signature seeking-verb, appearing more often in Chronicles than in any other biblical book. The text specifies a teacher: Zechariah who instructed him in the fear of God — the seeking is not solitary but covenantally mediated. The result clause uses <span class='term'>hiṣlîaḥ</span> (to prosper, succeed): 'in the days of his seeking God, God prospered him.' The formula — seek God → prosper — is the positive side of the Chronicler's covenant calculus; its negative counterpart appears in the Ahaz account (ch 28). The temporal marker 'in the days of his seeking' implies the seeking had a duration limit, anticipating 26:16's collapse.</p>",
    "16": "<p><span class='term'>wayyigbah libbô</span> — 'his heart was proud' (26:16). The <span class='term'>lēb + gābaH</span> idiom is the Chronicler's standard formula for pride that precedes divine discipline: 'When he became strong, his heart rose up to his destruction.' The <span class='term'>kᵉḥizzᵉqātô</span> causal clause (when he became strong) shows the pattern: strength achieved through divine favor generates pride that overcomes divine fear. The same movement appears in Hezekiah (32:25) and Nebuchadnezzar (Dan 5:20 uses the same ûgābaH libbō). The trespass (<span class='term'>mā'al</span>) consists specifically in crossing into the priestly domain — the sanctuary breach that triggers leprosy.</p>",
    "18": "<p><span class='term'>lōʾ-lᵉkā ʿuzzîyāhû lᵉhaqqṭîr laYHWH</span> — 'it is not for you, Uzziah, to burn incense to the LORD' (26:18). The priest Azariah's rebuke deploys the name with pointed irony: <span class='term'>ʿuzzîyāhû</span> means 'YHWH is my strength' (ʿōz + YHWH), yet this man of YHWH-strength is being expelled from YHWH's sanctuary for overstepping the bounds that YHWH set. The phrase <span class='term'>lōʾ-lᵉkā</span> (not for you) marks the priestly prerogative claim — burning incense was reserved for the Aaronide priests (Num 16-17; Korah's rebellion involved the same boundary). The Chronicler's use of this story functions as a theological statement on the irreducibility of priestly vocation: political power does not authorize cultic function.</p>",
    "20": "<p><span class='term'>wayyibbāhᵃlûhû lāṣēʾt</span> — 'they rushed/hurried him out' (26:20). The Piel of <span class='term'>bhl</span> (to hasten, panic) indicates the priests' alarm when they saw the leprosy appear on Uzziah's forehead (<span class='term'>miṣraʿat bᵉmitsḥô</span>). The Chronicler specifies <span class='term'>gam-hûʾ niḏḥap lāṣēʾt</span> — 'and he himself was in a hurry to go out' — suggesting the leprosy functioned as an immediate divine verdict that even Uzziah recognized. The noun <span class='term'>miṣraʿat</span> (leprosy/skin-disease) in cultic contexts is a sign of ritual exclusion; Miriam's affliction (Num 12) and Gehazi's (2 Kgs 5:27) follow the same pattern of divine verdict through skin affliction.</p>"
  },
  "27": {
    "2": "<p><span class='term'>ûḇᵉal-bāʾ ʾel-hêkal YHWH</span> — 'but he did not enter the temple of YHWH' (27:2). The clause is the Chronicler's key characterization of Jotham's reign: he did what was right in YHWH's eyes, but unlike his father Uzziah he did not transgress the sanctuary boundary. The negative specification — restraint, not innovation — is presented as virtue. The Chronicler records the shortest account of a 'good' king in Chronicles here (9 verses), suggesting that absence of transgression is a positive category in the covenantal ledger. The phrase <span class='term'>wayyᵉšaḥēt hāʿām ʿôḏ</span> (the people still acted corruptly) forms a foil: the king's personal piety could not prevent communal corruption.</p>",
    "6": "<p><span class='term'>wayyithazzēq yôtām kî hēkîn dᵉrākāyw</span> — 'Jotham became mighty because he ordered his ways before YHWH his God' (27:6). The <span class='term'>hithazzēq</span> (Hithpael of ḥāzaq, reflexive — strengthened himself) echoes the wayyitkazzēq of Solomon in 2 Chr 1:1, the charge in 1 Chr 22:13, and David's repeated use of the same verb. The Chronicler uses this as a theological seal-word: a king who 'orders his ways' (<span class='term'>hēkîn dᵉrākāyw</span>) achieves the strengthening that is divine gift filtered through covenantal fidelity. The <span class='term'>kî</span> causal conjunction makes the covenant logic explicit — strength is the result of ordered-before-YHWH living, not independent achievement.</p>"
  },
  "28": {
    "3": "<p><span class='term'>bᵉgêʾ ben-hinnōm</span> — 'in the valley of the son of Hinnom' (28:3). The specific geographic designation marks the historical site of child-sacrifice under Ahaz and later Manasseh. The toponym <span class='term'>gêʾ-hinnōm</span> (valley of Hinnom) — in Greek <i>Gehinnom</i>, contracted to <i>Gehenna</i> — becomes in Second Temple Judaism the name for the place of eschatological punishment. The fire-child rites (hᵉʿbîr bāʾēš, 'passed through the fire') are described in 2 Kgs 16:3 and condemned in the Torah (Deut 18:10; Lev 18:21). The Chronicler's naming of the site with the same precision found in Jeremiah's Topheth passages (Jer 7:31-32; 19:2-6) links this historical record to the prophetic oracle that the valley would become a 'valley of slaughter.'</p>",
    "9": "<p><span class='term'>ûnāḇîʾ laYHWH hāyāh šām ûšᵉmô ʿōḏēḏ</span> — 'a prophet of YHWH was there named Oded' (28:9). The narrator's formula introduces one of the most unusual prophetic figures in Chronicles: a northern (Israelite) prophet who intercedes on behalf of southern (Judahite) captives against his own king and army. The <span class='term'>hayyāh šām</span> (was there) is a simple presence-marker, but its function is theologically weighty: YHWH's word operated across the political north-south divide. The speech form in vv. 9-11 uses standard prophetic announcement language but directed at the northern army — your brothers, the wrath of YHWH is upon you. The rarity of a cross-kingdom prophetic intervention in the historical books makes this passage exceptional.</p>",
    "15": "<p><span class='term'>wayyilbᵉšûm wayyinᵉʿilûm... wayyaʾᵃkîlûm... wayyašqûm... wayyisᵉkûm... wayyarkîbûm... wayyᵉḇîʾûm liyrîḥôh</span> — the action chain of 28:15. The named men execute a sequence of seven compassion-acts toward captured Judahites: clothed-them, sandaled-them (wayyinᵉʿilûm — put sandals on them), fed-them, gave-them-drink, anointed-them (wayyisᵉkûm — anointed with oil, the medical act), carried-on-donkeys the faint, and brought-them to Jericho. The <span class='term'>kol-ḥᵃlûšêhem</span> (all their feeble ones) identifies the needy category. The specificity of seven acts and the destination (<span class='term'>liyrîḥôh</span>, Jericho) form the closest narrative analogue in the OT to the Good Samaritan parable — the unexpected party acting as comprehensive care-giver to the enemy's vulnerable. The wayyiqtol chain communicates efficient, thorough execution of compassion against all expectation.</p>",
    "22": "<p><span class='term'>wayyōsep lim'ōl baYHWH</span> — 'he added to his trespass against YHWH' (28:22). The idiom <span class='term'>yāsap + mā'al</span> (to add/compound + trespass/unfaithfulness) is the Chronicler's formula for cumulative covenant-breaking. The noun <span class='term'>mā'al</span> denotes breach of covenant fidelity — it appears in the Achan story (Josh 7), the priestly trespass laws (Lev 5:15), and as the Chronicler's terminal diagnostic for fallen kings (2 Chr 36:14). The phrase 'this was that king Ahaz' (<span class='term'>hûʾ hammelek ʾāḥāz</span>) functions as an epitaphic marker — a summary verdict that compounds the damning record. The Chronicler's theology of accumulation: unfaithfulness does not plateau; it deepens.</p>"
  }
}

def main():
    c = load_comm('mkt-original', '2chronicles')
    merge_comm(c, DATA)
    save_comm('mkt-original', '2chronicles', c)
    count = sum(len(v) for v in DATA.values())
    print(f'2chronicles mkt-original: wrote {count} verses across ch 25-28')

if __name__ == '__main__':
    main()
