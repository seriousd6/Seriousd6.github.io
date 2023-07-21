/*###################Chance and array manipulation methods#########################*/
function shuffle(array) {
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
    }
    return array;
};
function searchArray(array) {
    let shuffled = shuffle(array)
    return shuffled[Math.floor(Math.random() * shuffled.length)];
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
        let li = document.createElement("li");
        let text = document.createTextNode(item);
        li.appendChild(text);
        document.getElementById(id).appendChild(li);
    });
};
function modify(number) {
    return Math.floor(number * (.95 + Math.random() * .4))
};
function shuffleSlicePrint(array, number) {
    let a = shuffle(array).slice(0, number)
    return a.join(', ')
};
function shuffleSlice(array, number) {
    return shuffle(array).slice(0, number)
};
function loopCountPrintList(array, id) {

    final = array
    final.forEach(function(item) {
        let li = document.createElement("li");
        let text = document.createTextNode(item);
        li.appendChild(text);
        document.getElementById(id).appendChild(li);
    });
};
function toWords(s) {
    let th = ['', 'thousand', 'million', 'billion', 'trillion'];
    let dg = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'];
    let tn = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen'];
    let tw = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety'];


    s = s.toString();
    s = s.replace(/[\, ]/g, '');
    if (s != parseFloat(s)) return 'not a number';
    let x = s.indexOf('.');
    if (x == -1)
        x = s.length;
    if (x > 15)
        return 'too big';
    let n = s.split('');
    let str = '';
    let sk = 0;
    for (let i = 0; i < x; i++) {
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
        let y = s.length;
        str += 'point ';
        for (let i = x + 1; i < y; i++)
            str += dg[n[i]] + ' ';
    }
    return str.replace(/\s+/g, ' ');
};
function printArray(array) {
    for (i = 0; i < array.length; i++) {
        console.log(array[i])
    }
};
function reload() {
    location.reload()
};


/*==================================================================================*/
/*-----------------------------Page Scripts Below-----------------------------------*/
/*==================================================================================*/
    /*
    function magic() {
        const worldMagic = [
            "Magic is Mundane - Mortals have no magic, it is solely the domain of the world’s deities and lesser supernatural entities.", 
            "Magic is Rare - The world’s magic is hard to find and harder to use. The vast majority is useless superstition, incredibly tedious to employ, or dangerous to the user, but what works tends to be stronger than the freely available magic of other worlds.", 
            "Magic is Dark - All but the weakest magic comes only through diabolical pacts and unspeakable deeds, and when it does, it is corrupting, chaotic, and catastrophic to the user and their victims alike.",
            "Magic takes Tools - The mortal mind can’t grasp any but the weakest of magic, only through artifice, scroll-scribbling, alchemy, and enchantments can its energies be brought to bear.", 
            "Magic is Demanding - Magic is both powerful and attainable, but it requires decades of difficult study, ironclad self-control, and immense personal sacrifice from its users.", 
            "Magic is Inherited - Only mortals descended from or greatly favored by supernatural entities can channel magic, and while great within its scope, their power is narrow and limited.", 
            "Magic is Common - The study of magic is well-known and widespread, to the extent a town may have a wizard living between its carpenter and smith, but due to its ubiquity, it tends to be weaker than the less available magic of other worlds.", 
            "Magic is Myriad - Numerous methods of magic exist, everything from dark pacts, to artificial tools, to arduous study, and simple circumstance of birth, and its divergent practitioners may have an intense and oft-bloody rivalry with one another.", 
            "Magic is Science - In their curiosity, mortals have codified and tested magic to the extent it’s seen as merely another discipline of science, and broadly implemented in technology.", 
            "Magic is Everywhere - Powerful magic is freely accessible, at minimal to no cost and risk to its users, and magical entities that may be rare in other worlds readily serve mortals in all aspects of life.", 
            "Magic is Bound - The mortal races aren’t able to wield magic on their own, instead they must give up a part of themselves to bind a spirit’s soul to theirs, or entrap a spirit in an item of precious value and force it to cast at its wielder’s command.",
        ];
        document.getElementById("Magic").innerHTML = searchArray(worldMagic);
    };
    */

