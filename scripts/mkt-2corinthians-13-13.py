"""
MKT 2 Corinthians chapter 13 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-2corinthians-13-13.py

Translation decisions:
- G26 (ἀγάπη): "love" (L/M/T) — covenantal, willed love; appears in vv.11, 14 in distinct
  contexts: v11 "the God of love" (divine attribute), v14 "the love of God" (Trinitarian
  benediction). No variation; ἀγάπη kept as "love" throughout.
- G4102 (πίστις): "faith" (L/M/T) — v5 "whether you are in the faith" = living within the
  sphere of Christian faith/faithfulness; "in the faith" retained as a phrase unit.
- G4151 (πνεῦμα): "Spirit" capitalised (L/M/T) — v14 explicitly "Holy Spirit" (G40 + G4151),
  so theological context is unambiguous; Spirit capitalised.
- G96 (ἀδόκιμος): "unapproved / fail the test" (L: unapproved; M/T: fail the test) —
  cognate with G1381 (δοκιμάζω, examine/test/prove); the wordplay "test yourselves / we are
  not unapproved" is preserved. L keeps "unapproved" for literalness; M/T use the "fail the
  test" idiom to surface the irony.
- G2675 (καταρτίζω/κατάρτισις): "restore / restoration" (L/M) / "full restoration and
  maturity" (T v9), "be restored" (L/M v11) — KJV "be perfect" misses the Hellenistic sense
  of setting broken things right (a surgeon mending a joint, a fisherman mending a net);
  "restoration / be restored" conveys the Greek better.
- G5463 (χαίρετε) in v11: double sense — "rejoice" and "farewell/goodbye." In this closing
  benediction context, translated "farewell" in M/T to preserve the epistolary register; L
  keeps "rejoice" because that is the lexical primary.
- G2842 (κοινωνία): "fellowship" (L/M) / "communion" (T v14) — the Trinitarian benediction
  benefits from "communion" in T to surface the depth of shared life.
- G2962 (κύριος): "Lord" (all tiers) — standard NT convention; no divine-name controversy here.
- G1849 (ἐξουσία): "authority" (L/M/T) — v10 Paul says the Lord gave him ἐξουσία; "authority"
  is precise and carries the delegated-power nuance.
- Deut 19:15 citation in v1: set in quotation marks (L/M/T) as it is an explicit OT citation.
- v14 postscript in interlinear (scribal subscription about epistle written from Philippi via
  Titus and Lucas): this is not part of the canonical text; not translated in any tier.
- Aspect notes: v2 "sinned" (G4258 προαμαρτάνω) = perfect: prior, completed sin with ongoing
  status — rendered "who have been sinning" (M) to capture the perfect aspect. v4 "was crucified"
  (G4717 aorist) = single completed act; "lives" (G2198 present) = ongoing reality.
"""

import json, pathlib

ROOT  = pathlib.Path(__file__).parent.parent
DRAFT = ROOT / 'data' / 'translation' / 'draft'

def load(tier, book):
    p = DRAFT / tier / f'{book}.json'
    if p.exists():
        return json.loads(p.read_text())
    return {}

def save(tier, book, data):
    p = DRAFT / tier / f'{book}.json'
    p.write_text(json.dumps(data, ensure_ascii=False, indent=None))
    print(f'  wrote {p.relative_to(ROOT)}')

def merge_tier(existing, new_data, tier_key):
    for ch, verses in new_data.items():
        if ch not in existing:
            existing[ch] = {}
        for v, tiers in verses.items():
            existing[ch][v] = tiers[tier_key]

