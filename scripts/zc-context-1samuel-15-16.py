"""
MKT Context Commentary — 1 Samuel chapters 15–16
Run: python3 scripts/zc-context-1samuel-15-16.py

Ch15: Saul's Amalek campaign — herem (the ban/devotion); the theology of holy war;
      Samuel's oracle of rejection; the divine 'regret' (naham);
      prophetic authority over royal authority
Ch16: David's anointing at Bethlehem — anointing ritual in ANE; election of the
      youngest; YHWH's seeing vs. human seeing; the Spirit's transition from
      Saul to David

ANE/historical context:
- herem warfare paralleled in the Mesha Stele (ca. 830 BCE): Chemosh commands
  herem against Israelite cities — exact same institution on the other side
- Samuel's authority to reject a king establishes the prophet-over-king pattern
  that defines the entire monarchy (Nathan/David, Elijah/Ahab, Isaiah/Hezekiah)
- Bethlehem of Judah: the Ephrathite clan town (Ruth 1:2; Mic 5:2)
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

CONTEXT = {
  "15": {
    "3": "<p>The <em>ḥērem</em> (ban/devotion to destruction) commanded against Amalek is the most theologically contested institution in the OT and has generated extensive scholarly discussion. <em>Ḥērem</em> designates the total consecration of persons, livestock, and property to YHWH — which in practice meant their destruction, since they could not be used for ordinary purposes once devoted. The institution appears in the Mosaic law (Deut 7:2; 20:16-18), in Joshua's campaigns (Josh 6:17-21; 8:26), and here. The closest ANE parallel is the Mesha Stele (the Moabite Stone, ca. 830 BCE), in which King Mesha of Moab records that the god Chemosh commanded him to destroy the Israelite city of Nebo, putting all its inhabitants under <em>ḥrm</em> (the Moabite cognate of Hebrew <em>ḥērem</em>). This suggests <em>ḥērem</em> was a recognizable ANE category of sacred warfare in which the deity, not the king, is credited as the war's instigator and the spoils belong entirely to the deity. The theological problem — YHWH commanding the destruction of an entire people — has been addressed variously: as historical particularity (addressed to a specific people at a specific time), as the text's realistic portrayal of ancient warfare ideology being subjected to prophetic critique (Saul's failure is precisely his selective application), and eschatologically (as a type of the final divine judgment).</p>",
    "11": "<p>YHWH's 'regret' (<em>wāʾinnāḥem</em>) over making Saul king is a key theological text on divine repentance: <em>niḥamtî kî himlaktî ʾet šāʾûl lᵉmelek</em> — 'I regret that I have made Saul king.' The verb <em>nāḥam</em> in the <em>niphal</em> means to be sorry, to relent, to change direction — it is the same verb used in Gen 6:6 ('YHWH regretted that he had made man') and in Jonah 3:10 ('God relented of the disaster'). The theological tension is explicit in 15:29: Samuel says 'the Glory of Israel will not lie or relent (<em>yinnāḥēm</em>), for he is not a man, that he should relent (<em>lᵉhinnāḥēm</em>)' — yet YHWH relented in v11. The tension is not resolved by harmonization but represents the OT's honest portrayal of divine pathos: YHWH is genuinely affected by human choices while remaining sovereignly consistent in his covenant purposes. This is the background for the NT's theology of divine impassibility-in-engagement.</p>",
    "22": "<p>Samuel's oracle — 'to obey is better than sacrifice' — is the most concentrated statement of prophetic theology over against cultic theology in the pre-exilic period. The prophet-over-cult principle first appears explicitly here, though it is implicit in the Eli narrative. The pattern Samuel establishes — the prophet as the one who speaks YHWH's word in judgment over the king and the cult — defines the entire subsequent prophetic tradition: Nathan confronts David (2 Sam 12), Elijah confronts Ahab (1 Kgs 18-21), Isaiah confronts Ahaz (Isa 7), Jeremiah confronts Zedekiah (Jer 38). The prophetic word takes priority over royal and priestly acts. In ANE context, this is remarkable: in Mesopotamian tradition, the king was often the representative of the deity in both military and cultic matters, and prophets served the court. Israel's prophetic institution developed a distinctively adversarial relationship to the monarchy that has no close parallel in other ANE literature.</p>",
    "35": "<p>Samuel's grief over Saul and YHWH's grief over Saul run in parallel: <em>ûšᵉmûʾēl lōʾ yāsap lirʾôt ʾet šāʾûl ʿad yôm mōtô kî ʾitabbēl šᵉmûʾēl ʾel šāʾûl</em> — 'Samuel did not see Saul again until the day of his death, for Samuel was grieving over Saul.' The grief of the prophet for the rejected king is theologically significant: Samuel does not celebrate Saul's rejection but mourns it. The same grief marks YHWH in v11 — divine rejection is not divine indifference. The narrative portrays the cost of covenant unfaithfulness not as cold divine machinery but as divine and prophetic pathos. This motif of divine grief over the rejected runs through the OT into the NT: Jesus weeps over Jerusalem (Luke 19:41), knowing the destruction his people's rejection will bring.</p>"
  },
  "16": {
    "1": "<p>Samuel is sent to Bethlehem (<em>bêt lāḥem</em>, 'house of bread') to anoint one of Jesse's sons. Bethlehem was an Ephrathite clan town in the hill country of Judah — the same town identified as the birthplace of David in Ruth 1:1-2, and later as the birthplace of the Messiah in Mic 5:2. Archaeological surveys of the Bethlehem area have confirmed it as an occupied site throughout the Bronze and Iron Ages, though no major excavation has been undertaken beneath the modern town. Its identity as the 'city of David' is confirmed by Luke 2:4 and is consistent with the broader geographical picture of the Judahite hill country settlements. The Ephrathite designation (cf. 1 Sam 17:12: Jesse the Ephrathite) marks the family's connection to the ancient Judahite clan of Ephrath (cf. Gen 35:19; Ruth 4:11).</p>",
    "7": "<p>YHWH's statement to Samuel — <em>lōʾ yirʾeh hāʾāḏām ʾăšer yirʾeh ʾelōhîm kî hāʾāḏām yirʾeh lāʿênayim waYHWH yirʾeh lallēḇāḇ</em> — 'man does not see as God sees; man looks at the outward appearance (<em>ʿênayim</em>, eyes) and YHWH looks at the heart (<em>lēḇāḇ</em>)' — is the anointing narrative's theological thesis. The reversal of human evaluation is the consistent OT pattern: the last becomes first, the youngest becomes king, the shepherd becomes the anointed. In ANE coronation ideology, the king was typically the tallest, the most impressive, the most militarily dominant — the very description of Saul (1 Sam 9:2). David's election inverts this: he is the youngest, absent, tending the sheep. The election of the unlikely is not merely God's preference but the structural demonstration that the king rules by divine choice rather than human qualification — which is what distinguishes Israelite from Mesopotamian royal ideology.</p>",
    "13": "<p>The anointing ritual: Samuel takes the horn of oil (<em>qeren haššemen</em>) and anoints David in the midst of his brothers. The anointing with oil is attested in ANE coronation ceremonies from Egypt (where Pharaoh anointed vassal kings), to Ugarit, to the Hittite court. In Israel, the anointing functioned differently: it was a priestly-prophetic act that designated YHWH's chosen rather than a royal display of power. The immediate consequence — 'the Spirit of YHWH rushed upon David from that day forward' (<em>ṣālaḥ rûaḥ YHWH ʾel dāwiḏ mēhayyôm hahûʾ wāmāʿlāh</em>) — makes explicit the connection between the anointing and Spirit-empowerment. Three elements converge: the oil (material symbol), the prophetic word (Samuel's act is authoritative because Samuel is YHWH's prophet), and the Spirit (the effective power). The same three-element pattern appears at Jesus's baptism: water (the material), the divine voice (the word of authorization), and the Spirit (the effective anointing). Luke 4:18 cites Isa 61:1 — 'The Spirit of the Lord is upon me, because he has anointed me' — as Jesus's self-identification as the ultimate anointed one whose Spirit-empowerment is permanent rather than occasional.</p>",
    "14": "<p>The departure of the Spirit from Saul is one of the most theologically challenging verses in the Samuel narrative: <em>wərûaḥ YHWH sārāh mēʿim šāʾûl ûbiʿăṯāṯû rûaḥ rāʿāh mēʾēt YHWH</em> — 'the Spirit of YHWH departed from Saul, and a harmful spirit from YHWH tormented him.' The phrase <em>rûaḥ rāʿāh mēʾēt YHWH</em> (a harmful spirit from YHWH) raises questions about divine agency in distressing states. OT theology consistently subordinates all spiritual powers — including malevolent ones — to YHWH's sovereign will (cf. Job 1-2, where the adversary operates only within divinely permitted limits). The harmful spirit here is understood as YHWH's withdrawal of the Spirit's protective presence, leaving Saul vulnerable to spiritual distress. David's harp music (<em>kinnôr</em>) as the remedy introduces the therapeutic-liturgical dimension: music as the vehicle of spiritual relief anticipates the Psalms' role in Israel's spiritual formation. The image of the Spirit departing from Saul and resting permanently on David is the visual narrative of the covenant transition.</p>"
  }
}

def main():
    c = load_comm('mkt-context', '1samuel')
    merge_comm(c, CONTEXT)
    save_comm('mkt-context', '1samuel', c)
    count = sum(len(v) for v in CONTEXT.values())
    print(f'1samuel mkt-context: wrote {count} verses across ch 15-16')

if __name__ == '__main__':
    main()