//Defining magic
    //Source of arcane power
        //Calamity
        //Divine
        //Mortal invention
        //natural source
    //Status of magic
    //commonality
    //Pillars
        //source
        //cost
        //potency
        //commonality
        //accessibility
        //pillars of mastery
    //paths
        //scientific
        //Artisan
        //arcane
        //natural
        //legendary
        //forbidden

//Where is magic derived from?
const magics = {
    'Scientific': { /* The power of understanding and discovery*/
    'Source' : [ 'Chemistry', 'Physics', 'Mathematics', 'Biology', 'Astronomy', 'Engineering', 'Geology', 'Computers', 'Psychology', 'Sociology', 'Anthropology', 'Economics', 'Political Science', 'Linguistics', 'Neuroscience', 'Medicine', 'Genetics', 'Optics', 'Education', 'Botany', 'Zoology', 'Archaeology', 'Environmental Science', 'Climatology' ],
    'Cost' : [ 'Precision', 'Expense', 'Time', 'Complexity', 'Waste', 'Ethical Concerns', 'Experiments with Risks', 'Public Misunderstanding', 'Access to Cutting-Edge Technology' ],
    'Potency' : [ 'Precision', 'Material Quality', 'Material Volatility', 'Scale', 'Complexity', 'Controlled Conditions', 'Collaboration with Experts', 'Validation by Peer Review' ],
    'Accessibility' : [ 'Beliefs or Superstitions', `${buildClass()} relies on this magic`, 'Societal Impact Based on it', "What Can Practitioners Offer that Others Can't?", 'Where Can it be Learned?', 'When Would a Practitioner be Sought Out?', 'Scientific Institutions', 'Research Laboratories', 'Scientific Conferences', 'Scholarly Journals' ],
    'Mastery' : [ 'How is it Learned and Can it be Learned Elsewhere?', 'Is the Idea of a Master Formal or Informal? Can Great Knowledge be Possessed Without Being Respected?', 'Who is More Respected, Educators or Innovators?', 'Can Mastery be Achieved Through Scholarship Without Practical Experience?', 'Is Any Aspect Still Theoretical?', 'Research Collaboration', 'Innovative Breakthroughs', 'Pioneering Discoveries', 'Resolving Long-standing Mysteries', 'Mentorship and Apprenticeship' ],
    },

        'Artisan' : {/*Expression and creativity*/
            'Source' : ['Music', 'Textiles', 'Writing', 'Sculpting', 'Painting', 'Physical','Enchantment','Runes','Potions and elixers','weaving','Pottery and Ceramics','Glyphs','Culinary arts','Glassblowing','Tailoring','Architecture', 'Metalworking', 'Jewelry Crafting', 'Woodworking', 'Performing Arts'],
            'Cost' : ['Time', 'strain', 'Emotions', 'Intricacy', 'Material','Focus', 'Personal Sacrifice', 'Spirituality', 'Perfectionism'],
            'Potency' : ['Practice', 'Creativity', 'Education', 'Materials', 'Intimacy','Passion', 'Inspiration', 'Collaboration', 'Audience Response'],
            'Accessibility' : [ 'Beliefs or Superstitions', `${buildClass()} relies on this magic.`, 'Societal Impact Based on it', "What Can Practitioners Offer that Others Can't?", 'Where Can it be Learned?', 'When Would a Practitioner be Sought Out?', 'Artisan Guilds', 'Hidden Workshops', 'Mentorship Tradition', 'Public Competitions' ],
            'Mastery' : ['is mastery permanent or does it ebb and flow as te person changes', 'based on inflexible foundations or subjective creativity?', 'are masters bound by the same limitations for potency as other practitioners?', 'is a master more likely to influence their discipline through work or teaching?','what aspects cannot be taught?','Legacy of Masters', 'Innovations of Masters', 'Legendary Artisans', 'Sought After as Teachers', 'The Influence of Masterpieces']
            },

        'Arcane' : { /*Knowledge, Power, and experience beyond the mundane - magic by its own merit*/
            'Source' : [ 'Birthright', 'Truth', 'Emblems', 'Scholarship', 'Granted', 'Reservoir', 'Lost Texts', 'Cosmic Entities', 'Astral Realm', 'Mystic Artifacts', 'Arcane Inheritance', 'Dreams and Visions' ],
            'Cost' : [ 'Memory', 'Vitality', 'Ritual', 'Mortality', 'Sacrifice', 'Ancestral Connections', 'Psychic Strain', 'Time and Effort', 'Binding Contracts' ],
            'Potency' : [ 'Age', 'Will', 'Birthright', 'Knowledge', 'Secrecy', 'Mystical Significance', 'Manipulating Cosmic Energies', 'Channeling Ethereal Forces', 'Unlocking Hidden Potential' ],
            'Accessibility' : [ 'Beliefs or Superstitions', `${buildClass()} relies on this magic.`, 'Societal Impact Based on it', "What Can Practitioners Offer that Others Can't?", 'Where Can it be Learned?', 'When Would a Practitioner be Sought Out?', 'Mysterious Arcane Guilds', 'Hidden Orders of Sages', 'Eldritch Nexus Locations', 'Celestial Conjunctions' ],
            'Mastery' : [ 'Found in Developing New Ideas, Mastering Lost Ones, or Both?', 'Are There Any Limitations on Learning?', 'Masters Keep Company with Others? with Students? with the World?', 'What Skills Pave Paths to Master? What Makes Practitioners Falter?', 'What Roles do Masters Play in the World?', 'Pioneers of New Arcane Knowledge', 'Preservers of Ancient Arcane Lore', 'Harbingers of Astral Revelations', 'Wardens Against Arcane Abuses', 'Custodians of Cosmic Balance' ],
            },

        'Natural' : { /*Derived from the forces of nature*/
            'Source' : [ 'Elements', 'Flora', 'Beasts', 'Cycles', 'Positions', 'Spirits', 'Weather', 'Celestial Bodies', 'Natural Phenomena', 'Territory', 'Seasons', 'Tides' ],
            'Cost' : [ 'Control', 'Consumption', 'Vitality', 'Discomfort', 'Proximity', 'Harmony with Nature', 'Balance with the Ecosystem', 'Sacrifice for the Land', 'Communing with Nature' ],
            'Potency' : [ 'Environment', 'Connection', 'Uniqueness', 'Balance', 'Harmony', 'Amplification of Natural Forces', 'Alignment with Celestial Events', 'Harnessing Natural Cycles', 'Merging with the Land' ],
            'Accessibility' : [ 'Beliefs or Superstitions', `${buildClass()} relies on this magic.`, 'Societal Impact Based on it', "What Can Practitioners Offer that Others Can't?", 'Where Can it be Learned?', 'When Would a Practitioner be Sought Out?', 'Sacred Natural Sites', 'Druidic Circles', 'Nature Spirit Communes', 'Initiation Rites' ],
            'Mastery' : [ 'Do Masters Need to Fully Commit to Nature? Do They Maintain a Connection to Civilization? Do They Walk Between Worlds?', 'Do Masters Take on Aspects of Their Source in Thought or Appearance?', 'Who Depends on Masters of Natural Magic?', 'What Roles Do Masters Play in the World?', 'Balance Keepers of the Natural Order', 'Guardians of Sacred Natural Sites', 'Harmonizers of Nature and Civilization', 'Channellers of Celestial Energies', 'Stewards of Rare and Endangered Species' ],
            },

        'Legendary' : { /*It moves a story or defines the lesson of a story*/
            'Source' : [ 'Irony', 'Fate', 'Poetry', 'Gods', 'Folkways', 'Axiom', 'Artifacts', 'Locations', 'Legendary Creatures', 'Prophetic Visions', 'Sacred Texts', 'Mysterious Prophecies' ],
            'Cost' : [ 'Healing', 'Faith', 'Unlikeliness', 'Last Hope', 'OMNIPresent', 'Sacrifice of Loved Ones', 'Severing Bonds', 'Atonement', 'Permanence of Consequences' ],
            'Potency' : [ 'Almost Invisible', 'Only the Wise See It', 'Only Certain Individuals See and Understand It - It Should be a Secret', 'Only Certain Individuals See and Understand It - It Should be Explained', 'It is Obvious, Dramatic, and Undeniable', 'Reality-Bending', 'Altering the Fabric of Space and Time', 'Shaping the Course of Events', 'Changing the Fate of Nations' ],
            'Accessibility' : [ 'Beliefs or Superstitions', `${buildClass()} relies on this magic.`, 'Societal Impact Based on it', 'What Historical Event was Shaped by it?', 'What Figure was Associated with this Magic?', 'Ancient Riddles and Enigmas', 'Guardians of Legendary Knowledge', 'Visions and Dreams', 'Hereditary Lineages of Prophecy', 'Hidden Tombs and Temples' ],
            'Mastery' : [ 'Have There Been Masters of Legendary Magic? What Did They Do?', 'Are There Any Active Masters?', 'Do Beings Need to be Worthy of Legendary Magic or Can it Work Through Anyone?', 'Can a Being Temporarily Wield Legendary Magic or Does it Require a Permanent Change?', 'Does Legendary Magic Typically Solve or Create Problems?', 'Guardians of Ancient Secrets', 'Keepers of Prophetic Wisdom', 'Harbingers of Legendary Events', 'Envoys of the Gods', 'The Balance of Destiny' ],
            },

        'Forbidden' : { /*Magic that is feared or shunned*/
            'Source' : ['Alien', 'Sin', 'adversaries', 'appropriation', 'passion', 'desire','Taboo Rituals', 'Cursed Relics', 'Lost Artifacts', 'Malevolent Spirits'],
            'Cost' : ['reason', 'morality', 'transformation', 'blight', 'debt','Sanity', 'Loyalty', 'Life Essence', 'Loss of Innocence'],
            'Potency' : ['transgression', 'Sacrifice', 'Suffering', 'Woe', 'Perception','Corruption', 'Destruction', 'Temporal Anomalies', 'Reality Warping'],
            'Accessibility' : [`${buildClass()} relies on this magic.`, 'societal impact base don it', 'what can practitioners offer that others cant?', 'where can it be learned?', 'when would a practitioner be seeked out?','Hidden Cults', 'Forbidden Academies', 'Arcane Black Markets', 'Ancient Prophecies'],
            'Mastery' : ['IS forbidden magic inherently evil, or is there potential for good? should good guys have access to it?', 'is it possible to master forbidden magic without lettign it control you?', 'What threshold must be crossed to master that most shy away from?', 'is there a known limit to the power for forbidden magic?', 'how common is mastering forbidden magic?', 'The Price of Mastery', 'Guardians of Forbidden Knowledge', 'Covenants of the Forbidden', 'The Fall of Past Masters'],
            }
};

