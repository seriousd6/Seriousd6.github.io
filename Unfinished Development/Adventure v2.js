//Chance and array manipulation methods
function shuffle(array) {
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
    }
    return array;
};

function rollDice(number) {
    result = (Math.floor(Math.random() * number))
    return result;
};

function searchArray(array) {
    let shuffled = shuffle(array)
    return shuffled[Math.floor(Math.random() * shuffled.length)];
};

function variableEvent(Arg) {
    let chance = rollDice(100)
    if (chance < 90) {
        return ""
    } else {
        return Arg
    }
};
// convert numbers to word form
function toWords(s) {
    var th = ['', 'thousand', 'million', 'billion', 'trillion'];
    var dg = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'];
    var tn = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen'];
    var tw = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety'];


    s = s.toString();
    s = s.replace(/[\, ]/g, '');
    if (s != parseFloat(s)) return 'not a number';
    var x = s.indexOf('.');
    if (x == -1)
        x = s.length;
    if (x > 15)
        return 'too big';
    var n = s.split('');
    var str = '';
    var sk = 0;
    for (var i = 0; i < x; i++) {
        if ((x - i) % 3 == 2) {
            if (n[i] == '1') {
                str += tn[Number(n[i + 1])] + ' ';
                i++;
                sk = 1;
            } else if (n[i] != 0) {
                str += tw[n[i] - 2] + ' ';
                sk = 1;
            }
        } else if (n[i] != 0) { // 0235
            str += dg[n[i]] + ' ';
            if ((x - i) % 3 == 0) str += 'hundred ';
            sk = 1;
        }
        if ((x - i) % 3 == 1) {
            if (sk)
                str += th[(x - i - 1) / 3] + ' ';
            sk = 0;
        }
    }

    if (x != s.length) {
        var y = s.length;
        str += 'point ';
        for (var i = x + 1; i < y; i++)
            str += dg[n[i]] + ' ';
    }
    return str.replace(/\s+/g, ' ');
};
//Reload Page
function reload() {
    location.reload()
};

function printArray(array) {
    for (i = 0; i < array.length; i++) {
        console.log(array[i])
    }
}




let coreAssumptions = {
    "Divinity": [
        ["Distant", "involved", "Present", ],
        ["Loose Pantheon", "Tight Pantheon", "Mystery", "Monotheism", "Dualism", "Animism", "Idealogical", ]
    ],
    "Civilization": [],
    "Age": [],
    "History": [],
    "Magic": [],
    "Races": [],
    "Planes": ["Typical (Elemental, Fey, Shadowfell)", "None - these divisions are mental only, everything exists on this world"]

}
let government = {
    "Autocracy": "",
    "Bureaucracy": "",
    "Confederacy": "",
    "Democracy": "",
    "Dictatorship": "",
    "Feudalism": "",
    "Gerontocracy": "",
    "Hierarchy": "",
    "Magocracy": "",
    "Matriarchy": "",
    "Militocracy": "",
    "Monarchy": "",
    "Oligarchy": "",
    "Patriarchy": "",
    "Meritocracy": "",
    "Plutocracy": "",
    "Republic": "",
    "Satrapy": "",
    "Kleptocracy": "",
    "Theocracy": "",
}
let commerce = {
    "Currency": []
}
let factions = {
    "Roles": [],
    "Goals": [],
    "Magic": [],
}
let laws = {
    "Magic": [],
    "Weapons": [],
}
let startingArea = {
    "Base": [],
    "Region": [],
    "Adventure": [],
}
let adventure = {
    "Tier": ["1 (lvl 1-5)", "2 (lvl 6-10)", "3 (lvl 11-16", "4 (17-20)", "Marathon (Tier 1-4)"],
    "Theme": [],
    "Flavor": ["Heroic", "Sword and Sorcery", "Epic", "Mythic", "Dark", "Intrigue", "Mystery", "Swashbuckling", "War", "Wuxia"],
    "World-Shaking": [27 - 32],
    "Threat": [],
    "Trope": [],
    "Twist": [],
    "Type": ["Location based", "Event Based", "Mystery", "Intrigue"],
    "Surprises": [],
    "Beginning": [],
    "Middle": [],
    "End": [],
}
let villain = {
    "Objective": {
        "Immorality": [],
        "Influence": [],
        "Magic": [],
        "Mayhem": [],
        "Passion": [],
        "Power": [],
        "Revenge": [],
        "Wealth": [],
    },
    "Methods": {
        "Agricultural Devastation": [],
        "Assault or Beatings": [],
        "Bounty Hunting or Assasination": [],
        "Captivity or Coercion": [],
        "Confidence Scams": [],
        "Defamation": [],
        "Dueling": [],
        "Execution": [],
        "Impersination or disguise": [],
        "Lying or perjury": [],
        "Magical Mayhem": [],
        "Murder": [],
        "Neglect": [],
        "Politics": [],
        "Religion": [],
        "Stalking": [],
        "Theft or Property Crime": [],
        "Torture": [],
        "Vice": [],
        "Warfare": [],
    },
    "Weakness": []
}

