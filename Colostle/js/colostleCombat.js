/*###################Chance and array manipulation methods#########################*/
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
function rollArray(array) {
    let shuffled = shuffle(array)
    let index = Math.floor(Math.random() * shuffled.length)
    return `(Roll: ${index}/${shuffled.length}) ${shuffled[index]}`;
};
function searchArray(array) {
    let shuffled = shuffle(array)
    return shuffled[Math.floor(Math.random() * shuffled.length)];
};
function variableEffect(array, array2, array3,array4) {
    let chance = rollDice(100)
    if (chance > 80) {
        return 'No Special Effect'
    } else if (chance > 60) {
        return searchArray(array3)
    } else if (chance > 40) {
        return "Observing this artwork has caused " + searchArray(array2[0])
    } else if (chance > 20){
        return "If you " + searchArray(array) + ', then ' + searchArray(array2[1])
    } else {
        return `This artwork is cursed. ${searchArray(array4)}`
    }
};
function variableEvent(givenArray, number) {
    let chance = rollDice(100)
    if (chance < 75) {
        return ""
    } else if (number === undefined) {
        return searchArray(givenArray) + " "
    } else {
        return searchArray(givenArray[number]) + ' '
    }
};
function printFrom(array, number, id) {
    let list = shuffle(array).slice(0, number)
    list.forEach(function(item) {
        var li = document.createElement("li");
        var text = document.createTextNode(item);
        li.appendChild(text);
        document.getElementById(id).appendChild(li);
    });
};
function modify(number) {
    return Math.floor(number * (.95 + Math.random() * .4))
};
function shuffleSlice(array, number) {
    return shuffle(array).slice(0, number)

};
function loopCountPrintList(array, id) {
    let x = array

    function count(array) {
        a = array
        a.sort();
        var current = null;
        var cnt = 0;
        let final = []
        for (var i = 0; i < a.length; i++) {
            if (a[i] != current) {
                if (cnt > 0) {
                    final.push(cnt + "-" + current);
                }
                current = a[i];
                cnt = 1;
            } else {
                cnt++;
            }
        }
        if (cnt > 0) {
            final.push(cnt + "-" + current);
        }
        return final
    }
    final = count(x);
    final.forEach(function(item) {
        var li = document.createElement("li");
        var text = document.createTextNode(item);
        li.appendChild(text);
        document.getElementById(id).appendChild(li);
    });
};
function loopPrintList(array, id) {
    array.forEach(function(item) {
        let li = document.createElement("li");
        let text = document.createTextNode(item);
        li.appendChild(text);
        document.getElementById(id).appendChild(li);
    });
};
function printArray(array) {
    for (i = 0; i < array.length; i++) {
        console.log(array[i])
    }
};
function checkConflict(coord,array){
    let bad = 0
    for (i = 0; i <= array.length; i++) {
        if (JSON.stringify(coord) === JSON.stringify(array[i])) {
            bad = 1
            return bad
        } 
    }
    return bad
};
function combineArrays(array1,array2,sizecount){
    let c = []
    let i = 0
    do { 
        let addition = [`(${array1[i]}) | ${ array2[i]}`]
        c[i]= addition
        i++
    } while (c.length < sizecount)
    return c
};
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
function reload() {
    location.reload()
};


/*==================================================================================*/
/*-----------------------------Page Scripts Below-----------------------------------*/
/*==================================================================================*/