function buildClass() {
    function findClass() {
        //Class Array
        let classes = [
                [
                    'Bard', 'Cleric', 'Fighter', 'Paladin', 'Ranger', 'Rogue', 'Warlock',
                ],
                [
                    'Barbarian', 'Druid', 'Monk', 'Nomad',
                ],
                [
                    'Sorcerer', 'Wizard', 'Artificer', 'Summoner',
                ],
                [
                    'Bounty Hunter', 'Blood Hunter', 'Mystic',
                ],
            ]
            //Profession Array
        let professions = {
            'Agriculture, Animal-Husbandry, and Forestry': [
                'Animal Handler', 'Arborist', 'Beekeeper', 'Birdcatcher', 'Cowherd', 'Dairyboy/Dairymaid', 'Falconer', 'Farmer',
                'Fisher', 'Forager', 'Gamekeeper', 'Groom', 'Herder', 'Horse Trainer', 'Hunter', 'Master-of-Hounds', 'Miller',
                'Prospector', 'Ranger', 'Renderer', 'Shepherd', 'Stablehand', 'Thresher', 'Trapper', 'Vintner', 'Woodcutter', 'Zookeeper',
            ],
            'Architecture and Construction': [
                'Architect', 'Brickmaker', 'Brickmason', 'Carpenter', 'Claymason', 'Plasterer', 'Roofer', 'Stonemason', 'Streetlayer',
            ],
            'Arts and Entertainment': [
                'Acrobat', 'Actor', 'Chef', 'Dancer', 'Gladiator', 'Glasspainter', 'Jester', 'Illuminator', 'Minstrel', 'Musician', 'Painter', 'Piper', 'Playwright', 'Poet', 'Sculptor', 'Singer/Soprano', 'Tattooist', 'Wrestler', 'Brawler', 'Writer',
            ],
            'Business and Trade': [
                'Accountant', 'Banker', 'Brothel Owner/Pimp', 'Chandler', 'Collector', 'Entrepreneur', 'Fishmonger', 'General Contractor', 'Grocer', 'Guild Master',
                'Innkeeper', 'Ironmonger', 'Merchant', 'Peddler', 'Plantation Owner', 'Speculator', 'Street Vendor', 'Thriftdealer', 'Tradesman',
            ],
            'Communications': [
                'Courier', 'Herald', 'Interpreter', 'Linguist', 'Messenger', 'Town Crier', 'Translator',
            ],
            'Craftsman': [
                'Armorer', 'Blacksmith', 'Bladesmith', 'Bookbinder', 'Bowyer', 'Brewer', 'Broom Maker', 'Candlemaker',
                'Cartwright', 'Cobbler', 'Cooper/Hooper', 'Cutler', 'Embroiderer', 'Engraver', 'Fletcher', 'Furniture Artisan',
                'Furrier', 'Glazier/Glassmaker', 'Glovemaker', 'Goldsmith/ Silversmith', 'Hatter/Milliner',
                'Jeweler', 'Leatherworker', 'Locksmith', 'Mercer', 'Potter', 'Printer', 'Rope-maker', 'Saddler',
                'Seamstress/Tailor', 'Soaper', 'Tanner', 'Taxidermist', 'Thatcher', 'Tinker', 'Toymaker', 'Watchmaker',
                'Weaponsmith', 'Weaver', 'Wheelwright', 'Whittler', 'Woodcarver',
            ],
            'Crime': [
                'Assassin', 'Bandit', 'Burglar', 'Charlatan/Conman', 'Cockfighter/ Gamefighter', 'Crime Boss',
                'Cutpurse', 'Drug Lord', 'Fence', 'Kidnapper', 'Loan Shark', 'Outlaw', 'Pirate', 'Poacher', 'Smuggler',
                'Thief/Rogue',
            ],
            'Education, Science, and Math': [
                'Anthropologist', 'Apprentice', 'Archaeologist', 'Archivist', 'Artificer', 'Astrologer', 'Botanist', 'Cartographer', 'Chemist', 'Dean', 'Engineer', 'Historian', 'Horologist', 'Librarian',
                'Mathematician', 'Philosopher', 'Professor', 'Scholar / Researcher', 'Scribe', 'Student', 'Teacher', 'Theologian', 'Tutor',
            ],
            'Government and Law': [
                'Archduke / Archduchess', 'Aristocrat', 'Baron', 'Baroness', 'Chancellor', 'Chief', 'Constable', 'Count / Countess', 'Courtier', 'Diplomat', 'Duke / Duchess', 'Emperor / Empress', 'Judge',
                'King-Queen', 'Knight', 'Lady - in -Waiting', 'Lawyer / Advocate', 'Marquess', 'Master of Coin', 'Master of the Revels', 'Minister', 'Noble', 'Orator / Spokesman', 'Prince / Princess',
                'Steward', 'Squire', 'Tax Collector', 'Viscount / Viscountess', 'Ward',
            ],
            'Health': [
                'Alchemist', 'Apothecary', 'Bloodletter', 'Doctor', 'Healer', 'Herbalist', 'Midwife', 'Mortician', 'Nurse', 'Physician', 'Surgeon/ Chirurgeon', 'Veterinarian',
            ],
            'Hospitality and Common Labor': [
                'Baker', 'Barber', 'Barkeep', 'Barmaid', 'Butcher', 'Charcoal Maker', 'Chatelaine / Majordomo', 'Chimney Sweeper', 'Clerk', 'Cook', 'Copyist', 'Croupier', 'Distiller', 'Florist', 'Gardener',
                'Gongfarmer', 'Gravedigger', 'Housemaid', 'Kitchen Drudge', 'Laborer', 'Lamplighter', 'Landscaper', 'Laundry Worker', 'Longshoreman', 'Maid / Butler', 'Miner', 'Orphanage Caretaker', 'Page',
                'Pastry Chef', 'Plumer(Feather dealer)', 'Porter', 'Prostitute', 'Rag - and - Bone Man', 'Slave', 'Street Sweeper', 'Tavern Worker', 'Vermin Catcher', 'Water Bearer',
            ],
            'The Magical Arts': [
                'Abjurer', 'Archmage', 'Augurer', 'Conjuror', 'Elementalist', 'Enchanter / Enchantress', 'Evoker', 'Hearth - witch', 'Illusionist', 'Mage', 'Necromancer', 'Ritualist', 'Runecaster', 'Sage',
                'Seer / Oracle', 'Shaman', 'Shapeshifter', 'Sorcerer / Sorceress', 'Summoner', 'Transmuter', 'Warlock', 'Witchdoctor', 'Witch', 'Wizard', 'Wordsmith',
            ],
            'Military and Security': [
                'Admiral', 'Archer', 'Bailiff', 'Bodyguard', 'Bouncer', 'Captain', 'Castellan', 'Cavalier', 'City Watch', 'Detective / Investigator', 'Duelist', 'Executioner', 'Fireman', 'Guard', 'General',
                'Jailer', 'Man - at - Arms', 'Marshall', 'Mercenary', 'Sapper', 'Sentinel', 'Sergeant', 'Sergeant - at - Arms', 'Scout', 'Siege Artillerist', 'Slave Driver', 'Soldier', 'Spearman', 'Spy', 'Tactician',
                'Torturer', 'Warden', 'Warmage',
            ],
            'Religion': [
                'Abbot / Abbess', 'Acolyte', 'Archbishop', 'Bishop', 'Cardinal', 'Chaplain', 'Clergy', 'Cleric', 'Cultist', 'Cult Leader', 'Diviner', 'Friar', 'High Priest / Pope', 'Inquisitor', 'Missionary', 'Monk',
                'Nun', 'Paladin', 'Pardoner', 'Priest', 'Prophet', 'Sexton', 'Templar',
            ],
            'Transportation': [
                'Boatman', 'Bosun', 'Cabbie / Wagoner', 'Caravaneer', 'Caravan Guard', 'Charioteer', 'Ferryman', 'First Mate', 'Helmsman', 'Navigator', 'Purser', 'Sailor', 'Sea Captain', 'Shipwright', 'Swab',
            ],
            'Unemployed, Self-Employed, and Outcast': [
                'Adventurer', 'Beggar', 'Blood Hunter / Monster Hunter', 'Bounty Hunter', 'Deserter', 'Disgraced Noble', 'Dungeon Delver', 'Elder / Retiree', 'Exile', 'Explorer', 'Ex - Criminal', 'Far-Traveler',
                'Folk Hero', 'Fool', 'Gambler', 'Grave Robber / Tomb Raider', 'Heckler', 'Heretic', 'Hermit', 'Housewife / Househusband', 'Pilgrim', 'Rebel / Political Dissident', 'Refugee', 'Runaway Slave',
                'Squatter', 'Urchin', 'Vagabond'
            ],

        };

        //Pick a profession
        function findProf() {
            var getFieldName = searchArray(Object.keys(professions));
            var npcProf = searchArray(professions[getFieldName]);
            return npcProf + ", Subfield of " + getFieldName;
        };

        //Pick a class or profession
        function classReturn() {
            var chance = rollDice(100);
            if (chance > 98) {
                return searchArray(classes[3]);
            } else if (chance > 95) {
                return searchArray(classes[2]);
            } else if (chance > 85) {
                return searchArray(classes[1]);
            } else if (chance > 65) {
                return searchArray(classes[0]);
            } else {
                return findProf()
            };
        }
        return classReturn()
    };
    return findClass();
};

