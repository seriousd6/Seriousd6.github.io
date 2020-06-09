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
}

//page scripts


function findCorruption() {
    let front = [
        "drug den", "bar", "marketplace", "racetrack", "gambling den", "regional 'philanthropic' organization", "brothel", "arena",
    ]

    let customers = [
        "high-society types, the elite", "criminals, ne'er do wells and blackguards", "working class folk", "travelers, tourists, pilgrims", "ethnically, culturally or racially exclusive", "people of a certain faith", "petty bourgeoisie", "all walks of life",
    ]

    let owner = [
        "run by criminals", "run by some sort of powerful and sinister being", "run by some sort of powerful and benevolent being", "run by a member of the elite", "run by a guild or trade organization", "run by outsiders, from another polity", "run by a church or cult", "individually owned",
    ]

    let uniqueFeature = [
        "built in or atop the corpse or bones of some great beast", "the owners have connections to smugglers and can arrange the purchase of illegal goods", "the location is protected from magical intrusion, including scrying", "no matter the time, the place is never closed, they will always accept customers", "the place is protected by the powers that be, there is little to no chance of being hassled", "a secluded room in the establishment is home to a portal or gate to another dimension", "the location of the establishment rotates or shifts over time or by a set schedule", "it requires a password, certain style of dress or invitation to enter",
    ]
    let output = "There is corruption in the " + searchArray(front) + ". It is typically frequented by " + searchArray(customers) + ", but it is " + searchArray(owner) + ". I heard that " + searchArray(uniqueFeature) + ", but I think you should check it out yourself."
    document.getElementById("Corruption").innerHTML = output
}

function findLegalStructure() {
    let setting = [
        "barracks/guardhouse", "customs house", "guildhall", "prefect/sheriff's office", "local military order", "noble's court", "temple", "elder's abode",
    ]

    let helpfulness = [
        "of the extralegal kind. conversely it is difficult to get the help the place is ostensibly supposed to provide.", "as one would expect of the place, but the means to gaining it is excessively bureaucratic and roundabout.", "normally, provided that you can bribe your way in.", "that is of high quality and without strings, but only the favored may avail themselves of it. Who is among the favored is determined by the leader.", "that is low, and without much zeal. They cannot turn anyone away, regardless of social strata.", "that is high, but only citizens in good standing with the community are able to use the services.", "that is average, only those of a certain class can use it, such as those of a certain ethnicity or faith.", `that is average, however it is hopelessly overworked and the waiting list is at least ${1+rollDice(6)} weeks long.`,
    ]

    let leader = [
        "short tempered and overworked, but competent and dependable.", "distracted and half-hearted, a product of nepotism.", "kind, but ineffectual and relatively powerless in their own organization.", "domineering and power hungry, will try to utilize players to help themselves.", "eccentric and slightly bizarre with a focus on a hobby entirely unrelated to their own organization.", "responsible and busy, a true delegator who may have other obligations.", "prone to risky behaviors and indulging in vice, often needs to be talked out of poor courses of actions by their underlings.", "gregarious, with an eye towards expansion. May try to recruit or pressure the players into helping them.",
    ]

    let quirk = [
        "there are no doors, banners, tapestries or decorations - the better to spot potential assassins or thieves.", "a familiar spirit has been bound to the place. Though it cannot affect the corporeal, it can protect against other incorporeal threats as well as observe intruders and warn the residents.", "the place was made to be as self-sufficient as possible, there are areas set aside for the cultivation of food, a well and more.", "the building which houses the organization is one of the largest and most reinforced in town, it finds use as a citadel when the community is threatened.", "the structure is multi-purpose and extremely important. many members of the community often visit every day, even if they have no need for services.", "this particular organization is important to the wider world, perhaps they are a regional headquarters, perhaps they are the site of a pilgrimage. Regardless, the organization is notably wealthier than the community around them.", "the organization is in possession of a holy relic, such as the bones of a saint. Extraplanar entities cannot enter the building without grievous harm coming to them.", "the stones of the place have been enchanted somehow to prevent the use of teleportation magics. No one may safely use spells such as blink, dimension door or teleport within a mile of the building.",
    ]

    let output = "The legal structure of this place is centered around the " + searchArray(setting) + ". They offer help " + searchArray(helpfulness) + " The leader is " + searchArray(leader) + " Curiously, I've heard that " + searchArray(quirk)
    document.getElementById("Legal Structure").innerHTML = output
}


