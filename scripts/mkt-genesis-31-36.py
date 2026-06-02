"""
MKT Genesis chapters 31–36 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-genesis-31-36.py

Translation principles applied:
- H3068 יהוה → "the LORD" (all tiers)
- H430 אֱלֹהִים → "God"
- H2617 חֶסֶד → "steadfast love" (L), "unfailing love" (M), "covenant faithfulness" (T)
- H1285 בְּרִית → "covenant" (all tiers)
- פַּחַד יִצְחָק (31:42,53) → "the Fear of Isaac" (L); "the Awe of Isaac" (M/T) — a divine title
- יִשְׂרָאֵל (32:28) → T tier glosses the etymology explicitly
- פְּנִיאֵל / פְּנוּאֵל (32:30-31) → T tier glosses "face of God"
- Gen 33:10 deliberately echoes Peniel — T tier notes this
- Gen 35:18 Ben-oni/Benjamin: T tier preserves both names with meaning
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

GENESIS = {
  "31": {
    "1": {
      "L": "Now Jacob heard that the sons of Laban were saying, 'Jacob has taken all that was our father's, and from what was our father's he has gained all this wealth.'",
      "M": "Jacob heard that Laban's sons were saying, 'Jacob has taken everything our father owned and has gained all this wealth from what belonged to our father.'",
      "T": "Word reached Jacob that Laban's sons were grumbling: 'Jacob has stripped our father of everything. All this wealth of his came from what belonged to our father.'"
    },
    "2": {
      "L": "And Jacob saw that Laban did not regard him with favor as before.",
      "M": "And Jacob noticed that Laban's attitude toward him was not what it had been.",
      "T": "Jacob also saw that Laban no longer looked at him the way he once had."
    },
    "3": {
      "L": "Then the LORD said to Jacob, 'Return to the land of your fathers and to your kindred, and I will be with you.'",
      "M": "Then the LORD said to Jacob, 'Go back to the land of your fathers and to your relatives, and I will be with you.'",
      "T": "Then the LORD said to Jacob, 'Return to the land of your fathers and to your family. I will be with you.'"
    },
    "4": {
      "L": "So Jacob sent and called Rachel and Leah into the field where his flock was",
      "M": "So Jacob sent word to Rachel and Leah to come out to the fields where his flocks were.",
      "T": "So Jacob sent for Rachel and Leah to meet him in the fields where his flocks were."
    },
    "5": {
      "L": "and said to them, 'I see that your father does not regard me with favor as he did before. But the God of my father has been with me.'",
      "M": "He said to them, 'I see that your father's attitude toward me is not what it was before, but the God of my father has been with me.'",
      "T": "'I can see that your father's attitude toward me has changed,' he said. 'But the God of my father has been with me through all of this.'"
    },
    "6": {
      "L": "'You know that I have served your father with all my strength,'",
      "M": "'You know that I've worked for your father with all my strength,'",
      "T": "'You know how hard I have worked for your father—I gave him everything I had.'"
    },
    "7": {
      "L": "'yet your father has cheated me and changed my wages ten times. But God did not permit him to harm me.'",
      "M": "'yet your father has cheated me by changing my wages ten times. However, God has not allowed him to harm me.'",
      "T": "'Yet your father has cheated me and changed my wages ten times over. But God has not allowed him to actually harm me.'"
    },
    "8": {
      "L": "'If he said, \"The speckled shall be your wages,\" then all the flock bore speckled; and if he said, \"The striped shall be your wages,\" then all the flock bore striped.'",
      "M": "'If he said, \"The speckled ones will be your wages,\" then all the flocks gave birth to speckled young; and if he said, \"The streaked ones will be your wages,\" then all the flocks bore streaked young.'",
      "T": "'Whenever he said the speckled ones would be my wages, all the flock produced speckled young. Whenever he said the striped ones would be mine, all the flock produced striped young.'"
    },
    "9": {
      "L": "'Thus God has taken away the livestock of your father and given them to me.'",
      "M": "'So God has taken away your father's livestock and has given them to me.'",
      "T": "'In this way God has been transferring your father's livestock to me.'"
    },
    "10": {
      "L": "'In the breeding season of the flock I lifted up my eyes and saw in a dream that the goats that mated with the flock were striped, speckled, and mottled.'",
      "M": "'In breeding season I once had a dream in which I looked up and saw that the male goats mating with the flock were streaked, speckled or spotted.'",
      "T": "'Once during the breeding season I had a dream. I looked up and saw that all the male goats mating with the flock were streaked, speckled, and spotted.'"
    },
    "11": {
      "L": "'Then the angel of God said to me in the dream, \"Jacob,\" and I said, \"Here I am!\"'",
      "M": "'The angel of God said to me in the dream, \"Jacob.\" I answered, \"Yes.\"'",
      "T": "'Then the angel of God called to me in the dream: \"Jacob!\" I answered, \"Yes, I am here!\"'"
    },
    "12": {
      "L": "'And he said, \"Lift up your eyes and see, all the goats that mate with the flock are striped, speckled, and mottled, for I have seen all that Laban is doing to you.\"'",
      "M": "'He said, \"Look up and see that all the male goats mating with the flock are streaked, speckled or spotted, for I have seen all that Laban has been doing to you.\"'",
      "T": "'He said, \"Look—all the males mating with your flocks are streaked, speckled, and spotted. I have seen everything Laban has been doing to you.\"'"
    },
    "13": {
      "L": "'\"I am the God of Bethel, where you anointed a pillar and made a vow to me. Now arise, go out from this land and return to the land of your kindred.\"'",
      "M": "'\"I am the God of Bethel, where you anointed a pillar and where you made a vow to me. Now leave this land at once and go back to your native land.\"'",
      "T": "'\"I am the God of Bethel—the place where you poured oil on a pillar and made your vow to me. Now get up, leave this land, and return to the land where you were born.\"'"
    },
    "14": {
      "L": "Then Rachel and Leah answered and said to him, 'Is there any portion or inheritance left to us in our father's house?'",
      "M": "Then Rachel and Leah replied, 'Do we still have any share in the inheritance of our father's estate?'",
      "T": "Rachel and Leah answered him, 'Is there anything left for us in our father's house? Do we have any inheritance there?'"
    },
    "15": {
      "L": "'Are we not regarded by him as foreigners? For he has sold us, and he has indeed devoured our money.'",
      "M": "'Does he not regard us as foreigners? Not only has he sold us, but he has used up what was paid for us.'",
      "T": "'He treats us as outsiders—as foreigners! He sold us and then squandered the money that should have been ours.'"
    },
    "16": {
      "L": "'All the wealth that God has taken away from our father belongs to us and to our children. Now then, whatever God has said to you, do.'",
      "M": "'Surely all the wealth that God took away from our father belongs to us and our children. So do whatever God has told you.'",
      "T": "'All the wealth God has transferred from our father to you rightfully belongs to us and our children anyway. Do whatever God has told you to do.'"
    },
    "17": {
      "L": "So Jacob arose and set his sons and his wives on camels.",
      "M": "Then Jacob put his children and his wives on camels,",
      "T": "So Jacob loaded his children and wives onto camels"
    },
    "18": {
      "L": "He drove away all his livestock, all his property that he had gained, the livestock in his possession that he had acquired in Paddan-aram, to go to the land of Canaan to his father Isaac.",
      "M": "and he drove all his livestock ahead of him, along with all the goods he had accumulated in Paddan Aram, to go to his father Isaac in the land of Canaan.",
      "T": "and drove all his livestock and everything he had acquired in Paddan-aram ahead of him, heading for the land of Canaan to his father Isaac."
    },
    "19": {
      "L": "Laban had gone to shear his sheep, and Rachel stole her father's household gods.",
      "M": "When Laban had gone to shear his sheep, Rachel stole her father's household gods.",
      "T": "Laban had gone out to shear his sheep, and while he was away, Rachel stole her father's household gods."
    },
    "20": {
      "L": "And Jacob tricked Laban the Aramean, by not telling him that he intended to flee.",
      "M": "Moreover, Jacob deceived Laban the Aramean by not telling him he was running away.",
      "T": "Jacob also kept his departure secret from Laban—he gave no warning that he was about to flee."
    },
    "21": {
      "L": "He fled with all that he had and arose and crossed the Euphrates, and set his face toward the hill country of Gilead.",
      "M": "So he fled with all he had, crossed the Euphrates River, and headed for the hill country of Gilead.",
      "T": "So he fled with everything he had, crossed the Euphrates, and headed toward the hill country of Gilead."
    },
    "22": {
      "L": "When it was told Laban on the third day that Jacob had fled,",
      "M": "On the third day Laban was told that Jacob had fled.",
      "T": "Three days later, Laban got word that Jacob had run away."
    },
    "23": {
      "L": "he took his kinsmen with him and pursued him for seven days and followed close after him into the hill country of Gilead.",
      "M": "Taking his relatives with him, he pursued Jacob for seven days and caught up with him in the hill country of Gilead.",
      "T": "He took his relatives with him and pursued Jacob for seven days, finally catching up with him in the hill country of Gilead."
    },
    "24": {
      "L": "But God came to Laban the Aramean in a dream by night and said to him, 'Be careful not to say anything to Jacob, either good or bad.'",
      "M": "Then God came to Laban the Aramean in a dream at night and said to him, 'Be careful not to say anything to Jacob, either good or bad.'",
      "T": "But that night God came to Laban the Aramean in a dream and said, 'Be very careful not to say anything to Jacob, whether good or bad.'"
    },
    "25": {
      "L": "And Laban overtook Jacob. Now Jacob had pitched his tent in the hill country, and Laban with his kinsmen pitched tents in the hill country of Gilead.",
      "M": "Laban caught up with Jacob, who had set up his tent in the hill country of Gilead, and Laban and his relatives camped there too.",
      "T": "Laban caught up with Jacob, who had pitched his camp in the hill country. Laban and his relatives set up camp in the same hill country of Gilead."
    },
    "26": {
      "L": "And Laban said to Jacob, 'What have you done, that you have tricked me and driven away my daughters like captives taken by the sword?'",
      "M": "Then Laban said to Jacob, 'What have you done? You've deceived me, and you've carried off my daughters like captives in war.'",
      "T": "Laban confronted Jacob: 'What have you done? You deceived me and sneaked my daughters away like prisoners of war!'"
    },
    "27": {
      "L": "'Why did you flee secretly and trick me, and did not tell me, so that I might have sent you away with mirth and songs, with tambourine and lyre?'",
      "M": "'Why did you run off secretly and deceive me? Why didn't you tell me, so I could send you away with joy and singing to the music of timbrels and harps?'",
      "T": "'Why did you sneak away without telling me? I would have sent you off with celebration—with singing, tambourines, and harps!'"
    },
    "28": {
      "L": "'And why did you not permit me to kiss my sons and my daughters farewell? Now you have done foolishly.'",
      "M": "'You didn't even let me kiss my grandchildren and my daughters goodbye. You have done a foolish thing.'",
      "T": "'You didn't even give me the chance to kiss my grandchildren and daughters farewell. What you have done is senseless!'"
    },
    "29": {
      "L": "'It is in my power to do you harm. But the God of your father spoke to me last night, saying, \"Be careful not to say anything to Jacob, either good or bad.\"'",
      "M": "'I have the power to harm you; but last night the God of your father said to me, \"Be careful not to say anything to Jacob, either good or bad.\"'",
      "T": "'I have the power to do you harm. But last night the God of your father warned me: \"Be careful—don't say a word to Jacob, whether good or bad.\"'"
    },
    "30": {
      "L": "'And now you have gone away because you longed greatly for your father's house, but why did you steal my gods?'",
      "M": "'Now you have gone off because you longed to return to your father's household. But why did you steal my gods?'",
      "T": "'I understand that you longed to go home to your father's household—but why did you steal my gods?'"
    },
    "31": {
      "L": "Jacob answered and said to Laban, 'Because I was afraid, for I thought that you would take your daughters from me by force.'",
      "M": "Jacob answered Laban, 'I was afraid, because I thought you would take your daughters away from me by force.'",
      "T": "Jacob answered, 'I was afraid. I thought you would take your daughters from me by force.'"
    },
    "32": {
      "L": "'Anyone with whom you find your gods shall not live. In the presence of our kinsmen point out what I have that is yours, and take it.' Now Jacob did not know that Rachel had stolen them.",
      "M": "'But if you find anyone who has your gods, that person shall not live. In the presence of our relatives, see for yourself whether I have anything of yours and take it.' Now Jacob did not know that Rachel had taken the gods.",
      "T": "'But as for your gods—if you find them with anyone here, that person will not live. Search in front of our relatives, and if anything belongs to you, take it.' Jacob did not know that Rachel had stolen them."
    },
    "33": {
      "L": "So Laban went into Jacob's tent and into Leah's tent and into the tent of the two female servants, but he did not find them. And he went out of Leah's tent and entered Rachel's tent.",
      "M": "So Laban went into Jacob's tent and into Leah's tent and into the tent of the two female servants, but he found nothing. After he came out of Leah's tent, he entered Rachel's tent.",
      "T": "Laban searched Jacob's tent, then Leah's, then the tents of both female servants—and found nothing. Then he went into Rachel's tent."
    },
    "34": {
      "L": "Now Rachel had taken the household gods and put them in the camel's saddle and sat on them. Laban felt all about the tent, but did not find them.",
      "M": "Now Rachel had taken the household gods and put them inside her camel's saddle and was sitting on them. Laban searched through everything in the tent but found nothing.",
      "T": "Rachel had taken the household gods, hidden them in the camel's saddlebag, and was sitting on them. Laban searched the whole tent and found nothing."
    },
    "35": {
      "L": "And she said to her father, 'Let not my lord be angry that I cannot rise before you, for the way of women is upon me.' So he searched but did not find the household gods.",
      "M": "Rachel said to her father, 'Don't be angry, my lord, that I cannot stand up in your presence; I'm having my period.' So he searched but could not find the household gods.",
      "T": "Rachel said to her father, 'Please don't be angry, my lord—I can't get up because I'm having my period.' So he kept searching but did not find the gods."
    },
    "36": {
      "L": "Then Jacob became angry and berated Laban. Jacob said to Laban, 'What is my offense? What is my sin, that you have hotly pursued me?'",
      "M": "Jacob was angry and took Laban to task. 'What is my crime?' he asked Laban. 'How have I wronged you that you hunt me down?'",
      "T": "Jacob's anger boiled over and he confronted Laban: 'What have I done wrong? What crime have I committed, that you have chased me down like this?'"
    },
    "37": {
      "L": "'For you have felt through all my goods; what have you found of all your household goods? Set it here before my kinsmen and your kinsmen, that they may decide between us two.'",
      "M": "'Now that you have searched through all my goods, what have you found that belongs to your household? Put it here in front of your relatives and mine, and let them judge between the two of us.'",
      "T": "'You have ransacked all my belongings—what have you found that is yours? Put it here in front of both our families and let them be the judge between us!'"
    },
    "38": {
      "L": "'These twenty years I have been with you. Your ewes and your female goats have not miscarried, and I have not eaten the rams of your flocks.'",
      "M": "'I have been with you for twenty years now. Your sheep and goats have not miscarried, nor have I eaten rams from your flocks.'",
      "T": "'I have served you faithfully for twenty years. Not one of your ewes or female goats has miscarried, and I have never eaten a ram from your flocks.'"
    },
    "39": {
      "L": "'What was torn by wild beasts I did not bring to you. I bore the loss of it myself. From my hand you required it, whether stolen by day or stolen by night.'",
      "M": "'I did not bring you animals torn by wild beasts; I bore the loss myself. And you held me responsible for whatever was stolen by day or night.'",
      "T": "'When an animal was torn by wild beasts, I absorbed the loss myself rather than pass it on to you. And you held me accountable for every animal stolen, day or night.'"
    },
    "40": {
      "L": "'There I was: by day the heat consumed me, and the cold by night, and my sleep fled from my eyes.'",
      "M": "'This was my situation: The heat consumed me in the daytime and the cold at night, and sleep fled from my eyes.'",
      "T": "'Day after day I endured the scorching heat, and night after night the bitter cold. Sleep was driven from my eyes.'"
    },
    "41": {
      "L": "'These twenty years I have been in your house. I served you fourteen years for your two daughters, and six years for your flock, and you have changed my wages ten times.'",
      "M": "'It was like this for the twenty years I was in your household. I worked for you fourteen years for your two daughters and six years for your flocks, and you changed my wages ten times.'",
      "T": "'For twenty years I worked in your household—fourteen years for your two daughters and six years for your flocks—and you changed my wages ten times over.'"
    },
    "42": {
      "L": "'If the God of my father, the God of Abraham and the Fear of Isaac, had not been on my side, surely now you would have sent me away empty-handed. God saw my affliction and the labor of my hands and rebuked you last night.'",
      "M": "'If the God of my father, the God of Abraham and the Awe of Isaac, had not been with me, you would surely have sent me away empty-handed. But God has seen my hardship and the toil of my hands, and last night he rebuked you.'",
      "T": "'If the God of my father—the God of Abraham and the Awesome God whom Isaac revered—had not been on my side, you would have sent me away with nothing. But God saw my suffering and the work of my hands, and last night he stepped in and rebuked you.'"
    },
    "43": {
      "L": "Then Laban answered and said to Jacob, 'The daughters are my daughters, the children are my children, the flocks are my flocks, and all that you see is mine. But what can I do this day for these my daughters or for their children whom they have borne?'",
      "M": "Laban answered Jacob, 'The women are my daughters, the children are my children, and the flocks are my flocks. All you see is mine. Yet what can I do today about these daughters of mine, or about the children they have borne?'",
      "T": "Laban answered, 'The women are my daughters, the children are my grandchildren, the flocks are my flocks—everything you see belongs to me. But what can I do now for my daughters and their children?'"
    },
    "44": {
      "L": "'Come now, let us make a covenant, you and I. And let it be a witness between you and me.'",
      "M": "'Come now, let's make a covenant, you and I, and let it serve as a witness between us.'",
      "T": "'Come—let us make a covenant, you and I, to serve as a witness between us.'"
    },
    "45": {
      "L": "So Jacob took a stone and set it up as a pillar.",
      "M": "So Jacob took a stone and set it up as a pillar.",
      "T": "So Jacob took a stone and set it upright as a memorial pillar."
    },
    "46": {
      "L": "And Jacob said to his kinsmen, 'Gather stones.' And they took stones and made a heap, and they ate there by the heap.",
      "M": "He said to his relatives, 'Gather some stones.' So they took stones and piled them in a heap, and they ate there by the heap.",
      "T": "He said to his relatives, 'Gather stones.' They gathered stones and made a pile, then shared a meal together beside it."
    },
    "47": {
      "L": "Laban called it Jegar-sahadutha, but Jacob called it Galeed.",
      "M": "Laban called it Jegar Sahadutha, and Jacob called it Galeed.",
      "T": "Laban named it Jegar-sahadutha in Aramaic; Jacob named it Galeed in Hebrew—both mean 'Witness Heap.'"
    },
    "48": {
      "L": "Laban said, 'This heap is a witness between you and me today.' Therefore he named it Galeed,",
      "M": "Laban said, 'This heap is a witness between you and me today.' That is why it was called Galeed.",
      "T": "Laban said, 'This pile of stones stands as a witness between us today.' That is why it is called Galeed—'Witness Heap.'"
    },
    "49": {
      "L": "and Mizpah, for he said, 'The LORD watch between you and me, when we are out of one another's sight.'",
      "M": "It was also called Mizpah, because he said, 'May the LORD keep watch between you and me when we are away from each other.'",
      "T": "It was also called Mizpah—'Watchtower'—because Laban said, 'May the LORD keep watch between you and me when we cannot see each other.'"
    },
    "50": {
      "L": "'If you oppress my daughters, or if you take wives besides my daughters, although no one is with us, see, God is witness between you and me.'",
      "M": "'If you mistreat my daughters or if you take any wives besides my daughters, even though no one is with us, remember that God is a witness between you and me.'",
      "T": "'If you mistreat my daughters, or if you take other wives alongside them—even when no one else is watching—God himself will be the witness between us.'"
    },
    "51": {
      "L": "Then Laban said to Jacob, 'See this heap and the pillar, which I have set between you and me.'",
      "M": "Laban also said to Jacob, 'Here is this heap, and here is this pillar I have set up between you and me.'",
      "T": "Then Laban said, 'This heap of stones and this pillar between us—look at them.'"
    },
    "52": {
      "L": "'This heap is a witness, and the pillar is a witness, that I will not pass over this heap to you, and you will not pass over this heap and this pillar to me, to do harm.'",
      "M": "'This heap is a witness, and this pillar is a witness, that I will not go past this heap to your side to harm you and that you will not go past this heap and pillar to my side to harm me.'",
      "T": "'This heap and this pillar are witnesses: I will not cross this boundary to harm you, and you will not cross it to harm me.'"
    },
    "53": {
      "L": "'The God of Abraham and the God of Nahor, the God of their father, judge between us.' So Jacob swore by the Fear of his father Isaac,",
      "M": "'May the God of Abraham and the God of Nahor, the God of their father, judge between us.' So Jacob took an oath in the name of the Awe of his father Isaac.",
      "T": "'May the God of Abraham and the God of Nahor—the God of their fathers—judge between us.' And Jacob swore by the Awesome God his father Isaac revered."
    },
    "54": {
      "L": "and Jacob offered a sacrifice in the hill country and called his kinsmen to eat bread. They ate bread and spent the night in the hill country.",
      "M": "He offered a sacrifice there in the hill country and invited his relatives to a meal. After they had eaten, they spent the night there.",
      "T": "Jacob offered a sacrifice on the hill, and invited his relatives to share a meal. They ate together and spent the night on the hill."
    },
    "55": {
      "L": "Early in the morning Laban arose and kissed his grandchildren and his daughters and blessed them. Then Laban departed and returned home.",
      "M": "Early the next morning Laban kissed his grandchildren and his daughters and blessed them. Then he left and returned home.",
      "T": "Early the next morning, Laban kissed his grandchildren and daughters goodbye and blessed them. Then he turned and went back home."
    }
  },
  "32": {
    "1": {
      "L": "Jacob went on his way, and the angels of God met him.",
      "M": "Jacob also went on his way, and the angels of God met him.",
      "T": "Jacob continued on his way—and the angels of God encountered him."
    },
    "2": {
      "L": "And when Jacob saw them he said, 'This is God's camp!' So he called the name of that place Mahanaim.",
      "M": "When Jacob saw them, he said, 'This is the camp of God!' So he named that place Mahanaim.",
      "T": "When Jacob saw them he exclaimed, 'This is God's own camp!' He named the place Mahanaim—'Two Camps.'"
    },
    "3": {
      "L": "And Jacob sent messengers before him to Esau his brother in the land of Seir, the country of Edom,",
      "M": "Jacob sent messengers ahead of him to his brother Esau in the land of Seir, the country of Edom.",
      "T": "Jacob sent messengers ahead of him to his brother Esau in the land of Seir, the territory of Edom."
    },
    "4": {
      "L": "instructing them, 'Thus you shall say to my lord Esau: Thus says your servant Jacob, \"I have sojourned with Laban and stayed until now.\"'",
      "M": "He instructed them: 'This is what you are to say to my lord Esau: \"Your servant Jacob says, I have been staying with Laban and have remained there till now.\"'",
      "T": "He told them: 'Say this to my lord Esau: \"Your servant Jacob sends word: I have been living with Laban and have only just set out.\"'"
    },
    "5": {
      "L": "'\"I have oxen, donkeys, flocks, male servants, and female servants. I have sent to tell my lord, in order that I may find favor in your sight.\"'",
      "M": "'\"I have cattle and donkeys, sheep and goats, male and female servants. Now I am sending this message to my lord, that I may find favor in your eyes.\"'",
      "T": "'\"I have cattle, donkeys, sheep, and servants, male and female. I am sending word to you, my lord, hoping to find favor in your sight.\"'"
    },
    "6": {
      "L": "And the messengers returned to Jacob, saying, 'We came to your brother Esau, and he is coming to meet you, and there are four hundred men with him.'",
      "M": "When the messengers returned to Jacob, they said, 'We went to your brother Esau, and now he is coming to meet you, and four hundred men are with him.'",
      "T": "The messengers came back to Jacob and reported, 'We reached your brother Esau, and he is coming to meet you—with four hundred men.'"
    },
    "7": {
      "L": "Then Jacob was greatly afraid and distressed. He divided the people who were with him, and the flocks and herds and camels, into two camps,",
      "M": "In great fear and distress Jacob divided the people who were with him into two groups, and the flocks and herds and camels as well.",
      "T": "Jacob was filled with fear and dread. He divided his people and all his flocks, herds, and camels into two groups,"
    },
    "8": {
      "L": "thinking, 'If Esau comes to the one camp and attacks it, then the camp that is left will escape.'",
      "M": "He thought, 'If Esau comes and attacks one group, the group that is left may escape.'",
      "T": "reasoning, 'If Esau attacks one group, the other group can escape.'"
    },
    "9": {
      "L": "And Jacob said, 'O God of my father Abraham and God of my father Isaac, O LORD who said to me, \"Return to your country and to your kindred, that I may do you good,\"'",
      "M": "Then Jacob prayed, 'O God of my father Abraham, God of my father Isaac, LORD, who said to me, \"Go back to your country and your relatives, and I will make you prosper,\"'",
      "T": "Then Jacob prayed: 'O God of my father Abraham, God of my father Isaac—O LORD, who told me, \"Return to your land and your family, and I will prosper you\"—'"
    },
    "10": {
      "L": "'I am not worthy of the least of all the deeds of steadfast love and all the faithfulness that you have shown to your servant, for with only my staff I crossed this Jordan, and now I have become two camps.'",
      "M": "'I am unworthy of all the kindness and faithfulness you have shown your servant. I had only my staff when I crossed this Jordan, but now I have become two camps.'",
      "T": "'I am not worthy of the least of all the steadfast love and faithfulness you have shown me, your servant. I crossed this Jordan with nothing but a walking stick, and now I have become two great camps.'"
    },
    "11": {
      "L": "'Please deliver me from the hand of my brother, from the hand of Esau, for I fear him, that he may come and attack me, the mothers with the children.'",
      "M": "'Save me, I pray, from the hand of my brother Esau, for I am afraid he will come and attack me, and also the mothers with their children.'",
      "T": "'Please rescue me from the hand of my brother Esau—I am terrified that he is coming to kill me, along with the mothers and children.'"
    },
    "12": {
      "L": "'But you said, \"I will surely do you good, and make your offspring as the sand of the sea, which cannot be numbered for multitude.\"'",
      "M": "'But you have said, \"I will surely make you prosper and will make your descendants like the sand of the sea, which cannot be counted.\"'",
      "T": "'Yet you yourself promised, \"I will make you prosper and your descendants will be as countless as the sand of the sea.\"'"
    },
    "13": {
      "L": "So he stayed there that night, and from what he had with him he took a present for his brother Esau,",
      "M": "He spent the night there, and from what he had with him he selected a gift for his brother Esau:",
      "T": "He spent that night there. From his possessions he chose a gift for his brother Esau:"
    },
    "14": {
      "L": "two hundred female goats and twenty male goats, two hundred ewes and twenty rams,",
      "M": "two hundred female goats and twenty male goats, two hundred ewes and twenty rams,",
      "T": "two hundred female goats and twenty male goats, two hundred ewes and twenty rams,"
    },
    "15": {
      "L": "thirty milking camels and their calves, forty cows and ten bulls, twenty female donkeys and ten male donkeys.",
      "M": "thirty female camels with their young, forty cows and ten bulls, and twenty female donkeys and ten male donkeys.",
      "T": "thirty female camels with their calves, forty cows and ten bulls, twenty female donkeys and ten male donkeys."
    },
    "16": {
      "L": "These he handed over to his servants, every drove by itself, and said to his servants, 'Pass on ahead of me and put a space between drove and drove.'",
      "M": "He put them in the care of his servants, each herd by itself, and said to his servants, 'Go ahead of me, and keep some space between the herds.'",
      "T": "He gave each herd to a different servant and said, 'Go ahead of me, keeping space between each group.'"
    },
    "17": {
      "L": "He instructed the first, 'When Esau my brother meets you and asks you, \"To whom do you belong? Where are you going? And whose are these ahead of you?\"'",
      "M": "He also instructed the one in the lead: 'When my brother Esau meets you and asks, \"Who do you belong to, and where are you going, and who owns all these animals in front of you?\"'",
      "T": "He gave instructions to the servant at the front: 'When my brother Esau stops you and asks, \"Whose are you, and where are you going, and whose animals are these ahead of you?\"'"
    },
    "18": {
      "L": "'then you shall say, \"They belong to your servant Jacob. They are a present sent to my lord Esau. And moreover, he is behind us.\"'",
      "M": "'then you are to say, \"They belong to your servant Jacob; they are a gift sent to my lord Esau, and he is coming behind us.\"'",
      "T": "'say, \"They belong to your servant Jacob. It is a gift he is sending to his lord Esau. Jacob himself is following behind us.\"'"
    },
    "19": {
      "L": "He likewise instructed the second and the third and all who followed the droves, 'You shall say the same thing to Esau when you find him,'",
      "M": "He also instructed the second, the third and all the others who followed the herds: 'You are to say the same thing to Esau when you meet him.'",
      "T": "He gave the same instructions to the second and third servants and to all who followed with the herds: 'Say the same thing when you meet Esau.'"
    },
    "20": {
      "L": "'and you shall say, \"Moreover, your servant Jacob is behind us.\"' For he thought, 'I may appease him with the present that goes ahead of me, and afterward I shall see his face. Perhaps he will accept me.'",
      "M": "And be sure to say, 'Your servant Jacob is coming behind us.' For he thought, 'I will pacify him with these gifts I am sending on ahead; later, when I see him, perhaps he will receive me.'",
      "T": "'And add, \"Your servant Jacob is coming right behind.\"' For Jacob reasoned, 'Maybe I can soften him with these gifts going ahead. Then when I face him, perhaps he will accept me.'"
    },
    "21": {
      "L": "So the present passed on ahead of him, and he himself stayed that night in the camp.",
      "M": "So Jacob's gifts went on ahead of him, but he himself spent the night in the camp.",
      "T": "So the gifts went on ahead of him, while he himself spent that night in the camp."
    },
    "22": {
      "L": "The same night he arose and took his two wives, his two female servants, and his eleven children, and crossed the ford of the Jabbok.",
      "M": "That night Jacob got up and took his two wives, his two female servants and his eleven sons and crossed the ford of the Jabbok.",
      "T": "Later that same night, Jacob got up, took his two wives, his two female servants, and his eleven children, and crossed the ford of the Jabbok."
    },
    "23": {
      "L": "He took them and sent them across the stream, and everything else that he had.",
      "M": "After he had sent them across the stream, he sent over all his possessions.",
      "T": "He helped them all cross the stream and sent everything he owned across as well."
    },
    "24": {
      "L": "And Jacob was left alone. And a man wrestled with him until the breaking of the day.",
      "M": "So Jacob was left alone, and a man wrestled with him till daybreak.",
      "T": "Jacob was left alone. And then a man appeared and grappled with him until the first light of dawn."
    },
    "25": {
      "L": "When the man saw that he did not prevail against Jacob, he touched his hip socket, and Jacob's hip was put out of joint as he wrestled with him.",
      "M": "When the man saw that he could not overpower him, he touched the socket of Jacob's hip so that his hip was wrenched as he wrestled with the man.",
      "T": "When the man saw he could not overpower Jacob, he struck Jacob's hip socket, wrenching it out of joint as they wrestled."
    },
    "26": {
      "L": "Then he said, 'Let me go, for the day has broken.' But Jacob said, 'I will not let you go unless you bless me.'",
      "M": "Then the man said, 'Let me go, for it is daybreak.' But Jacob replied, 'I will not let you go unless you bless me.'",
      "T": "The man said, 'Let me go—dawn is breaking.' But Jacob said, 'I will not let you go unless you bless me.'"
    },
    "27": {
      "L": "And he said to him, 'What is your name?' And he said, 'Jacob.'",
      "M": "The man asked him, 'What is your name?' 'Jacob,' he answered.",
      "T": "The man asked, 'What is your name?' 'Jacob,' he said."
    },
    "28": {
      "L": "Then he said, 'Your name shall no longer be called Jacob, but Israel, for you have striven with God and with men, and have prevailed.'",
      "M": "Then the man said, 'Your name will no longer be Jacob, but Israel, because you have struggled with God and with humans and have overcome.'",
      "T": "Then the man said, 'Your name will no longer be Jacob but Israel—One Who Strives with God—because you have wrestled with God and with people, and you have won.'"
    },
    "29": {
      "L": "Then Jacob asked him, 'Please tell me your name.' But he said, 'Why is it that you ask my name?' And there he blessed him.",
      "M": "Jacob said, 'Please tell me your name.' But he replied, 'Why do you ask my name?' Then he blessed him there.",
      "T": "Jacob pressed him: 'Please, tell me your name.' But he said, 'Why do you ask my name?' And he blessed Jacob there."
    },
    "30": {
      "L": "So Jacob called the name of the place Peniel, saying, 'For I have seen God face to face, and yet my life has been delivered.'",
      "M": "So Jacob called the place Peniel, saying, 'It is because I saw God face to face, and yet my life was spared.'",
      "T": "Jacob named the place Peniel—'Face of God'—saying, 'I have seen God face to face, and yet I am still alive.'"
    },
    "31": {
      "L": "The sun rose upon him as he passed Penuel, limping because of his hip.",
      "M": "The sun rose above him as he passed Peniel, and he was limping because of his hip.",
      "T": "The sun rose as Jacob crossed Penuel, limping from the injury to his hip."
    },
    "32": {
      "L": "Therefore to this day the people of Israel do not eat the sinew of the thigh that is on the hip socket, because he touched the socket of Jacob's hip on the sinew of the thigh.",
      "M": "Therefore to this day the Israelites do not eat the tendon attached to the socket of the hip, because the socket of Jacob's hip was touched near the tendon.",
      "T": "That is why to this day the Israelites do not eat the tendon of the hip socket—because that is where the man struck Jacob and wrenched his hip."
    }
  },
  "33": {
    "1": {
      "L": "And Jacob lifted up his eyes and looked, and behold, Esau was coming, and four hundred men with him. So he divided the children among Leah and Rachel and the two female servants.",
      "M": "Jacob looked up and there was Esau, coming with his four hundred men; so he divided the children among Leah, Rachel and the two female servants.",
      "T": "Jacob looked up and saw Esau coming with his four hundred men. He divided the children among Leah, Rachel, and the two female servants."
    },
    "2": {
      "L": "And he put the servants with their children in front, then Leah with her children, and Rachel and Joseph last of all.",
      "M": "He put the female servants and their children in front, Leah and her children next, and Rachel and Joseph in the rear.",
      "T": "He placed the servants and their children at the front, Leah and her children next, and Rachel and Joseph at the back."
    },
    "3": {
      "L": "He himself went on before them, bowing himself to the ground seven times, until he came near to his brother.",
      "M": "He himself went on ahead and bowed down to the ground seven times as he approached his brother.",
      "T": "Jacob himself went ahead of them, bowing low to the ground seven times as he drew near to his brother."
    },
    "4": {
      "L": "But Esau ran to meet him and embraced him and fell on his neck and kissed him, and they wept.",
      "M": "But Esau ran to meet Jacob and embraced him; he threw his arms around his neck and kissed him. And they wept.",
      "T": "But Esau ran to meet him. He threw his arms around Jacob and embraced him, fell on his neck and kissed him. They both wept."
    },
    "5": {
      "L": "And when Esau lifted up his eyes and saw the women and children, he said, 'Who are these with you?' Jacob said, 'The children whom God has graciously given your servant.'",
      "M": "Then Esau looked up and saw the women and children. 'Who are these with you?' he asked. Jacob answered, 'They are the children God has graciously given your servant.'",
      "T": "When Esau looked up and saw the women and children, he asked, 'Who are all these with you?' Jacob answered, 'These are the children God has graciously given me, your servant.'"
    },
    "6": {
      "L": "Then the servants drew near, they and their children, and bowed down.",
      "M": "Then the female servants and their children approached and bowed down.",
      "T": "Then the female servants and their children came forward and bowed down."
    },
    "7": {
      "L": "Leah likewise and her children drew near and bowed down. And last Joseph and Rachel drew near, and they bowed down.",
      "M": "Next, Leah and her children came and bowed down. Last of all came Joseph and Rachel, and they too bowed down.",
      "T": "Leah and her children came next and bowed. Last of all, Joseph and Rachel came forward and bowed."
    },
    "8": {
      "L": "Esau said, 'What do you mean by all this company that I met?' Jacob answered, 'To find favor in the sight of my lord.'",
      "M": "Esau asked, 'What's the meaning of all these flocks and herds I met?' 'To find favor in your eyes, my lord,' Jacob said.",
      "T": "Esau asked, 'What was the purpose of all those animals I met on the road?' Jacob answered, 'To find favor with you, my lord.'"
    },
    "9": {
      "L": "But Esau said, 'I have enough, my brother; keep what you have for yourself.'",
      "M": "But Esau said, 'I already have plenty, my brother. Keep what you have for yourself.'",
      "T": "But Esau said, 'I already have more than enough, brother. Keep what is yours.'"
    },
    "10": {
      "L": "Jacob said, 'No, please, if I have found favor in your sight, then accept my present from my hand. For I have seen your face, which is like seeing the face of God, and you have accepted me.'",
      "M": "'No, please!' said Jacob. 'If I have found favor in your eyes, accept this gift from me. For to see your face is like seeing the face of God, now that you have received me favorably.'",
      "T": "'Please,' Jacob insisted, 'if I have found any favor with you, accept my gift. Seeing your face is like seeing the face of God—for you have received me with such grace.' (The echo of Peniel is deliberate: Jacob encounters the divine in his brother's unexpected mercy.)"
    },
    "11": {
      "L": "'Please accept my blessing that is brought to you, because God has dealt graciously with me, and because I have enough.' Thus he urged him, and he took it.",
      "M": "'Please accept the blessing I have brought you, for God has been gracious to me and I have all I need.' And because Jacob insisted, Esau accepted it.",
      "T": "'Please take the gift I have brought—God has been gracious to me and I have everything I need.' Jacob kept urging him, and Esau finally accepted."
    },
    "12": {
      "L": "Then Esau said, 'Let us journey on our way, and I will go ahead of you.'",
      "M": "Then Esau said, 'Let us be on our way; I'll accompany you.'",
      "T": "Then Esau said, 'Let us travel on together. I will lead the way.'"
    },
    "13": {
      "L": "But Jacob said to him, 'My lord knows that the children are frail, and that the nursing flocks and herds are a care to me. If they are driven hard for one day, all the flocks will die.'",
      "M": "But Jacob said to him, 'My lord knows that the children are tender and that I must care for the ewes and cows that are nursing their young. If they are driven hard just one day, all the animals will die.'",
      "T": "But Jacob said, 'My lord knows that the children are young and tender, and the nursing animals are my concern. If I drive them hard for a single day, the whole flock will die.'"
    },
    "14": {
      "L": "'Let my lord pass on ahead of his servant, and I will lead on slowly, at the pace of the livestock that are ahead of me and at the pace of the children, until I come to my lord in Seir.'",
      "M": "'So let my lord go on ahead of his servant, while I move along slowly at the pace of the flocks and herds before me and the pace of the children, until I come to my lord in Seir.'",
      "T": "'Please go ahead, my lord. I will travel more slowly, at the pace of the livestock and the children, until I join you in Seir.'"
    },
    "15": {
      "L": "So Esau said, 'Let me leave with you some of the people who are with me.' But he said, 'What need is there? Let me find favor in the sight of my lord.'",
      "M": "Esau said, 'Then let me leave some of my men with you.' 'But why do that?' Jacob asked. 'Just let me find favor in the eyes of my lord.'",
      "T": "Esau said, 'Let me at least leave some of my men to escort you.' Jacob replied, 'There is no need. I only want to find favor in my lord's eyes.'"
    },
    "16": {
      "L": "So Esau returned that day on his way to Seir.",
      "M": "So that day Esau started on his way back to Seir.",
      "T": "So Esau turned back that day and went on his way to Seir."
    },
    "17": {
      "L": "But Jacob journeyed to Succoth, and built himself a house and made booths for his livestock. Therefore the name of the place is called Succoth.",
      "M": "Jacob, however, went to Succoth, where he built a place for himself and made shelters for his livestock. That is why the place is called Succoth.",
      "T": "Jacob, however, went to Succoth, where he built himself a house and made shelters for his livestock. That is why the place is called Succoth—'Shelters.'"
    },
    "18": {
      "L": "And Jacob came safely to the city of Shechem, which is in the land of Canaan, on his way from Paddan-aram, and he camped before the city.",
      "M": "After Jacob came from Paddan Aram, he arrived safely at the city of Shechem in Canaan and camped within sight of the city.",
      "T": "Jacob arrived safely at the city of Shechem in the land of Canaan, having come from Paddan-aram, and camped outside the city."
    },
    "19": {
      "L": "And from the sons of Hamor, Shechem's father, he bought for a hundred pieces of money the piece of land on which he had pitched his tent.",
      "M": "For a hundred pieces of silver, he bought from the sons of Hamor, the father of Shechem, the plot of ground where he pitched his tent.",
      "T": "He purchased the plot of ground where he had pitched his tent from the sons of Hamor, Shechem's father, for a hundred pieces of silver."
    },
    "20": {
      "L": "There he erected an altar and called it El-Elohe-Israel.",
      "M": "There he set up an altar and called it El Elohe Israel.",
      "T": "There he set up an altar and named it El-Elohe-Israel—'God, the God of Israel.'"
    }
  },
  "34": {
    "1": {
      "L": "Now Dinah the daughter of Leah, whom she had borne to Jacob, went out to see the women of the land.",
      "M": "Now Dinah, the daughter Leah had borne to Jacob, went out to visit the women of the land.",
      "T": "One day Dinah—the daughter Leah had borne to Jacob—went out to visit the women of the region."
    },
    "2": {
      "L": "And when Shechem the son of Hamor the Hivite, the prince of the land, saw her, he seized her and lay with her and humiliated her.",
      "M": "When Shechem son of Hamor the Hivite, the ruler of that area, saw her, he took her and raped her.",
      "T": "When Shechem the son of Hamor—the Hivite ruler of that area—saw her, he seized her, raped her, and violated her."
    },
    "3": {
      "L": "And his soul was drawn to Dinah the daughter of Jacob. He loved the young woman and spoke tenderly to her.",
      "M": "His heart was drawn to Dinah daughter of Jacob; he loved the young woman and spoke tenderly to her.",
      "T": "But then his heart was captivated by Dinah. He loved her and tried to win her over with tender words."
    },
    "4": {
      "L": "So Shechem spoke to his father Hamor, saying, 'Get me this girl for my wife.'",
      "M": "And Shechem said to his father Hamor, 'Get me this girl as my wife.'",
      "T": "Shechem went to his father Hamor and said, 'Get me this girl as my wife.'"
    },
    "5": {
      "L": "Now Jacob heard that he had defiled his daughter Dinah. But his sons were with his livestock in the field, so Jacob held his peace until they came.",
      "M": "When Jacob heard that his daughter Dinah had been defiled, his sons were in the fields with his livestock; so he did nothing about it until they came home.",
      "T": "Jacob heard that his daughter Dinah had been violated. His sons were out in the fields with the livestock, so he said nothing until they returned."
    },
    "6": {
      "L": "And Hamor the father of Shechem went out to Jacob to speak with him.",
      "M": "Then Shechem's father Hamor went out to talk with Jacob.",
      "T": "Shechem's father Hamor went out to meet with Jacob."
    },
    "7": {
      "L": "The sons of Jacob had come in from the field as soon as they heard of it, and the men were indignant and very angry, because he had done an outrageous thing in Israel by lying with Jacob's daughter, for such a thing must not be done.",
      "M": "Now Jacob's sons had come in from the fields as soon as they heard what had happened. They were shocked and furious, because Shechem had done an outrageous thing in Israel by sleeping with Jacob's daughter—a thing that should not be done.",
      "T": "Meanwhile Jacob's sons had come in from the fields the moment they heard. They were furious and deeply outraged, because Shechem had done a vile and shameful thing against Israel by raping Jacob's daughter—something utterly unacceptable."
    },
    "8": {
      "L": "But Hamor spoke with them, saying, 'The soul of my son Shechem longs for your daughter. Please give her to him to be his wife.'",
      "M": "But Hamor said to them, 'My son Shechem has his heart set on your daughter. Please give her to him as his wife.'",
      "T": "But Hamor addressed them: 'My son Shechem is deeply in love with your daughter. Please give her to him as his wife.'"
    },
    "9": {
      "L": "'Make marriages with us. Give your daughters to us, and take our daughters for yourselves.'",
      "M": "'Intermarry with us; give us your daughters and take our daughters for yourselves.'",
      "T": "'Let us form marriage alliances with each other. Give us your daughters and take ours in return.'"
    },
    "10": {
      "L": "'You shall dwell with us, and the land shall be open to you. Dwell and trade in it, and get property in it.'",
      "M": "'You can settle among us; the land is open to you. Live in it, trade in it, and acquire property in it.'",
      "T": "'Settle here among us. The land is open to you—live here, trade freely, and acquire property.'"
    },
    "11": {
      "L": "Shechem also said to her father and to her brothers, 'Let me find favor in your eyes, and whatever you say to me I will give.'",
      "M": "Then Shechem said to Dinah's father and brothers, 'Let me find favor in your eyes, and I will give you whatever you ask.'",
      "T": "Shechem himself appealed to Dinah's father and brothers: 'Let me find favor with you. Name your price—I will pay whatever you ask.'"
    },
    "12": {
      "L": "'Ask me for as great a bride price and gift as you will, and I will give whatever you say to me. Only give me the young woman to be my wife.'",
      "M": "'Make the price for the bride and the gift I am to bring as great as you like, and I'll pay whatever you ask me. Only give me the young woman as my wife.'",
      "T": "'Set the bride price as high as you wish. I will give whatever gift you demand. Only let me marry the young woman.'"
    },
    "13": {
      "L": "The sons of Jacob answered Shechem and his father Hamor deceitfully, because he had defiled their sister Dinah.",
      "M": "Because their sister Dinah had been defiled, Jacob's sons replied deceitfully as they spoke to Shechem and his father Hamor.",
      "T": "Jacob's sons answered Shechem and his father Hamor with deception—because Shechem had violated their sister Dinah."
    },
    "14": {
      "L": "They said to them, 'We cannot do this thing, to give our sister to one who is uncircumcised, for that would be a disgrace to us.'",
      "M": "'We can't do such a thing,' they said, 'we can't give our sister to a man who is not circumcised. That would be a disgrace to us.'",
      "T": "'We cannot do this,' they said. 'Giving our sister to an uncircumcised man would be a disgrace to us.'"
    },
    "15": {
      "L": "'Only on this condition will we agree with you—that you will become as we are by every male among you being circumcised.'",
      "M": "'We will enter into an agreement with you on one condition only: that you become like us by circumcising all your males.'",
      "T": "'We will agree to this on one condition only: all your males must be circumcised, becoming as we are.'"
    },
    "16": {
      "L": "'Then we will give our daughters to you, and we will take your daughters to ourselves, and we will dwell with you and become one people.'",
      "M": "'Then we will give you our daughters and take your daughters for ourselves. We'll settle among you and become one people with you.'",
      "T": "'Then we will give you our daughters and take yours in marriage. We will settle among you and become one united people.'"
    },
    "17": {
      "L": "'But if you will not listen to us and be circumcised, then we will take our daughter, and we will be gone.'",
      "M": "'But if you will not agree to be circumcised, we'll take our sister and go.'",
      "T": "'But if you refuse to be circumcised, we will take our sister and leave.'"
    },
    "18": {
      "L": "Their words pleased Hamor and Hamor's son Shechem.",
      "M": "Their proposal seemed good to Hamor and his son Shechem.",
      "T": "This proposal satisfied Hamor and his son Shechem."
    },
    "19": {
      "L": "And the young man did not delay to do the thing, because he delighted in Jacob's daughter. Now he was the most honored of all his father's house.",
      "M": "The young man, who was the most honored of all his father's household, lost no time in doing what they said, because he was delighted with Jacob's daughter.",
      "T": "Shechem wasted no time acting on the agreement—he was captivated by Dinah. He was the most respected man in his father's household."
    },
    "20": {
      "L": "So Hamor and his son Shechem came to the gate of their city and spoke to the men of their city, saying,",
      "M": "So Hamor and his son Shechem went to the gate of their city to speak to the men of their city.",
      "T": "Hamor and Shechem went to the gate of their city and addressed the men of the city:"
    },
    "21": {
      "L": "'These men are at peace with us; let them dwell in the land and trade in it, for behold, the land is large enough for them. Let us take their daughters as wives, and let us give them our daughters.'",
      "M": "'These men are friendly toward us,' they said. 'Let them live in our land and trade in it; the land has plenty of room for them. We can marry their daughters and they can marry ours.'",
      "T": "'These men are peaceable toward us. Let them settle in the land and trade freely—there is plenty of room for them. We will marry their daughters and give our daughters to them.'"
    },
    "22": {
      "L": "'Only on this condition will the men agree to dwell with us to become one people—when every male among us is circumcised as they are circumcised.'",
      "M": "'But the men will agree to live with us as one people only on the condition that our males be circumcised, as they themselves are.'",
      "T": "'But the men will only agree to live with us and become one people on this condition: all our males must be circumcised, as they are.'"
    },
    "23": {
      "L": "'Will not their livestock, their property and all their beasts be ours? Only let us agree with them, and they will dwell with us.'",
      "M": "'Won't their livestock, their property and all their other animals become ours? So let us agree to their terms, and they will settle among us.'",
      "T": "'Won't all their livestock, their property, and their animals eventually become ours? Let us just agree to their terms, and they will settle here with us.'"
    },
    "24": {
      "L": "And all who went out of the gate of his city listened to Hamor and his son Shechem, and every male was circumcised, all who went out of the gate of his city.",
      "M": "All the men who went out of the city gate agreed with Hamor and his son Shechem, and every male in the city was circumcised.",
      "T": "All the men of the city gate agreed with Hamor and Shechem, and every male in the city was circumcised."
    },
    "25": {
      "L": "On the third day, when they were sore, two of the sons of Jacob, Simeon and Levi, Dinah's brothers, each took his sword and came against the city while it felt secure and killed all the males.",
      "M": "Three days later, while all of them were still in pain, two of Jacob's sons, Simeon and Levi, Dinah's brothers, took their swords and attacked the unsuspecting city, killing every male.",
      "T": "Three days later, when all the men were still in agony from the surgery, Simeon and Levi—two of Jacob's sons, full brothers to Dinah—drew their swords and slaughtered every male in the city without warning."
    },
    "26": {
      "L": "They killed Hamor and his son Shechem with the sword and took Dinah out of Shechem's house and went away.",
      "M": "They put Hamor and his son Shechem to the sword and took Dinah from Shechem's house and left.",
      "T": "They killed Hamor and his son Shechem with their swords and took Dinah from Shechem's house and left."
    },
    "27": {
      "L": "The sons of Jacob came upon the slain and plundered the city, because they had defiled their sister.",
      "M": "The sons of Jacob came upon the dead and looted the city where their sister had been defiled.",
      "T": "Jacob's other sons came upon the dead men and plundered the city that had violated their sister."
    },
    "28": {
      "L": "They took their flocks and their herds and their donkeys, and whatever was in the city and in the field.",
      "M": "They seized their flocks and herds and donkeys and everything else of theirs in the city and out in the fields.",
      "T": "They seized the flocks, herds, donkeys, and everything else in the city and in the surrounding fields."
    },
    "29": {
      "L": "All their wealth, all their little ones and their wives, all that was in the houses, they captured and plundered.",
      "M": "They carried off all their wealth and all their women and children, taking as plunder everything in the houses.",
      "T": "They carried off all the wealth, the women and children, and stripped everything from the houses."
    },
    "30": {
      "L": "Then Jacob said to Simeon and Levi, 'You have brought trouble on me by making me stink to the inhabitants of the land, the Canaanites and the Perizzites. My numbers are few, and if they gather themselves against me and attack me, I shall be destroyed, both I and my household.'",
      "M": "Then Jacob said to Simeon and Levi, 'You have brought trouble on me by making me obnoxious to the Canaanites and Perizzites, the people living in this land. We are few in number, and if they join forces against me and attack me, I and my household will be destroyed.'",
      "T": "Jacob said to Simeon and Levi, 'You have ruined me—you have made me repulsive to every Canaanite and Perizzite in this land. We are few in number. If they unite against me and attack, I and my whole family will be wiped out.'"
    },
    "31": {
      "L": "But they said, 'Should he treat our sister like a prostitute?'",
      "M": "But they replied, 'Should he have treated our sister like a prostitute?'",
      "T": "But they answered, 'Should he have been allowed to treat our sister as a prostitute?'"
    }
  },
  "35": {
    "1": {
      "L": "God said to Jacob, 'Arise, go up to Bethel and dwell there. Make an altar there to the God who appeared to you when you fled from your brother Esau.'",
      "M": "Then God said to Jacob, 'Go up to Bethel and settle there, and build an altar there to God, who appeared to you when you were fleeing from your brother Esau.'",
      "T": "God said to Jacob, 'Get up and go to Bethel and make your home there. Build an altar there to the God who appeared to you when you were fleeing from your brother Esau.'"
    },
    "2": {
      "L": "So Jacob said to his household and to all who were with him, 'Put away the foreign gods that are among you and purify yourselves and change your garments.'",
      "M": "So Jacob said to his household and to all who were with him, 'Get rid of the foreign gods you have with you, and purify yourselves and change your clothes.'",
      "T": "So Jacob said to his household and to all who were with him, 'Get rid of every foreign god you have. Purify yourselves and put on fresh clothes.'"
    },
    "3": {
      "L": "'Then let us arise and go up to Bethel, so that I may make there an altar to the God who answers me in the day of my distress and has been with me wherever I have gone.'",
      "M": "'Then come, let us go up to Bethel, where I will build an altar to God, who answered me in the day of my distress and who has been with me wherever I have gone.'",
      "T": "'Then we will go up to Bethel, where I will build an altar to the God who answered me when I was in trouble and who has been with me every step of the way.'"
    },
    "4": {
      "L": "So they gave to Jacob all the foreign gods that they had, and the rings that were in their ears. Jacob hid them under the terebinth tree that was near Shechem.",
      "M": "So they gave Jacob all the foreign gods they had and the rings in their ears, and Jacob buried them under the oak at Shechem.",
      "T": "So everyone handed over to Jacob their foreign gods and the earrings they wore, and Jacob buried them under the great tree near Shechem."
    },
    "5": {
      "L": "And as they journeyed, a terror from God fell upon the cities that were around them, so that they did not pursue the sons of Jacob.",
      "M": "Then they set out, and the terror of God fell on the towns all around them so that no one pursued them.",
      "T": "As they traveled, a divinely sent terror fell on all the surrounding towns, and no one dared to pursue Jacob's sons."
    },
    "6": {
      "L": "And Jacob came to Luz (that is, Bethel), which is in the land of Canaan, he and all the people who were with him.",
      "M": "Jacob and all the people with him came to Luz (that is, Bethel) in the land of Canaan.",
      "T": "Jacob and all his company arrived at Luz—that is, Bethel—in the land of Canaan."
    },
    "7": {
      "L": "And there he built an altar and called the place El-bethel, because there God had revealed himself to him when he fled from his brother.",
      "M": "There he built an altar, and he called the place El Bethel, because it was there that God had revealed himself to him when he was fleeing from his brother.",
      "T": "There he built an altar and named the place El-bethel—'God of Bethel'—because it was there that God had revealed himself to him when he was running from Esau."
    },
    "8": {
      "L": "And Deborah, Rebekah's nurse, died, and she was buried under an oak below Bethel. So he called its name Allon-bacuth.",
      "M": "Now Deborah, Rebekah's nurse, died and was buried under the oak outside Bethel. So it was named Allon Bakuth.",
      "T": "It was there that Deborah, Rebekah's nurse, died. She was buried under the oak below Bethel, and it was called Allon-bacuth—'Oak of Weeping.'"
    },
    "9": {
      "L": "God appeared to Jacob again, when he came from Paddan-aram, and blessed him.",
      "M": "After Jacob returned from Paddan Aram, God appeared to him again and blessed him.",
      "T": "God appeared to Jacob once more—this time after his return from Paddan-aram—and blessed him."
    },
    "10": {
      "L": "And God said to him, 'Your name is Jacob; no longer shall your name be called Jacob, but Israel shall be your name.' So he called his name Israel.",
      "M": "God said to him, 'Your name is Jacob, but you will no longer be called Jacob; your name will be Israel.' So he named him Israel.",
      "T": "God said to him, 'Your name is Jacob—but from now on you will be called Israel.' So God named him Israel."
    },
    "11": {
      "L": "And God said to him, 'I am God Almighty: be fruitful and multiply. A nation and a company of nations shall come from you, and kings shall come from your own body.'",
      "M": "And God said to him, 'I am God Almighty; be fruitful and increase in number. A nation and a community of nations will come from you, and kings will be among your descendants.'",
      "T": "God said to him, 'I am God Almighty. Be fruitful and multiply. A great nation—indeed, a whole community of nations—will spring from you, and kings will descend from your own body.'"
    },
    "12": {
      "L": "'The land that I gave to Abraham and Isaac I will give to you, and I will give the land to your offspring after you.'",
      "M": "'The land I gave to Abraham and Isaac I also give to you, and I will give this land to your descendants after you.'",
      "T": "'The land I gave to Abraham and Isaac—I now give to you, and I will give it to your descendants after you.'"
    },
    "13": {
      "L": "Then God went up from him in the place where he had spoken with him.",
      "M": "Then God went up from him at the place where he had talked with him.",
      "T": "Then God departed from him at the place where he had spoken."
    },
    "14": {
      "L": "And Jacob set up a pillar in the place where he had spoken with him, a pillar of stone. He poured out a drink offering on it and poured oil on it.",
      "M": "Jacob set up a stone pillar at the place where God had talked with him, and he poured out a drink offering on it; he also poured oil on it.",
      "T": "Jacob set up a stone pillar at the spot where God had spoken with him. He poured a drink offering over it and anointed it with oil."
    },
    "15": {
      "L": "So Jacob called the name of the place where God had spoken with him Bethel.",
      "M": "Jacob called the place where God had talked with him Bethel.",
      "T": "Jacob named the place where God had spoken with him Bethel—'House of God.'"
    },
    "16": {
      "L": "Then they journeyed from Bethel. When they were still some distance from Ephrath, Rachel went into labor, and she had hard labor.",
      "M": "Then they moved on from Bethel. While they were still some distance from Ephrath, Rachel began to give birth and had great difficulty.",
      "T": "They traveled on from Bethel. While they were still some distance from Ephrath, Rachel went into labor—and it was a very difficult labor."
    },
    "17": {
      "L": "And when her labor was at its hardest, the midwife said to her, 'Fear not, for you have another son.'",
      "M": "As she was having great difficulty in childbirth, the midwife said to her, 'Don't despair, for you have another son.'",
      "T": "When her labor was at its most severe, the midwife said to her, 'Don't be afraid—you have another son!'"
    },
    "18": {
      "L": "And as her soul was departing (for she was dying), she called his name Ben-oni; but his father called him Benjamin.",
      "M": "As she breathed her last—for she was dying—she named her son Ben-Oni. But his father named him Benjamin.",
      "T": "As her life slipped away—for she was dying—she named her son Ben-oni, 'Son of My Sorrow.' But his father named him Benjamin—'Son of My Right Hand' or 'Son of Good Fortune.'"
    },
    "19": {
      "L": "So Rachel died, and she was buried on the way to Ephrath (that is, Bethlehem).",
      "M": "So Rachel died and was buried on the way to Ephrath (that is, Bethlehem).",
      "T": "So Rachel died and was buried beside the road to Ephrath—that is, Bethlehem."
    },
    "20": {
      "L": "And Jacob set up a pillar over her tomb. It is the pillar of Rachel's tomb, which is there to this day.",
      "M": "Over her tomb Jacob set up a pillar, and to this day that pillar marks Rachel's tomb.",
      "T": "Jacob set up a pillar over her grave. It stands there to this day as the Pillar of Rachel's Tomb."
    },
    "21": {
      "L": "Israel journeyed on and pitched his tent beyond the tower of Eder.",
      "M": "Israel moved on again and pitched his tent beyond Migdal Eder.",
      "T": "Israel traveled on and set up camp beyond the tower of Eder."
    },
    "22": {
      "L": "While Israel lived in that land, Reuben went and lay with Bilhah his father's concubine. And Israel heard of it.\n\nNow the sons of Jacob were twelve.",
      "M": "While Israel was living in that region, Reuben went in and slept with his father's concubine Bilhah, and Israel heard of it.\n\nJacob had twelve sons:",
      "T": "While Israel was living in that region, Reuben slept with his father's concubine Bilhah. Israel heard what had happened.\n\nJacob had twelve sons:"
    },
    "23": {
      "L": "The sons of Leah: Reuben (Jacob's firstborn), Simeon, Levi, Judah, Issachar, and Zebulun.",
      "M": "The sons of Leah: Reuben the firstborn of Jacob, Simeon, Levi, Judah, Issachar and Zebulun.",
      "T": "The sons of Leah: Reuben (Jacob's firstborn), Simeon, Levi, Judah, Issachar, and Zebulun."
    },
    "24": {
      "L": "The sons of Rachel: Joseph and Benjamin.",
      "M": "The sons of Rachel: Joseph and Benjamin.",
      "T": "The sons of Rachel: Joseph and Benjamin."
    },
    "25": {
      "L": "The sons of Bilhah, Rachel's servant: Dan and Naphtali.",
      "M": "The sons of Rachel's servant Bilhah: Dan and Naphtali.",
      "T": "The sons of Rachel's servant Bilhah: Dan and Naphtali."
    },
    "26": {
      "L": "The sons of Zilpah, Leah's servant: Gad and Asher. These were the sons of Jacob who were born to him in Paddan-aram.",
      "M": "The sons of Leah's servant Zilpah: Gad and Asher. These were the sons of Jacob, born to him in Paddan Aram.",
      "T": "The sons of Leah's servant Zilpah: Gad and Asher. These were the twelve sons of Jacob born to him in Paddan-aram."
    },
    "27": {
      "L": "And Jacob came to his father Isaac at Mamre, or Kiriath-arba (that is, Hebron), where Abraham and Isaac had sojourned.",
      "M": "Jacob came home to his father Isaac in Mamre, near Kiriath Arba (that is, Hebron), where Abraham and Isaac had stayed.",
      "T": "Jacob finally came home to his father Isaac at Mamre—Kiriath-arba, that is Hebron—where Abraham and Isaac had lived as sojourners."
    },
    "28": {
      "L": "Now the days of Isaac were 180 years.",
      "M": "Isaac lived a hundred and eighty years.",
      "T": "Isaac lived to be 180 years old."
    },
    "29": {
      "L": "And Isaac breathed his last, and he died and was gathered to his people, old and full of days. And his sons Esau and Jacob buried him.",
      "M": "Then he breathed his last and died and was gathered to his people, old and full of years. And his sons Esau and Jacob buried him.",
      "T": "Then he breathed his last and died, joining his ancestors. He was old and had lived a full life. His sons Esau and Jacob buried him together."
    }
  },
  "36": {
    "1": {
      "L": "These are the generations of Esau (that is, Edom).",
      "M": "This is the account of the family line of Esau (that is, Edom).",
      "T": "This is the family record of Esau—the man also called Edom."
    },
    "2": {
      "L": "Esau took his wives from the Canaanites: Adah the daughter of Elon the Hittite, Oholibamah the daughter of Anah the daughter of Zibeon the Hivite,",
      "M": "Esau took his wives from the women of Canaan: Adah daughter of Elon the Hittite, and Oholibamah daughter of Anah and granddaughter of Zibeon the Hivite—",
      "T": "Esau had taken his wives from among the Canaanite women: Adah the daughter of Elon the Hittite; Oholibamah the daughter of Anah, granddaughter of Zibeon the Hivite;"
    },
    "3": {
      "L": "and Basemath, Ishmael's daughter, the sister of Nebaioth.",
      "M": "also Basemath daughter of Ishmael and sister of Nebaioth.",
      "T": "and Basemath, Ishmael's daughter, the sister of Nebaioth."
    },
    "4": {
      "L": "Adah bore to Esau, Eliphaz; Basemath bore Reuel;",
      "M": "Adah bore Eliphaz to Esau, Basemath bore Reuel,",
      "T": "Adah bore Eliphaz to Esau; Basemath bore Reuel;"
    },
    "5": {
      "L": "and Oholibamah bore Jeush, Jalam, and Korah. These are the sons of Esau who were born to him in the land of Canaan.",
      "M": "and Oholibamah bore Jeush, Jalam and Korah. These were the sons of Esau, who were born to him in Canaan.",
      "T": "and Oholibamah bore Jeush, Jalam, and Korah. These were the sons born to Esau in the land of Canaan."
    },
    "6": {
      "L": "Then Esau took his wives, his sons, his daughters, and all the members of his household, his livestock, all his beasts, and all his property that he had acquired in the land of Canaan. He went into a land away from his brother Jacob.",
      "M": "Esau took his wives and sons and daughters and all the members of his household, as well as his livestock and all his other animals and all the goods he had acquired in Canaan, and moved to a land some distance from his brother Jacob.",
      "T": "Esau took his wives, sons, daughters, and everyone in his household—along with his livestock and all the possessions he had accumulated in Canaan—and moved to a land far from his brother Jacob."
    },
    "7": {
      "L": "For their possessions were too great for them to dwell together. The land of their sojournings could not support them because of their livestock.",
      "M": "Their possessions had become too great for them to remain together; the land where they were staying could not support them both because of their livestock.",
      "T": "Their combined possessions were simply too great to remain in the same place. The land could not support both of them because of their enormous flocks and herds."
    },
    "8": {
      "L": "So Esau settled in the hill country of Seir. Esau is Edom.",
      "M": "So Esau (that is, Edom) settled in the hill country of Seir.",
      "T": "So Esau—that is, Edom—settled in the hill country of Seir."
    },
    "9": {
      "L": "These are the generations of Esau the father of the Edomites in the hill country of Seir.",
      "M": "This is the account of the family line of Esau the father of the Edomites in the hill country of Seir.",
      "T": "This is the family line of Esau, ancestor of the Edomites in the hill country of Seir."
    },
    "10": {
      "L": "These are the names of Esau's sons: Eliphaz the son of Adah the wife of Esau, Reuel the son of Basemath the wife of Esau.",
      "M": "These are the names of Esau's sons: Eliphaz, the son of Esau's wife Adah, and Reuel, the son of Esau's wife Basemath.",
      "T": "Esau's sons: Eliphaz, born to his wife Adah; and Reuel, born to his wife Basemath."
    },
    "11": {
      "L": "The sons of Eliphaz were Teman, Omar, Zepho, Gatam, and Kenaz.",
      "M": "The sons of Eliphaz: Teman, Omar, Zepho, Gatam and Kenaz.",
      "T": "Eliphaz's sons: Teman, Omar, Zepho, Gatam, and Kenaz."
    },
    "12": {
      "L": "(Timna was a concubine of Eliphaz, Esau's son; she bore Amalek to Eliphaz.) These are the sons of Adah, Esau's wife.",
      "M": "(Esau's son Eliphaz also had a concubine named Timna, who bore him Amalek.) These were grandsons of Esau's wife Adah.",
      "T": "(Eliphaz also had a concubine named Timna, who bore him Amalek—ancestor of the Amalekites.) These were the grandsons through Esau's wife Adah."
    },
    "13": {
      "L": "These are the sons of Reuel: Nahath, Zerah, Shammah, and Mizzah. These are the sons of Basemath, Esau's wife.",
      "M": "The sons of Reuel: Nahath, Zerah, Shammah and Mizzah. These were grandsons of Esau's wife Basemath.",
      "T": "Reuel's sons: Nahath, Zerah, Shammah, and Mizzah. These were the grandsons through Esau's wife Basemath."
    },
    "14": {
      "L": "These are the sons of Oholibamah the daughter of Anah the daughter of Zibeon, Esau's wife: she bore to Esau Jeush, Jalam, and Korah.",
      "M": "The sons of Esau's wife Oholibamah daughter of Anah and granddaughter of Zibeon, whom she bore to Esau: Jeush, Jalam and Korah.",
      "T": "The sons of Oholibamah—daughter of Anah, granddaughter of Zibeon, and wife of Esau—whom she bore to Esau: Jeush, Jalam, and Korah."
    },
    "15": {
      "L": "These are the chiefs of the sons of Esau. The sons of Eliphaz the firstborn of Esau: the chiefs Teman, Omar, Zepho, Kenaz,",
      "M": "These were the chiefs among Esau's descendants: The sons of Esau's firstborn Eliphaz: Chiefs Teman, Omar, Zepho, Kenaz,",
      "T": "These were the clan chiefs among Esau's descendants: From Eliphaz, Esau's firstborn: Chief Teman, Chief Omar, Chief Zepho, Chief Kenaz,"
    },
    "16": {
      "L": "Korah, Gatam, and Amalek; these are the chiefs of Eliphaz in the land of Edom; these are the sons of Adah.",
      "M": "Chief Korah, Chief Gatam and Chief Amalek. These were the chiefs descended from Eliphaz in Edom; they were grandsons of Adah.",
      "T": "Chief Korah, Chief Gatam, and Chief Amalek. These were the chiefs descended from Eliphaz in the land of Edom—grandsons through Adah."
    },
    "17": {
      "L": "These are the sons of Reuel, Esau's son: the chiefs Nahath, Zerah, Shammah, and Mizzah; these are the chiefs of Reuel in the land of Edom; these are the sons of Basemath, Esau's wife.",
      "M": "The sons of Esau's son Reuel: Chiefs Nahath, Zerah, Shammah and Mizzah. These were the chiefs descended from Reuel in Edom; they were grandsons of Esau's wife Basemath.",
      "T": "From Reuel, Esau's son: Chief Nahath, Chief Zerah, Chief Shammah, and Chief Mizzah. These were the chiefs descended from Reuel in the land of Edom—grandsons through Esau's wife Basemath."
    },
    "18": {
      "L": "These are the sons of Oholibamah, Esau's wife: the chiefs Jeush, Jalam, and Korah; these are the chiefs born of Oholibamah the daughter of Anah, Esau's wife.",
      "M": "The sons of Esau's wife Oholibamah: Chiefs Jeush, Jalam and Korah. These were the chiefs descended from Esau's wife Oholibamah daughter of Anah.",
      "T": "From Oholibamah, Esau's wife: Chief Jeush, Chief Jalam, and Chief Korah. These were the chiefs descended from Oholibamah daughter of Anah, Esau's wife."
    },
    "19": {
      "L": "These are the sons of Esau (that is, Edom), and these are their chiefs.",
      "M": "These were the sons of Esau (that is, Edom), and these were their chiefs.",
      "T": "These were the sons of Esau—that is, Edom—and these were their chiefs."
    },
    "20": {
      "L": "These are the sons of Seir the Horite, the inhabitants of the land: Lotan, Shobal, Zibeon, Anah,",
      "M": "These were the sons of Seir the Horite, who were living in the region: Lotan, Shobal, Zibeon, Anah,",
      "T": "These were the sons of Seir the Horite, the original inhabitants of the land: Lotan, Shobal, Zibeon, Anah,"
    },
    "21": {
      "L": "Dishon, Ezer, and Dishan; these are the chiefs of the Horites, the sons of Seir in the land of Edom.",
      "M": "Dishon, Ezer and Dishan. These sons of Seir in Edom were Horite chiefs.",
      "T": "Dishon, Ezer, and Dishan. These were the Horite chiefs, descendants of Seir in the land of Edom."
    },
    "22": {
      "L": "The sons of Lotan were Hori and Hemam; and Lotan's sister was Timna.",
      "M": "The sons of Lotan: Hori and Homam. Timna was Lotan's sister.",
      "T": "Lotan's sons: Hori and Hemam. Lotan's sister was Timna."
    },
    "23": {
      "L": "These are the sons of Shobal: Alvan, Manahath, Ebal, Shepho, and Onam.",
      "M": "The sons of Shobal: Alvan, Manahath, Ebal, Shepho and Onam.",
      "T": "Shobal's sons: Alvan, Manahath, Ebal, Shepho, and Onam."
    },
    "24": {
      "L": "These are the sons of Zibeon: Aiah and Anah; he is the Anah who found the hot springs in the wilderness, as he pastured the donkeys of Zibeon his father.",
      "M": "The sons of Zibeon: Aiah and Anah. This is the Anah who discovered the hot springs in the desert while he was grazing the donkeys of his father Zibeon.",
      "T": "Zibeon's sons: Aiah and Anah. This is the Anah who discovered the hot springs in the desert while tending his father Zibeon's donkeys."
    },
    "25": {
      "L": "These are the children of Anah: Dishon and Oholibamah the daughter of Anah.",
      "M": "The children of Anah: Dishon and Oholibamah daughter of Anah.",
      "T": "Anah's children: Dishon and Oholibamah the daughter of Anah."
    },
    "26": {
      "L": "These are the sons of Dishon: Hemdan, Eshban, Ithran, and Cheran.",
      "M": "The sons of Dishon: Hemdan, Eshban, Ithran and Keran.",
      "T": "Dishon's sons: Hemdan, Eshban, Ithran, and Cheran."
    },
    "27": {
      "L": "These are the sons of Ezer: Bilhan, Zaavan, and Akan.",
      "M": "The sons of Ezer: Bilhan, Zaavan and Akan.",
      "T": "Ezer's sons: Bilhan, Zaavan, and Akan."
    },
    "28": {
      "L": "These are the sons of Dishan: Uz and Aran.",
      "M": "The sons of Dishan: Uz and Aran.",
      "T": "Dishan's sons: Uz and Aran."
    },
    "29": {
      "L": "These are the chiefs of the Horites: the chiefs Lotan, Shobal, Zibeon, Anah,",
      "M": "These were the Horite chiefs: Chiefs Lotan, Shobal, Zibeon, Anah,",
      "T": "These were the Horite chiefs: Chief Lotan, Chief Shobal, Chief Zibeon, Chief Anah,"
    },
    "30": {
      "L": "Dishon, Ezer, and Dishan; these are the chiefs of the Horites, chief by chief in the land of Seir.",
      "M": "Dishon, Ezer and Dishan. These were the Horite chiefs, according to their divisions, in the land of Seir.",
      "T": "Chief Dishon, Chief Ezer, and Chief Dishan. These were the Horite chiefs, listed by division, in the land of Seir."
    },
    "31": {
      "L": "These are the kings who reigned in the land of Edom, before any king reigned over the Israelites.",
      "M": "These were the kings who reigned in Edom before any Israelite king reigned:",
      "T": "These are the kings who ruled in the land of Edom before any king reigned over Israel:"
    },
    "32": {
      "L": "Bela the son of Beor reigned in Edom, the name of his city being Dinhabah.",
      "M": "Bela son of Beor became king of Edom. His city was named Dinhabah.",
      "T": "Bela the son of Beor reigned in Edom, with his capital at Dinhabah."
    },
    "33": {
      "L": "Bela died, and Jobab the son of Zerah of Bozrah reigned in his place.",
      "M": "When Bela died, Jobab son of Zerah from Bozrah succeeded him as king.",
      "T": "When Bela died, Jobab the son of Zerah from Bozrah succeeded him."
    },
    "34": {
      "L": "Jobab died, and Husham of the land of the Temanites reigned in his place.",
      "M": "When Jobab died, Husham from the land of the Temanites succeeded him as king.",
      "T": "When Jobab died, Husham from the land of the Temanites succeeded him."
    },
    "35": {
      "L": "Husham died, and Hadad the son of Bedad, who defeated Midian in the country of Moab, reigned in his place, the name of his city being Avith.",
      "M": "When Husham died, Hadad son of Bedad, who defeated Midian in the country of Moab, succeeded him as king. His city was named Avith.",
      "T": "When Husham died, Hadad the son of Bedad—who had defeated Midian in the territory of Moab—succeeded him. His capital was Avith."
    },
    "36": {
      "L": "Hadad died, and Samlah of Masrekah reigned in his place.",
      "M": "When Hadad died, Samlah from Masrekah succeeded him as king.",
      "T": "When Hadad died, Samlah from Masrekah succeeded him."
    },
    "37": {
      "L": "Samlah died, and Shaul of Rehoboth on the Euphrates reigned in his place.",
      "M": "When Samlah died, Shaul from Rehoboth on the river succeeded him as king.",
      "T": "When Samlah died, Shaul from Rehoboth-on-the-River succeeded him."
    },
    "38": {
      "L": "Shaul died, and Baal-hanan the son of Achbor reigned in his place.",
      "M": "When Shaul died, Baal-Hanan son of Akbor succeeded him as king.",
      "T": "When Shaul died, Baal-hanan the son of Achbor succeeded him."
    },
    "39": {
      "L": "Baal-hanan the son of Achbor died, and Hadar reigned in his place, the name of his city being Pau; his wife's name was Mehetabel, the daughter of Matred, daughter of Mezahab.",
      "M": "When Baal-Hanan son of Akbor died, Hadad succeeded him as king. His city was named Pau, and his wife's name was Mehetabel daughter of Matred, the daughter of Me-Zahab.",
      "T": "When Baal-hanan died, Hadar succeeded him. His capital was Pau; his wife's name was Mehetabel, the daughter of Matred and granddaughter of Mezahab."
    },
    "40": {
      "L": "These are the names of the chiefs of Esau, according to their clans and their dwelling places, by their names: the chiefs Timna, Alvah, Jetheth,",
      "M": "These were the chiefs descended from Esau, by name, according to their clans and regions: Chiefs Timna, Alvah, Jetheth,",
      "T": "These were the chiefs descended from Esau, listed by name according to their clans and territories: Chief Timna, Chief Alvah, Chief Jetheth,"
    },
    "41": {
      "L": "Oholibamah, Elah, Pinon,",
      "M": "Oholibamah, Elah, Pinon,",
      "T": "Chief Oholibamah, Chief Elah, Chief Pinon,"
    },
    "42": {
      "L": "Kenaz, Teman, Mibzar,",
      "M": "Kenaz, Teman, Mibzar,",
      "T": "Chief Kenaz, Chief Teman, Chief Mibzar,"
    },
    "43": {
      "L": "Magdiel, and Iram; these are the chiefs of Edom (that is, Esau, the father of Edom), according to their dwelling places in the land of their possession.",
      "M": "Magdiel and Iram. These were the chiefs of Edom, according to their settlements in the land they occupied. This was Esau the father of the Edomites.",
      "T": "Chief Magdiel and Chief Iram. These were the chiefs of Edom—that is, Esau, father of the Edomites—listed according to their settlements in the land they occupied."
    }
  }
}

for tier, key in [('literal','L'), ('mediating','M'), ('thought','T')]:
    data = load(tier, 'genesis')
    merge_tier(data, GENESIS, key)
    save(tier, 'genesis', data)

print('\nGenesis 31–36 written to all three tiers.')
print('Chapters covered:', sorted(GENESIS.keys(), key=int))
