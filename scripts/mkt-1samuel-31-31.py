"""
MKT 1 Samuel chapter 31 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-1samuel-31-31.py

Translation decisions:
- H3068 (יהוה): not present in ch 31; the chapter is entirely secular-narrative with no invocation of
  the divine name. This silence is itself significant — contrast with 30:8 where David inquires of the
  LORD. The divine name's absence in Saul's death narrative is noted in T tier where relevant.
- H6189 (ʿārēl, "uncircumcised"): v4 — Saul's dread is not merely of death but of ritual shame and
  post-mortem humiliation at Philistine hands. L "uncircumcised," M "uncircumcised," T surfaces the
  honor-shame dimension explicitly.
- H5953 (ʿālaʿ, "abuse/deal wantonly with"): v4 — the verb connotes both physical mutilation and
  sexual violation/mockery of a defeated enemy. L "abuse," M "abuse," T "have their sport with me"
  (making the shame motive explicit).
- H2428 (ḥayil, "valor/force"): v12 — rendered L "valiant men," M "fighting men," T reads as "every
  fighting man." The men of Jabesh-gilead owe their town's existence to Saul (1 Sam 11); the T tier
  makes this covenant-loyalty explicit in v11/v12.
- H815 (ʾēshel, "tamarisk"): v13 — the same tree under which Saul sat in 22:6 when he rallied his
  men. The burial under this species carries quiet poetic resonance; T notes it.
- H6912 (qābar, "bury"): v13 — simple burial of bones after burning. The burning (v12) was likely
  practical (preventing further Philistine desecration), not cremation for ritual reasons. This
  aligns with the urgency of the night march.
- Aspect notes: waw-consecutive imperfects throughout = narrative past; translated as simple past
  in L/M. Perfect verbs (h 31:6 "died") = completed acts; so rendered.
- Honor-shame: the entire chapter turns on the theme of the body's honor in death. Saul's request in
  v4 is motivated by shame (not wanting to become a Philistine trophy). The Jabesh-gilead men's night
  march is an act of covenant loyalty that restores Saul's honor in death.
- OT echo: Jabesh-gilead's rescue of Saul's body echoes 1 Sam 11 (Saul's first military act was
  rescuing Jabesh-gilead from Nahash). The T tier notes this covenantal arc in v11/v13.
- No textual-critical issues; the chapter is stable across MT/LXX. The LXX expands v12 slightly
  (adds "in Jabesh") but the MT reading is followed.
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

SAMUEL = {
  "31": {
    "1": {
      "L": "Now the Philistines fought against Israel, and the men of Israel fled from before the Philistines and fell slain in mount Gilboa.",
      "M": "The Philistines attacked Israel, and the Israelites fled before them, falling slain on Mount Gilboa.",
      "T": "The reckoning came at Gilboa. The Philistines drove into Israel and Israel broke—the men fleeing, falling, dying on the open slopes of the mountain."
    },
    "2": {
      "L": "And the Philistines followed hard on Saul and his sons, and the Philistines killed Jonathan and Abinadab and Malchishua, the sons of Saul.",
      "M": "The Philistines closed in hard on Saul and his sons, killing Jonathan, Abinadab, and Malchishua.",
      "T": "The Philistines drove straight for Saul and his sons. Jonathan fell. Abinadab fell. Malchishua fell. Three sons dead on the same field as their father."
    },
    "3": {
      "L": "And the battle was heavy against Saul, and the archers found him, and he was sorely wounded by the archers.",
      "M": "The battle pressed hard against Saul. The archers found their mark, and he was badly wounded.",
      "T": "The battle closed around Saul himself. The archers found him, and the wounds were severe—mortal."
    },
    "4": {
      "L": "Then Saul said to his armor-bearer, Draw your sword and thrust me through with it, lest these uncircumcised come and thrust me through and abuse me. But his armor-bearer would not, for he was very afraid; therefore Saul took a sword and fell upon it.",
      "M": "Saul said to his armor-bearer, 'Draw your sword and run me through—I don't want these uncircumcised men to come and abuse me.' But his armor-bearer was too terrified to do it. So Saul took his own sword and fell on it.",
      "T": "Saul had one fear left—not death but the shame of capture. 'Kill me now,' he told his armor-bearer, 'before these Philistines get their hands on me and have their sport with me.' The armor-bearer could not move. So Saul took matters into his own hands: he fell on his sword."
    },
    "5": {
      "L": "And when his armor-bearer saw that Saul was dead, he also fell on his sword and died with him.",
      "M": "When his armor-bearer saw that Saul was dead, he too fell on his own sword and died with him.",
      "T": "The armor-bearer saw Saul dead and could not outlive him. He fell on his own sword and died at Saul's side."
    },
    "6": {
      "L": "So Saul died, and his three sons, and his armor-bearer, and all his men together on that same day.",
      "M": "So Saul died, along with his three sons, his armor-bearer, and all his men—all on that same day.",
      "T": "In a single day: Saul dead. His three sons dead. His armor-bearer dead. All his men. A dynasty ended between sunrise and sunset."
    },
    "7": {
      "L": "And when the men of Israel who were on the other side of the valley and on the other side of the Jordan saw that the men of Israel had fled and that Saul and his sons were dead, they forsook the cities and fled; and the Philistines came and dwelt in them.",
      "M": "When the Israelites on the far side of the valley and across the Jordan saw that the army had fled and that Saul and his sons were dead, they abandoned their cities and fled. The Philistines came and settled in them.",
      "T": "Word of the disaster traveled fast. Israelites on the valley's far side and beyond the Jordan saw the rout and understood—Saul was dead, his sons were dead, the army was broken. They abandoned their towns and ran. The Philistines moved in and claimed them."
    },
    "8": {
      "L": "And it came to pass on the morrow, when the Philistines came to strip the slain, that they found Saul and his three sons fallen on mount Gilboa.",
      "M": "The next day, when the Philistines came to plunder the dead, they found Saul and his three sons lying fallen on Mount Gilboa.",
      "T": "The day after the battle, the Philistines worked the field—stripping the slain of armor and weapons. They found Saul and his three sons where they had fallen on Gilboa's slope."
    },
    "9": {
      "L": "And they cut off his head and stripped off his armor, and sent throughout the land of the Philistines round about to carry the good news to their idols and to the people.",
      "M": "They cut off his head, stripped his armor, and sent messengers throughout Philistia to announce the victory to their idols and to the people.",
      "T": "They beheaded Saul, stripped the royal armor from his body, and dispatched messengers to race through every Philistine city—proclaiming the victory before their idols and to the people. Saul had become a trophy of war."
    },
    "10": {
      "L": "And they put his armor in the house of the Ashtaroth, and they fastened his body to the wall of Beth-shan.",
      "M": "They placed his armor in the temple of Ashtaroth and pinned his body to the wall of Beth-shan.",
      "T": "His armor was dedicated as a war trophy in the temple of Ashtaroth. His body was nailed to the wall of Beth-shan for all to see—public humiliation in death, exactly the fate he had tried to prevent."
    },
    "11": {
      "L": "And when the inhabitants of Jabesh-gilead heard what the Philistines had done to Saul,",
      "M": "When the people of Jabesh-gilead heard what the Philistines had done to Saul,",
      "T": "But word reached Jabesh-gilead—the town whose existence Saul had secured in his first act as king, when he routed Nahash the Ammonite."
    },
    "12": {
      "L": "all the valiant men arose and went all night and took the body of Saul and the bodies of his sons from the wall of Beth-shan, and came to Jabesh and burned them there.",
      "M": "all their fighting men rose, traveled through the night, took the bodies of Saul and his sons from the wall of Beth-shan, brought them to Jabesh, and burned them there.",
      "T": "Every fighting man in Jabesh rose and marched through the night—a night march of covenant loyalty. They pulled Saul and his sons from the wall of Beth-shan and carried them home. At Jabesh they burned the bodies—protecting them from further desecration."
    },
    "13": {
      "L": "And they took their bones and buried them under the tamarisk tree at Jabesh and fasted seven days.",
      "M": "They gathered the bones and buried them under the tamarisk tree at Jabesh, then fasted for seven days.",
      "T": "They buried the bones under the tamarisk at Jabesh and kept seven days of mourning. Saul had sat beneath a tamarisk in Gibeah (22:6) to hold his last court before his decline; he was laid to rest beneath another. The men of Jabesh honored what they owed him. The debt was paid."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, '1samuel')
        merge_tier(existing, SAMUEL, tier_key)
        save(tier_dir, '1samuel', existing)
    print('1 Samuel 31 written.')

if __name__ == '__main__':
    main()
