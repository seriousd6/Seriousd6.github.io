function rollDice(number) {
    result = (Math.floor(Math.random() * number))
    return result;
};

function searchArray(array) {
    return array[Math.floor(Math.random() * array.length)];
};

function toWords(s) {
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

function modify(number) {
    return Math.floor(number * (.85 + Math.random() * .4))
};

function partySize() {
    return 3 + rollDice(2)
}
rivalSize = partySize()
let standing = [
    "Friendly towards your party", "Hostile towards your party", "for past deeds", "Stand - offish and secretive", "Drunk", "Currently looking", "for someone", "Recovering / Wounded from a battle that went poorly",
]
let travelPlans = [
    "North", "North - East", "East", "South - East", "South", "South - West", "West", "North - West",
]

function partyLevel() {
    return 1 + rollDice(10)
}
console.log(`The party level is (${partyLevel()})`)

function partyPrint(Number) {
    function pBuilder(Number) {
        let party = []
        for (let i = 0; i < Number; i++) {
            party[i] = `${raceReturn()}, ${findClass()}, ${genderReturn()}`
        };

        function raceReturn() {
            var races = [
                [ //Common
                    'Human',
                ],
                [ //Uncommon
                    'Dwarf', 'Elf', 'Gnome', 'Half-Elf', 'Halfling',
                ],
                [ //Rare
                    'Dragonborn', 'Tiefling', 'Genasi', 'Aasimar', 'Half-Orc', 'Tabaxi',
                ],
                [ //Very Rare
                    'Kalashtar', 'Shifter', 'Warforged', 'Simic Hybrid', 'Changeling', 'Goliath', 'Gith', 'Yuan-Ti', 'Tortle', 'Aarakocra', 'Orc',
                ],
                [ //Ultimate Rare
                    'Bugbear', 'Firbolg', 'Goblin', 'Hobgoblin', 'Kenku', 'Kobold', 'Triton', 'Lizardfolk', 'Vedalken', 'Verdan', 'Locathah', 'Grung', 'Centaur', 'Loxodon', 'Minotaur',
                ],
            ]

            let chance = rollDice(100)
            if (chance > 98) {
                let raceArray = races[4]
                return searchArray(raceArray);
            } else if (chance > 95) {
                let raceArray = races[3]
                return searchArray(raceArray);
            } else if (chance > 80) {
                let raceArray = races[2]
                return searchArray(raceArray);
            } else if (chance > 50) {
                let raceArray = races[1]
                return searchArray(raceArray);
            } else {
                let raceArray = races[0]
                return searchArray(raceArray);
            }
        };

        function findClass() {
            //Class Array
            let classes = [
                [
                    'Bard', 'Cleric', 'Fighter', 'Ranger', 'Rogue',
                ],
                [
                    'Barbarian', 'Druid', 'Monk', 'Paladin',
                ],
                [
                    'Sorcerer', 'Warlock', 'Wizard', 'Artificer', 'Summoner',
                ],
                [
                    'Bounty Hunter', 'Blood Hunter', 'Mystic',
                ],
            ]

            function classReturn() {
                var chance = rollDice(100);
                if (chance > 98) {
                    return searchArray(classes[3]);
                } else if (chance > 75) {
                    return searchArray(classes[2]);
                } else if (chance > 45) {
                    return searchArray(classes[1]);
                } else {
                    return searchArray(classes[0]);
                };
            }
            return classReturn()
        };

        function genderReturn() {
            let chance = rollDice(100)
            if (chance < 50) {
                return "(F)"
            } else {
                return "(M)"
            }
        };
        return party
    }
    let rivalParty = pBuilder(Number)
    console.log(rivalParty)
    console.log(
        `The party level is (${1 + rollDice(10)})`)
}

/*"d12: Amount of Gold Pieces the party is currently carrying",
//=level
let wealth

"d20: The party is carrying a magic item either obscured or in plain view;",
//insert loot * levelgenerator'
*/