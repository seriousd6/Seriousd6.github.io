"""
MKT Christ Commentary — Isaiah chapter 58
Run: python3 scripts/zc-christ-isaiah-58.py

Source data used:
- data/interlinear/isaiah.json
- data/translation/draft/mediating/isaiah.json

Key decisions in this range:
- v. 6: loose bonds, free the oppressed — direct: Luke 4:18; Heb 2:14-15
- v. 7: share bread with hungry — shadow: Matt 25:35-40; John 6:35
- v. 8: light breaking like dawn — shadow: John 8:12; Luke 1:78-79
- v. 11: spring whose waters do not fail — shadow: John 4:14; 7:38
- v. 12: repairer of the breach — shadow: Eph 2:14-15
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
    # INTENT: Non-destructive merge — existing entries are never overwritten, safe to re-run
    for ch, verses in new_data.items():
        if ch not in existing: existing[ch] = {}
        for v, html in verses.items():
            if v not in existing[ch]: existing[ch][v] = html

ISAIAH = {
"58": {
"1": "<p>A revelation of God: cry aloud, spare not; lift up your voice like a trumpet; declare to my people their transgression — yet they seek YHWH daily and delight to know his ways, as if they were a nation that did righteousness. The exposure of religious performance that masks ethical failure is the consistent concern of the prophets. Jesus applies the same critique to his contemporaries: Matthew 15:8 (<em>this people honors me with their lips, but their heart is far from me</em>); Matthew 23:23 (you tithe mint and dill and cumin but have neglected the weightier matters of the law: justice and mercy and faithfulness). The God who sees through form to substance is the God who reveals his Son as the one who does the substance perfectly.</p>",
"2": "<p>A revelation of God: they ask of YHWH righteous judgments and delight to draw near to God — yet without the righteousness the delight-claims presuppose. The disconnect between expressed delight in God and actual righteousness is the hypocrite's signature. Christ exposes it directly: Matthew 7:21-23 (<em>not everyone who says to me 'Lord, Lord' will enter the kingdom of heaven, but the one who does the will of my Father</em>). The one who does the Father's will in full, and calls others to do the same, is the antidote to the formal religion of Isaiah 58:2.</p>",
"3": "<p>A revelation of God: <em>why have we fasted, and you see it not?</em> — because on your fast day you seek your own pleasure and oppress all your workers. The fasting that accompanies exploitation is not fasting before YHWH. James 2:14-17 applies the same principle: faith without works is dead — the one who says <em>go in peace, be warmed and filled</em> while doing nothing for the needy has not met the requirement. Christ's critique of the Pharisees' ostentatious fasting (Matt 6:16-18) targets the same self-displaying devotion that Isaiah 58:3 exposes.</p>",
"4": "<p>A revelation of God: your fasting leads to quarreling and strife, even to striking with a wicked fist — fasting like this is not heard on high. The performance of religious discipline that fuels rather than restrains conflict is a contradiction in terms. Paul frames the NT version: Galatians 5:14-15 (the whole law is fulfilled in <em>love your neighbor as yourself</em> — but if you bite and devour one another...). The Spirit produces peace, not quarreling — the fruit of genuine encounter with God (Gal 5:22-23) is what fasting is meant to cultivate.</p>",
"5": "<p>A revelation of God: is this the fast I choose — a day for a man to humble himself, to bow his head like a reed and to spread sackcloth and ashes? Is this what you call a fast? The external gestures without internal and ethical reality are the target. Christ does not abolish fasting but reframes it entirely: Matthew 6:17-18 (when you fast, anoint your head and wash your face, that your fasting may not be seen by others but by your Father who is in secret). The fast that YHWH chooses is defined in vv. 6-7; the fast Christ exemplifies is his entire self-giving life (cf. Phil 2:7: he emptied himself).</p>",
"6": "<p>A direct typological connection. <em>Hălō' zeh ṣôm 'eb̠ĕḥārēhû pittēaḥ ḥarsinnôt reša' hattēr 'aguddôt môṭāh wĕšallaḥ rĕṣûṣîm ḥop̄šîm wĕk̠ol-môṭāh tĕnatēqû</em> — is this not the fast I choose: to loose the bonds of wickedness, to undo the straps of the yoke, to let the oppressed go free, and to break every yoke? Luke 4:18-19 quotes the related passage of Isaiah 61:1-2 as Jesus' programmatic announcement: <em>he has sent me to proclaim liberty to the captives and recovering of sight to the blind, to set at liberty those who are oppressed</em>. Hebrews 2:14-15 frames Christ's death as the liberation of all who were enslaved through fear of death. The fast YHWH chooses is the shape of Christ's entire mission: the undoing of bondage in all its forms.</p>",
"7": "<p>A shadow: is it not to share your bread with the hungry and bring the homeless poor into your house; when you see the naked, to cover him? Matthew 25:35-40 makes this the criterion of judgment: <em>I was hungry and you gave me food, I was a stranger and you welcomed me, I was naked and you clothed me</em> — and identifies Christ with the needy neighbor. James 2:14-17 frames it as the test of living faith. Christ as the bread of life (John 6:35) and the incarnate God who takes in the outcast (Luke 14:21-23: bring in the poor and crippled) is the fulfillment of the true fast at the personal level, which he then extends through his community.</p>",
"8": "<p>A shadow: <em>then shall your light break forth like the dawn, and your healing shall spring up speedily</em> — your righteousness shall go before you; the glory of YHWH shall be your rear guard. The light breaking forth like dawn is the imagery that the NT applies to Christ: Luke 1:78-79 (the sunrise from on high will visit us, to give light to those who sit in darkness); John 8:12 (<em>I am the light of the world</em>); 2 Corinthians 4:6 (the light of the knowledge of God's glory in the face of Jesus Christ). The healing that springs up speedily is the sign of the messianic age: Matthew 11:5 (the blind receive their sight, the lame walk, the lepers are cleansed).</p>",
"9": "<p>A revelation of God: then you shall call and YHWH will answer; you shall cry and he will say, <em>here I am</em> (<em>hinnēnî</em>). The divine <em>hinnēnî</em> — here I am, I am present, I am available — is the summit of covenant relationship. Christ as the one in whom YHWH is permanently present: John 14:9 (<em>whoever has seen me has seen the Father</em>); Matthew 18:20 (<em>where two or three are gathered in my name, there am I among them</em>); John 14:21 (I will manifest myself to him). The God who says <em>hinnēnî</em> in Isaiah 58:9 says it definitively and permanently in the incarnate Son.</p>",
"10": "<p>A shadow: if you pour yourself out for the hungry and satisfy the desire of the afflicted, then your light shall rise in the darkness. The self-pouring (<em>tāp̄ēq</em> — to pour out, empty) for the needy is the shape of agape love. Paul describes Christ's self-giving in the same language: Philippians 2:7 (he emptied himself, taking the form of a servant). 1 John 3:17 applies this to the community: whoever has the world's goods and sees his brother in need yet closes his heart against him — how does God's love abide in him? The community formed by the self-poured Christ practices the self-pouring of Isaiah 58:10.</p>",
"11": "<p>A shadow: YHWH will guide you continually and satisfy your desire in scorched places — you shall be like a watered garden, like a spring whose waters do not fail (<em>wĕk̠ĕmôṣā' mayim 'ăšer lō' yĕk̠azzĕb̠û mêmāyw</em>). The never-failing spring is Christ's promise: John 4:14 (<em>the water that I will give him will become a spring of water welling up to eternal life</em>); John 7:38-39 (<em>rivers of living water will flow from within</em> — which he said about the Spirit). The guidance continually given (the pillar of cloud and fire in Exodus) is now the Spirit of truth who guides into all truth (John 16:13). YHWH's unfailing spring and guide are embodied in Christ and given through the Spirit.</p>",
"12": "<p>A shadow: your ancient ruins shall be rebuilt; you shall be called the repairer of the breach (<em>gōdēr peretz</em>), the restorer of streets to dwell in. Ephesians 2:14-16 describes Christ as the one who has broken down the dividing wall of hostility — making peace, reconciling both to God in one body through the cross. The breach (<em>peretz</em>) between God and humanity is the gap Christ's cross spans; the breach between Jew and Gentile is the wall Christ demolishes. The rebuilding of ancient ruins points to the new creation (Rev 21:5: behold, I am making all things new) in which every ruin is restored and every breach repaired.</p>",
"13": "<p>A revelation of God: if you turn back your foot from the Sabbath and call the Sabbath a delight (<em>'ōneg</em>), the holy day of YHWH honorable — then you shall take delight in YHWH. Christ as Lord of the Sabbath (Mark 2:28) does not abolish the Sabbath principle but fulfills it: Hebrews 4:9-10 (a Sabbath rest remains for the people of God; whoever has entered God's rest has also rested from his works as God did from his). The delight in YHWH that true Sabbath-keeping produces is the participation in the divine rest that Christ opens — the rest of completed work, finished redemption.</p>",
"14": "<p>A revelation of God: then you shall take delight in YHWH, and I will make you ride on the heights of the earth, and feed you with the heritage of Jacob your father — for the mouth of YHWH has spoken. The promised blessing of riding the heights and inheriting the full covenant heritage is the eschatological reward of those who keep covenant faithfully. Revelation 21:7 frames the same promise: the one who conquers will inherit these things. Christ is the one who rides the heights (Rev 19:11-16) and leads those who are his into the same inheritance (1 Pet 1:4; Heb 6:17). The mouth of YHWH has spoken — and that Word took flesh and dwelt among us (John 1:14).</p>"
}
}

def main():
    existing = load_comm('mkt-christ', 'isaiah')
    merge_comm(existing, ISAIAH)
    save_comm('mkt-christ', 'isaiah', existing)
    v = sum(len(vs) for vs in ISAIAH.values())
    print(f'Isaiah 58 mkt-christ: {v} verses written.')

if __name__ == '__main__':
    main()