function findThePeople() {
    let character = [
        "martial", "urbane", "faithful", "agrarian", "reserved", "mercantile", "peaceful", "decadent", "erudite"
    ]
    let govSubArray = [
        [ //0
            "fiend", "celestial", "aberration", "dragon", "undead/spirits",
        ],
        [ //1
            "spellcasters", "militants", "merchants", "priests",
        ],
        [ //2
            'popular', 'despised',
        ],
        [ //3
            "nearby polity", "far-away empire", "tyrant", "puppet governor",
        ],
    ]
    let governance = [
        `by a ${searchArray(govSubArray[0])}`,
        "a noble or member of royalty",
        "a council, perhaps of elders or potentates",
        "nobody. This place is in anarchy, law & order has broken down, or perhaps never existed in the first place",
        "criminals. They've overwhelmed the proper authorities, or perhaps it was their town to begin with",
        `a cabal of ${searchArray(govSubArray[1])} that is ${searchArray(govSubArray[2])} by the populace`,
        `an oppressive ${searchArray(govSubArray[3])}`,
        "democratically",
    ]
    let knownForSubArray = [
        "swimming", "hunting", "agility", "strength"
    ]
    let knownFor = [
        `their fine crafts`, `being near the site of a great battle`, `maintaining the grave of a great king or hero`, `their luxurious hospitality`, `their livestock`, `their physical prowess in ${searchArray(knownForSubArray)}`, `their skilled warriors or soldiers`, `their knowledge or learning`,
    ]
    let customsSubArray = [
        ["fiend", "celestial", "military order", "faith", "monster", ],
        ["by the local criminal organization", "through trial by combat", "augury (reading omens)", "through agreed upon written law"],
        ["in trees", "underground", "on or under water", "an animal or some other huge beast"],
        ["spellcasters", "a certain faith", "members of a certain race or ethnicity", "outsiders"],
    ]
    let customs = [
        `they are bound to service or stewardship of a ${searchArray(customsSubArray[0])}`,
        'these people are nomadic, whether by inclination or necessity, the community is where they are',
        'currency does not exist here, instead "gifts" & barter are the rule',
        `justice here is decided ${searchArray(customsSubArray[1])}`,
        'the people here dress themselves in strange clothes or odd adornments',
        `they dwell in an odd (to you) living space, namely ${searchArray(customsSubArray[2])}`,
        'interactions here follow a sort of script or tradition and it is taboo to break with them',
        `there is a fear or hatred held towards ${searchArray(customsSubArray[3])}`,
    ]

    let output = "This community is known for it's " + searchArray(character) + " citizenry, as well as for " + searchArray(knownFor) + ". They are governed " + searchArray(governance) + ". I've also heard that " + searchArray(customs) + '.'
    document.getElementById("People").innerHTML = output
}

