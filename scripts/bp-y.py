#!/usr/bin/env python3
import json, os

OUT_DIR = '../data/biblepedia/articles'
os.makedirs(OUT_DIR, exist_ok=True)

def merge_article(slug, data):
    path = os.path.join(OUT_DIR, f'{slug}.json')
    if os.path.exists(path):
        return False
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)
    return True

ARTICLES = {
"yarn": {
  "id": "yarn",
  "term": "Yarn",
  "category": "concepts",
  "intro": "<p>\"Yarn\" appears in the Authorized Version of <strong>1 Kings 10:28</strong> and <strong>2 Chronicles 1:16</strong>, where it is said that Solomon's merchants received \"linen yarn\" from Egypt at a price. The Hebrew word rendered thus is <em>mikveh</em>, meaning \"a stringing together\" or \"a company.\" Modern scholarship and the Revised Version reject the translation \"linen yarn\" in favor of \"droves\" of horses: the king's merchants received horses from Egypt in droves, each at a set price.</p><p>The confusion arose from a misreading of the Hebrew text. Smith's dictionary likewise notes the passage is \"extremely obscure\" and that Gesenius preferred to read <em>mikveh</em> as referring to a band or company of the merchants themselves buying a drove of horses. There is no credible reference to the textile trade in this context; the verse concerns Solomon's horse-trading with Egypt and Kue (Cilicia).</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["1 Kings 10:28", "2 Chronicles 1:16"]
},

"year": {
  "id": "year",
  "term": "Year",
  "category": "concepts",
  "intro": "<p>The Hebrew word for year, <em>shanah</em>, signifies \"repetition\" or \"revolution\" (<strong>Gen. 1:14</strong>; <strong>5:3</strong>). The Israelites reckoned two parallel years: a <em>sacred calendar</em> beginning at the vernal equinox with the month Abib (later called Nisan), inaugurated at the Exodus; and a <em>civil calendar</em> beginning at the autumnal equinox. The year was essentially solar in its agricultural anchoring — harvest festivals were fixed to seasonal dates — but the months were lunar, each opening with a new moon, requiring periodic intercalation of a thirteenth month to keep the calendar aligned with the sun.</p><p>An earlier 360-day year (twelve months of thirty days) appears to underlie the flood narrative in Genesis. Egyptian reckoning used twelve 30-day months plus five added days. The Jewish year now begins with the month Tishri. The sacred-civil dual reckoning explains apparent inconsistencies in dating across Old Testament narratives.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["Genesis 1:14", "Genesis 5:3", "Exodus 12:2", "Leviticus 23:5"]
},

"yeshebi": {
  "id": "yeshebi",
  "term": "Yeshebi",
  "category": "places",
  "intro": "<p>Yeshebi is a Hebrew word rendered \"inhabitants\" in <strong>Joshua 17:7</strong> in the Authorized Version, where it appears in the description of the boundary of Manasseh. Easton's dictionary suggests it is more likely a proper place name — possibly the village of Yashepheh, tentatively identified with modern Yassuf, approximately eight miles south of Shechem in the hill country of Ephraim.</p><p>The site sits near the frontier between Manasseh and Ephraim, which Joshua 17 carefully demarcates. If Yeshebi is indeed a village name rather than a common noun, its appearance marks a boundary landmark in the tribal allotments of the central highlands, though its exact identification remains uncertain.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton"],
  "key_refs": ["Joshua 17:7"]
},

"yoke": {
  "id": "yoke",
  "term": "Yoke",
  "category": "concepts",
  "intro": "<p>In its primary sense the yoke was a curved wooden bar fitted across the necks of a pair of oxen to bind them to the traces of a plough or cart (<strong>Num. 19:2</strong>; <strong>Deut. 21:3</strong>). The Hebrew <em>ʿol</em> denotes this implement; a second word, <em>motah</em> (\"bar\" or \"staff\"), appears in Jeremiah 27–28 where the Revised Version renders it \"bar\" rather than \"yoke.\" A third term, <em>tzemed</em>, means \"a pair\" of yoked oxen and by extension came to denote the area of land such a pair could plough in one day — equivalent to the Latin <em>jugum</em> and translated \"acre\" in Isaiah 5:10.</p><p>Both Hebrew terms are used extensively as metaphors for subjection, oppression, and servitude (<strong>Lev. 26:13</strong>; <strong>1 Kings 12:4</strong>; <strong>Isa. 47:6</strong>; <strong>Lam. 1:14</strong>). An \"iron yoke\" denotes especially galling bondage. In the New Testament Jesus invites his followers to take his yoke — describing discipleship as a light burden set against the heavy yoke of the law (<strong>Matt. 11:29–30</strong>); Paul applies the same imagery to warn against returning to the yoke of slavery under the law (<strong>Gal. 5:1</strong>; <strong>Acts 15:10</strong>).</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["Matthew 11:29", "Galatians 5:1", "1 Kings 12:4", "Numbers 19:2"]
},

"yoke-fellow": {
  "id": "yoke-fellow",
  "term": "Yoke-fellow",
  "category": "people",
  "intro": "<p>\"Yoke-fellow\" (Greek <em>syzygos</em>, meaning \"one yoked together with\") appears in <strong>Philippians 4:3</strong>, where Paul writes: \"I ask you also, true companion, help these women.\" The term denotes a partner sharing the same burden of apostolic work. Some interpreters take <em>syzygos</em> as a personal name (Syzygus), though this usage is unattested. Wycliffe rendered the phrase \"thee, germane felowe,\" meaning \"genuine comrade.\"</p><p>Several early commentators identified the unnamed yoke-fellow with Epaphroditus, the bearer of the letter to Philippi, while others have suggested Silas, Luke, or Timothy. The ambiguity is unresolvable from the text alone. What the passage makes clear is that the person was closely associated with Paul's missionary labor — sharing a common yoke with him in the proclamation of the gospel — and was trusted to mediate a dispute between Euodia and Syntyche, two women who had \"labored side by side\" with Paul.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton"],
  "key_refs": ["Philippians 4:3"]
},
}

def main():
    written = skipped = 0
    for slug, data in ARTICLES.items():
        if merge_article(slug, data):
            written += 1
        else:
            skipped += 1
    print(f"BP y: Yarn → Yoke-fellow: wrote {written}, skipped {skipped} existing.")

main()