//General Combat
    //Rooks
    const magic = [
        'No','Scientific', 'Artisan' , 'Arcane' , 'Natural' , 'Legendary', 'Forbidden' , 'Dimensional', "Light", "Shadow", "Time", "Chaos", "Illusion", "Stealth", "Enchanting", "Technomancy", "Emotion", "Psychic", "Dream", "Necromancy", "Music and Song", "Mirror", "Word", "Hex", "Void", "Bloodline", "Blood", "Corruption", "Alchemy", "Plant", "Animal", "Transformation", "Destruction", "Alteration", "Healing" , "Crystal", "Sight", "Bone", "Dragon", "Divine", "Defensive", "Absorption", "Battlefield", "Aura", "Banishment", "Divination", "Physical", "Spirit", "Fey", "Wish", "Order", "Sealing", "Summoning", "Dance", "Love", "Sacrifice", "Infernal", "Culinary", "Luck", "Wild", "Death", "Life", "Mycomancy", "Cataclysmic", "Weather", "Geo-Shaper", "Metal", "Ritual", "Space", "Voodoo", "Travel", "Demi-God", "Patron", "Tattoo", "Item Enhancement", "Temperament", "Kinetic", "Smoke", "Fire", "Rock", "Sand", "Water", "Ice", "Wind", "Lightning", "Poison", "Petrifying", "Memory", "Glass", "Paper and Origami", "Touch", "Taste", "Sound", "Mind", "Shamanistic", "Enraging", "Horror", "Humor", "Manipulation", "Knight", "Royalty", "Survival", "Hunger", "Mercantile", "Money", "Materials", "Druidic", "Tailoring", "Gemstone", "Runic", "Locks", "Beast Mastery",, "Discipline", "Insight", "Monsterous", "Doppleganger", "Ooze", "Mimic", "Construct", "Firearm", "Demon Hunter", "Giant", "Undeath", "Sentience", "Awakening", "Lycanthropic", "Vampiric", "Creation", "Wood", "Support", "Flight", "Burrowing", "Swimming", "Fighting", "Bug", "Pathogenic", "Titan", "Mastermind", "Forsaken", "Nomadic", "Mutagenic", "Gravity", "Growth", "Farming", "Hunter-Gatherer", "Balance", "Artifice"
    ]
    let rook= [
        /*0- materials*/
        [
            "Primarily made of sturdy stone, with a few metal reinforcements.",
            "Built mostly from weathered stones, accentuated with gleaming metal elements.",
            "A solid structure crafted from ancient stones and adorned with precious gemstone inlays.",
            "A magnificent creation constructed from a blend of polished stone and robust metal components.",
            "A formidable creature composed of interlocking stones, fortified by durable metal joints.",
            "Mainly hewn from rough-hewn stones, complemented by ornate metal carvings and accents.",
            "A majestic being constructed with massive stone blocks, punctuated by elegant metalwork.",
            "A resilient entity crafted with a mixture of aged stone and resilient metals for added strength.",
            "An imposing figure crafted entirely from interwoven stone and molten metal, creating a unique fusion.",
            "A marvel of architecture fashioned from a combination of ancient stones and precious metals.",
            "An enigmatic colossus constructed from a harmonious blend of ancient stones and shimmering metals.",
            "A grand edifice assembled with massive stone slabs and glistening metal adornments.",
            "A magnificent amalgamation of rugged stone surfaces and intricate metallic embellishments.",
            "A formidable behemoth crafted from a seamless fusion of polished stones and gleaming alloys.",
            "A towering monolith comprised of massive stone blocks with subtle accents of gleaming metal.",
            "A resolute guardian built with a mix of fortified stone and reinforced metal for maximum durability.",
            "An awe-inspiring construct that marries the elegance of sculpted stone with the resilience of forged metal.",
            "A striking creature fashioned from interlocking stones and exquisite metallic filigree.",
            "A legendary titan forged from time-worn stones and augmented by enchanted metallic engravings.",
            "An enduring colossus melding the solidity of stone with the strength of finely-crafted metal joints.",
            "A monumental masterpiece, its foundation laid with enduring stone and its spires adorned with precious metals.",
            "A living fortress hewn from ancient stone and accentuated by shimmering metallic accents.",
            "A formidable structure crafted from immense stones, laced with veins of molten metal.",
            "A sight to behold, with its rugged stone exterior complemented by metallic symbols of ancient power.",
            "A towering marvel, composed of massive stone slabs and intricately crafted metal ornamentation.",
            "A stoic entity, its stone surface adorned with glistening metals to channel its mystic energy.",
            "A breathtaking work of art, its stone-and-metal composition standing tall against the test of time.",
            "A majestic titan, its stone core encased in intricately interlocking metal plates.",
            "An architectural wonder, a seamless fusion of hand-carved stone and precision-crafted metal components.",
            "A marvel of engineering, its stone foundation overlaid with a network of shimmering metallic veins.",
        ],
        /*1- arcitecture*/
        [
            "Massive crenellated battlements that crown its towering form, providing both defense and an imposing visage.",
            "Elegant flying buttresses that arc gracefully from its sides, lending support and grandeur to its structure.",
            "Numerous watchtowers and spires that rise like sentinels, offering a commanding view of the surrounding landscape.",
            "Gothic-style pointed arches that adorn its entrances and windows, giving it an air of timeless elegance.",
            "A labyrinth of hidden passages and secret chambers within its walls, reminiscent of a medieval fortress.",
            "Impressive machicolations projecting from its parapets, designed to repel attackers with boiling oil or projectiles.",
            "Ornate stained glass windows that glow like jewels, adding a touch of artistry to its formidable presence.",
            "Gargoyles and grotesques perched along its ledges, serving as both decorative features and guardians.",
            "Stately colonnades and arcades that grace its courtyards, creating an aura of grandiosity and sophistication.",
            "An imposing portcullis at its entrance, evoking the idea of an impenetrable stronghold.",
            "A majestic keep rising from its center, symbolizing strength and resilience.",
            "Bridges and walkways connecting different sections of the rook, creating an intricate network of pathways.",
            "Tall minarets and turrets that reach for the sky, adding an element of verticality to its design.",
            "Decorative merlons and embrasures along its parapets, reflecting a blend of aesthetics and defense.",
            "An awe-inspiring drawbridge that can be lowered to allow passage and raised to safeguard against threats.",
            "Enchanting water features like fountains and moats surrounding its base, lending a touch of serenity to its might.",
            "Stylish balustrades and railings lining its terraces, adding an element of refinement to its appearance.",
            "Mysterious catacombs and crypts hidden beneath its surface, hinting at a history steeped in legends.",
            "Charming dormer windows and rooftop gardens that soften the sternness of its stone facade.",
            "Elaborate cornices and friezes adorned with intricate carvings, telling tales of ancient heroes and mythical creatures.",
            "A majestic clock tower rising from its core, keeping time and announcing its presence to all who behold it.",
            "Elongated flying arches that create a sense of graceful movement, as if the rook is in perpetual motion.",
            "A series of grand balconies and terraces, offering breathtaking views of the surrounding landscapes.",
            "Ancient runes and symbols etched into its stone walls, imbuing it with a touch of mystical power.",
            "Mysterious trapdoors and hidden compartments that hold long-forgotten secrets and treasures.",
            "Eerie gargoyles that come to life and prowl its walls during the night, acting as guardians of the darkness.",
            "A majestic central dome or cupola, adding a touch of magnificence to its silhouette.",
            "Defensive arrow slits and gun loops that evoke the image of a fortress ready to withstand any assault.",
            "Exquisite sculptures and statues of legendary figures, commemorating heroes of old.",
            "A network of decorative spandrels and finials, adding an artistic flourish to its architecture.",
            "An imposing gatehouse complete with a formidable portcullis, welcoming visitors and deterring intruders.",
            "Enigmatic runic inscriptions that glow faintly with an otherworldly light, adding an aura of mystery.",
            "Tall chimneys and smokestacks billowing with magical smoke, hinting at unseen forces at work inside.",
            "Grand ceremonial halls and ballrooms, fit for regal gatherings and celebrations.",
            "High ramparts adorned with banners and flags, displaying the emblems of a noble lineage.",
            "A series of cascading waterfalls and aqueducts that channel water through its grounds, providing life to its surroundings.",
            "A majestic bell tower with resonating bells that echo across the land, marking significant moments.",
            "Elegant spiral staircases that wind their way through its interior, connecting different levels with grace.",
            "Ancient crypts and reliquaries holding sacred artifacts and powerful relics of bygone eras.",
            "Elaborate metalwork and wrought iron detailing that accentuates its stonework with finesse.",
            "A labyrinthine maze of passages and corridors within its walls, disorienting those who dare to explore.",
            "Decorative stained glass windows that scatter vibrant hues across its interiors when touched by sunlight.",
            "An observatory perched atop one of its towers, allowing it to gaze at the stars and ponder the cosmos.",
            "Intricate lattice screens and trellises that add an air of elegance and privacy to its inner sanctums.",
            "A colossal portico supported by massive columns, exuding an aura of strength and grandeur.",
            "A central courtyard adorned with an enchanting fountain, its waters shimmering with an otherworldly glow.",
            "A series of enchanted tapestries that come to life, narrating the rook's ancient history.",
            "Mysterious alchemical laboratories tucked away in hidden chambers, where arcane experiments take place.",
            "A weather vane perched high atop one of its spires, changing direction as if guided by a hidden intelligence.",
            "A network of underground catacombs, said to hold the resting places of legendary knights of old.",
            "Stunning frescoes and murals depicting mythical creatures and epic battles, adorning its walls.",
            "A breathtaking glass dome covering its grand hall, allowing celestial light to bathe the space within.",
            "A collection of ornate chandeliers hanging from its ceilings, illuminating its chambers with warm radiance.",
            "An elegant drawbridge spanning a deep moat, providing access to its fortified heart.",
            "An extensive library filled with ancient tomes and spellbooks, each containing forgotten knowledge.",
            "A system of majestic archways that lead from one wing to another, creating an air of regal splendor.",
            "A majestic amphitheater nestled within its walls, serving as a venue for grand performances and ceremonies.",
            "A series of powerful ballistae and catapults mounted on its ramparts, ready to defend against invaders.",
            "A magical observatory equipped with enchanted telescopes, allowing it to see far beyond the horizon.",
            "A divine shrine dedicated to celestial beings, where prayers echo through its hallowed halls.",
            "A collection of enchanted suits of armor standing guard in its corridors, as if possessed by a silent sentry."
        ],
        /*2- animatedElements*/
        [
            "The massive stone walls ripple and shift as if breathing, giving the impression of a living entity.",
            "The doors and gates creak open and shut on their own, responding to the presence of intruders or allies.",
            "Gargoyles and statues along its battlements animate, turning their heads to watch and track movements.",
            "The stone floors seem to undulate like waves, creating an eerie sensation of walking on a living surface.",
            "The rook's grand staircase spirals and changes its form, leading explorers to new locations within.",
            "Tapestries and banners sway gently in the absence of wind, as if brushed by an invisible hand.",
            "Ancient runes and carvings carved into its walls glow faintly, recounting forgotten tales of its past.",
            "The rook's watchtowers swivel and turn, as if scanning the horizon for potential threats.",
            "Peculiar whispering echoes through its halls, forming words and sentences in long-lost languages.",
            "Hidden passageways shift and reveal themselves, guiding curious souls deeper into its secrets.",
            "The rook's immense chains and drawbridge seem to extend and retract with a life of their own.",
            "Stone gargoyles detach from the walls and swoop down in silent surveillance of the rook grounds.",
            "Flickering torch sconces illuminate spontaneously, casting dancing shadows that seem to tell stories.",
            "The rook's stone ornaments reshape themselves, depicting different scenes and figures throughout the day.",
            "Animated suits of armor patrol the corridors, their presence both protective and unnerving.",
            "The rook's grand chandelier sways gracefully, its crystals emitting a soft, soothing glow.",
            "Living vines and foliage grow along its walls, intertwining with the stone in a harmonious embrace.",
            "Ornate wall carvings come to life, depicting historic events that play like moving paintings.",
            "The rook's stone gargoyles take flight, circling overhead with an imposing yet majestic aura.",
            "Enchanted stained glass windows depict animated scenes, showcasing tales of the rook's past.",
            "Mystical sigils etched into the floors glow brightly, illuminating hidden paths and chambers.",
            "The rook's stone defenses reconfigure themselves, creating new barriers and fortifications.",
            "Mysterious glowing eyes appear within the rook's dark recesses, watching and following intruders.",
            "The sound of distant battle cries and clashing swords echoes through its halls, despite no one being present.",
            "The rook's gates and drawbridge seem to welcome allies, lowering gently to grant safe passage.",
            "Stone creatures and mythical beasts emerge from the walls, surveying the surroundings with curiosity.",
            "The rook's massive portcullis rises and falls with purpose, seemingly guarding against unseen threats.",
            "Animated water features within the rook form intricate patterns, flowing gracefully along its interiors.",
            "Invisible ethereal music fills the air, accompanying visitors as they explore its grand chambers.",
            "The rook's grand library comes alive, with books flying off shelves and opening to desired pages.",
            "Mystical symbols on the floors shimmer with power, granting protection to those who walk upon them.",
            "The rook's towering spires sway and twist gently, as if reaching towards the heavens.",
            "The whispers of the rook's ancient inhabitants can be heard, sharing their wisdom and stories.",
            "Glowing orbs of light guide wanderers through its maze-like corridors, illuminating the way ahead.",
            "Animated chains and mechanisms rearrange the layout, leading adventurers to unexplored realms.",
            "The rook's grand clockwork ticks and chimes, keeping its own mysterious time.",
            "Paintings on the walls shift and change, depicting scenes from other worlds and dimensions.",
            "The rook's majestic banners billow and flutter, displaying insignias of its illustrious history.",
            "Living water fountains dance with elegance, forming mesmerizing patterns in the air.",
            "Animated suits of armor perform ceremonial movements, echoing a long-lost knightly order.",
            "The rook's massive bells ring out on their own, tolling for forgotten celebrations and tragedies.",
            "The rook's massive chandeliers sway gently, casting flickering shadows across the halls.",
            "Hidden passages and secret doorways open and close, revealing new paths throughout the rook.",
            "The stone gargoyles that adorn the rook's exterior come to life, watching over its domain with vigilance.",
            "Animated vines and foliage cover the rook walls, giving it an ancient and overgrown appearance.",
            "The rook's ancient stone runes glow with an otherworldly light, telling tales of forgotten times.",
            "The wind seems to whisper messages to those who dare to listen, carrying the secrets of the rook.",
            "Animated stained glass windows depict mesmerizing scenes that change with the shifting light.",
            "The rook's statues and sculptures move gracefully, performing a silent dance of stone.",
            "Living tapestries and banners unfurl, showcasing the rook's rich history and heroic deeds.",
            "The rook's moat ripples and moves, as if concealing mysterious creatures beneath its surface.",
            "Animated cogs and gears turn within the rook's walls, powering its enigmatic machinery.",
            "The sound of ghostly laughter and echoes of old celebrations fill the rook's grand ballroom.",
            "Animated elements of nature, such as rainbows and shimmering auroras, adorn the rook's sky-like ceilings.",
            "The rook's doors appear to breathe, opening and closing as if with a life of their own.",
            "Animated constellations swirl in the rook's observatory, guiding explorers through the night sky.",
            "The rook's grand organ plays haunting melodies, its keys moving without a musician's touch.",
            "Living sculptures of mythical creatures roam the rook grounds, guarding its secrets.",
            "The rook's clockwork mechanisms create intricate patterns of movement, like an elegant dance.",
            "Animated fireplaces cast a warm and welcoming glow, as if inviting visitors to stay awhile.",
        ],
        /*3- Defenses*/
        [
            "The rook can launch massive stone boulders from its towering battlements, crushing anything in their path.",
            "It shoots scorching streams of molten lava from hidden vents, turning invaders to ash.",
            "The rook's walls are equipped with powerful ballistae and catapults, raining down destruction upon its foes.",
            "It can summon swirling winds that knock back and disorient attackers, making them easy prey.",
            "The rook's exterior is laced with deadly spikes and razor-sharp blades, making climbing almost impossible.",
            "It can release torrents of boiling water or freezing ice from its gargoyles, depending on its mood.",
            "The rook's drawbridge doubles as a massive battering ram, smashing into enemies foolish enough to approach.",
            "It can create illusions and mirages, confusing and misleading those who seek to infiltrate its domain.",
            "The rook's floors are rigged with trapdoors and hidden pitfalls, ensnaring trespassers as they explore.",
            "It can release a blinding cloud of dust and debris, obscuring vision and disorienting attackers.",
            "The rook's gates are reinforced with enchanted barriers that repel and weaken incoming attacks.",
            "It can summon spectral knights and defenders to fight alongside it, protecting the rook's borders.",
            "The rook's statues come to life, wielding mighty weapons to defend their home from intruders.",
            "It can generate powerful energy shields, deflecting and absorbing incoming projectiles.",
            "The rook's interior is filled with deadly mazes and shifting walls, making navigation treacherous for invaders.",
            "It can call upon the elements to create thunderstorms, blizzards, or scorching heatwaves.",
            "The rook's central tower can rise and collapse, creating seismic shockwaves that topple enemies.",
            "It can release swarms of enchanted ravens or bats, attacking from all directions.",
            "The rook's gargoyles and stone guardians awaken to defend their master, attacking with surprising agility.",
            "It can activate ancient machinery that launches a barrage of fiery cannonballs at approaching threats.",
            "It can manipulate the terrain around it, causing the ground to shift and trap invaders.",
            "The rook's walls are enchanted to self-repair and reassemble after being damaged.",
            "It can unleash a deafening sonic blast, disorienting and stunning nearby enemies.",
            "The rook can channel powerful energy beams from its towers, obliterating anything in their path.",
            "It can create illusions of itself, confusing attackers and making it challenging to identify the real target.",
            "The rook's moat is filled with corrosive acid or venomous creatures, dissuading anyone from crossing it.",
            "It can release clouds of toxic gas or noxious fumes, choking and incapacitating intruders.",
            "The rook's gargoyles can detach and pursue intruders, carrying them away to unknown fates.",
            "It can activate magical force fields that repel physical and mystical attacks alike.",
            "The rook can manipulate gravity, making it difficult for attackers to move or stand upright.",
            "It can transform parts of its structure into living vines or thorny brambles, ensnaring trespassers.",
            "The rook's spires and turrets can retract or extend, reaching out to grab and crush intruders.",
            "It can release swarms of enchanted insects or vermin, causing panic and distraction.",
            "The rook can create mirages and illusions of its surroundings, disorienting attackers.",
            "It can call upon ancient spirits or elemental beings to aid in its defense.",
            "The rook's walls are fortified with enchanted runes that deflect and weaken magical attacks.",
            "It can release a powerful shockwave that knocks back and disorients nearby enemies.",
            "The rook's exterior can shift and morph, creating new pathways while sealing off others.",
            "It can generate blinding flashes of light or darkness, impairing vision and causing confusion.",
            "The rook can merge with its surroundings, becoming nearly invisible to those seeking it.",
            "It can summon powerful elemental storms, such as lightning strikes or tornadoes, to repel attackers.",
            "The rook's interior is filled with shifting mazes and labyrinthine corridors, disorienting intruders.",
            "It can unleash a barrage of magical projectiles, seeking out and homing in on its targets.",
            "The rook can manipulate time within its walls, aging or rejuvenating anyone who enters.",
            "It can project terrifying illusions of legendary creatures or nightmarish visions, paralyzing fear in intruders.",
            "The rook's architecture can rearrange itself into different configurations, catching invaders by surprise.",
            "It can release a noxious fog or mist that weakens and incapacitates those who breathe it.",
            "The rook can create pocket dimensions or portals, transporting attackers to other realms.",
            "It can generate powerful seismic tremors, causing the ground to shake and crumble beneath intruders.",
            "The rook's statues and gargoyles can come to life, attacking invaders with stone fists.",
            "It can release a swarm of enchanted projectiles, such as fiery boulders or icy shards, to ward off enemies.",
            "The rook can drain energy or life force from nearby beings, weakening and exhausting them.",
            "It can project force fields that distort reality, making it difficult for attackers to perceive their surroundings.",
            "The rook's exterior can become superheated or freezing cold, discouraging intruders from getting close.",
            "It can manipulate the elements of the environment, such as creating quicksand or raising water levels.",
            "The rook can unleash a powerful roar or sonic blast that disorients and incapacitates intruders.",
            "It can control the weather around it, summoning thunderstorms, blizzards, or intense heat.",
            "The rook's windows can transform into glowing eyes that shoot powerful beams at intruders.",
            "It can deploy an army of animated stone soldiers or golems to defend its grounds.",
            "The rook can project an impenetrable aura that repels all attacks and spells."
        ],
        /*4- Rook Components */
        [
            "The rook's massive head serves as the main watchtower, scanning the surroundings for intruders.",
            "Powerful stone arms extend from the walls, ready to strike at enemies and crush obstacles.",
            "Glowing eyes atop the rook's towers act as the surveillance system.",
            "The rook's battlements are adorned with crenellations and embrasures, providing both aesthetics and defense.",
            "Graceful wings are integrated into the structure, adding a touch of majesty to the rook's appearance.",
            "Intricate engravings and ancient symbols decorate the rook's exterior, enhancing its mystical aura.",
            "Turrets and spires rise like spears from the rook's silhouette, adding to its imposing presence.",
            "Massive stone torsos serve as additional guard towers and defense points.",
            "The rook's entrance features a grand portcullis designed to resemble a formidable beak.",
            "Mechanisms integrated into the rook's interior animate walls and create moving barriers.",
            "An ancient heartstone powers the rook's core, providing life to the entire structure.",
            "Gargoyles line the walls, acting as both ornamentation and functional drainage spouts.",
            "A drawbridge fashioned as a massive arm, capable of smashing obstacles and foes.",
            "Guardian statues stand at the rook's perimeters, ready to defend against potential threats.",
            "The throne room features a magnificent seat symbolizing the ruler's power and dominance.",
            "Cores are scattered throughout the structure, channeling ancient magic to fortify its defenses.",
            "Layered stone plates cover the rook's exterior, reminiscent of formidable armor.",
            "Banners and pennants flutter from the rook's ramparts, displaying its symbolic colors.",
            "The rook's form incorporates stone claws that extend menacingly from its walls.",
            "A network of underground tunnels and secret passages provides hidden escape routes.",
            "Ancient glyphs and runes etched into the stone surface hum with mystical energy.",
            "Huge stone gears and mechanisms whir and clank, animating the rook's movements.",
            "A majestic stone crown adorns the highest tower, symbolizing its dominion over the land.",
            "The rook's windows are designed as piercing eyes, seemingly watching all who approach.",
            "In times of danger, massive stone wings unfurl, granting the rook the ability to soar above.",
            "The rook's main gate is a massive, menacing mouth, ready to devour intruders.",
            "The stone walls are reinforced with gleaming metal bands, adding to its formidable defense.",
            "A central courtyard features a grand stone chessboard, evoking its chess piece inspiration.",
            "The rook's foundation is built from ancient, enchanted stone, resilient to attacks.",
            "Glowing crystals embedded in the walls channel magical energy, empowering its defenses.",
            "The interior chambers are vast, with stone columns resembling the rook's legs.",
            "Stone lanterns along the paths emit an eerie, ethereal glow, guiding the way at night.",
            "The rook's main keep is shaped like a fearsome stone beak, a symbol of its power.",
            "Horns and trumpets fashioned from stone emit haunting sounds during alarms.",
            "The rook's ramparts feature retractable stone spikes, deterring any attempts to scale them.",
            "Massive stone banners hang from the walls, displaying the rook's heraldry.",
            "In the heart of the rook, an ancient golem-like entity fuels its life force.",
            "Enchanted stone talismans are scattered throughout, amplifying the rook's magic.",
        ],
        /*5- Magic Descriptions*/
        [
            "Scientific: The rook's attacks are infused with advanced scientific knowledge, allowing it to manipulate matter and energy with deadly precision.",
            "Artisan: Each strike of the rook is a masterpiece, crafted with exceptional craftsmanship and artistry, leaving devastating impacts on its foes.",
            "Arcane: Arcane energies surge through the rook's attacks, unleashing mysterious and esoteric powers that defy conventional defenses.",
            "Natural: The rook channels the forces of nature into its attacks, commanding the elements and living creatures to strike with primal fury.",
            "Legendary: Legends come alive as the rook's attacks embody the awe-inspiring powers of mythical tales, leaving foes in disbelief.",
            "Forbidden: Dark and forbidden energies empower the rook's attacks, unleashing sinister and dangerous forces upon its enemies.",
            "Dimensional: The rook manipulates space and reality with each strike, bending and distorting the battlefield to its advantage.",
            "Light: Radiant light accompanies the rook's attacks, blinding and burning its foes with divine intensity.",
            "Shadow: From the darkness, the rook's attacks emerge, striking with stealth and penetrating the defenses of its enemies.",
            "Time: The rook warps time to accelerate its strikes or slow down its opponents, gaining an edge in combat with temporal manipulation.",
            "Chaos: Chaos fuels the rook's attacks, causing unpredictable and unstable effects, throwing its enemies into disarray.",
            "Illusion: The rook weaves illusions into its attacks, confusing and deceiving its foes, leaving them vulnerable to its strikes.",
            "Stealth: The rook's attacks strike from the shadows, taking its enemies by surprise and vanishing before retaliation.",
            "Enchanting: The rook's attacks are imbued with enchanting magic, captivating its foes and making them susceptible to its will.",
            "Technomancy: Advanced technology powers the rook's attacks, unleashing mechanized onslaughts that defy conventional warfare.",
            "Emotion: The rook's attacks evoke powerful emotions in its enemies, manipulating their actions and leaving them vulnerable to its strikes.",
            "Psychic: The rook's attacks target the minds of its enemies, inflicting psychic trauma and confusion with every strike.",
            "Dream: With dream magic, the rook's attacks infiltrate the minds of its foes, turning their own dreams into nightmarish reality.",
            "Necromancy: The rook summons the powers of death to its attacks, draining life and raising undead to fight on its behalf.",
            "Music and Song: The rook's attacks are accompanied by mystical music and haunting songs, affecting the emotions and willpower of its foes.",
            "Mirror: Mirror magic reflects the attacks of its enemies, turning their own strikes against them with uncanny precision.",
            "Word: The rook's commanding words carry magical power, compelling its enemies to obey or suffer dire consequences.",
            "Hex: The rook's attacks place malevolent hexes on its foes, causing misfortune and bad luck with every strike.",
            "Void: The rook manipulates the void, conjuring and harnessing the power of nothingness to annihilate its enemies.",
            "Bloodline: The rook's attacks draw strength from its ancient inhabitant's bloodline, empowering it with the abilities of its ancestors.",
            "Blood: Blood magic infuses the rook's attacks, making them more potent but at a cost of bodies already captured inside.",
            "Corruption: Corruption magic taints the rook's enemies with each strike, weakening them from within and leaving them vulnerable to further attacks.",
            "Alchemy: The rook's attacks utilize alchemical concoctions, unleashing potent elixirs and explosives on its foes.",
            "Plant: With plant magic, the rook commands the flora to ensnare and crush its enemies with natural fury.",
            "Animal: The rook's attacks harness the power of animals, summoning and commanding creatures to fight alongside it.",
            "Transformation: The rook's attacks shape-shift and transform, making each strike unpredictable and versatile in combat.",
            "Destruction: Destruction magic empowers the rook's attacks with raw force, causing devastation and obliteration upon impact.",
            "Alteration: Alteration magic changes the properties of its attacks, making them more versatile and adaptive to different situations.",
            "Healing: The rook's attacks possess healing properties, allowing it to mend its wounds and those of its allies in the midst of battle.",
            "Crystal: Crystal magic enhances the rook's attacks with the power of mystical crystals, creating explosive and dazzling impacts.",
            "Sight: Sight magic enhances the rook's vision, allowing it to see through illusions and strike its enemies with uncanny accuracy.",
            "Bone: The rook's attacks wield the power of bones, using them as deadly projectiles and weapons.",
            "Dragon: The rook's attacks emulate the might of dragons, breathing fire and unleashing draconic fury on its enemies.",
            "Divine: Divine magic fuels the rook's attacks, allowing it to wield holy powers and smite its enemies with celestial strength.",
            "Defensive: Defensive magic shields the rook from harm, allowing it to absorb and deflect attacks with resilience.",
            "Absorption: Absorption magic lets the rook absorb and redirect the energies of its enemies, converting them into its own power.",
            "Battlefield: The rook's attacks are attuned to the battlefield, allowing it to manipulate the terrain and gain strategic advantages.",
            "Aura: The rook exudes a powerful aura that affects those around it, bolstering allies and intimidating enemies.",
            "Banishment: Banishment magic banishes foes to other planes or dimensions, removing them from the battlefield.",
            "Divination: The rook's attacks provide glimpses of the future, allowing it to anticipate its enemies' actions and plan its own strikes.",
            "Physical: Physical magic enhances the rook's physical attributes, making it stronger, faster, and more agile in battle.",
            "Spirit: Spirit magic connects the rook to the spirit realm, enabling it to commune with spirits and use their powers in combat.",
            "Fey: The rook's attacks are infused with the magic of the fae, beguiling and enchanting its enemies.",
            "Wish: Wish magic grants the rook the ability to make wishes come true, altering reality with its attacks but at a great cost.",
            "Order: With order magic, the rook brings structure and organization to the chaos of battle, gaining tactical advantage.",
            "Sealing: Sealing magic allows the rook to seal away enemies' powers and abilities, rendering them powerless.",
            "Summoning: The rook can summon and command powerful beings with summoning magic, bolstering its forces in battle.",
            "Dance: Dance magic infuses the rook's movements with mystical choreography, creating mesmerizing effects on its enemies.",
            "Love: With love magic, the rook can invoke feelings of love and pacify its enemies, making them less prone to violence.",
            "Sacrifice: Sacrifice magic allows the rook to offer sacrifices for greater power, increasing the potency of its attacks.",
            "Infernal: Infernal magic channels dark powers from the underworld, allowing the rook to unleash demonic forces on its enemies.",
            "Culinary: Culinary magic uses the power of food and cooking to heal and strengthen the rook in the heat of battle.",
            "Luck: Luck magic manipulates chance and probability, granting the rook a fortunate advantage in combat.",
            "Wild: Wild magic is unpredictable and untamed, causing chaotic and random effects in the rook's attacks.",
            "Death: Death magic brings the power of mortality and decay, inflicting harm and weakening its enemies.",
            "Life: The rook's attacks possess life-giving properties, healing and revitalizing both itself and its allies.",
            "Mycomancy: Mycomancy allows the rook to control and manipulate fungi and mushrooms to create various effects in combat.",
            "Cataclysmic: Cataclysmic magic triggers apocalyptic events and disasters, unleashing devastation on the battlefield.",
            "Weather: The rook's attacks manipulate the weather, creating storms and natural disasters to disrupt and harm its enemies.",
            "Geo-Shaper: Geo-Shaper magic allows the rook to shape and manipulate the earth, altering the terrain to its advantage.",
            "Metal: Metal magic strengthens the rook's attacks with metallic properties, making them more potent and resilient.",
            "Ritual: The rook's attacks draw power from ancient rituals, invoking magical energies with ceremonial precision.",
            "Space: Space magic grants the rook control over spatial dimensions, warping and distorting the battlefield.",
            "Voodoo: The rook's attacks utilize voodoo magic, causing spiritual harm and curses on its enemies.",
            "Travel: Travel magic enables the rook to move swiftly and traverse great distances, appearing in unexpected places on the battlefield.",
            "Demi-God: The rook embodies demi-god powers, commanding forces beyond the scope of mortal comprehension in its attacks.",
            "Patron: Patron magic calls upon the favor of powerful patrons or deities, lending their power to the rook's attacks.",
            "Tattoo: Tattoo magic infuses the rook's body with enchanted tattoos via tapestries that grant it various mystical abilities in combat.",
            "Item Enhancement: The rook enchants its weaponry and armor with magical properties, making its attacks more formidable.",
            "Temperament: The rook's attacks influence the emeies temperament, causing inbalance in battle.",
            "Kinetic: Kinetic magic channels kinetic energy into the rook's attacks, increasing their impact and velocity.",
            "Smoke: The rook's attacks release thick smoke, obscuring vision and providing cover for strategic maneuvers.",
            "Fire: With fire magic, the rook's attacks unleash flames that scorch and incinerate its foes.",
            "Rock: The rook's attacks wield the power of solid rock, crushing and pulverizing its enemies with earthen force.",
            "Sand: Sand magic manipulates sand and dust, creating abrasive and choking attacks against its foes.",
            "Water: The rook's attacks control the flow of water, unleashing powerful torrents and floods upon its enemies.",
            "Ice: With ice magic, the rook's attacks freeze and immobilize its foes, leaving them vulnerable to shattering strikes.",
            "Wind: Wind magic grants the rook control over the air, creating gusts and cyclones that buffet and disorient its enemies.",
            "Lightning: The rook's attacks harness the power of lightning, delivering electrifying and shocking assaults.",
            "Poison: Poison magic infuses the rook's attacks, causing venomous harm and debilitating effects on its enemies.",
            "Petrifying: The rook's attacks have a petrifying effect, turning its foes to stone upon contact.",
            "Memory: Memory magic manipulates the memories of its enemies, causing confusion and disorientation in combat.",
            "Glass: The rook's attacks use glass shards, piercing and shattering upon impact.",
            "Paper and Origami: Paper and origami magic conjure origami creations and paper constructs, surprising and confounding its foes.",
            "Touch: Touch magic affects its enemies upon physical contact, inflicting various effects and curses.",
            "Taste: Taste magic alters the taste of its enemies' senses, causing nausea or luring them into traps.",
            "Sound: The rook's attacks are accompanied by powerful soundwaves, causing sonic damage and disorientation.",
            "Mind: Mind magic manipulates the thoughts and emotions of its enemies, controlling their actions in battle.",
            "Shamanistic: The rook employs shamanistic magic, communicating with spirits and invoking their powers in its attacks.",
            "Enraging: Enraging magic incites rage and fury in its enemies, causing them to lose focus and attack recklessly.",
            "Horror: The rook's attacks invoke terror and horror, instilling fear and panic in its foes.",
            "Humor: Humor magic causes hysterical laughter, catching its enemies off guard or distracting them in battle.",
            "Manipulation: The rook's attacks manipulate the battlefield and enemy movements, controlling the flow of the fight.",
            "Knight: Knight magic imbues the rook with chivalrous valor and honor, inspiring loyalty and bravery in allies.",
            "Royalty: The rook's attacks exude an aura of royalty, commanding respect and awe in its foes.",
            "Survival: Survival magic ensures the rook's survival, enabling it to endure and recover from severe injuries.",
            "Hunger: The rook's attacks instill hunger and weakness in its enemies, sapping their strength and resolve.",
            "Mercantile: Mercantile magic influences trade and bargaining, potentially pacifying its enemies or enhancing its own fortune.",
            "Money: The rook's attacks involve the use of currency and wealth, causing material damage and financial consequences.",
            "Materials: Materials magic manipulates various materials to form powerful constructs and weapons in its attacks.",
            "Druidic: The rook channels druidic powers, connecting with nature and its elements to aid in its attacks.",
            "Tailoring: Tailoring magic allows the rook to weave fabric and clothing into versatile tools and weapons for combat.",
            "Gemstone: The rook's attacks are infused with gemstone magic, creating sparkling projectiles and dazzling impacts.",
            "Runic: Runic magic inscribes powerful runes into the rook's attacks, augmenting them with ancient powers.",
            "Locks: The rook's attacks can magically seal or unlock barriers and doors, controlling the battlefield's access points.",
            "Beast Mastery: The rook's attacks command and control wild beasts, utilizing them to fight alongside it in battle.",
            "Discipline: Discipline magic instills discipline and order into the rook's attacks, ensuring precise and controlled strikes.",
            "Insight: The rook's attacks grant insight and foresight into its enemies' actions, anticipating and countering their moves.",
            "Monstrous: Monstrous magic transforms the rook into somethign resembling a terrifying and fearsome creature, striking terror into its foes.",
            "Doppleganger: The rook can create illusory doppelgangers of itself, confusing and overwhelming its enemies.",
            "Ooze: Ooze magic allows the rook to transform launch and control gelatinous oozes, absorbing and engulfing its enemies.",
            "Mimic: The rook can mimic the abilities and attacks of its foes, turning their own strengths against them.",
            "Construct: Construct magic empowers the rook to form constructs and golems, summoning obedient minions to fight in its stead.",
            "Firearm: The rook's attacks utilize magical firearms and artillery, delivering explosive and ranged firepower on the battlefield.",
            "Demon Hunter: The rook becomes a demon hunter, gaining abilities and powers to combat demonic adversaries.",
            "Giant: Giant magic enlarges the rook, granting immense strength and causing massive destruction with its attacks.",
            "Undeath: The rook draws power from undeath, transforming its attacks into necrotic forces that drain life from its enemies.",
            "Sentience: The rook's attacks carry sentience and intelligence, adapting to its enemies' actions and countering with strategic strikes.",
            "Awakening: Awakening magic awakens dormant powers and abilities within the rook, unleashing newfound potential in combat.",
            "Lycanthropic: Lycanthropic magic allows the rook to transform into different beast-liek shapes, gaining animalistic abilities in battle.",
            "Vampiric: The rook's attacks feed on the life force of its enemies, replenishing its own strength with each strike.",
            "Creation: Creation magic manifests matter from thin air, creating objects and elements for versatile attacks.",
            "Wood: The rook's attacks manipulate wood and plant life, using it as a flexible and resilient weapon.",
            "Support: Support magic aids and heals its allies, bolstering them for battle and enhancing their capabilities.",
            "Flight: Flight magic grants the rook the ability to soar above the battlefield, launching aerial assaults on its enemies.",
            "Burrowing: The rook can burrow underground, surprising its enemies with sneak attacks from beneath.",
            "Swimming: Swimming magic enables the rook to move effortlessly underwater, launching amphibious strikes on its foes.",
            "Fighting: The rook's attacks embody the essence of fighting prowess, combining martial skills with magical precision.",
            "Bug: Bug magic summons swarms of insects and bugs, pestering and weakening its enemies with insectile assaults.",
            "Pathogenic: Pathogenic magic infects its enemies, causing diseases and weakening their physical abilities.",
            "Titan: The rook becomes a titan, towering over its foes and unleashing colossal attacks with tremendous power.",
            "Mastermind: The rook becomes a mastermind strategist, orchestrating cunning and coordinated attacks on its enemies.",
            "Forsaken: Forsaken magic saps the strength and life force of its enemies, leaving them weakened and vulnerable.",
            "Nomadic: Nomadic magic endows the rook with adaptability and versatility, utilizing diverse combat techniques from different cultures.",
            "Mutagenic: Mutagenic magic alters the rook's physical form, transforming it into a mutated being with extraordinary powers.",
            "Gravity: The rook manipulates gravity in its attacks, causing objects and enemies to be drawn or repelled with force.",
            "Growth: Growth magic enlarges the rook's attacks, causing them to expand and engulf its enemies.",
            "Farming: Farming magic cultivates powerful crops and vegetation, using them as weapons in combat.",
            "Hunter-Gatherer: The rook's attacks mimic the prowess of hunter-gatherers, utilizing resourcefulness and survival skills in battle.",
            "Balance: Balance magic maintains equilibrium in the rook's attacks, ensuring a harmonious combination of offensive and defensive maneuvers.",
            "Artifice: Artifice magic empowers the rook's attacks with intricate mechanisms and devices, creating ingenious and deadly contraptions."
        ],
        /*6- Roaming behaviors*/
        [
            "Clattering Sounds: The rook moves with loud and echoing clatters, announcing its presence from afar.",
            "Deliberate Strides: The rook takes slow and deliberate strides, each step shaking the ground beneath its colossal weight.",
            "Stone Dragging: As it moves, the rook's stone components may scrape and drag along the terrain, leaving marks in its wake.",
            "Gleaming Trail: The rook leaves behind a trail of faint glowing light as it roams, giving an otherworldly aura to its movements.",
            "Ghostly Glide: The rook appears to glide or float across the landscape, almost as if it defies gravity.",
            "Spectral Phasing: The rook's form intermittently phases in and out of the material plane as it moves, adding an eerie and elusive quality to its roaming.",
            "Rooted Movement: The rook appears rooted to the ground, with the land itself shifting and molding to accommodate its progress.",
            "Levitation: The rook levitates slightly above the ground as it moves, leaving no footprints and showing a supernatural grace.",
            "Emerging from the Earth: The rook emerges from the ground as it roams, appearing to rise from the very earth itself.",
            "Shadow Traces: As it moves, the rook leaves fleeting shadowy traces behind, as if the darkness itself follows its path.",
            "Echoing Echoes: The rook's movements are accompanied by echoing echoes, reverberating through the surroundings with each step.",
            "Cosmic Ripples: The rook's roaming leaves faint ripples in the air and space around it, like a cosmic disturbance.",
            "Thunderous Footfalls: The rook's heavy steps generate thunderous footfalls, shaking the landscape and startling all nearby.",
            "Floating Tendrils: Ethereal tendrils or wisps extend from the rook's body, gently caressing the terrain as it moves.",
            "Glowing Runes: Glowing runes appear on the ground beneath the rook as it roams, marking its mystical path.",
            "Celestial Traces: The rook's movements seem to draw constellations in the sky above, forming celestial patterns with its path.",
            "Temporal Displacement: The rook's roaming creates temporal displacements, causing strange fluctuations in time around it.",
            "Living Shadows: The rook's shadow seems to have a life of its own, moving independently as it roams.",
            "Crystal Echoes: Crystal fragments embedded in the rook's body resonate with a crystalline echo as it moves.",
            "Flickering Phantasm: The rook appears as a flickering phantasm, sometimes almost disappearing before materializing again.",
            "Veil of Invisibility: The rook becomes momentarily invisible as it moves, blending into its surroundings.",
            "Earthquake Tremors: The rook's roaming sends shockwaves through the ground, creating earthquake-like tremors in its wake.",
            "Aurora Traces: The rook leaves behind glowing aurora-like traces as it moves, lighting up the sky with vibrant colors.",
            "Wailing Whispers: Ghostly whispers or moans accompany the rook's movements, lending an eerie atmosphere to its roaming.",
            "Gusts of Wind: The rook's movement generates powerful gusts of wind, sweeping away objects and debris from its path.",
            "Ephemeral Apparition: The rook appears as an ephemeral apparition, flickering in and out of existence with its roaming.",
            "Radiant Emanation: The rook emanates radiant energy as it moves, illuminating the landscape with a brilliant glow.",
            "Chromatic Spectrum: The rook's body reflects a shifting spectrum of colors as it roams, creating a mesmerizing visual effect.",
            "Hallowed Ground: The rook leaves behind hallowed ground or sacred symbols where it treads, imbuing the area with mystical significance.",
            "Silent Strides: The rook moves with such stealth that its steps create no sound, allowing it to approach unnoticed.",
            "Time-Warping Trails: The rook's movement leaves behind time-warping trails, distorting the perception of time for those nearby.",
            "Ethereal Drift: The rook seems to drift ethereally across the landscape, as if untethered from the physical realm.",
            "Magnetic Attraction: The rook's roaming generates a magnetic field, affecting nearby objects and metal.",
            "Pulsating Heartbeat: The rook's movement is accompanied by a pulsating heartbeat sound, echoing through the surroundings.",
            "Crimson Embers: Crimson embers trail in the rook's wake, leaving a fiery aura behind its movements.",
            "Mystic Whirlpools: The rook's roaming creates mystic whirlpools in the air and ground, generating swirling energies.",
            "Thundering Roar: The rook releases a thundering roar as it moves, intimidating its foes and asserting its presence.",
            "Phantom Echoes: The rook's footsteps echo long after it has moved, giving an ethereal and haunting quality to its roaming.",
            "Invisible Threads: The rook's movement is guided by invisible threads or forces, almost as if it dances across the landscape.",
            "Eyes of Light: The rook's eyes emit beams of light, casting a radiant glow on its surroundings as it roams.",
            "Temporal Anomalies: The rook's roaming creates temporal anomalies, causing shifts and anomalies in the flow of time.",
            "Eternal Resonance: The rook's movements have an eternal resonance, leaving a lingering effect on the surrounding environment.",
            "Molten Wake: The rook's movement leaves behind a molten wake, as if its body radiates intense heat.",
            "Glowing Footprints: Glowing footprints appear on the ground behind the rook as it roams, marking its path.",
            "Phasing Veil: The rook seems to pass in and out of phase with reality, giving its roaming a ghostly quality.",
            "Penumbral Silhouette: The rook's silhouette appears penumbral, with its edges blurred and undefined as it moves.",
            "Living Incarnate: The rook's movement gives the impression of a living incarnate, embodying elemental and cosmic forces.",
            "Searing Aura: The rook emanates a searing aura as it moves, leaving a trail of scorching heat.",
            "Arcane Ripples: The rook's roaming creates ripples in arcane energy, distorting the magical fabric of the surrounding area.",
            "Transcendent Phasing: The rook's movement transcends physicality, phasing through obstacles and terrain with ease.",
            "Celestial Symphony: The rook's movement produces a celestial symphony, filling the air with ethereal music.",
            "Mystic Duality: The rook's roaming embodies a mystic duality, blending opposing elements and energies in harmony.",
            "Whispering Winds: The rook's movement stirs whispering winds, carrying cryptic messages through the air.",
            "Ghostly Afterimages: Ghostly afterimages trail behind the rook as it moves, leaving traces of its presence.",
            "Shimmering Mirage: The rook's form shimmers like a mirage as it roams, creating a hypnotic and elusive effect.",
            "Tectonic Shifts: The rook's roaming causes tectonic shifts, altering the landscape with its colossal presence.",
            "Celestial Confluence: The rook's movement aligns with celestial forces, channeling the power of the stars and planets.",
            "Timeless Cadence: The rook moves with a timeless cadence, seemingly unaffected by the flow of time.",
            "Energetic Emanations: The rook emanates bursts of energetic waves with each step, pulsating through the terrain.",
            "Living Thunderstorm: The rook's movement creates a living thunderstorm, with lightning crackling and thunder booming in its wake.",
            "Ethereal Threads: Ethereal threads trail from the rook's body as it roams, weaving through the landscape.",
            "Shifting Sands: The rook's movement stirs shifting sands, leaving behind patterns in the desert.",
            "Gravity Wells: The rook's roaming creates gravity wells, affecting nearby objects and beings with gravitational force.",
            "Astral Projection: The rook's form appears to astral project as it roams, with its spiritual presence drifting alongside its physical form.",
            "Living Hologram: The rook's roaming creates a living hologram, projecting spectral images around its body.",
            "Timeless Stasis: The rook's movement invokes a timeless stasis, seemingly frozen in time as it traverses the landscape."
        ],
        /*7- Interior Spaces*/
        [
        "Chambers of Wisdom: Within the rook's interior lie vast chambers filled with ancient knowledge and arcane secrets.",
        "Passage of Whispers: A network of passages where distant whispers seem to echo, hinting at hidden truths.",
        "Hidden Sanctuary: A secluded and well-concealed sanctuary within the rook, offering a sense of tranquility and safety.",
        "Labyrinthine Corridors: Endless twisting corridors that lead to various parts of the rook's interior, making it easy to get lost.",
        "Vault of Treasures: A grand vault containing valuable treasures and artifacts collected over centuries.",
        "Halls of Reflection: Halls adorned with reflective surfaces, creating a mesmerizing and disorienting effect.",
        "Mechanical Workshop: A workshop within the rook, filled with gears, levers, and mechanisms that keep it operational.",
        "Chamber of Relics: A special chamber dedicated to holding ancient relics and mementos from past ages.",
        "Enigmatic Observatory: An observatory where the rook can gaze upon the stars and study celestial phenomena.",
        "Theater of Illusions: An interior space designed for creating captivating and immersive illusions.",
        "The Chamber of Wonders: A chamber that houses mysterious and awe-inspiring artifacts from distant lands.",
        "Inner Sanctum: A deeply hidden and heavily protected chamber, serving as the rook's most sacred space.",
        "Library of Enchantment: A vast library containing tomes of magical knowledge and forgotten spells.",
        "Chamber of Echoes: A chamber where sounds and voices echo endlessly, creating a haunting ambiance.",
        "Garden of Serenity: An interior garden filled with lush foliage and calming natural beauty.",
        "Chamber of Time: A space that seems to exist outside of time, where past, present, and future intertwine.",
        "Arcane Laboratory: A laboratory equipped for conducting magical experiments and alchemical research.",
        "Theater of Memories: A chamber that allows one to relive memories and visions of the past.",
        "Hidden Armory: A well-guarded armory stocked with powerful weapons and ancient armaments.",
        "Chamber of Harmonies: A chamber filled with wondrous harmonies that resonate through the rook's structure.",
        "Chamber of Illusions: An interior space filled with mesmerizing and disorienting illusions.",
        "The Endless Gallery: A seemingly infinite gallery displaying artistic masterpieces and enigmatic artworks.",
        "Chamber of Echoes: A chamber where sounds and voices echo endlessly, creating a haunting ambiance.",
        "Theater of Shadows: A chamber where shadows seem to have a life of their own, dancing and moving with an eerie grace.",
        "Cryptic Passageways: Secret passageways leading to unknown destinations, concealed within the rook's structure.",
        "Chamber of Puzzles: A room filled with intricate puzzles and riddles that challenge the mind.",
        "Chamber of Celestial Maps: An area with detailed celestial maps, guiding the rook's navigation across the skies.",
        "Chamber of Timeless Artifacts: A chamber containing artifacts that seem to defy the passage of time.",
        "The Hidden Nexus: A central nexus within the rook, connecting and controlling its various functions.",
        "Chamber of Illusionary Projections: A room where illusionary projections can be displayed for various purposes.",
        "Chamber of Harmonies: A chamber filled with wondrous harmonies that resonate through the rook's structure.",
        "The Endless Gallery: A seemingly infinite gallery displaying artistic masterpieces and enigmatic artworks.",
        "Chamber of Echoes: A chamber where sounds and voices echo endlessly, creating a haunting ambiance.",
        "Theater of Shadows: A chamber where shadows seem to have a life of their own, dancing and moving with an eerie grace.",
        "Cryptic Passageways: Secret passageways leading to unknown destinations, concealed within the rook's structure.",
        "Chamber of Puzzles: A room filled with intricate puzzles and riddles that challenge the mind.",
        "Chamber of Celestial Maps: An area with detailed celestial maps, guiding the rook's navigation across the skies.",
        "Chamber of Timeless Artifacts: A chamber containing artifacts that seem to defy the passage of time.",
        "The Hidden Nexus: A central nexus within the rook, connecting and controlling its various functions.",
        "Chamber of Illusionary Projections: A room where illusionary projections can be displayed for various purposes.",
        "Chamber of Whispers: A chamber where cryptic whispers seem to emanate from the very walls.",
        "The Arcane Forge: A forge where elemental energies are harnessed to shape and strengthen the rook's structure.",
        "Chamber of Enigmatic Symbols: A room adorned with enigmatic symbols and runes, each holding hidden meanings.",
        "The Astral Observatory: An observatory focused on studying celestial phenomena and cosmic events.",
        "Chamber of Elemental Cores: A chamber containing the elemental cores that grant power to the rook's attacks.",
        "The Hall of Enigmas: A hall filled with enigmatic statues and puzzles that test the rook's visitors.",
        "Chamber of Prismatic Light: A room where prismatic light dances, creating a mesmerizing spectacle.",
        "The Oracle's Chamber: A chamber where the rook can receive cryptic visions of the future.",
        "Chamber of Harmonious Resonance: A space where harmonic resonances produce soothing and healing effects.",
        "The Gilded Vault: A vault filled with golden treasures and rare gems, symbolizing the rook's wealth and power.",
        "Chamber of Elemental Balance: A chamber that embodies the balance of elemental forces within the rook.",
        "The Celestial Terrace: A high terrace with an unobstructed view of the night sky and celestial bodies.",
        "Chamber of Perpetual Motion: A chamber where gears and mechanisms are in constant motion, keeping the rook alive.",
        "The Sanctuary of Silence: A serene sanctuary where peace and tranquility reign, shielding from outside disturbances.",
        "Chamber of Ethereal Portals: A room with ethereal portals that lead to other realms and dimensions.",
        "The Starlight Chamber: A chamber bathed in soft starlight, creating a peaceful and dreamlike atmosphere.",
        "Chamber of Timeless Wisdom: A chamber filled with ancient texts and scrolls containing boundless knowledge.",
        "The Mechanist's Workshop: A workshop where the rook's mechanisms are maintained and improved.",
        "Chamber of Celestial Energies: A chamber where celestial energies are harnessed to empower the rook's attacks.",
        "The Maze of Illusions: An illusionary maze within the rook's interior, disorienting and confounding intruders.",
        "Chamber of Elemental Fusion: A room where elemental forces merge and amplify the rook's powers.",
        "The Rook's Heart: A central chamber deep within the rook, serving as its core and life force.",
        "Chamber of Astral Projection: A space where astral projections can explore distant places and realms.",
        "The Vanishing Gallery: A gallery filled with paintings that seem to come to life, blurring the line between art and reality.",
        "Chamber of Time Weaving: A chamber where time itself is woven and manipulated to the rook's advantage.",
        "Chamber of Celestial Harmony: A chamber resonating with the harmony of celestial bodies and cosmic forces.",
        "The Engine Room: A room housing the powerful engine that keeps the rook animated and operational.",
        "Chamber of Elemental Amplification: A chamber that amplifies the rook's elemental powers to extraordinary levels.",
        "The Veiled Crypt: A crypt hidden within the rook, containing ancient secrets and forgotten memories.",
        "Chamber of Infinite Stars: A celestial observatory where stars seem to stretch into infinity.",
        "The Laboratory of Conjuration: A laboratory dedicated to summoning and controlling various entities.",
        "Chamber of Elemental Attunement: A room where the rook attunes itself to the elemental energies of the surroundings.",
        "The Nexus of Dimensions: A chamber where different dimensions converge, granting access to alternate realities.",
        "Chamber of Morphic Resonance: A space where the rook's form can adapt and change to suit various situations.",
        "The Aetheric Nexus: A nexus where aetheric energies flow, granting the rook mysterious and otherworldly abilities.",
        "Chamber of Elemental Integration: A chamber where elemental energies are integrated into the rook's very being.",
        "The Eternal Library: A vast library containing knowledge from the distant past and future.",
        "Chamber of Harmonic Dissonance: A chamber where harmonic dissonance creates disorienting effects on intruders.",
        "The Observatory of Souls: An observatory focused on studying the souls and spirits of living beings.",
        "Chamber of Elemental Resonance: A space where the rook resonates with the elemental forces of the world.",
        "The Ethereal Vault: A vault hidden within the rook, containing ethereal treasures from other realms.",
        "Chamber of Alchemical Synthesis: A room dedicated to the synthesis of powerful alchemical compounds.",
        "The Rook's Nexus: A central nexus where the rook's various powers and abilities converge.",
        "Chamber of Celestial Sights: A chamber with celestial sights, offering glimpses into the vast cosmos.",
        "The Chamber of Manifestations: A chamber where manifestations of thoughts and emotions take shape.",
        "Chamber of Elemental Mastery: A space where the rook achieves complete mastery over elemental forces.",
        "The Forgotten Archive: An archive filled with forgotten knowledge and forbidden secrets.",
        "Chamber of Astral Projection: A space where astral projections can explore distant places and realms.",
        "The Vanishing Gallery: A gallery filled with paintings that seem to come to life, blurring the line between art and reality.",
        "Chamber of Time Weaving: A chamber where time itself is woven and manipulated to the rook's advantage.",
        "Chamber of Celestial Harmony: A chamber resonating with the harmony of celestial bodies and cosmic forces.",
        "The Engine Room: A room housing the powerful engine that keeps the rook animated and operational.",
        "Chamber of Elemental Amplification: A chamber that amplifies the rook's elemental powers to extraordinary levels.",
        "The Veiled Crypt: A crypt hidden within the rook, containing ancient secrets and forgotten memories.",
        "Chamber of Infinite Stars: A celestial observatory where stars seem to stretch into infinity.",
        "The Laboratory of Conjuration: A laboratory dedicated to summoning and controlling various entities.",
        "Chamber of Elemental Attunement: A room where the rook attunes itself to the elemental energies of the surroundings.",
        "The Nexus of Dimensions: A chamber where different dimensions converge, granting access to alternate realities.",
        "Chamber of Morphic Resonance: A space where the rook's form can adapt and change to suit various situations.",
        "The Aetheric Nexus: A nexus where aetheric energies flow, granting the rook mysterious and otherworldly abilities.",
        "Chamber of Elemental Integration: A chamber where elemental energies are integrated into the rook's very being.",
        "The Eternal Library: A vast library containing knowledge from the distant past and future.",
        "Chamber of Harmonic Dissonance: A chamber where harmonic dissonance creates disorienting effects on intruders.",
        "The Observatory of Souls: An observatory focused on studying the souls and spirits of living beings.",
        "Chamber of Elemental Resonance: A space where the rook resonates with the elemental forces of the world.",
        "The Ethereal Vault: A vault hidden within the rook, containing ethereal treasures from other realms.",
        "Chamber of Alchemical Synthesis: A room dedicated to the synthesis of powerful alchemical compounds.",
        "The Rook's Nexus: A central nexus where the rook's various powers and abilities converge.",
        "Chamber of Celestial Sights: A chamber with celestial sights, offering glimpses into the vast cosmos.",
        "The Chamber of Manifestations: A chamber where manifestations of thoughts and emotions take shape.",
        "Chamber of Elemental Mastery: A space where the rook achieves complete mastery over elemental forces.",
        "The Forgotten Archive: An archive filled with forgotten knowledge and forbidden secrets."
        ],
        /*8- Menacing Visage*/
        [
        "Menacing Gargoyles: Gargoyles perched atop the rook's battlements, with stone expressions that strike fear into onlookers.",
        "Eyes of Unyielding Flame: Eyes that glow with an unyielding flame, revealing the rook's burning determination.",
        "Animated Carvings: Elaborate carvings that come to life, depicting scenes of battle and conquest.",
        "Visage of Ancient Kings: The face of ancient kings sculpted onto the rook's exterior, exuding an air of regal authority.",
        "Glowing Rune Patterns: Intricate rune patterns etched into the rook's surface, emitting an eerie glow.",
        "Formidable Watchtowers: Towering watchtowers with dark openings that seem to stare at all who approach.",
        "Living Ramparts: Ramparts that shift and move, creating an illusion of a living and breathing fortress.",
        "Eyes of Malevolence: Malevolent eyes that peer from the depths of arrow slits, unsettling those who catch a glimpse.",
        "Sinister Spikes: Sinister-looking spikes jutting out from the rook's walls, adding to its menacing aura.",
        "Animated Banners: Banners that move with a life of their own, displaying the rook's ancient symbols and emblems.",
        "Foreboding Arrowslits: Arrow slits that resemble dark, foreboding eyes, hinting at the rook's deadly capabilities.",
        "Glowing Glyphs: Glyphs carved into the rook's stonework that emit an otherworldly glow.",
        "Ominous Portcullis: An ominous portcullis with intricate patterns, giving the impression of a sinister grin.",
        "Haunting Engravings: Engravings of haunting scenes and ghostly figures that seem to come alive.",
        "Glowing Sigils: Glowing sigils etched into the rook's surface, amplifying its magical presence.",
        "Terrifying Turrets: Turrets that resemble menacing, open jaws, ready to unleash destruction.",
        "Veil of Darkness: A veil of darkness that shrouds the rook, making it seem like a harbinger of doom.",
        "Flickering Torches: Flickering torches illuminating the rook's walls, casting eerie shadows all around.",
        "Eerie Statues: Eerie statues of mythical creatures guarding the rook's entrances.",
        "Ancient Hieroglyphs: Ancient hieroglyphs telling tales of battles and conquests etched into the stone.",
        "Radiant Crest: A radiant crest emblazoned on the rook's facade, symbolizing its power and authority.",
        "Shadowy Overhangs: Shadowy overhangs that conceal mysterious secrets within the rook's depths.",
        "Glowing Mosaics: Glowing mosaics that depict cosmic scenes and celestial wonders.",
        "Dreadful Gates: Gates adorned with fearsome spikes, warning intruders of the rook's formidable defenses.",
        "Animated Chains: Chains that writhe and move on their own, creating an unsettling spectacle.",
        "Eyes of the Abyss: Eyes resembling deep, dark abysses that seem to draw people in.",
        "Stone Serpents: Serpentine sculptures slithering along the rook's walls, evoking feelings of unease.",
        "Grimacing Grotesques: Grotesque sculptures that contort their faces into sinister grimaces.",
        "Luminous Crest: A luminous crest glowing with mystical energies, revealing the rook's magical nature.",
        "Threatening Pinnacles: Pinnacles that rise like menacing spires, adding to the rook's imposing silhouette.",
        "Living Mural: A mural that appears to come to life, showing scenes of epic battles and mythical creatures.",
        "Fiery Sconces: Sconces that emanate flickering flames, casting an eerie light on the rook's exterior.",
        "Ominous Runes: Ominous runes etched into the rook's walls, carrying ancient, dark incantations.",
        "Glowing Arrowslits: Arrowslits that emit an eerie glow, making them look like eyes of the unknown.",
        "Foreboding Crest: A foreboding crest carved with sinister motifs, signifying the rook's ominous presence.",
        "Menacing Crenellations: Crenellations shaped like sinister grins, creating a foreboding appearance.",
        "Animated Gargoyles: Gargoyles with animated expressions, appearing to watch the surroundings vigilantly.",
        "Baleful Symbols: Baleful symbols etched into the rook's surface, emanating a sense of dark power.",
        "Glowing Portcullis: A portcullis glowing with mystic energy, guarding the rook's inner sanctum.",
        "Terrifying Spikes: Spikes that appear like monstrous teeth, warning intruders of the rook's danger.",
        "Cursed Inscriptions: Inscriptions carrying ancient curses, contributing to the rook's malevolent air.",
        "Eerie Tapestries: Tapestries that shift and move, depicting haunting scenes and spectral figures.",
        "Malevolent Eyes: Eyes carved into the stone, exuding a malevolent gaze that chills the heart.",
        "Haunting Carvings: Carvings of eerie figures and nightmarish creatures, evoking a sense of dread.",
        "Darkling Emblems: Emblems of dark entities and otherworldly beings that adorn the rook's surface.",
        "Radiating Glyphs: Glyphs that radiate with mystical energy, pulsating with arcane power.",
        "Spectral Flames: Ethereal flames that dance along the rook's walls, emitting an otherworldly glow.",
        "Macabre Crest: A crest with macabre symbols and imagery, representing the rook's ominous nature.",
        "Eldritch Carvings: Carvings depicting eldritch scenes and cosmic horrors, hinting at forbidden knowledge.",
        "Glowing Turrets: Turrets with a mesmerizing glow, exuding an aura of enchantment.",
        "Grim Portraits: Portraits of grim-faced rulers and ancient conquerors, intimidating intruders.",
        "Fearsome Crest: A crest featuring fierce creatures and symbols, instilling fear in those who see it.",
        "Ephemeral Wisps: Wisps of ephemeral light that flicker and vanish, giving the rook an otherworldly appearance.",
        "Mystical Runes: Mystical runes inscribed onto the rook's walls, imbued with magical energies.",
        "Silent Watchers: Sculptures of silent figures watching over the rook, adding an eerie atmosphere.",
        "Enigmatic Glimmer: An enigmatic glimmer that shimmers across the rook's surface, captivating onlookers.",
        "Stone Phantoms: Phantasmal figures seemingly made of stone, drifting along the rook's walls.",
        "Ethereal Symbols: Ethereal symbols glowing with an otherworldly luminescence, hinting at ancient secrets.",
        "Dreadful Crest: A crest evoking dread and unease, signifying the rook's menacing presence.",
        "Spectral Orbs: Spectral orbs hovering around the rook's exterior, emanating an eerie light.",
        "Menacing Battlements: Battlements lined with menacing features, resembling the maws of fierce beasts.",
        "Eldritch Carvings: Carvings of eldritch symbols and alien geometry, suggesting an arcane purpose.",
        "Glowing Portals: Glowing portals that seem to lead to other dimensions, adding an otherworldly aura.",
        "Cursed Engravings: Engravings carrying dark curses and malevolent spells, deterring intruders.",
        "Haunting Crest: A crest with haunting imagery, embodying the rook's enigmatic and ghostly presence.",
        "Sinister Sigils: Sinister sigils etched into the rook's surface, enhancing its magical potency.",
        "Luminous Arrowslits: Arrowslits that radiate a luminous glow, illuminating the rook's dark corridors.",
        "Ominous Gargoyles: Gargoyles with ominous expressions, watching over the rook's domain.",
        "Glowing Emblems: Emblems glowing with ethereal light, symbolizing the rook's magical essence.",
        "Malevolent Spikes: Spikes that seem to bristle with malevolence, adding to the rook's threatening appearance."
        ],
        /*9- Haunted Aura*/
        [
        "Chilling Mists: Mysterious mists that surround the rook, obscuring its form and sending shivers down the spine.",
        "Whispers of the Past: Eerie whispers that echo through the air, carrying tales of the rook's dark history.",
        "Ghastly Wails: Ghastly wails that emanate from the rook's depths, haunting the surrounding area.",
        "Haunted Shadows: Shadows that seem to move on their own, creating an unsettling and eerie presence.",
        "Cursed Aura: An aura of dark energy that surrounds the rook, evoking a sense of ancient curses.",
        "Spectral Presence: A spectral presence that lingers around the rook, giving it an otherworldly air.",
        "Enigmatic Fog: A dense, enigmatic fog that blankets the rook's surroundings, obscuring its intentions.",
        "Phantom Echoes: Echoes of long-lost battles and haunting memories that resonate within the rook.",
        "Supernatural Gloom: A supernatural gloom that envelopes the rook, casting a feeling of perpetual dusk.",
        "Ethereal Whispers: Ethereal whispers that only the bravest can hear, filling the air with unease.",
        "Ghostly Apparitions: Ghostly figures that flicker in and out of existence around the rook.",
        "Unearthly Presence: An unearthly presence that lingers in the vicinity, chilling those who come near.",
        "Spectral Shroud: A spectral shroud that seems to wrap itself around the rook's formidable form.",
        "Macabre Visions: Macabre visions that haunt the minds of those who approach the rook.",
        "Enchanted Mist: An enchanted mist that seems to have a life of its own, swirling around the rook.",
        "Cursed Whispers: Cursed whispers that echo through the air, foretelling doom for trespassers.",
        "Apparitions of the Past: Apparitions of bygone eras that manifest around the rook's battlements.",
        "Eerie Aura: An eerie aura that seems to pulse with dark energy, heightening the sense of foreboding.",
        "Mysterious Shroud: A mysterious shroud that veils the rook's intentions, leaving it an enigma.",
        "Haunted Ambience: A haunted ambience that permeates the area, filling it with a sense of dread.",
        "Phantasmal Fog: A phantasmal fog that twists and turns, taking on ghostly shapes around the rook.",
        "Chilling Presence: A chilling presence that freezes the air, leaving a feeling of perpetual cold.",
        "Spectral Gloom: A spectral gloom that shrouds the rook's surroundings, evoking a sense of the unknown.",
        "Grim Haunting: A grim haunting that lingers around the rook, unsettling all who approach.",
        "Mystic Enigma: A mystic enigma that surrounds the rook, making it a riddle to be unraveled.",
        "Sinister Whispers: Sinister whispers that seem to come from the very stone of the rook itself.",
        "Ghostly Presence: A ghostly presence that appears and vanishes, leaving an eerie impression.",
        "Ominous Fog: An ominous fog that creeps around the rook, concealing its secrets.",
        "Ethereal Vapors: Ethereal vapors that flow through the air, adding to the rook's mystique.",
        "Creeping Shadows: Shadows that crawl and creep along the rook's walls, like lurking specters.",
        "Enshrouded Mystery: An enshrouded mystery that surrounds the rook, beckoning the curious and the brave.",
        "Haunting Haze: A haunting haze that hangs in the air, making the rook feel like a place of lost souls.",
        "Spectral Aura: A spectral aura that glows with a pale light, casting an otherworldly glow.",
        "Grim Presence: A grim presence that permeates the surroundings, instilling a sense of unease.",
        "Mysterious Echoes: Mysterious echoes that resonate within the rook, as if the past reaches into the present.",
        "Ephemeral Spirits: Ephemeral spirits that dance around the rook, evoking a hauntingly beautiful sight.",
        "Chilling Mist: A chilling mist that rolls in with the rook, enveloping everything in an eerie haze.",
        "Supernatural Presence: A supernatural presence that seems to linger in the air, creating a sense of foreboding.",
        "Eerie Vortex: An eerie vortex of wind and mist that swirls around the rook, like a portal to another realm.",
        "Phantom Whispers: Phantom whispers that tickle the ears of those who dare to listen.",
        "Haunted Enigma: A haunted enigma that surrounds the rook, making it an enigmatic and eerie sight.",
        "Sinister Mists: Sinister mists that twist and coil, making it hard to see beyond the rook's silhouette.",
        "Ghostly Spectacle: A ghostly spectacle of light and shadow, creating an ethereal and haunting display.",
        "Cryptic Atmosphere: A cryptic atmosphere that envelops the rook, hiding its secrets in the mist.",
        "Spectral Veil: A spectral veil that seems to blur the lines between the rook and the spirit world.",
        "Enchanted Shroud: An enchanted shroud of mist that gives the rook an air of enchantment.",
        "Macabre Presence: A macabre presence that seems to loom over the rook's surroundings.",
        "Ethereal Mystery: An ethereal mystery that surrounds the rook, calling out to those who seek answers.",
        "Cursed Aura: A cursed aura that emanates from the rook, making it feel like a place of ill fortune.",
        "Apparitional Haze: An apparitional haze that veils the rook's form, making it appear ghostly and insubstantial.",
        "Chill of the Unknown: A chilling sensation that creeps up the spine of anyone who enters the rook's domain.",
        "Phantasmal Presence: A phantasmal presence that seems to linger even after the rook has passed.",
        "Eerie Enchantment: An eerie enchantment that pervades the area around the rook, bewitching all who draw near.",
        "Spectral Embrace: A spectral embrace that seems to reach out from the rook's walls, beckoning visitors inside.",
        "Ghastly Glow: A ghastly glow that emanates from the rook's depths, casting haunting shadows.",
        "Haunted Murmurs: Haunting murmurs that seem to echo through the rook's chambers, telling forgotten tales.",
        "Mysterious Phantoms: Mysterious phantoms that appear fleetingly, leaving a sense of unseen entities.",
        "Enigmatic Presence: An enigmatic presence that leaves those who encounter it with more questions than answers.",
        "Sinister Shroud: A sinister shroud that cloaks the rook in darkness, like a specter lurking in the night.",
        "Ghostly Whispers: Ghostly whispers that seem to come from the very stone of the rook, telling ancient secrets.",
        "Ominous Aura: An ominous aura that hovers around the rook, forewarning of danger and mystery.",
        "Ethereal Shadows: Ethereal shadows that dance along the rook's walls, making it appear alive with unseen movements.",
        "Chilling Presence: A chilling presence that fills the air, making it feel as if the rook is watching.",
        "Supernatural Fog: A supernatural fog that hangs heavily around the rook, creating an otherworldly atmosphere.",
        "Ephemeral Echoes: Ephemeral echoes that seem to reverberate through the rook, as if the past has come to life.",
        "Spectral Phenomenon: A spectral phenomenon that defies explanation, making the rook an enigma.",
        "Grim Enigma: A grim enigma that shrouds the rook, hinting at ancient mysteries and secrets.",
        "Mysterious Shivers: Mysterious shivers that run down the spine of those who come close to the rook.",
        "Haunted Vortex: A haunted vortex of mist and darkness that surrounds the rook, like a portal to the unknown.",
        "Phantom Presence: A phantom presence that lingers long after the rook has passed by, haunting the area.",
        "Eerie Aura: An eerie aura that envelops the rook, making it feel like a place of restless spirits.",
        "Cryptic Whispers: Cryptic whispers that echo through the rook's chambers, hinting at forgotten truths.",
        "Spectral Mystery: A spectral mystery that surrounds the rook, drawing curious souls into its embrace.",
        "Enchanted Spectacle: An enchanted spectacle of light and shadow that dances across the rook's surface.",
        "Macabre Atmosphere: A macabre atmosphere that clings to the rook, leaving a sense of foreboding.",
        "Ethereal Veil: An ethereal veil that seems to blur the lines between the rook and the ethereal plane.",
        "Cursed Haunting: A cursed haunting that fills the rook's halls, making it seem like a place of tragedy.",
        "Apparitional Whispers: Apparitional whispers that seem to speak directly to the hearts of those who listen.",
        "Chill of the Unseen: A chilling sensation that lingers in the air, as if unseen eyes watch your every move.",
        "Phantasmal Presence: A phantasmal presence that appears at the edge of vision, vanishing when approached.",
        "Eerie Enchantment: An eerie enchantment that seems to linger in the air, filling the rook with a magical aura.",
        "Spectral Embrace: A spectral embrace that seems to surround the rook, drawing those who enter into its grasp.",
        "Ghastly Glow: A ghastly glow that seeps from the rook's windows and openings, casting eerie shadows.",
        "Haunted Murmurs: Haunting murmurs that seem to echo through the rook's halls, as if the walls themselves whisper.",
        "Mysterious Phantoms: Mysterious phantoms that manifest in the corners of vision, vanishing before they can be seen clearly.",
        "Enigmatic Presence: An enigmatic presence that lingers in the air, as if the rook holds secrets yet to be uncovered.",
        "Sinister Shroud: A sinister shroud that surrounds the rook, like a cloak of darkness draped over its form.",
        "Ghostly Whispers: Ghostly whispers that seem to resonate through the rook's stone, telling tales of days long past.",
        "Ominous Aura: An ominous aura that emanates from the rook, enveloping its surroundings in an air of dread.",
        "Ethereal Shadows: Ethereal shadows that flicker and dance along the rook's walls, giving it an eerie appearance.",
        "Chilling Presence: A chilling presence that seems to seep from the very stone of the rook, making it feel alive with unseen energy.",
        "Supernatural Fog: A supernatural fog that blankets the rook, creating an otherworldly and mysterious atmosphere.",
        "Ephemeral Echoes: Ephemeral echoes that seem to reverberate through the rook's halls, as if the past speaks to the present.",
        "Spectral Phenomenon: A spectral phenomenon that defies explanation, making the rook an enigma waiting to be unraveled.",
        "Grim Enigma: A grim enigma that seems to surround the rook, hinting at untold secrets and hidden passages.",
        "Mysterious Shivers: Mysterious shivers that run down the spine of anyone who steps inside the rook's domain.",
        "Haunted Vortex: A haunted vortex of mist and shadow that swirls around the rook, as if drawing people closer to its heart.",
        "Phantom Presence: A phantom presence that seems to linger long after the rook has passed, leaving an eerie afterglow.",
        "Eerie Aura: An eerie aura that envelops the rook, making it feel like a place of forgotten memories and restless spirits.",
        "Cryptic Whispers: Cryptic whispers that seem to drift on the air, carrying tales of the rook's ancient past.",
        "Spectral Mystery: A spectral mystery that seems to permeate the rook, as if it holds secrets that few can fathom.",
        "Enchanted Spectacle: An enchanted spectacle of light and shadow that dances across the rook's surface, bewitching all who see it.",
        "Macabre Atmosphere: A macabre atmosphere that clings to the rook, leaving a sense of unease and foreboding.",
        "Ethereal Veil: An ethereal veil that seems to shroud the rook, giving it an otherworldly and mystical air.",
        "Cursed Haunting: A cursed haunting that fills the rook's halls, making it feel like a place of sorrow and loss.",
        "Apparitional Whispers: Apparitional whispers that seem to fill the air, as if the very walls of the rook speak.",
        "Chill of the Unseen: A chilling sensation that lingers in the air, like an unseen presence watching from the shadows.",
        "Phantasmal Presence: A phantasmal presence that seems to move along the rook's walls, as if unseen spirits walk its halls.",
        "Eerie Enchantment: An eerie enchantment that seems to pulse through the rook, filling it with an otherworldly magic.",
        "Spectral Embrace: A spectral embrace that seems to envelop the rook, drawing those who come near into its haunting aura.",
        "Ghastly Glow: A ghastly glow that emanates from the rook, casting haunting shadows and eerie illumination.",
        "Haunted Murmurs: Haunting murmurs that seem to echo through the rook's chambers, as if the very stone speaks.",
        "Mysterious Phantoms: Mysterious phantoms that appear and disappear around the rook, leaving a sense of unseen spirits.",
        "Enigmatic Presence: An enigmatic presence that lingers around the rook, like a riddle waiting to be solved.",
        "Sinister Shroud: A sinister shroud that envelops the rook, making it feel like a place of dark and malevolent forces.",
        "Ghostly Whispers: Ghostly whispers that seem to fill the air, as if the rook is speaking in hushed tones.",
        "Ominous Aura: An ominous aura that surrounds the rook, creating a sense of impending doom and ancient mystery.",
        "Ethereal Shadows: Ethereal shadows that dance and flicker along the rook's walls, as if unseen spirits move within.",
        "Chilling Presence: A chilling presence that seeps from the very stone of the rook, making it feel alive with supernatural energy.",
        "Supernatural Fog: A supernatural fog that blankets the rook, creating an otherworldly and mysterious atmosphere.",
        "Ephemeral Echoes: Ephemeral echoes that seem to resonate through the rook's halls, as if the past speaks to the present.",
        "Spectral Phenomenon: A spectral phenomenon that defies explanation, making the rook an enigma waiting to be unraveled.",
        "Grim Enigma: A grim enigma that seems to surround the rook, hinting at untold secrets and hidden passages.",
        "Mysterious Shivers: Mysterious shivers that run down the spine of anyone who steps inside the rook's domain.",
        "Haunted Vortex: A haunted vortex of mist and shadow that swirls around the rook, as if drawing people closer to its heart.",
        "Phantom Presence: A phantom presence that seems to linger long after the rook has passed, leaving an eerie afterglow.",
        "Eerie Aura: An eerie aura that envelops the rook, making it feel like a place of forgotten memories and restless spirits.",
        "Cryptic Whispers: Cryptic whispers that seem to drift on the air, carrying tales of the rook's ancient past.",
        "Spectral Mystery: A spectral mystery that seems to permeate the rook, as if it holds secrets that few can fathom.",
        "Enchanted Spectacle: An enchanted spectacle of light and shadow that dances across the rook's surface, bewitching all who see it.",
        "Macabre Atmosphere: A macabre atmosphere that clings to the rook, leaving a sense of unease and foreboding.",
        "Ethereal Veil: An ethereal veil that seems to shroud the rook, giving it an otherworldly and mystical air.",
        "Cursed Haunting: A cursed haunting that fills the rook's halls, making it feel like a place of sorrow and loss.",
        "Apparitional Whispers: Apparitional whispers that seem to fill the air, as if the very walls of the rook speak.",
        "Chill of the Unseen: A chilling sensation that lingers in the air, like an unseen presence watching from the shadows.",
        "Phantasmal Presence: A phantasmal presence that seems to move along the rook's walls, as if unseen spirits walk its halls.",
        "Eerie Enchantment: An eerie enchantment that seems to pulse through the rook, filling it with an otherworldly magic.",
        "Spectral Embrace: A spectral embrace that seems to envelop the rook, drawing those who come near into its haunting aura.",
        "Ghastly Glow: A ghastly glow that emanates from the rook, casting haunting shadows and eerie illumination.",
        "Haunted Murmurs: Haunting murmurs that seem to echo through the rook's chambers, as if the very stone speaks.",
        "Mysterious Phantoms: Mysterious phantoms that appear and disappear around the rook, leaving a sense of unseen spirits.",
        "Enigmatic Presence: An enigmatic presence that lingers around the rook, like a riddle waiting to be solved.",
        "Sinister Shroud: A sinister shroud that envelops the rook, making it feel like a place of dark and malevolent forces."
        ],
        /*10 -Roar*/
        [
        "Roaring Roar: A deafening roar that echoes through the land, shaking the very ground beneath it.",
        "Thunderous Rumble: A thunderous rumble that reverberates through the air, sending chills down the spines of all who hear it.",
        "Ear-Piercing Screech: An ear-piercing screech that cuts through the silence like a blade, filling the air with terror.",
        "Resounding Bellow: A resounding bellow that carries for miles, striking fear into the hearts of all who hear it.",
        "Haunting Howl: A haunting howl that sends shivers down the spines of those who dare to approach.",
        "Eerie Wail: An eerie wail that drifts on the wind, chilling all who listen.",
        "Mournful Moan: A mournful moan that echoes through the night, haunting the dreams of those who hear it.",
        "Spectral Scream: A spectral scream that pierces the darkness, filling the night with an otherworldly sound.",
        "Guttural Growl: A guttural growl that rumbles deep within the creature's chest, warning all who come near.",
        "Unearthly Roar: An unearthly roar that seems to come from the very depths of the earth, shaking the world around it.",
        "Chilling Chant: A chilling chant that rises and falls like the tide, captivating all who listen.",
        "Ghostly Groan: A ghostly groan that seems to emanate from the very stone of the creature, making it feel alive.",
        "Phantom Fury: A phantom fury that fills the air with its intensity, leaving a sense of impending doom.",
        "Vengeful Vibration: A vengeful vibration that hums in the air, as if the very earth itself is angry.",
        "Sinister Serenade: A sinister serenade that lulls its victims into a false sense of security before striking.",
        "Banshee's Bellow: A banshee's bellow that cuts through the night, foretelling a fate worse than death.",
        "Beastly Bellow: A beastly bellow that rumbles through the air, announcing the creature's presence.",
        "Malevolent Murmur: A malevolent murmur that seems to carry with it a promise of doom and destruction.",
        "Horrifying Howl: A horrifying howl that freezes the blood of all who hear it, leaving them paralyzed with fear.",
        "Soul-Shaking Shriek: A soul-shaking shriek that sends chills down the spines of even the bravest souls.",
        "Titanic Tremor: A titanic tremor that shakes the very foundations of the earth, leaving a wake of destruction in its path.",
        "Ghastly Growl: A ghastly growl that fills the air with an aura of malevolence and dread.",
        "Majestic Roar: A majestic roar that commands respect and awe, leaving all who hear it in its thrall.",
        "Dreadful Drone: A dreadful drone that hangs in the air, creating an atmosphere of foreboding and fear.",
        "Ancient Anthem: An ancient anthem that resounds through the ages, carrying with it the weight of history.",
        "Epic Echo: An epic echo that seems to reverberate through time itself, leaving a lasting impression on all who hear it.",
        "Vexing Vocalization: A vexing vocalization that teases and taunts, playing with the emotions of its prey.",
        "Ethereal Emanation: An ethereal emanation that seems to come from another realm, filling the air with mystery.",
        "Infernal Inferno: An infernal inferno that crackles with dark energy, engulfing its surroundings in flames.",
        "Spectral Symphony: A spectral symphony that weaves a haunting melody, enticing and terrifying in equal measure.",
        "Cacophonic Crescendo: A cacophonic crescendo that builds to a deafening climax, leaving all in its wake stunned.",
        "Abyssal Chorus: An abyssal chorus that echoes from the depths of the unknown, haunting the minds of those who hear it.",
        "Harmonic Havoc: A harmonic havoc that disrupts the very fabric of reality, creating chaos and confusion.",
        "Enigmatic Echolocation: An enigmatic echolocation that allows the creature to navigate with uncanny precision.",
        "Rumbling Reverberation: A rumbling reverberation that shakes the air, causing a feeling of unease.",
        "Chilling Cadence: A chilling cadence that sends a shiver down the spine, foreshadowing the horror to come.",
        "Eerie Euphony: An eerie euphony that fills the night with an unsettling melody, leaving all who hear it unnerved.",
        "Soul-Stirring Sonance: A soul-stirring sonance that reaches deep into the hearts of its audience, manipulating emotions.",
        "Astral Aria: An astral aria that seems to come from beyond the stars, captivating all who listen.",
        "Ominous Overture: An ominous overture that sets the stage for impending doom, striking fear into the hearts of onlookers.",
        "Mystic Melody: A mystic melody that carries with it a sense of ancient wisdom and power.",
        "Monstrous Melisma: A monstrous melisma that shifts and warps, twisting the very air into an unsettling harmony.",
        "Dissonant Dirge: A dissonant dirge that resonates with sorrow and despair, evoking a sense of loss.",
        "Demonic Decrescendo: A demonic decrescendo that fades into silence, leaving a lingering sense of dread.",
        "Resonating Rumble: A resonating rumble that seems to vibrate through the air, creating an eerie atmosphere.",
        "Spine-Chilling Serenade: A spine-chilling serenade that lulls its victims into a false sense of security before striking.",
        "Otherworldly Opera: An otherworldly opera that transports its audience to realms unknown, leaving them entranced.",
        "Cursed Chant: A cursed chant that carries a malevolent energy, capable of inflicting suffering on its listeners.",
        "Spectral Staccato: A spectral staccato that pierces the silence, leaving a sense of unease in its wake.",
        "Mythical Melisma: A mythical melisma that seems to resonate with the stories of ancient legends, filling the air with wonder.",
        "Chaos Crescendo: A chaos crescendo that builds in intensity, reflecting the tumultuous nature of the creature's power.",
        "Arcane Anthem: An arcane anthem that weaves a spellbinding melody, ensnaring the minds of all who hear it."
        ],
        /*11- Siege*/
        [
        "Flaming Trebuchets: Enormous trebuchets perched atop the rook's battlements, launching flaming projectiles at its foes.",
        "Crystal Cannons: Shimmering crystal cannons mounted on the rook's walls, firing powerful energy beams with deadly accuracy.",
        "Thundering Ballistae: Massive ballistae positioned throughout the rook, firing thundering bolts that can pierce through armor.",
        "Arcane Catapults: Arcane catapults hidden within the rook's interior, launching magical spheres that explode upon impact.",
        "Molten Mortars: Molten mortars embedded in the rook's structure, launching streams of molten lava at its enemies.",
        "Venomous Crossbows: Venomous crossbows adorning the rook's towers, shooting toxic bolts that corrode and weaken their targets.",
        "Stormcaller Cannons: Stormcaller cannons mounted on the rook's outer walls, firing bolts of lightning at its adversaries.",
        "Shadowcaster Ballistae: Shadowcaster ballistae concealed in the rook's shadows, firing bolts of darkness that sap the strength of their victims.",
        "Frostfire Catapults: Frostfire catapults positioned strategically around the rook, launching icy fireballs that freeze and burn simultaneously.",
        "Sonic Blasters: Sonic blasters affixed to the rook's battlements, emitting powerful shockwaves that can disorient and incapacitate foes.",
        "Cursed Crossbows: Cursed crossbows wielded by animated statues on the rook's parapets, shooting spectral arrows that haunt their targets.",
        "Golem Artillery: Golem-like constructs stationed within the rook, hurling massive boulders with tremendous force.",
        "Divine Arbalists: Divine arbalists lining the rook's walls, shooting holy arrows that can banish evil and protect the righteous.",
        "Inferno Mortars: Inferno mortars installed on the rook's upper levels, raining down fireballs that engulf the battlefield in flames.",
        "Enchanted Scorpions: Enchanted scorpions perched on the rook's ledges, firing magically charged darts that seek out their prey.",
        "Gravity Cannons: Gravity cannons positioned within the rook's chambers, launching projectiles that disrupt the laws of gravity and pull foes towards them.",
        "Aetherial Ballistae: Aetherial ballistae mounted atop the rook, firing bolts imbued with otherworldly energy that can pass through obstacles.",
        "Corrosive Catapults: Corrosive catapults fixed to the rook's structure, launching acid-filled vials that eat through armor and defenses.",
        "Celestial Crossbows: Celestial crossbows on the rook's rooftops, shooting radiant bolts that can blind and dazzle opponents.",
        "Blazing Trebuchets: Blazing trebuchets situated within the rook, launching fireballs that leave trails of scorching flames.",
        "Harmonic Harpooners: Harmonic harpooners stationed on the rook's terraces, firing sonic-infused harpoons that can immobilize targets with vibrations.",
        "Astral Artillery: Astral artillery placed within the rook's hidden chambers, launching projectiles that phase through solid objects and barriers.",
        "Magnetic Catapults: Magnetic catapults mounted on the rook's outer walls, firing metal projectiles that draw metal armor and weapons towards them.",
        "Spectral Snipers: Spectral snipers lurking in the rook's shadows, shooting ethereal arrows that can pass through multiple targets.",
        "Windstorm Ballistae: Windstorm ballistae positioned atop the rook, shooting gusts of wind that can push back and knock down enemies.",
        "Fatebreaker Cannons: Fatebreaker cannons hidden within the rook, firing beams that disrupt fate itself and alter the course of events.",
        "Chrono Mortars: Chrono mortars concealed within the rook's foundations, launching time-altering projectiles that slow or hasten their targets.",
        "Sentinel Crossbows: Sentinel crossbows mounted on the rook's highest towers, firing bolts that never miss their mark.",
        "Sanguine Catapults: Sanguine catapults adorning the rook's parapets, launching blood-red spheres that drain the life force of those they hit.",  
        "Frostbite Scorpions: Frostbite scorpions perched on the rook's exterior, firing icy stingers that freeze their targets in place.",
        "Ethereal Ballistae: Ethereal ballistae floating near the rook's battlements, firing spectral arrows that phase through solid objects.",
        "Solar Cannons: Solar cannons positioned atop the rook's towers, firing beams of intense sunlight that scorch and blind opponents.",
        "Abyssal Catapults: Abyssal catapults concealed within the rook's dark passages, launching void-infused projectiles that swallow light and matter.",
        "Stormstrike Harpooners: Stormstrike harpooners stationed on the rook's rooftops, firing harpoons electrified with lightning to stun and incapacitate foes.",
        "Terracotta Trebuchets: Terracotta trebuchets adorned with ancient runes, launching clay pots filled with alchemical concoctions that explode on impact.",
        "Gustcaller Artillery: Gustcaller artillery positioned on the rook's highest spires, firing tornado-like projectiles that create destructive whirlwinds.",
        "Phantom Crossbows: Phantom crossbows wielded by ghostly figures on the rook's parapets, shooting incorporeal bolts that haunt and torment their victims.",
        "Nova Mortars: Nova mortars embedded in the rook's structure, launching orbs of stellar energy that explode into blinding bursts of light.",
        "Venomous Scorpions: Venomous scorpions hidden in the rook's nooks, firing venom-filled stingers that induce paralysis in their targets.",
        "Geomancer Cannons: Geomancer cannons positioned within the rook, firing elemental projectiles imbued with the power of earth, water, fire, and air.",
        "Chaos Catapults: Chaos catapults mounted atop the rook's towers, firing chaotic bolts that cause unpredictable and random effects on impact.",
        "Spectral Ballistae: Spectral ballistae lining the rook's walls, firing ethereal arrows that phase through solid objects and barriers.",
        "Voidfire Artillery: Voidfire artillery positioned on the rook's highest platforms, launching spheres of dark energy that explode into void flames.",
        "Thundershock Crossbows: Thundershock crossbows wielded by animated statues on the rook's parapets, shooting bolts charged with thunder and electricity.",
        "Crystal Cannonade: Crystal cannonade hidden within the rook's chambers, releasing barrages of crystalline projectiles that penetrate armor with precision.",
        "Necrotic Catapults: Necrotic catapults affixed to the rook's exterior, launching cursed spheres that drain the life force from those they strike.",
        "Aurora Harpooners: Aurora harpooners stationed on the rook's terraces, firing harpoons infused with the vivid hues of the northern lights.",
        "Harmonic Ballistae: Harmonic ballistae positioned throughout the rook, firing harmonic bolts that create powerful resonating shockwaves.",
        "Dimensional Cannons: Dimensional cannons concealed within the rook's interior, firing beams that warp and distort the fabric of reality.",
        "Mythical Scorpions: Mythical scorpions perched on the rook's ledges, firing magical stingers that cause hallucinations and illusions.",
        "Searing Trebuchets: Searing trebuchets mounted atop the rook, launching incendiary projectiles that ignite everything they touch.",
        "Soulbound Artillery: Soulbound artillery hidden within the rook's foundations, launching projectiles that ensnare the souls of their targets.",
        "Eclipse Crossbows: Eclipse crossbows adorned with lunar symbols, shooting bolts infused with the dark energy of an eclipse.",
        "Stardust Catapults: Stardust catapults positioned on the rook's outer walls, launching celestial projectiles that leave trails of stardust in their wake.",
        "Vortex Mortars: Vortex mortars embedded in the rook's structure, launching swirling vortexes that pull in nearby objects and enemies.",
        "Thunderous Scorpions: Thunderous scorpions hidden within the rook, firing electrified stingers that deliver shocking blows.",
        "Runic Ballistae: Runic ballistae inscribed with ancient runes, firing bolts infused with elemental powers based on the runes used.",
        "Ephemeral Cannons: Ephemeral cannons placed atop the rook, firing bolts of pure magical energy that dissipate after striking their target.",
        "Firestorm Harpooners: Firestorm harpooners stationed on the rook's rooftops, firing harpoons enveloped in swirling flames.",
        "Lunar Catapults: Lunar catapults affixed to the rook's structure, launching spheres imbued with the mystical energy of the moon.",
        "Cosmic Crossbows: Cosmic crossbows adorned with celestial symbols, shooting bolts infused with the power of the stars.",
        "Hallowed Mortars: Hallowed mortars concealed within the rook, launching blessed orbs that purify and ward off evil.",
        "Shadowstrike Scorpions: Shadowstrike scorpions lurking in the rook's shadows, firing venomous stingers that also darken the senses of their victims.",
        "Soulfire Artillery: Soulfire artillery positioned within the rook, launching projectiles that consume the souls of those they strike.",
        "Mystic Ballistae: Mystic ballistae lining the rook's walls, firing bolts charged with mystical energies and ancient wisdom.",
        "Solar Flare Cannons: Solar flare cannons mounted on the rook's battlements, firing beams of solar energy that blind and burn enemies.",
        "Voidborne Catapults: Voidborne catapults hidden within the rook, launching void-infused spheres that create temporary void rifts on impact.",
        "Harmony Harpooners: Harmony harpooners stationed on the rook's terraces, firing harmonious harpoons that restore balance and peace.",
        "Elemental Cannons: Elemental cannons affixed to the rook's exterior, firing projectiles infused with the powers of the four classical elements.",
        "Luminescent Trebuchets: Luminescent trebuchets situated atop the rook, launching orbs of radiant light that blind and disorient adversaries.",
        "Abyssal Mortars: Abyssal mortars embedded in the rook's structure, launching orbs of darkness that suck the light and life out of their targets.",
        "Phantom Catapults: Phantom catapults hidden within the rook, launching spectral spheres that can pass through solid objects.",
        "Starcaller Artillery: Starcaller artillery positioned on the rook's highest platforms, launching celestial projectiles that explode like falling stars.",
        "Ethereal Crossbows: Ethereal crossbows wielded by ghostly figures on the rook's parapets, shooting arrows that can traverse between the material and ethereal planes.",
        "Crimson Harpooners: Crimson harpooners stationed on the rook's rooftops, firing harpoons infused with fiery red energy that burn and ignite targets.",
        "Lorekeeper Ballistae: Lorekeeper ballistae positioned throughout the rook, firing bolts inscribed with ancient knowledge and forgotten truths.",
        "Plasma Cannons: Plasma cannons concealed within the rook's interior, firing bolts of superheated plasma that melt through armor.",
        "Luminous Scorpions: Luminous scorpions perched on the rook's ledges, firing glowing stingers that emit blinding light.",
        "Voidspark Trebuchets: Voidspark trebuchets mounted atop the rook, launching orbs of dark energy that unleash destructive void sparks upon impact."
        ],
        /*12- Luminous Elements*/
        [
        "Bioluminescent Moss: Bioluminescent moss covering the rook's surfaces, emitting an eerie green glow in the darkness.",
        "Luminescent Runes: Luminescent runes etched onto the rook's walls and floors, emitting a soft, otherworldly light.",
        "Glowing Crystals: Glowing crystals embedded within the rook's structure, illuminating its interior with a radiant glow.",
        "Twinkling Stars: Twinkling stars scattered across the rook's surface, shining like distant celestial bodies in the night sky.",
        "Luminous Glyphs: Luminous glyphs engraved into the rook's stones, emitting a mesmerizing light that dances in the darkness.",
        "Glowing Vines: Glowing vines winding their way up the rook's walls, emitting a soft and enchanting luminescence.",
        "Radiant Spires: Radiant spires atop the rook, emanating a warm and inviting glow that contrasts with the twilight.",
        "Luminescent Eyes: Luminescent eyes on the rook's gargoyles and statues, casting an eerie glow across its exterior.",
        "Glowing Pools: Glowing pools of mystical liquid within the rook's interior, casting an ethereal radiance in its chambers.",
        "Lustrous Statues: Lustrous statues that line the rook's passageways, glowing with an ethereal light in the dimness.",
        "Luminous Lichen: Luminous lichen covering the rook's surfaces, creating a soft blue glow in the shadowy corners.",
        "Phosphorescent Orbs: Phosphorescent orbs floating around the rook's upper levels, emitting a soft and mysterious light.",
        "Glimmering Crests: Glimmering crests adorning the rook's turrets, shining with a celestial brilliance in the moonlight.",
        "Radiant Lanterns: Radiant lanterns hanging from the rook's walls, illuminating its chambers with a warm and welcoming glow.",
        "Luminous Stained Glass: Luminous stained glass windows decorating the rook, casting a kaleidoscope of colors onto its surfaces.",
        "Glowing Embers: Glowing embers scattered across the rook's rooftops, reminiscent of stars fallen to the earth.",
        "Luminescent Filigree: Luminescent filigree intertwined with the rook's architecture, creating an intricate and glowing lattice.",
        "Luminous Arches: Luminous arches framing the rook's entrances, providing a guiding light for those who dare to enter.",
        "Twilight Sparkle: The rook's surfaces shimmering with a captivating twilight sparkle, enchanting all who gaze upon it.",
        "Glowing Keystone: A glowing keystone embedded within the heart of the rook, emanating a powerful and radiant light.",
        "Luminous Gargoyles: Luminous gargoyles perched on the rook's ledges, glowing with an otherworldly luminescence.",
        "Radiant Skylights: Radiant skylights atop the rook, allowing beams of sunlight to illuminate its interior.",
        "Luminescent Webbing: Luminescent webbing stretching between the rook's towers, creating a mesmerizing and otherworldly network.",
        "Ethereal Illumination: An ethereal illumination enveloping the rook's body, glowing softly in the dark like a ghostly aura.",
        "Glowing Carvings: Glowing carvings etched into the rook's stones, depicting mysterious and arcane symbols.",
        "Luminous Antennae: Luminous antennae atop the rook's highest spires, shining like beacons in the night.",
        "Radiant Braziers: Radiant braziers placed strategically on the rook's exterior, illuminating the twilight with their fiery glow.",
        "Glowing Wards: Glowing wards inscribed on the rook's walls, protecting it with an aura of shimmering light.",
        "Lustrous Crests: Lustrous crests adorning the rook's battlements, glowing with a celestial brilliance.",
        "Luminous Windows: Luminous windows on the rook's highest floors, radiating a warm and inviting light.",
        "Starlit Roof: The rook's rooftops covered in a mesmerizing array of starlit patterns, twinkling in the darkness.",
        "Glowing Moat: A glowing moat surrounding the rook, casting an ethereal glow on its reflective surface.",
        "Luminous Foliage: Luminous foliage adorning the rook's exterior, glowing softly in the moonlight.",
        "Radiant Engravings: Radiant engravings etched into the rook's stones, imbuing it with a captivating radiance.",
        "Glimmering Gates: Glimmering gates leading into the rook, shining like beacons of light.",
        "Luminous Lanterns: Luminous lanterns hanging from the rook's ceilings, illuminating its chambers with a soft and enchanting glow.",
        "Glowing Gargoyles: Glowing gargoyles perched on the rook's towers, their eyes emitting an eerie and mysterious light.",
        "Moonlit Balconies: Moonlit balconies jutting out from the rook's walls, glowing softly under the moon's gentle gaze.",
        "Lustrous Crestings: Lustrous crestings lining the rook's parapets, casting a shimmering glow upon its silhouette.",
        "Luminescent Stalactites: Luminescent stalactites hanging from the rook's ceilings, illuminating its chambers with a soft, ethereal light.",
        "Radiant Banners: Radiant banners hanging from the rook's towers, glowing with the symbols of ancient power.",
        "Luminous Staircases: Luminous staircases leading up the rook's heights, guiding the way with their radiant glow.",
        "Glowing Glyphs: Glowing glyphs etched into the rook's walls, pulsating with mystical energy.",
        "Luminescent Ramparts: Luminescent ramparts lining the rook's exterior, glowing softly in the moonlit night.",
        "Radiant Observatory: A radiant observatory crowning the rook, its telescopes emitting beams of light into the night sky.",
        "Glowing Mosaics: Glowing mosaics decorating the rook's floors, shimmering with an otherworldly radiance.",
        "Luminous Buttresses: Luminous buttresses supporting the rook's walls, their glow lending an ethereal beauty to the structure.",
        "Twilight Adornments: Twilight adornments scattered across the rook's surface, emitting a gentle and mysterious light.",
        "Glowing Crown: A glowing crown perched atop the rook's highest tower, shining like a beacon in the darkness.",
        "Ethereal Spires: Ethereal spires adorning the rook's turrets, their glow casting an otherworldly aura around the structure.",
        "Luminous Observatory: A luminous observatory at the rook's peak, its telescopes casting an eerie radiance across the landscape.",
        "Lustrous Lamps: Lustrous lamps lining the rook's corridors, illuminating its passageways with a warm and inviting glow.",
        "Glowing Tapestries: Glowing tapestries hanging from the rook's walls, depicting scenes of ancient power and magic.",
        "Moonlit Rookery: A moonlit rookery on the highest tower, its inhabitants emitting a soft, ethereal glow.",
        "Luminous Courtyards: Luminous courtyards within the rook's heart, shining with an otherworldly radiance.",
        "Glowing Stairwells: Glowing stairwells winding through the rook's interior, providing a guiding light in the darkness.",
        "Lustrous Gargoyles: Lustrous gargoyles perched on the rook's parapets, their eyes glowing with an ominous light.",
        "Luminescent Halls: Luminescent halls within the rook, bathed in a soft and mystical glow.",
        "Radiant Chandeliers: Radiant chandeliers hanging from the rook's ceilings, illuminating its grand chambers with an opulent glow.",
        "Luminous Courtyards: Luminous courtyards within the rook's heart, shining with an otherworldly radiance."
        ],
        /*13- shape*/
        [
            "Defensive Shape: The rook's body is fortified with thick, sturdy walls, creating a formidable defense against attacks and making it difficult for enemies to breach its defenses.",
            "Offensive and Defensive Shape: The rook's body strikes a balance between offense and defense, with strategic designs that can both attack foes and withstand assaults with equal efficiency.",
            "Aggressive Shape: The rook's body takes on a fierce and aggressive form, exuding an aura of intimidation that can unsettle and deter adversaries from engaging in combat.",
            "Fortress Shape: The rook's body is akin to a massive fortress, boasting towering walls, battlements, and imposing gates, creating an almost impenetrable stronghold.",
            "Adaptive Shape: The rook's body can shift and change its form, allowing it to adapt to different combat situations and surprise opponents with its versatility.",
            "Evasive Shape: The rook's body is crafted with sleek and agile features, allowing it to maneuver swiftly and avoid attacks with ease.",
            "Shielding Shape: The rook's body incorporates large, shield-like elements that can provide protective barriers for itself and nearby allies during battle.",
            "Spiked Shape: The rook's body is covered in menacing spikes and jagged edges, turning it into a deadly hazard for any adversary that comes into contact with it.",
            "Ancient Form: The rook's body is reminiscent of ancient and powerful creatures, invoking a sense of reverence and fear in those who face it in combat.",
            "Elemental Form: The rook's body takes on the shape of a legendary elemental creature, harnessing the powers of nature to unleash devastating attacks on its foes.",
            "Deflecting Shape: The rook's body has angled surfaces and reflective materials, enabling it to deflect and redirect incoming attacks back at its opponents.",
            "Swift Striker: The rook's body is designed for swift and precise strikes, allowing it to deliver rapid and focused attacks with deadly accuracy.",
            "Sturdy Structure: The rook's body is built with a robust and unyielding structure, making it highly resistant to damage and challenging to topple in battle.",
            "Arcane Configuration: The rook's body is adorned with mystical symbols and runes, channeling arcane energies that enhance its offensive and defensive capabilities.",
            "Charging Form: The rook's body features a streamlined shape, allowing it to charge at enemies with tremendous force, knocking them aside with its sheer momentum.",
            "Martial Array: The rook's body incorporates elements inspired by various martial disciplines, granting it a diverse array of offensive and defensive maneuvers.",
            "Eldritch Design: The rook's body is infused with eldritch magic, giving it otherworldly abilities that can confound and terrify its adversaries.",
            "Divine Structure: The rook's body is imbued with divine power, providing it with divine protection and the ability to smite evil with righteous fury.",
            "Titanic Build: The rook's body is colossal and titanic in size, towering over enemies and causing the ground to quake with its every step.",
            "Invisible Enchantments: The rook's body contains hidden enchantments and magical barriers, making it deceptively resistant and elusive in battle.",
            "Demonic Form: The rook's body bears demonic symbols and infernal designs, evoking terror and dread in those who face it in combat.",
            "Celestial Shape: The rook's body takes on a celestial form, with celestial patterns and glowing motifs, harnessing celestial powers to enhance its attacks and defenses.",
            "Berserker Build: The rook's body is crafted to amplify its raw strength and aggression, turning it into a berserk force on the battlefield.",
            "Enigmatic Configuration: The rook's body is shrouded in mystery, with enigmatic patterns and shifting shapes that confound and disorient adversaries.",
            "Venomous Form: The rook's body secretes toxic substances and venomous compounds, making its attacks poisonous and lethal to those it strikes.",
            "Winged Structure: The rook's body features wings or wing-like appendages, allowing it to take to the skies and engage in aerial combat.",
            "Titanium Reinforced: The rook's body is reinforced with titanium plating, making it incredibly durable and resistant to all but the most powerful attacks.",
            "Rune-Carved Form: The rook's body is adorned with intricate runes that empower it with various magical effects, enhancing its combat abilities.",
            "Golem-like Shape: The rook's body resembles a formidable golem, imbued with the strength and resilience of ancient constructs.",
            "Clockwork Design: The rook's body incorporates clockwork mechanisms, enabling it to move with precision and timing in battle.",
            "Molten Composition: The rook's body is composed of molten rock and lava, capable of emitting scorching attacks and igniting adversaries.",
            "Arcing Tesla Coils: The rook's body has arcing Tesla coils that discharge potent electrical attacks, shocking and incapacitating its foes.",
            "Phantom Build: The rook's body has an ethereal and ghostly appearance, allowing it to phase through attacks and turn intangible when necessary.",
            "Crystalline Structure: The rook's body is made of crystalline material, refracting light and energy to create dazzling and disorienting displays in battle.",
            "Magnetic Core: The rook's body has a magnetic core that enables it to manipulate metallic objects and pull enemies towards its grasp.",
            "Frost-Infused Form: The rook's body is infused with frigid ice, freezing enemies and creating icy defenses to protect itself.",
            "Ensnaring Vines: The rook's body grows ensnaring vines that can immobilize and entangle foes, hindering their movement in battle.",
            "Stormforged Build: The rook's body is forged in the heart of a powerful storm, granting it control over wind and thunder in combat.",
            "Bloodthirsty Design: The rook's body is designed to absorb the essence of defeated enemies, granting it increased strength and resilience as it feeds on the fallen.",
            "Void-Touched Form: The rook's body is touched by the void, allowing it to manipulate darkness and shadows for stealthy attacks.",
            "Radiant Aura: The rook's body emits a radiant aura, imbuing its attacks with divine light and providing healing energy to allies in its vicinity.",
            "Time-Bending Configuration: The rook's body can manipulate time to accelerate its movements or slow down adversaries, gaining the upper hand in combat.",
            "Empowering Sigils: The rook's body is adorned with empowering sigils that enhance the strength and abilities of allies who fight alongside it.",
            "Chainbreaker Form: The rook's body is equipped with chains that can lash out and immobilize enemies, preventing them from escaping its grasp.",
            "Cursed Shape: The rook's body is cursed with malevolent magic, causing misfortune and ill fate to befall those who confront it in battle.",
            "Sunfire Build: The rook's body contains a core of intense sunfire, radiating powerful heat and light that can scorch adversaries.",
            "Venomous Mist: The rook's body can expel a toxic mist, enveloping the battlefield and inflicting venomous damage on any caught within it.",
            "Empyrean Architecture: The rook's body is constructed with celestial materials and heavenly craftsmanship, exuding an aura of divine presence.",
            "Thunderous Roar: The rook's body can unleash a thunderous roar, disorienting and staggering enemies with its sheer soundwaves.",
            "Magnetic Storm: The rook's body generates a magnetic storm, causing metallic objects to fly towards it and creating a dangerous environment for adversaries.",
            "Lunar Radiance: The rook's body emits a soft lunar radiance, granting it enhanced agility and heightened senses under the moonlight.",
            "Galeforce Form: The rook's body can unleash powerful gusts of wind, toppling enemies and creating a turbulent battlefield.",
            "Spiritbind Design: The rook's body is intricately woven with ethereal chains, enabling it to bind and trap the spirits of defeated foes.",
            "Volcanic Core: The rook's body houses a volcanic core, enabling it to erupt with scalding lava and molten rocks in combat.",
            "Dreadful Presence: The rook's body emits a dreadful aura that can instill fear and panic in those who encounter it, disrupting their focus and resolve in battle.",
            "Solar Flare: The rook's body can unleash a blinding solar flare, temporarily dazzling enemies and making them vulnerable to its attacks.",
            "Mindmeld Configuration: The rook's body can establish a psychic link with nearby allies, allowing them to coordinate and act as one in combat.",
            "Thorned Exterior: The rook's body is covered in sharp thorns and brambles, causing harm to any who attempt to get close.",
            "Gemheart Core: The rook's body contains a powerful gemheart core, radiating mystical energy and amplifying its magical attacks.",
            "Spectral Phasing: The rook's body can phase in and out of the spectral realm, making it elusive and difficult to target with physical attacks.",
            "Wardbearer Build: The rook's body is inscribed with ancient wards and protective symbols, providing it with powerful defenses against magic and curses.",
            "Gravity Well: The rook's body can create a localized gravity well, pulling enemies towards it and rendering them immobile.",
            "Vortex Formation: The rook's body can generate swirling vortexes, redirecting and neutralizing incoming projectiles.",
            "Netherforged Design: The rook's body is forged from the netherrealm, granting it eerie powers that defy the laws of reality.",
            "Fiery Annihilation: The rook's body can release a torrent of fiery destruction, incinerating foes with relentless flames.",
            "Quakebringer Form: The rook's body can cause the ground to tremble and shake, unsettling and destabilizing enemies.",
            "Sentinel Configuration: The rook's body contains sentinel constructs that can detach and patrol the battlefield, attacking enemies with precision and coordination.",
            "Echoing Howl: The rook's body can emit an echoing howl, disorienting and distracting adversaries with its deafening sound.",
            "Harmonious Ensemble: The rook's body can harmonize with other rooks, forming a cohesive ensemble to overwhelm enemies with synchronized attacks.",
            "Lifedrain Core: The rook's body contains a lifedrain core, absorbing the life force of enemies and rejuvenating itself in battle.",
            "Chrono-Temporal Design: The rook's body is infused with chrono-temporal energies, enabling it to manipulate time and space for tactical advantages.",
            "Dark Moon Eclipse: The rook's body can eclipse the moon, shrouding the battlefield in darkness and granting it heightened power under the night sky.",
            "Banebound Form: The rook's body is bound to the bane of its enemies, allowing it to exploit their weaknesses and inflict extra damage in combat.",
            "Primordial Composition: The rook's body is composed of primordial matter, harnessing the raw essence of creation to shape the battlefield."
        ]
    ]

    let reward= ['Helm','Arm','Rookling, a miniature version of itself,',`${searchArray(['ranged','melee'])} weapon`]

    

