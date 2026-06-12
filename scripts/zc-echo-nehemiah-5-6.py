"""
Echo Layer — Nehemiah chapters 5–6
Run: python3 scripts/zc-echo-nehemiah-5-6.py

Key echo connections in this range:
- 5:5: Debt slavery of brothers — "we are the same flesh" → Heb 2:14; Lev 25:39-41
- 5:8: Nehemiah redeems exiled brothers sold to foreigners → Gal 3:13; Lev 25:47-55
- 5:10-11: Stop interest, restore pledged fields → Lev 25:35-37; Luke 6:34-35
- 5:13: Robe-shaking judgment sign → Matt 10:14; Acts 18:6
- 5:14-15: Servant-governor refusing the food allowance → Matt 20:28; Phil 2:7
- 5:19: "Remember me for good" — appeal to divine memory → Heb 7:25
- 6:3: "I am doing a great work and cannot come down" → Acts 20:24; Phil 3:13-14
- 6:9: "Now strengthen my hands" — prayer under intimidation → Isa 35:3; Heb 12:12
- 6:10-12: False prophet hired to make Nehemiah sin → Jer 23:21; 2 Pet 2:1-3
- 6:15: Wall completed in 52 days → Zech 4:6 (by the Spirit, not by might)
- 6:16: Nations see and recognize God's work → Ps 118:23; Isa 60:5
"""

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
    """Merge echo entries; deduplicate by (type, target) within each verse."""
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