function findTown() {
    let mainFeature = [
        'the town square', 'a water well', 'a bonfire', 'an open market/bazaar', 'a statue/shrine',
    ]
    let lodging = [
        'a relatively safe clearing near town', 'the house of a generous citizen with a vacancy', 'the open-air campground', 'a spare building (barn, empty home)', 'the communal lodge', 'the inn/tavern', 'the inn/tavern', 'the inn/tavern', 'the inn/tavern', 'the inn/tavern', 'the inn/tavern', 'the inn/tavern', 'the inn/tavern', 'the inn/tavern', 'the inn/tavern',
    ]
    let food = [
        'someone cooking their recent wild game/fish haul', 'neighbor (they share generously)', 'public vegetable garden', 'communal potluck', 'open pit barbecue', 'smokehouse', 'marketplace', 'tavern',
    ]
    let shop = [
        'blacksmith (armor, weapons, tools)', 'carpenter (boats, buildings, wagons)', 'tailor (common, fine)', 'leatherworks (armor, saddlery)',

    ]
    let specialtyShop = [
        'n alchemist/herbalist/healer', 'n enchanter/hex den', ' glassblower', ' horse trader', 'n exotic goods merchant (carpets & cloth, jewelry, perfumes, curio)',
    ]
    let economicTouchstone = [
        'the fact that it is a crossroads between a few larger settlements', 'their crops', 'their livestock', 'their docks/harbor', 'the ferry/major bridge', 'their fishery', 'their holy site', 'a source of magical power', 'their mill', 'the mine', 'that it became a trade hub', 'their defense (barracks, defending a strategic location or road, gatehouse, training)', 'their production industry (shipyards, ironworks)',
    ]
    let landmark = [
        'a wizard’s tower (active, abandoned)', 'a college (arcane, bardic, scholarly)', 'a combat training school', 'a church/shrine/temple', 'a fighting pit', 'a tended gardens', 'a guild hall (craft, trade, fighter, thieves)', 'a library/knowledge repository', 'a lighthouse or watchtower', 'a racetrack (dogs, horses)', 'ruins (castle, cathedral, shipyards)', 'a sealed cave entrance', 'what looks like a skirmish aftermath (neighboring town, invading horde, rampaging beast)', 'a spiritual lodge', 'a standing corporal punishment fixture (stocks, gallows, chopping block)', 'theater/amphitheater', 'that a river runs through it', 'that it is built into a hill- or mountain-side', 'that it is built into a canyon or ravine', 'that it is surrounded by forest/wilderness',
    ]
    let uniqueFeatures = [
        `there is a unusually large concentration of sky iron (meteoric iron) in the nearby hills`, `that in ancient times, these lands were flooded with lava from the nearby volcano. Today, the volcano lies silent, long since extinct, fertile soil is plentiful, and signs point to the possibility of veins of adamant (the main component of adamantine) underground`, `that the water from the lake is not only extraordinarily pure, it contains minerals that help to promote good health`, `that the nearby caves contain crystals made of concentrated magic`, `that there is a dangerous portal to yggdrassil (built to keep the baddies from comin out)somehwere nearby`, `that there is an alchemy ingredient only farmed here... like miniature bullette farms for their unfertilized eggs to make an omelette of digging giving you a burrow speed of 5' or 10' with a pick or shovel`, `that self aware water weirds gather fish for the nearby gnomes who then buy water from other sources with the fish money to feed the water weirds. They were influenced by the gnomish goodness long enough to change their attitude`, `that the hills around and in the village are actually giants’ skeletons, long since grown over in a graveyard forgotten`, `that there is a giant slab of rock. If the slab comes down the whole city comes down with it one building at a time`, `that there is an abandoned cursed royal palace which has the corpses of the royal family and the previous king inside. People call the city the “dead capital” because of this`, `the town has a giant sleeping monster under it, with parts of its claws, feet, mouth and tail in different underground places of the town (abandoned houses basements, sewers, etc...)`, `there is a shrine to an unknown god, that gets regular blessings and sacraments`, `there was an animal that saved a child from a lake, and the village was the original settlers who protected the animal out of respect`, `there are some unique flowers here that make a honey that had unique properties`, `the city is in a bio-dome/micro climate`, `this is a highly magical city that binds underneath a sleeping tarrasque - stolen from somewhere else`, `the village is protected by an invisibility bubble in the middle of a forest`, `the village is only accessible by a lifting bucket, as it is in the middle of a tight mountainous land - think the greek meteora monastery`, `that the town is a thieves guild operation center and has all kinds of subterranean tunnels leading outwards, and connecting major buildings`, `the town has a giant spire enables ordinary people to cast sending across the continent`, `the town is at the site of an ancient battle between giants and dragons have filled the area with giant skeletons and weapons. People have used these as a foundation for their houses`, `the entire town is built around a school that teaches magic. As a result everyone can cast some magic`, `that for some reason, the chickens grow real big here. Like turkey-size, not t-rex size. Eggs are bigger, too. Nobody knows why`, `that eons ago, a gargantuan semi-magical whale died here. Its blubber has seeped through cracks in the rock under the earth, and can occasionally be found dripping from cliffs on the side of the hill that formed above the carcass. The blubber can be used for lamps, greasing axles, and many other uses. There is a thriving mining industry exporting the blubber to the nearby towns and cities, but it's becoming harder and harder to find usable veins of blubber`, `that a pleasant song constantly plays on the very edge of hearing. The town is tranquil and peaceful; arguments are resolved amicably, and fights never break out amongst the residents. If outsiders come into town and attempt to fight, they will find that any lethal attacks or spells suffer a flat -5 damage reduction. Nonlethal attacks are unaffected`, `that the trees in the forest surrounding the town are slightly sentient. Unusually fast-growing, they built up a surplus of dried and seasoned branches still attached to the tree. Anybody walking through the forest holding at least one twig of dry firewood will find branches dropping in neat circles around trees near them. There's no need to wear a helmet: the trees are careful not to hit anybody. In return, the villagers divert a portion of their manure and compost to fertilizing around the trees, and allow their goats to graze in the forest, eating plants that compete with the trees. When the town is about to be in danger, the trees will start dropping healthy branches with leaves, alerting villagers in time to build defenses`, `the town has a large geyser or hot spring`, `that the center of town is always raining. no one knows why. It's suspected that it is magic from an ancient wizard, and no one is able to stop it`, `there is a feral cat that lives in town. All the people worship the cat, despite the fact that it seems like a normal cat`, `the town is made up of cliff dwellers who mine guano from an extensive network of deeper, bat infested caves, and who exports fireworks`, `the town is a cosmopolitan atoll inhabited by folks who are comfortable living both above and below sea level`, `that the town is atop a mesa that breeds and trains griffons and other winged mounts`, `that a giant metal rod has been left in a field over the ages people tried to investigate it but had no luck in finding out why it was there. Eventually people built a town around this pole and now there can always be sure of a thunderstorm in the town. The townspeople used this to their advantage and are now leading in the use of electrical appliances`, `there is an obelisk at the center of town fairly hums with magical power. All the townsfolk can tell you about it is that it brings good health and prosperity to the town. you learn that they’ve never had a blight to their crops in the town’s history, and neither flood nor drought afflicts then either. A child skips happily around the town square, proclaiming it is her birthday. Indulgently, you ask how old she is today, and you’re shocked when she proclaims herself to be 50 years old today. the other children chime in with their ages, and you’re surprised that the older teenager minding them proclaims herself to be 96 years old! the people of this town know no illness. They know no hunger. The river of time flows slowly around them, and the elders remember fondly the founding of the town hundreds of years ago. They all attribute the town’s happiness and good fortune to the obelisk, but none seem to find this odd`, `that the town is built on a literal mountain of bodies and populated by friendly undead residents`, `that the dangerous creatures in the thick forest nearby refuse to pass the tree line where the town was built. There are ancient glowing stones dug deep into the ground in a circular pattern around the city and nobody knows the origin of them as it has been lost with time`, `that this town was built on an island in the middle of a river. The river splits in two, creating a sizable chunk of land before merging below the city again. A rock escarpment in the upstream portion of the island provides a base for a considerable citadel with which to observe (and tax) the river traffic`, `the town is built next to a giant mining pit. the mining company has long since moved on because the lode of copper went dry. the pit is wide and deep. The town has a bad habit of casting things to get rid of into the pit. offal. chamber pots. criminals. you know... garbage. Once a year, however, on hextor's eve, things cast in the pit tend to come back`, `the town was built around the harvest of giant bee honey. The fields are well pollinated and the honey the bees produce is known far and wide to be a delicacy but harvesting it is not for the faint of heart.`, `the town's treasure is wolfpine. A big pine that smells like wet dog. Keeps wild animals from wondering into town`,
        `the town is built on top of an unusual “island” that occasionally moves, looks suspiciously like a turtle shell and freshly boiled fish are often found along the beaches of this “island”. The townsfolk all worship some strange turtle-like deity`, `the town is built along the edge of, and in the sides of, the place where the god fell (an impact crater, visually) - the god's residue still lingers, harvested by magic-users in secret, and guarded by priests`, `that a cabal of evil wizards created a permanent gate to the nether realms. they were defeated and the gate locked by a group of adventurers, but they weren't able to fully close it. The energies that leak out around the lock attract evil beings, who in turn attract heroes to fight them, and who in turn attracted shopkeepers who knew the real way to become rich wasn't to go adventuring but to sell swords to the adventurers`, `the town exists at the exact center of a large anti-magic zone, making it ideal for people on the run from some magic-user or merchants who don't want to see a fourth business go up in fireballs`, `that long ago, the avatar of a agriculture deity was sacrificed here. the fallout from her death fertilized the land and has ensured good crops ever since`, `that the town is built up around an oasis which provides a vital resource not found anywhere else nearby. This could be water in a desert, air in an undersea kingdom, or just dependable rules of reality in a chaotic far realm`, `that this town has a connection to a gigantic corpse of some elder god that floats in the void. A mining colony sprung up to harvest body parts for all manner of alchemical and magical reagents. adventurers come to bid on the lucrative contracts to protect the miners from still active antibodies and parasites`, `that this fishing village is built mainly upon the side of a gigantic karst just offshore, accessible by wooden stairways and rope ladders. Those with particularly strong ties to nature (or geology) recognize that this karst is not made of stone, but is actually the petrified remains of a titanic tree that once rose out of the ocean`, `that at the center of a large crater there is a large spring of fresh water, the only source of drinkable water within a hundred miles (a desert, tundra, swamp, or arid savanna). The crater itself is lush and green - nearly tropical, even - and the people enjoy a comfortable existence. However, the inhospitable landscape around the crater leaves the townsfolk unable to travel, and news barely ever reaches them`, `that a geyser at the center of the village deep within the taiga erupts, with clockwork regularity, at noon every day. In the winter, the townsfolk gather around the geyser to enjoy the warm steam from its eruptions, and during the spring children frolic underneath the spout of water and play`, `the mining village has sprung up around the massive hole left in the ground by a passing elder purple worm. the worm disrupted hundreds of thousands of gold worth of ores and precious gems - though only the most experienced miners and spelunkers can safely traverse the deep tunnel`, `that giant metal pumps from ages long ago keep the endless subterranean caverns filled with locked vaults and adamantine doors beneath the city dry enough for explorers to delve. for 300 years, adventurers and archaeologists have flocked here, extracting untold wealth every time a vault is successfully opened`, `that lava from the mountains flows under the town, giving rise to several hot springs`, `that the town is at the edge of a rain-forest, a forest made of literal rain. This is their primary means of water collection, and by extension, agriculture. They must traverse the treacherous rain-forest and its amphibious residents, including the frog-men ninja clans`, `the town is plagued by sky-stompers (you could replace sky-stompers with dragons if you prefer), giant, glistening, photosynthetic monsters that hover in orbit, only occasionally dropping to the planet for a quick breath, water, other nutrients, or mating. the entire town exists on moving structures, and astrologers and geomancers are trained to predict the drops and move the town to a nearby but safe distance from the dropped sky-stompers. for as much as a hassle as this can be, for the brief period of time the sky-stompers land, they often bring with them items or resources of scientific or religious interest, or of practical value, from far above. a religion has also formed around the sky-stompers, with many believing they are messengers who come and go from the celestial realm itself. Scientists believe that energy can be siphoned from the sky-stompers, which could lead to full-scale industrialization. A fantasy and/or solarpunk setting`, `there is a bottomless pit with an intricate cave system with fertile soil and bioluminescent bacteria meaning free real estate for farming`, `that a spring gushes forth from the center of town, providing a nearly unlimited supply of sweet fresh water. The town has a legend that many centuries past, a nature spirit disguised herself as a homeless traveler and was given warm reception by the town. In return for their kindness she caused the spring to burst forth. Since that time, no wanderer is ever turned away by the townsfolk, some saying that to do so would cause the spring to dry up`, `that a massive telescope like device fell to pieces on the edge of a large desert. The angel, and still in tact glass dome created a massive terrarium full of strange exotic woods and creatures. The village has built up around the metallic walls, and use the various game and lumber as their livelihood. Upkeep on the glass dome it top priority`, `the town is ringed by a large wall made out of living trees: in fact a specific tree known as a "walking tree." As it grows, it sends out branches that will eventually root into the ground and grow another trunk. The villagers, over centuries, have carefully pruned and guided the growth of the tree until it has encircled the town. now the roots are deep in the earth, while the trunks are twisted giants blocking all entry. two large gates have been carefully maintained as arching openings in the wall (though canny carpenters have fitted swinging doors to the arches). Some of the branches have been sewn into walkways that mimic battlements and provide protection and security to the defenders. due to its great age, at this point the bark is nearly as hard as stone, heavy with moss that denies fire a purchase, and eerily beautiful`, `the city is built on a extremely wide solid rock plateau. carved into the ground are massive teleportation circles that surround the city. When activated (through some strenuous magical means) it teleports the whole city into a sealed underground cavern with no entrances or exits. Essentially making it an escape bunker until whatever danger was threatening the city passes`, `the ruins of a temple lay in the city center. What's abnormal about this temple is the alter to an unidentified god that constantly sprays fresh clean water from a pot he holds into a fountain beneath him giving the city an unending supply of clean water`, `that the town was built on the back and in the arms of an enormous golem like giant creature who one day started walking out of the side of the mountain where the city originally was built centuries ago. It walks at a pace slow enough to not be felt much by the residents. Perhaps it's destination is important`, `there is a huge intricate sun dial that as well as telling the time for the locals has a tally that is ceremoniously completed every summer solstice. However this coming summer an ancient carving of a skeleton lies in the next available tally spot. There are many rumours of what this foretells but most agree it is the end of times`, `the whole village lies on a rotating stone bed one mile in diameter. Local dwarven miners dug exploration tunnels to determine the cause of this turning. one by one curses, misfortune and death befell anyone who was involved in the mining exploration and thus all efforts have ceased`, `that this village is built in a monstrous towering evergreen tree with an incredibly ornate spiral staircase that traverses around the outside of the bark and a working pulley lift system to transport resources up and down the centre of the trunk. Each of the 50 or so branches can support two or three huts and there is a clear hierarchy of wealth. The lower branches are occupied by the poor labourers whilst the very canopy is the residence of the wealthy`, `that this village situated in the middle of a gas marsh. The small town is built on an artificial hill and the gates are secured at sunrise when the marsh fills with noxious gas`, `that the town is built around a wizard's tower. Every wizard that has taken up residence there has supported and cared for the townsfolk. The town itself is littered with small magical artifacts made by wizards of the tower in days gone by. Examples are a magically turning water wheel that brings water up from the bottom of the well and local hospital that the current wizard makes weekly visits to`, `that a unique breed of sea creature frequents the area of this fishing town. When properly prepared, parts of this creature can be used to create potent healing tonics, while if prepared another way, it can be used to create potent poison. The assassin's guild and healer's guild in this town are continually at odds, trying to control the supply of the creatures for their own uses`, `that this is a thriving town built around the corpse of a terrasque felled generations ago. No one has determined a means to permanently kill it so the city corp of miners harvest and despose of matter as fast as it regenerates. Rumor has it that if it were permanently killed it would manifest elsewhere to wreak havoc, that is why more powerful magics are highly regulated in the region`, `that a huge meteor crater that has a lake in it, with an “island” at the centre`, `this village is hellgate - a quaint village built inside of a cavern, inhabited by tieflings, demons, and warlocks. In an adjacent antechamber there is a massive adamantine gate carved with images of debauchery and torments, a pilgrimage site for all who worship the infernal. The town is filled with shops that sell pentacle charms, goat-headed statues, brimstone candles, and other religious paraphernalia. Once a year, the villagers hold a doomsday parade. They march through the streets carrying battering rams, which they take to the antechamber and knock on the hellgate itself. Afterwards, there is much drunknenness and merriment`, `that this town was built around an strange wreck in a crater. The inhabitants of starfell are of an unknown race. They are hospitable but aloof and will not answer questions regarding their nature or that of the wreck. Outsiders are welcome to visit the markets and taverns in the crater, but exploring the ruined structure is forbidden. Any character that is attuned to living things will notice that there are a number of faint life signs emanating from inside the wreck..`, `this town was fractured across multiple realities in a long-forgotten cataclysm. Most of the main streets and markets are in our universe, but beware of entering strange doors or alleyways--they can leave you stranded in a parallel reality if you don't know how to find your way back. The city is filled with the ephemera of other universes: there is coinage bearing the faces of leaders and nations that never existed; there are books filled with spells and alchemical formulae that don't work here; there are pieces of magic and technology that are utterly unknown, and will cease to work if taken far from splinterpoint`, `this town was built on the back of a massive land snail. The crawl has a single main road that winds in a spiral up to the peak of the shell. Most of the time, the crawl stays in the wild areas far from civilization and trade routes--most believe it is nothing more than a legend. The few explorers who manage to find it can trade for healing snail-slime unguents, pearls, and knives and jewelry crafted from nacre`, `that long ago a band of heroes battled a necromancer and were able to defeat him by turning him to stone; the now stone necromancer stands on the hill overlooking the town, covered in graffiti. His finger still points to the town's center`, `that a chain, with links as big as the city itself, is anchored to the earth around the city's borders and protrudes into the sky; nobody knows what it is attached to on the other end`, `this town has a high wall, made entirely of what appears to be skeletons (either made of or possibly coated in metal) with outstretched hands, as though they are reaching for something, that stretches as far as the eye can see; the wall itself exudes a powerful fear aura which deters locals from approaching, peering over, or going around it`, `this town has a very large tree, which, when rested directly under for at least a long rest, permanently bestows the plant sub-type on the resting pc/npc. this change in sub-type can only be reversed with a wish spell; the spell will automatically fail however, if both the afflicted and the caster are not directly under the tree`, `there is a nearby field is full of hundreds of tenser's floating discs which wander the field aimlessly, allowing wildlife to appear to defy gravity. Nobody knows where they came from or how long they have been there, but they range in appearance from completely transparent/translucent to covered in dirt and other sparse natural phenomena. Anyone that is in physical contact with one of the discs may mentally control it at will, but it will not leave the borders of that field`, `that a neighboring village has balls of floating light appearing intermittently that cause anyone that sees them to stop what they are doing, stand in place, stare blindly into the distance, and babble (and sometimes drool) gibberish to themselves for hours. This is a daily occurrence the villagers have turned into a sport they lovingly refer to as "babble-ball" where the last man standing that has not laid eyes on the orbs that day wins. Chikoh is the reigning champion who has not "been babbled" for the past 22 days, since he was last caught with his pants down babbling with the butcher's wife`, `this village has an idiot. This idiot is not just any village idiot, mind you; he is bound to the land, magically speaking of course. When he is happy, the weather is agreeable, crops are plentiful, etc. and when he is feeling bad the weather is extreme for whatever season it currently is, wildlife becomes sparse and hostile, etc. The villagers fear that should he die, the land would die with him, so he is kept indoors and tended to hand and foot like a god in order to keep him safe and happy. He likes to get out and cause mischief though, whenever he can`, `this city has a large pedestal in the middle of downtown there a glass orb sits with an object inside. This object is constantly shifting form to resemble the various currencies of the world. Rumors circulate that if the orb is ever broken whatever currency it is currently in the form of will disappear world-wide, others say that if it is broken whatever currency it is in the form of will erupt forth from it. As a result of these and other rumors, the city guard and local mages college have formed a unified front to defend the orb from any attempt at breaking it open, though all attempts have proven ineffective since a visiting mage from a neighboring city experimented by dropping an elephant on it and it was undamaged`, `that on the outskirts of town there is a giant metal dome. Inside this dome is a series of smaller metal domes (like a nesting doll). At the core, rests the still-beating heart of a hill giant that once tended the land with utmost care. The heartbeat, however faint, echoes through the layered domes and grants a calming effect on those that hear it`, `this desert oasis has its own permanent portal to the elemental plane of ice located just left of the pond in the palm grove. Very popular tourist attraction`, `that this is a simple farming village with really fertile soils. Because after battling at the same exact place for thousands of years, the grounds are fertile due to the excess punts of blood and bone that the ground soaks`, `the only known vein of living silver, a crucial component in the making of great weapons, lies beneath the mines that this village supports`, `a millenia ago, the ancients knew better ways to survive, explore, and travel the great vastness of the sky-void; than capturing and enslaving air elementals to provide lift and thrust to the great ships of etheria. Now, an entire civilization and the lives of every being depends on finding elemental alcheras, holes in reality where the elemental planes poke thru, entering them, and capturing short-lived elementals, then getting out before the alcheras close. This is one of the only known stable alcheras ever found, deep inside a floating island known as "the respite", built up over the years from the floating hulks of several hundred airships of war moored around a small chunk of floating stone a quarter mile across. ships everywhere flock here for water, fresh elementals, and repair, and the weaponry bristling aboard the respite keeps it firmly in the hands of the ruling elite`, `there are remains of an intelligent, prehistoric life form in the centre of the town. When people have touched the remains they gain some sort of change to their self be it they gain magical powers or they lose a limb. The town is based off of the ‘blessing’ of the forgotten one. Some people are lucky, others are not`,
    ]
    let output = "In the center of the town you notice " + searchArray(mainFeature) + " and " + searchArray(landmark) + ". While on your way to where the town can host you, " + searchArray(lodging) + ", you smell food... it is coming from the " + searchArray(food) + ". There are a few shops in town, a general store, a " + searchArray(shop) + ", and a" + searchArray(specialtyShop) + ". The town's economic touchstone was/is " + searchArray(economicTouchstone) + "." + " Rumors of this town say " + searchArray(uniqueFeatures) + '.'
    document.getElementById("Town").innerHTML = output
}

