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

NEW = {
"31": {
"1": "<p>Woe to those who go down to Egypt for help, relying on horses and chariots — but who do not look to the Holy One of Israel or seek the LORD! The fundamental covenant sin: substituting military-political alliance for YHWH. The Holy One of Israel who they refuse to look to is identified in the NT as Jesus (Mark 1:24; John 6:69). His invitation in Matthew 11:28-30 (<em>Come to me, all who are weary and burdened</em>) is the positive form of Isaiah 31:1's negative: look to me rather than to Egypt's chariots. The NT equivalent is 1 Corinthians 1:24 — Christ as the true power and wisdom that replaces military and intellectual strength.</p>",
"2": "<p>Yet he too is wise and brings disaster — he does not take back his word. YHWH's wisdom stands against and outlasts the wisdom of Egypt's strategists. This is the exact framework Paul develops in 1 Corinthians 1:18-25: <em>the foolishness of God is wiser than human wisdom, and the weakness of God is stronger than human strength.</em> The wisdom that appears as disaster (the cross) is YHWH's word that he does not take back — the eternal plan (Eph 1:11) that proceeds through apparent defeat to certain victory. Against those who plot against YHWH, he rises; his word is irrevocable.</p>",
"3": "<p>The Egyptians are human, not God — their horses are flesh, not spirit. When YHWH stretches out his hand, both the helper and the helped will fall. The flesh/spirit contrast is foundational to NT anthropology: <em>what is born of the flesh is flesh; what is born of the Spirit is spirit</em> (John 3:6). Paul: <em>those who live according to the flesh cannot please God</em> (Rom 8:8). The Egyptian military power Israel trusted is flesh — capable of impressive feats but unable to produce the spiritual new birth that Christ offers. When YHWH stretches out his hand, the flesh-systems collapse; the same hand raised over Egypt at the Exodus is now the hand of the risen Christ who has all authority (Matt 28:18).</p>",
"4": "<p>As a lion growls over its prey and no company of shepherds can deter it — so the LORD of hosts will come down to wage war on Mount Zion. The divine warrior-lion descending on Zion is unstoppable. Revelation 5:5 identifies Jesus as <em>the Lion of the tribe of Judah, the Root of David</em> who has conquered. The lion who cannot be intimidated by the shepherds' noise is the Messiah who moves with absolute sovereign determination toward his purpose — and whose resurrection-victory cannot be undone by any earthly or heavenly opposition. His coming down to wage war on Zion is, paradoxically, the cross: where YHWH executes judgment on sin through his own Son.</p>",
"5": "<p>Like birds hovering over their young — so the LORD of hosts will shield Jerusalem; shielding, he will deliver it; passing over, he will rescue it. The Passover echo (<em>passing over</em>, <em>pasach</em>) in the bird-hovering image is explicit: YHWH passes over Jerusalem as he passed over the doorposts in Egypt. Jesus uses the identical mother-bird image for his own posture toward Jerusalem: <em>how often I have longed to gather your children together as a hen gathers her chicks under her wings, but you were not willing</em> (Matt 23:37; Luke 13:34). The bird who shields her young is YHWH's self-description — and Jesus embodies it as he weeps over the city and then opens his arms on the cross to shield it from the judgment it would not accept.</p>",
"6": "<p>Turn back to him from whom the people of Israel have so deeply defected. The call to return (<em>shuvu</em>) from deep apostasy is the prophetic message Jesus intensifies and centralizes: <em>Repent, for the kingdom of heaven is at hand</em> (Matt 3:2; 4:17; Mark 1:15). The depth of the defection — <em>amaq sarah</em>, profound moral departure — mirrors what Jesus finds in his generation (Matt 23's extended condemnation). The return he calls for is not a minor adjustment but the turning back from deep defection that Isaiah 31:6 names — made possible by the Spirit who enables genuine teshuvah (Acts 5:31; 11:18).</p>",
"7": "<p>In that day every person will throw away the idols of silver and gold their own hands have made — things that have been their sin. The eschatological abandonment of handmade idols is the conversion pattern the NT consistently describes. Paul at Athens: God commands all people everywhere to repent, having overlooked the times of idol-worship (Acts 17:29-30). The Thessalonians <em>turned to God from idols to serve the living and true God</em> (1 Thess 1:9). 1 John 5:21: <em>little children, keep yourselves from idols.</em> The idol-throwing of Isaiah 31:7 is what happens when the Holy One of Israel is finally looked to — the false gods become obviously worthless in his presence.</p>",
"8": "<p>The Assyrian will fall by a sword that is not of any man — no human sword will consume him. The defeat of the great enemy without conventional military action is fulfilled historically in the angel's overnight destruction of 185,000 Assyrians (37:36). The theological principle — victory by the not-of-human-hands sword — governs Christ's method of defeating the powers. Paul: <em>the weapons of our warfare are not of the flesh but have divine power to destroy strongholds</em> (2 Cor 10:4). The weapon is the word of God (Eph 6:17) and the Spirit — the sword that proceeds from the mouth of the returning Christ (Rev 1:16; 19:15) rather than from any human forge.</p>",
"9": "<p>His stronghold will crumble in terror at the signal standard (<em>nes</em>) — declares YHWH, whose fire is in Zion and whose furnace is in Jerusalem. The signal standard raised on the mountain is developed in Isaiah 11:10 as the Root of Jesse lifted as a banner to which the nations rally. Jesus claims this fulfillment in John 12:32: <em>when I am lifted up from the earth, I will draw all people to myself</em> — the cross as the signal standard that causes every stronghold of the enemy to crumble. YHWH's fire in Zion is the Pentecost fire that descended on the disciples gathered in Jerusalem (Acts 2:3) — the same divine fire that Isaiah sees as the presence consuming the enemy is the Spirit-fire that empowers the church.</p>"
}
}

data = load_comm('mkt-christ', 'isaiah')
merge_comm(data, NEW)
save_comm('mkt-christ', 'isaiah', data)
print('Done.')
