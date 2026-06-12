"""
MKT Original Commentary — 1 Chronicles chapters 19–22
Run: python3 scripts/zc-original-1chronicles-19-22.py

Ch21: sāṭān in Chronicles vs. YHWH in 2 Sam 24:1 — the theological shift in causation
      Ornan's threshing floor / Mount Moriah — the convergence of sacrifice sites
Ch22: Solomon (šᵉlōmōh) / šālôm etymology and the Davidic covenant sonship language
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
  "21": {
    "1": "<p>The census narrative&rsquo;s opening differs in one critical word from its Samuel parallel: where 2 Sam 24:1 reads <em>wayyōsep ʾap YHWH laḥărōt bᵉyiśrāʾēl wayyāset ʾet dāwîḏ bāhem</em>, &lsquo;again the anger of YHWH was kindled against Israel, and he incited David against them,&rsquo; the Chronicler writes <em>wayyaʿamod śāṭān ʿal yiśrāʾēl wayyāset ʾet dāwîḏ limpōr ʾet yiśrāʾēl</em>, &lsquo;and Satan stood up against Israel and incited David to number Israel.&rsquo; The Chronicles version substitutes <em>śāṭān</em> for the divine agency of Samuel. The word <em>śāṭān</em> appears here without the definite article (unlike Job 1-2 and Zech 3:1-2 where it is <em>haśśāṭān</em>, &lsquo;the adversary&rsquo;) — some read it as a proper name, others as the noun &lsquo;an adversary.&rsquo; The substitution reflects a theological development in the post-exilic period: the distinction between divine sovereignty (YHWH ultimately permits) and proximate agency (a hostile adversarial being incites) that the book of Job articulates and that becomes more developed in 2nd Temple Judaism. The Chronicler does not contradict Samuel: YHWH remains sovereign (the plague is YHWH&rsquo;s judgment; the staying of the plague is YHWH&rsquo;s mercy, 21:15). The Chronicler disaggregates the causation that Samuel telescopes. The trajectory from haśśāṭān in Zechariah (3:1-2, contemporary with the Chronicler&rsquo;s era) to the NT&rsquo;s <em>diabolos</em> and <em>satanas</em> passes through this terminological shift.</p>",
    "22": "<p>David&rsquo;s request to purchase the threshing floor of Ornan the Jebusite — <em>tᵉnāh lî mᵉqôm haggōren</em>, &lsquo;give me the place of the threshing floor&rsquo; — establishes the site that 2 Chr 3:1 will identify as Mount Moriah: <em>wayyāḥel šᵉlōmōh liḇnôt ʾet bêt YHWH bîrûšālaim bᵉhar hammōriyyāh</em>, &lsquo;Solomon began to build the house of YHWH in Jerusalem on Mount Moriah.&rsquo; The Chronicler makes explicit what the Samuel account leaves implicit: the threshing floor purchased under plague-judgment is the same mountain as the Moriah of Gen 22:2, where YHWH commanded Abraham, <em>lᵉḵ lᵉḵā ʾel ʾereṣ hammōriyyāh wᵉhaʿălēhû šām lᵉʿōlāh</em>, &lsquo;go to the land of Moriah, and offer him there as a burnt offering.&rsquo; The convergence is theologically loaded: the site where YHWH stayed Abraham&rsquo;s knife and provided the substitute sacrifice (Gen 22:13-14), and where YHWH&rsquo;s destroying angel was stayed (1 Chr 21:15-16), becomes the site of the permanent temple where sacrifice is offered in perpetuity. The ram caught in the thicket (Gen 22), the plague-stayed angel over the threshing floor (1 Chr 21), and the daily burnt offerings on the temple altar (2 Chr 2:4) form a single sacrificial sequence. The name YHWH-yireh (&lsquo;YHWH will provide&rsquo;, Gen 22:14) is the theology of the site — a provision that the NT reads as anticipating the ultimate sacrifice (John 1:29; Heb 10:5-10).</p>"
  },
  "22": {
    "9": "<p>YHWH&rsquo;s announcement of Solomon&rsquo;s name to David — <em>hinnēh bēn nôlāḏ lāḵ hûʾ yihyeh ʾîš mᵉnûḥāh wᵉhaniḥôtî lô miqqōl ʾōyᵉḇāyw missāḇîḇ kî šᵉlōmōh yihyeh šᵉmô wᵉšālôm wāšeqeṭ ʾettēn ʿal yiśrāʾēl bᵉyāmāyw</em>, &lsquo;Behold, a son shall be born to you who shall be a man of rest. I will give him rest from all his surrounding enemies. For his name shall be Solomon (<em>šᵉlōmōh</em>), and I will give peace (<em>šālôm</em>) and quiet to Israel in his days&rsquo; — makes the name-etymology explicit: Solomon is the peace-king. The name <em>šᵉlōmōh</em> derives from the root <em>šālem</em>/<em>šālôm</em> (wholeness, completeness, peace). The Chronicler&rsquo;s emphasis on <em>šālôm</em> and <em>mᵉnûḥāh</em> (rest, repose) as Solomon&rsquo;s defining gifts frames the temple-building as the culmination of Israel&rsquo;s progress toward rest — from the wilderness wandering (no rest, no temple) through the conquest (partial rest, no temple) through David&rsquo;s wars (not yet rest) to Solomon&rsquo;s reign (rest, temple). Heb 4:9-10 invokes the same framework for the eschatological rest: <em>ara apoleipetai sabbatismos tō laō tou theou; ho gar eiselthōn eis tēn katapausin autou kai autos katepausen apo tōn ergōn autou</em> — &lsquo;so then, there remains a Sabbath rest for the people of God, for whoever has entered God&rsquo;s rest has also rested from his works.&rsquo; Solomon&rsquo;s <em>šālôm</em>-reign is the historical type of the eschatological rest; Jesus, son of David (Matt 1:1) and &lsquo;greater than Solomon&rsquo; (Matt 12:42), is its fulfillment.</p>"
  }
}

def main():
    c = load_comm('mkt-original', '1chronicles')
    merge_comm(c, ORIGINAL)
    save_comm('mkt-original', '1chronicles', c)
    count = sum(len(v) for v in ORIGINAL.values())
    print(f'1chronicles mkt-original: wrote {count} verses across ch 19-22')

if __name__ == '__main__':
    main()