CORINTHIANS2 = {
  "13": {
    "1": {
      "L": "This is the third time I am coming to you. 'By the mouth of two or three witnesses every word shall be established.'",
      "M": "This is the third time I am coming to you. 'Every charge must be established by the testimony of two or three witnesses.'",
      "T": "I am coming to you for the third time. And Scripture's standard applies here: no accusation stands unless it is confirmed by two or three witnesses."
    },
    "2": {
      "L": "I warned before and I warn now in advance—as when I was present the second time, and now though absent—to those who have sinned before and to all the rest: that if I come again I will not spare.",
      "M": "I gave a warning when I was with you the second time; I am giving it again now while absent—to those who have been sinning and to all the rest: if I come again, I will not spare anyone.",
      "T": "When I was there the second time I gave a clear warning. I am giving it again now, from a distance—to those who have been living in sin and to everyone else: if I come back, I will not hold back."
    },
    "3": {
      "L": "since you seek proof that Christ is speaking in me—who toward you is not weak but is powerful among you.",
      "M": "Since you are demanding proof that Christ speaks through me. He is not weak in dealing with you but is powerful among you.",
      "T": "You want proof that Christ really speaks through me? Then consider this: Christ does not act weakly toward you—he exercises his full power in your midst."
    },
    "4": {
      "L": "For indeed he was crucified out of weakness, yet he lives by the power of God; for we also are weak in him, yet toward you we will live with him by the power of God.",
      "M": "He was crucified in weakness, yet he lives by the power of God. We too are weak in him, but in our dealing with you we will live with him by the power of God.",
      "T": "He was crucified as an act of weakness—but he now lives through the sheer power of God. We share in that weakness, yes; but when we must deal with you, we will be fully alive with him in the power of God."
    },
    "5": {
      "L": "Examine yourselves, whether you are in the faith; test yourselves. Or do you not know your own selves, that Jesus Christ is in you?—unless indeed you are unapproved.",
      "M": "Examine yourselves, to see whether you are in the faith. Test yourselves. Do you not realize that Jesus Christ is in you?—unless indeed you fail the test.",
      "T": "Stop putting me to the test and examine yourselves instead. Are you actually living in the faith? Put yourselves to the test. Surely you know that Jesus Christ lives in you—unless you have already disqualified yourselves."
    },
    "6": {
      "L": "But I hope you will know that we are not unapproved.",
      "M": "I hope you will discover that we have not failed the test.",
      "T": "And I am confident that when you examine us honestly, you will see we have not been disqualified."
    },
    "7": {
      "L": "Now we pray to God that you do no evil—not that we may appear approved, but that you may do what is good, even if we appear unapproved.",
      "M": "We pray to God that you will do nothing wrong—not to show we have passed the test, but so that you will do what is right, even if we appear to have failed.",
      "T": "Our prayer to God is simply that you do nothing wrong—not so that we get credit for passing some test, but because we genuinely want you to do what is right. Even if that makes us look like failures, so be it."
    },
    "8": {
      "L": "For we are not able to do anything against the truth, but only for the truth.",
      "M": "For we cannot work against the truth; we can only work for it.",
      "T": "We have no capacity to act in opposition to the truth—only in its service."
    },
    "9": {
      "L": "For we rejoice when we are weak and you are strong; this also we pray for: your restoration.",
      "M": "We are glad whenever we are weak and you are strong; and this we pray for: your complete restoration.",
      "T": "We are entirely content to be weak if it means you are strong. In fact, that is exactly what we pray for—your full restoration and maturity in Christ."
    },
    "10": {
      "L": "Because of this I write these things while absent, so that when present I need not act with sharpness, according to the authority which the Lord gave me for building up and not for tearing down.",
      "M": "This is why I write these things while I am away—so that when I arrive I will not need to be harsh in my use of the authority the Lord gave me for building up, not for tearing down.",
      "T": "That is why I am writing all this now, before I get there. When I arrive, I want to use the authority the Lord gave me gently—for building people up, not for knocking them down."
    },
    "11": {
      "L": "Finally, brothers, rejoice; be restored, be encouraged, be of one mind, live in peace; and the God of love and peace will be with you.",
      "M": "Finally, brothers and sisters, farewell. Aim for restoration, encourage one another, be of one mind, live in peace. And the God of love and peace will be with you.",
      "T": "One last word, dear brothers and sisters: keep growing toward wholeness. Encourage each other. Be of one heart and mind. Live at peace. And the God who is love, the God who gives peace, will be with you."
    },
    "12": {
      "L": "Greet one another with a holy kiss.",
      "M": "Greet one another with a holy kiss.",
      "T": "Greet each other with a holy kiss—the outward sign of the life you share together."
    },
    "13": {
      "L": "All the saints greet you.",
      "M": "All God's people here send their greetings.",
      "T": "Every member of God's family here adds their greeting to mine."
    },
    "14": {
      "L": "The grace of the Lord Jesus Christ and the love of God and the fellowship of the Holy Spirit be with you all.",
      "M": "May the grace of the Lord Jesus Christ, the love of God, and the fellowship of the Holy Spirit be with you all.",
      "T": "The grace that flows from the Lord Jesus Christ, the love that is the very nature of God, and the deep communion that the Holy Spirit creates—may all of this be with every one of you."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, '2corinthians')
        merge_tier(existing, CORINTHIANS2, tier_key)
        save(tier_dir, '2corinthians', existing)
    print('2 Corinthians 13 written.')

if __name__ == '__main__':
    main()
