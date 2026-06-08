"""
MKT Original Commentary — Isaiah 46 (13 verses)
Run: python3 scripts/zc-original-isaiah-46.py
Key decisions:
- vv1-2: Bel (H1078) = Marduk / Nebo (H5015) = Nabu — Babylon's chief gods
  ironically depicted as being loaded like cargo onto fleeing baggage animals;
  maśśaʾ (H4853) = 'burden/load' plays on the double sense of 'oracle' vs. dead
  weight — the MKT renders 'burdens on exhausted beasts'
- vv3-4: triple nāśaʾ / sābal / nāśaʾ (carry) + divine ʾānî hûʾ (I am he,
  H589+H1931): the contrast is load-bearing: idols are carried by animals, YHWH
  carries Israel — ʾānî hûʾ is the Deutero-Isaiah self-identification formula
  underlying John's egō eimi sayings
- v5: mi-ʾadammeh (H1819, 'compare/liken') — the incomparability challenge;
  same root as Adam/human-likeness; MKT adds 'make me equal' to capture the
  stepped parallelism (compare / equate / liken)
- v10: qēts (H7093, 'end') from rēʾšît (H7225, 'beginning') — the structural
  axis of the verse; ʿētsah (H6098, 'counsel/plan') stands as YHWH's deliberate
  purpose, not mere foreknowledge; MKT 'my plan shall stand' captures this
- v11: ʿayit (H5861, 'bird of prey/eagle') from the east = Cyrus; MKT renders
  'man of my purpose' for ʾîš ʿētsatî, preserving both person and divine intent
- v13: tsĕdāqāh (H6666) in Deutero-Isaiah carries salvation/vindication force,
  not merely moral righteousness; tĕšûʿāh (H8668) = salvation; placed in Zion
"""
import json, pathlib

ROOT = pathlib.Path(__file__).parent.parent


def load_comm(layer, book):
    p = ROOT / "data" / "commentary" / layer / f"{book}.json"
    return json.loads(p.read_text()) if p.exists() else {}


def save_comm(layer, book, data):
    p = ROOT / "data" / "commentary" / layer / f"{book}.json"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=2))


def merge_comm(existing, new_data):
    # INTENT: Write only absent keys so re-running is safe after manual edits.
    # CHANGE? If isaiah.json schema changes, update merge_comm and ISAIAH dict below.
    # VERIFY: python3 -c "import json; d=json.load(open('data/commentary/mkt-original/
    #   isaiah.json')); print('Isa 46 v4:',d.get('46',{}).get('4','MISSING')[:80])"
    for ch, verses in new_data.items():
        existing.setdefault(ch, {})
        for v, text in verses.items():
            existing[ch].setdefault(v, text)


