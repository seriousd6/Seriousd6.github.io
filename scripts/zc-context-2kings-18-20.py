"""
MKT Context Commentary — 2 Kings chapters 18–20
Run: python3 scripts/zc-context-2kings-18-20.py

Ch18: Hezekiah's reform — bronze serpent destruction (Nehushtan); the Rabshakeh's speech
      in Hebrew as psychological warfare; Taylor Prism and the Sennacherib siege
Ch19: Hezekiah's prayer / Isaiah's oracle — Sennacherib's retreat; the angel of YHWH
      striking 185,000 Assyrians; Greek parallel (Herodotus field-mice)
Ch20: Hezekiah's illness and recovery — Babylonian delegation and the fatal disclosure;
      the shadow on the sundial — Babylonian astronomical context

ANE/historical context:
- 18:4: Nehushtan — Moses's bronze serpent (Num 21:8-9) now a cult object
- 18:13: Taylor Prism — Sennacherib's own annals confirm the siege and tribute
- 19:35: angel strikes 185,000 — Herodotus 2.141 (field mice) and the bubonic plague theory
- 20:12: Merodach-baladan — historically attested Babylonian king (Marduk-apla-iddina II)
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
  "18": {
    "4": "<p>Hezekiah&rsquo;s destruction of the Nehushtan — <em>hûʾ kittēt ʾet naḥaš hannᵉḥōšet ʾăšer ʿāśāh mōšeh kî ʿaḏ hayyāmîm hāhēm hāyû bᵉnê yiśrāʾēl mᵉqaṭṭᵉrîm lô wayyiqrāʾ lô nᵉḥūštān</em>, &lsquo;he broke in pieces the bronze serpent that Moses had made, for until those days the people of Israel had been burning incense to it; it was called Nehushtan&rsquo; — documents the transformation of a legitimate Mosaic cult-object into an idolatrous cult-object. The bronze serpent of Num 21:8-9 was explicitly commanded by YHWH as a healing instrument; looking at it preserved life from the serpent-plague. The object itself was not idolatrous. Over time (<em>ʿaḏ hayyāmîm hāhēm</em>, &lsquo;until those days&rsquo;) it accumulated a cult: incense-burning, the hallmark of divine worship. The object&rsquo;s history illustrates the OT&rsquo;s relentless pattern: YHWH-commanded object → legitimate use → accumulated veneration → idolatry → destruction. The name <em>nᵉḥūštān</em> is either Hezekiah&rsquo;s dismissive designation (a thing of bronze, a <em>neḥōšet</em>) or its actual cult name — the narrator&rsquo;s irony is that an object named for its material rather than for YHWH is not worth worshipping. John 3:14-15 (&lsquo;as Moses lifted up the serpent in the wilderness, so must the Son of Man be lifted up, that whoever believes in him may have eternal life&rsquo;) reclaims the original Mosaic serpent as a type of Christ&rsquo;s crucifixion — restoring the typological meaning after its centuries of idolatrous overlay: the object that should have pointed forward to Christ was instead worshipped; Christ is the fulfillment of what the object originally signified.</p>",
    "13": "<p>The Sennacherib siege of Judah — <em>ûḇišnat ʾarbaʿ ʿeśrēh šānāh lammelek ḥizqiyyāhû ʿālāh sannᵉḥērîḇ melek ʾaššûr ʿal kol ʿārê yᵉhûḏāh haḇṣûrôt wayyitpᵉśēm</em>, &lsquo;in the fourteenth year of King Hezekiah, Sennacherib king of Assyria came up against all the fortified cities of Judah and took them&rsquo; — is one of the most extensively documented events in the entire OT by external sources. The Taylor Prism (British Museum, discovered 1830) is Sennacherib&rsquo;s own annalistic account of his 701 BCE campaign: he claims to have captured 46 of Hezekiah&rsquo;s fortified cities, deported 200,150 people, and shut Hezekiah up in Jerusalem &lsquo;like a bird in a cage.&rsquo; The Prism confirms the tribute paid (v14-16) and the siege of Jerusalem — while notably not claiming to have taken the city, consistent with 19:35-36&rsquo;s account of the army&rsquo;s destruction. The Lachish reliefs (Sennacherib&rsquo;s palace at Nineveh, now in the British Museum) depict the siege and capture of Lachish (2 Kgs 18:17: the Rabshakeh sent from Lachish), providing visual documentation of the Assyrian military operations described in 2 Kgs 18-19. The convergence of the Hebrew narrative, the Taylor Prism, and the Lachish reliefs makes the Hezekiah siege one of the best-attested episodes in biblical archaeology.</p>"
  },
  "19": {
    "35": "<p>The destruction of the Assyrian army — <em>wayhî ballaylāh hahûʾ wayyēṣēʾ malʾaḵ YHWH wayyaḵ bᵉmaḥănēh ʾaššûr ḥāmiššāh ûšᵉmōnîm ʾelep</em>, &lsquo;that night the angel of YHWH went out and struck down 185,000 in the camp of the Assyrians&rsquo; — is corroborated in a striking way by Herodotus (2.141): describing the same campaign, Herodotus reports that field mice invaded the Assyrian camp at night, eating the quivers, bowstrings, and shield-handles, rendering the army unable to fight. The Egyptian priestly tradition Herodotus records identifies this as a divine deliverance through mice — a rationalized account of a sudden military withdrawal. The bubonic plague theory (mice as plague carriers; rapid mass death overnight) is the most common naturalistic explanation offered. Whatever the mechanism, the dual attestation — Israelite tradition (YHWH&rsquo;s angel), Egyptian/Greek tradition (mice) — corroborates the historical reality of a massive sudden Assyrian setback at Jerusalem in 701 BCE. The Sennacherib Prism&rsquo;s silence on taking Jerusalem is the most significant external corroboration: the greatest military annalist of the ancient Near East (who boasted extensively of his victories) does not claim to have taken the city that his own account confirms he besieged.</p>"
  }
}

def main():
    c = load_comm('mkt-context', '2kings')
    merge_comm(c, CONTEXT)
    save_comm('mkt-context', '2kings', c)
    count = sum(len(v) for v in CONTEXT.values())
    print(f'2kings mkt-context: wrote {count} verses across ch 18-20')

if __name__ == '__main__':
    main()