NEH_ECHO_5_6 = {
  "5": {
    "5": [
      {"type": "allusion", "target": "Heb 2:14", "note": "&#8220;We are the same flesh as our brothers (<em>kᵉḇaśar ʾaḥênû bᵉśārānû</em>)&#8221; — the covenantal appeal to shared humanity: our children are like their children, so selling them into slavery violates the bond of brother-flesh; Hebrews uses the same logic in the opposite direction: &#8220;since the children share in flesh and blood, he too partook of the same things, so that through death he might destroy the one who has the power of death&#8221; (Heb 2:14); the incarnation is the ultimate sharing of flesh with brothers that liberates from the deepest bondage"},
      {"type": "allusion", "target": "Lev 25:39", "note": "&#8220;We are having to reduce our sons and daughters to slavery&#8221; — the crisis Leviticus 25 was designed to prevent: &#8220;if your brother becomes poor beside you and sells himself to you, you shall not make him serve as a slave&#8221; (Lev 25:39); the Jubilee legislation exists precisely to prevent the internal debt-slavery that Nehemiah&#8217;s community has allowed; the Torah&#8217;s provisions have been violated by the very people who returned to restore the covenant order"}
    ],
    "8": [
      {"type": "allusion", "target": "Lev 25:47", "note": "&#8220;We have done everything we could to buy back (<em>qānînû</em>) our Jewish brothers who were sold to foreign nations — and now you are selling your own brothers back into that same bondage!&#8221; — the buying-back of enslaved brothers is the enacted form of Leviticus 25&#8217;s redemption laws (Lev 25:47-55): a kinsman-redeemer (<em>gōʾēl</em>) was obligated to redeem a poor brother sold to a foreigner; Nehemiah has personally acted as gōʾēl while the nobles are creating the very situation that requires redemption"},
      {"type": "allusion", "target": "Gal 3:13", "note": "The pattern of redemption from bondage to foreign nations — &#8220;we bought back our brothers who were sold to the nations&#8221; — is the structural form of Galatians 3:13: &#8220;Christ redeemed us from the curse of the law by becoming a curse for us&#8221;; Nehemiah&#8217;s redemption is economic and temporary; Christ&#8217;s is spiritual and permanent — but both operate through the same logic: one who is free uses his own resources to purchase the freedom of those in bondage"}
    ],
    "10": [
      {"type": "allusion", "target": "Lev 25:36", "note": "&#8220;Let us stop charging interest (<em>nešeḵ</em>) altogether&#8221; — Nehemiah&#8217;s reform implements Leviticus 25:36: &#8220;take no interest (<em>nešeḵ</em>) or profit from him, but fear your God&#8221;; the same Hebrew term (<em>nešeḵ</em>, usury/bite) is used in both — the charging of interest on loans to covenant brothers is a direct violation of the Torah&#8217;s vision of the covenant community as an interest-free solidarity, in which the fear of God rather than profit governs economic relations"},
      {"type": "allusion", "target": "Luke 6:34", "note": "The interest-free lending reform of Nehemiah 5 (backed by covenantal solidarity) anticipates Jesus&#8217; instruction: &#8220;lend, expecting nothing in return, and your reward will be great&#8221; (Luke 6:34-35); Jesus radicalizes Nehemiah&#8217;s reform from &#8220;no interest from brothers&#8221; to &#8220;no expectation of return from anyone&#8221;; the economic ethic of the kingdom community is grounded in the character of God who is &#8220;kind to the ungrateful and the evil&#8221; (Luke 6:35)"}
    ],
    "11": [
      {"type": "allusion", "target": "Lev 25:28", "note": "&#8220;Restore to them today their fields, vineyards, olive groves, and houses&#8221; — the restoration of pledged ancestral land is the Jubilee provision of Leviticus 25:28: &#8220;it shall remain in the hand of the buyer until the year of jubilee. In the jubilee it shall be released, and he shall return to his property&#8221;; Nehemiah accelerates what the Jubilee legislates — the return of land to its covenant owners — making the fifth-year of his governorship a voluntary jubilee; Luke 4:18 presents Jesus&#8217; ministry as the year of the LORD&#8217;s favor in which all such debts are cancelled"}
    ],
    "13": [
      {"type": "allusion", "target": "Acts 18:6", "note": "Nehemiah shakes out the fold of his robe and declares: &#8220;May God shake out every man like this from his house and from his labor who does not keep this promise&#8221; — the robe-shaking is a prophetic embodied sign-act, where the physical action enacts the judgment it announces; the same sign recurs in Acts 18:6 where Paul &#8220;shook out his garments and said, &#8216;Your blood be on your own heads! I am innocent&#8217;&#8221; — and in Jesus&#8217; instruction to shake the dust off feet at rejection (Matt 10:14; Luke 9:5), the judgment-sign of the refused covenant carried in the body"},
      {"type": "allusion", "target": "Matt 10:14", "note": "The robe-shaking of Nehemiah 5:13 is the OT antecedent to Jesus&#8217; instruction in Matt 10:14: &#8220;if anyone will not receive you or listen to your words, shake off the dust from your feet when you leave&#8221;; both are embodied prophetic declarations: the sign-act transfers the judgment to those who refuse the covenant summons and removes it from the messenger; the whole assembly&#8217;s &#8220;Amen&#8221; and praise of YHWH confirms the prophetic character of the act"}
    ],
    "14": [
      {"type": "allusion", "target": "Matt 20:28", "note": "&#8220;Neither I nor my brothers drew on the governor&#8217;s food allowance&#8221; — Nehemiah explicitly renounces the rights and privileges of his gubernatorial office out of consideration for the people&#8217;s burden; this is the OT model of servant leadership that Jesus articulates in Matt 20:28: &#8220;the Son of Man came not to be served but to serve, and to give his life as a ransom for many&#8221;; both Nehemiah and Jesus have legitimate authority they set aside for the sake of those under them"},
      {"type": "allusion", "target": "2 Cor 11:7", "note": "Nehemiah&#8217;s self-funded governance — feeding 150 Jewish officials at his own expense while refusing the governor&#8217;s allotment &#8220;because the burden on these people was already too great&#8221; (v.18) — is the direct OT parallel to Paul&#8217;s self-funding apostleship: &#8220;Did I commit a sin in humbling myself so that you might be exalted, because I preached God&#8217;s gospel to you free of charge?&#8221; (2 Cor 11:7); both are deliberate economic expressions of servant authority"}
    ],
    "19": [
      {"type": "allusion", "target": "Heb 7:25", "note": "&#8220;Remember me with favor, O my God, for everything I have done for this people&#8221; — Nehemiah&#8217;s &#8220;remember me&#8221; appeals (five times in the memoir: 5:19; 13:14, 22, 29, 31) are appeals to God&#8217;s memory as the record of covenant faithfulness; they represent the highest OT intercessory posture — yet they are backward-looking, reciting accomplished deeds; Hebrews 7:25 presents Christ&#8217;s intercession as categorically different: &#8220;he always lives to make intercession for them&#8221; — present and perpetual, not retrospective; Nehemiah prays that God will remember his works; Christ intercedes as the living mediator whose death is his perpetual plea"}
    ]
  },
  "6": {
    "3": [
      {"type": "allusion", "target": "Acts 20:24", "note": "&#8220;I am engaged in an important work and cannot come down (<em>lōʾ ʾûḵal lāreḏeṯ</em>). Why should the work stop while I leave it to come to you?&#8221; — Nehemiah&#8217;s refusal to be distracted from the wall-building is the OT model of mission-focus under pressure; Paul&#8217;s farewell speech to the Ephesians uses the same language: &#8220;I do not account my life of any value nor as precious to myself, if only I may finish my course and the ministry that I received from the Lord Jesus&#8221; (Acts 20:24); both Nehemiah and Paul refuse to &#8220;come down&#8221; from their God-given work"},
      {"type": "allusion", "target": "Phil 3:13", "note": "Nehemiah&#8217;s refusal to leave the work — repeated four times against the same pressure (v.4: &#8220;Four times they sent the same kind of message, and each time I gave them the same answer&#8221;) — is the practical form of Paul&#8217;s theological declaration: &#8220;forgetting what lies behind and straining forward to what lies ahead, I press on toward the goal&#8221; (Phil 3:13-14); both texts describe the single-minded focus that mission demands against the persistent distraction strategy of the enemy"}
    ],
    "9": [
      {"type": "allusion", "target": "Isa 35:3", "note": "&#8220;They were all trying to frighten us (<em>lᵉyarʾēnû</em>), thinking our hands would go limp (<em>yirpû yᵉḏêhem</em>) and the work would stop. So I prayed: Now, O God, give me strength (&#8216;strengthen my hands&#8217;)&#8221; — the limp-hands motif echoes Isaiah&#8217;s consolation to the exiles: &#8220;strengthen the weak hands, and make firm the feeble knees&#8221; (Isa 35:3); both texts describe the community that has nearly lost its capacity for action and receives divine strengthening to continue; Hebrews 12:12 applies the Isaiah passage to the Christian community under trial"},
      {"type": "allusion", "target": "Heb 12:12", "note": "Nehemiah&#8217;s prayer against the limpness-of-hands strategy — &#8220;strengthen my hands&#8221; against those trying to make the builders&#8217; hands go slack — is cited in Heb 12:12 which applies Isa 35:3 to the Christian under discipline: &#8220;lift your drooping hands and strengthen your weak knees&#8221;; the pattern runs Isa 35 → Neh 6:9 → Heb 12:12: the same physical-spiritual image of arms weakened by pressure and restored by divine action describes the exile&#8217;s, the builder&#8217;s, and the Christian&#8217;s experience"}
    ],
    "10": [
      {"type": "allusion", "target": "Jer 23:21", "note": "Shemaiah prophesies that Nehemiah should hide in the temple to escape assassination — but Nehemiah discerns: &#8220;God had not sent him — he had given this prophecy against me because Tobiah and Sanballat had paid him&#8221; (v.12); Jeremiah&#8217;s warning against false prophets covers exactly this category: &#8220;I did not send the prophets, yet they ran; I did not speak to them, yet they prophesied&#8221; (Jer 23:21); the false prophet who speaks without divine commission but with human motivation is the recurring threat across both testaments"},
      {"type": "allusion", "target": "2 Pet 2:1", "note": "The hired prophet Shemaiah — paid by Nehemiah&#8217;s enemies to deliver a false prophecy that would both terrify him and lead him into sin — is the OT pattern for 2 Peter&#8217;s warning: &#8220;there will be false prophets among you, who will secretly bring in destructive heresies... and in their greed they will exploit you with false words&#8221; (2 Pet 2:1-3); the mechanism is the same: the false prophet&#8217;s theological language is real, but the motivation is financial and the purpose is to compromise the leader and damage the community"}
    ],
    "14": [
      {"type": "allusion", "target": "2 Tim 4:14", "note": "&#8220;My God, remember what Tobiah and Sanballat have done — and also the prophetess Noadiah and the other prophets who were trying to intimidate me&#8221; — Nehemiah&#8217;s imprecatory prayer committing the case to God&#8217;s memory mirrors Paul&#8217;s final letter: &#8220;Alexander the coppersmith did me great harm; the Lord will repay him according to his deeds&#8221; (2 Tim 4:14); both are the covenant community&#8217;s response to specific opponents: not personal vengeance but handing the record to God, trusting divine justice"}
    ],
    "15": [
      {"type": "allusion", "target": "Zech 4:6", "note": "The wall of Jerusalem completed in 52 days — a feat the enemies had intended to prevent through opposition, false counsel, hired prophets, and intimidation — is the practical fulfillment of Zechariah&#8217;s oracle to Zerubbabel: &#8220;Not by might, nor by power, but by my Spirit, says the LORD of hosts&#8221; (Zech 4:6); Zechariah was prophesying to the temple-rebuilding community in Jerusalem at the same generation (520 BCE); the wall-completion is the later chapter of the same divine enablement that the prophet had declared; supernatural speed in an impossible task is the Spirit&#8217;s signature"}
    ],
    "16": [
      {"type": "allusion", "target": "Ps 118:23", "note": "&#8220;Their confidence collapsed, for they recognized that this work had been accomplished with the help of our God&#8221; — when the wall was complete in 52 days, the surrounding nations underwent exactly the response Psalm 118 anticipates: &#8220;This is the LORD&#8217;s doing; it is marvelous in our eyes&#8221; (Ps 118:23); the nations&#8217; recognition of divine action in the completion of the wall is the OT pattern for Matt 21:42 where Jesus applies Ps 118:22-23 to his own rejection and vindication: what looks impossible to human observers is recognized retrospectively as YHWH&#8217;s work"},
      {"type": "allusion", "target": "Isa 60:5", "note": "The nations&#8217; recognition of God&#8217;s work in the wall&#8217;s completion — &#8220;they recognized that this work had been accomplished with the help of our God&#8221; — begins to fulfill Isaiah 60&#8217;s vision of the nations seeing and acknowledging the glory of YHWH upon Israel: &#8220;then you shall see and be radiant; your heart shall thrill and exult, because the abundance of the sea shall be turned to you&#8221; (Isa 60:5); the restoration of Jerusalem&#8217;s walls is a partial and provisional fulfillment of Isaiah&#8217;s eschatological vision; Rev 21:24-26 describes the ultimate completion of this trajectory"}
    ]
  }
}

def main():
    existing = load_echo('nehemiah')
    merge_echo(existing, NEH_ECHO_5_6)
    save_echo('nehemiah', existing)
    print('Nehemiah 5-6 echo layer written.')

if __name__ == '__main__':
    main()
