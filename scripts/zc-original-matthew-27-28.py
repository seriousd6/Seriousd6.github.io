"""
MKT Original — Matthew chapters 21–28
Output: data/commentary/mkt-original/matthew.json (adds ch21-28)
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
  "21": {
    "42": '<p><strong>lithon hon apedokimasan hoi oikodomountes houtos egeneto eis kephalen gonias</strong> — the stone which the builders rejected, this one became the head of the corner — <em>apedokimasan</em> (rejected after examination, found to be unfit) is the technical term for the stone-mason\'s rejection of a stone after inspection. <em>Kephalen gonias</em> (head of the corner) denotes either the capstone (keystone completing an arch) or the cornerstone (the principal foundation stone that sets the line of the building). Both readings apply Christologically: the rejected Jesus becomes the load-bearing stone of the new community. The citation is Ps 118:22-23 LXX.</p>'
  },
  "22": {
    "37": '<p><strong>agapeseis kyrion ton theon sou en hole te kardia sou kai en hole te psyche sou kai en hole te dianoia sou</strong> — you shall love the Lord your God with all your heart and all your soul and all your mind — the Shema (Deut 6:5 LXX) adds <em>dianoia</em> (mind, understanding) to the MT\'s heart-soul-strength, creating a triad that covers the affective, volitional, and cognitive dimensions of the whole person. The totality-markers (<em>holos</em> = whole, in all three cases) indicate that the love commanded is total — leaving no part of the person divided or uncommitted.</p>',
    "44": '<p><strong>eipen kyrios to kyrio mou</strong> — the LORD said to my Lord — the LXX renders Ps 110:1\'s <em>YHWH ladon</em> (YHWH to my Adonai); Jesus\'s argument turns on David calling his own descendant Lord (<em>kyrios</em>), which would be unseemly if the son were merely human. The Davidic messianic expectation assumed the son-of-David would be David\'s inferior; Jesus uses Ps 110:1 to demonstrate that the Messiah is simultaneously son and superior — a paradox that points to the divine sonship.</p>'
  },
  "23": {
    "23": '<p><strong>apodekatoun to heduosmon kai to anethon kai to kyminon kai aphekate ta baryteta tou nomou</strong> — you tithe mint and dill and cumin and neglect the weightier matters of the law — <em>baryteta</em> (weighty things, the heavy end of a scale) is the metaphor: some laws have greater weight than others. The three weighty matters named are <em>krisis</em> (justice/judgment), <em>eleos</em> (steadfast covenant-love/mercy), and <em>pistis</em> (faithfulness); these are the OT prophetic priorities (Mic 6:8, Hos 6:6) that the scribal tradition had flattened by treating every regulation equally.</p>'
  },
  "24": {
    "30": '<p><strong>kai tote phanesetai to semeion tou huiou tou anthropou en ourano</strong> — and then the sign of the Son of Man will appear in heaven — the sign (<em>semeion</em>) is disputed: whether the cross appearing in the sky, or the Son of Man himself as the sign, or the Shekinah-cloud. The citation of Dan 7:13 that follows (<em>erchomenon epi ton nephelos tou ouranou</em>) suggests the sign is the appearing of the Son of Man himself in the divine glory-cloud. <strong>kopsontai pasai hai phylai tes ges</strong> — all the tribes of the earth will mourn — citing Zech 12:10 (the mourning that follows seeing the one they pierced); grief and recognition converge at the parousia.</p>'
  },
  "25": {
    "40": '<p><strong>eph hoson epoiesate heni touton ton adelphon mou ton elachiston emoi epoiesate</strong> — inasmuch as you did it to one of the least of these my brothers, you did it to me — the identification of Jesus with the least (<em>elachistos</em>, the lowest-ranked, the most inconsequential) is the theological core of the passage. The phrasing <em>eph hoson</em> (to the degree that, inasmuch as) makes the identification proportional and complete: every act of mercy to the suffering is simultaneously an act toward Jesus himself. This is not metaphor but an ontological claim about Christ\'s solidarity with human suffering.</p>'
  },
  "26": {
    "28": '<p><strong>touto gar estin to haima mou tes diathēkēs to peri pollon ekchynnomenon eis aphesin hamartion</strong> — for this is my blood of the covenant which is poured out for many for the forgiveness of sins — the phrase draws together four OT streams: (1) covenant-blood of Sinai (<em>haima tes diathēkēs</em>, Exod 24:8); (2) Servant for many (<em>peri pollon</em>, Isa 53:12); (3) Jeremianic new covenant (Jer 31:31-34); (4) Zechariah\'s blood-of-the-covenant (<em>bedam beritecha</em>, Zech 9:11). The cup-word is a compressed Christological commentary on the whole OT sacrificial and covenantal tradition.</p>'
  },
  "27": {
    "46": '<p><strong>eli eli lema sabachthani</strong> — My God, my God, why have you forsaken me — the Aramaic form (Matthew uses transliterated Aramaic, Mark has Aramaic too; both differ slightly from each other and from the LXX) reproduces the opening of Ps 22:1. The question <em>hina ti</em> (why, for what purpose) is not a denial of God\'s sovereignty but a genuine cry from within the experience of abandonment. Jesus prays the whole Psalm, which ends in vindication (Ps 22:24-31); the cry of dereliction is the beginning of the Passion Psalm, not its whole message. The darkness and the cry together communicate the full weight of bearing divine wrath on behalf of others.</p>'
  },
  "28": {
    "18": '<p><strong>edothe moi pasa exousia en ourano kai epi ges</strong> — to me has been given all authority in heaven and on earth — <em>edothe</em> (has been given, divine passive) grounds the authority in the Father\'s gift, not in Christ\'s inherent right alone (though the divine sonship implies it); the crucified one now speaks as the enthroned one. The scope is total (<em>pasa exousia</em> = all authority) and universal (<em>en ourano kai epi ges</em> = in heaven and on earth) — the Danielic authority of the Son of Man (Dan 7:14) now historically enacted in the post-resurrection commission.</p>',
    "20": '<p><strong>idou ego meth hymon eimi pasas tas hemeras heos tes synteleias tou aionos</strong> — behold I am with you all the days until the completion of the age — <em>idou</em> (behold, a call to attention) introduces the climactic promise. <em>Ego eimi</em> (I am) is the divine-presence formula; <em>pasas tas hemeras</em> (all the days = every single day, not merely always in general) stresses the daily-accompanying reality. The frame of the Gospel (Immanuel = God with us, 1:23; I am with you always, 28:20) is the Matthean inclusio: the Gospel\'s subject is the presence of God incarnate, permanently dwelling with his people to the end of the age.</p>'
  }
}

def main():
    existing = load_comm('mkt-original', 'matthew')
    merge_comm(existing, DATA)
    save_comm('mkt-original', 'matthew', existing)
    total = sum(len(v) for v in existing.values())
    print(f'Matthew mkt-original: {len(existing)} chapters, {total} verses written.')

if __name__ == '__main__':
    main()
