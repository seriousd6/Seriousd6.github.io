"""
Echo layer -- Jeremiah chapters 41-45
Run: python3 scripts/zc-echo-jeremiah-41-45.py

Chapters covered:
- Ch41: Gedaliah's assassination; Ishmael's atrocities; the remnant's fear-driven flight to Egypt
- Ch42: The remnant's oath to obey YHWH, the ten-day wait, God's conditional promise to the land
- Ch43: Disobedience; rejection of the prophetic word; Jeremiah's symbolic act at Tahpanhes
- Ch44: YHWH's indictment of idolatry in Egypt; the queen of heaven controversy; the remnant's defiance
- Ch45: Baruch's personal lament; YHWH's answer: no great things, but your life as plunder

Key NT connections:
- 42:5-6:  oath to obey God's word (then broken) -- James 1:22-24
- 42:10-12: I am with you to save -- Matt 28:20; Heb 13:5
- 43:2-4:  rejecting the prophet's word -- 2 Tim 4:3-4
- 43:10:   Nebuchadnezzar "my servant" -- Acts 4:27-28; Rom 13:1
- 44:4:    servants the prophets sent again and again -- Matt 21:34-37
- 44:17:   queen of heaven; idolatry defended -- 1 Cor 10:14; Rev 2:20
- 44:28:   whose word will stand -- 2 Pet 1:21; Matt 24:35
- 45:3:    weary with groaning, no rest -- Matt 11:28
- 45:5:    not seeking great things; life as prize -- Mark 10:43-45; Luke 21:19
"""

import json, pathlib

ROOT = pathlib.Path(__file__).parent.parent

def load_echo(book):
    p = ROOT / "data" / "echoes" / f"{book}.json"
    return json.loads(p.read_text()) if p.exists() else {}

def save_echo(book, data):
    p = ROOT / "data" / "echoes" / f"{book}.json"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=None))
    print(f"  wrote {p.relative_to(ROOT)}")

def merge_echo(existing, new_data):
    for ch, verses in new_data.items():
        if ch not in existing:
            existing[ch] = {}
        for v, entries in verses.items():
            if v not in existing[ch]:
                existing[ch][v] = entries
            else:
                seen = {(e["type"], e["target"]) for e in existing[ch][v]}
                for e in entries:
                    if (e["type"], e["target"]) not in seen:
                        existing[ch][v].append(e)
                        seen.add((e["type"], e["target"]))

