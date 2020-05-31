function rollDice(number) {
    result = 1 + (Math.floor(Math.random() * number))
    return result;
};

function shuffle(array) {
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
    }
    return array;
};

function searchArray(array) {
    return array[Math.floor(Math.random() * array.length)];
};

var th = ['', 'thousand', 'million', 'billion', 'trillion'];
var dg = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'];
var tn = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen'];
var tw = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety'];

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

function populate() {
    var worldIntSpecies = [
        "Only " + '@@Placeholder@@' + "species, Humans, exist in this world.", "Only Humans and " + '@@Placeholder@@' + "other significant subspecies exist in the world.", "Humans and " + '@@Placeholder@@' + "other species exist in the world.", "Humans and " + '@@Placeholder@@' + "other species exist in the world.", "Humans and " + '@@Placeholder@@' + "other species exist in the world.", "Humans and " + '@@Placeholder@@' + "other species exist in the world.", "No Humans exist in the world, instead, there is/are " + '@@Placeholder@@' + "other species.", "No Humans exist in the world, instead, there is/are " + '@@Placeholder@@' + "other species.", "No Humans exist in the world, instead, there is/are " + '@@Placeholder@@' + "other species.",
    ];
    const worldSpecArchetypes = [
        "Brute - This species is known for its prodigal strength, near-endless endurance, and dim wittedness.", "Vermin - This species is known for its individual incompetence, short lifespan, and rapid rate of reproduction.", "Agile - This species is known for its incredible dexterity, mind-boggling flexibility, and skill at moving unseen.", "Elder - This species is known for its ancient history, long lifespan, deep wisdom, and keen intellect.", "Comfy - This species is known for its tight-knit families, friendly demeanor, and talent at agriculture.", "Alien - This species is known for the unsettling adaptations that allow it to thrive in areas other species couldn’t.", "Artisan - This species is known for its industriousness, secretive demeanor, and talent at craftsmanship.", "Big/Tiny - This species is known for its physical stature, which is much larger, or smaller than other species.", "Arcane - This species is known for its high affinity for the supernatural, or its seemingly supernatural abilities.", "Collective - This species is known for its intensely hierarchal society, and the huge variation between its castes.", "Mundane - This species is known for its lack of distinguishing traits, versatile mediocrity, and widespread settlement.",
    ];
    const specInterRelat = [
        "Master Race - One species is widely considered to be superior paragons, to which others should defer.", "Enslaved - One species is widely considered to be inferior, and is enslaved to an extent by the other species.", "Race War - The species rarely meet, unless weapons are drawn. There is a long-held and irreconcilable animosity between the species.", "Deep Mistrust - The species shun and avoid one another if possible, though outright violence is uncommon, race riots aren’t unheard of.", "That Part of Town - Members of both species that live in the same region are discouraged from closer association. Any close relationships would mark those involved as pariahs.", "Separate But Equal - The species have no hate for one another, and show their respect by staying out of each other’s way. Though there may be trade, the societies themselves are largely separate.", "Pragmatic - Members of both species are businesslike in their dealings with one another, if it pays off to band together they’ll do so, but they won’t go out of their way to integrate.", "Melting Pot - The species meet, trade, and form alliances fairly cordially, but primarily in trade hubs and major population centers. Sparks fly and cultures blend.", "Amicable - Members of both species get along fairly well, all things considered. There are prejudices, but they are by no means universal.", "Friendly - The species are quite close to one another, and interspecies marriages are not uncommon, though there are some few who’d prefer to remain separate.", "What Species? - Members of both species are blind to their differences, and view themselves as one and the same in all matters, save mutually exclusive physical needs, of course.", "The Same Species - Members of both species are in fact members of the same species, and can’t exist without one another, each is either different phases in the same species’ lifespan, or comprised of only gender that requires the other to reproduce. If deemed appropriate, this table may be rerolled to determine the relations between each part of the species.",
    ];

    let intSpecIndexObj = {
        '0': 0,
        '1': 3,
        '2': 4,
        '3': 6,
        '4': 2,
        '5': 8,
        '6': 3,
        '7': 6,
        '8': 9,
    };

    function findSpec() {
        let intSpecIndex = Math.floor(Math.random() * worldIntSpecies.length);
        let rawString = worldIntSpecies[intSpecIndex];
        let otherSpecies = (rollDice(intSpecIndexObj[intSpecIndex].valueOf()));
        let numbSpecInWords = toWords(otherSpecies);
        let fixedString = rawString.replace("@@Placeholder@@", numbSpecInWords);
        //document.getElementById("Species").innerHTML = fixedString;
        console.log(fixedString)
        if (intSpecIndex >= 6) {
            let numbSpecies = otherSpecies;
            return numbSpecies
        } else if (intSpecIndex === 0) {
            let numbSpecies = 1
            return numbSpecies
        } else {
            let numbSpecies = 1 + otherSpecies;
            return numbSpecies
        };

    }
    let numbSpecies = findSpec()
    console.log(numbSpecies)

    function findSpecArchs() {
        let numArchs = numbSpecies;
        let finalArchs = shuffle(worldSpecArchetypes).slice(0, numArchs)
        let chosenArchs = finalArchs;
        return chosenArchs
    }
    let archetypes = findSpecArchs()

    document.getElementById("Intera").innerHTML = JSON.stringify(archetypes, null, 4);

    function findInteractions() {
        if (numbSpecies === 1) {
            return 'There are no other species, this race has taken over the world.'
        } else if (numbSpecies === 2) {
            let interaList = specInterRelat;
            shuffle(interaList);
            var finalIntera = interaList.slice(0, 1)
            return 'There is only one relationship between these two species:' + '#1: ' + finalIntera[0];
        } else {
            let numOfInteract = Math.floor((numbSpecies / 1.5) + .5);
            let interaList = specInterRelat;
            shuffle(interaList);
            var multipleIntera = interaList.slice(0, numOfInteract)
            return multipleIntera
        };
    };
    let interactions = findInteractions()
    console.log(findInteractions());
    document.getElementById("Intera").innerHTML = JSON.stringify(interactions, null, 4);
};
populate()