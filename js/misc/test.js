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

function variableEvent(array, number) {
    let chance = rollDice(100)
    if (chance < 75) {
        return ""
    } else if (number === undefined) {
        return searchArray(array) + " "
    } else {
        return searchArray(array[number]) + ' '
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
    location.reload();
};

function printArray(array) {
    for (i = 0; i < array.length; i++) {
        console.log(array[i])
    }
}
/*-----------------------------DELETE BELOW ONLY------------------------------------*/

function artGenerator(number) {
    document.getElementById("Art").innerHTML = ""
    let status = [
        [ /*Stained Glass*/ "dusty", "dirty", "vandalized", "scratched", "broken", "faded", "discolored", "unfinished", "incomplete", "cracked", "pristine", "vibrant", "well-repaired", "poorly-repaired"],
        [ /*Mural*/ "dusty", "dirty", "vandalized", "scratched", "broken", "cracked", "stained", "faded", "eroded", "unfinished", "incomplete", "pristine", "moss/ivy-covered", "well-repaired", "poorly-repaired"],
        [ /*Pottery*/ "dusty", "dirty", "vandalized", "scratched", "broken", "cracked", "stained", "faded", "shattered", "unfinished", "pristine", "well-repaired", "poorly-repaired"],
        [ /*Figurine/ stauette/ carving*/ "dusty", "dirty", "vandalized", "scratched", "broken", "cracked", "stained", "broken (and missing some pieces)", "eroded", "shattered", "unfinished", "pristine", "moss/ivy-covered", "well-repaired", "poorly-repaired", "sliced in half"],
        [ /*Painting*/ "dusty", "dirty", "torn", "stained", "cut", "water-stained", "vandalised", "faded", "unfinished", "vibrant", "pristine", ],
        [ /*Relief*/ "dusty", "dirty", "vandalized", "scratched", "cracked", "unfinished", "incomplete", "pristine", "moss/ivy-covered", "well-repaired", "poorly-repaired"],
        [ /*Tapestry*/ "dusty", "dirty", "torn", "thread-bare", "worn", "water-stained", "shredded", "stained", "cut", "vandalised", "faded", "unfinished", "vibrant", "pristine", ],
        [ /*Fine Jewelry*/ "fine", "dusty", "dirty", "broken", "bent", "unfinished", "incomplete", "pristine", "vibrant", "well-repaired", "poorly-repaired"],
        [ /*Fine clothes*/ ]
    ]
    let pottery = ["vase", "jug", "pot", "jar", "jug", "plate", "tray", "cup", "bowl", "oil-lamp", "teapot", "ewer"]
    let jewelry = ["arm-band", "ring", "necklace", "choker", "crown", "scepter", "bracelet", "earrings", "anklet", "chalice", "bowl", "locket", "comb", "brooch", "music box", "jewelry box"]
    let material = [
        [ /*pottery*/ "pewter", "lead", "bronze", "gold", "iron", "silver", "platinum", "electrum", "copper", "nickel", "ruby", "sapphire", "jade", "amethyst", "bone", "teeth-bone", "hide", "emerald", "topaz", "opal", "diamond", "moonstone", "clay", "granite", "marble", "obsidian", "porcelain", "sandstone", "quartz", "amber", "cork", "petrified wood", "unidentifiable substance", "mohogany", "cherry wood", "oak wood", "apple wood", "teak wood", "pine wood", "birch wood", "shell", "sea glass", "glass", ],
        [ /*statues*/ "marble", "golden", "granite", "silver", "platinum", "copper", "bronze", "electrum", "obsidian", "clay", "bone"],
        [ /*Carvings*/ "bone", "mohogany", "cherry wood", "oak wood", "apple wood", "teak wood", "pine wood", "birch wood", ],
        [ /*Fine jewelry*/ "gold", "platinum", "electrum", "silver", "copper", "gold with platinum inlay", "gold and copper alloy", "gold and silver alloy", "jewelled gold", "jewelled platinum", "jewelled electrum", "jewelled silver", "jewelled copper", "jewelled gold with platinum inlay", "jewelled gold and copper alloy", "jewelled gold and silver alloy"],
        [ /*Fine Clothes*/ "silk", "purple velvet", "spider-silk"],
    ]

    let artA = ["Silver ewer(25gp)", "Carved bone statuette(25gp)", "Small gold bracelet(25gp)", "Cloth-of-gold vestments(25gp)", "Black velvet mask stitched with silver thread(25gp)", "Copper chalice with silver filigree(25gp)", "Pair of engraved bone dice(25gp)", "Small mirror set in a painted wooden frame(25gp)", "Embroidered silk handkerchief(25gp)", "Gold locket with a painted portrait inside(25gp)"]
    let artB = ["Gold ring set with bloodstones(250gp)", "Carved ivory statuette(250gp)", "Large gold bracelet(250gp)", "Silver necklace with a gemstone pendant(250gp)", "Bronze crown(250gp)", "Silk robe with gold embroidery(250gp)", "Large well-made tapestry(250gp)", "Brass mug with jade inlay(250gp)", "Box of turquoise animal figurines(250gp)", "Gold bird cage with electrum filigree(250gp)"]
    let artC = ["Silver chalice set with moonstones(750gp)", "Silver-plated steel longsword with jet set in hilt(750gp)", "Carved harp of exotic wood with ivory inlay and zircon gems(750gp)", "Small gold idol(750gp)", "Gold dragon comb set with red garnets as eyes(750gp)", "Bottle stopper cork embossed with gold leaf and set with amethysts(750gp)", "Ceremonial electrum dagger with a black pearl in the pommel(750gp)", "Silver and gold brooch(750gp)", "Obsidian statuette with gold fittings and inlay(750gp)", "Painted gold war mask(750gp)"]
    let artD = ["Fine gold chain set with a fire opal(2500gp)", "Old masterpiece painting(2500gp)", "Embroidered silk and velvet mantle set with numerous moonstones(2500gp)", "Platinum bracelet set with a sapphire(2500gp)", "Embroidered glove set with jewel chips(2500gp)", "Jeweled anklet(2500gp)", "Gold music box(2500gp)", "Gold circlet set with four aquamarines(2500gp)", "Eye patch with a mock eye set in blue sapphire and moonstone(2500gp)", "A necklace string of small pink pearls(2500gp)"]
    let artE = ["Jeweled gold crown(7500gp)", "Jeweled platinum ring(7500gp)", "Small gold statuette set with rubies(7500gp)", "Gold cup set with emeralds(7500gp)", "Gold jewelry box with platinum filigree(7500gp)", "Painted gold child's sarcophagus(7500gp)", "Jade game board with solid gold playing pieces(7500gp)", "Bejeweled ivory drinking horn with gold filigree(7500gp)"]

    let artForm = [
        [
            `${variableEvent(status,0)}stained glass window`,
            `${variableEvent(status,1)}mural`,
            `${variableEvent(status,2)}${searchArray(material[0])} ${searchArray(pottery)}`,
            `${variableEvent(status,3)}${searchArray(material[1])} ${searchArray(["statuette","figurine",])}`,
            `${variableEvent(status,3)}${searchArray(material[2])} carving`,
            `${variableEvent(status,4)}painting`,
            `${variableEvent(status,5)}relief`,
            `${variableEvent(status,6)}tapestry`,
        ],
        [
            `${variableEvent(status,7)}${searchArray(material[3])} ${searchArray(jewelry)}`,
        ]
    ]

    let size = ["large", "small", "tiny", "life-size", "huge", "gargantuan"]
    let many = ["a small group of", "a large group of", "a small army of", "a few", "a large force composed of"]
    let adjective = [
        ['airborne', 'slouching', 'giddy', 'brazen', 'hobbled', 'wrinkled', 'broken', 'happy', 'sunken', 'headless', 'burning', 'toothy', 'mighty', 'frisky', 'staggering', 'gutted', 'glorious', 'crooked', 'joyful', 'wise', 'sweet', 'surly', 'reverent', 'clumsy', 'clever', 'prone', 'restrained', 'unconscious', 'invisible', 'petrified', 'poisoned', 'charmed', 'frightened', 'grappled', 'acrobatic', 'dextrous', 'intelligent', 'strong', 'athletic', 'deceitful', 'charismatic', 'insightful', 'intimidating', 'observant', 'perceptive', 'persuasive', 'stealthy', 'dirty', 'dangerous', 'deadly', 'hidden', 'alert', 'brave', 'wicked', 'tricky', 'mysterious', 'kind', 'handsome', 'frantic', 'foolish', 'adorable', 'cruel', 'elegant', 'friendly', 'gnashing', 'winking', 'smiling', 'waving', 'ugly', 'busy', 'creepy', 'grotesque', 'poor', 'puzzled', 'obnoxious', 'fierce', 'fancy', 'magnificent', 'enchanting', 'eager', 'determined', 'horrible', 'wide-eyed', 'victorious', 'uptight', 'unusual', 'troubled', 'thankful', 'terrible', 'tame', 'repulsive', ],
        []
    ]
    let monster = ['aarakocra', 'aboleth', 'angel', 'animated object', 'animated weapon', 'ankheg', 'azer', 'banshee', 'basilisk', 'behir', 'beholder', 'blight', 'bugbear', 'bulette', 'bullywug', 'cambion', 'carrion crawler', 'centaur', 'chimera', 'chuul', 'cloaker', 'cockatrice', 'couatl', 'crawling claw', 'cyclops', 'darkmantle', 'death knight', 'demilich', 'demon', 'devil', 'dinosaur', 'displacer beast', 'doppleganger', 'dracolich', 'shadow dragon', 'dragon', 'dragon turtle', 'drider', 'dryad', 'duergar', 'elemental', 'empyrean', 'ettercap', 'ettin', 'faerie dragon', 'flameskull', 'flumph', 'fomorian', 'fungi', 'galeb duhr', 'gargoyle', 'genie', 'ghost', 'giant', 'gibbering mouther', 'gith', 'gnoll', 'goblin', 'golem', 'gorgon', 'grell', 'grick', 'griffon', 'grimlock', 'hag', 'half dragon', 'harpy', 'hell hound', 'helmed horror', 'hippogriph', 'hobgoblin', 'homunculus', 'hook horror', 'hydra', 'intellect devourer', 'invisible stalker', 'jakalwere', 'kenku', 'kobold', 'kraken', 'kuo-toa', 'lamia', 'lich', 'lizardfolk', 'lycanthrope', 'magmin', 'manticore', 'medusa', 'mephits', 'merfolk', 'merrow', 'mimic', 'mind flayer', 'minotaur', 'modron', 'mummie', 'myconid', 'naga', 'nightmare', 'nothic', 'ogre', 'oni', 'ooze', 'orc', 'otyugh', 'owlbear', 'pegasus', 'peryton', 'piercer', 'pixie', 'psuedodragon', 'purple worm', 'quaggoth', 'rakshasa', 'remorhazes', 'revenant', 'roc', 'roper', 'rust monster', 'sahuagin', 'salamander', 'satyr', 'scarecrow', 'shadow', 'shambling mound', 'shield guardian', 'skeleton', 'slaadi', 'specter', 'sphinx', 'sprite', 'stirge', 'succubus', 'incubus', 'terrasque', 'thri-kreen', 'treant', 'troglodyte', 'troll', 'umber hulk', 'unicorn', 'vampire', 'water weird', 'wight', `will-o'-wisp`, 'wraith', 'wyvern', 'xorn', 'yeti', 'yuan-ti', 'yugoloth', 'zombie', 'ape', 'awakened tree', 'awakened shrub', 'axe beak', 'baboon', 'badger', 'bat', 'black bear', 'blink dog', 'blood hawk', 'boar', 'brown bear', 'camel', 'cat', 'constrictor snake', 'crab', 'crocodile', 'death dog', 'deer', 'dire wolf', 'draft horse', 'eagle', 'elephant', 'elk', 'flying snake', 'frog', 'giant ape', 'giant badger', 'giant bat', 'giant boar', 'giant centipede', 'giant constrictor snake', 'giant crab', 'giant crocodile', 'giant eagle', 'giant elk', 'giant fire beetle', 'giant frog', 'giant goat', 'giant hyena', 'giant lizard', 'giant octopus', 'giant owl', 'giant poisonous snake', 'giant rat', 'giant scorpion', 'giant sea horse', 'giant shark', 'giant spider', 'giant toad', 'giant vulture', 'giant wasp', 'giant weasel', 'giant wolf spider', 'goat', 'hawk', 'hunter shark', 'hyena', 'jackal', 'killer whale', 'lion', 'lizard', 'mammoth', 'mastiff', 'mule', 'octopus', 'owl', 'panther', 'phase spider', 'poisonous snake', 'polar bear', 'pony', 'quipper', 'rat', 'raven', 'reef shark', 'rhinoceros', 'riding horse', 'saber-toothed tiger', 'scorpion', 'sea horse', 'spider', 'bat swarm', 'insect swarm', 'poisonous snake swarm', 'quipper swarm', 'rat swarm', 'raven swarm', 'tiger', 'vulture', 'warhorse', 'weasel', 'winter wolf', 'wolf', 'worg', ]
    let person = ['refugee', 'acolyte', 'archmage', 'assassin', 'bandit', 'berserker', 'commoner', 'cultist', 'fanatic', 'gladiator', 'mage', 'preist', 'scout', 'spy', 'thug', 'veteran', 'dutchess', 'paladin', 'farmer', 'knight', 'scholar', 'seadog', 'jester', 'noble', 'king', 'thief', 'sailor', 'farmer', 'soldier', 'mercenary', 'mage', 'scholar', 'beggar', 'bard', 'guard', 'knight', 'merchant', 'smuggler', 'fool', 'druid', 'witch', 'traveler', 'fisherman', 'lady', 'harlot', 'bounty hunter', 'gardener', 'gambler', 'prince', 'princess', 'pirate', 'journeyman', 'chieftain', 'lord', 'archer', 'lumberjack', 'miner', 'hunter', 'villager', 'settler', 'butcher', 'oracle', 'pilgrim', 'courier', 'hero', 'necromancer', 'sorcerer', 'wizard', 'barbarian', 'ranger', 'fighter', 'monk', 'warlock', 'summoner', 'arcanist', 'blood hunter', 'cleric', 'rogue', 'artificer', 'outlander', 'exile', ]

    function findRace() {
        var races = {
            "Common": { 'Human': undefined, },
            'Uncommon': { 'Dwarf': undefined, 'High-Elf': undefined, 'Wood-Elf': undefined, 'Gnome': undefined, 'Half-Elf': undefined, 'Halfling': undefined, },
            'Rare': { 'Dragonborn': undefined, 'Tiefling': undefined, 'Genasi': undefined, 'Aasimar': undefined, 'Half-Orc': undefined, 'Tabaxi': undefined, 'Drow': undefined, },
            "Very Rare": { 'Kalashtar': undefined, 'Shifter': undefined, 'Warforged': undefined, 'Simic Hybrid': undefined, 'Changeling': undefined, 'Goliath': undefined, 'Gith': undefined, 'Yuan-Ti': undefined, 'Tortle': undefined, 'Aarakocra': undefined, 'Orc': undefined, },
            'Ultimate Rare': { 'Bugbear': undefined, 'Firbolg': undefined, 'Goblin': undefined, 'Hobgoblin': undefined, 'Kenku': undefined, 'Kobold': undefined, 'Triton': undefined, 'Lizardfolk': undefined, 'Vedalken': undefined, 'Verdan': undefined, 'Locathah': undefined, 'Grung': undefined, 'Centaur': undefined, 'Loxodon': undefined, 'Minotaur': undefined, },
        };
        let chance = rollDice(100)
        if (chance > 98) {
            return searchArray(Object.keys(races["Ultimate Rare"]));
        } else if (chance > 95) {
            return searchArray(Object.keys(races["Very Rare"]));
        } else if (chance > 80) {
            return searchArray(Object.keys(races["Rare"]));
        } else if (chance > 50) {
            return searchArray(Object.keys(races["Uncommon"]));
        } else {
            return searchArray(Object.keys(races["Common"]));
        }
        //document.getElementById("Race").innerHTML = characterRace
    };
    let historicalEvent = ["a creation myth", "a constellation", "an ascension story", "a historical battle", "a coronation", "an ancient disaster", "an ancient prophecy", "the aligment of the stars", `the rise of a great ${findRace()} hero`, `the fall of a great ${findRace()} hero`, "the defeat of a powerful nation", "the creation of a powerful artifact", "the destruction of a powerful artifact", "the fall of an angel", "the rise of a demon", "the affair of a god", "entrance to another plane", "a mortal besting a God", "a hero's quest", `a historical battle between ${findRace()}s and ${searchArray(monster)}s`, `a historical battle between ${findRace()}s and ${findRace()}s`, `a historical battle between ${searchArray(monster)}s and ${searchArray(monster)}s`, ]
    let tool = ['weapon', 'tool', 'treasure chest', 'sword', 'shovel']
    let item = ['whistle', 'anchor', 'nail', 'scale', 'open book', 'bugle', 'keystone', 'hook', 'tree', 'flower', 'drum', 'buckle', 'chair', 'spoon', 'fork', 'axe', 'sword', 'shield', 'armor', 'bedroll', 'barrel', 'keg', 'crate', 'box', 'pot', 'vial', 'arrow', 'broom', 'shovel', 'pillow', 'candle', 'lantern', 'mug', 'cup', 'tankard', 'bottle', 'plate', 'plow', 'pot', 'pan', 'lamp', 'rug', 'hammer', 'anvil', 'goblet', 'chest', 'tankard of alcohol', 'feather', 'oar', 'cask', 'harp', 'lute', 'necklace', 'bracelet', 'comb', 'crown', 'ring', 'oil-lamp', 'potion', 'gem', 'scroll', 'wand', 'horseshoe', 'pike', 'bow', 'slippers', 'trident', 'brooch', 'amulet', 'pipe', 'figurine', 'deck', 'circlet', 'fan', 'boot', 'quiver', 'helm', 'gloves', 'belt', 'cape', 'dagger', 'shackles', 'horn', 'staff', 'book', 'wings', 'crystal ball', 'carpet', 'cask', 'flask', 'map', 'artifact', 'trap', 'spear', 'halberd', 'key', 'stone', 'talisman', 'scimitar', 'bracer', 'bowl', 'chime', 'elixer', 'hat', 'clothes', 'headband', 'haversack', 'mirror', 'mace', 'rope', 'trinket', 'statue', 'hankercheif', 'locket', 'bone', 'skull', 'sickle']
    let action = [
        ["fighting a(n)", "being killed by a(n)", "stalking a(n)", "conquered by a(n)", "standing over a(n)"],
        ["looking towards the sky", "preparing to attack", "ready to swing", "sitting on a rock", "bracing for impact", "singing", "dancing in ceremonial dress"],
        ["sitting in its lair", `clutching a(n) ${searchArray(item)} tightly`, "stalking around a city", "in a house", "standing on top of a large building", "on top of a building"]
    ]
    let location = ["underfoot", "next to it", "in its mouth", "on its back"]
    let ageDescriptor = ["young", "older"]
    let adultGender = ["man", "woman"]
    let anyAgeGender = ["man", "woman", "boy", "girl"]
    let youngGender = ["boy", "girl"]
    let verb = [
        ["raiding a village", "destroying a caravan", "being killed by a hero", "being killed by a group of heroes", "surrounding a group of heroes", "fleeing from something large and ominous", "killing a child", "razing a village"],
        ["nursing a friend back to health", "holding a baby in their hands", `defending against an onslaught of ${searchArray(monster)}s`, "playing with a pet", "laughing with friends", "playing a tabletop game with friends", `holding (a(n)) ${searchArray(item)} in one hand, and a ${searchArray(item)} in the other`, `weeping with a lifeless ${variableEvent(ageDescriptor)}${findRace()} ${searchArray(adultGender)} in their arms`, `working on a ship`, 'leaning against a cannon', 'loading a cannon', 'boarding a flying airship', 'seated on an ornate throne', 'seated on an ornate throne, an arrow is headed towards their head', `walking underneath an archway surrounded by woodland creatures`, "dancing in long flowing clothes", "with an anguished expression on their face and a broken crown on their head"],
        ["nursing a friend back to health", `defending against an onslaught of ${searchArray(monster)}s`, "playing with a pet", "laughing together", "playing a tabletop game", `- one holding (a(n)) ${searchArray(item)}, the other holding (a(n)) ${searchArray(item)}, looking at each other`, `weeping with a lifeless ${variableEvent(ageDescriptor)}${findRace()} ${searchArray(adultGender)} in their arms`, `working on a ship`, 'leaning against a cannon', 'loading a cannon', 'boarding a flying airship', 'seated in a throneroom', 'seated in a throneroom, arrows are headed towards their heads', `walking underneath an archway surrounded by woodland creatures`, "dancing in long flowing clothes", ],
    ]
    let time = ["somehow up to date", "changing-in-real-time", "slightly outdated"]
    let drink = ["tankard of mead", "cup of ale", "glass of wine", "goblet of blood"]
    let scene = ['swamp', 'mire', 'bridge', 'gate', 'road', 'paradise', 'fort', 'house', 'hut', 'keep', 'garden', 'room', 'sanctum', 'asylum', 'hideaway', 'refuge', 'shelter', 'shack', 'den', 'clearing', 'dungeon', 'castle', 'cottage', 'dungeon', 'field', 'camp', 'lean-to', 'mountain', 'cave', 'town', 'city', 'lake', 'pond', 'lair', 'chamber', 'hovel', ]
    let weapons = ["sword", "dagger", "axe", "mace", "staff", "wand", "quarterstaff", "broadsword", "skull", "book", ]
    let bodyparts = ["eyes", "teeth", "skin", "external markings", "face"]
    let audience = ["royals", "monsters", "commoners", "villagers", "dragons", "tavern patrons", "heroes", `${findRace()}s`, `${searchArray(monster)}s`]
    let instruments = ["a harpsichord", "a piano", "a pipe organ", "bells", "chimes", "drums", "a gong", "a fiddle", "a harp", "a lute", "a mandolin", "a flute", "pan pipes", "a shawm", "a trumpet"]
    let color = [`black`, `pink`, `red`, `hazel`, `indigo`, `purple`, `rainbow`, `white`, `lime`, `grey`, `green`, `brown`, `orange`, `blue`, `yellow`, `gold`, `turquoise`, ]
    let projectile = ["dart", "javelin", "arrow", "wood splinter", "glass shard", "metal shrapnel", "spear"]
    let celebration = ["a bonfire", "a feast table", "an encampment", "a pile of bodies", "a pole in the center of town", "a pile of gold and gems"]
    let hair = ["long flowing", "short", "no"]
    let mount = ["dinosaur", "griffon", "pegasus", "dragon", "displacer beast", "mammoth", "lion", "tiger", "warhorse", "horse", "moose"]
    let organization = ['theives guild', 'city', 'temple', "oracle's", "king's"]
    let facialExpression = ["Awed", "angry", "disgusted", "surprised", "grinning", "stern", "fearful", "sad", "appalled", "smirking", "smiling", "beaming", "grimacing", "winking", "scowling", "terrified", "hardened", "stone-faced", "frowning"]


    let template = [
        `A ${variableEvent(size)}${searchArray(artForm[0])} depicting a(n) ${variableEvent(ageDescriptor)}${findRace()} ${searchArray(person)} ${searchArray(verb[1])}.`,
        `A ${variableEvent(size)}${searchArray(artForm[0])} depicting a(n) ${variableEvent(ageDescriptor)}${findRace()} ${searchArray(adultGender)} ${searchArray(verb[1])}.`,
        `A ${variableEvent(size)}${searchArray(artForm[0])} with the depiction of a(n) ${variableEvent(adjective,0)}${searchArray(monster)} ${searchArray(action[2])}.`,
        `A ${variableEvent(size)}${searchArray(artForm[0])} depicting a(n) ${searchArray(monster)} ${searchArray(action[0])} ${searchArray(monster)}.`,
        `A ${variableEvent(size)}${searchArray(artForm[0])} depicting a(n) ${searchArray(monster)} ${searchArray(action[0])} ${variableEvent(ageDescriptor)}${findRace()} ${searchArray(person)}.`,
        `A ${variableEvent(size)}${searchArray(artForm[0])} depicting a(n) ${searchArray(monster)} ${searchArray(action[0])} ${variableEvent(ageDescriptor)}${findRace()} ${searchArray(adultGender)}.`,
        `A ${variableEvent(size)}${searchArray(artForm[0])} depicting a gilded ceremonial ${searchArray(item)} being held by a(n) ${findRace()} ${searchArray(person)}.`,
        `A ${variableEvent(size)}${searchArray(artForm[0])} depicting a(n) ${findRace()} ${variableEvent(adultGender)}${searchArray(verb[1])}.`,
        `A ${variableEvent(size)}${searchArray(artForm[0])} depicting ${searchArray(many)} ${searchArray(monster)}s ${searchArray(verb[0])}.`,
        `A ${variableEvent(size)}${searchArray(artForm[0])} with ${searchArray(many)} ${searchArray(person)}s holding ${searchArray(tool)}s and ${searchArray(action[1])}.`,
        `A ${variableEvent(size)}${searchArray(artForm[0])} depicting a(n) ${searchArray(monster)} ${searchArray(action[2])} with a(n) ${searchArray(item)} ${searchArray(location)}.`,
        `A ${variableEvent(size)}${searchArray(artForm[0])} depicting a(n) ${searchArray(monster)} ${searchArray(action[2])}.`,
        `A ${variableEvent(size)}${searchArray(artForm[0])} depicting ${searchArray(historicalEvent)}.`,
        `A ${variableEvent(size)}${searchArray(artForm[0])} depicting two ${findRace()}s ${searchArray(verb[2])}.`,
        `A ${variableEvent(size)}${searchArray(artForm[0])} depicting a crying ${findRace()} ${searchArray(anyAgeGender)} holding a(n) ${searchArray(item)} in their hands.`,
        `A ${variableEvent(size)}${searchArray(artForm[0])} depicting a ${variableEvent(time)}map, with the name of ${toWords(2+rollDice(10))}locations on it.`,
        `A ${variableEvent(size)}${searchArray(artForm[0])} depicting a snake coiled around (a(n)) ${searchArray(item)}.`,
        `A ${variableEvent(size)}${searchArray(artForm[0])} depicting ${toWords(5+rollDice(15))}humaniods of various races holding a(n) ${searchArray(item)} over their heads.`,
        `A ${variableEvent(size)}${searchArray(artForm[0])} depicting a(n) ${variableEvent(ageDescriptor)}${findRace()} ${searchArray(adultGender)} raising a ${searchArray(drink)}.`,
        `A ${variableEvent(size)}${searchArray(artForm[0])} depicting a ${searchArray(scene)}, a(n) ${searchArray(monster)}, and ${toWords(2+rollDice(4))}humaniod figures ${searchArray(action[1])}.`,
        `A ${variableEvent(size)}${searchArray(artForm[0])} depicting a distraught ${variableEvent(ageDescriptor)}${findRace()} ${searchArray(adultGender)} clutching their chest with one hand and reaching out with the other.`,
        `A ${variableEvent(size)}${searchArray(artForm[0])} depicting a winged ${variableEvent(ageDescriptor)}${findRace()} ${searchArray(adultGender)} in a combat stance with a(n) ${searchArray(item)} in their hand.`,
        `A ${variableEvent(size)}${searchArray(artForm[0])} depicting a(n) ${variableEvent(ageDescriptor)}${findRace()} ${searchArray(adultGender)} with two ${searchArray(weapons)}s by their side.`,
        `A ${variableEvent(size)}${searchArray(artForm[0])} depicting a(n) ${searchArray(monster)} with large and intricately detailed ${searchArray(bodyparts)}.`,
        `A ${variableEvent(size)}${searchArray(artForm[0])} depicting a(n) ${variableEvent(ageDescriptor)}${findRace()} ${searchArray(adultGender)} astride a(n) ${searchArray(monster)}, holding a ${searchArray(weapons)} in their hand.`,
        `A ${variableEvent(size)}${searchArray(artForm[0])} depicting a(n) ${variableEvent(ageDescriptor)}${findRace()} ${searchArray(adultGender)} playing ${searchArray(instruments)} to ${searchArray(many)} ${searchArray(audience)}.`,
        `A ${variableEvent(size)}${searchArray(artForm[0])} depicting a(n) ${variableEvent(ageDescriptor)}${findRace()} ${searchArray(anyAgeGender)} kissing a(n) ${variableEvent(ageDescriptor)}${findRace()} ${searchArray(anyAgeGender)} on the cheek.`,
        `A ${variableEvent(size)}${searchArray(artForm[0])} depicting a(n) ${variableEvent(ageDescriptor)}${findRace()} ${searchArray(anyAgeGender)} with ${searchArray(projectile)}s stuck in their back, protectively holding a small ${searchArray(monster)}.`,
        `A ${variableEvent(size)}${searchArray(artForm[0])} depicting a(n) ${variableEvent(ageDescriptor)}${findRace()} ${searchArray(anyAgeGender)} with ${searchArray(projectile)}s stuck in their back, protectively holding a tiny ${searchArray(item)}.`,
        `A ${variableEvent(size)}${searchArray(artForm[0])} depicting a(n) ${variableEvent(ageDescriptor)}${findRace()} ${searchArray(anyAgeGender)} with ${searchArray(projectile)}s stuck in their back, protectively holding a baby ${findRace()} ${searchArray(youngGender)}.`,
        `A ${variableEvent(size)}${searchArray(artForm[0])} depicting a(n) ${variableEvent(ageDescriptor)}${findRace()} ${searchArray(anyAgeGender)} in a loincloth with a ${searchArray(ageDescriptor)} ${searchArray(monster)} next to them.`,
        `A ${variableEvent(size)}${searchArray(artForm[0])} depicting a(n) ${variableEvent(ageDescriptor)}${findRace()} ${searchArray(anyAgeGender)} holding a large bouquet of flowers in their arms.`,
        `A ${variableEvent(size)}${searchArray(artForm[0])} depicting a seated crying ${variableEvent(ageDescriptor)}${findRace()} ${searchArray(anyAgeGender)} holding a lifeless ${variableEvent(ageDescriptor)}${findRace()} ${searchArray(anyAgeGender)} in their arms.`,
        `A ${variableEvent(size)}${searchArray(artForm[0])} depicting a(n) a large group of mostly ${findRace()}s dancing and celebrating around ${searchArray(celebration)}.`,
        `A ${variableEvent(size)}${searchArray(artForm[0])} depicting a(n) ${variableEvent(ageDescriptor)}${findRace()} ${searchArray(anyAgeGender)} with a sword and shield fighting an imposing ${searchArray(monster)}.`,
        `A ${variableEvent(size)}${searchArray(artForm[0])} depicting a handsome bare chested ${variableEvent(ageDescriptor)}${findRace()} man with ${searchArray(hair)} hair riding a ${searchArray(mount)}.`,
        `A ${variableEvent(size)}${searchArray(artForm[0])} depicting a beautiful ${variableEvent(ageDescriptor)}${findRace()} woman with a ${searchArray(weapons)} in her hand riding a ${searchArray(mount)}.`,
        `A ${variableEvent(size)}${searchArray(artForm[0])} showing a schematic of all the planes of existence.`,
        `A ${variableEvent(size)}${searchArray(artForm[0])} depicting a faceless angelic being holding a ${searchArray(item)}.`,
        `A ${variableEvent(size)}${searchArray(artForm[0])} depicting a heavenly court.`,
        `A ${variableEvent(size)}${searchArray(artForm[0])} depicting a hellish court.`,
        `A ${variableEvent(size)}${searchArray(artForm[0])} depicting a ${searchArray(monster)} on top of (a(n)) ${searchArray(item)} with a ${searchArray(organization)} crest on it.`,
        `A ${variableEvent(size)}${searchArray(artForm[0])} depicting a ${searchArray(size)} ${searchArray(monster)} daintily picking up a ${searchArray(item)} at its feet.`,
        `A ${variableEvent(size)}${searchArray(artForm[0])} depicting a ${searchArray(item)} with various birds perched on it.`,
        `A ${variableEvent(size)}${searchArray(artForm[0])} depicting a ${variableEvent(ageDescriptor)}${findRace()} ${searchArray(anyAgeGender)} playing an ${searchArray(instruments)} with ${toWords(2+rollDice(4))}${searchArray(monster)}s looking at them.`,
        `A ${variableEvent(size)}${searchArray(artForm[0])} depicting ${toWords(2+rollDice(10))}${searchArray(person)}s looking at (a(n)) ${searchArray(item)} held by the one in the center.`,
        `A ${variableEvent(size)}${searchArray(artForm[0])} depicting ${toWords(2+rollDice(10))}${searchArray(monster)}s looking at (a(n)) ${searchArray(item)} on the ground between them.`,
        `A ${variableEvent(size)}${searchArray(artForm[0])} depicting a(n) ${variableEvent(ageDescriptor)}${findRace()} ${searchArray(anyAgeGender)} pouring a(n) ${searchArray(color)} liquid into a(n) ${searchArray(color)} flask.`,
        `A ${variableEvent(size)}${searchArray(artForm[0])} depicting an extremely detailed muscular ${variableEvent(ageDescriptor)}${findRace()} ${searchArray(anyAgeGender)}.`,
        `A ${variableEvent(size)}${searchArray(artForm[0])} depicting a ${searchArray(facialExpression)} ${variableEvent(ageDescriptor)}${findRace()} ${searchArray(anyAgeGender)} playing chess with a ${searchArray(facialExpression)} ${variableEvent(ageDescriptor)}${findRace()} ${searchArray(anyAgeGender)}.`,
        `A ${searchArray(artForm[1])}`
    ]

    if (number === 50) {
        printFrom(template, 50, "Art")
    } else if (number === 25) {
        printFrom(template, 25, "Art")
    } else {
        printFrom(template, 10, "Art")
    }
};