//People
    let intention = [ 
        "to kill you.", "to steal from you.", "to flee from you.", "to hide something from you.", "to negotiate a truce or alliance.", "to seek your assistance or guidance.", "to warn you about an impending danger.", "to challenge you to a friendly duel or competition.", "to request your help in a quest or mission.", "to offer a valuable reward or information.", "to seek forgiveness for past actions.", "to deliver a message from a distant ally.", "to share a secret or revelation.", "to request protection or refuge from a common threat.", "to ask for directions or assistance in finding a location.", "to trade valuable items or resources.", "to provide valuable information about an enemy or plot.", "to invite you to a prestigious event or gathering.", "to offer their services as a guide or mentor.", "to seek your advice on matters of great importance.", "to challenge you to a test of intelligence or wisdom.", "to ask for your aid in solving a local mystery.", "to seek a cure for a rare and deadly affliction.", "to offer a unique and powerful magical item.", "to share a prophetic vision or dream.", "to request your help in rescuing a loved one or friend.", "to seek your assistance in uncovering a hidden treasure.", "to warn you about a traitor or spy in your midst.", "to request your aid in overthrowing an oppressive ruler.", "to seek a rare and valuable artifact together.", "to offer their loyalty and service as a follower.", "to challenge you to a test of strength or combat.", "to ask for your assistance in uniting warring factions.", "to seek your guidance in resolving a moral dilemma.", "to request your help in stopping a natural disaster.", "to offer a chance to join a prestigious organization.", "to seek your aid in freeing enslaved or oppressed people.", "to challenge you to a series of trials or tests.", "to ask for your help in fulfilling a prophecy.", 
    "to seek your aid in breaking a powerful curse.", "to offer valuable information about a hidden enemy base.", "to request your assistance in rebuilding a destroyed community.", "to seek your wisdom in settling a longstanding dispute.", "to challenge you to a race or athletic competition.", "to ask for your help in unraveling a complex conspiracy.", "to seek your aid in finding a lost or stolen heirloom.", "to offer a chance to join a legendary group of heroes.", "to request your assistance in saving a dying land.", "to seek your advice on harnessing powerful magical energies.", "to challenge you to a game of strategy or tactics.", "to ask for your help in reuniting long-lost family members.", "to offer a rare opportunity to commune with ancient spirits.", "to seek your aid in restoring a fallen deity or guardian.", "to request your assistance in breaking a curse on their family.", "to challenge you to a dance or musical competition.", "to ask for your help in deciphering an ancient prophecy.", "to seek your aid in preventing a catastrophic event.", "to offer a chance to join a noble and honorable quest.", "to request your assistance in healing a dying world.", "to seek your guidance in mastering a powerful arcane art.", "to challenge you to a series of mind-bending riddles.", "to ask for your help in understanding a forgotten language.", "to offer a rare chance to witness a celestial phenomenon.", "to seek your aid in stopping a relentless undead horde.", "to request your assistance in locating a legendary mentor.", "to challenge you to a test of faith or belief.", "to ask for your help in reconciling feuding gods or deities.", "to offer a sacred and powerful oath of loyalty.", "to seek your guidance in unlocking hidden memories.", "to request your aid in dispelling a powerful illusion.", "to challenge you to a friendly cooking or culinary contest.", "to ask for your help in restoring a corrupted magical spring.", "to seek your assistance in mastering a forbidden technique.", 
    "to offer a chance to witness an ancient and epic battle.", "to request your aid in repairing a damaged time continuum.", "to challenge you to a friendly artistic or crafting competition.", "to ask for your help in retrieving a stolen legendary sword.", "to seek your guidance in communicating with elemental beings.", "to offer a glimpse into a distant and utopian future.", "to request your assistance in calming an enraged mythical beast.", "to challenge you to a test of endurance or survival skills.", "to ask for your help in navigating a treacherous magical maze.", "to seek your aid in breaking an ancient family curse.", "to offer a chance to witness a celestial alignment of planets.", "to request your guidance in understanding an ancient prophecy.", "to challenge you to a friendly drinking or ale-quaffing contest.", "to ask for your help in saving a dying magical creature.", "to seek your assistance in uncovering a long-lost magical city.", "to offer a chance to witness a rare cosmic event.", "to request your aid in unlocking the secrets of a sacred temple.", "to challenge you to a test of compassion and kindness.", "to ask for your help in releasing a trapped and vengeful spirit.", "to seek your guidance in forging a legendary weapon.", "to offer a glimpse into a dark and dystopian future.", "to request your assistance in breaking a time loop.", "to challenge you to a friendly storytelling or bardic contest.", "to ask for your help in preventing a catastrophic magical surge.", "to seek your aid in appeasing an ancient and wrathful god.", "to offer a chance to witness the rise of a new moon deity.", "to request your guidance in taming a powerful mythical beast.", "to challenge you to a test of empathy and emotional understanding.", "to ask for your help in recovering a stolen tome of forbidden knowledge.", "to seek your assistance in dispelling a powerful curse on a kingdom.", "to offer a chance to witness a rare and awe-inspiring meteor shower.", "to request your aid in healing a corrupted and decaying magical forest.", "to seek your guidance in unlocking the secrets of an ancient cosmic library.", "to challenge you to a friendly contest of wit and cleverness.", "to ask for your help in freeing a powerful being trapped in an artifact.", "to offer a glimpse into a future where darkness and light collide.", "to request your assistance in preventing a cataclysmic magical convergence.", 
    "to seek your aid in negotiating a delicate and fragile peace between warring nations.", "to challenge you to a test of humility and selflessness.", "to ask for your help in restoring balance to a chaotic and war-torn realm.", "to offer a chance to witness a celestial dance of stars and constellations.", "to kill, because they are under the influence of mind control.", "to kill, because they mistake you for someone else.", "to test your strength or abilities.", "to kill, due to a prophecy or curse.", "to kill, because they are controlled by a malicious entity.", "to settle a personal vendetta.", "to obtain a valuable item in your possession.", "to eliminate a witness of their dark deeds.", "to kill, because they are following orders from a superior.", "to prove themselves to their group or leader.", "to kill, out of fear or misunderstanding.", "to gain power or influence.", "to kill, because they are in a berserker rage.", "to kill, as part of a ritual or sacrifice.", "to fulfill an ancient prophecy.", "to kill, due to a cultural or historical conflict.", "to protect someone they care about.", "to kill, because they see you as a threat to their goals.", "to kill, because they believe it is their destiny.", "to avenge the death of a loved one.", "to kill, because they are cursed or hexed.", "to test the loyalty of their followers.", "to kill, as a result of a misunderstanding or miscommunication.", "to kill,to gain favor with a powerful entity.", "to kill, due to deep-seated prejudices or biases.", "to prove their loyalty to a secret society.", "to kill,because they are possessed by a malevolent spirit.", "to protect a sacred or forbidden place.", "to kill,because they are driven by an insatiable bloodlust.", "to acquire resources for their group or faction.", "to maintain their reputation as a formidable warrior.", "to kill, due to an ancient rivalry between their people and yours.", "to kill, because they believe you hold a valuable secret.", "to demonstrate their dominance over you.", "to kill, because they are mercenaries hired to attack you.", "to prevent you from reaching a significant goal.", 
    "to distract you while their allies carry out a plan.", "to kill, because they have a twisted sense of justice.", "to exact revenge for a past conflict.", "to kill, because they are desperate and see you as an easy target.", "to impress or gain recognition from a powerful figure.", "to protect their way of life or beliefs.", "to kill, because they are affected by a contagious madness.", "to silence you before you expose their evil deeds.", "to kill, because they are fanatically devoted to a cause.", "to prove their worthiness to join a notorious group.", "to kill, due to a misunderstanding of a prophecy.", "to stop you from uncovering a hidden truth.", "to eliminate potential competition or rivals.", "to kill, because they are cursed to attack all who approach.", "to conquer new territories for their ruler.", "to kill, because they are trapped and must fight to survive.", "to retrieve a stolen artifact in your possession.", "to guard a forbidden knowledge or artifact.", "to kill, because they are seeking redemption for their past.", "to maintain control over a region or population.", "to defend their homeland from perceived invaders.", "to kill, because they are on a quest for personal glory.", "to uphold their code of honor or duty.", "to kill, because they are manipulated by a cunning mastermind.", "to demonstrate their loyalty to an evil overlord.", "to kill, because they are hunting specific creatures, and you fit the description.", "to prevent you from fulfilling a prophecy that opposes their goals.", "to test your worthiness to join their elite group.", "to kill, because they are trying to prove a point or make a statement.", "to eradicate a perceived threat to their race or species.", "to kill, because they are compelled by a magical geas or curse.", "to eliminate witnesses to their dark rituals.", "to fulfill an ancient blood feud between families.",
        "to kill, because they believe they can gain supernatural powers by defeating you.", "to defend a powerful artifact or location.", "to settle a dispute over limited resources.", "to kill, because they are manipulated by a powerful artifact or entity.", "to punish you for trespassing on sacred ground.", "to satisfy the demands of a malevolent deity.", "to kill, because they are seeking redemption through violence.", "to protect a rare and endangered species you are studying.", "to kill, because they are convinced you are a spy or infiltrator.", "to stop you from uncovering a corrupt organization.", "to silence a whistleblower who knows too much.", "to kill, because they are on a quest to collect bounties on wanted individuals.", "to ensure the fulfillment of a prophecy or dark prophecy.", "to kill, because they are in a state of religious fervor.", "to eliminate a witness to their true identity or nature.", "to kill, because they are seeking revenge for a past defeat.", "to prevent you from accessing powerful magical knowledge.", "to kill, because they are under the effects of a rage-inducing substance.", "to appease their bloodthirsty god or goddess.", "to kill, because they are under the control of an evil artifact.", "to stop you from breaking a curse that binds them.", "to challenge you for the title of a legendary warrior.", "to kill, because they are affected by a rare celestial alignment.", "to fulfill a prophecy that requires your defeat.", "to prevent you from uncovering a hidden magical academy.", "to kill, because they are agents of a malevolent otherworldly entity.", "to protect a sacred creature or guardian.", "to kill, because they are seeking a legendary weapon that you possess.", "to prevent you from saving a loved one from a curse.", "to kill, because they are manipulated by a charismatic cult leader.", "to eliminate all witnesses to their dark experiments.", "to maintain their dominance over a region's criminal activities.", "to kill, because they are part of a cursed undead horde.", "to prevent you from reaching a mythical location with untold power." 
    ]
    function rookWeapon(){
        let melee = [
            `Siege Maul: A massive, spiked hammer for smashing opponents and structures alike.`,
            `Rampart Shield: A gigantic shield resembling a castle wall, used for defense and bashing.`,
            `Towering Halberd: A long polearm with an axe blade and spearhead, capable of reaching distant foes.`,
            `Gatecrasher Gauntlets: Enormous metal gauntlets that can pummel enemies and crush obstacles.`,
            `Battlement Blade: A colossal, double-edged sword reminiscent of castle battlements.`,
            `Drawbridge Maul: A heavy, chain-linked mace capable of tearing through armor.`,
            `Turret Lance: A long, spear-like weapon with a pointed top, used for charging attacks.`,
            `Crenellation Claws: Gigantic, castle-like claws for slashing and tearing at enemies.`,
            `Moat Cleaver: A massive, curved blade resembling the shape of a castle moat.`,
            `Portcullis Axe: A large axe with a retractable, castle gate-like blade for trapping and slashing foes.`,
            `Balustrade Flail: A chain weapon with spiked spheres, inspired by castle balcony railings.`,
            `Rook's Tower Shield: A tower shield with the appearance of a rook chess piece, offering exceptional defense.`,
            `Keep Cleaver: A heavy, two-handed cleaver weapon, perfect for cleaving through armor.`,
            `Dungeon Club: A large, wooden club with metal bands, reminiscent of a dungeon cell door.`,
            `Parapet Pikes: Long, spear-like pikes designed to hold back enemies from reaching the castle's walls.`,
            `Mantlet Mace: A mace with a collapsible, protective shield attached for added defense.`,
            `Great Hall Greataxe: A massive, double-bladed greataxe designed for overwhelming strikes.`,
            `Vaulted Hammer: A colossal hammer with intricate designs reminiscent of a vaulted ceiling.`,
            `Hearthstone Hammer: A stone hammer with a fiery core, inspired by castle hearthstones.`,
            `Throne Room Broadsword: A large, wide-bladed sword resembling a throne room's majesty.`,
            `Castle Spire Spear: A long spear with a spearhead resembling the spires of a castle tower.`,
            `Alcove War Pick: A heavy, pickaxe-like weapon with intricate designs inspired by alcoves.`,
            `Courtyard Battleaxe: A massive, single-bladed battleaxe used for powerful cleaving strikes.`,
            `Chandelier Morningstar: A chain weapon with a spiked ball inspired by castle chandeliers.`,
            `Tower Shield Bash: A large tower shield used for bashing and pushing opponents.`,
            `Dais Dagger: A short, broad dagger with ornate designs resembling a castle dais.`,
            `Armory Warhammer: A warhammer with the appearance of an armory rack, adorned with various weapons.`,
            `Guardhouse Glaive: A long glaive with a blade resembling a guardhouse roof.`,
            `Hearthside Spear: A long spear with a blade shaped like a castle hearth.`,
            `Moat Maul: A massive, spiked maul used to crush enemies like a moat's drawbridge.`,
            `Castle Chain Whip: A chain weapon with a castle-shaped weight on the end, capable of tripping foes.`,
            `Crenelation Crescent Blade: A curved blade resembling the shape of a crenelation on a castle wall.`,
            `Chandelier Chain Scourge: A chain weapon with multiple spiked balls inspired by castle chandeliers.`,
            `Gallery Glaive: A glaive with a blade shaped like an ornate gallery railing.`,
            `Bastion Broadsword: A large, wide-bladed sword resembling a fortified bastion.`,
            `Drawbridge Cleaver: A heavy, cleaver-like weapon with a retractable blade reminiscent of a drawbridge.`,
            `Pillar Pike: A long spear with a pointed top resembling the shape of a castle pillar.`,
            `Citadel Sledgehammer: A massive sledgehammer used for breaking through barriers and armor.`,
            `Tapestry Flail: A chain weapon with spiked balls adorned with intricate tapestry designs.`,
            `Dungeon Door Shield: A shield designed to look like a dungeon door, offering sturdy protection.`,
            `Pillared Pike: A long spear with a pointed top resembling the shape of a castle pillar.`,
            `Roofscape Spear: A spear with a blade designed to resemble the silhouette of castle rooftops.`,
            `Crenelated Cudgel: A cudgel with an intricate, crenelated design for added impact.`,
            `Tapestried Tower Shield: A tower shield with colorful tapestry designs, both protective and decorative.`,
            `Alcove Broadsword: A large, broad-bladed sword with ornate designs inspired by alcoves.`,
            `Gallery Guisarme: A long polearm with a blade shaped like an ornate gallery railing.`,
            `Pillared Parry Dagger: A short parry dagger with designs inspired by castle pillars.`,
            `Hearthside Halberd: A long polearm with an axe blade and spearhead, inspired by a castle hearth.`,
            `Vaulted Voulge: A long polearm with a curved blade resembling the shape of a vaulted ceiling.`,
            `Rampart Rapier: A rapier with an ornate hilt and guard inspired by castle ramparts.`
        ]
        let ranged = [
            `Ballista: A massive crossbow-like weapon that launches large bolts with incredible force and range.`,
            `Catapult: A siege weapon that hurls massive stones, boulders, or even fiery projectiles at long distances.`,
            `Trebuchet: A powerful siege engine that flings massive projectiles using a counterweight system.`,
            `Cannon: An enormous, artillery-like firearm that shoots heavy iron or stone balls.`,
            `Siege Crossbow: A giant crossbow designed to shoot large arrows or bolts with tremendous power.`,
            `Mortar: A heavy, short-barreled cannon used for lobbing explosive shells over walls and fortifications.`,
            `Ballistae Volley: A multi-shot ballista that fires a barrage of smaller bolts in a wide spread.`,
            `Boulder Launcher: A mechanical launcher that propels massive stones or boulders towards its targets.`,
            `Stone Hurler: A slingshot-like device that hurls rocks and debris with tremendous force.`,
            `Catapult Turret: A rotating turret equipped with a catapult, allowing for quick and precise targeting.`,
            `Crossbow Barrage: A volley of giant crossbow bolts shot in rapid succession.`,
            `Flame Spewer: A device that emits jets of fiery flames, engulfing enemies in burning chaos.`,
            `Rock Rain: A mechanism that releases a storm of smaller rocks raining down on foes from above.`,
            `Arrow Storm: A hail of giant arrows or bolts raining down upon enemies in a widespread pattern.`,
            `Chainshot Launcher: A launcher that propels chains or large metal links to entangle and immobilize targets.`,
            `Boulder Barrage: A continuous barrage of large stones and boulders launched in succession.`,
            `Fireball Catapult: A specialized catapult that launches huge fireballs, causing massive explosions.`,
            `Thunder Cannon: A cannon that fires large iron spheres, causing deafening concussions upon impact.`,
            `Ballista Crossfire: Multiple ballistae firing in unison, unleashing a deadly barrage of bolts.`,
            `Molten Rock Eruption: A device that spews molten rock and lava at enemies from a distance.`,
            `Stone Slingshot: A massive slingshot that propels enormous stones with great force.`,
            `Boulder Storm: A barrage of massive boulders crashing down on enemies in a chaotic storm.`,
            `Iron Spike Launcher: A launcher that hurls massive iron spikes, piercing through armor and structures.`,
            `Flame Cannon: A cannon that shoots streams of blazing flames, incinerating anything in its path.`,
            `Arrow Barrage: A storm of giant arrows raining down on enemies, covering a wide area.`,
            `Chainnet Volley: A volley of chain nets launched to ensnare and immobilize foes.`,
            `Molten Fireburst: A burst of molten rock and fire expelled in all directions, creating a hazardous area.`,
            `Siege Harpoon: A harpoon-like projectile that impales and draws enemies closer to the monster.`,
            `Stone Fragmentation: A mechanism that launches stones with explosive shells, causing shrapnel damage.`,
            `Flame Arrow Volley: A volley of flaming arrows raining down upon enemies, setting everything ablaze.`,
            `Iron Shard Rain: A barrage of sharp iron shards launched to rain down on enemies below.`,
            `Ballista Burst: A powerful, charged shot from a ballista that creates an explosive impact on impact.`,
            `Chain Shot Barrage: A barrage of large, chain-linked projectiles launched at enemies.`,
            `Fireball Volley: A volley of fiery orbs raining down on enemies, causing widespread devastation.`,
            `Boulder Bombardment: A continuous bombardment of large boulders crashing onto the battlefield.`,
            `Scalding Steam Emission: A release of scalding hot steam, blinding and scorching enemies.`,
            `Iron Spike Barrage: A continuous barrage of giant iron spikes propelled towards enemies.`,
            `Thunderous Blast: A massive explosion caused by launching a heavy projectile with great force.`,
            `Chainnet Storm: A storm of chain nets launched to trap and immobilize enemies from all sides.`,
            `Molten Slag Shower: A shower of molten slag and lava raining down on enemies.`,
            `Firestorm Cannon: A cannon that fires a rapid succession of explosive fireballs.`,
            `Boulder Volley: A volley of massive boulders sent crashing into enemy ranks.`,
            `Crossbow Salvo: A salvo of large crossbow bolts fired in quick succession.`,
            `Shrapnel Scatter: A mechanism that launches projectiles to spread deadly shrapnel across the battlefield.`,
            `Fire Arrow Barrage: A continuous barrage of flaming arrows raining down upon enemies.`,
            `Iron Shard Barrage: A barrage of sharp iron shards raining down on enemies below.`,
            `Molten Rock Shower: A shower of molten rock and lava raining down on enemies.`,
            `Ballista Barrage: A barrage of large bolts unleashed in quick succession from multiple ballistae.`,
            `Chainnet Barrage: A continuous barrage of chain nets launched at enemies from all angles.`,
            `Flamethrower: A device that emits a continuous stream of intense flames, engulfing foes in fire.`
        ]
        if(rollDice(100)>50) {
            return `a melee weapon (${searchArray(melee)})`
        } else {
            return `a ranged weapon (${searchArray(ranged)})`
        }
    }
    function rookDescription(){
        const stasis = [0,1,2,3,4,5,6,7,8,9,10,11,12,13]
        let choices = shuffleSlice(stasis, 3+rollDice(4))
        console.log('Choices:'+ choices)
        let rookDescriptionArray =[]
        choices.forEach(element => rookDescriptionArray.push(searchArray(rook[element])))
        return rookDescriptionArray
    }

    function humanEnemy(){
        document.getElementById("Enemy").innerHTML = ''
        document.getElementById("Enemy").innerHTML =  `${searchArray([`One person`,`A duo`, `a group of ${toWords(2+rollDice(3))} people`])} attacks! They are using ${searchArray(['ranged','melee'])} attacks. Their intention is ${searchArray(intention)}.`
    }
    function rookEnemy(){
        document.getElementById("Enemy").innerHTML = ''
        document.getElementById("Enemy").innerHTML = `A Rook Appears! It is infused with ${searchArray(magic)} magic. The rook primarily uses ${rookWeapon()}. Should the rook be defeated, a ${searchArray(reward)} can be found. There are a few features that make this rook special:`
        loopPrintList(rookDescription(),"Enemy")
    }


