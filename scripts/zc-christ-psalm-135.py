"""
MKT Christ Commentary — Psalm 135 (21 verses — praise + anti-idol polemic)
Run: python3 scripts/zc-christ-psalm-135.py
Key decisions:
- v4 'chose Jacob as his own / treasured possession' → 1 Pet 2:9 applied to
  the church in Christ; election language transferred to the new-covenant community
- v13 name-endures-forever → Phil 2:9 name above every name given to Christ
- v14 uphold-cause-of-people → Rom 8:34 Christ intercedes at right hand
- v15-18 idol polemic → Col 1:15 Christ the true image of the invisible God
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
    # CHANGE? If psalms.json schema changes, update merge_comm and PSALMS below.
    # VERIFY: python3 -c "import json; d=json.load(open('data/commentary/mkt-christ/
    #   psalms.json')); print('135 v4:',d.get('135',{}).get('4','MISSING')[:60])"
    for ch, verses in new_data.items():
        existing.setdefault(ch, {})
        for v, text in verses.items():
            existing[ch].setdefault(v, text)


PSALMS = {
    "135": {
        "1": "<p>\"Praise the LORD! Praise the name of the LORD; praise him, all you servants of the LORD\" — the call to praise that opens this psalm, echoing and expanding on Psalm 134. Hebrews 13:15: \"Through Jesus, therefore, let us continually offer to God a sacrifice of praise — the fruit of lips that openly profess his name.\" The servants called to praise in Psalm 135:1 are the new-covenant community offering perpetual praise through Christ the mediator. \"Praise the name\" is the posture of the church at every gathering.</p>",
        "2": "<p>\"you who stand in the LORD's house and serve in the courts of our God\" — the servants stationed in the divine house. Hebrews 3:6: Christ is \"faithful as the Son over God's house. And we are his house, if indeed we hold firmly to our confidence.\" The servants who stand in the LORD's house are now the living stones of the house that Christ is building (1 Pet 2:5) — the community is simultaneously the servant-worshipers and the house they serve in, because Christ is both Son-over-the-house and the cornerstone.</p>",
        "3": "<p>\"Praise the LORD, for the LORD is good; sing praises to his name — it is a delight\" — the goodness of YHWH as the ground of praise. Mark 10:18: Jesus said \"No one is good — except God alone\" — paradoxically pointing to his own identity with the God whose goodness is absolute. Romans 8:28: \"in all things God works for the good of those who love him.\" The goodness of YHWH that makes praise a delight is the goodness revealed in the gospel: the God who is good enough to give his Son for enemies (Rom 5:8).</p>",
        "4": "<p>\"For the LORD chose (<em>bahar</em>) Jacob as his own, Israel as his <strong>prized and treasured possession</strong> (<em>segullah</em>)\" — the election of Israel. First Peter 2:9: \"But you are a chosen people (<em>genos eklekton</em>), a royal priesthood, a holy nation, <strong>God's special possession</strong> (<em>laos eis peripoiesin</em>).\" Peter applies the language of Psalm 135:4 directly to the new-covenant community — the election and treasured-possession status of Israel moves to all who are in Christ (Gal 3:29). Christ is himself the chosen one (Luke 9:35: \"This is my Son, whom I have chosen\"), and in him all who believe share the elect status of the beloved Son.</p>",
        "5": "<p>\"I know that the LORD is great — our Lord stands above every so-called god\" — the confession of YHWH's supremacy over all competitors. Ephesians 1:20-21: Christ was raised and \"seated at his right hand in the heavenly realms, <strong>far above all rule and authority, power and dominion, and every name that is invoked</strong>.\" The supremacy of YHWH over every so-called god in Psalm 135:5 is the supremacy that Christ exercises at the right hand of the Father — he is above every principality, power, and divine competitor.</p>",
        "6": "<p>\"The LORD does whatever he pleases — in heaven and on earth, in the seas and every depth\" — divine sovereignty across all domains. Matthew 6:10: \"Your will be done, on earth as it is in heaven\" — Christ's prayer is that the sovereign will operative in heaven might now penetrate earth. Ephesians 1:11: \"In him we were also chosen, having been predestined according to the plan of him who works out everything in conformity with the purpose of his will.\" The God who does whatever he pleases is the God whose eternal pleasure includes the Incarnation, death, and resurrection of his Son.</p>",
        "7": "<p>\"He draws up clouds from the far ends of the earth, makes lightning flash with the rain, and releases the wind from his storehouses\" — the Creator God who commands the weather. Colossians 1:16-17: \"all things have been created through him and for him. He is before all things, and in him all things hold together.\" The weather-commanding God of Psalm 135:7 is the one through whom Christ creates and sustains — the disciples in the boat marveled: \"Who is this? Even the wind and the waves obey him!\" (Mark 4:41).</p>",
        "8": "<p>\"He struck down the firstborn of Egypt — both people and animals alike\" — the Passover plague. First Corinthians 5:7: \"For Christ, our Passover lamb, has been sacrificed.\" The striking of Egypt's firstborn in Psalm 135:8 is the judgment that the Passover Lamb absorbs and redirects — God's firstborn Son takes the judgment so that all who shelter under his blood are spared. The death of Egypt's firstborn at the Exodus is the type; the death of God's own firstborn at Calvary is the antitype that accomplishes what the type pointed toward.</p>",
        "9": "<p>\"He sent miraculous signs and wonders into Egypt — striking Pharaoh and all his servants\" — the Exodus signs. Acts 2:22: \"Jesus of Nazareth was a man accredited by God to you by miracles, wonders and signs, which God did among you through him.\" The signs-and-wonders vocabulary of the Exodus is applied directly to Jesus's ministry — he is the new Moses, the one through whom God performs the definitive signs that establish the new covenant community and certify his identity as the Sent One.</p>",
        "10": "<p>\"He defeated great nations and put mighty kings to death\" — the conquest of Canaan. Colossians 2:15: \"And having disarmed the powers and authorities, he made a public spectacle of them, triumphing over them by the cross.\" Christ's victory over the powers is the definitive conquest that all the military victories of Israel only foreshadow. The great nations defeated at the Exodus and conquest are the type of every power that opposes God, defeated by Christ's death and resurrection.</p>",
        "11": "<p>\"Sihon king of the Amorites, Og king of Bashan, and all the kingdoms of Canaan\" — the named defeated kings. Each specific king represents a power that stood against the progress of God's purposes — and each fell. Revelation 19:19-21: \"the beast and the kings of the earth and their armies gathered together to wage war against the rider on the horse and his army. But the beast was captured... The rest were killed.\" The Og-and-Sihon pattern of defeat anticipates the final defeat of every anti-God power by the rider on the white horse who is Christ.</p>",
        "12": "<p>\"and gave their land as an inheritance — an inheritance to his people Israel\" — the land-grant that follows conquest. Hebrews 4:8-11: \"For if Joshua had given them rest, God would not have spoken later about another day. There remains, then, a Sabbath-rest for the people of God.\" Matthew 5:5: \"Blessed are the meek, for they will inherit the earth.\" The land given to Israel as inheritance is the prototype of the eschatological inheritance — the whole renewed earth — that Christ secures for his people through his death and resurrection (Col 1:12: the Father \"has qualified you to share in the inheritance of his holy people in the kingdom of light\").</p>",
        "13": "<p>\"O LORD, <strong>your name endures forever</strong>; your memory is kept alive through every generation\" — the permanence of the divine name. Philippians 2:9-11: \"God exalted him to the highest place and gave him <strong>the name that is above every name</strong>, so that at the name of Jesus every knee should bow.\" The name that endures forever in Psalm 135:13 is the name given to Christ — YHWH's own name, whose permanence and universal recognition the NT attributes to Christ. Hebrews 13:8: \"Jesus Christ is the same yesterday and today and forever\" — his name endures as the living carrier of the divine identity across every generation.</p>",
        "14": "<p>\"The LORD will uphold the cause of his people and will show compassion toward his servants\" — divine advocacy and compassion. Romans 8:34: \"Christ Jesus who died — more than that, who was raised to life — is at the right hand of God and is also <strong>interceding for us</strong>.\" The LORD's upholding of the people's cause in Psalm 135:14 is what Christ does perpetually as the living intercessor at the Father's right hand: Hebrews 7:25: \"he always lives to make intercession for them.\" Every servant of God has Christ as their advocate before the Father (1 John 2:1).</p>",
        "15": "<p>\"The idols of the nations are silver and gold — nothing but the work of human hands\" — the idol polemic (cf. Ps 115:4-8). Colossians 1:15: Christ is \"the <strong>image of the invisible God</strong>.\" The contrast between the man-made idol and the divinely given image is the implicit Christological argument: humanity needs a true image of the living God, and Christ is that image. Acts 17:29: \"We should not think that the divine being is like gold or silver or stone — an image made by human design and skill.\" The idol critique prepares for the announcement of the living God revealed in Christ.</p>",
        "16": "<p>\"They have mouths, but they cannot speak; they have eyes, but they cannot see\" — the impotent idol (cf. Ps 115:5). In contrast, Jesus speaks with divine authority (Matt 7:29), sees with perfect perception (John 2:25), and hears every cry (John 11:35). The list of idol-failures in Psalm 135:16-17 is the negative of everything Christ positively is: the living Word who speaks, the Light who sees, the ear that hears every prayer — the true image of the living God as opposed to the dead image of human manufacture.</p>",
        "17": "<p>\"they have ears but cannot hear; there is not a breath of air in their mouths\" — the idol has no breath (<em>ruah</em>). John 20:22: the risen Christ \"breathed on them and said, 'Receive the Holy Spirit.'\" The idol's breathless, lifeless mouth is the negative of Christ who breathes the Spirit into his disciples — the divine breath that first animated humanity (Gen 2:7) is now given by the risen Son to animate the new creation community. The breathless idol contrasts with the breath-giving Lord.</p>",
        "18": "<p>\"Those who make them will become like them — and so will all who put their trust in them\" — the moral conformity principle: worshipers become like what they worship. Second Corinthians 3:18: \"we all, who with unveiled faces contemplate the Lord's glory, are being <strong>transformed into his image</strong> with ever-increasing glory, which comes from the Lord, who is the Spirit.\" The inverse of idol-deformation is Christ-transformation: those who fix their eyes on Christ become like Christ, progressively conformed to the image of the Son (Rom 8:29).</p>",
        "19": "<p>\"Praise the LORD, O house of Israel! Praise the LORD, O house of Aaron!\" — the first two of three groups called to praise. The new-covenant community fulfills and extends this call: \"you are a chosen people, a royal priesthood, a holy nation\" (1 Pet 2:9). The house of Israel and house of Aaron that the psalm calls to praise now gather in Christ, who is both the true Israel and the great High Priest who supersedes Aaron (Heb 7:11). Their praise is offered through him.</p>",
        "20": "<p>\"Praise the LORD, O house of Levi! All who fear the LORD, praise the LORD!\" — the priestly tribe and all God-fearers called to join. Hebrews 7:11-12: \"If perfection could have been attained through the Levitical priesthood... why was there still need for another priest?\" The house of Levi is superseded by Christ, who holds a permanent priesthood (Heb 7:24). The \"all who fear the LORD\" of Psalm 135:20 is the widest possible invitation, encompassing every nation — the phrase that points toward the Gentile mission (Acts 10:34-35).</p>",
        "21": "<p>\"Praise be to the LORD from Zion — he who makes his home in Jerusalem. Praise the LORD!\" — the praise ascending from the divine dwelling-place. Hebrews 12:22-24: \"you have come to Mount Zion and to the city of the living God, the heavenly Jerusalem... to Jesus the mediator of a new covenant.\" The praise from Zion in Psalm 135:21 is the eschatological praise of the heavenly Jerusalem — the city of which Christ is the cornerstone (Eph 2:20) and the temple (Rev 21:22: \"I did not see a temple in the city, because the Lord God Almighty and the Lamb are its temple\").</p>"
    }
}


def main():
    existing = load_comm("mkt-christ", "psalms")
    before = sum(len(v) for v in existing.values())
    merge_comm(existing, PSALMS)
    after = sum(len(v) for v in existing.values())
    save_comm("mkt-christ", "psalms", existing)
    print(f"{len(existing)} chapters, {after} verse entries total (+{after - before} new)")
    for v, kw in [("4", "chosen"), ("13", "name"), ("14", "interceding"), ("18", "image")]:
        entry = existing.get("135", {}).get(v, "MISSING")
        print(f"  Ps 135:{v} — {'OK' if kw.lower() in entry.lower() else 'CHECK'}")


if __name__ == "__main__":
    main()