JEREMIAH_ECHOES = {
  "41": {
    "5": [
      {"type": "allusion", "target": "Heb 13:15", "note": "Eighty pilgrims come from Shechem, Shiloh, and Samaria with grain offerings and incense for the ruined house of the LORD -- the impulse to bring worship to YHWH even in the desolation of the temple's destruction anticipates the NT principle that the sacrifice of praise through Christ does not require a standing temple (Heb 13:15: through Christ let us continually offer up a sacrifice of praise to God, the fruit of lips that acknowledge his name); worship persists beyond the institution"}
    ],
    "17": [
      {"type": "allusion", "target": "2 Tim 1:7", "note": "They set out for Egypt because they were afraid of the Chaldeans -- the fear that drives the remnant away from God's appointed path is the spirit 2 Tim 1:7 contrasts with the Spirit of God: God gave us not a spirit of fear but of power and love and self-control; the paralyzing fear that propels the remnant toward Egypt rather than toward trust in YHWH's protection is the recurring OT manifestation of what the Spirit of Christ is sent to overcome"}
    ]
  },
  "42": {
    "5": [
      {"type": "allusion", "target": "James 1:22", "note": "May the LORD be a true and faithful witness against us if we do not act in accordance with all that the LORD your God sends you to tell us -- the gap between promise to obey and actual obedience (the remnant swears fidelity, then immediately defies the word they receive) is the structural problem James addresses: be doers of the word, and not hearers only, deceiving yourselves (James 1:22); the Jeremianic remnant is the OT illustration of the self-deceiving hearer who never acts on what God said"}
    ],
    "7": [
      {"type": "allusion", "target": "Acts 1:4", "note": "At the end of ten days the word of the LORD came to Jeremiah -- the ten-day wait before receiving divine guidance after earnest seeking is the OT pattern of disciplined waiting on God's word; Acts 1:4 records Jesus commanding the disciples to wait in Jerusalem for the promise of the Father; in both cases, faithful action is conditioned on prior waiting for God's timing rather than proceeding on human urgency"},
    ],
    "10": [
      {"type": "allusion", "target": "Matt 28:20", "note": "I will build you up and not tear you down, and I will plant you and not uproot you, for I am with you to save you -- the covenant-presence promise that God gives to the remnant if they remain in the land is the OT form of Jesus's closing commission promise: I am with you always, to the end of the age (Matt 28:20); the divine presence that makes faithfulness possible despite impossible circumstances is the constant offered to the covenant community across both testaments"},
      {"type": "allusion", "target": "Heb 13:5", "note": "I will rescue you from the power of the Babylonian king -- the promise of divine rescue for those who trust and remain in God's appointed place echoes the assurance Hebrews draws from Joshua: I will never leave you nor forsake you (Heb 13:5, citing Josh 1:5); the remnant's failure to trust this promise repeats the pattern that Hebrews warns the NT church not to repeat -- hardening the heart when the word says trust and remain"}
    ],
    "16": [
      {"type": "allusion", "target": "Matt 6:34", "note": "The sword you fear will overtake you in Egypt, and the famine you dread will pursue you right into Egypt -- the thing the remnant flees toward (Egypt as safety from sword and famine) becomes the place where the sword and famine find them; Jesus's teaching addresses this irony directly: do not be anxious about tomorrow, for tomorrow will be anxious for itself (Matt 6:34); the anxious pursuit of security through self-managed escape from God's appointed path is precisely what produces the disaster being fled"}
    ]
  },
  "43": {
    "2": [
      {"type": "allusion", "target": "2 Tim 4:3", "note": "You are speaking falsely! The LORD our God has not sent you -- the remnant rejects Jeremiah's word the moment it conflicts with their prior decision; 2 Tim 4:3 predicts that people will not endure sound teaching but will accumulate teachers to suit their own passions and will turn away from the truth; the Jeremianic pattern -- seeking a prophet's counsel, then accusing him of lying when his word is inconvenient -- is the archetype of the itching-ears syndrome the NT warns about"}
    ],
    "10": [
      {"type": "allusion", "target": "Acts 4:28", "note": "I am going to send for Nebuchadnezzar king of Babylon, my servant -- the pagan conqueror is YHWH's instrument of judgment; the designation of a pagan ruler as God's servant for divine purposes is the OT ground for the NT's theology of divine sovereignty over hostile human powers: Herod and Pontius Pilate gathered to do whatever God's hand and plan had predestined to take place (Acts 4:27-28); in both cases, the human agents executing destructive power are instruments of a higher purpose"},
      {"type": "allusion", "target": "Rom 13:1", "note": "Nebuchadnezzar king of Babylon, my servant -- the appointment of pagan rulers as divine servants for temporal purposes underlies Paul's instruction: there is no authority except from God, and those that exist have been instituted by God (Rom 13:1); Nebuchadnezzar as YHWH's servant is the strongest OT statement of this principle -- even the destroyer of Jerusalem serves the divine purpose"}
    ]
  },
  "44": {
    "4": [
      {"type": "allusion", "target": "Matt 21:34", "note": "I sent you all my servants the prophets, again and again, urgently, saying: Do not do this detestable thing that I hate -- the pattern of repeated prophetic sending that is consistently rejected is exactly the dynamic Jesus dramatizes in the parable of the tenants: a man sends servant after servant, all of whom are beaten or killed by the tenants (Matt 21:34-36); then he sends his son, who is killed last; Jesus's parable is the Christological recapitulation of Jeremiah's pattern, identifying himself as the final sending"},
      {"type": "allusion", "target": "Heb 1:1", "note": "I sent all my servants the prophets, again and again, urgently -- the serial prophetic sending that characterizes YHWH's patience with Israel in the OT is the background for Hebrews' opening statement: in many times and in many ways God spoke of old to the fathers by the prophets; Jer 44:4 captures the persistence and urgency of that prophetic sending that culminates in the Son (Heb 1:2)"}
    ],
    "17": [
      {"type": "allusion", "target": "1 Cor 10:14", "note": "We will do everything we have vowed -- making offerings to the queen of heaven -- the women defend their idolatry with a prosperity argument: when we burned offerings to her, we had plenty of food; 1 Cor 10:14 confronts this same logic in the NT context: flee from idolatry; Paul's Corinthian audience also faced arguments for accommodation to pagan religious practice, and Paul's counter-argument is that participation in pagan cult is incompatible with participation at the Lord's table (1 Cor 10:21)"},
      {"type": "allusion", "target": "Rev 2:20", "note": "Making offerings to the queen of heaven... we had plenty of food and were well off -- the Jezebel of Thyatira in Rev 2:20 teaches the same accommodation logic: she seduces servants of God to practice sexual immorality and eat food sacrificed to idols; the prosperity argument for idolatry (the queen of heaven gave us prosperity in the past) reappears as the Nicolaitan teaching against which Revelation warns the churches"}
    ],
    "28": [
      {"type": "allusion", "target": "Matt 24:35", "note": "Then they will know whose word has stood -- mine or theirs -- the contest between the prophetic word that stands and the human defiance that is proven empty is the OT form of Jesus's assertion: heaven and earth will pass away but my words will not pass away (Matt 24:35); the fulfilled prophecy of Jeremiah is the precedent for Jesus's absolute confidence in the permanence of his own word"},
      {"type": "allusion", "target": "2 Pet 1:21", "note": "Whose word has stood, mine or theirs -- the difference between the word that comes true (Jeremiah's) and the word that fails (the false prophets') is the OT ground for 2 Peter's defense of prophetic authority: no prophecy of Scripture comes from someone's own interpretation, for no prophecy was ever produced by the will of man, but men spoke from God as they were carried along by the Holy Spirit (2 Pet 1:21)"}
    ]
  },
  "45": {
    "3": [
      {"type": "allusion", "target": "Matt 11:28", "note": "You said: Woe is me! For the LORD has added sorrow to my pain. I am weary with my groaning and I find no rest -- Baruch's depletion in the prophetic ministry -- worn out from writing Jeremiah's words and facing mounting hostility -- is the exact condition Jesus addresses in his invitation: come to me, all who are weary and burdened, and I will give you rest (Matt 11:28); the rest that Baruch cannot find in the prophetic labor under the old covenant is the rest Christ offers to those who come to him"}
    ],
    "5": [
      {"type": "allusion", "target": "Mark 10:43", "note": "Are you seeking great things for yourself? Stop seeking them -- YHWH's rebuke of Baruch's ambition for great personal recognition or safety is the OT form of Jesus's teaching on greatness: whoever wants to be great among you must be your servant... whoever wants to be first among you must be slave of all (Mark 10:43-44); in both cases, the seeking of great things for oneself is the disposition that must be surrendered in faithful service"},
      {"type": "allusion", "target": "Luke 21:19", "note": "I will give you your life as a prize of war wherever you go -- the promise is not prosperity or greatness but bare survival amid universal disaster; Jesus offers his disciples the same limited but certain promise in Luke 21:18-19: not a hair of your head will perish; by your endurance you will gain your lives; both YHWH to Baruch and Christ to his disciples promise life-through-endurance rather than exemption from tribulation"}
    ]
  }
}

def main():
    existing = load_echo("jeremiah")
    merge_echo(existing, JEREMIAH_ECHOES)
    save_echo("jeremiah", existing)
    print("Jeremiah 41-45 echoes written.")

if __name__ == "__main__":
    main()