function magic() {
    let typeArray = Object.keys(magics)
    let pure = searchArray(typeArray)
    let dual = shuffleSlice(typeArray,2)
    let primary = dual[0]
    let secondary = dual[1]
    let trio = shuffleSlice(typeArray,3)
    let t1= trio[0]
    let t2= trio[1]
    let t3= trio[2]
    let c1 = shuffleSlice(typeArray,1)
    let c2 = shuffleSlice(typeArray,1)
    let c3 = shuffleSlice(typeArray,1)
    let c4 = shuffleSlice(typeArray,1)


    //2 Cost
    //2 Potency
    //2 Accessibility
    //2 masters
    let templates = [
        /*Pure*/ `Pure: ${pure} || Source: ${searchArray(magics[pure].Source)} || Costs : ${shuffleSlicePrint(magics[pure].Cost,2)} || Potencies: ${shuffleSlicePrint(magics[pure].Potency,2)} || Accessibility: ${shuffleSlicePrint(magics[pure].Accessibility,2)} || Mastery: ${shuffleSlicePrint(magics[pure].Mastery,2)}`,
        /*Hybrid*/`Duo: ${dual[0] + ', '+ dual[1]} || Source: ${searchArray(magics[primary].Source)}, ${searchArray(magics[secondary].Source)} || Costs : ${searchArray(magics[primary].Cost)}, ${shuffleSlicePrint(magics[secondary].Cost,2)}  || Potencies: ${searchArray(magics[primary].Potency)}, ${shuffleSlicePrint(magics[secondary].Potency,2)}  || Accessibility: ${searchArray(magics[primary].Accessibility)}, ${shuffleSlicePrint(magics[secondary].Accessibility,2)}  || Mastery: ${searchArray(magics[primary].Mastery)}, ${shuffleSlicePrint(magics[secondary].Mastery,2)} `,
        /*Trio*/`Trio: ${t1 + ', '+ t2+ ', '+t3} || Source: ${searchArray(magics[t1].Source)}, ${searchArray(magics[t2].Source)}, ${searchArray(magics[t3].Source)} || Costs : ${searchArray(magics[t1].Cost)}, ${searchArray(magics[t2].Cost)}, ${searchArray(magics[t3].Cost)}  || Potencies: ${searchArray(magics[t1].Potency)}, ${searchArray(magics[t2].Potency)}, ${searchArray(magics[t3].Potency)} || Accessibility: ${searchArray(magics[t1].Accessibility)}, ${searchArray(magics[t2].Accessibility)}, ${searchArray(magics[t3].Accessibility)}  || Mastery: ${searchArray(magics[t1].Mastery)}, ${searchArray(magics[t2].Mastery)}, ${searchArray(magics[t3].Mastery)}`,
        /*Complex*/`Complex: ${c1 + ', '+ c2+ ', '+c3+ ', '+c4} || Source: ${searchArray(magics[c1].Source)}, ${searchArray(magics[c2].Source)}, ${searchArray(magics[c3].Source)}, ${searchArray(magics[c4].Source)}  || Costs : ${searchArray(magics[c1].Cost)}, ${searchArray(magics[c2].Cost)}, ${searchArray(magics[c3].Cost)}, ${searchArray(magics[c4].Cost)}   || Potencies: ${searchArray(magics[c1].Potency)}, ${searchArray(magics[c2].Potency)}, ${searchArray(magics[c3].Potency)}, ${searchArray(magics[c4].Potency)} || Accessibility: ${searchArray(magics[c1].Accessibility)}, ${searchArray(magics[c2].Accessibility)}, ${searchArray(magics[c3].Accessibility)}, ${searchArray(magics[c4].Accessibility)}   || Mastery: ${searchArray(magics[c1].Mastery)}, ${searchArray(magics[c2].Mastery)}, ${searchArray(magics[c3].Mastery)}, ${searchArray(magics[c4].Mastery)}`
        /**/
        /**/
        /**/
    ]
    document.getElementById("Magic").innerHTML = searchArray(templates)
};