let wilderness = {
    "Monuments": [],
    "Ruins": [],
    "Settlements": [],
    "Strongholds": [],
    "Oddities": [],
}
let settlements = {
    "Race Relations": [],
    "Ruler Status": [],
    "Notable Traits": [],
    "Renown": [],
    "Calamity": [],
    "Buildings": {
        "Residence": [],
        "Tavern": [],
        "Religious": [],
        "Warehouse": [],
        "Shop": [],
        "Urban Encounter": [],
    }
}
let dungeon = {
    "Location": ["beneath a building in a city", "built into the catacombs or sewers beneath a city", "beneath a farmhouse", "beneath a graveyard", "beneath a ruined castle", "beneath a ruined city", "beneath a temple", "in a chasm", "in a cliff face", "in a desert", "in a forest", "in a glacier", "in a gorge", "in a jungle", "in a mountain pass", "in a swamp", "beneath or on top of a mesa", "in sea caves", "in several connected mesas", "on a mountain peak", " on a promontory", "on an island", "underwater", `${searchArray(["in the branches of a tree","around a geyser", "behind a waterfall","buried in an avalanche","buried in a sandstorm", "buried in volcanic ash","Sunk in a swamp", "floating on the sea", "in a meteorite","on a demiplane or pocket dimension", "in an area devastated by a magical catastrophe", "on a cloud", "in the Feywild", "in the Shadowfell", "on an island in an underground sea","In a volcano","on the back of a gargantuan living creature","sealed in a magical dome of force","inside a mordenkainen's magnificent mansion"])}`],
    "Creator": {
        "Basic": ["beholder", "dwarves", "elves (including drow)", "giants", "hobgoblins", "kuo-toa", "lich", "mind flayers", "yuan-ti", "devil or demons", "natural or magical phenomena"],
        "Human": {
            "Alignment": ["lawful good", "neutral good", "chaotic good", "lawful neutral", "neutral", "chaotic neutral", "lawful evil", "neutral evil", "chaotic evil"],
            "Class": ["barbarian", "bard", "cleric", "druid", "fighter", "monk", "paladin", "ranger", "rogue", "sorcerer", "warlock", "wizard"]
        }
    },
    "Purpose": {
        "death trap": ["antechamber or waiting room for spectators", "guardroom fortified against intruders", `vault for holding important treasures, accessible only by locked or secret door (${searchArray(["trapped","trapped","trapped","not trapped"])})`, "room containing a puzzle that must be solved to bypass a trap or monster", "trap designed to kill or capture creatures", "observation room, allowing guards or spectators to observe creatures moving through the dungeon"],
        "lair": ["armory stocked with weapons and armor", "audience chamber used to recieve guests", "banquet room used for important celebrations", "barracks where the lairs defenders are quartered", "bedroom for use by leaders", "chapel where the lair's inhabitants worship", "cistern or well for drinking water", "guardroom for defense of the lair", "kennel for pets and guard beasts", "kitchen for food storage and preparation", "pen or prison where captives are held", "storage, mostly nonperishable goods", "throne room where the lairs leaders hold court", "torture chamber", "training and exercise room", "trophy room or museum", "latrine or bath", "workshop for the contruction of weapons, armor, tools, and other goods"],
        "maze": ["conjuring room, used to summon creatures that guard the maze", "guardroom for sentinel that patrol the maze", "lair for guard beasts that partol the maze", "pen or prison accessible only by secret door, used to hold captives condemned to the maze", "shrine dedicated to a god or other entity", "storage for food, as well as tools used by the maze's guardians to keep the complex in working order", "trap to confound or kill those sent into the maze", "well that provides drinking water", "workshop where doors, torch sconces, and other furnishings are repaired and maintained"],
        "mine": ["barracks for miners", "bedroom for a supervisor or manager", "chapel dedicated to a patron diety of miners, earth, or protection", "cistern providing drinking water for miners", "guardroom", "kitchen used to feed workers", "laboratory used to conduct test on strange minerals extracted from the mine", `lode where metal ore is mined (${searchArray(["depleted","depleted","depleted","some ore left"])})`, "office used by the mine supervisor", "smithy for repairing damaged tools", "storage for tools and other equipment", "storage room or vault used to store ore for transport to the surface"],
        "planar gate": ["decorated foyer antechamber", "armory used by the portal's guardians", "audience chamber for recieving visitors", "barracks used by the portal's guards", "bedroom for use by the high tanking members of the order that guards the portal", "chapel dedicated to a diety or dieties related to the protal and its defender", "cistern providing fresh water", "classroom for use of initiates learning about the portal's secrets", "conjuring room for summoning creatures used to investigate or defend the portal", "crypt where the remains of those that died guarding the portal are kept", "dining room", "divination room used to investigate the portal and events tied to it", "dormitory for visitors and guards", "entry room or vestibule", "gallery used for displaying trophies and objects related to the portal and those that guard it", "guardroom to protect or watch over the portal", "kitchen", "laboratory for conducting experiments related to the portal and the creatures that emerge form it", "library holding books abour the protal's history", "pen or prison for holding captives or creatures that emerge form the portal", `planar junction, where the gate to another plane ${searchArray(["once stood", "once stood","once stood", "is currently active"])}`, "storage", "strong room or vault, for guarding valuable treasures connected to the portal or funds used to pay the planar gate's guardians", "study", "torture chamber, for questioning creatures that pass through the portal or to clandestinely use it", "latrine or bath", "workshop for constructing the tools and gear needed to study the portal"],
        "strongold": ["antechamber where visitors seeking access to the stronghold wait", "armory holding high-quality gear, including light siege weapons such as ballistas", "audience chamber used by the master of the stronghold to recieve visitors", "aviary or zoo for keeping exotic creatures", "banquet room for hosting celebrations and guests", "barracks used by elite guards", "bath outfitted with a marble floor and other luxurious accroutrements", "bedroom for use by the stronghold's master and other important guests", "chapel dedicated to a diety associated with the stronghold's master", "cistern providing drinking water", "dining room for intimate gatherings or informal meals", "dressing room featuring a number of wardrobes", "gallery for the display of expensive works of art and trophies", "game room used to entertain visitors", "guardroom", "kennel where monsters or trained animals that protect the stronghold are kept", "kitchen designed to prepare exotic foods for large numbers of guests", "library with an extensive collection of rare books", "lounge used to entertain guests", "pantry, including cellar for wine or spirits", "sitting room for family and intimate guests", "stable", "storage for mundane goods and supplies", `strong room or vault for protecting important treasures ${searchArray(["hidden behind a secret door","hidden behind a secret door","hidden behind a secret door","and the door is not hidden"])}`, "study, including a writing desk", "throneroom elaborately decorated", "waiting room where lesser guests are held before recieving an audience", "latrine or bath", "crypt blonging to the stronghold's master or someone else of importance"],
        "temple/shrine": ["armory filled with weapons and armor, battle banners, and pennants", "audience chamber where priests of the temple recieve commoners and low-ranking visitors", "banquet room used for celebrations and holy days", "barracks for the temple's military arm or its hired guards", "cells where the faithful can sit in quiet contemplation", "central temple built to accomodate rituas", "chapel dedicated to a lesser diety associated with the temple's major diety", "classroom used to train initiates and priests", "conjuring room, specially sanctified and used to summon extraplanar creatures", "crypt for a high priest or similar figure, hidden and heavily guarded by creatures and traps", "divination room, inscribed with runes and stocked with soothsaying elements", "dining room (small), for the temple's high priests", "dining room (large) for the temple's servants and lesser priests", "dormitory for lesser priests or students", "guardroom", "kennel for animals or monsters associated with the temple's diety", "kitchen (might bear a disturbing resemblance to a torture chamber in an evil temple", "library, well stocked with religious treatises", "prison for captured enemies (in good or neutral temples) or those designated for sacrifices (in evil temples)", "robing room containing ceremonial outfits and items", "stable for riding horses and mounts belonging to the temple, or for visiting messengers and caravans", "storage holding mundane supplies", "strong room or vault holding important relics and ceremonial items, heavily trapped", "torture chamber, used in inquisitions (in lawful good and neutral temples) or for the sheer joy of causing pain (evil temples)", "latrine or bath", "well for drinking water, defendable in the case of attack or siege", "workshop for repairing or creating weapons, religious item, and tools"],
        "tomb": ["antechamber for those that have come to pay respect to the dead or prepare themselves for burial rituals", "chapel dedicated to dieties that watch over the dead and protect their restng places", "a crypt for less important burials", "divination room, used in rituals to contact the dead for guidance", "false crypt(trapped) used to kill or capture thieves", "gallery to display the deeds of the deceased through trophies, statues, paintings, and so forth", "grand crypt for a noble, high priest, or other important indivudal", "guardroom, usually guarded by undead, constructs, or other creatures that do not need to eat or sleep", "robing room for preists to prepare for burial rituals", "storage, stocked with tools for maintaining the tomb and preparing the dead for burial", "tomb where the wealthiest and more important folk are interred, protected by secret doors and traps", "workshop for embalming the dead"],
        "treasure vault": ["antechamber for visiting dignitaries", "armory containign mundane and magic gear used by the treasure vault's guards", "barracks for the guards", "cistern providing fresh water", "guardroom for defending against intruders", "kennel for trained beasts used to guard the treasure vault", "kitchen for feeding gaurds", "watch room that allows guards to observe those who approach the dungeon", "prison for holding captured intruders", "strong room or vault, for guarding the treasure hidden in the dungeon, accessible only by a locked secret door", "torture chamber for extracting information from captured intruders", "trap or other trick designed to kill or capture creatures that enter the dungeon", ],
    },
    "History": ["it has been long since abandoned", "it has been abandoned due to a plague", "it has been conquered by invaders", "it is avoided due to attacking raiders", "the pioneers of the area were destroyed by a discovery made within", "infighting destroyed the first residents", "it is the site of a magical catastrophe, killing the first ones here", "it has been battered and deemed unusable due to natural disasters", "this location has been cursed by the gods and shunned", `it is currently under intelligent control`, "it is overrun by planar creatures", "it is the site of a great miracle", ],
    "Layout": {
        "Starting area": [
            [
                "square, 20x20 ft.; passage on each wall",
                "square, 20x20 ft.; doors on two walls, passage in third wall",
                "square, 40x40 ft.; doors on three walls",
                "Rectangle, 80x20 ft.; with a row of pillars down the middle; two passages leading from each long wall, doors on each short wall",
                "rectangle 20x40 ft.; passage on each wall",
                "circle, 40 ft. diameter; one passage at each cardinal direction",
                "circle, 40 ft. diameter; one passage in each cardinal direction; well in middle of room (might lead to a lower level)",
                "square, 20x20 ft.; door on two walls, passage on third wall, secret door on fourth wall",
                "passage, 10 ft. wide; T intersection",
                "passage, 10 ft. wide; four way intersection"
            ],
            [
                4,
                3,
                3,
                6,
                4,
                4,
                5,
                4,
                2,
                4,
            ]

        ],
        "Passage width": ["5 ft.", "10 ft.", "20 ft.", "30 ft.", "40 ft., with a row of pillars down the middle", "40 ft., with a double row of pillars", "40 ft. wide, 20 ft high", "40 ft. wide, 20 ft. high, (with a second floor balcony/gallery 10 ft. above)"],
        "Stairs": ["down one level to a chamber", "down one level to a passage 20 ft. long", "down two levels to a chamber", "down two levels to a passage 20 ft. long", "down three levels to a chamber", "down three levels to a passage 20 ft. long", "up one level to a chamber", "up one level to a passage 20 ft. long", "up to a dead end", "down to a dead end", "chimney up one level to a passage 20 ft. long", "chimney up two levels to a passage 20 ft. long", "shaft (with or without elevator) down one level to a chamber", "shaft (with or without elevator) down two levels to a chamber"],
        "Passage": ["30 ft. long with no side passages", "20 ft. long, door to the right, then and additional 10 ft. ahead", "20 ft. long, door to the left, then and additional 10 ft. ahead", "20 ft. long, passage ends in a door", "20 ft. long, side passage to the right, then an additional 10 ft. ahead", "20 ft. long, side passage to the left, then an additional 10 ft. ahead", `20 ft. long, comes to a dead end; (there is a secret door)`, "20 ft. long, then the passage turns left and continues 10 ft.", "20 ft. long, then the passage turns right and continues 10 ft."],
        "PassageCount": [1, 2, 2, 1, 2, 2, 1, 1, 1],
        "Door": {
            "Type": ["wooden", "wooden, barred or locked", "stone", "stone, barred or locked", "iron", "iron, barred or locked", "portcullis", "portcullis, locked in place", "secret door", "secred door, barred or locked", ],
            "Beyond": ["a passage extending 10 ft., then T intersection extending 10ft. to the right and left", "passage 20 ft. straight ahead", "false door with trap", ],
        },
        "Chambers": {
            "Chamber Types": ["antechamber", "armory", "audience chamber", "Aviary", "Banquet room", "barracks", "bath or latrine", "bedrooms", "bestiary", "cell", "chantry", "chapel", "cistern", "classroom", "closet", "conjuring room", "court", "crypt", "dining room", "divination room", "dormitory", "Dressing room", " entry room or vestibule", "Gallery", "Game room", "guardroom", "Hall", "great hall", "Hallway", "Kennel", "Kitchen", "laboratory", "Library", "Lounge", "meditation chamber", "Observatory", "office", "Pantry", "pen or prison", "reception room", "refectory", "robing room", "salon", "shrine", "sitting room", "smithy", "stable", "storage room", "strong room or vault", "study", "temple", "throne room", "torture chamber", "training or exercise room", "trophy room or museum", "waiting room", "nursery or schoolroom", "well", "workshop"],
            "Shape": [
                /*Small*/
                [`Square, 20x20 ft.`, `Square, 30x30 ft.`, `Square, 40x40 ft.`, `Rectangle, 20x30 ft.`, `Rectangle, 30x40 ft.`, `Circle, 30 ft. diameter`, ],
                /*Large*/
                [`Rectangle, 40x50 ft.`, `Rectangle, 50x80 ft.`, `Circle, 50 ft. diameter`, `Octagon, 40x40 ft.`, `Octagon, 60x60 ft.`, `Trapeziod, roughly 40x60 ft.`, ]
            ],
            "Chamber Exits": [
                /*Small*/
                [0, 0, 1, 1, 2, 2, 3, 3, 4, 4],
                /*Large*/
                [0, 1, 1, 2, 2, 3, 3, 4, 5, 6]
            ],
            "Exit locations": [
                "wall opposite entrance", "wall left of entrance", "wall right of entrance", "same wall as entrance",
            ],
            "Exit type": [
                "corridor, 10 ft. long"
            ]
        },

        "State": ["rubble, ceiling partially collapsed", "holes, floor partially collapsed", "Ashes, contents mostly burned", "used as a campsite", "pool of water, chambers original contents are water damaged", "furniture wrecked but still present", `Converted to a(n) ${"chamber"}`, "Stripped bare", "Pristine and in original state"]
    },
    "Contents": {}

}

