"""
MKT Deuteronomy chapters 7–12 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-deuteronomy-7-12.py

Covers: the command to dispossess seven nations and destroy their cult sites (ch. 7);
the wilderness memory and warning against prosperity-pride (ch. 8); Israel's stubbornness,
the golden calf, and Moses' intercession (ch. 9); new tablets, the Levites, and what God
requires (ch. 10); love the LORD, the land drinks rain from heaven, blessings and curses,
Gerizim and Ebal (ch. 11); the central sanctuary law and the blood prohibition (ch. 12).

Translation decisions:
- H3068 (יהוה): "LORD" in L/M; "the LORD" in T — matches prior Numbers/Exodus/Leviticus scripts
- H430 (אֱלֹהִים): "God" all tiers
- H2617 (חֶסֶד): "steadfast love" all tiers — no single English word suffices; covenant loyalty + active kindness
- H1285 (בְּרִית): "covenant" all tiers
- H5459 (סְגֻלָּה): "treasured possession" L/M; "treasured people" T — royal/personal possession idiom
- H6918 (קָדוֹשׁ): "holy" all tiers
- H5971 (עַם): "people" all tiers
- H3820/H3824 (לֵב/לֵבָב): "heart" all tiers; the longer form לֵבָב emphasises inner totality — T notes this where it falls in the Shema passages
- H5315 (נֶפֶשׁ): "soul" L/M; "whole self" T — embodied self, not Greek immaterial soul
- H8085 (שָׁמַע): "hear" L; "obey/heed" M where the obedience sense dominates; T surfaces both registers
- H7186 (קָשֶׁה) / H6203 (עֹרֶף): "stiff-necked" all tiers — ox-yoke metaphor; T notes the agricultural image
- H6189 (עָרֵל) in 10:16: "foreskin of your heart" — L/M preserve the shocking body-metaphor; T makes inner-transformation explicit
- H4148 (מוּסָר): "discipline" all tiers — not punishment alone but the father-son correction of 8:5
- H5772/H842 (אֲשֵׁרָה): "Asherah poles" all tiers — Canaanite goddess cult poles; not "groves"
- H4676 (מַצֵּבָה): "sacred pillars" L/M; "standing stones" T
- H6459 (פֶּסֶל): "carved images" all tiers
- H7307 (רוּחַ): not prominent in these chapters
- H5930 (עֹלָה): "burnt offering(s)" all tiers
- H4503 (מִנְחָה): "contribution/offering" all tiers depending on context
- H4643 (מַעֲשֵׂר): "tithe" all tiers
- H1060 (בְּכוֹר): "firstborn" all tiers
- H4196 (מִזְבֵּחַ): "altar" all tiers
- H5159 (נַחֲלָה): "inheritance" all tiers
- H1818 (דָּם): "blood" all tiers; the blood-prohibition in ch. 12 is that blood = life (נֶפֶשׁ); T surfaces this equation
- Ch. 7 note: The destruction of Canaanite cult objects is framed theologically — their gods will become
  a snare (v.16,25). L/M render all commands plainly; T notes the protective logic behind the severity.
- Ch. 8:3 note: "Man does not live by bread alone" — this verse (later quoted by Jesus in Matt 4:4) refers
  to God's spoken word sustaining life through manna; T makes the word/provision connection explicit.
- Ch. 8:17 note: "My power and the might of my hand" — pride-of-achievement is the central danger of
  prosperity. T renders this as a cautionary direct speech pattern.
- Ch. 9 note: Moses' intercession (vv.25-29) is theologically crucial — he appeals to God's reputation
  among the nations and to the patriarchal oath, not to Israel's merit. T surfaces both arguments.
- Ch. 10:12 note: The "what does the LORD require" formula anticipates Micah 6:8. T notes the parallel.
- Ch. 10:16 note: "Circumcise the foreskin of your heart" is one of Deuteronomy's signature metaphors —
  inner covenant-marking. T renders this as a call to remove inner resistance.
- Ch. 10:17 note: "God of gods, Lord of lords" — a superlative construction (not polytheistic affirmation).
  T renders this with superlative force: "the supreme God, Sovereign above all rulers."
- Ch. 11:10-12 note: Egypt vs. Canaan contrast — Egypt's irrigation was human labour (foot-operated
  channels); Canaan is watered by heaven. T makes the theological implication explicit: Canaan is a land
  of dependence on God, not human control.
- Ch. 11:18-21: The second Shema passage — bind/teach/write. T reads this as a total formation programme.
- Ch. 12 note: The centralization law is a major theological move — worship consolidation destroys the
  syncretistic local-shrine pattern. T notes this is about purity of worship, not convenience.
- Ch. 12:23: "The blood is the life" — נֶפֶשׁ in both terms; T: "the blood carries the life-force of the
  creature." This is the foundational reason behind all blood prohibitions in the Torah.
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

DEUTERONOMY = {
  "7": {
    "1": {
      "L": "When the LORD your God brings you into the land you are going to possess, and drives out before you many nations — the Hittites, the Girgashites, the Amorites, the Canaanites, the Perizzites, the Hivites, and the Jebusites, seven nations greater and mightier than you —",
      "M": "When the LORD your God brings you into the land you are entering to possess and drives out before you many nations — the Hittites, Girgashites, Amorites, Canaanites, Perizzites, Hivites, and Jebusites, seven nations greater and mightier than you —",
      "T": "When the LORD your God brings you into the land you are about to enter and possess, driving out ahead of you seven nations greater and stronger than you — the Hittites, Girgashites, Amorites, Canaanites, Perizzites, Hivites, and Jebusites —"
    },
    "2": {
      "L": "and when the LORD your God delivers them before you, and you strike them, you shall utterly destroy them. You shall make no covenant with them and show them no mercy.",
      "M": "and when the LORD your God delivers them over to you and you defeat them, you must completely destroy them. Make no covenant with them and show them no mercy.",
      "T": "when the LORD your God hands them over to you and you defeat them, you must devote them to complete destruction. Make no treaty with them; extend them no mercy."
    },
    "3": {
      "L": "And you shall not intermarry with them. Your daughter you shall not give to his son, nor his daughter shall you take for your son,",
      "M": "Do not intermarry with them. Do not give your daughter to their sons or take their daughters for your sons,",
      "T": "Do not intermarry with them — do not give your daughters to their sons or take their daughters for your sons."
    },
    "4": {
      "L": "for he will turn your son from following me, and they will serve other gods, and the anger of the LORD will be kindled against you, and he will destroy you quickly.",
      "M": "for they will turn your sons away from following me to serve other gods, and then the anger of the LORD will burn against you and he will destroy you quickly.",
      "T": "For those foreign wives will turn your sons away from me toward other gods, and then the LORD's anger will blaze against you and he will bring you to sudden ruin."
    },
    "5": {
      "L": "But thus you shall do to them: their altars you shall break down, and their sacred pillars you shall shatter, and their Asherah poles you shall cut down, and their carved images you shall burn with fire.",
      "M": "Instead, this is what you shall do to them: tear down their altars, shatter their sacred pillars, cut down their Asherah poles, and burn their carved images with fire.",
      "T": "This is how you must deal with them: demolish their altars, smash their standing stones, cut down their Asherah poles, and burn their idols to ash."
    },
    "6": {
      "L": "For you are a people holy to the LORD your God. The LORD your God has chosen you to be a people for his treasured possession out of all the peoples who are on the face of the earth.",
      "M": "For you are a people holy to the LORD your God. The LORD your God has chosen you to be his treasured possession from all the peoples on the face of the earth.",
      "T": "You are a people consecrated to the LORD your God. Out of all the peoples on the face of the earth, the LORD your God chose you to be his own treasured people."
    },
    "7": {
      "L": "Not because you were more in number than any other people did the LORD set his love on you and choose you, for you were the fewest of all peoples,",
      "M": "The LORD did not set his love on you and choose you because you were more numerous than any other people — you were the smallest of all peoples.",
      "T": "The LORD did not set his love on you or choose you because you outnumbered other peoples — you were the smallest nation of all."
    },
    "8": {
      "L": "but because the LORD loved you and kept the oath that he swore to your fathers, the LORD has brought you out with a mighty hand and redeemed you from the house of slavery, from the hand of Pharaoh king of Egypt.",
      "M": "Rather, it was because the LORD loved you and was keeping the oath he swore to your fathers that he brought you out with a mighty hand and redeemed you from the house of slavery, from the hand of Pharaoh king of Egypt.",
      "T": "Rather, it was because the LORD loved you and was faithful to the oath he swore to your ancestors that he brought you out with a powerful hand and ransomed you from the grip of slavery — from the hand of Pharaoh king of Egypt."
    },
    "9": {
      "L": "Know therefore that the LORD your God is God, the faithful God who keeps covenant and steadfast love with those who love him and keep his commandments, to a thousand generations,",
      "M": "Know therefore that the LORD your God is God — the faithful God who keeps his covenant and steadfast love with those who love him and keep his commandments, to a thousand generations.",
      "T": "Understand this: the LORD your God is the true God — the faithful God who maintains his covenant loyalty toward those who love him and keep his commands, down to a thousand generations."
    },
    "10": {
      "L": "and repays to their face those who hate him by destroying them. He will not be slow with one who hates him; he will repay him to his face.",
      "M": "but he repays those who hate him to their face by destroying them. He will not delay with the one who hates him; he will repay him to his face.",
      "T": "But he repays those who hate him — he destroys them openly, without delay. Those who oppose him he pays back in full, face to face."
    },
    "11": {
      "L": "You shall therefore keep the commandment and the statutes and the rules that I command you today, to do them.",
      "M": "Therefore keep the commandments, statutes, and rules that I am commanding you today, and carry them out.",
      "T": "So keep all the commandments, statutes, and ordinances I am giving you today — carry them out."
    },
    "12": {
      "L": "And because you listen to these rules and keep and do them, the LORD your God will keep with you the covenant and the steadfast love that he swore to your fathers.",
      "M": "If you heed these ordinances, keep them, and carry them out, the LORD your God will maintain his covenant and steadfast love with you, just as he swore to your fathers.",
      "T": "If you hear these ordinances and faithfully carry them out, the LORD your God will uphold the covenant loyalty he promised your ancestors."
    },
    "13": {
      "L": "He will love you, bless you, and multiply you. He will also bless the fruit of your womb and the fruit of your ground — your grain and your wine and your oil, the increase of your herds and the young of your flock — in the land that he swore to your fathers to give you.",
      "M": "He will love you, bless you, and increase your numbers. He will bless the fruit of your womb and the fruit of your ground — your grain, new wine, and olive oil, the young of your cattle and the lambs of your flock — in the land he swore to your fathers to give you.",
      "T": "He will love you, bless you, and cause you to flourish. He will bless the children born to you and the crops you grow — grain, wine, and oil; the calves of your herds and the lambs of your flocks — in the land he promised your ancestors."
    },
    "14": {
      "L": "You shall be blessed above all peoples. There shall not be male or female barren among you or among your livestock.",
      "M": "You will be blessed more than any other people. None of your men or women will be childless, and none of your livestock will be barren.",
      "T": "You will be the most blessed of nations. No one among you — man or woman — will be childless, and no animal in your herds will be barren."
    },
    "15": {
      "L": "And the LORD will take away from you all sickness, and none of the evil diseases of Egypt that you knew will he put on you, but he will put them on all who hate you.",
      "M": "The LORD will keep you free from every sickness and will not inflict on you the dreadful diseases of Egypt that you know about, but will lay them on all who hate you.",
      "T": "The LORD will remove every disease from you. None of the terrible Egyptian plagues you know about will fall on you — instead they will fall on all who oppose you."
    },
    "16": {
      "L": "And you shall consume all the peoples that the LORD your God delivers to you. Your eye shall not pity them, and you shall not serve their gods, for that would be a snare to you.",
      "M": "You must destroy all the peoples the LORD your God hands over to you. Do not look on them with pity, and do not serve their gods, for that will be a snare to you.",
      "T": "Destroy every nation the LORD your God delivers into your hands. Show no pity — and never serve their gods, for that path leads straight into a trap."
    },
    "17": {
      "L": "If you say in your heart, 'These nations are greater than I; how can I dispossess them?'",
      "M": "If you say to yourself, 'These nations are more powerful than I am — how can I drive them out?'",
      "T": "If the thought crosses your mind: 'These nations are too strong for me — how could I ever drive them out?'"
    },
    "18": {
      "L": "you shall not be afraid of them. You shall remember well what the LORD your God did to Pharaoh and to all Egypt —",
      "M": "do not be afraid of them. Remember carefully what the LORD your God did to Pharaoh and to all Egypt:",
      "T": "— do not be afraid. Call to mind exactly what the LORD your God did to Pharaoh and all Egypt:"
    },
    "19": {
      "L": "the great trials that your eyes saw, the signs and the wonders, the mighty hand and the outstretched arm, by which the LORD your God brought you out. So will the LORD your God do to all the peoples of whom you are afraid.",
      "M": "the great ordeals your eyes witnessed, the signs and wonders, the mighty hand and outstretched arm by which the LORD your God brought you out. That is what the LORD your God will do to all the peoples you now fear.",
      "T": "the great trials your own eyes witnessed — the signs and wonders, the strong hand and the outstretched arm by which the LORD brought you out. That same LORD will do it again to every nation you fear."
    },
    "20": {
      "L": "Moreover, the LORD your God will send the hornet among them, until those who are left and those who hide from you are destroyed.",
      "M": "Furthermore, the LORD your God will send the hornet among them until those who survive and hide from you have also perished.",
      "T": "Beyond that, the LORD your God will unleash a relentless plague among them, hunting down even those who escape and go into hiding, until none remain."
    },
    "21": {
      "L": "You shall not be in dread of them, for the LORD your God is in your midst, a great and awesome God.",
      "M": "Do not be terrified by them, for the LORD your God is among you — a great and awesome God.",
      "T": "Do not be terrified by them. The LORD your God is with you in the midst of the camp — a God of overwhelming greatness and holy terror."
    },
    "22": {
      "L": "The LORD your God will clear away these nations before you little by little. You may not make an end of them at once, lest the wild beasts grow too numerous for you.",
      "M": "The LORD your God will drive out these nations before you gradually, little by little. You must not eliminate them all at once, or the wild animals will multiply against you.",
      "T": "The LORD your God will clear these nations away before you bit by bit — not all at once, so that the wilderness does not fill with wild animals while the land remains unsettled."
    },
    "23": {
      "L": "But the LORD your God will deliver them over to you and throw them into great confusion, until they are destroyed.",
      "M": "But the LORD your God will hand them over to you and throw them into great panic until they are destroyed.",
      "T": "The LORD your God will hand them over to you, throwing them into mounting panic until they are completely wiped out."
    },
    "24": {
      "L": "And he will give their kings into your hand, and you shall make their name perish from under heaven. No one will be able to stand against you until you have destroyed them.",
      "M": "He will hand their kings over to you, and you will erase their name from under heaven. No one will be able to stand against you until you have destroyed them.",
      "T": "He will deliver their kings into your hands, and you will wipe their names off the earth. No one will be able to hold their ground against you until you have finished the work."
    },
    "25": {
      "L": "The carved images of their gods you shall burn with fire. You shall not covet the silver or the gold on them or take it for yourself, lest you be ensnared by it, for it is an abomination to the LORD your God.",
      "M": "Burn the carved images of their gods with fire. Do not covet the silver or gold on them or take any of it for yourself, lest you be ensnared by it — it is an abomination to the LORD your God.",
      "T": "Burn their idols in the fire. Do not be drawn to the silver and gold on them; do not take any of it for yourself — it will ensnare you. It is something the LORD your God finds utterly repugnant."
    },
    "26": {
      "L": "And you shall not bring an abominable thing into your house lest you become devoted to destruction like it. You shall utterly detest it and utterly abhor it, for it is devoted to destruction.",
      "M": "Do not bring a detestable thing into your house, or you will be devoted to destruction along with it. Utterly detest it and utterly abhor it, for it is set apart for destruction.",
      "T": "Do not bring an accursed thing into your house — that path leads to sharing in its destruction. Loathe it completely, despise it utterly, for it is under the ban of destruction."
    }
  },
  "8": {
    "1": {
      "L": "All the commandments that I command you today you shall be careful to do, that you may live and multiply, and go in and possess the land that the LORD swore to give to your fathers.",
      "M": "Be careful to carry out every commandment I am giving you today, so that you may live and multiply and go in and possess the land the LORD swore to give your fathers.",
      "T": "Keep every commandment I am giving you today — carry them out faithfully, so that you may live, grow numerous, and enter and possess the land the LORD promised your ancestors."
    },
    "2": {
      "L": "And you shall remember the whole way that the LORD your God has led you these forty years in the wilderness, that he might humble you, testing you to know what was in your heart, whether you would keep his commandments or not.",
      "M": "Remember the whole journey the LORD your God led you these forty years in the wilderness, humbling you and testing you to know what was in your heart — whether or not you would keep his commandments.",
      "T": "Remember every step of the way the LORD your God led you through forty years in the wilderness. He was humbling you, testing you — probing what was truly in your heart, whether you would keep his commands or not."
    },
    "3": {
      "L": "And he humbled you and let you hunger and fed you with manna, which you did not know, nor did your fathers know, that he might make you know that man does not live by bread alone, but by every word that proceeds from the mouth of the LORD.",
      "M": "He humbled you by letting you go hungry and then feeding you with manna, which neither you nor your fathers had ever known, to teach you that man does not live by bread alone but by every word that comes from the mouth of the LORD.",
      "T": "He humbled you — letting you feel real hunger, then feeding you manna that neither you nor your ancestors had ever tasted. The lesson: human life is not sustained by food alone but by every word God speaks. His provision is as real as bread, and more fundamental."
    },
    "4": {
      "L": "Your clothing did not wear out on you and your foot did not swell these forty years.",
      "M": "Your clothing did not wear out and your feet did not swell during those forty years.",
      "T": "Through forty years, your clothing never wore out and your feet never blistered — the LORD sustained you in details you barely noticed."
    },
    "5": {
      "L": "Know then in your heart that as a man disciplines his son, so the LORD your God disciplines you.",
      "M": "Know this in your heart: just as a man disciplines his son, so the LORD your God has been disciplining you.",
      "T": "Understand this in the depths of your heart: the LORD your God has been dealing with you as a father deals with a son — disciplining you for love, not abandoning you in anger."
    },
    "6": {
      "L": "So you shall keep the commandments of the LORD your God by walking in his ways and by fearing him.",
      "M": "Therefore keep the commandments of the LORD your God by walking in his ways and fearing him.",
      "T": "Therefore keep the LORD your God's commandments — walk in his ways and stand in reverent awe before him."
    },
    "7": {
      "L": "For the LORD your God is bringing you into a good land, a land of brooks of water, of fountains and springs, flowing out in the valleys and hills,",
      "M": "For the LORD your God is bringing you into a good land — a land with streams, pools, and springs flowing through valleys and hills,",
      "T": "The LORD your God is bringing you into a good land — a land laced with streams and springs, water flowing freely through valleys and over hills,"
    },
    "8": {
      "L": "a land of wheat and barley, of vines and fig trees and pomegranates, a land of olive oil and honey,",
      "M": "a land producing wheat and barley, vines, fig trees, and pomegranates, a land of olive oil and honey,",
      "T": "a land of wheat and barley, of grapevines and fig trees and pomegranates, of olive groves and honey —"
    },
    "9": {
      "L": "a land in which you will eat bread without scarcity, in which you will lack nothing, a land whose stones are iron and out of whose hills you can dig copper.",
      "M": "a land where you will eat bread without shortage and will lack nothing, a land whose rocks contain iron and whose hills yield copper.",
      "T": "a land where you will never go hungry, where nothing will be lacking — a land where iron lies in the rocks and copper waits in the hillsides."
    },
    "10": {
      "L": "And you shall eat and be full, and you shall bless the LORD your God for the good land he has given you.",
      "M": "When you have eaten and are full, you shall bless the LORD your God for the good land he has given you.",
      "T": "When you have eaten your fill, you must bless the LORD your God for this good land he has given you — the moment of satisfaction is the moment of thanksgiving."
    },
    "11": {
      "L": "Take care lest you forget the LORD your God by not keeping his commandments and his rules and his statutes, which I command you today,",
      "M": "Be careful that you do not forget the LORD your God by failing to keep his commandments, ordinances, and statutes that I am commanding you today.",
      "T": "Guard yourself: do not forget the LORD your God by letting his commandments, ordinances, and statutes go unkept. That is what forgetting him looks like."
    },
    "12": {
      "L": "lest, when you have eaten and are full and have built good houses and live in them,",
      "M": "Otherwise, when you have eaten your fill, have built fine houses and settled in them,",
      "T": "The danger comes when you are well-fed, living in fine houses,"
    },
    "13": {
      "L": "and when your herds and your flocks multiply and your silver and your gold is multiplied and all that you have is multiplied,",
      "M": "when your herds and flocks have grown large and your silver and gold have increased along with everything else you own,",
      "T": "when your herds and flocks are multiplying, your silver and gold accumulating, and everything you own is increasing —"
    },
    "14": {
      "L": "then your heart be lifted up and you forget the LORD your God, who brought you out of the land of Egypt, out of the house of slavery,",
      "M": "then your heart will become proud and you will forget the LORD your God who brought you out of Egypt, out of the house of slavery.",
      "T": "— that is when your heart grows proud and you forget the LORD your God, who brought you out of Egypt, out of the slave-house."
    },
    "15": {
      "L": "who led you through the great and terrifying wilderness, with its fiery serpents and scorpions and thirsty ground where there was no water, who brought you water out of the flinty rock,",
      "M": "He led you through that vast and fearful wilderness with its venomous snakes and scorpions, its parched ground with no water, and brought you water out of solid flint.",
      "T": "He led you through that vast, terrifying wasteland — through fiery serpents and scorpions, across cracked, waterless ground — and drew water for you from solid rock."
    },
    "16": {
      "L": "who fed you in the wilderness with manna that your fathers did not know, that he might humble you and test you, to do you good in the end.",
      "M": "He fed you with manna in the wilderness, which your fathers had not known, in order to humble you and test you, so that he might do you good in the end.",
      "T": "He fed you with manna in the wilderness — food your ancestors never knew — humbling and testing you, all with your ultimate good in mind."
    },
    "17": {
      "L": "Beware lest you say in your heart, 'My power and the might of my hand have gotten me this wealth.'",
      "M": "Beware of saying to yourself, 'My power and the strength of my hands have produced this wealth for me.'",
      "T": "Guard against the thought: 'It was my own strength and skill that built this wealth.' That is the central lie of prosperity."
    },
    "18": {
      "L": "You shall remember the LORD your God, for it is he who gives you power to get wealth, that he may confirm his covenant that he swore to your fathers, as it is this day.",
      "M": "Remember the LORD your God, for it is he who gives you the ability to produce wealth, in order to confirm his covenant that he swore to your fathers — as it is today.",
      "T": "Remember the LORD your God — he is the one who gives you the capacity to generate wealth, fulfilling the covenant he swore to your ancestors, as you see this day."
    },
    "19": {
      "L": "And if you forget the LORD your God and go after other gods and serve them and worship them, I solemnly warn you today that you shall surely perish.",
      "M": "If you ever forget the LORD your God and follow other gods, serving and bowing down to them, I warn you solemnly today: you will certainly perish.",
      "T": "If you forget the LORD your God and go running after other gods — serving and worshipping them — I warn you plainly today: you will perish. Completely."
    },
    "20": {
      "L": "Like the nations that the LORD makes to perish before you, so shall you perish, because you would not obey the voice of the LORD your God.",
      "M": "You will perish just like the nations the LORD is destroying before you, because you would not obey the LORD your God.",
      "T": "You will go the same way as those nations the LORD is sweeping away before you — because you refused to listen to the voice of the LORD your God."
    }
  },
  "9": {
    "1": {
      "L": "Hear, O Israel: you are to cross over the Jordan today, to go in to dispossess nations greater and mightier than yourselves, cities great and fortified up to heaven,",
      "M": "Hear, O Israel: today you are about to cross the Jordan to go in and dispossess nations greater and mightier than you, with large cities fortified to the sky.",
      "T": "Listen, Israel: today you are crossing the Jordan to drive out nations stronger than you, occupying cities whose walls seem to reach the sky."
    },
    "2": {
      "L": "a people great and tall, the sons of the Anakim, whom you know, and of whom you have heard it said, 'Who can stand before the sons of Anak?'",
      "M": "These are a great people, tall as the Anakites — you know them and have heard the saying: 'Who can stand up to the Anakites?'",
      "T": "These are large, powerful people — descendants of the Anakim, the very ones about whom people say: 'Who could possibly stand against them?'"
    },
    "3": {
      "L": "Know therefore today that he who goes over before you as a consuming fire is the LORD your God. He will destroy them and subdue them before you, so you shall drive them out and make them perish quickly, as the LORD has spoken to you.",
      "M": "Understand today that the LORD your God is the one going ahead of you as a consuming fire. He will destroy and subdue them before you, so that you will drive them out and bring them to ruin quickly, just as the LORD has said.",
      "T": "Understand this: the LORD your God goes before you like a devouring fire. He will break them and bring them low before you — then you will drive them out and destroy them quickly, exactly as the LORD has promised."
    },
    "4": {
      "L": "Do not say in your heart, after the LORD your God has thrust them out before you, 'It is because of my righteousness that the LORD has brought me in to possess this land,' whereas it is because of the wickedness of these nations that the LORD is driving them out before you.",
      "M": "When the LORD your God drives them out before you, do not say to yourself, 'The LORD has brought me in to possess this land because of my righteousness.' No — it is because of the wickedness of these nations that the LORD is driving them out before you.",
      "T": "After the LORD drives them out, do not tell yourself: 'The LORD gave me this land because I am righteous.' That is not it. These nations are being expelled because of their own wickedness, not because of your virtue."
    },
    "5": {
      "L": "Not because of your righteousness or the uprightness of your heart are you going in to possess their land, but because of the wickedness of these nations the LORD your God is driving them out from before you, and that he may confirm the word that the LORD swore to your fathers, to Abraham, to Isaac, and to Jacob.",
      "M": "It is not because of your righteousness or integrity of heart that you are entering to possess their land, but because of the wickedness of these nations that the LORD your God is driving them out before you, and in order to fulfill the promise the LORD swore to your fathers — to Abraham, Isaac, and Jacob.",
      "T": "You are not going in because you are righteous or morally upright. You are going in because these nations are wicked, and because the LORD is keeping the oath he swore to your ancestors Abraham, Isaac, and Jacob. He is being faithful to his word, not rewarding your goodness."
    },
    "6": {
      "L": "Know therefore that the LORD your God is not giving you this good land to possess because of your righteousness, for you are a stubborn people.",
      "M": "Understand that the LORD your God is not giving you this good land to possess because of your righteousness — you are a stubborn people.",
      "T": "Get this clearly: the LORD is not giving you this good land as a reward for righteousness. You are a stiff-necked people — the gift is entirely his grace, not your merit."
    },
    "7": {
      "L": "Remember and do not forget how you provoked the LORD your God to wrath in the wilderness. From the day you came out of the land of Egypt until you came to this place, you have been rebellious against the LORD your God.",
      "M": "Remember this — do not forget how you provoked the LORD your God to anger in the wilderness. From the day you left Egypt until you arrived here, you have been rebellious against the LORD.",
      "T": "Remember — and do not let yourself forget — how you enraged the LORD your God in the wilderness. From the day you walked out of Egypt to this very day, you have been persistently rebellious."
    },
    "8": {
      "L": "Even at Horeb you provoked the LORD to wrath, and the LORD was so angry with you that he was ready to destroy you.",
      "M": "At Horeb you provoked the LORD to such anger that he was ready to destroy you.",
      "T": "Even at Horeb — the mountain of the covenant — you pushed the LORD to fury so severe that he was on the verge of destroying you entirely."
    },
    "9": {
      "L": "When I went up the mountain to receive the tablets of stone, the tablets of the covenant that the LORD made with you, I remained on the mountain forty days and forty nights. I neither ate bread nor drank water.",
      "M": "When I went up the mountain to receive the tablets of stone — the covenant tablets the LORD made with you — I stayed on the mountain forty days and forty nights, eating no bread and drinking no water.",
      "T": "When I went up the mountain to receive the stone tablets — the covenant the LORD was making with you — I remained there forty days and forty nights, eating nothing, drinking nothing."
    },
    "10": {
      "L": "And the LORD gave me the two tablets of stone written with the finger of God, and on them were all the words that the LORD had spoken with you on the mountain out of the midst of the fire on the day of the assembly.",
      "M": "The LORD gave me the two stone tablets, written by the finger of God. On them were all the words the LORD had spoken to you on the mountain out of the fire on the day of the assembly.",
      "T": "Then the LORD gave me the two stone tablets — written by God's own finger — bearing every word he had spoken to you from the fire on the mountain, on the day of the great assembly."
    },
    "11": {
      "L": "And at the end of forty days and forty nights the LORD gave me the two tablets of stone, the tablets of the covenant.",
      "M": "At the end of those forty days and forty nights, the LORD handed me the two stone tablets — the tablets of the covenant.",
      "T": "When the forty days and forty nights were finished, the LORD placed in my hands the two stone tablets — the covenant itself, written in stone."
    },
    "12": {
      "L": "Then the LORD said to me, 'Arise, go down quickly from here, for your people whom you have brought from Egypt have acted corruptly. They have turned aside quickly from the way that I commanded them; they have made a metal image.'",
      "M": "Then the LORD said to me, 'Get up and go down quickly from here, because your people, whom you brought from Egypt, have acted corruptly. They have quickly turned from the way I commanded them; they have cast a metal idol.'",
      "T": "Then the LORD said to me: 'Get up — go back down immediately. Your people, the ones you led out of Egypt, have corrupted themselves. They have bolted from the path I commanded them and cast themselves a metal idol.'"
    },
    "13": {
      "L": "Furthermore the LORD said to me, 'I have seen this people, and behold, it is a stubborn people.'",
      "M": "The LORD also said to me, 'I have observed this people, and they are indeed a stubborn people.'",
      "T": "The LORD continued: 'I have watched this people. They are thoroughly stiff-necked.'"
    },
    "14": {
      "L": "'Let me alone, that I may destroy them and blot out their name from under heaven. And I will make of you a nation mightier and greater than they.'",
      "M": "'Leave me alone so that I may destroy them and blot out their name from under heaven. Then I will make a nation mightier and greater than they from you.'",
      "T": "'Stand aside — I will destroy them and erase their name from the earth. From you I will raise a nation mightier and greater than they ever were.'"
    },
    "15": {
      "L": "So I turned and came down from the mountain, and the mountain was burning with fire. And the two tablets of the covenant were in my two hands.",
      "M": "So I turned and came down from the mountain while it was ablaze with fire, with the two covenant tablets still in my hands.",
      "T": "I turned and came down the mountain — fire still blazing on it — the two covenant tablets gripped in both my hands."
    },
    "16": {
      "L": "And I looked, and behold, you had sinned against the LORD your God. You had made yourselves a calf of metal. You had turned aside quickly from the way that the LORD had commanded you.",
      "M": "And I saw that you had sinned against the LORD your God — you had made yourselves a cast metal calf and had quickly turned from the way the LORD had commanded you.",
      "T": "I saw it for myself: you had sinned against the LORD your God. You had cast yourselves a golden calf and turned off the path the LORD had laid out — astonishingly quickly."
    },
    "17": {
      "L": "So I took hold of the two tablets and threw them out of my two hands and broke them before your eyes.",
      "M": "So I seized the two tablets and threw them from my hands, smashing them before your eyes.",
      "T": "So I seized the two tablets and hurled them down, shattering them in full view of all of you."
    },
    "18": {
      "L": "Then I lay prostrate before the LORD as before, forty days and forty nights. I neither ate bread nor drank water, because of all the sin that you had committed, in doing what was evil in the sight of the LORD to provoke him to anger.",
      "M": "Then I lay prostrate before the LORD as I had before — forty days and forty nights, eating no bread and drinking no water — because of all the sin you had committed by doing what was evil in the LORD's sight, provoking him to anger.",
      "T": "Then I prostrated myself before the LORD a second time — forty days and forty nights, no food, no water — on account of every sin you had committed, doing what is evil in the LORD's sight and provoking his anger."
    },
    "19": {
      "L": "For I was afraid of the anger and hot displeasure that the LORD bore against you, so that he was ready to destroy you. But the LORD listened to me at that time also.",
      "M": "I was terrified of the LORD's fierce anger against you, which was about to destroy you. But the LORD listened to me that time as well.",
      "T": "I was genuinely afraid — the LORD's anger and intense fury against you were at the point of annihilation. But even then, the LORD heard me."
    },
    "20": {
      "L": "And the LORD was so angry with Aaron that he was ready to destroy him. And I prayed for Aaron also at the same time.",
      "M": "The LORD was also very angry with Aaron and was ready to destroy him, so I prayed for Aaron at that time too.",
      "T": "The LORD's anger against Aaron was equally severe — ready to destroy him as well. I interceded for Aaron at the same time."
    },
    "21": {
      "L": "Then I took the sinful thing you had made, the calf, and burned it with fire and crushed it, grinding it very small until it was as fine as dust. And I threw the dust of it into the brook that ran down from the mountain.",
      "M": "I took the sinful calf you had made and burned it in the fire, then crushed and ground it until it was as fine as dust. I threw the dust into the stream running down the mountain.",
      "T": "I took the calf — that sinful thing you had made — burned it, crushed it, and ground it down to powder fine as dust, then scattered the dust into the stream flowing down from the mountain. Utter destruction."
    },
    "22": {
      "L": "And at Taberah also, and at Massah, and at Kibroth-hattaavah, you provoked the LORD to wrath.",
      "M": "You also provoked the LORD to anger at Taberah, at Massah, and at Kibroth-hattaavah.",
      "T": "And it was not only Horeb. At Taberah, at Massah, at Kibroth-hattaavah — you provoked the LORD's fury again and again."
    },
    "23": {
      "L": "And when the LORD sent you from Kadesh-barnea, saying, 'Go up and possess the land that I have given you,' then you rebelled against the commandment of the LORD your God and did not believe him and did not obey his voice.",
      "M": "When the LORD sent you from Kadesh-barnea and said, 'Go up and take possession of the land I am giving you,' you rebelled against the LORD your God's command. You did not trust him and refused to obey him.",
      "T": "When the LORD sent you from Kadesh-barnea and said, 'Go up and take the land I am giving you,' you revolted against his direct command. You did not trust him. You did not obey his voice."
    },
    "24": {
      "L": "You have been rebellious against the LORD from the day that I knew you.",
      "M": "You have been rebellious against the LORD from the day I first knew you.",
      "T": "You have been in rebellion against the LORD for as long as I have known you."
    },
    "25": {
      "L": "So I lay prostrate before the LORD for the forty days and forty nights that I lay prostrate, because the LORD had said he would destroy you.",
      "M": "So I lay prostrate before the LORD for those forty days and forty nights because the LORD had threatened to destroy you.",
      "T": "That is why I lay face down before the LORD for forty days and forty nights — because the LORD had declared he would destroy you."
    },
    "26": {
      "L": "And I prayed to the LORD and said, 'O Lord GOD, do not destroy your people and your heritage, whom you have redeemed through your greatness, whom you have brought out of Egypt with a mighty hand.",
      "M": "I prayed to the LORD and said, 'O Lord GOD, do not destroy your people and your inheritance, whom you redeemed by your greatness and brought out of Egypt with a mighty hand.",
      "T": "I prayed to the LORD: 'O Sovereign LORD, do not destroy your people — your very own inheritance — those you ransomed through your great power and brought out of Egypt with your mighty hand.'"
    },
    "27": {
      "L": "Remember your servants Abraham, Isaac, and Jacob. Do not regard the stubbornness of this people, or their wickedness or their sin,",
      "M": "Remember your servants Abraham, Isaac, and Jacob. Do not consider the stubbornness of this people, their wickedness, or their sin.",
      "T": "Remember Abraham, Isaac, and Jacob — your servants. Do not fix your gaze on this people's stubbornness and wickedness and sin."
    },
    "28": {
      "L": "lest the land from which you brought us say, \"Because the LORD was not able to bring them into the land that he promised them, and because he hated them, he brought them out to put them to death in the wilderness.\"",
      "M": "Otherwise the land you brought us from will say, \"The LORD was unable to bring them to the land he had promised, and because he hated them, he brought them out to put them to death in the wilderness.\"",
      "T": "Otherwise the Egyptians — the land you brought us from — will say: 'The LORD could not bring them to the land he promised, and he hated them anyway, so he led them out to kill them in the wilderness.' Do not let that be the story they tell."
    },
    "29": {
      "L": "For they are your people and your heritage, whom you brought out by your great power and by your outstretched arm.'",
      "M": "But they are your people and your inheritance, whom you brought out by your great power and your outstretched arm.'",
      "T": "They are your people — your heritage. You brought them out with overwhelming power and a fully outstretched arm. That counts for something.'"
    }
  },
  "10": {
    "1": {
      "L": "At that time the LORD said to me, 'Carve out for yourself two tablets of stone like the first, and come up to me on the mountain and make for yourself an ark of wood.",
      "M": "At that time the LORD said to me, 'Chisel out two stone tablets like the first ones, and come up to me on the mountain. Also make a wooden chest.",
      "T": "Then the LORD said to me: 'Carve two stone tablets like the first ones and come up to me on the mountain. Also make a wooden ark to keep them in.'"
    },
    "2": {
      "L": "And I will write on the tablets the words that were on the first tablets that you broke, and you shall put them in the ark.'",
      "M": "I will write on the tablets the words that were on the first tablets, which you broke, and you shall place them in the chest.'",
      "T": "'I will inscribe on them the same words that were on the tablets you shattered. Put them in the ark.'"
    },
    "3": {
      "L": "So I made an ark of acacia wood and carved out two tablets of stone like the first, and went up the mountain with the two tablets in my hand.",
      "M": "So I made an ark of acacia wood and chiseled out two stone tablets like the first, and went up the mountain carrying the two tablets.",
      "T": "I made an ark of acacia wood, carved two stone tablets like the originals, and climbed the mountain with the tablets in hand."
    },
    "4": {
      "L": "And he wrote on the tablets the same writing as before — the Ten Commandments that the LORD had spoken to you on the mountain out of the midst of the fire on the day of the assembly — and the LORD gave them to me.",
      "M": "He wrote on the tablets the same words as before — the Ten Commandments that the LORD had spoken to you from the fire on the mountain on the day of the assembly — and the LORD gave them to me.",
      "T": "He inscribed on the tablets exactly what he had written before — the Ten Commandments that the LORD had spoken from the fire on the day of the assembly — and placed them in my hands."
    },
    "5": {
      "L": "Then I turned and came down from the mountain and put the tablets in the ark that I had made. And there they are, as the LORD commanded me.",
      "M": "Then I came down from the mountain and placed the tablets in the ark I had made. And there they remain — just as the LORD commanded me.",
      "T": "I came down the mountain and placed the tablets in the ark I had built. There they remain to this day — exactly as the LORD commanded."
    },
    "6": {
      "L": "(The people of Israel journeyed from Beeroth Bene-jaakan to Moserah. There Aaron died, and there he was buried. And Eleazar his son ministered as priest in his place.",
      "M": "(The Israelites journeyed from the wells of the Jaakanites to Moserah. There Aaron died and was buried, and Eleazar his son took over the priestly ministry.",
      "T": "(Israel's journey: from Beeroth Bene-jaakan to Moserah, where Aaron died and was buried. His son Eleazar stepped into the priestly office in his place."
    },
    "7": {
      "L": "From there they journeyed to Gudgodah, and from Gudgodah to Jotbathah, a land with streams of water.",
      "M": "From there they traveled to Gudgodah and from Gudgodah to Jotbathah, a land of flowing streams.)",
      "T": "From there: Gudgodah, then Jotbathah — a well-watered land of flowing streams.)"
    },
    "8": {
      "L": "At that time the LORD set apart the tribe of Levi to carry the ark of the covenant of the LORD, to stand before the LORD to minister to him and to bless in his name, to this day.",
      "M": "At that time the LORD set apart the tribe of Levi to carry the ark of the covenant of the LORD, to stand before the LORD and minister to him, and to pronounce blessings in his name — which they do to this day.",
      "T": "At that same time, the LORD singled out the tribe of Levi for a distinct calling: to carry the ark of the covenant, to stand in the LORD's presence and serve him, to speak his blessing over Israel. They are doing it still."
    },
    "9": {
      "L": "Therefore Levi has no portion or inheritance with his brothers. The LORD is his inheritance, as the LORD your God said to him.)",
      "M": "That is why Levi has no share of land or inheritance among his brothers — the LORD himself is his inheritance, as the LORD your God promised him.)",
      "T": "This is why Levi received no land allotment among the tribes — the LORD himself is his inheritance, as the LORD declared. To serve God directly is its own portion.)"
    },
    "10": {
      "L": "I myself stayed on the mountain, as at the first time, forty days and forty nights, and the LORD listened to me at that time also. The LORD was not willing to destroy you.",
      "M": "As for me, I stayed on the mountain forty days and forty nights, as I had the first time, and the LORD listened to me that time as well — the LORD was unwilling to destroy you.",
      "T": "I remained on the mountain forty days and forty nights — a second time. And again the LORD heard me. He was not willing to destroy you."
    },
    "11": {
      "L": "Then the LORD said to me, 'Arise, go on your journey at the head of the people, so that they may go in and possess the land that I swore to their fathers to give them.'",
      "M": "The LORD said to me, 'Get up and lead the people on their journey so that they may go in and take possession of the land I swore to their fathers I would give them.'",
      "T": "The LORD said to me: 'Rise up. Lead the people forward — let them go in and possess the land I promised their ancestors.'"
    },
    "12": {
      "L": "And now, Israel, what does the LORD your God require of you but to fear the LORD your God, to walk in all his ways, to love him, to serve the LORD your God with all your heart and with all your soul,",
      "M": "And now, Israel, what does the LORD your God ask of you except to fear the LORD your God, to walk in all his ways, to love him, and to serve the LORD your God with all your heart and with all your soul —",
      "T": "So now, Israel — what does the LORD your God actually ask of you? Simply this: to revere the LORD your God, to walk in all his ways, to love him, and to serve him with your whole heart and your whole self —"
    },
    "13": {
      "L": "and to keep the commandments and statutes of the LORD, which I am commanding you today for your good?",
      "M": "and to keep the LORD's commandments and statutes that I am commanding you today for your own good?",
      "T": "— and to keep his commandments and statutes, which I am giving you today entirely for your benefit."
    },
    "14": {
      "L": "Behold, to the LORD your God belong heaven and the heaven of heavens, the earth and all that is in it.",
      "M": "To the LORD your God belong the heavens, even the highest heavens, the earth and everything in it.",
      "T": "The heavens — even the highest heavens — belong to the LORD your God. The earth and everything it contains is his."
    },
    "15": {
      "L": "Yet the LORD set his heart in love on your fathers and chose their offspring after them — you above all peoples — as you are this day.",
      "M": "Yet the LORD delighted in your fathers and loved them, and he chose you, their descendants, above all peoples — as it is today.",
      "T": "And yet — the LORD set his love on your ancestors, delighting in them, and chose you, their descendants, out of all the peoples on earth. That is what today proves."
    },
    "16": {
      "L": "Circumcise therefore the foreskin of your heart, and be no longer stubborn.",
      "M": "So circumcise your hearts and stop being stubborn.",
      "T": "Circumcise your hearts — cut away the inner resistance that keeps you from full commitment to God. Stop being stiff-necked."
    },
    "17": {
      "L": "For the LORD your God is God of gods and Lord of lords, the great, the mighty, and the awesome God, who is not partial and takes no bribe.",
      "M": "For the LORD your God is God of gods and Lord of lords — the great, mighty, and awesome God who shows no partiality and accepts no bribe.",
      "T": "The LORD your God is the supreme God, sovereign over all lords — the great, the powerful, the awe-inspiring One who plays no favorites and cannot be bought."
    },
    "18": {
      "L": "He executes justice for the fatherless and the widow, and loves the sojourner, giving him food and clothing.",
      "M": "He upholds justice for the fatherless and the widow, and loves the foreigner, providing them with food and clothing.",
      "T": "He secures justice for the orphan and the widow. He loves the foreigner — providing them food and clothing. This is what the supreme God does with his power."
    },
    "19": {
      "L": "Love the sojourner therefore, for you were sojourners in the land of Egypt.",
      "M": "So love the foreigner, for you were foreigners in the land of Egypt.",
      "T": "Therefore love the foreigner. You know exactly what it is to be an outsider — you lived it in Egypt."
    },
    "20": {
      "L": "The LORD your God you shall fear; him you shall serve and hold fast to him, and by his name you shall swear.",
      "M": "Fear the LORD your God. Serve him, hold fast to him, and take oaths in his name.",
      "T": "Revere the LORD your God. Serve him. Cling to him. When you make solemn oaths, invoke his name alone."
    },
    "21": {
      "L": "He is your praise and he is your God, who has done for you these great and terrifying things that your eyes have seen.",
      "M": "He is your praise and he is your God — the one who has done these great and awe-inspiring things for you that your own eyes have seen.",
      "T": "He is the one you praise; he is your God — the one whose great, overwhelming acts your own eyes have witnessed."
    },
    "22": {
      "L": "Your fathers went down to Egypt seventy persons, and now the LORD your God has made you as numerous as the stars of heaven.",
      "M": "Your fathers went down to Egypt as seventy people, and now the LORD your God has made you as numerous as the stars of the sky.",
      "T": "Seventy people went down to Egypt. Now the LORD your God has made you as countless as the stars in the sky. From seventy to a nation — that is what he has done."
    }
  },
  "11": {
    "1": {
      "L": "You shall therefore love the LORD your God and keep his charge, his statutes, his rules, and his commandments always.",
      "M": "Love the LORD your God and always keep his requirements, his statutes, his ordinances, and his commandments.",
      "T": "Love the LORD your God. Keep his requirements, his statutes, his ordinances, his commandments — always."
    },
    "2": {
      "L": "And consider today — since I am not speaking to your children who have not known or seen it — the discipline of the LORD your God, his greatness, his mighty hand and his outstretched arm,",
      "M": "Know today — I am not speaking to your children who have not known or seen it — but know the discipline of the LORD your God: his greatness, his mighty hand, and his outstretched arm,",
      "T": "Understand this today — I am addressing you, not your children who have no firsthand memory — you know the LORD's discipline: his greatness, his powerful hand, his outstretched arm,"
    },
    "3": {
      "L": "his signs and his deeds that he did in Egypt to Pharaoh the king of Egypt and to all his land,",
      "M": "his signs and deeds that he performed in Egypt against Pharaoh king of Egypt and all his land,",
      "T": "his signs and mighty acts performed in Egypt against Pharaoh and his whole land,"
    },
    "4": {
      "L": "and what he did to the army of Egypt, to their horses and to their chariots — how he made the water of the Red Sea flow over them as they pursued after you, and how the LORD has destroyed them to this day —",
      "M": "and what he did to Egypt's army, its horses and chariots — how he caused the waters of the Red Sea to engulf them as they chased you, and how the LORD has defeated them permanently —",
      "T": "and what he did to the Egyptian army, their horses and chariots — how the waters of the Red Sea crashed over them as they pursued you, and how the LORD has kept them destroyed to this very day —"
    },
    "5": {
      "L": "and what he did to you in the wilderness until you came to this place,",
      "M": "and what he did to you in the wilderness until you reached this place,",
      "T": "and what he did to sustain and discipline you through the wilderness until you arrived here —"
    },
    "6": {
      "L": "and what he did to Dathan and Abiram the sons of Eliab, son of Reuben — how the earth opened its mouth and swallowed them, with their households and their tents and every living thing that followed them, in the midst of all Israel —",
      "M": "and what he did to Dathan and Abiram sons of Eliab son of Reuben — how the earth split open and swallowed them, along with their households, tents, and every living creature with them, before all Israel —",
      "T": "and what he did to Dathan and Abiram, those sons of Eliab of Reuben — how the earth opened its mouth and swallowed them, their households, their tents, every living creature with them, while all Israel watched —"
    },
    "7": {
      "L": "but your eyes have seen all the great work of the LORD that he did.",
      "M": "your own eyes saw every great act the LORD performed.",
      "T": "your own eyes saw it all. Every great act the LORD performed — you were there."
    },
    "8": {
      "L": "You shall therefore keep the whole commandment that I command you today, that you may be strong and go in and possess the land that you are crossing over to possess,",
      "M": "Therefore keep every commandment I am commanding you today, so that you may be strong enough to cross over and take possession of the land you are going to possess,",
      "T": "So keep every commandment I am giving you today — all of it — so that you will have the strength to go in and possess the land you are crossing over to take."
    },
    "9": {
      "L": "and that you may live long in the land that the LORD swore to your fathers to give to them and to their offspring, a land flowing with milk and honey.",
      "M": "and that you may live long in the land the LORD swore to your fathers to give them and their descendants — a land flowing with milk and honey.",
      "T": "Long life in the land — that is the promise. The land flowing with milk and honey that the LORD swore to your ancestors. Keep the commands and inherit both the land and the years."
    },
    "10": {
      "L": "For the land that you are entering to possess is not like the land of Egypt, from which you have come, where you sowed your seed and irrigated it like a garden of vegetables.",
      "M": "The land you are entering to possess is not like Egypt, from which you have come, where you planted your seed and irrigated it by foot like a vegetable garden.",
      "T": "The land you are entering is nothing like Egypt, where you sowed seed and irrigated it by foot — running water through channels like a vegetable garden, entirely by human effort."
    },
    "11": {
      "L": "But the land that you are going over to possess is a land of hills and valleys, which drinks water by the rain from heaven,",
      "M": "But the land you are crossing over to possess is a land of hills and valleys that drinks in the rain from heaven.",
      "T": "The land you are crossing into is a land of hills and valleys that drinks its water straight from heaven's rain."
    },
    "12": {
      "L": "a land that the LORD your God cares for. The eyes of the LORD your God are always on it, from the beginning of the year to the end of the year.",
      "M": "It is a land the LORD your God continually watches over. The eyes of the LORD your God are on it from the beginning of the year to its end.",
      "T": "This is a land the LORD your God personally tends and watches over. His eyes are on it from the first day of the year to the last. It is a land of dependence on him — not human irrigation, but his gift of rain."
    },
    "13": {
      "L": "And if you will indeed listen to my commandments that I command you today, to love the LORD your God and to serve him with all your heart and with all your soul,",
      "M": "If you carefully obey the commandments I am giving you today — to love the LORD your God and to serve him with all your heart and with all your soul —",
      "T": "If you truly listen to the commandments I give you today — genuinely loving the LORD your God and serving him with your whole heart and your whole self —"
    },
    "14": {
      "L": "he will give the rain for your land in its season, the early rain and the later rain, that you may gather in your grain and your wine and your oil.",
      "M": "then he will send rain on your land at the right time — the autumn rains and the spring rains — so you can harvest your grain, new wine, and olive oil.",
      "T": "he will send your land rain in the right seasons — the early autumn rains and the late spring rains — so that you harvest your grain, your wine, your oil."
    },
    "15": {
      "L": "And he will give grass in your fields for your livestock, and you shall eat and be full.",
      "M": "He will provide grass in your fields for your livestock, and you will eat and be satisfied.",
      "T": "He will grow grass in your fields for your animals, and you will eat and be satisfied. The land will feed you — if you are faithful to him."
    },
    "16": {
      "L": "Take care lest your heart be deceived, and you turn aside and serve other gods and worship them,",
      "M": "Be careful that you are not led astray so that you turn aside, serve other gods, and bow down to them.",
      "T": "Guard yourselves. Do not let your hearts be seduced into turning aside to serve and worship other gods."
    },
    "17": {
      "L": "lest the anger of the LORD be kindled against you, and he shut up the heavens so that there is no rain, and the land yields no fruit, and you perish quickly from the good land the LORD is giving you.",
      "M": "Otherwise the LORD's anger will burn against you; he will shut up the sky so that there is no rain, the land will produce no crops, and you will quickly perish from the good land the LORD is giving you.",
      "T": "If you do, the LORD's anger will blaze against you — he will lock up the sky, stop the rain, the land will bear nothing, and you will quickly vanish from the good land the LORD is giving you."
    },
    "18": {
      "L": "You shall therefore lay up these words of mine in your heart and in your soul, and you shall bind them as a sign on your hand, and they shall be as frontlets between your eyes.",
      "M": "Impress these words of mine on your hearts and minds. Tie them as a symbol on your hands and bind them on your foreheads.",
      "T": "Take these words and drive them deep into your heart and your whole being. Bind them on your hands as a visible sign. Fix them between your eyes — make them a constant presence."
    },
    "19": {
      "L": "You shall teach them to your children, talking of them when you sit in your house, and when you walk by the way, and when you lie down, and when you rise.",
      "M": "Teach them to your children by talking about them when you sit at home, when you walk along the road, when you lie down, and when you get up.",
      "T": "Teach them to your children — talk about them at home, on the road, at bedtime, in the morning. Total formation: every moment, every setting."
    },
    "20": {
      "L": "You shall write them on the doorposts of your house and on your gates,",
      "M": "Write them on the doorframes of your houses and on your gates,",
      "T": "Write them on your doorposts and your gates — let them mark every threshold, every entrance and exit of your life."
    },
    "21": {
      "L": "that your days and the days of your children may be multiplied in the land that the LORD swore to your fathers to give them, as long as the heavens are above the earth.",
      "M": "so that you and your children may enjoy long life in the land the LORD swore to your fathers to give them — as long as the heavens are above the earth.",
      "T": "Do this, and your days in the land the LORD promised your ancestors will stretch as long as the sky stretches above the earth."
    },
    "22": {
      "L": "For if you will be careful to keep all this commandment that I command you to do, loving the LORD your God, walking in all his ways, and holding fast to him,",
      "M": "For if you carefully observe all this command that I am giving you — to love the LORD your God, to walk in all his ways, and to hold fast to him —",
      "T": "If you diligently keep every commandment I give you — loving the LORD your God, walking in all his ways, clinging to him —"
    },
    "23": {
      "L": "then the LORD will drive out all these nations before you, and you will dispossess nations greater and mightier than yourselves.",
      "M": "then the LORD will drive out all these nations before you, and you will dispossess nations greater and more powerful than you.",
      "T": "then the LORD will drive every one of these nations out before you, and you will displace peoples stronger and larger than yourselves."
    },
    "24": {
      "L": "Every place on which the sole of your foot treads shall be yours. Your territory shall be from the wilderness to Lebanon and from the River, the Euphrates, to the western sea.",
      "M": "Every place where you set your foot will be yours. Your borders will extend from the wilderness to Lebanon and from the Euphrates River to the Mediterranean Sea.",
      "T": "Everywhere you walk will be yours. Your land will stretch from the wilderness to Lebanon, from the Euphrates River to the sea in the west."
    },
    "25": {
      "L": "No one shall be able to stand against you. The LORD your God will put the fear of you and the dread of you on all the land that you tread, as he promised you.",
      "M": "No one will be able to stand against you. The LORD your God will cause all the peoples of the land you walk through to fear and dread you, as he has told you.",
      "T": "No one will stand in your way. The LORD your God will spread fear and dread of you over every land you walk through — exactly as he has promised."
    },
    "26": {
      "L": "See, I am setting before you today a blessing and a curse:",
      "M": "See, I am placing before you today a blessing and a curse:",
      "T": "Today I set before you two roads: a blessing and a curse."
    },
    "27": {
      "L": "the blessing, if you obey the commandments of the LORD your God, which I command you today,",
      "M": "The blessing will come if you obey the commandments of the LORD your God that I am giving you today.",
      "T": "The blessing falls on you if you obey the commandments of the LORD your God that I give you today."
    },
    "28": {
      "L": "and the curse, if you do not obey the commandments of the LORD your God, but turn aside from the way that I am commanding you today, to go after other gods that you have not known.",
      "M": "The curse will come if you do not obey the commandments of the LORD your God, and turn from the way I am commanding you today to follow other gods you have not known.",
      "T": "The curse falls on you if you refuse to obey the LORD your God's commandments, turning off the road I set before you today to chase after gods you have never known."
    },
    "29": {
      "L": "And when the LORD your God brings you into the land that you are entering to possess, you shall set the blessing on Mount Gerizim and the curse on Mount Ebal.",
      "M": "When the LORD your God brings you into the land you are entering to possess, you are to proclaim the blessing from Mount Gerizim and the curse from Mount Ebal.",
      "T": "When the LORD your God brings you into the land, you are to ratify this choice on the landscape itself: proclaim the blessing from Mount Gerizim and the curse from Mount Ebal."
    },
    "30": {
      "L": "Are they not beyond the Jordan, west of the road, toward the going down of the sun, in the land of the Canaanites who live in the Arabah, opposite Gilgal, beside the oak of Moreh?",
      "M": "Are these mountains not west of the Jordan, along the road toward the sunset, in the territory of the Canaanites living in the Arabah, near Gilgal, beside the great trees of Moreh?",
      "T": "These mountains are beyond the Jordan — west of the road, toward the setting sun, in the Canaanite territory of the Arabah, near Gilgal, by the oak of Moreh. You will know the place."
    },
    "31": {
      "L": "For you are crossing over the Jordan to go in to possess the land that the LORD your God is giving you. And when you possess it and live in it,",
      "M": "You are about to cross the Jordan to enter and possess the land the LORD your God is giving you. When you take possession of it and settle there,",
      "T": "You are crossing the Jordan to take possession of the land the LORD your God is giving you. When you hold it and settle in it,"
    },
    "32": {
      "L": "you shall be careful to observe all the statutes and the rules that I am setting before you today.",
      "M": "be careful to observe all the statutes and ordinances I am setting before you today.",
      "T": "observe every statute and ordinance I am placing before you today. All of them."
    }
  },
  "12": {
    "1": {
      "L": "These are the statutes and the rules that you shall be careful to do in the land that the LORD, the God of your fathers, has given you to possess, all the days that you live on the earth.",
      "M": "These are the statutes and ordinances you must carefully observe in the land that the LORD, the God of your fathers, has given you to possess — for as long as you live on the earth.",
      "T": "These are the statutes and ordinances you must live by in the land the LORD, the God of your ancestors, has given you to possess — for every day you live on this earth."
    },
    "2": {
      "L": "You shall surely destroy all the places where the nations whom you shall dispossess served their gods, on the high mountains and on the hills and under every green tree.",
      "M": "Completely destroy all the places where the nations you are dispossessing served their gods — on high mountains, on hills, and under every spreading tree.",
      "T": "Completely demolish every site where the nations you displace worshipped their gods — on every high mountain, every hill, beneath every spreading green tree."
    },
    "3": {
      "L": "You shall tear down their altars and shatter their sacred pillars and burn their Asherah poles with fire. You shall chop down the carved images of their gods and destroy their name out of that place.",
      "M": "Tear down their altars, smash their sacred pillars, burn their Asherah poles, and cut down their carved idols. Wipe out the very name of their gods from those places.",
      "T": "Tear down their altars. Smash their sacred stones. Burn their Asherah poles to ash. Chop down their carved idols. Erase every trace of their gods' names from those places."
    },
    "4": {
      "L": "You shall not worship the LORD your God in that way.",
      "M": "You must not worship the LORD your God in the same way as these nations worship their gods.",
      "T": "Do not worship the LORD your God the way these nations worship theirs. The method matters — not just the object."
    },
    "5": {
      "L": "But you shall seek the place that the LORD your God will choose out of all your tribes to put his name and make his habitation there. There you shall go,",
      "M": "Instead, you are to seek the place the LORD your God will choose from among all your tribes to establish his name and make his dwelling. You must go there",
      "T": "Instead, seek the one place the LORD your God will choose from among all your tribes — the place where he will set his name and establish his presence. Go there,"
    },
    "6": {
      "L": "and there you shall bring your burnt offerings and your sacrifices, your tithes and the contribution that you present, your vow offerings, your freewill offerings, and the firstborn of your herd and of your flock.",
      "M": "and there bring your burnt offerings and sacrifices, your tithes and special gifts, your vow offerings and freewill offerings, and the firstborn of your herds and flocks.",
      "T": "and bring there everything: your burnt offerings and sacrifices, your tithes and contributions, your vow offerings and freewill offerings, the firstborn of your herds and flocks."
    },
    "7": {
      "L": "And there you shall eat before the LORD your God, and you shall rejoice, you and your households, in all that you undertake, in which the LORD your God has blessed you.",
      "M": "There you shall eat in the presence of the LORD your God and rejoice, you and your households, in everything you have undertaken, because the LORD your God has blessed you.",
      "T": "There you will eat in the LORD's presence and celebrate — you and your whole household — over everything you have worked for, because the LORD your God has blessed it."
    },
    "8": {
      "L": "You shall not do according to all that we are doing here today, everyone doing whatever is right in his own eyes,",
      "M": "You are not to act as we act here today, with everyone doing as he sees fit,",
      "T": "Stop doing what we are doing now — everyone acting on their own judgment about what seems right."
    },
    "9": {
      "L": "for you have not as yet come to the rest and to the inheritance that the LORD your God is giving you.",
      "M": "because you have not yet reached the rest and the inheritance the LORD your God is giving you.",
      "T": "We are in transit — you have not yet entered the rest and the inheritance the LORD your God is giving you. That changes everything."
    },
    "10": {
      "L": "But when you go over the Jordan and live in the land that the LORD your God is giving you to inherit, and when he gives you rest from all your enemies around you, so that you live in safety,",
      "M": "When you cross the Jordan and settle in the land the LORD your God is giving you as your inheritance, and he gives you rest from all the enemies surrounding you so that you live in security,",
      "T": "But once you cross the Jordan and settle in the land the LORD your God is giving you, when he grants you rest from all your enemies and you live in real security —"
    },
    "11": {
      "L": "then to the place that the LORD your God will choose, to make his name dwell there, there you shall bring all that I command you: your burnt offerings and your sacrifices, your tithes and the contribution that you present, and all your choice vow offerings that you vow to the LORD.",
      "M": "then bring everything I command you to the place the LORD your God will choose as a dwelling for his name: your burnt offerings and sacrifices, your tithes and special gifts, and all your finest vow offerings that you dedicate to the LORD.",
      "T": "then bring everything I command to the one place the LORD chooses as the home of his name: burnt offerings, sacrifices, tithes, contributions — all your best vow offerings dedicated to the LORD."
    },
    "12": {
      "L": "And you shall rejoice before the LORD your God, you and your sons and your daughters, your male servants and your female servants, and the Levite who is within your gates, since he has no portion or inheritance with you.",
      "M": "Rejoice before the LORD your God — you, your sons and daughters, your male and female servants, and the Levites in your towns, since they have no portion or inheritance among you.",
      "T": "And celebrate before the LORD your God — you, your sons and daughters, your servants, and especially the Levites in your towns, since they hold no land of their own. Include them."
    },
    "13": {
      "L": "Take care that you do not offer your burnt offerings at any place that you see,",
      "M": "Be careful not to offer your burnt offerings at just any place you happen to see.",
      "T": "Guard against this: do not offer burnt offerings at whatever location strikes you as convenient."
    },
    "14": {
      "L": "but only at the place that the LORD will choose in one of your tribes. There you shall offer your burnt offerings and there you shall do all that I am commanding you.",
      "M": "Offer them only at the place the LORD will choose in one of your tribal territories. Everything I command you, you are to do there.",
      "T": "Do it only at the place the LORD chooses — one place, in the territory of one tribe. Every act of worship I am commanding belongs there."
    },
    "15": {
      "L": "However, you may slaughter and eat meat within any of your towns, as much as you desire, according to the blessing of the LORD your God that he has given you. The unclean and the clean may eat of it, as of the gazelle and as of the deer.",
      "M": "Nevertheless, you may slaughter your animals and eat meat in any of your towns, as much as you want, based on the blessing the LORD your God has given you. Both the ceremonially unclean and the clean may eat it, as they would the gazelle or deer.",
      "T": "That said, you may butcher and eat meat whenever you wish, in any of your towns — as much as the LORD your God has blessed you with. Ritual purity is not required for ordinary meals: unclean and clean alike may eat, the same as gazelle or deer."
    },
    "16": {
      "L": "Only you shall not eat the blood. You shall pour it out on the earth like water.",
      "M": "But you must never eat the blood. Pour it out on the ground like water.",
      "T": "One absolute: never eat the blood. Pour it on the ground like water."
    },
    "17": {
      "L": "You may not eat within your towns the tithe of your grain or of your wine or of your oil, or the firstborn of your herd or of your flock, or any of your vow offerings that you vow, or your freewill offerings or the contribution that you present,",
      "M": "But within your own towns you may not eat the tithe of your grain, new wine, or olive oil, or the firstborn of your herds and flocks, or any offering you have vowed, or your freewill offerings or special gifts.",
      "T": "But the tithe of your grain, your wine, your oil; the firstborn of herd and flock; your vow offerings, freewill offerings, contributions — none of these are for eating at home in your towns."
    },
    "18": {
      "L": "but you shall eat them before the LORD your God in the place that the LORD your God will choose, you and your son and your daughter, your male servant and your female servant, and the Levite who is within your gates. And you shall rejoice before the LORD your God in all that you undertake.",
      "M": "Instead, eat them in the presence of the LORD your God at the place the LORD your God will choose — you, your son and daughter, your male and female servant, and the Levite in your town. Rejoice before the LORD your God in everything you do.",
      "T": "These belong at the chosen place — eaten before the LORD your God: you, your children, your servants, and the Levite in your town. Let it be a celebration in the LORD's presence for all that you have worked on."
    },
    "19": {
      "L": "Take care that you do not neglect the Levite as long as you live in your land.",
      "M": "Be careful not to neglect the Levite as long as you live in your land.",
      "T": "Make sure the Levite is never left out. He has no land. As long as you are in this land, that responsibility is yours."
    },
    "20": {
      "L": "When the LORD your God enlarges your territory, as he has promised you, and you say, 'I will eat meat,' because you crave meat, you may eat meat whenever you desire.",
      "M": "When the LORD your God extends your territory as he has promised, and you desire to eat meat because you crave it, you may eat meat whenever you wish.",
      "T": "When the LORD your God expands your territory, as he has promised, and you feel the desire for meat — go ahead, eat meat as often as you like."
    },
    "21": {
      "L": "If the place that the LORD your God will choose to put his name there is too far from you, then you may slaughter any of your herd or flock that the LORD has given you, as I have commanded you, and you may eat within your towns whenever you desire.",
      "M": "If the place where the LORD your God will establish his name is too far away, you may slaughter from your herd or flock that the LORD has given you, as I have instructed you, and eat as much as you want in your towns.",
      "T": "If the chosen sanctuary is simply too far from you, then slaughter from your herds and flocks — the ones the LORD has given you — following my instructions, and eat your fill at home in your towns."
    },
    "22": {
      "L": "Just as the gazelle or the deer is eaten, so you may eat of it. The unclean and the clean alike may eat of it.",
      "M": "Eat it as you would gazelle or deer. Both the ceremonially unclean and the clean may eat it.",
      "T": "Eat it the same as you would venison — gazelle or deer. Clean and unclean alike may share in this ordinary meal."
    },
    "23": {
      "L": "Only be sure that you do not eat the blood, for the blood is the life, and you shall not eat the life with the flesh.",
      "M": "But do not eat the blood, because the blood is the life-force, and you must not eat the life along with the flesh.",
      "T": "But the blood — never. The blood carries the life-force of the creature. Do not consume the life together with the flesh. These are kept distinct."
    },
    "24": {
      "L": "You shall not eat it. You shall pour it out on the earth like water.",
      "M": "Do not eat it. Pour it out on the ground like water.",
      "T": "Don't eat it. Pour it out on the ground like water — return the life to the earth."
    },
    "25": {
      "L": "You shall not eat it, that all may go well with you and with your children after you, when you do what is right in the sight of the LORD.",
      "M": "Do not eat it, so that it may go well with you and with your children after you, when you do what is right in the LORD's sight.",
      "T": "Obey this, and things will go well with you and your children after you — because you are doing what is right before the LORD."
    },
    "26": {
      "L": "Only the holy things that are due from you, and your vow offerings, you shall take and go to the place that the LORD will choose.",
      "M": "But take your sacred gifts and vow offerings and go to the place the LORD will choose.",
      "T": "Any sacred gifts and vow offerings you have set apart — take them to the place the LORD will choose."
    },
    "27": {
      "L": "And you shall offer your burnt offerings, the flesh and the blood, on the altar of the LORD your God. The blood of your sacrifices shall be poured out on the altar of the LORD your God, and you shall eat the flesh.",
      "M": "Present your burnt offerings — both the flesh and the blood — on the altar of the LORD your God. The blood of your other sacrifices must be poured out beside the altar, but you may eat the flesh.",
      "T": "Offer your burnt offerings — flesh and blood both — on the LORD's altar. For other sacrifices, pour the blood out against the altar; the flesh is yours to eat."
    },
    "28": {
      "L": "Be careful to obey all these words that I command you, that it may go well with you and with your children after you forever, when you do what is good and right in the sight of the LORD your God.",
      "M": "Be careful to obey all these commands I give you, so that it may always go well with you and with your descendants, because you are doing what is good and right in the sight of the LORD your God.",
      "T": "Obey all these commands carefully. That is the path to lasting wellbeing — for you and for your children after you forever — when you do what is good and right before the LORD your God."
    },
    "29": {
      "L": "When the LORD your God cuts off before you the nations that you go in to dispossess, and you dispossess them and dwell in their land,",
      "M": "When the LORD your God has cut off the nations you are going to dispossess and you have driven them out and settled in their land,",
      "T": "When the LORD your God has swept away the nations before you, and you have displaced them and settled in their land,"
    },
    "30": {
      "L": "take care that you are not ensnared to follow them, after they have been destroyed before you, and that you do not inquire about their gods, saying, 'How did these nations serve their gods? — that I also may do the same.'",
      "M": "be careful that you are not drawn into following them after they have been destroyed before you. Do not inquire about their gods and say, 'How did these nations worship their gods? I will do the same.'",
      "T": "guard yourself against being drawn into imitating them — even after they are gone. Do not ask: 'How did they worship their gods? I want to do the same.' That question is already the trap."
    },
    "31": {
      "L": "You shall not worship the LORD your God in that way, for every abominable thing that the LORD hates they have done for their gods, for they even burn their sons and their daughters in the fire to their gods.",
      "M": "You must not worship the LORD your God in the way they worshipped theirs, because they practiced every detestable thing the LORD hates in the service of their gods — they even burned their sons and daughters as offerings to their gods.",
      "T": "Do not worship the LORD your God the way they worship theirs. These nations did every abominable thing the LORD detests in their religious practice — they burned their own sons and daughters as offerings. This is the end of that road."
    },
    "32": {
      "L": "Everything that I command you, you shall be careful to do. You shall not add to it or take from it.",
      "M": "Everything that I command you, be careful to do. Do not add to it or subtract from it.",
      "T": "Whatever I command you — keep it. Do not add one thing. Do not remove one thing."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'deuteronomy')
        merge_tier(existing, DEUTERONOMY, tier_key)
        save(tier_dir, 'deuteronomy', existing)
    print('Deuteronomy 7–12 written.')

if __name__ == '__main__':
    main()