ISAIAH = {
    "46": {
        "1": "<p><strong>Bel</strong> (<em>Bēl</em>, H1078) is the Babylonian title of Marduk, chief deity of Babylon; <strong>Nebo</strong> (<em>Nĕbô</em>, H5015) is Nabu, god of scribal wisdom and son of Marduk — both among the most prominent gods of the empire. The verb <strong>kāraʿ</strong> (H3766, \"bows down\") paired with <strong>qāras</strong> (\"stoops\") ironically applies postures of worship to the gods themselves: they are the ones doing the bowing, not receiving it. <strong>Maśśāʾ</strong> (H4853) means both \"burden/load\" and, in prophetic literature, a weighty oracle — the pun stings: the idol-oracle is nothing but dead weight. The MKT renders \"burdens on exhausted beasts\" to capture the physical futility of transporting gods who cannot save themselves.</p>",
        "2": "<p>The verb <strong>qāras</strong> (\"stoops\") continues the mocking bowing posture. The crucial phrase is that the idols \"cannot save (<em>mālaṭ</em>, H4422) the load\" — the same verb YHWH uses for saving his people (v4: \"I will carry you and <em>save</em> you\"). <strong>Captivity</strong> (<em>šĕbî</em>, H7628) is the humiliating destination of both gods and their worshipers — the empire that exiled Israel will itself be exiled, carrying its helpless gods on carts. The MKT \"they themselves go into captivity\" captures the reversal: the gods cannot prevent their own exile, much less their worshipers'.</p>",
        "3": "<p>YHWH addresses \"the house of Jacob and all the remnant of the house of Israel\" — the two-fold address (<em>bêt Yaʿaqōb</em> and <em>šĕʾērît bêt Yiśrāʾēl</em>) encompasses both the northern and southern traditions, calling the whole covenant people to hear. The participle <strong>hăʿămusîm</strong> (\"carried\" or \"borne as a burden,\" from <em>ʿāmas</em>, H6006) answers the burden-language of v1: unlike Bel and Nebo who are burdens on their carriers, Israel is carried by YHWH. The phrase \"since before birth, borne since the womb\" (<em>min-beṭen</em>, H990) traces the carrying back to Israel's origins — election and sustenance are co-extensive with existence itself.</p>",
        "4": "<p>The theological center of the chapter. <strong>ʾĂnî hûʾ</strong> (\"I am he,\" H589 + H1931) is Deutero-Isaiah's signature divine self-identification formula, appearing at key moments throughout Isaiah 40–55 (41:4; 43:10, 13, 25; 48:12). This formula underlies the Greek <em>egō eimi</em> — the \"I am\" of John's Gospel echoes precisely this self-identifying divine speech. The verse strings four first-person verbs: <strong>ʿāśîtî</strong> (\"I have made/created\"), <strong>ʾeśśāʾ</strong> (\"I will carry/bear\"), <strong>ʾeśbol</strong> (\"I will sustain/carry as a burden\"), <strong>ʾămalēṭ</strong> (\"I will deliver/save\"). The verbs span creation, ongoing sustenance, and final salvation — YHWH carries his people from womb to gray hair, from origin to end. The MKT \"I have made you, and I will sustain you; I will carry you and save you\" preserves this four-verb sequence.</p>",
        "5": "<p><strong>Mî-ʾĕdammeh-lî</strong> (\"to whom will you compare me?\") opens the incomparability challenge. The root <em>dāmāh</em> (H1819, \"to liken/compare\") appears three times in different conjugations — compare, equate, liken — a rhetorical tripling that exhausts the vocabulary of comparison. Notably, the same root underlies <em>dĕmût</em> (\"likeness\") in Genesis 1:26 and the making of an image after a likeness in v5-7. The irony: the idol-makers try to make something \"like\" God, but no comparison is possible — YHWH's uniqueness cannot be reduced to a <em>dĕmût</em>. The MKT adds \"and make me equal\" to render the step-parallelism of the three comparison terms.</p>",
        "6": "<p>The idol-making sequence: <strong>yāzûbû zāhāb</strong> (\"they pour out gold\") uses the verb for pouring molten metal; <strong>yišqĕlû</strong> (\"they weigh\") emphasizes the commercial transaction — the idol is a purchase, not a gift. <strong>Tsôrēp</strong> (H6884, \"goldsmith/refiner\") is a craftsman who transforms raw metal, but what is produced is <strong>ʾēl</strong> (\"god\") — the same word used for YHWH himself in v9 (<em>ʾānî ʾēl</em>, \"I am God\"). The irony compounds: the goldsmiths produce an <em>ʾēl</em> that must be carried (v7), while the true <em>ʾēl</em> carries them (v4). The MKT \"makes it into a god\" leaves <em>ʾēl</em> lowercase to mark the irony without being heavy-handed.</p>",
        "7": "<p>The helpless idol's lifecycle: it is <strong>hoisted</strong> (<em>yiśśāʾuhû</em>, from <em>nāśāʾ</em>, the same verb YHWH uses for carrying Israel), <strong>carried</strong>, <strong>set in place</strong> (<em>yannîḥuhû</em>), and then it simply <strong>stands</strong> (<em>yaʿămōd</em>) — motionless. The key phrase is <strong>mimĕqômô lōʾ yāmîš</strong> (\"it cannot move from its place\") — the idol is geographically fixed, utterly incapable of the dynamic presence YHWH exercises everywhere. The final line: it cannot <strong>answer</strong> (<em>yaʿaneh</em>) nor <strong>save</strong> (<em>yôšîaʿ</em>) — the two defining divine activities of prayer-and-response and deliverance are both beyond the idol's reach. \"Rescues no one from trouble\" (MKT) renders <em>lōʾ yôšîaʿ</em> with practical specificity.</p>",
        "8": "<p>The imperative <strong>zizkĕrû-zōʾt</strong> (\"remember this\") shifts the address from idol-critique to covenant demand. <strong>Hitʾōšāšû</strong> (H376 + root, \"stand firm\" or \"take it to heart\") is unusual — some read it as \"act like men,\" others as \"strengthen yourselves.\" The word <strong>pōšĕʿîm</strong> (H6586, \"rebels/transgressors\") identifies the audience not as innocent exiles but as those with a history of covenant defection — the call to remember is also a call to repent. The MKT \"bring it to mind, you rebels\" captures the confrontational tone without softening the identity the prophet assigns.</p>",
        "9": "<p>The double declaration: <strong>ʾānî ʾēl wĕʾên ʿôd</strong> (\"I am God [<em>ʾEl</em>], and there is no other\") followed by <strong>ʾānî ʾĕlōhîm wĕʾên kāmônî</strong> (\"I am God [<em>Elohim</em>], and there is none like me\"). The shift from <em>ʾēl</em> (the generic singular) to <em>ʾĕlōhîm</em> (the majestic plural) is deliberate — both divine names are claimed absolutely. <strong>ʾEpes</strong> (H657, \"none other/nothing else\") is stronger than the more common <em>lōʾ</em> — it means \"end, cessation, there is nothing remaining beyond this.\" This verse is the theological summit of the chapter: all comparison has failed (v5), all idols are helpless (vv6-7), and now comes the unqualified divine claim of sole deity.</p>",
        "10": "<p>The signature of YHWH's uniqueness: <strong>maggid mērēʾšît ʾaḥărît</strong> (\"declaring from the beginning the end\") — note that <em>rēʾšît</em> (H7225, \"beginning\") and <em>ʾaḥărît</em> (H319, \"end/latter things\") frame all of history. This is not mere prediction but sovereign declaration: the same God who was at the beginning determines what the end will be. <strong>ʿĒṣāh</strong> (H6098, \"counsel/plan/purpose\") is the deliberate, reasoned intent of YHWH — not reactive to events but shaping them. The verb <strong>tāqûm</strong> (H6965, \"will stand/rise\") paired with <strong>ʾeʿĕśeh</strong> (\"I will do/carry out\") asserts that the divine plan is both stable (standing) and active (being executed). MKT \"my plan shall stand\" chooses the stability sense of <em>qûm</em>.</p>",
        "11": "<p><strong>ʿĂyiṭ</strong> (H5861, \"bird of prey/eagle\") from the east is the Cyrus figure — the same raptor image used in 41:2 where YHWH \"stirs up one from the east.\" The word <em>ʿayiṭ</em> connotes a swooping predator, fitting for the military campaigns Cyrus conducted across the ancient Near East. <strong>ʾÎš ʿĕṣātî</strong> (\"man of my counsel/purpose\") identifies Cyrus not by name here (as in 44:28; 45:1) but by divine designation — he is a person (<em>ʾîš</em>) instrumentalized by YHWH's plan (<em>ʿēṣāh</em>). The final couplet — <strong>dibbartî ʾap-ʾăbîʾennāh</strong> (\"I have spoken, and I will bring it to pass\") and <strong>yātsartî ʾap-ʾeʿĕśennāh</strong> (\"I have planned, and I will do it\") — closes with the word-act unity that defines YHWH's sovereignty: speaking and doing are never separated in his governance of history.</p>",
        "12": "<p><strong>ʾAbbirê-lēb</strong> (H47 + H3820, literally \"mighty-hearted\" or \"strong-of-heart\") is translated variously as \"stubborn of heart\" (MKT), \"stout-hearted,\" or \"hard-hearted.\" The same root (<em>ʾabbîr</em>) can describe the noble bull or the mighty warrior — here it is ironized: those who think their strength of heart places them beyond need of God. <strong>Hārĕḥôqîm mitsĕdāqāh</strong> (\"far from righteousness\") uses <em>tsĕdāqāh</em> in its Deutero-Isaianic sense of saving-righteousness or vindication, not merely moral conduct — they are far from the salvation that YHWH is about to bring near (v13).</p>",
        "13": "<p>The chapter's resolution: <strong>tsĕdāqāh</strong> (H6666) here means not \"moral righteousness\" but divine <em>vindication/salvation</em> — the act by which YHWH demonstrates his righteous character by rescuing his people. In Deutero-Isaiah, <em>tsĕdāqāh</em> and <em>tĕšûʿāh</em> (H8668, \"salvation\") function as near-synonyms (cf. 51:6, 8; 56:1; 62:1). The verb <strong>nātattî</strong> (H5414, \"I will give/place\") takes Zion as the location of salvation's installation — it is not merely promised but will be <em>placed</em> there like a foundation stone. The final phrase <strong>lĕYiśrāʾēl tiпʾartî</strong> (\"for Israel my glory\") concludes the chapter with covenant identity: the salvation of Israel is itself the manifestation of YHWH's glory. The MKT \"for Israel my glory\" keeps the possessive, marking the glory as his own character displayed in Israel's redemption.</p>"
    }
}


def main():
    existing = load_comm("mkt-original", "isaiah")
    before = sum(len(v) for v in existing.values())
    merge_comm(existing, ISAIAH)
    after = sum(len(v) for v in existing.values())
    save_comm("mkt-original", "isaiah", existing)
    print(f"{len(existing)} chapters, {after} verse entries total (+{after - before} new)")
    for v, kw in [("4", "I am he"), ("9", "none like me"), ("10", "beginning"), ("13", "vindication")]:
        entry = existing.get("46", {}).get(v, "MISSING")
        print(f"  Isa 46:{v} — {'OK' if kw.lower() in entry.lower() else 'CHECK'}")


if __name__ == "__main__":
    main()