function printDungeon() {
    let creator = "";
    let purpose = searchArray(Object.keys(dungeon.Purpose));
    if (rollDice(100) < 50) {
        creator = searchArray(dungeon.Creator.Basic);
    } else {
        let creatorAlig = searchArray(dungeon.Creator.Human.Alignment);
        let creatorClass = searchArray(dungeon.Creator.Human.Class);
        creator = `a humaniod, specifically a ${creatorAlig} aligned ${creatorClass},`;
    }


    function dungeonBuilder(purpose) {
        let roomCount = 0;
        let limiter = 50
        function start() {
            let inde = Math.floor(Math.random(1) * dungeon.Layout["Starting area"][0].length);
            let start = dungeon.Layout["Starting area"][0][inde];
            roomCount += dungeon.Layout["Starting area"][1][inde];
            return `The entrance of this dungeon lets into a ${start}, likely this area was a(n) ${searchArray(dungeon.Purpose[purpose])}.`
        };
        let output = `There is an area of interest ${searchArray(dungeon.Location)}, it was created by ${creator} and historically it has been used as a ${purpose}. Also, ${searchArray(dungeon.History)}.`
        console.log(output + "\n\n" + start())
        
        let newRooms = [roomCount]
        let outputArray = []
        let counter = 1
        for (t = 1; roomCount < limiter; t++) {

            function determineType(num, x) {
                let Arrg = []
                for (i = x; i < num; i++) {

                    let chance = rollDice(100)
                    if (chance < 25) {
                        Arrg.push(`Path ${toWords(counter)}is ${searchArray(["sealed", "blocked by rubble", "caved in", "too small to enter"])}`)
                        counter++
                    } else if (chance < 75) {
                        if (roomCount > limiter) {
                            let size = rollDice(1)
                            let chamber = dungeon.Layout.Chambers.Shape[size][Math.floor(Math.random(1 * dungeon.Layout.Chambers.Shape[size].length))]
                            let exits = 0
                            roomCount += exits
                            Arrg.push(`Path ${toWords(counter)}leads to a chamber that is ${chamber}, seeming to be used as a ${searchArray(dungeon.Purpose[purpose])} with ${exits} exits.`)
                            counter++
                        } else {
                            let size = rollDice(1)
                            let chamber = dungeon.Layout.Chambers.Shape[size][Math.floor(Math.random(1 * dungeon.Layout.Chambers.Shape[size].length))]
                            let exits = searchArray(dungeon.Layout.Chambers["Chamber Exits"][size])
                            roomCount += exits
                            Arrg.push(`Path ${toWords(counter)}leads to a chamber that is ${chamber}, seeming to be used as a ${searchArray(dungeon.Purpose[purpose])} with ${exits} exits.`)
                            counter++
                        }
                    } else {
                        let inde = Math.floor(Math.random(1 * dungeon.Layout.Passage.length));
                        let passage = "";
                        let exits = "";
                        let size = searchArray(dungeon.Layout["Passage width"]);

                        function passType() {
                            let chance = rollDice(100)
                            if (chance < 75) {
                                passage = 'passage that is ' + dungeon.Layout.Passage[inde];
                                exits = dungeon.Layout.PassageCount[inde]
                            } else {
                                passage = 'staircase that is ' + searchArray(dungeon.Layout.Stairs)
                                exits = 1
                            }
                        }
                        passType()
                        roomCount += exits
                        Arrg.push(`Path ${toWords(counter)}leads to a ${size +" "+ passage} with ${exits} connection(s)`)
                        counter++
                    }
                }
                return Arrg
            }
            let build = determineType(roomCount, counter);
            let bog = [].concat(outputArray, build)
            outputArray = bog

            newRooms.push(roomCount)
        }
        printArray(outputArray)
    };
    dungeonBuilder(purpose)

}
printDungeon();