//Draw
    let cardHistory = []
    function draw(id) {
        let cardArray =  [2,3,4,5,6,7,8,9,10,'j','q','k','a']
        let suitArray = ['c','h','s','d']
        const cards= {
            ac:"./images/cards/ac.png",
            ad:"./images/cards/ad.png",
            ah:"./images/cards/ah.png",
            as:"./images/cards/as.png",
            kc:"./images/cards/kc.png",
            kd:"./images/cards/kd.png",
            kh:"./images/cards/kh.png",
            ks:"./images/cards/ks.png",
            qc:"./images/cards/qc.png",
            qd:"./images/cards/qd.png",
            qh:"./images/cards/qh.png",
            qs:"./images/cards/qs.png",
            jc:"./images/cards/jc.png",
            jd:"./images/cards/jd.png",
            jh:"./images/cards/jh.png",
            js:"./images/cards/js.png",
            '1c':"./images/cards/1c.png",
            '2c':"./images/cards/2c.png",
            '3c':"./images/cards/3c.png",
            '4c':"./images/cards/4c.png",
            '5c':"./images/cards/5c.png",
            '6c':"./images/cards/6c.png",
            '7c':"./images/cards/7c.png",
            '8c':"./images/cards/8c.png",
            '9c':"./images/cards/9c.png",
            '10c':"./images/cards/10c.png",
            '1d':"./images/cards/1d.png",
            '2d':"./images/cards/2d.png",
            '3d':"./images/cards/3d.png",
            '4d':"./images/cards/4d.png",
            '5d':"./images/cards/5d.png",
            '6d':"./images/cards/6d.png",
            '7d':"./images/cards/7d.png",
            '8d':"./images/cards/8d.png",
            '9d':"./images/cards/9d.png",
            '10d':"./images/cards/10d.png",
            '1h':"./images/cards/1h.png",
            '2h':"./images/cards/2h.png",
            '3h':"./images/cards/3h.png",
            '4h':"./images/cards/4h.png",
            '5h':"./images/cards/5h.png",
            '6h':"./images/cards/6h.png",
            '7h':"./images/cards/7h.png",
            '8h':"./images/cards/8h.png",
            '9h':"./images/cards/9h.png",
            '10h':"./images/cards/10h.png",
            '1s':"./images/cards/1s.png",
            '2s':"./images/cards/2s.png",
            '3s':"./images/cards/3s.png",
            '4s':"./images/cards/4s.png",
            '5s':"./images/cards/5s.png",
            '6s':"./images/cards/6s.png",
            '7s':"./images/cards/7s.png",
            '8s':"./images/cards/8s.png",
            '9s':"./images/cards/9s.png",
            '10s':"./images/cards/10s.png"
        }
        function pickCardAndSuit(){
            let x = searchArray(cardArray) + searchArray(suitArray)
            if (checkConflict(x,cardHistory)===1){
                do {
                    x = searchArray(cardArray) + searchArray(suitArray)
                } while (checkConflict(x,cardHistory)===1) 
                cardHistory.push(x)
                return x
            } else {
                cardHistory.push(x)
                return x
            }

        }

        let cardChoice = pickCardAndSuit()
        var img = new Image();
        img.src = cards[cardChoice]
        let elem = img
        img.onload = function () {
            if (id === 'playerDrawCon') {
                document.getElementById("playerDrawCon").appendChild(elem)
            } else {
                document.getElementById("enemyDrawCon").appendChild(elem)
            }
        }
        if (cardHistory.length ===52) {
            cardHistory.length = 0
            console.log('Deck shuffled.')
        }
        
    }

//shuffle and clear board
function shuffleDeck() {
    cardHistory.length = 0
    console.log('Deck shuffled.')
}
function clearBoard() {
    document.getElementById("playerDrawCon").innerHTML=''
    document.getElementById("enemyDrawCon").innerHTML=''
}


    









