"""
MKT Christ Commentary — Isaiah chapter 39
Run: python3 scripts/zc-christ-isaiah-39.py

Isaiah 39 is the structural pivot of the book: Hezekiah shows Babylonian envoys
all the temple treasury, and Isaiah pronounces the coming Babylonian exile as a
consequence. This chapter bridges First Isaiah (chs 1-39, Assyrian crisis) and
Second Isaiah (chs 40-66, Babylonian comfort).

Christological notes:
- The Babylonian envoys bringing gifts → reversed by the Magi who bring gifts
  to the true Davidic king (Matt 2:1-12)
- Hezekiah's proud display vs. Christ's kenosis (Phil 2:6-8)
- The post-deliverance pride that brings future judgment: the pattern of
  transfiguration-then-passion announcement (Matt 17:22-23)
- v.8 (peace in my days): Luke 12:19-20 (the rich fool's "eat, drink, be merry")
- The Babylon prophecy fulfilled in Daniel 1 (the king's children as eunuchs)
  fulfilled ultimately in Christ who transforms the curse into kingdom service
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
    """Merge new_data into existing without overwriting present entries."""
    for ch, verses in new_data.items():
        if ch not in existing:
            existing[ch] = {}
        for v, html in verses.items():
            if v not in existing[ch]:
                existing[ch][v] = html

ISAIAH = {
  "39": {
    "1": '<p>"At that time Merodach-baladan the son of Baladan, king of Babylon, sent envoys with letters and a present to Hezekiah." The Babylonian king sending envoys with gifts to the Davidic king who has been miraculously preserved from death (ch. 38) is structurally parallel to the Magi from the East bringing gifts to the newborn Davidic king (Matt 2:1-12). Both are foreign rulers or representatives acknowledging a Judean king\'s significance. But the Magi story reverses the Hezekiah story\'s outcome: where Hezekiah\'s encounter with Babylonian envoys ends in the announcement of exile, the Magi\'s encounter with the Christ-child fulfills the promise that the nations will come to Israel\'s light (Isa 60:3: "nations shall come to your light"). Christ transforms the Babylonian pivot into the eschatological ingathering.</p>',
    "2": '<p>"And Hezekiah welcomed them gladly and showed them his treasure house, the silver, the gold, the spices, the precious oil, his whole armory, all that was found in his storehouses." The proud display of everything — his whole house, nothing withheld (<em>kol-bêtô</em>) — is the pride that precedes the fall. Phil 2:6-7: "though he was in the form of God, did not count equality with God a thing to be grasped, but emptied himself." Christ who possessed all things withheld them from display; Hezekiah who possessed mortal treasures displayed them to the wrong audience. The contrast between Hezekiah\'s proud showing-everything and Christ\'s self-emptying is the contrast between the failure of the Davidic dynasty and its ultimate fulfillment in the humble king.</p>',
    "3": '<p>"Then Isaiah the prophet came to King Hezekiah, and said to him, \'What did these men say? And from where did they come to you?\' Hezekiah said, \'They have come to me from a far country, from Babylon.\'" The prophetic interrogation about origin — "from where?" — is the question Jesus repeatedly poses in John\'s Gospel about himself and his opponents: "you are from below; I am from above" (John 8:23); "no one has ascended into heaven except he who descended from heaven" (3:13). Origin determines destiny — Hezekiah\'s friendly visitors from Babylon represent the exile he will not personally experience; their origin is the indicator of the coming judgment.</p>',
    "4": '<p>"Then he said, \'What have they seen in your house?\' Hezekiah answered, \'They have seen all that is in my house; there is nothing in my storehouses that I did not show them.\'" Nothing withheld. The comprehensive disclosure to the Babylonian envoys is the opposite of the discernment that the situation demanded. In the NT, Jesus\'s instruction to his disciples is precisely about discernment in what to reveal to whom: "Do not give dogs what is holy, and do not throw your pearls before pigs" (Matt 7:6). The wisdom Christ teaches — knowing when to speak and when to withhold — is what Hezekiah lacks. Hezekiah\'s complete disclosure is his pride made manifest.</p>',
    "5": '<p>"Then Isaiah said to Hezekiah, \'Hear the word of YHWH of hosts.\'" The formal introductory formula for a major oracle. This is the word of judgment that pivots the entire book toward exile — and toward the comfort of chs 40-66. In Heb 4:12-13, the word of God is "living and active, sharper than any two-edged sword... no creature is hidden from his sight, but all are naked and exposed to the eyes of him to whom we must give account." The word that Hezekiah hears after exposing everything is the word of reckoning: everything he showed will go to Babylon. The full disclosure invites the full accounting.</p>',
    "6": '<p>"Behold, the days are coming, when all that is in your house, and that which your fathers have stored up till this day, shall be carried to Babylon. Nothing shall be left, says YHWH." The exile prophecy delivered at the moment of greatest post-deliverance prosperity — the announcement of future loss immediately after miraculous rescue. Matt 17:22-23: Jesus announces his coming death immediately after the Transfiguration ("the Son of Man is about to be delivered into the hands of men, and they will kill him"). The pattern of glory-followed-by-announcement-of-suffering is the prophetic template that the Passion itself fulfills. In both cases, the announcement is not a contradiction of the deliverance but its extension — the full divine plan requires both the rescue and the suffering that follows.</p>',
    "7": '<p>"And some of your own sons, who will come from you, whom you will father, shall be taken away, and they shall be eunuchs in the palace of the king of Babylon." The prophecy is fulfilled in Daniel 1:3-7: Daniel and his three friends are taken from the Judean nobility to serve in the Babylonian court, their names changed, their status as eunuchs implied. The cursed status of the exile — the cutting off of the royal line in Babylon — is redeemed in Isaiah 56:3-5 where YHWH promises eunuchs who keep the covenant "a monument and a name better than sons and daughters." Christ\'s redemption transforms even the Babylonian curse into kingdom service: the eunuch Philip baptizes in Acts 8, and the Ethiopian eunuch carries the gospel back to Africa.</p>',
    "8": '<p>"Then Hezekiah said to Isaiah, \'The word of YHWH that you have spoken is good.\' For he thought, \'There will be peace and security in my days.\'" The chilling conclusion — Hezekiah accepts the judgment about future exile with equanimity because "at least there will be peace in my time." Luke 12:19-20: "\'Soul, you have ample goods laid up for many years; relax, eat, drink, be merry.\' But God said to him, \'Fool!\'" The temporal limitation of concern ("in my days") is exactly the rich fool\'s logic. Jesus\'s entire orientation is toward the eternal and the final reckoning — he will not let the disciples settle for temporary security (Matt 16:26: "what will it profit a man if he gains the whole world and forfeits his soul?"). Isaiah 39:8 is the OT\'s most concentrated instance of the failure of eschatological seriousness, standing as the dark counterpoint to the comfort of chapters 40-66 that Christ embodies and inaugurates.</p>',
  },
}

def main():
    existing = load_comm('mkt-christ', 'isaiah')
    merge_comm(existing, ISAIAH)
    save_comm('mkt-christ', 'isaiah', existing)
    # INTENT: Verify all 8 Isaiah 39 mkt-christ verses present against interlinear
    # CHANGE? If interlinear/isaiah.json ch 39 verse count changes, update expected total
    # VERIFY: Console shows OK with 8 verses; no MISSING output
    il = json.loads((ROOT / 'data' / 'interlinear' / 'isaiah.json').read_text())
    out = json.loads((ROOT / 'data' / 'commentary' / 'mkt-christ' / 'isaiah.json').read_text())
    missing = [v for v in il.get('39', {}) if v not in out.get('39', {})]
    if missing:
        print(f'  MISSING: {missing}')
    else:
        print(f'  OK: all Isaiah 39 mkt-christ verses present ({len(il.get("39", {}))} verses)')

if __name__ == '__main__':
    main()
