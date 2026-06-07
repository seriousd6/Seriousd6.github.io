"""
mkt-christ layer — Acts chapters 27–28
Output: data/commentary/mkt-christ/acts.json
Run: python3 scripts/zc-christ-acts-27-28.py
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
    # INTENT: Merge new verse entries without overwriting already-present keys — safe to re-run.
    # CHANGE? If commentary JSON structure changes from {ch:{v:html}}, update this traversal.
    # VERIFY: Re-running the script should produce identical output.
    for ch, verses in new_data.items():
        if ch not in existing:
            existing[ch] = {}
        for v, html in verses.items():
            if v not in existing[ch]:
                existing[ch][v] = html

NEW = {
  "27": {
    "1": "Paul is handed over to a centurion named Julius for the voyage to Rome — his passage into Roman custody mirrors Jesus being handed over to Roman authorities (Luke 23:1; John 18:28). Both carry out their mission under imperial constraint.",
    "2": "The party boards an Adramyttian ship, beginning the final sea-journey that will end at Rome — fulfilling the trajectory Jesus set in Acts 1:8, from Jerusalem to the ends of the earth.",
    "3": "The centurion Julius shows Paul kindness and lets him visit friends at Sidon — a foreshadowing of the centurion at the cross (Luke 23:47) who recognized the truth about Jesus; now one of Rome's soldiers serves Paul's mission.",
    "4": "The ship sails under the lee of Cyprus because of contrary winds — the journey is difficult from the start, as Paul's passion-pattern narrative has been difficult from Jerusalem onward.",
    "5": "They cross the open sea off Cilicia and Pamphylia — passing the region of Paul's first missionary journey, moving now toward the imperial capital where the testimony must reach.",
    "6": "Julius transfers the prisoners to an Alexandrian grain ship — the largest cargo vessels of antiquity, carrying the bread that sustained the empire; Paul will soon preside over a different bread-breaking aboard this very ship.",
    "7": "Sailing slowly and arriving off Cnidus with difficulty — Luke lingers on the resistance to heighten the contrast with the ultimate deliverance that Paul's word promises.",
    "8": "They reach Fair Havens near the city of Lasea — a name Luke uses with quiet irony; the haven will not prove fair enough, but the God who guides Paul's mission provides a haven that is truly fair at journey's end.",
    "9": "The Fast (Yom Kippur, autumn) has passed and sailing is dangerous — Paul warns that disaster lies ahead. The Day of Atonement is the day Israel's high priest intercedes before God for the people; Paul, apostle of the true High Priest, now intercedes for the ship's company.",
    "10": "Paul warns that the voyage will bring disaster and great loss — a prophetic word from one who carries the Spirit, overruled as prophetic warnings were overruled at every stage of Jesus's passion.",
    "11": "The centurion listens to the pilot and shipowner rather than to Paul — those with worldly expertise are preferred over the apostle, just as the crowd chose Barabbas over Jesus (Luke 23:18).",
    "12": "The majority vote to sail on — a democratic rejection of the prophetic voice, recalling the crowd's cry at the crucifixion. Decisions by human consensus override the word of God.",
    "13": "When a gentle south wind blows they suppose their purpose is achieved — the calm before the storm mirrors every moment of false security before crisis in the passion narrative.",
    "14": "The Euraquilo, a violent northeastern wind, strikes the ship — the great storm bursts in unexpectedly, as violence descended on Jesus in Gethsemane after apparent calm.",
    "15": "The ship is caught and cannot face the wind, so they give way and let it drive — surrender to forces beyond human control, as Jesus surrendered to arrest and prayed that the Father's will be done (Luke 22:42).",
    "16": "Under the shelter of Cauda they secured the lifeboat with difficulty — barely surviving each moment; the preservation of the boat mirrors God's preservation of the remnant through the storm.",
    "17": "They use cables to undergird the ship and lower the sea anchor, fearing the Syrtis shoals — human ingenuity in the face of catastrophe; but the ultimate anchor is the word Paul will receive from God (vv. 23-25).",
    "18": "The storm is so violent that they throw the cargo overboard — loss of everything material precedes the total dependence that leads to salvation; earthly provision is cast away so lives might be saved.",
    "19": "On the third day they throw the ship's tackle overboard with their own hands — Luke marks the third day: throughout Acts and the Gospel, the third day is the day of resurrection and new life. What is lost in three days of storm will be restored.",
    "20": "When neither sun nor stars appear for many days and the storm continues, all hope of being saved is abandoned — the nadir, as at the crucifixion when hope was extinguished and the disciples scattered (Mark 14:50).",
    "21": "Paul stands up and says they should have listened to him — not to condemn but to introduce the word of assurance that follows; as Jesus spoke authoritatively even in a storm-tossed boat (Mark 4:39-41).",
    "22": "Paul urges them to take heart — tharseite, the same word Jesus used when walking on water (Matt 14:27) and in the upper room (John 16:33: take heart, I have overcome the world). Not one of them will be lost.",
    "23": "An angel of the God Paul belongs to and serves has stood beside him — as an angel appeared to Jesus in Gethsemane to strengthen him (Luke 22:43); the same divine provision attends the apostle in his moment of extremity.",
    "24": "The angel declares that Paul must stand before Caesar and that God has granted him all who sail with him — Paul's intercessory presence saves the entire company. As the Father gave disciples to the Son and the Son kept all of them safe (John 17:12), so Paul's apostolic commission encompasses the lives of all entrusted to him.",
    "25": "Paul urges them to take heart again, trusting God that it will happen exactly as he was told — faith in the divine promise against all visible evidence, as Abraham believed God (Rom 4:18-21) and Jesus entrusted himself to the Father (1 Pet 2:23).",
    "26": "Paul says they will run aground on some island — his prophecy is detailed and exact; the word of God given through Paul is more reliable than any instrument of navigation.",
    "27": "On the fourteenth night the sailors detect land — the fourteenth night echoes the Passover night (Exodus 12:6, the 14th of Nisan); deliverance is imminent on the night when God historically acts to save his people.",
    "28": "They sound the depth and find twenty fathoms, then fifteen — the sea grows shallower; the crisis approaches its resolution, as the passion narrative approaches the dawn of resurrection.",
    "29": "Fearing they might run aground on the rocks they let out four anchors and pray for day to come — even pagan sailors pray for dawn; the resurrection dawn that Paul has proclaimed is the only anchor that truly holds.",
    "30": "The sailors attempt to escape in the lifeboat under pretense of dropping anchors — human schemes for self-preservation at the expense of others; the disciples too fled to save themselves (Mark 14:50).",
    "31": "Paul tells the centurion that unless these men stay in the ship no one can be saved — Paul is the mediating voice of salvation; remaining in the vessel together is the condition of deliverance, as remaining in Christ is the condition of life (John 15:4).",
    "32": "The soldiers cut away the lifeboat — a radical act of trust: they destroy the apparent means of escape, throwing themselves entirely on the word Paul has given. Faith required abandoning the fallback.",
    "33": "Just before dawn Paul urges all 276 aboard to eat — the pre-dawn meal before crossing to safety echoes the Passover meal before the Exodus; Paul provides strength for the final crossing.",
    "34": "Paul assures them that not a hair of anyone's head will perish — the exact language Jesus used in Luke 21:18, now fulfilled through Paul's apostolic word.",
    "35": "Paul takes bread, gives thanks to God before all, breaks it, and begins to eat — the eucharistic formula: taking, giving thanks (eucharistesas), breaking (klasas); on the night of greatest danger, Paul presides at a table that echoes the Last Supper (Luke 22:19; 1 Cor 11:23-24).",
    "36": "They all take heart and eat — the meal produces courage and renewed life, as the resurrection appearance meals restored the disciples. The bread of thanksgiving precedes the crossing to safety.",
    "37": "There are 276 persons on the ship — Luke records the exact number; every one of them must be accounted for, as the shepherd counts each sheep (Luke 15:4) and the Father does not lose any given to the Son (John 6:39).",
    "38": "They lighten the ship by throwing the wheat into the sea — the grain cargo that fed the empire is sacrificed so that lives might be saved. The paradox of loss for gain echoes the cross.",
    "39": "Day comes and they make for the beach — resurrection dawn; the voyage toward death has turned toward life.",
    "40": "They cast off the anchors, loosen the rudder ropes, hoist the foresail, and head for the beach — the ship moves toward the shore of deliverance under the providential guidance of the word Paul has proclaimed.",
    "41": "The ship strikes a reef; the bow lodges fast while the stern breaks apart under the waves — the vessel is broken so that its passengers might reach land, as the body of Christ was broken that many might live.",
    "42": "The soldiers plan to kill the prisoners to prevent escape — the threat of death at the moment of deliverance mirrors every violent attempt to thwart God's saving purpose, from the slaughter of the innocents (Matt 2:16) to the orders to kill Jesus (Luke 22:2).",
    "43": "The centurion, wishing to save Paul, prevents the plan and orders those who can swim to jump overboard first — Julius acts to protect Paul as the centurion at the cross bore witness to Jesus (Luke 23:47); Rome's agents repeatedly serve God's plan despite their ignorance.",
    "44": "All 276 escape safely to land — Paul's prophecy is fulfilled exactly: not one hair perished. The complete deliverance of all who sail with the apostle is the sign of resurrection power: death cannot hold those entrusted to God's word.",
  },
  "28": {
    "1": "Once safe on land they learn the island is Malta — after storm and shipwreck comes unexpected refuge; the pattern of death-and-resurrection lands the company in a new place of hospitality and mission.",
    "2": "The native people show unusual kindness, building a fire because of the rain and cold — the welcome Paul receives from pagans anticipates the welcome the Gentile church extends to the gospel; unexpected grace from unexpected people.",
    "3": "Paul gathers sticks and a viper fastens on his hand from the heat — the encounter with the serpent echoes the primeval enmity of Genesis 3:15, where the seed of the woman would be struck by the serpent; Paul, in the apostolic line of that Seed, is struck.",
    "4": "The islanders conclude Paul must be a murderer whom justice does not allow to live — the same logic applied to Jesus: the crowd believed one crucified under Roman authority must be guilty; suffering is read as divine punishment.",
    "5": "Paul shakes the snake into the fire and suffers no harm — the seed of the woman crushes the serpent's head (Gen 3:15); Jesus declared that his disciples would have authority to trample serpents (Luke 10:19), and Paul enacts that promise.",
    "6": "The islanders wait for Paul to swell up or die, but when nothing happens they change their minds and call him a god — the reversal of judgment: one believed cursed is now believed divine. The resurrection of Jesus effected the same reversal: crucified as a criminal, declared Son of God by the Spirit of holiness (Rom 1:4).",
    "7": "Publius, the leading man of the island, receives them for three days with generous hospitality — three days of welcome after shipwreck; the resonance of three days throughout Luke-Acts always points toward the resurrection pattern.",
    "8": "Paul prays and lays his hands on Publius's father, who is healed of fever and dysentery — the gesture and sequence echo Jesus healing Peter's mother-in-law (Mark 1:30-31), who lay ill with fever and was healed by his touch. Paul's healing ministry continues Jesus's own.",
    "9": "When this happens, the rest of the sick on the island come and are healed — as Jesus's healings drew crowds from the whole region (Mark 1:32-34), Paul's single act of healing opens the entire island to the restoration that the kingdom brings.",
    "10": "They honor Paul's company with many gifts and provisions for the voyage — Malta is a type of the new creation: those who encounter the apostolic word are healed, restored, and equipped. The mission is self-sustaining because God provides through those who receive it.",
    "11": "After three months they sail on an Alexandrian ship with the Twin Brothers as figurehead — Castor and Pollux, patron deities of sailors, adorn the ship; Paul rides to Rome under the ironic banner of pagan savior-figures while the apostle of the true Savior carries the message of the one resurrection.",
    "12": "They put in at Syracuse and stay three days — three days again; the resurrection cadence marks each stopping point on the journey to Rome.",
    "13": "They reach Rhegium and Puteoli — the final Italian ports before Rome; the mission is steps away from the heart of the empire.",
    "14": "At Puteoli they find brothers who invite them to stay seven days — a community of resurrection faith already exists in the shadow of Rome. The mission has preceded the apostle.",
    "15": "Brothers from Rome travel to the Forum of Appius and Three Taverns to meet Paul; on seeing them Paul thanks God and takes heart — the verb used for courage (etharsen) is the same root as tharseite, the word Jesus spoke to his disciples (Matt 14:27; John 16:33). The community of the resurrection gives the apostle what the risen Christ gave the disciples: courage to continue.",
    "16": "In Rome Paul is allowed to live by himself with a soldier guarding him — Paul is under guard but not imprisoned; the chain is real but the word is unbound. As the word of God cannot be chained (2 Tim 2:9), so Paul's proclamation continues unimpeded.",
    "17": "Three days after arriving Paul calls together the local Jewish leaders — Paul's first act in Rome comes on the third day after arrival, as the most significant acts of God in Luke-Acts happen on the third day. He presents himself as the faithful Jew who has done nothing against the law or customs.",
    "18": "The Roman authorities examined him and wanted to release him, finding no ground for capital punishment — identical to Pilate's repeated verdict of no guilt (Luke 23:4, 14, 22); both Jesus and Paul are adjudicated innocent by Rome and yet remain in Roman custody.",
    "19": "Paul appealed to Caesar not because he had charges against his own nation — Paul distances himself from political accusation, as Jesus refused the title of revolutionary king (John 18:36); both bear witness to a kingdom not of this world.",
    "20": "Paul is bound with this chain for the sake of the hope of Israel — the Messianic hope, the resurrection from the dead, the fulfillment of every promise God made to Israel through the prophets. Paul is in chains because he proclaims the risen Jesus as the fulfillment of Israel's hope.",
    "21": "The Jewish leaders say they have received no letters about Paul from Judea — the accusers have not followed through; as those who condemned Jesus could not prevent the resurrection, those who sought Paul's death cannot reach him in Rome.",
    "22": "The leaders want to hear Paul about the sect that is spoken against everywhere — Christianity divides opinion wherever it goes; the same was said of Jesus (Luke 2:34: destined for the falling and rising of many, a sign that will be spoken against).",
    "23": "From morning until evening Paul explains and testifies about the kingdom of God, persuading them about Jesus from both the Law of Moses and the Prophets — this is the hermeneutic of the risen Jesus himself (Luke 24:27, 44-45): all Scripture rightly read testifies to him. Paul does in Rome what Jesus did on the road to Emmaus.",
    "24": "Some are convinced by what Paul says, while others refuse to believe — the division of response mirrors every encounter with Jesus throughout Luke-Acts; the gospel is the stone over which some stumble and on which others are built (Luke 20:17-18; 1 Pet 2:7-8).",
    "25": "They disagree and leave after Paul makes one final statement — the final statement is the hinge of the entire Lukan narrative: Paul quotes Isaiah 6:9-10, the same oracle Jesus quoted when explaining why he spoke in parables (Matt 13:14-15; Mark 4:12; Luke 8:10). The frame opens and closes with the same scripture.",
    "26": "The Isaiah citation: go to this people and say, you will indeed hear but never understand, you will indeed see but never perceive — this oracle was fulfilled in Israel's response to Jesus's preaching; Paul now applies it to its second fulfillment in Rome. The pattern of Israel's rejection runs from Isaiah through Jesus to Paul.",
    "27": "The heart of this people has grown dull — John 12:40 cites this same Isaiah text to explain why Israel did not believe in Jesus despite his signs; Paul cites it to explain why the Roman Jewish community divides over the resurrection. The blindness is the same; the light being rejected is the same.",
    "28": "Paul declares that this salvation of God has been sent to the Gentiles and they will listen — the fulfillment of Isaiah 49:6, which the angel declared over the infant Jesus (Luke 2:32: a light for revelation to the Gentiles) and which Paul and Barnabas claimed as their commission (Acts 13:47). The Lukan arc closes: what was promised over the cradle is proclaimed in the capital of the Gentile world.",
    "29": "The Jews depart, arguing vigorously among themselves — the word of God continues to divide, as Jesus said he came not to bring peace but a sword (Matt 10:34) and as Simeon prophesied that the child would cause the rising and falling of many (Luke 2:34).",
    "30": "Paul lives two whole years in his own rented dwelling and welcomes all who come to him — the open house in the heart of Rome is the fulfillment of Acts 1:8: Jerusalem, Judea, Samaria, and now the uttermost part of the earth. The mission is established at the center of the world.",
  }
}

if __name__ == '__main__':
    existing = load_comm('mkt-christ', 'acts')
    merge_comm(existing, NEW)
    save_comm('mkt-christ', 'acts', existing)
    for ch in ['27', '28']:
        print(f'  ch {ch}: {len(existing.get(ch, {}))} verses')