function findResources() {
    let food = [
        "pelts/game (rich ecosystem)",
        "fish (natural fisheries)",
        "farmed animals (using range land)",
        "clean water and farming (aquifer)",
    ]
    let luxury = [
        "non-precious stone or metal (large sedimentary rock formations)",
        "sap/rubber (sugar maple/ rubber tree)",
        "timber (lush forests)",
        "precious stones or metal (large underground caverns)",
    ]
    let prosperity = [
        "nearly exhausted. The community is likely dying if this is the only major resource in the area. The resource itself has nearly petered out.",
        "on it's last legs. While there are some reserves left, it has grown increasingly clear to everyone that the good times are gone.",
        "hitting hard times. If any one was on the precipice of leaving, they'll probably do so now.",
        "hitting a rough patch. The easy work has started to dry up; outsiders trying to make their fortune will not be welcome.",
        "business as usual. Residents have long ago developed a routine, the extraction is steady and the methods are all well known and effective.",
        "experiencing rising tides. People are rich, there's always a hunger for new laborers and the community is building for the future.",
        "flourishing. New claims are being made all of the time, the amount seems almost endless.",
        "in 'boom town' mode. The amount of material they have on hand is enough to support their own needs, as well as several smaller outlying communities.",
    ]
    let hazard = [
        "hellish. Procuring the resource is almost more trouble than it is worth. perhaps there are hostile beings or spirits guarding it, or it is in an area of active environmental peril.",
        "miserable. There could be aggressive or predatory creatures which lurk in the area, or it could be in a place which is unpleasant to work in, such as an area with constant inclement weather.",
        "normal. It is as dangerous to gather this material as it would be in real life.",
        "normal. It is as dangerous to gather this material as it would be in real life.",
        "normal. It is as dangerous to gather this material as it would be in real life.",
        "normal. It is as dangerous to gather this material as it would be in real life.",
        "safe. The resource is well-managed and maintained, perhaps there is competent management, or the area itself has somehow been changed to ease the work.",
        "arcadian. It is so easy to find or secure more of the material that is is nearly worthless locally.",
    ]

    let interesting = [
        "the resources are contested, whether by another nearby community, or some sort of population or force which guards it.",
        "while the quality of the material is objectively as high as any other location, it is widely thought of as being cursed or bringing ill-luck.",
        "the material isn't naturally occurring, it is being drawn from the ruins or rubble of some previous civilization.",
        "an annual ritual or sacrifice is required to keep the spirits or beings which inhabit the area satisfied. The consequences will be dire if the oblations aren't performed.",
        "the resource requires a special treatment or process to be rendered safe to humanoids. This process is a closely guarded secret.",
        "a guild or another similar organization controls access. Competitors can expect serious reprisals.",
        "the quality of the resource from this area is renowned far and wide. It fetches an unusually high price.",
        "gathering the resource can only be done on a certain schedule. Perhaps it is underwater some of the year, or the path to access it is cut off for weeks or months on end.",
    ]

    let secondaryAction = [
        'they do not know of/ understand their capability for using/exporting ',
        'they are also well aware of and capitalize on ',
        'they cannot access (due to natural barriers) ',
        'something has taken away their previous access to ',
    ]

    function pickFoodOrLuxury() {
        let chance = rollDice(100)
        if (chance < 50) {
            return "has a focus on exporting their " + searchArray(food) + ' while ' + searchArray(secondaryAction) + searchArray(luxury) + "."
        } else {
            return "focuses mainly on harvesting and exporting " + searchArray(luxury) + ' while ' + searchArray(secondaryAction) + searchArray(food) + "."
        }
    }
    let output = "This community " + pickFoodOrLuxury() + " Regarding the main resource, it is " + searchArray(prosperity) + " Getting the material is " + searchArray(hazard) + " Also, " + searchArray(interesting)
    document.getElementById("Resources").innerHTML = output
}

function rollTown() {
    findTown()
    findResources()
    findThePeople()
    findLegalStructure()
    findCorruption()
}