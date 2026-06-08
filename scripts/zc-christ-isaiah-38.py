"""
MKT Christ Commentary — Isaiah chapter 38
Run: python3 scripts/zc-christ-isaiah-38.py

Source data used:
- data/interlinear/isaiah.json
- data/translation/draft/mediating/isaiah.json

Key decisions in this range:
- vv. 1-3: death sentence and Hezekiah's prayer — type: Gethsemane (Heb 5:7)
- v. 5: fifteen years added — type: resurrection life granted by YHWH
- v. 8: sundial reversal — revelation of God: Creator-sovereignty over time
- vv. 10-12: descent to Sheol — shadow: Christ's descent to the dead (1 Pet 3:19; Acts 2:27)
- v. 17: sins cast behind YHWH's back — type: Col 2:14 forgiveness through Christ
- v. 18: Sheol cannot praise — resolved by Christ's resurrection (Phil 2:10-11)
- vv. 21-22: fig-cake healing / temple sign — shadow: Christ as healer and true temple
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
"38": {
"1": "<p>A type: Hezekiah becomes mortally ill (<em>ḥālāh lāmût</em>) and Isaiah delivers the death sentence: <em>set your house in order, for you shall die and not recover</em>. The royal figure facing death becomes a type of the Son of God who enters the full reality of mortal vulnerability. Hebrews 2:14-15 frames the Incarnation precisely as participation in death and the flesh, so that Christ could destroy the one who has the power of death. Hezekiah's death sentence is the type; Christ's willing reception of the sentence of death (John 12:27: <em>now is my soul troubled; and what shall I say? Father, save me from this hour?</em>) is the antitype.</p>",
"2": "<p>A type: Hezekiah turns his face to the wall and prays to YHWH. The turning away from the human scene toward YHWH alone in extremity is the posture of authentic prayer under mortal crisis. Jesus in Gethsemane falls on his face and prays (Matt 26:39), withdrawing from the disciples to seek the Father's face. Hebrews 5:7 frames this: <em>in the days of his flesh, Jesus offered up prayers and supplications, with loud crying and tears, to the one who was able to save him from death</em>. Hezekiah's turned face toward the wall is the type of Christ's turned face toward the Father.</p>",
"3": "<p>A type: Hezekiah's prayer — <em>remember, YHWH, how I have walked before you in truth and with a whole heart</em> — and the bitter weeping (<em>wayib̠k̠e bĕk̠î gādôl</em>). The combination of faithfulness-appeal and tears is the posture of those who trust YHWH at death's door. Christ's Gethsemane prayer is not a faithfulness-appeal but its inverse — a complete surrender to the Father's will rather than his own. Hebrews 5:7 notes that his prayers with loud cries and tears were heard because of his godly fear (<em>eulabeias</em>) — the same deep reverence Hezekiah's tears express.</p>",
"4": "<p>A revelation of God: the word of YHWH comes to Isaiah immediately — the divine response to prayer is prompt and active. The sequence (prayer → divine word → messenger → healing) models the NT promise of prayer's effectiveness: before they call I will answer, while they are still speaking I will hear (Isa 65:24). This responsiveness of YHWH to the prayer of the desperate is the character that Christ reveals as Father (Matt 6:8: your Father knows what you need before you ask).</p>",
"5": "<p>A type: YHWH's response — <em>I have heard your prayer, I have seen your tears</em> (<em>šāma'tî 'et-tĕpillatĕkā rā'îtî 'et-dimĕ'ātĕkā</em>); I will add fifteen years to your life. The divine grant of additional years of life is the type of resurrection life — not mere biological extension but YHWH's sovereign decision to overcome the decree of death. The one who raises Hezekiah from the threshold of Sheol is the same God who raises Christ from the dead (Acts 2:24: God raised him up). The fifteen years granted to Hezekiah points toward the eternal life granted to those in Christ (John 10:28: I give them eternal life, and they shall never perish).</p>",
"6": "<p>A revelation of God: YHWH promises to deliver Hezekiah and Jerusalem from the Assyrian king. The double promise — personal healing and political deliverance — is paired. YHWH does not merely heal one person and abandon the city. This comprehensiveness of divine salvation is reflected in Christ's work: he heals individuals and gathers a people (Acts 20:28: the church which he purchased with his own blood). Personal redemption and community rescue are inseparable in both Hezekiah's deliverance and the gospel.</p>",
"7": "<p>A revelation of God: YHWH gives a sign to authenticate his promise. The sign is freely given — YHWH initiates it, not in response to Hezekiah's demand. The sign-granting God throughout the OT (the rainbow, Gideon's fleece, the burning bush) is the same God who gives the sign of the resurrection: <em>destroy this temple, and in three days I will raise it up</em> (John 2:19). The sign is always external confirmation of internal divine commitment.</p>",
"8": "<p>A revelation of God: the shadow on the sundial of Ahaz goes back ten steps (<em>kĕ'āḥôr 'eśer hamma'ălôt</em>). The reversal of time's arrow — shadow moving backward — is the most dramatic of YHWH's cosmic signs in the Hezekiah narrative. The God who moves the shadow backward is the same God who raises the dead — both are sovereign acts over the natural order. Joshua's long day (Josh 10:12-14) is the companion sign. Christ's resurrection is the ultimate reversal of the shadow — death going backward, time reopened.</p>",
"9": "<p>A shadow: Hezekiah's writing (<em>miktāb</em>) — a psalm or inscription composed after his recovery. The practice of writing a thanksgiving after deliverance from death is the pattern fulfilled by the NT's resurrection testimony: the disciples' witness after the resurrection is the <em>miktāb</em> of those delivered from death's claim. Just as Hezekiah reflects on his near-death and transformation, the apostolic letters reflect on the community's passage through death to life in Christ.</p>",
"10": "<p>A shadow: <em>in the middle of my days I must depart; I am consigned to the gates of Sheol for the rest of my years</em>. Hezekiah's lament — mid-life death, loss of future — is the existential fear that Christ's resurrection resolves. Acts 2:27 (quoting Ps 16:10) applies directly to Christ: <em>you will not abandon my soul to Sheol, nor let your Holy One see corruption</em>. Christ is consigned to the gates of Sheol (Matt 12:40: three days and three nights in the heart of the earth) and then released — the anti-type of Hezekiah's feared but averted descent.</p>",
"11": "<p>A shadow: <em>I shall not see YHWH in the land of the living</em> — the anticipation of Sheol as the end of YHWH-relationship. The OT's partial understanding of Sheol (Ps 6:5: in death there is no remembrance of you) is the dark backdrop against which the resurrection appears in full light. Christ's descent to the dead and resurrection (1 Pet 3:19; 4:6) opens the very place Hezekiah feared as the end of divine relationship into a place penetrated by the risen Lord.</p>",
"12": "<p>A shadow: <em>my dwelling is plucked up and removed from me like a shepherd's tent</em> — the tent that is rolled up, the life cut off like a weaver cutting the thread. Paul uses the same tent-metaphor in 2 Corinthians 5:1-4: <em>we know that if the earthly tent we live in is destroyed, we have a building from God, a house not made with hands, eternal in the heavens</em>. Hezekiah's fear of the tent being dismantled becomes, through Christ, the hope of the permanent dwelling replacing it.</p>",
"13": "<p>A revelation of God: <em>like a lion he breaks all my bones</em> — YHWH as the afflicting power who brings Hezekiah to death's door. The divine affliction of the righteous is a persistent OT theme (Job's suffering; the Psalms of complaint). Christ bears the full weight of this divine affliction: Isaiah 53:4 (<em>he was stricken, smitten by God, and afflicted</em>; <em>it was the will of YHWH to crush him</em>, 53:10). Hezekiah experiences what Hezekiah cannot understand; Christ undergoes it deliberately, for others.</p>",
"14": "<p>A revelation of God: <em>like a swallow or crane I chirp; I moan like a dove; my eyes are weary looking upward — O YHWH, I am oppressed; be my pledge of safety</em> (<em>hā'ōrĕbēnî</em>). The feeble, birdlike cries of extremity — no longer human eloquence but animal vulnerability — is the reduction to which suffering brings the sufferer. Christ on the cross cries the opening of Psalm 22 (<em>My God, my God, why have you forsaken me?</em>) — not philosophical query but the raw cry of abandonment. The swallow's chirp of Hezekiah models the inarticulate extremity from which Christ's cry comes.</p>",
"15": "<p>A revelation of God: <em>what shall I say? For he has spoken to me, and he himself has done it</em> — silence before the divine action. Hezekiah recognizes that YHWH is the agent both of the affliction and the deliverance; speech fails before both. Christ in Gethsemane reaches the same point: <em>nevertheless, not my will but yours be done</em> (Luke 22:42) — the surrender of any claim against divine sovereignty. The anguished silence of <em>what shall I say?</em> becomes the perfect obedience of <em>your will be done</em>.</p>",
"16": "<p>A revelation of God: <em>O Lord, by these things men live, and in all these is the life of my spirit. Oh, restore me to health and make me live.</em> The identification of divine affliction as the very medium of true life — <em>by these things men live</em> — is the paradox of the cross. Christ's death is the means of life for all who trust him (John 12:24: unless a grain of wheat falls into the earth and dies, it remains alone; but if it dies, it bears much fruit). The afflictions that seem to undo life are, in YHWH's economy, the instruments by which life is given.</p>",
"17": "<p>A type: <em>for my welfare I had great bitterness; but in love you have delivered my life from the pit of destruction, for you have cast all my sins behind your back</em> (<em>kî hišlak̠tā 'aḥarê gēwĕkā kol-ḥăṭā'āy</em>). The casting of sins behind YHWH's back — out of sight, permanently dismissed — is the type of forgiveness that Christ achieves definitively. Colossians 2:14 uses the imagery of the written record of debt being erased and set aside by the cross. Hezekiah experiences the cancellation of sins in deliverance; Christ effects the cancellation of sins for all who are in him (Heb 9:28: to take away sins once for all).</p>",
"18": "<p>A shadow: <em>for Sheol does not thank you; death does not praise you; those who go down to the pit do not hope for your faithfulness</em>. The OT understanding that Sheol is the end of praise — resolved definitively by Christ's resurrection. Christ descends into the realm where YHWH cannot be praised (1 Pet 3:19) and emerges, so that even those in the grave will hear his voice (John 5:28-29: all who are in the tombs will hear his voice and come out). Philippians 2:10-11 announces that every knee shall bow — in heaven, on earth, and <em>under the earth</em> — the very place Isaiah 38:18 says cannot praise. Christ's resurrection opens Sheol's silence to sound.</p>",
"19": "<p>A shadow: <em>the living, the living, he thanks you, as I do this day; the father makes known to the children your faithfulness</em>. The generational transmission of praise — the living father telling children of YHWH's faithfulness — is the pattern of resurrection testimony. Acts 2:39 (the promise is for you and your children and all who are far off) frames the gospel's generational reach. The Psalmist's vow (Ps 22:30-31: posterity shall serve him; it shall be told of the Lord to the coming generation) is the same pattern: the one delivered from death tells the next generation. Hezekiah's <em>the living, the living</em> becomes the NT's resurrection proclamation.</p>",
"20": "<p>A shadow: <em>YHWH will save me, and we will sing my songs to the stringed instruments all the days of our life, at the house of YHWH</em>. The vow of perpetual praise in the temple community is the type of the eternal worship of the new Jerusalem (Rev 5:9: they sang a new song; Rev 14:3: the new song before the throne). Hezekiah's deliverance from death issues in song; Christ's resurrection issues in the new song of the redeemed — the eternal Hezekiah-praise of those raised from the threat of Sheol.</p>",
"21": "<p>A shadow: Isaiah's instruction — take a cake of figs and apply it to the boil (<em>dĕb̠elet tĕ'ēnîm</em>), that Hezekiah may recover. The use of a natural remedy (figs/poultice) as the instrument of divine healing establishes the pattern that YHWH works through ordinary means. The NT's healing ministry of Jesus uses a range of means — mud, spit, word, touch. The fig-cake is neither magic nor medicine but an obedient act within the framework of divine promise. Christ heals through his word, through the Spirit, through the sacraments — ordinary means carrying extraordinary grace.</p>",
"22": "<p>A shadow: Hezekiah asks <em>what is the sign that I shall go up to the house of YHWH?</em> — the restored king's goal is not merely survival but temple-access, restored relationship. The temple is the destination of the healed: Luke 17:14 (the healed lepers go to show themselves to the priests; one returns to give thanks). Christ is the true temple (John 2:21) and the true access to the Father (John 14:6; Heb 4:16: we may draw near to the throne of grace with confidence). Hezekiah's question — how do I get to the house of YHWH? — finds its answer in the one who is the way to the Father's house.</p>"
}
}

def main():
    existing = load_comm('mkt-christ', 'isaiah')
    merge_comm(existing, ISAIAH)
    save_comm('mkt-christ', 'isaiah', existing)
    v = sum(len(vs) for vs in ISAIAH.values())
    print(f'Isaiah 38 mkt-christ: {v} verses written.')

if __name__ == '__main__':
    main()
