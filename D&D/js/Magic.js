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
const magics = {
    'Scientific': { /* The power of understanding and discovery*/
        'Source' : [ //The 'Scientific' magical system draws its power from the understanding and exploration of various branches of science. The sources of this magic include:
            `Chemistry: The manipulation of chemical elements and compounds to achieve magical effects.`,
            `Physics: The harnessing of the fundamental laws of the universe to wield magical forces.`,
            `Mathematics: The application of mathematical principles to create magical formulas and patterns.`,
            `Biology: The utilization of biological processes and organisms to produce magical phenomena.`,
            `Astronomy: The study of celestial bodies and their interactions to channel cosmic energies.`,
            `Engineering: The application of practical and technical knowledge to create magical devices and structures.`,
            `Geology: The utilization of geological forces and materials to manifest magical powers.`,
            `Computers: The integration of computational power and algorithms to create digital magic.`,
            `Psychology: The understanding of the human mind to influence emotions and thoughts magically.`,
            `Sociology: The study of societal structures and behaviors to create magical effects.`,
            `Anthropology: The knowledge of cultural practices and traditions to wield cultural magic.`,
            `Economics: The understanding of economic systems to manipulate wealth and resources magically.`,
            `Political Science: The utilization of political strategies and power dynamics to shape events magically.`,
            `Linguistics: The use of language and communication to cast magical spells and incantations.`,
            `Neuroscience: The knowledge of the brain and nervous system to influence thoughts and actions magically.`,
            `Medicine: The application of medical knowledge to heal and enhance through magical means.`,
            `Genetics: The manipulation of genetic information to produce magical changes in living beings.`,
            `Optics: The manipulation of light and optics to create illusions and visual magic.`,
            `Education: The dissemination of magical knowledge through educational methods.`,
            `Botany: The study of plants and their properties to access botanical magic.`,
            `Zoology: The understanding of animals and their behavior to wield zoological magic.`,
            `Archaeology: The knowledge of ancient artifacts and civilizations to access ancient magic.`,
            `Environmental Science: The understanding of the environment and ecosystems to use environmental magic.`,
            `Climatology: The study of climate and weather patterns to harness weather-related magic.`,
            `Astrology: The belief in the influence of celestial bodies on magical powers and destinies.`,
            `Parapsychology: The exploration of psychic and paranormal phenomena for magical applications.`,
            `Robotics and AI: The integration of artificial intelligence and robotics into magical constructs.`,
            `Nanotechnology: The manipulation of materials at the nanoscale to achieve magical effects.`,
            `Mythology and Folklore: Drawing power from mythical tales and cultural legends for magical purposes.`,
            `Quantum Mechanics: Utilizing quantum principles to enable unconventional magical phenomena.`,
            `Virtual Reality: Using virtual worlds and simulations to enhance magical experiences.`,
            `Time Manipulation: Tapping into the fabric of time to affect past, present, or future magically.`,
            `Chaos Theory: Embracing chaos and unpredictability to achieve chaotic magic.`,
            `Dark Matter and Energy: Harnessing the mysteries of the universe's dark components for magical use.`,
            `Music and Sound: The use of harmonics and sound frequencies to create musical magic.`,
            `Art and Creativity: Channeling the power of artistic expression for magical enchantments.`,
            `Dreams and Subconscious: Manipulating the realm of dreams and the subconscious mind for magic.`,
            `Alchemy: The transmutation of materials and the quest for magical perfection.`,
            `Magnetism and Electromagnetism: Controlling magnetic forces to achieve magnetic magic.`,
            `Acoustics: The study of sound propagation and its magical applications.`,
            `Plasma Physics: Utilizing plasma states for fiery and electrifying magical effects.`,
            `Hydrology: Manipulating water and its flow for hydro-magical abilities.`,
            `Pyrotechnics: The art of magical fireworks and controlled explosions.`,
            `Psychokinesis: Using the mind to influence matter and energy through psychic magic.`
        ],
        'Cost' : [ //Utilizing scientific magic comes with specific costs and challenges related to the nature of science and experimentation. The costs associated with this magic include:
            `Precision: Achieving accurate results and maintaining precision in magical experiments.`,
            `Expense: The cost of acquiring and using sophisticated equipment and materials.`,
            `Time: The extensive time required for research, experiments, and analysis.`,
            `Complexity: Dealing with intricate scientific theories and formulas in magical applications.`,
            `Waste: The potential for resources and materials to be wasted during experimentation.`,
            `Ethical Concerns: The moral dilemmas arising from the use of scientific magic.`,
            `Experiments with Risks: The inherent dangers and uncertainties involved in magical experimentation.`,
            `Public Misunderstanding: Dealing with skepticism and misunderstanding from non-magical communities.`,
            `Access to Cutting-Edge Technology: The need for access to advanced technology for complex magical tasks.`,
            `Personnel and Expertise: The cost of employing skilled magical researchers and specialists.`,
            `Maintenance and Repairs: The ongoing expenses to keep magical equipment and facilities functional.`,
            `Environmental Impact: Considering the ecological consequences of magical experiments.`,
            `Energy Consumption: The high energy requirements of certain magical processes.`,
            `Competition and Rivalry: The costs of engaging in magical research competition with other practitioners.`,
            `Regulatory Compliance: The expenses involved in adhering to magical regulations and laws.`,
            `Funding and Grants: Securing financial support for magical research and projects.`,
            `Information Security: Protecting sensitive magical knowledge from theft or misuse.`,
            `Mistakes and Failures: Dealing with setbacks and losses resulting from unsuccessful experiments.`,
            `Balancing Cost and Benefit: Weighing the potential benefits of magical advancements against their costs.`,
            `Long-Term Sustainability: Ensuring the viability and affordability of magical practices over time.`
        ],
        'Potency' : [ //The potency of scientific magic relies on the careful application of scientific principles and collaboration with experts. Factors influencing the potency of this magic include:
            `Precision: Achieving accurate and reliable magical effects through precise measurements and controls.`,
            `Material Quality: Using high-quality materials that impact the magical outcome positively.`,
            `Material Volatility: Harnessing volatile materials that amplify the magical effects.`,
            `Scale: The size and scope of the magical experiment or application affecting its power.`,
            `Complexity: The level of complexity in the magical processes and calculations.`,
            `Controlled Conditions: Maintaining controlled environments for magical experiments.`,
            `Collaboration with Experts: Engaging with specialists and experts in specific scientific fields.`,
            `Validation by Peer Review: Gaining recognition and validation through peer-reviewed scientific work.`,
            `Energy Efficiency: Maximizing the magical output while minimizing energy consumption.`,
            `Time-Dependent Effects: How the duration of a magical effect impacts its potency.`,
            `Magical Catalysts: The use of catalysts to enhance the potency and efficiency of magical reactions.`,
            `Environmental Interactions: How external factors and the environment influence magical potency.`,
            `Adaptability and Flexibility: The potency of magical systems in adapting to various situations.`,
            `Psychological Factors: The influence of a magician's mental state on the potency of their magic.`,
            `Interdisciplinary Insights: Leveraging knowledge from different scientific disciplines to boost potency.`,
            `Historical Advancements: Learning from past breakthroughs and discoveries to increase potency.`,
            `Limitations and Trade-Offs: Exploring the boundaries and trade-offs in magical potency.`,
            `Ethical Considerations in Potency: The moral implications of using highly potent magical effects.`,
            `Cultural and Regional Variations: How different cultures approach and measure magical potency.`
        ],
        'Accessibility' : [ //Accessing scientific magic is closely tied to educational institutions and research settings. Factors impacting its accessibility include:
            `Beliefs or Superstitions: Cultural beliefs and superstitions influencing the acceptance of scientific magic.`,
            `Dependant: The "${buildClass()}" profession heavily relies on this magic.`,
            `Societal Impact: The impact of scientific magic on society affecting its acceptance and regulation.`,
            `What Can Practitioners Offer that Others Can't?: The unique abilities and contributions of scientific practitioners.`,
            `Where Can it be Learned?: The specific institutions or locations where scientific magic is taught.`,
            `When Would a Practitioner be Sought Out?: Situations and circumstances that lead people to seek scientific magic users.`,
            `Scientific Institutions: Formal educational and research institutions where scientific magic is studied.`,
            `Research Laboratories: Specialized facilities for conducting magical experiments and studies.`,
            `Scientific Conferences: Events where magical researchers present their findings and exchange knowledge.`,
            `Scholarly Journals: Publications that disseminate magical research and discoveries.`,
            `Cost of Magical Education: Exploring the financial barriers to accessing formal magical education.`,
            `Inclusivity and Diversity: The representation and inclusion of diverse individuals and cultures in magical education.`,
            `Public Perception of Scientific Magic: How the general public views and perceives scientific magic.`,
            `Legal and Regulatory Frameworks: The laws and regulations governing the practice of scientific magic.`,
            `Apprenticeships and Informal Training: The role of informal methods in passing on magical knowledge.`,
            `Access to Magical Resources: Availability and distribution of essential magical resources.`,
            `Remote Learning: The potential for distance magical education.`,
            `Entry Requirements and Admission Criteria: The prerequisites for enrolling in magical educational programs.`,
            `Barriers Faced by Non-Affiliated Practitioners: Challenges encountered by magical practitioners who are not associated with formal institutions.`,
            `Role of Government in Promoting Accessibility: Government initiatives to make magical education more accessible to the population.`,
            `The Future of Magical Education: Speculations on how accessibility might change and improve in the future.`
        ],
        'Mastery' : [ //Mastery within the scientific magical system is achieved through rigorous learning and experimentation. Aspects related to the concept of Mastery in scientific magic include:
            `How is it Learned and Can it be Learned Elsewhere?: The process of learning scientific magic and its potential transferability.`,
            `Is the Idea of a Master Formal or Informal? Can Great Knowledge be Possessed Without Being Respected?: The recognition and respect associated with becoming a master in scientific magic.`,
            `Who is More Respected, Educators or Innovators?: The differing levels of respect for those who excel in teaching and those who drive innovation.`,
            `Can Mastery be Achieved Through Scholarship Without Practical Experience?: Whether theoretical knowledge alone is sufficient for mastery.`,
            `Is Any Aspect Still Theoretical?: Whether certain aspects of scientific magic remain unproven and theoretical.`,
            `Research Collaboration: The importance of collaboration in advancing magical knowledge and discoveries.`,
            `Innovative Breakthroughs: Masters who have achieved groundbreaking discoveries and advancements.`,
            `Pioneering Discoveries: Masters who have made significant contributions to the field of scientific magic.`,
            `Resolving Long-standing Mysteries: Masters who have unraveled age-old magical enigmas and puzzles.`,
            `Mentorship and Apprenticeship: The role of experienced masters in mentoring and guiding aspiring magical researchers.`,
            `Ethical Considerations in Mastery: Exploring the moral and ethical implications of mastering scientific magic.`,
            `Cultural Variations in Magical Mastery: How different cultures perceive and value mastery within their magical systems.`,
            `Mastery Challenges and Obstacles: Discussing the difficulties and challenges faced by individuals on their path to mastery.`,
            `The Role of Failure in Mastery: How failures and mistakes contribute to the learning process and ultimate mastery.`,
            `Mastery and Responsibility: Examining the responsibilities that come with being a master magician.`,
            `Mastery in Multiple Magical Systems: Can a magician achieve mastery in multiple magical disciplines?`,
            `Mastery vs. Power: Distinguishing between mastery of magic and the pursuit of power for personal gain.`,
            `Mastery and Innovation: How mastery can lead to the development of new magical techniques and practices.`,
            `Mastery and the Passage of Time: How the concept of mastery evolves and changes over generations.`,
            `The Influence of Environment on Mastery: How the environment and magical resources available impact the attainment of mastery.`,
            `Mastery and Magical Artifacts: The role of magical artifacts in assisting or hindering the path to mastery.`
        ]
        },
    'Artisan' : {/*Expression and creativity*/
        'Source': [
            // Artisans draw their magical abilities from various creative disciplines known as the 'Source.' Each Source represents a distinct form of expression and creativity. For instance:
            'Music: Artisans who harness the power of music can create harmonies that evoke emotions, influence moods, or even manipulate the natural elements through carefully orchestrated melodies.',
            'Textiles: Weaving intricate patterns into fabrics, skilled Artisans can imbue them with magical properties, like granting protection or enhancing the wearer\'s abilities.',
            'Writing: Words written by Artisans can become enchanted, revealing hidden truths or manifesting the contents of the text in reality.',
            'Sculpting: Master Artisans sculpt statues that come to life, guarding sacred places or assisting in various tasks.',
            'Painting: Paintings can act as portals to other realms, display visions of the past or future, or alter perceptions of reality.',
            'Physical: Artisans with a focus on physical prowess can manipulate their bodies to perform extraordinary feats or enhance their combat skills with magical techniques.',
            'Enchantment: These Artisans specialize in imbuing ordinary objects with magical properties, such as charms, amulets, or enchanted weapons.',
            'Runes: The power of ancient runes allows Artisans to inscribe magical symbols on surfaces or objects, creating spells or altering reality based on the symbols\' meanings.',
            'Potions and Elixirs: Artisans skilled in potion-making can brew concoctions that grant temporary magical abilities, healing, or transformations.',
            'Pottery and Ceramics: Clay objects crafted by Artisans can become vessels of power, storing energy, or serving as conduits for spells.',
            'Glyphs: Artisans use intricate glyphs to shape the flow of magic, directing it for specific purposes or creating magical barriers.',
            'Culinary Arts: Artisans infuse their culinary creations with magic, providing sustenance, healing, or even changing the eater\'s emotions or perceptions.',
            'Glassblowing: Glassblowers create enchanted glass items with unique properties, like revealing truths or concealing secrets.',
            'Tailoring: Clothes tailored by Artisans can provide camouflage, enhance abilities, or even grant temporary transformations.',
            'Architecture: Masterful architectural designs imbue buildings with magical properties, like strength, protection, or illusions.',
            'Metalworking: Artisans work with metals to create enchanted armors, weapons, or intricate mechanisms with magical functions.',
            'Jewelry Crafting: Artisans craft exquisite magical jewelry that enhances the wearer\'s abilities or offers protection.',
            'Woodworking: Woodworkers create enchanted wooden artifacts, such as staves or wands, that amplify their wielder\'s magic.',
            'Performing Arts: Artisans utilizing performing arts can captivate audiences with magical performances, affecting emotions, or even creating illusions.',
            'Clockwork: Artisans create intricate clockwork mechanisms that harness magical energy to perform various functions.',
            'Calligraphy: Master calligraphers use elegant and precise writing to inscribe potent magical scrolls or spellbooks.',
            'Alchemy: Alchemists combine mystical substances to produce powerful elixirs, transmutations, or magical reactions.',
            'Topiary: Artisans skilled in topiary can sculpt living plants into magical shapes or creatures that serve various purposes.',
            'Brewing: Brewmasters create magical brews that grant temporary abilities, foresight, or heightened senses.',
            'Tinkering: Master tinkers craft magical gadgets and inventions that can perform unique tasks or solve intricate problems.',
            'Illusionary Art: Artisans adept in illusionary art can create intricate and convincing illusions that deceive the senses.',
            'Inscription: Artisans use magical inscriptions on objects or surfaces to activate or enhance their properties.',
            'Pyrotechnics: Pyromancers manipulate fire and create mesmerizing firework displays with magical effects.',
            'Cartography: Master cartographers create maps that reveal hidden locations, pathways, or magical phenomena.',
            'Maritime Arts: Artisans skilled in maritime arts can control water currents, summon protective mists, or communicate with sea creatures.',
            'Forgery: Expert forgers create counterfeit magical items or documents with convincing enchantments.',
            'Light Manipulation: Artisans with the power of light can create illusions, manipulate shadows, or reveal hidden truths.',
            'Stone Shaping: Stonemasons can manipulate stone structures, create golems, or meld with stone for protection.',
            'Candlemaking: Master candlemakers produce magical candles that emit unique effects when lit.',
            'Mechanical Automata: Artisans build intricate mechanical automata powered by magic, capable of performing various tasks.',
            'Geomancy: Geomancers tap into the energy of the earth, detecting ley lines, or influencing terrain.',
            'Gardening: Green-thumbs can cultivate enchanted plants with various magical properties.',
            'Taxidermy: Master taxidermists create enchanted taxidermy that can move, speak, or hold magical properties.',
            'Cobbling: Cobblers can create shoes that enhance the wearer\'s abilities, grant stealth, or bestow other magical effects.',
            'Psychometry: Artisans skilled in psychometry can read the history of objects by touching them, uncovering hidden information.',
            'Horology: Horologists craft magical timepieces that manipulate time or provide insights into the future.',
            'Shadows: Manipulating shadows to conceal, travel, or manifest as tangible entities for various purposes.',
            'Feng Shui: Practitioners of Feng Shui can balance and manipulate the flow of energy within spaces for harmonious effects.',
            'Artificial Intelligence: Artisans adept in AI can imbue objects or constructs with artificial intelligence and magical capabilities.',
            'Environmental Art: Creating magical art installations that interact with the environment or amplify natural energies.',
            'Esoteric Symbols: Artisans who specialize in using esoteric symbols to access unique magical powers or dimensions.',
            'Spiritual Callings: Channeling spirits or otherworldly entities to perform magic or gain insights into the supernatural.',
            'Tattooing: Magical tattoos that bestow abilities, protection, or connections to magical realms.',
            'Photography: Artisans who capture magical moments or scenes to reveal hidden truths or capture fleeting enchantments.',
            'Herbology: Herbalists with magical abilities use plants for healing, protection, or creating potions.',
            'Weather Manipulation: Manipulating weather patterns to influence the elements or create magical storms.',
            'Astrology: Reading and influencing fate and energies based on celestial alignments.',
            'Holography: Creating holographic displays that can serve as portals or convey magical information.',
            'Origami: Masterful origamists can fold intricate paper creations with magical properties and applications.',
            'Shadow Puppetry: Artisans who use shadow puppets to cast illusions or tell magical stories.',
            'Mineralogy: Working with crystals and gemstones to harness their magical properties.',
            'Soundscaping: Creating intricate soundscapes that manipulate emotions or alter perceptions.',
            'Dreamweaving: Artisans who can manipulate dreams or enter the dream realm for various purposes.',
            'Time-Lapse Art: Creating art that captures the essence of time and its magical properties.',
            'Hieroglyphics: Artisans proficient in hieroglyphics can decipher ancient magic and create powerful spells.',
            'Cymatics: Using sound vibrations to create magical patterns and manipulate energy.',
            'Metal Engraving: Engraving metal objects with magical symbols or patterns for specific effects.',
            'Entomancy: Artisans working with insects and arachnids to channel their magical properties.',
            'Bonecraft: Crafting magical artifacts or tools from the bones of magical creatures.',
            'Linguistics: Artisans with the power to create new languages or use ancient languages for spells.',
            'Terraforming: Artisans capable of reshaping the environment using magical means.',
            'Holography: Creating holographic displays that can serve as portals or convey magical information.',
            'Bioluminescence: Manipulating bioluminescent organisms to create magical light displays or effects.',
            'Perfumery: Creating enchanted perfumes and scents with various magical properties.',
            'Symbolic Dance: Dance movements and gestures used for spellcasting or invoking specific energies.',
            'Numerology: Using numbers to derive magical meanings and unlock hidden potentials.',
            'Nanomancy: Controlling and manipulating nanoscale particles for magical effects.',
            'Whispers of the Ancients: Artisans who can communicate with ancient spirits and draw power from their guidance.',
            'Aeromancy: Artisans who manipulate air currents for flight, summoning storms, or creating barriers.',
            'Holography: Creating holographic displays that can serve as portals or convey magical information.',
            'Bioluminescence: Manipulating bioluminescent organisms to create magical light displays or effects.',
            'Perfumery: Creating enchanted perfumes and scents with various magical properties.',
            'Symbolic Dance: Dance movements and gestures used for spellcasting or invoking specific energies.',
            'Numerology: Using numbers to derive magical meanings and unlock hidden potentials.',
            'Nanomancy: Controlling and manipulating nanoscale particles for magical effects.',
            'Whispers of the Ancients: Artisans who can communicate with ancient spirits and draw power from their guidance.',
            'Aeromancy: Artisans who manipulate air currents for flight, summoning storms, or creating barriers.',
            'Cosmography: Mapping the magical energies and ley lines of the cosmos.',
            'Veilweaving: Weaving invisible threads of magic to create illusions or concealments.',
            'Holography: Creating holographic displays that can serve as portals or convey magical information.',
            'Bioluminescence: Manipulating bioluminescent organisms to create magical light displays or effects.',
            'Perfumery: Creating enchanted perfumes and scents with various magical properties.',
            'Symbolic Dance: Dance movements and gestures used for spellcasting or invoking specific energies.',
            'Numerology: Using numbers to derive magical meanings and unlock hidden potentials.',
            'Nanomancy: Controlling and manipulating nanoscale particles for magical effects.',
            'Whispers of the Ancients: Artisans who can communicate with ancient spirits and draw power from their guidance.',
            'Veilweaving: Weaving invisible threads of magic to create illusions or concealments.',
            'Candle Carving: Artisans who carve intricate designs into candles to imbue them with magical properties.',
            'Cosmic Symphony: Harnessing celestial harmonies to create magical effects or enhance abilities.',
            `Living Ink: Artisans who create magical inks that respond to the writer's intentions or reveal hidden messages.`,
            'Aether Sculpting: Shaping the mystical substance of aether to create constructs or manipulate energies.',
            'Inkwater Calligraphy: Writing magical symbols or spells on water surfaces to invoke their power.',
            'Quantum Entanglement: Utilizing quantum principles to create instantaneous magical effects.',
            'Memoryscaping: Creating magical landscapes or realms within the minds of others.',
            'Sentient Constructs: Crafting constructs with their own consciousness and magical abilities.',
            'Amorphous Art: Shaping and manipulating magical energies into abstract forms and manifestations.',
            'Biomimicry: Emulating magical properties from the behavior of animals or creatures.',
            'Chromatic Artistry: Manipulating colors and hues to influence emotions or reality.',
            'Spatial Folds: Creating folds in space to teleport, create pockets of space, or access other dimensions.',
            'Vocal Sigils: Crafting magical sigils through vocalizations or chants.',
            'Urban Alchemy: Harnessing the energies of cities and urban environments for magical effects.',
            'Weather Dancing: Performing intricate dances to influence weather patterns or create microclimates.',
            'Interdimensional Sketching: Drawing portals or windows to other dimensions through art.',
            'Aetherial Welding: Joining magical energies together to create powerful constructs or spells.',
            'Electromancy: Controlling electricity and electromagnetic fields for various purposes.',
            'Esoteric Artifacts: Crafting objects with obscure magical properties and hidden purposes.',
            'Spirit Trapping: Containing and using spirits or entities for magical workings.',
            'Cosmic Sketching: Drawing constellations or celestial patterns to influence cosmic energies.',
            'Solar Adornments: Crafting jewelry or objects infused with the power of the sun.',
            'Emotion Tethering: Tethering emotions to objects or people to influence their feelings or actions.',
            'Mirrored Art: Creating magical mirrors that reveal truths or reflect alternate realities.',
            'Bio-Resonance: Creating harmonious connections with living organisms for mutual benefits.',
            'Vein Reading: Reading the magical energies flowing through living beings or objects.',
            'Temporal Sculpture: Creating temporary sculptures that alter time or perception.',
            'Metallurgical Transmutation: Transforming metals to imbue them with magical properties.',
            'Psychic Mosaics: Creating mosaics that channel psychic energy or enhance mental abilities.',
            'Light Sculpting: Sculpting light to create illusions, displays, or protective barriers.',
            'Acoustic Enchantment: Creating magical music and sounds with specific effects or intentions.',
            'Ocular Artistry: Drawing sigils or runes with magical properties that interact with the eyes.',
            'Magical Knots: Using intricately tied knots for various magical purposes.',
            'Psychic Weaving: Weaving psychic energies to influence minds or perform mental feats.',
            'Chaos Sketching: Creating drawings that release chaotic energies when activated.',
            'Temporal Inversion: Temporarily reversing the flow of time for specific purposes.',
            'Elemental Fusion: Combining elemental energies to create new and powerful effects.',
            'Aural Visions: Translating visions or dreams into enchanting auditory experiences.',
            'Memory Infusion: Infusing memories into objects to convey information or emotions.',
            'Ancestral Channeling: Communicating with ancestors for guidance or power.',
            'Dimensional Fabrication: Creating temporary or small-scale dimensional spaces.',
            'Cosmic Luminescence: Manipulating cosmic energies to produce radiant light displays.',
            'Sentient Portraits: Paintings or portraits that hold consciousness or interact with viewers.',
            'Cosmological Erosion: Eroding space or time to access alternate realities.',
            'Morphic Sand Art: Creating sand art that reshapes reality or alters perceptions.',
            'Pyroclastic Art: Sculpting lava or volcanic materials for various effects.',
            'Harmony Harmonics: Using harmonic frequencies to manipulate energy or emotions.',
            'Vortex Manipulation: Creating and controlling magical vortexes or whirlpools.',
            'Occult Typography: Writing in arcane symbols or languages to activate magical effects.',
            'Starforging: Crafting objects infused with starlight and celestial energies.',
            'Psychic Dissonance: Creating disruptions in psychic energies or abilities.',
            'Echoing Whispers: Amplifying or projecting voices for various purposes.',
            'Chrono-Ceramics: Creating time-based constructs with ceramic materials.',
            'Luminary Art: Using luminescent materials to create magical artworks.',
            'Quantum Illumination: Manipulating light particles for dazzling visual effects.',
            'Resonant Architecture: Constructing buildings that resonate with magical energies.',
            'Sonic Sigils: Infusing sound waves with magical symbols or intentions.',
            'Dance of the Zephyr: Dancing with the wind to influence atmospheric phenomena.',
            'Ethereal Glass Art: Creating ethereal sculptures with enchanted glass.',
            'Dream Mosaics: Assembling mosaic pieces to influence dreams or memories.',
            'Cacophonic Enchantment: Using dissonance to create chaotic magical effects.',
            'Spectral Calligraphy: Writing with ghostly or otherworldly energies.',
            'Psychic Tethers: Creating psychic connections between individuals or objects.',
            'Mindscapes: Crafting mental landscapes for exploration or healing.',
            'Runic Astronomy: Mapping the stars to reveal arcane connections and patterns.',
            'Fae Glammer: Creating illusory appearances or hiding magical features.',
            'Enchanted Spectacles: Crafting glasses or lenses with magical properties.',
            'Clockwork Symphony: Orchestrating mechanical wonders for magical effects.',
            'Vitreous Runes: Inscribing magical symbols on glass for various purposes.',
            'Entheogenic Art: Creating art infused with plant-based hallucinogenic magic.',
            'Horizon Sculpting: Sculpting the horizon to create optical illusions.',
            'Levity Calligraphy: Writing that lightens emotions or mood.',
            'Astral Scribing: Drawing symbols that connect with astral planes.',
            'Eclipse Craft: Harnessing the power of eclipses for magical workings.',
            'Tempo Infusion: Infusing objects or people with specific rhythms for effects.',
            'Primordial Painting: Creating artworks with the power of primordial elements.',
            'Terra Melody: Using melodies to influence nature and earth energies.',
            'Arcane Sculpture: Creating sculptures with magical properties or sentience.',
            'Abyssal Tapestry: Weaving shadows and darkness for various magical purposes.',
            'Magnetic Calligraphy: Writing with magnetic forces for manipulation or control.',
            'Sonic Dispersion: Dispersing sound waves to create magical effects.',
            'Veil-Carved Masks: Creating masks that hide or enhance magical identities.',
            'Leyline Tapping: Harnessing the power of ley lines for magical energy.',
            'Heliographic Enchantment: Enchanting objects with solar energy.',
            'Chrono-Choreography: Creating temporal dances that manipulate time.',
            'Prismatic Lenses: Crafting lenses to manipulate light and colors.',
            'Luminous Glyphs: Inscribing glowing symbols with specific magical meanings.',
            'Quantum Animation: Animating objects with quantum forces or effects.',
            'Resonant Ceremonies: Performing ceremonies that resonate with magic.',
            'Specter Writings: Writing that interacts with or attracts spirits.',
            'Liminal Architecture: Designing structures on the borders of reality.',
            'Amplification Resonance: Amplifying magical energies through resonance.',
            'Astral Embroidery: Using embroidery to connect with astral energies.',
            'Vibrational Choreography: Dancing to manipulate vibrations and frequencies.',
            'Nebulaic Illumination: Capturing nebulae patterns to infuse objects with magic.',
            'Essence Vessels: Crafting containers to capture and store magical essence.',
            'Aureate Calligraphy: Writing in gold or metallic inks for potent spells.',
            'Kinetic Glyphs: Using kinetic energy to activate magical symbols.',
            'Crystal Resonance: Using crystals to amplify or focus magical energies.',
            'Solar Flare Artistry: Capturing solar flares to empower artwork with magic.',
            'Temporal Assemblage: Creating temporal constructs from scattered fragments.',
            'Shadow Manipulation: Controlling shadows for concealment or as weapons.',
            'Tome Artifice: Creating magical tomes or books with unique properties.',
            'Morphic Metallurgy: Shaping metal to change its form or properties.',
            'Rainbow Illumination: Using the full spectrum of colors for magical effects.',
            'Telepathic Frescoes: Painting frescoes that convey telepathic messages.',
            'Harmonic Energetics: Utilizing harmonics to align or redirect energy.',
            'Resonating Totems: Crafting totems that resonate with spiritual forces.',
            'Nebulic Sculpture: Sculpting nebulous shapes that shift and change.',
            'Choreography of Dreams: Dancing to control or influence dreams.',
            'Luminescent Tapestry: Weaving light into magical tapestries.',
            'Planar Pictograms: Drawing symbols that connect with other planes.',
            'Astrolabe Craft: Constructing astrolabes to read cosmic patterns.',
            'Arcane Weathervanes: Creating weathervanes to harness weather magic.',
            'Cathedral Magic: Designing cathedrals with magical motifs and intentions.',
            'Shadow Casting: Using shadows to create illusions or weaken opponents.',
            'Resonating Ink: Using inks that vibrate with magical power.',
            'Ancestral Portraits: Painting portraits infused with ancestral energies.',
            'Prismatic Enchantment: Infusing objects with multifaceted magical effects.',
            'Quantum Etchings: Etching magical symbols that interact with quantum energies.',
            'Ethereal Sculpture: Sculpting with otherworldly or ethereal substances.',
            'Phantasmal Symphony: Conducting musical illusions with ghostly sounds.',
            'Holographic Scribing: Writing that appears holographic under certain conditions.',
            'Chrono-Botany: Manipulating plant growth through time manipulation.',
            'Cerulean Glyphs: Inscribing symbols that harness the power of water.',
            'Sonic Constructs: Creating physical constructs through sound manipulation.',
            'Astral Manuscripts: Writing manuscripts that connect with the astral plane.',
            'Aetherial Marquetry: Crafting marquetry with otherworldly materials.',
            'Eidos Dance: Dancing to alter the fundamental nature of objects or phenomena.',
            'Mystic Pyrotechnics: Creating fireworks with magical effects and patterns.',
            'Spectral Threads: Weaving threads that connect with the spirit realm.',
            'Harmonious Geometry: Designing structures with harmonizing shapes and angles.',
            'Echo Chamber Enchantment: Using sound chambers for amplification or focus.',
            'Temporal Crescendo: Building up magical energy over time for powerful effects.',
            'Chromatic Aura: Radiating colored auras to indicate magical properties.',
            'Aurelian Constructs: Creating constructs infused with golden light.',
            'Lunar Engravings: Engraving symbols that harness the power of the moon.',
            'Resonant Portals: Creating portals that resonate with specific energies.',
            'Veil Evasion: Using illusions to evade detection or physical obstacles.',
            'Echo Casting: Casting spells that leave lingering echoes or reverberations.',
            'Prismatic Essences: Channeling the essence of colors for magical effects.',
            'Enchanted Frescoes: Painting frescoes that tell magical stories or histories.',
            'Spectral Glassblowing: Creating glass objects that interact with the spirit world.',
            'Harmonic Divination: Using harmonic frequencies for divinatory purposes.',
            'Resonance Infusion: Infusing objects with specific resonances for effects.',
            'Temporal Stasis: Temporarily freezing time in a localized area.',
            'Geomantic Sketching: Drawing symbols that interact with the earth\'s energies.',
            'Auroral Enchantment: Enchanting objects with ethereal lights and auras.',
            'Leyline Harmonics: Using sound or music to tap into leyline energies.',
            'Chrono-Textiles: Weaving fabrics that manipulate time or temporal energies.',
            'Morphic Ink: Using ink that can change or morph into different patterns.',
            'Phantom Artifacts: Crafting objects that appear and disappear at will.',
            'Spectral Choreography: Performing dances that summon or control spirits.',
            'Aetherial Glyphs: Inscribing symbols that tap into the aetheric plane.',
            'Harmony of Embers: Controlling and manipulating ember-based magic.',
            'Cosmic Mandala: Creating magical mandalas with cosmic symbols and patterns.',
            'Resonant Emanations: Emitting magical resonances for various purposes.',
            'Echoing Engravings: Engraving objects that produce echo-like effects.',
            'Timepiece Artistry: Creating clocks or timepieces with magical properties.',
            'Spectral Call: Creating sounds that attract or interact with spirits.',
            'Ethereal Embroidery: Using embroidery to weave spells or protective wards.',
            'Prism Craft: Creating prisms to refract and manipulate light energies.',
            'Quantum Sigils: Creating sigils that interact with quantum mechanics.',
            'Astral Ceramics: Crafting ceramics that connect with the astral realm.',
            'Ethereal Dance: Dancing to access ethereal or otherworldly energies.',
            'Cacophonic Conduction: Using dissonant sounds to manipulate energies.',
            'Geomantic Pottery: Creating pottery that resonates with earth energies.',
            'Chrono-Photography: Capturing temporal images or visions through photography.',
            'Aetherial Serenade: Singing or playing music that taps into aetheric energies.',
            'Harmonic Engravings: Engraving objects with harmonic patterns and symbols.',
            'Vitric Spellwork: Infusing glass objects with magical intentions and properties.',
            'Cosmic Filigree: Crafting delicate filigree with cosmic motifs and designs.',
            'Shadow Weaver: Weaving shadows to cloak or disguise objects or people.',
            'Temporal Glyphs: Inscribing symbols that manipulate time or temporal phenomena.',
            'Auroral Borealis: Creating magical displays inspired by the aurora borealis.',
            'Luminous Sculpture: Sculpting magical forms that emit their own light.',
            'Whispering Wind: Using wind to carry messages or magical effects.',
            'Resonant Totems: Crafting totems that resonate with elemental energies.',
            'Spectral Illumination: Creating ghostly lights and illuminations.',
            'Auric Brushwork: Painting with colors that represent different auras or energies.',
            'Chrono-Metallurgy: Shaping metal through time manipulation.',
            'Ephemeral Melodies: Composing melodies that evoke transient emotions or effects.',
            'Prismatic Calligraphy: Writing with colors that shimmer and change.',
            'Quantum Mechanisms: Creating machines with quantum-based effects.',
            'Astral Threads: Weaving threads that connect with the astral plane.',
            'Ethereal Pyrotechnics: Creating firework displays with otherworldly lights.',
            'Spectral Harmony: Conducting music that resonates with the spirit world.',
            'Aurelian Filigree: Crafting delicate filigree with golden motifs and designs.',
            'Ceremonial Glyphs: Inscribing symbols that activate during rituals.',
            'Resonating Shadows: Using shadows to carry or amplify magical effects.',
            'Luminous Enchantment: Infusing objects with radiant, glowing magic.',
            'Morphic Murals: Creating murals that change or morph over time.',
            'Phantom Orchestration: Conducting orchestras of ghostly musicians.',
            'Veil of Illusion: Using illusions to create barriers or cloaking effects.',
            'Echolocation Artistry: Using sound to navigate or perceive surroundings.',
            'Prismatic Reflections: Using mirrors to manipulate light and energies.',
            'Quantum Sculpture: Creating sculptures that interact with quantum states.',
            'Astral Stained Glass: Crafting stained glass that connects with the astral plane.',
            'Ethereal Vortex: Creating swirling vortexes of otherworldly energies.',
            'Spectral Warding: Using spectral energies to create protective wards.',
            'Aureate Symphony: Conducting orchestras with golden and radiant instruments.',
            'Chrono-Photonic Art: Creating images that capture the essence of time.',
            'Resonant Engravings: Engraving objects with harmonizing patterns.',
            'Whispers of Nature: Communicating with plants and animals through whispers.',
            'Spectral Animations: Creating animated scenes with ghostly characters.',
            'Astral Lacework: Weaving lace with patterns that connect with the astral plane.',
            'Ethereal Projection: Projecting one\'s consciousness to other realms or planes.',
            'Prismatic Illusions: Creating illusions with shifting colors and shapes.',
            'Quantum Sorcery: Practicing sorcery that exploits quantum phenomena.',
            'Temporal Origami: Folding paper to create time-based constructs.',
            'Vivid Entropy: Creating dynamic artwork that captures the essence of change.',
            'Ephemeral Calligraphy: Writing with disappearing or transient inks.',
            'Spectral Enchantment: Infusing objects with ethereal and ghostly magic.',
            'Auric Energetics: Harnessing the power of auras for magical effects.',
            'Chrono-Mechanics: Creating mechanical devices that manipulate time.',
            'Resonating Chimes: Using chimes or bells for harmonizing effects.',
            'Windwhisper Art: Drawing intricate patterns that interact with the wind.',
            'Astral Forge: Crafting weapons and tools that resonate with astral energies.',
            'Ethereal Masquerade: Wearing masks that alter perceptions or identities.',
            'Prismatic Ink: Using ink that changes colors under different lights.',
            'Quantum Conjuring: Summoning creatures or objects from quantum states.',
            'Temporal Murals: Creating murals that depict scenes from different eras.',
            'Vortex Projection: Projecting images or energies through vortexes.',
            'Spectral Elegy: Composing mournful melodies to communicate with spirits.',
            'Aurelian Architecture: Designing structures with golden proportions and motifs.',
            'Chromatic Symphony: Conducting musical performances with vibrant colors.',
            'Whispers of the Elements: Communicating with the elements through whispers.',
            'Temporal Incantations: Using time-based incantations to cast spells.',
            'Ethereal Filigree: Crafting delicate filigree with ethereal motifs and designs.',
            'Prismatic Arcana: Utilizing arcana that draws power from the colors of the spectrum.',
            'Quantum Sketching: Drawing images that shift and change as observed.',
            'Astral Projection: Projecting one\'s consciousness to other realms or planes.',
            'Ephemeral Illumination: Creating temporary light displays or illusions.',
            'Spectral Illuminations: Using light to reveal or communicate with spirits.',
            'Aura Alchemy: Manipulating auras for various magical purposes.',
            'Chrono-Orchestration: Conducting orchestras with time-manipulating effects.',
            'Resonant Chants: Using chants or mantras for harmonizing or focusing energy.',
            'Windwhisper Art: Drawing intricate patterns that interact with the wind.',
            'Astral Forge: Crafting weapons and tools that resonate with astral energies.',
            'Ethereal Masquerade: Wearing masks that alter perceptions or identities.',
            'Prismatic Ink: Using ink that changes colors under different lights.',
            'Quantum Conjuring: Summoning creatures or objects from quantum states.',
            'Temporal Murals: Creating murals that depict scenes from different eras.',
            'Vortex Projection: Projecting images or energies through vortexes.',
            'Spectral Elegy: Composing mournful melodies to communicate with spirits.',
            'Aurelian Architecture: Designing structures with golden proportions and motifs.',
            'Chromatic Symphony: Conducting musical performances with vibrant colors.',
            'Whispers of the Elements: Communicating with the elements through whispers.',
            'Temporal Incantations: Using time-based incantations to cast spells.',
            'Ethereal Filigree: Crafting delicate filigree with ethereal motifs and designs.',
            'Prismatic Arcana: Utilizing arcana that draws power from the colors of the spectrum.',
            'Quantum Sketching: Drawing images that shift and change as observed.',
            'Ephemeral Illumination: Creating temporary light displays or illusions.',
            'Spectral Illuminations: Using light to reveal or communicate with spirits.',
            'Aura Alchemy: Manipulating auras for various magical purposes.',
            'Chrono-Orchestration: Conducting orchestras with time-manipulating effects.',
            'Resonant Chants: Using chants or mantras for harmonizing or focusing energy.',
            'Astral Tapestry: Weaving tapestries that depict astral scenes or journeys.',
            'Ethereal Quill: Writing with a quill that produces ethereal or magical ink.',
            'Prismatic Murmurs: Creating soundscapes with harmonizing colors.',
            'Quantum Weaving: Weaving fabrics with quantum properties or patterns.',
            'Temporal Infusions: Infusing objects with temporal or time-based properties.',
            'Vortex Navigation: Using vortexes to traverse dimensions or planes.',
            'Spectral Tracery: Creating patterns that channel spectral or ghostly energies.',
            'Aurelian Glyphs: Inscribing symbols that resonate with golden energies.',
            'Chromatic Calligraphy: Writing with vibrant colors and changing hues.',
            'Whispers of the Spirits: Communicating with spiritual entities through whispers.',
            'Elemental Resonance: Harmonizing with the elements for magical effects.',
            'Windwhisper Architecture: Designing structures to interact with wind energies.',
            'Temporal Sculpture: Sculpting with time-manipulating materials.',
            'Prismatic Etching: Etching images that shift and change with light.',
            'Quantum Sculpting: Creating sculptures with quantum properties.',
            'Astral Luminance: Creating light displays infused with astral energy.',
            'Ethereal Conduction: Conducting ethereal energies through objects.',
            'Spectral Convergence: Merging spectral energies for amplified effects.',
            'Aura Weaving: Manipulating auras to create protective barriers or shields.',
            'Chrono-Chromatic Art: Painting with colors that represent different time periods.',
            'Resonant Divination: Using resonance for enhanced divinatory abilities.',
            'Astral Glyphs: Inscribing symbols that connect with the astral plane.',
            'Ephemeral Enchantment: Infusing objects with transient or fleeting magic.',
            'Prismatic Rituals: Conducting rituals that involve harmonizing colors.',
            'Quantum Illuminations: Creating light displays that play with quantum effects.',
            'Temporal Verse: Composing poetic verses that manipulate time or perception.',
            'Vortex Binding: Using vortexes to bind or imprison entities or energies.',
            'Spectral Engravings: Engraving objects with ghostly or ethereal images.',
            'Aurelian Conjuring: Summoning creatures or entities through golden rituals.',
            'Chromatic Illusions: Creating illusions with shifting colors and patterns.',
            'Whispers of the Stars: Communicating with celestial beings through whispers.',
            'Windwhisper Calligraphy: Writing with strokes that dance with the wind.',
            'Temporal Alchemy: Practicing alchemy with time-related materials or processes.',
            'Prismatic Divination: Using crystals with prismatic properties for divination.',
            'Quantum Embroidery: Creating embroidered patterns that shift and change.',
            'Astral Alloys: Crafting alloys infused with astral or otherworldly properties.',
            'Ethereal Weaving: Weaving fabrics with ethereal or otherworldly threads.',
            'Spectral Animancy: Animating objects with spectral or ghostly energies.',
            'Aura Infusion: Infusing objects with specific auras for magical effects.',
            'Chrono-Poetry: Composing poems that manipulate time or time perception.',
            'Resonating Prisms: Using prisms to manipulate and focus magical energies.',
            'Astral Artifacts: Crafting artifacts with connections to the astral plane.',
            'Ephemeral Sculpture: Creating temporary sculptures that shift or vanish.',
            'Prismatic Rituals: Conducting rituals that involve harmonizing colors.',
            'Quantum Illuminations: Creating light displays that play with quantum effects.',
            'Temporal Verse: Composing poetic verses that manipulate time or perception.',
            'Vortex Binding: Using vortexes to bind or imprison entities or energies.',
            'Spectral Engravings: Engraving objects with ghostly or ethereal images.',
            'Aurelian Conjuring: Summoning creatures or entities through golden rituals.',
            'Chromatic Illusions: Creating illusions with shifting colors and patterns.',
            'Whispers of the Stars: Communicating with celestial beings through whispers.',
            'Elemental Manipulation: Using the elements to influence surroundings or events.',
            'Auroral Pyrotechnics: Creating fireworks that display the colors of the aurora borealis.',
            'Windwhisper Glyphs: Inscribing symbols that harness the power of the wind.',
            'Temporal Crescendo: Building up magical energy over time for powerful effects.',
            'Prismatic Sketching: Drawing images with vibrant and shifting colors.',
            'Quantum Inlays: Inlaying objects with materials that exhibit quantum properties.',
            'Astral Ceramics: Crafting ceramics that connect with the astral realm.',
            'Ethereal Sculpture: Sculpting with otherworldly or ethereal substances.',
            'Spectral Aria: Singing or playing music to communicate with spirits.',
            'Aura Harmonics: Using harmonics to attune or resonate with auras.',
            'Chrono-Graphics: Creating visual representations of time and its flows.',
            'Resonant Mosaics: Creating mosaics that resonate with specific energies.',
            'Astral Ephemera: Crafting objects that can only be seen in the astral plane.',
            'Windwhisper Symphony: Conducting orchestras with music inspired by the wind.',
            'Temporal Glyphs: Inscribing symbols that manipulate time or temporal phenomena.',
            'Astral Vortex: Creating swirling vortexes of astral or otherworldly energies.',
            'Ethereal Embroidery: Using embroidery to weave spells or protective wards.',
            'Spectral Conduction: Conducting spectral energies through objects or mediums.',
            'Aura Attunement: Attuning oneself to different auras for specific purposes.',
            'Chrono-Chromatic Art: Painting with colors that represent different time periods.',
            'Resonant Divination: Using resonance for enhanced divinatory abilities.'
        ],
        'Cost': [
            // To wield their magical abilities, Artisans must pay certain costs. These costs represent the investment of energy and resources required for their magic to work effectively. Some examples include:
            'Time: Artisan magic often requires significant time to perform rituals, craft objects, or perfect their skills.',
            'Strain: Harnessing powerful magic can place physical and mental strain on the Artisan.',
            `Emotions: Strong emotions may fuel or hinder an Artisan's magical abilities, making emotional control essential.`,
            'Intricacy: Complex magical works demand precision and attention to detail.',
            'Material: Enchanting objects often requires rare or specific materials with inherent magical properties.',
            'Focus: Concentration and focus are vital for channeling magic accurately.',
            'Personal Sacrifice: Some potent spells might require the Artisan to sacrifice something significant to activate them.',
            'Spirituality: Connection with the spiritual realm may be necessary to access certain magical abilities.',
            'Perfectionism: Pursuit of perfection may lead to more potent and refined magical creations.',
            'Patience: Achieving desired magical results may require the Artisan to wait for the right moment or conditions.',
            'Sleep Deprivation: Staying awake for extended periods to complete intricate magical works.',
            'Disconnection: Maintaining distance from personal relationships to avoid their interference with magic.',
            'Energy Conservation: Balancing magical output to prevent physical and mental exhaustion.',
            'Secret Keeping: Concealing arcane knowledge or magical works to protect them from misuse.',
            'Cultural Obligations: Fulfilling cultural duties or rituals as part of magical practices.',
            'Dealing with Spirits: Negotiating with spirits or entities for assistance in magic, requiring offerings or favors.',
            'Risk of Backlash: Powerful magic may have unintended consequences or magical backlash.',
            'Learning from Failure: Overcoming the setbacks and failures that come with mastering magical arts.',
            'Borrowed Power: Drawing energy from external sources, such as ley lines or natural phenomena.',
            `Life's Essence: Using life force or part of the Artisan's essence to fuel potent magic.`,
            'Challenges of Permanence: Ensuring lasting magical effects without causing harm or imbalance.'
        ],
        'Potency': [
            // The potency of Artisan magic depends on various factors, which determine how powerful and effective their spells or creations can be. Some factors influencing potency include:
            `Practice: Regular practice hones an Artisan's skills and makes their magic more potent.`,
            'Creativity: Uniqueness and originality in magical works can enhance their impact.',
            'Education: Knowledge of magical theory and history can improve magical prowess.',
            'Materials: High-quality and rare materials may amplify the power of enchanted objects.',
            'Intimacy: A strong emotional connection to their creations can enhance their magical potential.',
            `Passion: Deep passion for their art fuels an Artisan's magic.`,
            'Inspiration: Moments of inspiration can lead to breakthroughs in magical abilities.',
            'Collaboration: Working with other skilled practitioners can yield powerful cooperative magic.',
            `Audience Response: The reaction of the audience to performing Arts can influence the magic's impact.`,
            'Precision: Highly precise craftsmanship enhances the magical properties of Artisan creations.',
            'The Source of Inspiration: Gaining magical power from a specific muse or source of inspiration.',
            'Hidden Techniques: Secret techniques passed down through Artisan lineages for heightened potency.',
            'Cultural Significance: Artisan magic intertwined with the cultural identity of certain groups.',
            `The Master's Touch: The touch of a master Artisan infuses their creations with potent magic.`,
            'Alignment with Elementals: Harmonizing with elemental spirits to empower elemental-based creations.',
            'Living Art: Magic infused into living creations, such as animated sculptures or enchanted flora.',
            'Concealed Artistry: Concealing powerful spells within seemingly ordinary artistic works.',
            'The Ephemeral: Channeling transient emotions or moments to create fleeting yet potent magic.',
            'Signature Style: Artisans may develop a unique signature style that amplifies their magical works.',
            'History and Legacy: Tapping into the history and legacy of past master Artisans for added potency.',
            'Arcane Amplification: Enhancing Artisan magic by tapping into arcane energies or ley lines.',
            'Artistic Fusion: Blending multiple artistic disciplines to create profoundly potent magic.'
        ],
        'Accessibility': [
            // The accessibility of Artisan magic describes how easily it can be accessed or utilized within the society or magical world. Various factors influence its accessibility, such as:
            'Beliefs or Superstitions: Cultural beliefs and superstitions may shape the perception and acceptance of Artisan magic.',
            `Dependant: The "${buildClass()}" profession heavily relies on this magic.`,
            'Societal Impact: The societal impact of Artisan magic can determine its acceptance or restrictions.',
            'Unique Offerings: Artisans may provide magical services or objects that other practitioners cannot replicate.',
            'Learning Opportunities: The availability of places or institutions to learn Artisan magic.',
            'Seeking Practitioners: People might seek out Artisans for their magical expertise in specific situations or needs.',
            'Artisan Guilds: Guilds may exist to support and regulate Artisan magic.',
            'Hidden Workshops: Secretive or secluded workshops where Artisans practice their craft away from the public eye.',
            'Mentorship Tradition: Artisans may pass down their knowledge through mentorship.',
            'Public Competitions: Competitions can showcase and celebrate Artisan talents.',
            'Mystical Apprenticeship: Seeking out and being chosen by a master Artisan for specialized training.',
            'Artisan Marketplaces: Venues where Artisans display and trade their magical creations.',
            'Entwined with Trade: Artisan magic is an integral part of trade and commerce in certain regions.',
            'Artisan Legacies: Ancient artifacts or creations left behind by legendary Artisans.',
            'Elite Patronage: Artisans receiving support and protection from powerful patrons.',
            'Cultural Heritage: Artisan magic deeply embedded in the culture and traditions of specific societies.',
            'Artisan Festivals: Celebratory events showcasing the achievements of Artisans.',
            'Inherited Workshops: Families passing down magical workshops through generations.',
            'Artisan Contests: Competitive events where Artisans prove their skill and gain recognition.'
        ],
        'Mastery': [
            // Mastery in Artisan magic refers to achieving the highest level of skill and expertise within a particular Source or discipline. Several aspects define the concept of Mastery for Artisans, including:
            'Permanence or Fluctuation: Whether mastery is a permanent state or fluctuates as the individual evolves.',
            'Inflexible Foundations or Subjective Creativity: Whether mastery is achieved through strict adherence to rules and foundations or through unique and creative approaches.',
            'Limitations for Potency: Whether master Artisans face similar limitations as other practitioners or can transcend them.',
            'Influence through Work or Teaching: Whether a master Artisan\'s impact is more significant through their own creations or their teaching of others.',
            'Aspects that Cannot be Taught: Certain aspects of Artisan magic might be innate or deeply personal, making them difficult to teach.',
            'Legacy of Masters: The influence and contributions of past master Artisans in shaping the magical world.',
            'Innovations of Masters: How master Artisans push the boundaries of their Source, creating new techniques or spells.',
            'Legendary Artisans: Artisans who reach legendary status due to their immense skill and contributions.',
            'Sought After as Teachers: As master Artisans, they become highly sought-after mentors for aspiring practitioners.',
            'Influence of Masterpieces: Masterpieces created by these artisans can have profound effects on the magical world and future generations.',
            'Transcending Tradition: Master Artisans who go beyond conventional practices, developing new schools or disciplines within their Source.',
            'Artisan Guilds: Secretive organizations where master Artisans exchange knowledge and refine their craft.',
            `Masters' Duels: Competitions or duels between master Artisans to showcase their skill and establish dominance.`,
            'Masters of Fusion: Those who masterfully combine multiple Sources to create unique and potent magical effects.',
            'Restoration of Lost Arts: Master Artisans who resurrect ancient magical techniques lost to time.',
            'Artisan Enclaves: Hidden communities where master Artisans live and practice their craft away from the world.',
            'Symbiotic Relationships: Master Artisans forming bonds with magical creatures to enhance their abilities.',
            'Artisan Epics: Legends and tales chronicling the journeys and accomplishments of master Artisans.'
        ]
        },
    'Arcane' : { /*Knowledge, Power, and experience beyond the mundane - magic by its own merit*/
        'Source' : [ 
            //The 'Arcane' magical system draws its power from diverse and esoteric sources, representing knowledge, power, and experiences beyond the mundane. These sources include:
            `Birthright: Some individuals are born with innate magical abilities, inheriting them from their bloodline or heritage.`,
            `Truth: Unraveling the mysteries of the universe and understanding fundamental truths can grant access to arcane powers.`,
            `Emblems: Symbols or emblems that hold ancient and potent arcane energies can be used for magical purposes.`,
            `Scholarship: Extensive study and knowledge in various arcane disciplines provide access to magical abilities.`,
            `Granted: Arcane abilities may be bestowed upon individuals by higher beings or entities.`,
            `Reservoir: Drawing power from personal or external reservoirs allows for the manipulation of arcane energies.`,
            `Lost Texts: Ancient texts containing forgotten or forbidden knowledge can unlock arcane potential.`,
            `Cosmic Entities: Forging pacts or connections with cosmic entities can grant access to their arcane powers.`,
            `Astral Realm: Tapping into the astral realm enables practitioners to harness its energies for magical feats.`,
            `Mystic Artifacts: Powerful artifacts with arcane properties can be used for magical purposes.`,
            `Dreams and Visions: Mystical dreams or visions can reveal arcane insights and grant magical abilities.`,
            'Sacrificial Rites: Performing intricate rituals involving sacrifices can unlock arcane powers.',
            'Dimensional Gateways: Opening portals to other dimensions for arcane knowledge and energies.',
            'Spiritual Ascension: Attaining spiritual enlightenment can lead to unlocking hidden arcane potential.',
            'Time Dilation: Manipulating time and temporal energies to perform arcane feats.',
            'Quantum Entanglement: Harnessing the connections between particles for powerful arcane effects.',
            'Occult Symbols: Utilizing secret and arcane symbols to channel mystical energies.',
            'Energy Leylines: Tapping into the flow of natural energy leylines for potent magic.',
            `Karmic Bonds: The alignment of one's karma with the cosmic forces to access arcane abilities.`,
            'Runic Inscriptions: Using ancient runic symbols to evoke arcane powers.',
            'Ancestral Guidance: Seeking guidance from ancestors to unlock arcane potential.',
            'Ethereal Conduits: Establishing connections with ethereal beings for arcane knowledge.',
            'Akashic Records: Accessing the cosmic records of all knowledge and history for arcane insights.'
        ],
        'Cost': [
            // Utilizing the arcane magic often demands sacrifices or costs from the practitioner. These costs can include:
            'Memory: Arcane magic may require the practitioner to forget or sacrifice memories to fuel spells or rituals.',
            `Vitality: Harnessing arcane energies can drain the practitioner's physical or mental vitality.`,
            'Ritual: Performing elaborate rituals or ceremonies is necessary for certain arcane practices.',
            `Mortality: Some arcane spells or abilities might come at the risk of the practitioner's life or well-being.`,
            'Sacrifice: Making significant sacrifices, like offering possessions or life-force, may unlock potent magic.',
            'Ancestral Connections: Connecting with ancestral spirits or entities can require offerings or services.',
            'Psychic Strain: Handling powerful arcane energies can cause mental strain or even psychic backlash.',
            'Time and Effort: Mastering arcane arts often demands immense time and effort from the practitioner.',
            'Arcane Debt: Utilizing arcane powers may create a debt to cosmic forces or entities.',
            'Ethereal Imbalance: Drawing too much from the ethereal realm can lead to disconnection from reality.',
            'Emotional Turmoil: Emotional control and balance may be challenged when wielding arcane magic.',
            'Forbidden Knowledge: Unraveling dark or forbidden knowledge can exact a high price.',
            'Interdimensional Strain: Traveling through dimensions may put immense strain on the practitioner.',
            'Reality Paradox: Altering reality can lead to unforeseen consequences or paradoxes.',
            'Cosmic Toll: Arcane spells that tap into cosmic energies may have cosmic consequences.',
            'Astral Projection: Projecting the astral self can risk separation from the physical body.',
            'Karmic Backlash: Arcane actions may attract karmic repercussions in return.',
            'Binding Contracts: Forging pacts or contracts with entities for power may have binding consequences.',
            'Temporal Displacement: Manipulating time can cause temporal disorientation and dislocation.',
            'Existential Uncertainty: Exploring the boundaries of existence may lead to existential challenges.',
            `Eldritch Taint: Prolonged exposure to eldritch magic can leave a taint on the practitioner's soul.`,
            'Mystical Oaths: Taking sacred oaths to access arcane abilities may come with severe consequences.'
        ],
        'Potency': [
            // The potency of arcane magic refers to the strength and effectiveness of spells and abilities. The factors determining potency include:
            'Age: Ancient or elder practitioners may have access to more potent and profound arcane knowledge, or the age of the materials used in the magic.',
            'Will: The strength of an individual\'s willpower and determination can amplify their arcane abilities.',
            'Birthright: Innate abilities inherited from a powerful arcane lineage can bestow inherent potency.',
            'Knowledge: In-depth knowledge of arcane lore and principles can lead to more potent magic.',
            'Secrecy: Arcane secrets known only to a select few can hold immense potency.',
            'Mystical Significance: Magical locations or times with cosmic significance can amplify arcane powers.',
            'Manipulating Cosmic Energies: The ability to manipulate cosmic forces can enhance the potency of spells.',
            'Channeling Ethereal Forces: Connecting with ethereal beings can grant access to potent arcane energies.',
            'Unlocking Hidden Potential: Uncovering hidden abilities or potential within oneself can increase potency.',
            'Eldritch Focus: The use of powerful or unique arcane foci can amplify the potency of spells.',
            'Cosmic Conjunctions: The alignment of cosmic bodies can temporarily surge arcane potency.',
            'Ley Lines Attunement: Practitioners attuned to ley lines may wield greater magical power.',
            `Arcane Alignment: Aligning one's intentions with the arcane forces increases potency.`,
            'Sacred Geometry: Utilizing intricate geometric patterns can enhance magical efficacy.',
            'Quantum Manipulation: Understanding and manipulating quantum phenomena can boost potency.',
            'Spiritual Nexus: Tapping into spiritual energy centers increases arcane power.',
            'Astral Harmonization: Harmonizing with the astral plane enhances spellcasting prowess.',
            'Mana Resonance: Resonating with abundant mana sources amplifies magical potential.',
            'Cosmic Insights: Gaining insights into the mysteries of the cosmos boosts arcane potency.',
            'Synchronicity: Being in sync with cosmic rhythms heightens magical effectiveness.',
            'Metaphysical Mastery: Profound understanding of metaphysical principles enhances potency.',
            'Arcane Augmentation: Enhancing spells through infusion with rare magical materials.',
            'Convergence of Realms: Accessing the overlap of multiple realms amplifies magical abilities.',
            'Time Dilation: Temporal manipulation can extend the duration and impact of spells.',
            'Quantum Entanglement: Utilizing quantum entanglement to influence multiple targets.',
            'Divine Blessings: Divine favor can bestow greater potency upon arcane practitioners.'
        ],
        'Accessibility': [
            // The accessibility of arcane magic addresses how readily it can be accessed or learned within the society or magical world. Factors impacting its accessibility include:
            'Beliefs or Superstitions: Cultural beliefs and superstitions may shape how arcane magic is perceived and accepted.',
            `Dependant: The "${buildClass()}" profession heavily relies on this magic.`,
            'Societal Impact: The impact of arcane magic on society may influence its acceptance or regulation.',
            'Unique Offerings: Arcane practitioners may provide magical services or knowledge that others cannot replicate.',
            'Learning Opportunities: Availability of places or institutions to learn arcane magic.',
            'Seeking Practitioners: People might seek out arcane practitioners for their expertise in specific magical matters.',
            'Mysterious Arcane Guilds: Secretive guilds or organizations that hold knowledge and training in arcane arts.',
            'Hidden Orders of Sages: Enigmatic groups of sages or scholars who safeguard arcane knowledge.',
            'Eldritch Nexus Locations: Specific places where the veil between dimensions is thin, enhancing arcane powers.',
            'Celestial Conjunctions: Rare celestial events that can temporarily amplify arcane abilities.',
            'Profound Initiation Rites: Arcane magic may require arduous and secretive initiation rites to access its full potential.',
            'Eccentric Mentors: Eccentric and reclusive mentors may teach the ways of arcane magic to chosen students.',
            'Sacrificial Offering: Accessing hidden libraries of arcane knowledge may require a personal sacrifice.',
            'Forbidden Libraries: Arcane knowledge locked away in forbidden libraries accessible to only a few.',
            'Arcane Puzzles: Solving arcane puzzles and riddles to gain access to magical teachings.',
            'Dimensional Travel: Accessing other planes of existence to acquire elusive arcane wisdom.',
            'Legacy Artifacts: Unearthing powerful artifacts that bestow arcane knowledge and abilities.',
            'Fateful Encounters: Chance meetings with mysterious beings that grant knowledge of arcane secrets.',
            'Arcane Prophecies: Fulfilling arcane prophecies to unlock hidden magical potential.',
            'Elemental Attunement: Forging a bond with elemental spirits to gain access to arcane arts.',
            'Cosmic Vortexes: Harnessing the power of cosmic vortexes to awaken arcane abilities.'
        ],
        'Mastery': [
            // Mastery within the arcane magical system represents the highest level of expertise and understanding. Elements related to the concept of Mastery in the arcane arts include:
            'Developing New Ideas, Mastering Lost Ones, or Both?: Mastery can involve discovering new arcane concepts or mastering ancient techniques.',
            'Limitations on Learning: Are there any restrictions or challenges to attaining mastery in arcane magic?',
            'Masters Keep Company with Others? with Students? with the World?: The role and involvement of master arcane practitioners within the magical society or world.',
            'What Skills Pave Paths to Master? What Makes Practitioners Falter?: The key skills and attributes required to achieve mastery and the potential pitfalls or challenges faced along the way.',
            'What Roles do Masters Play in the World?: The influence, responsibilities, and impact of master arcane practitioners on the world at large.',
            'Pioneers of New Arcane Knowledge: Masters who push the boundaries of arcane understanding and develop new magical concepts.',
            'Preservers of Ancient Arcane Lore: Masters who safeguard and uphold the wisdom of ancient arcane practices.',
            'Harbingers of Astral Revelations: Masters who explore the secrets of the astral realm and reveal cosmic insights.',
            'Wardens Against Arcane Abuses: Masters who act as guardians against those who misuse or abuse arcane magic.',
            'Custodians of Cosmic Balance: Masters who strive to maintain harmony and balance in the use of cosmic energies.',
            'Guardians of Ethereal Gateways: Masters who safeguard portals to other realms and dimensions.',
            'Arcane Council Elders: The most respected and wise arcane practitioners who form a governing council.',
            'Legacy of Master-Disciple Lineages: Passing down arcane knowledge through generations of master-disciple relationships.',
            'Enlightened Researchers: Masters dedicated to unraveling the deepest mysteries of arcane magic through research.',
            'Masters of Ritualistic Arcana: Specialists in ancient rituals and ceremonies that wield immense power.',
            'Arcane Artisans: Masters who craft enchanted artifacts and items of great magical potency.',
            'Astrological Visionaries: Masters who interpret celestial movements and use astrology for powerful magic.',
            'Arcane Ascetics: Practitioners who pursue mastery through solitary and disciplined practices.',
            'Arcane Vision Quests: Spiritual journeys undertaken to gain profound insights into arcane mysteries.'
        ]         
        },
    'Natural' : { /*Derived from the forces of nature*/
        'Source' : [ 
            //The 'Natural' magical system derives its power from the forces of nature, tapping into various elements and aspects of the natural world. These sources include:
            `Elements: Harnessing the powers of earth, water, fire, and air to manipulate the natural world.`,
            `Flora: Drawing power from plants and their energies for healing, growth, or even defensive purposes.`,
            `Beasts: Establishing connections with animals and creatures to gain their abilities or understanding.`,
            `Cycles: Working with the natural cycles, such as day-night, lunar phases, or seasonal changes, to enhance magic.`,
            `Positions: Aligning with specific geographic or celestial positions to tap into unique energies.`,
            `Spirits: Communing with nature spirits or entities for guidance and assistance in magical endeavors.`,
            `Weather: Controlling or influencing weather patterns, such as rain, wind, or storms.`,
            `Celestial Bodies: Drawing power from the movements and positions of celestial bodies like stars and planets.`,
            `Natural Phenomena: Tapping into the energy of phenomena like earthquakes, volcanoes, or auroras.`,
            `Territory: Channeling the power of specific natural territories, like forests, mountains, or oceans.`,
            `Seasons: Working with the energy and characteristics of different seasons for magical effects.`,
            `Tides: Aligning with the ebb and flow of tides to enhance magical abilities`,
            'Solar Energy: Utilizing the energy from the sun to empower magical workings.',
            'Lunar Energies: Drawing power from the phases of the moon for various magical intents.',
            'Mountain Spirits: Establishing connections with spirits residing in mountains for wisdom and strength.',
            'Oceanic Forces: Harnessing the power of ocean currents and waves for potent water-based magic.',
            'Forest Guardians: Seeking the guidance and protection of ancient forest spirits.',
            'Starlight Magic: Utilizing the energies of starlight and celestial events for divination and guidance.',
            'Animal Totems: Adopting animal totems as symbols of power and guidance in magical practice.',
            'Volcanic Energies: Drawing on the raw power of volcanic activity for transformational magic.',
            'Cosmic Alignment: Aligning magical workings with cosmic events like meteor showers or eclipses.',
            `Wind Manipulation: Controlling the wind's direction and intensity for various purposes.`,
            'Rooted in Earth: Drawing power from the deep connection with the earth and its energy.',
            'Solar Eclipse Magic: Utilizing the rare occurrence of solar eclipses for potent magical rituals.',
            'Rainwater Blessings: Collecting and using rainwater for purification and magical empowerment.'
        ],
        'Cost' : [ 
            //Utilizing natural magic requires practitioners to respect the delicate balance of the natural world, and the cost of their magic can include:
            `Control: Maintaining control over the powers harnessed to prevent unintended consequences.`,
            `Consumption: Using natural resources or life force to fuel spells or magical abilities.`,
            `Vitality: Expending personal energy or life force to perform powerful natural magic.`,
            `Discomfort: Enduring physical or mental discomfort during the practice of natural magic.`,
            `Proximity: Being physically close to the natural source to effectively wield its power.`,
            `Harmony with Nature: Practitioners must be in harmony with the natural world to access its magic.`,
            `Balance with the Ecosystem: Ensuring that their magic does not disrupt the delicate ecosystem.`,
            `Sacrifice for the Land: Making sacrifices or offerings to maintain the balance of nature.`,
            `Communing with Nature: Establishing a deep connection with nature through meditation or rituals.`,
            'Cycles of Renewal: Practitioners may undergo periods of rest and renewal after using powerful magic.',
            'Eco-Friendly Practices: Using eco-friendly materials and methods to align with natural magic.',
            'Guardian Duties: Taking on the role of protecting and preserving specific natural areas or species.',
            `Seasonal Alignment: The magic's potency may be influenced by the practitioner's alignment with the seasons.`,
            'Ancestral Pacts: Fulfilling ancient pacts or agreements with nature to access magic.',
            'Environmental Restoration: Using magic to restore and heal damaged natural environments.',
            'Empathy with Flora and Fauna: Practitioners may experience the emotions of plants and animals they interact with.',
            `Nature's Harmonic Balance: Ensuring that their magical actions contribute to the overall harmony of nature.`,
            `Biorhythmic Alignment: Aligning magical practices with the practitioner's own biorhythms for efficacy.`,
            'Spiritual Cleansing: Regularly cleansing the spirit and mind to maintain purity in magical workings.',
            'Elemental Respect: Revering and showing respect to the elemental spirits tied to natural magic.',
            `Nature's Blessings: Seeking the blessings of nature spirits or deities before performing magic.`,
            'Karmic Repercussions: Being mindful of the karmic consequences of their magical actions.',
            'Seasonal Offerings: Offering gifts or rituals during specific seasonal transitions to honor nature.',
            'Energetic Exchange: Practitioners may exchange energy with nature as a form of payment for magical use.'
        ],
        'Potency' : [ 
            //The potency of natural magic depends on the understanding and alignment with the forces of nature. Factors that determine potency include:
            `Environment: The magical power increases when practicing in environments aligned with the natural source.`,
            `Connection: Strong connections with the natural source result in more potent magical effects.`,
            `Uniqueness: Uncommon or rare natural sources may yield more powerful magic.`,
            `Balance: Maintaining a balanced approach to magic ensures stable and powerful results.`,
            `Harmony: In harmony with nature, practitioners can amplify the natural energies they draw upon.`,
            `Amplification of Natural Forces: Enhancing or amplifying existing natural forces through magic.`,
            `Alignment with Celestial Events: Harnessing power from celestial events like eclipses or meteor showers.`,
            `Harnessing Natural Cycles: Using the flow of natural cycles to empower magical workings.`,
            `Merging with the Land: Practitioners merging their essence with natural landscapes to amplify magic.`,
            'The Power of Seasons: The potency of natural magic may vary with the changing seasons.',
            'Ley Lines and Nexus Points: Accessing potent magical energies through ley lines and nexus points.',
            'Moon Phases: The magical strength may fluctuate based on the phase of the moon.',
            `Elemental Affinity: The practitioner's affinity with specific elements affects the potency of magic.`,
            'Spiritual Ascendance: Achieving higher spiritual levels can unlock more potent magical abilities.',
            'Life-Death-Rebirth Cycle: Drawing power from the cyclical nature of life, death, and rebirth.',
            `Primal Wilderness: Practicing in untouched wilderness areas boosts the magic's strength.`,
            'Ancestral Blessings: Inherited blessings from ancestors may empower the magic.',
            'Eclipse Magic: Harnessing the unique power of solar and lunar eclipses for magical workings.',
            'Natural Euphony: Performing magic in sync with natural sounds and rhythms enhances potency.',
            'Oceanic Tides: The power of magic may be linked to the ebb and flow of ocean tides.',
            'Spiritual Allies: Calling upon benevolent spirits of nature to aid in magical endeavors.',
            'Cosmic Convergence: Gaining access to extraordinary magical energies during rare cosmic events.',
            'Energetic Vortexes: Tapping into energy vortexes for heightened magical potency.',
            'Wisdom of Ancient Trees: Drawing knowledge and power from ancient and wise trees.',
            'Fauna Empowerment: Connecting with wildlife to amplify natural magical abilities.',
            'Mystical Water Sources: Accessing potent magic from sacred springs, rivers, or waterfalls.'
        ],
        'Accessibility' : [ 
            //The accessibility of natural magic addresses how readily it can be accessed or learned within the society or magical world. Factors impacting its accessibility include:
            `Beliefs or Superstitions: Cultural beliefs and superstitions shape the perception and acceptance of natural magic.`,
            `Dependant: The "${buildClass()}" profession heaviliy relies on this magic.`,
            `Societal Impact: The impact of natural magic on society may influence its acceptance or regulation.`,
            `Unique Offerings: Practitioners of natural magic may provide services or abilities others cannot replicate.`,
            `Learning Opportunities: Availability of places or institutions to learn natural magic.`,
            `Seeking Practitioners: People might seek out natural magic practitioners for their unique abilities and insights.`,
            `Sacred Natural Sites: Locations with potent natural magic are revered and protected.`,
            `Druidic Circles: Secretive or sacred groups of druids devoted to natural magic and preservation.`,
            `Nature Spirit Communes: Practitioners establish connections with nature spirits and entities.`,
            `Initiation Rites: Rites or tests one must undergo to gain access to natural magic.`,
            `Nature's Call: Access to natural magic through a spiritual calling to serve and protect the natural world.`,
            'Hereditary Lineages: The magic is passed down through specific bloodlines with inherent connections to nature.',
            `Nature's Balance: Accessible only to those who demonstrate a deep understanding and respect for the balance of nature.`,
            'Animals as Guides: Practitioners gain access to natural magic through the guidance of animal spirits.',
            'Eco-Magic Conclaves: Gatherings or meetings where practitioners share and learn about natural magic.',
            'Celestial Alignments: The magic becomes accessible during specific celestial events or planetary alignments.',
            'Sacred Symbols and Runes: The use of specific symbols or runes to unlock the secrets of natural magic.',
            'Elemental Trials: Initiates must undergo trials representing the elements to prove their worthiness for the magic.',
            `Nature's Guardians: The magic is accessible to those chosen by nature itself to safeguard its sanctity.`,
            'Mystical Journeys: Access to natural magic through undertaking transformative and enlightening journeys.',
            'Natural Intuition: Some are born with an innate affinity for the magic and can access it intuitively.',
            'Ancient Artefacts: Certain ancient artifacts grant access to the knowledge and power of natural magic.'
        ],
        'Mastery' : [ 
            //Mastery within the natural magical system represents a deep understanding and harmonious coexistence with nature. Aspects related to the concept of Mastery in natural magic include:
            `Do Masters Need to Fully Commit to Nature? Do They Maintain a Connection to Civilization? Do They Walk Between Worlds?: The balance between living closely with nature and interacting with civilization.`,
            `Do Masters Take on Aspects of Their Source in Thought or Appearance?: Whether mastery affects the practitioner's mindset or physical characteristics.`,
            `Who Depends on Masters of Natural Magic?: The individuals or communities relying on the guidance and protection of masters.`,
            `What Roles Do Masters Play in the World?: The impact and responsibilities of master natural magic practitioners on the world.`,
            `Balance Keepers of the Natural Order: Masters who safeguard the equilibrium of natural forces and ecosystems.`,
            `Guardians of Sacred Natural Sites: Masters protecting and preserving sacred locations with potent natural magic.`,
            `Harmonizers of Nature and Civilization: Masters bridging the gap between the needs of nature and civilization.`,
            `Channellers of Celestial Energies: Masters who harness the power of celestial events for magical purposes.`,
            `Stewards of Rare and Endangered Species: Masters dedicated to preserving and healing endangered natural life`,
            'Caretakers of Ancient Wisdom: Masters who hold and pass down ancient knowledge of natural magic.',
            'Ritualists of the Natural Cycles: Masters who perform sacred rituals to honor and harness the cycles of nature.',
            'Healers of the Land: Masters who use natural magic to heal and restore the health of the environment.',
            'Emissaries of Elemental Spirits: Masters who communicate and work with elemental spirits for magical purposes.',
            'Natural Architects: Masters who shape and harmonize the landscape using natural magic in architectural design.',
            'Mystics of the Wild: Masters who delve into the mysteries and spiritual aspects of nature and its creatures.',
            'Weather Wardens: Masters who have command over weather patterns and can temper natural disasters.',
            'Nurturers of Magical Gardens: Masters who cultivate magical gardens that yield potent and unique flora.',
            'Druids of the Old Ways: Masters following ancient druidic traditions, serving as wisdom-keepers and advisors.',
            'Shapeshifters and Animal Allies: Masters who form powerful bonds with animals and embody their spirits through shape-shifting.',
            `Nature's Conservators: Masters who protect and defend natural habitats from harm and exploitation.`,
            'Ecological Innovators: Masters who use natural magic to create sustainable solutions for environmental challenges.',
            'Spiritual Guides and Shamans: Masters who guide individuals on spiritual journeys and connect with the spirit world.',
            'Guardians of the Elemental Nexus: Masters who maintain balance among the elemental forces in the world.',
            'Keepers of Ancestral Wisdom: Masters who honor and pass down the ancient magical traditions of their ancestors.',
            'Seekers of Hidden Knowledge: Masters who explore hidden realms and ancient texts to uncover forgotten natural magic.'
        ]
        },
    'Legendary' : { /*It moves a story or defines the lesson of a story*/
        'Source' : [ 
            //The 'Legendary' magical system draws its power from sources that carry great significance in shaping stories, lessons, and the course of events. These sources include:
            `Irony: The irony of situations and events can create potent magical effects or twists in the narrative.`,
            `Fate: The mystical force that determines the destinies and outcomes of individuals and events.`,
            `Poetry: The power of words and poetic expressions can manifest as magical phenomena.`,
            `Gods: Deities and divine beings may grant or manipulate legendary magic in the world.`,
            `Folkways: The customs, traditions, and beliefs of a culture can imbue magic with legendary qualities.`,
            `Axiom: Fundamental principles or truths that govern reality can influence legendary magic.`,
            `Artifacts: Powerful and ancient relics hold extraordinary magical properties.`,
            `Locations: Certain legendary places possess unique and mystical energies.`,
            `Legendary Creatures: Mythical beings and creatures contribute to the magical lore.`,
            `Prophetic Visions: Foretelling the future through visions bestows magical insights.`,
            `Sacred Texts: Ancient texts or scriptures contain hidden magical knowledge.`,
            `Mysterious Prophecies: Enigmatic predictions shape the unfolding of events.`,
            `The Weaver's Loom: The fabric of fate and destiny is the source of the magic's power.`,
            `Songs of Creation: The magic is born from the harmonious songs of cosmic entities.`,
            `Tales of Yore: Ancient legends and folklore infuse the magic with their essence.`,
            `Ephemeral Spirits: Intangible spirits from other realms grant access to the magic.`,
            `Harmony of Elements: The elemental forces in perfect balance grant mastery over the magic.`,
            `Cosmic Alchemy: The magic arises from the blending of celestial energies.`,
            `The Great Myths: The tales of legendary heroes empower the magic's wielders.`,
            `Chords of the Spheres: The celestial melodies weave the magic's power.`,
            `The Enchanted Scribe: A mystical being inscribes the magical symbols into existence.`,
            `The Cosmic Librarian: The keeper of cosmic knowledge imparts the magic's secrets.`,
            `Celestial Confluence: The alignment of stars and planets channels the magic's energy.`,
            `The Weeping Moon: The magic's source is a celestial body mourning a cosmic tragedy.`,
            `Eternal Flame of Creativity: The ever-burning flame of creativity fuels the magic.`,
            `Echoes of Creation: The echoes of the universe's birth resonate within the magic.`,
            `Eyes of the Oracle: The all-seeing eyes of a prophetic figure channel the magic.`,
            `Veil of the Muse: The inspiration of a mysterious muse infuses the magic's essence.`,
            `The Gilded Tome: An ancient book of wisdom is the wellspring of the magic's power.`,
            `The Everlasting Oath: The fulfillment of an unbreakable oath grants access to the magic.`,
            `Crescent Serenade: The magic's melody is carried on the celestial song of the moon.`              
        ],
        'Cost' : [ 
            //Legendary magic often requires profound sacrifices or commitments to evoke its power. The costs associated with wielding legendary magic include:
            `Healing: Utilizing magic to heal may require sacrificing one's own well-being or life force.`,
            `Faith: Faith and belief in the magic's significance can be a necessary cost.`,
            `Unlikeliness: The magic may require overcoming seemingly impossible odds or challenges.`,
            `Last Hope: Utilizing legendary magic as a final resort or the last hope.`,
            `Omnipresent: Being present in all places and times can be a cost for wielding such magic.`,
            `Sacrifice of Loved Ones: Powerful magic may demand the sacrifice of loved ones.`,
            `Severing Bonds: Wielding legendary magic might require severing personal bonds or connections.`,
            `Atonement: Seeking redemption or atonement for past actions can empower the magic.`,
            `Permanence of Consequences: The consequences of wielding such magic may be irreversible.`,
            `Burdens of Legacy: Practitioners may carry the weight of the magic's historical legacy and expectations.`,
            `Eclipse of the Self: Harnessing the magic requires temporarily suppressing one's own identity.`,
            `Blood Ties: Drawing power from ancestral bloodlines may come at a cost to family ties.`,
            `Cursed Empowerment: Wielding the magic may come with a burden of a personal curse.`,
            `Guardianship Duty: Practitioners become guardians of sacred places tied to the magic.`,
            `Echoes of Loss: The magic carries the echoes of past losses and sufferings.`,
            `Sanctity of Vows: Fulfilling sacred vows and pledges can amplify the magic's strength.`,
            `Convergence of Emotions: Practitioners must channel intense emotions to evoke the magic.`,
            `Limitation of Time: The magic may only be accessible during specific fleeting moments.`,
            `Harmony of Elements: Achieving balance among elemental forces is required to access the magic.`,
            `Temporal Balance: The magic's use must maintain the balance between past, present, and future.`,
            `Eternal Vigilance: Practitioners must be ever vigilant to prevent the magic from being misused.`,
            `Sustaining Prophecy: Maintaining the magic's power requires interpreting and fulfilling prophecies.`,
            `Paradox of Truth: Utilizing the magic may force the practitioner to confront uncomfortable truths.`,
            `Binding Oaths: Practitioners are bound by ancient oaths to uphold the magic's principles.`,
            `Duality of Desires: The magic demands navigating conflicting desires and motivations.`,
            `Harvesting Memories: The magic draws strength from shared memories or collective consciousness.`,
            `The Entwined Threads: Practitioners must navigate complex interwoven destinies to harness the magic.`,
            `Veil of Remembrance: Remembering and honoring the magic's past keepers is a necessary cost.`,
            `Purification Rite: Before accessing the magic, practitioners must undergo a ritual of purification.`,
            `Crown of Regret: The magic may evoke deep feelings of regret for past actions.`
        ],
        'Potency' : [ 
            //The potency of legendary magic can vary from subtle and secretive to grand and world-altering. Factors influencing potency include:
            `Almost Invisible: The magic's effects may be barely noticeable to most, leaving no trace.`,
            `Only the Wise See It: Only those with great wisdom or insight can perceive the magic.`,
            `Only Certain Individuals See and Understand It - Limited to a select few who can keep the magic's existence hidden.`,
            `Only Certain Individuals See and Understand It - The magic is known to some but requires explanation and understanding.`,
            `It is Obvious, Dramatic, and Undeniable: The magic's effects are clear, dramatic, and undeniable to all.`,
            `Reality-Bending: Legendary magic can bend reality and alter the natural order.`,
            `Altering the Fabric of Space and Time: The magic can manipulate space and time itself.`,
            `Shaping the Course of Events: The magic influences events on a significant scale.`,
            `Changing the Fate of Nations: The magic can alter the destiny of entire nations.`,
            `Whispers of Destiny: Legendary magic can subtly influence the paths individuals take in life.`,
            `Echoes of Legends: The magic echoes the feats and powers of ancient legendary figures.`,
            `Cosmic Resonance: The magic resonates with cosmic forces, enhancing its potency.`,
            `Celestial Augury: Practitioners can read the signs and symbols of the heavens to wield the magic.`,
            `Chronicles of Time: The magic allows practitioners to view the past, present, and future.`,
            `Unraveling Illusions: Legendary magic can dispel illusions and reveal hidden truths.`,
            `Crescendo of Power: The magic's potency grows with the passing of time or critical events.`,
            `Songs of Creation: Mastery of legendary magic allows practitioners to weave reality through song.`,
            `Tidal Influence: The magic waxes and wanes with celestial cycles and phases.`,
            `Resurgence of Legends: The magic strengthens as tales and legends of its feats spread.`,
            `Legacy of Ages: Potency is tied to the echoes of ancient practitioners who wielded the magic.`,
            `Confluence of Elements: The magic reaches its peak when the elements are in perfect alignment.`,
            `Ephemeral Embers: The magic can only be harnessed during specific fleeting moments.`,
            `Harmony of Souls: The potency increases when practitioners work in perfect harmony.`,
            `Astral Convergence: Legendary magic peaks during rare astral conjunctions.`,
            `Eclipse Empowerment: The magic gains strength during solar or lunar eclipses.`,
            `Cataclysmic Catalyst: Potency is unleashed when the world faces a critical turning point.`,
            `Celestial Symphony: The magic's potency resonates with the harmony of celestial bodies.`,
            `Everlasting Epics: The magic's effects endure through the ages and leave a lasting impact.`,
            `Quintessence Unleashed: The magic harnesses the essence of life and creation.`,
            `Veil of Legends: The true potency of legendary magic remains veiled in mystery and awe.`
        ],
        'Accessibility' : [ 
            //The accessibility of legendary magic touches upon how it is obtained or accessed within the society or magical world. Factors impacting its accessibility include:
            `Beliefs or Superstitions: Cultural beliefs and superstitions shape the perception and acceptance of legendary magic.`,
            `Dependant: The "${buildClass()}" profession heaviliy relies on this magic.`,
            `Societal Impact: The impact of legendary magic on society may influence its acceptance or regulation.`,
            `Historical Event Shaped by it: A significant historical event tied to the legendary magic's origin or impact.`,
            `Figure Associated with this Magic: A legendary figure or hero linked to the magic's origin or manifestation.`,
            `Ancient Riddles and Enigmas: Solving ancient riddles and enigmas may grant access to the magic.`,
            `Guardians of Legendary Knowledge: Keepers of ancient secrets related to legendary magic.`,
            `Visions and Dreams: Receiving visions and dreams may reveal the magic's secrets.`,
            `Hereditary Lineages of Prophecy: Certain bloodlines hold the key to the magic's potential.`,
            `Hidden Tombs and Temples: Secrets of the magic are hidden in ancient tombs or temples.`,
            `Cosmic Convergence: The magic becomes accessible during specific celestial alignments.`,
            `Tales of Wanderers: Legends speak of elusive wanderers who possess knowledge of legendary magic.`,
            `Chosen Fates: Access to the magic is granted to individuals chosen by destiny or divine will.`,
            `Epic Trials: Aspiring practitioners must complete epic trials to prove their worthiness.`,
            `Celestial Blessing: Legendary magic can be accessed through a divine blessing from celestial beings.`,
            `Shrouded Provenance: The magic's true source remains shrouded in mystery and secrecy.`,
            `Nexus of the Lost: Access to legendary magic lies at the intersection of multiple lost paths.`,
            `Forbidden Illumination: Insights into the magic are gained by exploring forbidden realms.`,
            `Lost Prophecies: Unraveling long-lost prophecies is the key to accessing legendary magic.`,
            `Temporal Nexus: The magic is accessible during rare temporal phenomena or time anomalies.`,
            `Starlit Portals: Legendary magic can be found through ancient starlit portals.`,
            `The Fateful Tome: A mythical tome holds the secrets of legendary magic, but its location is unknown.`,
            `Eternal Echoes: Only those who hear the eternal echoes of legendary tales can access the magic.`,
            `Custodians of the Glyphs: Masters protect the ancient glyphs that unlock legendary magic.`,
            `Mystical Pilgrimage: Accessing the magic requires embarking on a sacred and perilous pilgrimage.`,
            `Winds of Revelation: The magic becomes accessible when the winds of revelation blow.`,
            `Voyage of Legends: Navigating a treacherous voyage leads to the discovery of legendary magic.`,
            `The Celestial Omen: The magic becomes accessible when a celestial omen manifests.`,
            `Whispers of the Ancients: Whispered words from ancient beings guide practitioners to legendary magic.`
        ],
        'Mastery' : [ 
            //Mastery within the legendary magical system represents a deep understanding and command over the magic's unique qualities. Aspects related to the concept of Mastery in legendary magic include: 
            `Masters of Legendary Magic: The actions and achievements of past masters of legendary magic.`,
            `Active Masters: Whether there are currently individuals who have mastered legendary magic.`,
            `Worthy Beings: Whether only worthy individuals can wield legendary magic or if it can work through anyone.`,
            `Permanent Change: Whether mastering the magic requires a permanent transformation or commitment.`,
            `Solving or Creating Problems: The nature of legendary magic in either resolving or creating new challenges.`,
            `Guardians of Ancient Secrets: Masters who safeguard the knowledge and history of legendary magic.`,
            `Keepers of Prophetic Wisdom: Masters with the ability to interpret and guide others through prophecies.`,
            `Harbingers of Legendary Events: Masters whose actions set in motion legendary events.`,
            `Envoys of the Gods: Masters who act as intermediaries between mortals and divine beings.`,
            `The Balance of Destiny: Masters who uphold the balance and purpose of legendary magic in the world.`,
            `Living Myths: Some masters are seen as living embodiments of mythical figures associated with legendary magic.`,
            `Timeless Vision: Legendary masters possess an innate understanding of the flow of time and its significance.`,
            `Lore Manipulation: Mastery allows the practitioner to influence the narratives and tales surrounding legendary magic.`,
            `Eternal Wanderers: Masters wander the world, leaving a trail of legendary feats and stories in their wake.`,
            `Custodians of Sacred Artifacts: Legendary masters safeguard powerful artifacts associated with the magic.`,
            `Songs of Power: Some masters use their voice or music to channel the power of legendary magic.`,
            `Legendary Ancestry: Mastery is passed down through ancient lineages with connections to legendary figures.`,
            `Weavers of Fate: Masters can subtly manipulate destiny and fate using legendary magic.`,
            `Living Prophecies: Masters embody the prophecies they interpret, becoming living conduits of fate.`,
            `Unraveling Myths: Masters seek to understand the true origins and meanings behind legendary tales.`,
            `Celestial Pupils: Masters receive guidance and training from celestial beings or celestial realms.`,
            `Mythical Stewards: Masters are entrusted with the preservation and continuation of legendary traditions.`,
            `Bridges Between Worlds: Mastery allows practitioners to traverse between the mortal realm and mythical realms.`,
            `Chroniclers of Legends: Masters record and protect the history of legendary magic for future generations.`,
            `Fabled Visions: Masters experience visions that guide them to legendary artifacts or revelations.`,
            `Elemental Harmonies: Some masters harness legendary magic through attuning with elemental forces.`,
            `Veil of Immortality: Legendary masters may possess eternal life as a result of their mastery.`,
            `Primordial Nexus: Masters tap into the primordial source from which legendary magic originates.`,
            `Oracles of the Ages: Masters gain insights into past, present, and future through legendary visions.`,
            `Eternal Echoes: Legends and tales of legendary masters resonate through the ages, inspiring others.`
        ]
        },
    'Forbidden' : { /*Magic that is feared or shunned*/
        'Source' : [
            //The 'Forbidden' magical system draws its power from sources that are feared, shunned, or deemed dangerous by society. These sources include:
            `Alien: Magic from otherworldly entities or dimensions that is not well understood or controlled.`,
            `Sin: Magic derived from acts or beliefs considered morally wrong or sinful.`,
            `Adversaries: Power drawn from malevolent or hostile forces seeking harm or chaos.`,
            `Appropriation: Magic obtained by stealing or forcefully taking it from its rightful owners.`,
            `Passion: Magical energies fueled by intense emotions, which may lead to loss of control.`,
            `Desire: Magic derived from unhealthy obsessions or uncontrollable cravings.`,
            `Taboo Rituals: Magical practices that are strictly prohibited or forbidden due to their nature.`,
            `Cursed Relics: Objects or artifacts with malevolent magic that bring misfortune to those who wield them.`,
            `Lost Artifacts: Ancient magical relics that have been forgotten or hidden for a reason.`,
            `Malevolent Spirits: Magic channeled from maleficent spirits or entities.`,
            `Forbidden Knowledge: Magic derived from forbidden texts or secret occult teachings.`,
            `Blood Magic: Utilizing the life force or blood of oneself or others to fuel powerful spells.`,
            `Necromancy: Dealing with the dead or manipulation of life and death energies.`,
            `Dark Rituals: Invoking dark powers or entities for malevolent purposes.`,
            `Curses and Hexes: Casting spells to inflict harm or misfortune upon others.`,
            `Sacrificial Magic: Performing rituals that require sacrifices of living beings.`,
            `Demonic Pacts: Forging agreements with demons or dark entities in exchange for power.`,
            `Shadow Magic: Drawing power from the realm of shadows and darkness.`,
            `Soul Manipulation: Tampering with souls, leading to potential spiritual corruption.`,
            `Blood Sacrifice: The use of blood rituals to appease or summon powerful entities.`,
            `Black Arts: Delving into forbidden and dangerous magical arts that defy natural laws.`,
            `Destruction Magic: Wielding magic focused on causing devastation and ruin.`,
            `Forbidden Alchemy: Pursuing alchemical transmutations that could have disastrous consequences.`,
            `Forbidden Summoning: Calling forth entities beyond mortal comprehension.`,
            `Chaos Magic: Tapping into unpredictable and chaotic magical forces.`,
            `Maleficent Enchantments: Casting malevolent spells to manipulate or harm others.`,
            `Dark Runes: Inscribing runes with dark and dangerous meanings and intentions.`,
            `Corruption Magic: Using magic to corrupt or taint living beings and nature.`,
            `Forbidden Ciphers: Decrypting ancient and forbidden magical codes and scripts.`,
            `Eldritch Energies: Harnessing otherworldly and incomprehensible magical energies.`,
            `Wrathful Deities: Drawing power from deities or beings associated with rage and destruction.`,
            `Tainted Elementals: Manipulating corrupted elemental forces to cause harm.`,
            `Occult Bloodlines: Accessing arcane powers through bloodlines with dark origins.`,
            `Plague Magic: Wielding magic related to diseases and spreading illness.`,
            `Rituals of Betrayal: Performing rituals that betray or harm trust.`,
            `Forbidden Totems: Utilizing cursed totems or objects of dark origin for magic.`,
            `Maddening Whispers: Hearing and channeling voices from unknown and chaotic sources.`,
            `Nightmare Conjuring: Summoning nightmares and bringing them into reality.`,
            `Haunting Spirits: Manipulating vengeful and malevolent spirits for power.`,
            `Forbidden Arts of Decay: Using magic to accelerate the decay and destruction of objects or beings.`,
            `Abomination Alchemy: Creating monstrous and twisted creatures through alchemical means.`,
            `Vampiric Magic: Drawing energy and life force from unwilling victims.`,
            `Phantasmal Illusions: Casting illusions that induce terror or madness in those who perceive them.`,
            `Abyssal Tethering: Forging connections with dark and abyssal realms for power.`,
            `Forbidden Prophecies: Decoding prophecies with catastrophic outcomes.`,
            `Forsaken Contracts: Entering into dark pacts that bring calamitous consequences.`,
            `Haunted Bloodlines: Harnessing powers from cursed bloodlines and ancestors.`,
            `Cataclysmic Elemental Magic: Controlling elemental forces with catastrophic potential.`,
            `Feral Shapeshifting: Transforming into uncontrollable and dangerous beasts.`,
            `Forbidden Grimoires: Drawing power from cursed or forbidden spellbooks.`,
            `Dreadful Charms: Using cursed charms to manipulate or harm others.`,
            `Occult Astral Projection: Traveling the astral plane with dark intentions.`,
            `Venomous Conjurations: Summoning and manipulating venomous creatures for harm.`,
            `Dark Enchantment Circles: Casting malevolent spells within forbidden enchantment circles.`,
            `Dark Star Alignments: Harnessing dark energies during celestial alignments.`,
            `Malevolent Artifacts: Wielding cursed and malevolent artifacts for sinister purposes.`,
            `Unholy Ritual Sacrifices: Performing rituals that desecrate holy sites or symbols.`,
            `Nether Realm Invocation: Invoking entities from the nether realm for dark magic.`
        ],
        'Cost' : [
            //Utilizing forbidden magic comes with significant costs, often impacting the practitioner's well-being and moral integrity. The costs associated with forbidden magic include:
            `Reason: Practitioners may lose their rationality and succumb to irrational impulses.`,
            `Morality: Using forbidden magic might require compromising one's moral principles.`,
            `Transformation: Wielding such magic could lead to physical or mental transformations.`,
            `Blight: The environment or living beings may suffer from the use of forbidden magic.`,
            `Debt: The magic may demand repayment in unexpected and undesirable ways.`,
            `Sanity: The practitioner's mental stability may deteriorate over time.`,
            `Loyalty: Using forbidden magic may cause conflicts within relationships or loyalties.`,
            `Life Essence: The magic may consume or drain the life force of the practitioner or others.`,
            `Loss of Innocence: Practitioners may lose their innocence or purity due to the dark nature of the magic.`,
            `Corruption: The practitioner's heart and soul may be tainted by the corrupting influence of forbidden magic.`,
            `Isolation: Wielding forbidden magic can lead to isolation and rejection from society and loved ones.`,
            `Twisted Fate: Practitioners may be bound to a dark destiny or cursed by the use of forbidden magic.`,
            `Existential Dread: The burden of knowing and dealing with the consequences of forbidden magic can lead to existential crises.`,
            `Karmic Backlash: The universe may exact a heavy price for daring to manipulate forbidden powers.`,
            `Eternal Vigilance: Practitioners must constantly battle against inner darkness and temptation after using forbidden magic.`,
            `Haunted Dreams: Nightmares and haunting visions may plague practitioners after delving into the forbidden arts.`,
            `Cursed Existence: Forbidden magic could bring a perpetual curse upon the practitioner and those close to them.`,
            `Soul Fragmentation: The use of forbidden magic may fragment the practitioner's soul, causing inner turmoil.`,
            `Lost Connections: Practitioners risk losing their connection with the natural world and the spirits that govern it.`,
            `Spectral Haunting: The spirits of the deceased may be drawn to those who practice forbidden magic.`,
            `Eternal Debt: The magic may demand a never-ending debt that the practitioner can never fully repay.`,
            `Desolation: Forbidden magic may leave a trail of desolation and ruin in its wake.`,
            `Eternal Torment: The magic could subject practitioners to eternal torment or suffering in the afterlife.`,
            `Existence Cycles: The use of forbidden magic could lead to endless cycles of suffering and rebirth.`,
            `Doomed Prophecies: Practitioners may be bound by dark prophecies that foretell their downfall.`,
            `Family Curse: Forbidden magic may curse the practitioner's entire family line for generations.`,
            `Haunted Legacy: The repercussions of using forbidden magic may haunt the practitioner's descendants.`,
            `Infernal Bargains: Forbidden magic may require making deals with infernal entities with dire consequences.`,
            `Abyssal Erosion: The dark forces behind the magic may erode the practitioner's very soul.`
        ],
        'Potency' : [
            //Forbidden magic can be potent and destructive, harnessing negative energies and causing significant consequences. The potency of forbidden magic includes:
            `Transgression: The magic's power increases with the level of forbidden actions or rules broken.`,
            `Sacrifice: Greater magical effects may require more significant sacrifices or suffering.`,
            `Suffering: The magic thrives on the pain and suffering of the practitioner or others.`,
            `Woe: Forbidden magic can bring misery and suffering to those who encounter it.`,
            `Perception: The perception of the magic's forbidden nature may amplify its effects.`,
            `Corruption: The magic can corrupt the practitioner's soul or mind over time.`,
            `Destruction: The magic's potency may be destructive and catastrophic in its effects.`,
            `Temporal Anomalies: Forbidden magic may tamper with time, creating unpredictable consequences.`,
            `Reality Warping: The magic can bend and distort reality itself.`,
            `Nightmare Manifest: The magic can turn dark dreams and fears into nightmarish reality.`,
            `Cataclysmic Catalyst: Forbidden magic can act as a catalyst for apocalyptic events.`,
            `Unholy Nexus: The magic connects practitioners to malevolent forces, magnifying its strength.`,
            `Entropy Amplification: Forbidden magic accelerates the natural decay and entropy of all things.`,
            `Soul Devourer: The magic may consume the essence or souls of its victims to gain power.`,
            `Eldritch Nexus: Forbidden magic taps into unfathomable and ancient cosmic energies.`,
            `Cursed Blessing: The potency of forbidden magic comes at the cost of bestowing curses upon the practitioner.`,
            `Dreadful Aura: Forbidden magic radiates an aura of terror, affecting those nearby.`,
            `Nefarious Catalyst: The magic fuels dark plans and schemes, influencing malevolent intentions.`,
            `Maleficent Echoes: The effects of forbidden magic reverberate long after its use, causing harm to others.`,
            `Chaotic Catalyst: Forbidden magic disrupts the natural order and introduces chaos.`,
            `Eternal Resonance: The magic's consequences echo throughout eternity, with no end in sight.`,
            `Unfathomable Reach: The magic's power extends beyond the practitioner's control, affecting distant realms.`,
            `Whispers of Damnation: Forbidden magic is accompanied by haunting whispers from the netherworld.`,
            `Eclipse of Hope: The magic casts a shadow on hope and optimism, leading to despair.`,
            `Pandemonium Surge: Forbidden magic may trigger uncontrollable surges of pandemonium.`,
            `Abominable Empowerment: Forbidden magic empowers the practitioner, but at the cost of their humanity.`,
            `Lost Arcane Cataclysm: The magic taps into forgotten arcane forces capable of cataclysmic upheaval.`,
            `Endless Nightfall: Forbidden magic perpetuates darkness, preventing the dawn of a new day.`,
            `Apocalyptic Enchantment: Forbidden magic enchants objects or beings with apocalyptic potential.`,
            `Cursed Ward: The magic creates a cursed barrier, bringing calamity to those who cross it.`,
            `Forbidden Entropy: The magic disrupts reality's balance, leading to increasing disorder and chaos.`,
        ],
        'Accessibility' : [
            //Accessing forbidden magic can be challenging, requiring practitioners to navigate secretive and hidden paths. Factors impacting its accessibility include:
            `Dependant: The "${buildClass()}" profession heaviliy relies on this magic.`,
            `Societal Impact: The impact of forbidden magic on society may affect its availability or use.`,
            `Unique Offerings: Practitioners of forbidden magic may provide abilities or knowledge unavailable to others.`,
            `Learning Opportunities: The places or institutions where forbidden magic can be learned.`,
            `Seeking Practitioners: People may seek out practitioners of forbidden magic for specific purposes.`,
            `Hidden Cults: Secretive cults or organizations that practice forbidden magic in seclusion.`,
            `Forbidden Academies: Schools or academies that clandestinely teach forbidden magic.`,
            `Arcane Black Markets: Illicit markets where forbidden magical artifacts or knowledge are traded.`,
            `Ancient Prophecies: Prophecies or ancient texts that hint at the existence of forbidden magic.`,
            `Eldritch Veil: Accessing forbidden magic requires the practitioner to pass through an enigmatic veil or barrier.`,
            `Dark Nexus: Forbidden magic can only be accessed through hidden locations with strong dark energies.`,
            `Cursed Bloodline: Only those born into certain cursed bloodlines can access the forbidden arts.`,
            `Trial of Shadows: Aspiring practitioners must undergo a series of shadowy trials to gain access to the magic.`,
            `Dark Rites of Initiation: Initiates must partake in ominous rituals to unlock the secrets of forbidden magic.`,
            `Sacrificial Gate: The path to accessing forbidden magic involves sacrificing something of great value.`,
            `Forbidden Prophecies: The secrets of forbidden magic are concealed within cryptic and forbidden prophetic writings.`,
            `Ward of Forbiddance: Powerful wards or enchantments guard the knowledge of forbidden magic.`,
            `Tainted Inheritance: Forbidden magic can only be inherited by those destined to carry a tainted legacy.`,
            `Occult Infiltration: Gaining access to forbidden magic requires infiltrating secretive occult circles.`,
            `Forbidden Chosen Ones: Only specific individuals, chosen by dark forces, can access the magic.`,
            `Unspeakable Tomes: Forbidden knowledge is hidden in ancient and forbidden grimoires.`,
            `Dark Alchemy: Alchemical processes are required to unlock the secrets of forbidden magic.`,
            `Cursed Mark: The magic can only be accessed by bearing a cursed mark or sigil.`,
            `Whispers of the Nether: The voices of malevolent entities guide practitioners towards forbidden magic.`,
            `Eclipse of Knowledge: Accessing forbidden magic requires aligning with cosmic events.`,
            `Realm of Shadows: Forbidden magic can be accessed only in the realm of shadows or the netherworld.`,
            `Ancestral Anomaly: Forbidden magic becomes accessible when a family's dark past is uncovered.`,
            `Blood Oath of Secrecy: Aspiring practitioners must swear a blood oath to keep the magic's secrets.`,
            `Dark Travelers: Forbidden magic can be accessed only by those who journey to other realms or dimensions.`,
            `Veil of Forgetfulness: The path to forbidden magic involves forgetting parts of one's past.`
        ],
        'Mastery' : [
            //Mastery within the forbidden magical system raises questions about the nature of good and evil, control, and the consequences of wielding such power. Aspects related to the concept of Mastery in forbidden magic include:
            `Good vs. Evil: The ethical debate on whether forbidden magic is inherently evil or if there is potential for good to emerge from it.`,
            `Control: Mastering forbidden magic without being consumed by its darkness is a significant challenge.`,
            `Threshold to Master: The dark or dangerous actions that must be taken to achieve mastery.`,
            `Limits to Power: Whether there are known limits to the potency of forbidden magic or if it has unforeseen consequences.`,
            `Commonness of Mastery: How frequently individuals achieve mastery in forbidden magic.`,
            `The Price of Mastery: The toll on the practitioner's soul and life for mastering such dark magic.`,
            `Guardians of Forbidden Knowledge: Masters who safeguard and regulate access to forbidden magic.`,
            `Covenants of the Forbidden: Secret societies or groups that govern the use of forbidden magic.`,
            `The Fall of Past Masters: Tales of past masters who succumbed to the darkness of forbidden magic.`,
            `Echoes of Redemption: Masters seeking redemption for their past misdeeds through the responsible use of forbidden magic.`,
            `Veiled Allegiance: Some masters secretly work against the dark forces behind forbidden magic.`,
            `Legacy of the Lost: Masters who inherit their knowledge and power from a lineage lost to time.`,
            `Puppeteer's Mastery: Forbidden magic masters manipulate events from the shadows to achieve their goals.`,
            `Darkened Teachings: Mastery is often passed down through disturbing and unsettling mentorship.`,
            `Rumors of Ascendancy: Some masters are rumored to have transcended their mortal form through forbidden magic.`,
            `Balance Seekers: Masters strive to maintain balance while wielding dark powers for a higher purpose.`,
            `Forbidden Symbiosis: The magic forms a symbiotic relationship with masters, granting them heightened abilities.`,
            `Taming the Beast Within: Masters must constantly battle the darkness within themselves to maintain control.`,
            `Undying Pursuit: Forbidden magic grants masters unnaturally long lifespans in pursuit of mastery.`,
            `Whispers of Redemption: The possibility of redemption for masters through the use of forbidden magic.`,
            `Suppressed Darkness: Some masters suppress their magic to avoid the lure of forbidden knowledge.`,
            `Veiled Exile: Masters may live in seclusion to protect the world from their dark powers.`,
            `Eclipsed Nobility: Masters of forbidden magic may come from noble backgrounds with hidden secrets.`,
            `Forbidden Healer: A master who uses forbidden magic for healing and restoration, despite its dark nature.`,
            `Veil of Misdirection: Some masters conceal their true intentions and actions while using forbidden magic.`,
            `Doomed Seeker: Aspiring masters may seek forbidden magic for noble reasons, unaware of the danger.`,
            `Forgotten Remorse: Masters may struggle with guilt and remorse for the harm caused by their magic.`,
            `Transcendent Sacrifice: Some masters willingly sacrifice themselves to contain the dark magic they wield.`,
            `Ancient Enigma: Masters embody the mystery and wisdom of ancient practitioners of forbidden magic.`,
            `Tragic Vigilance: Masters must remain vigilant to avoid the temptations that come with their power.`
        ]
        }
};



function magic() {
    const typeArray = Object.keys(magics)



    function findPure(){
        let pureChoice = [searchArray(typeArray)]
        document.getElementById("Magic").innerHTML = ''
        document.getElementById("Source").innerHTML = ''
        document.getElementById("Cost").innerHTML = ''
        document.getElementById("Potencies").innerHTML = ''
        document.getElementById("Accessibility").innerHTML = ''
        document.getElementById("Mastery").innerHTML = ''
        
        document.getElementById("Magic").innerHTML = 'PURE:'
        loopCountPrintList(pureChoice,"Magic")
        loopCountPrintList([searchArray(magics[pureChoice].Source)], "Source")
        loopCountPrintList(shuffleSlice(magics[pureChoice].Cost,2), "Cost")
        loopCountPrintList(shuffleSlice(magics[pureChoice].Potency,2), "Potencies")
        loopCountPrintList(shuffleSlice(magics[pureChoice].Accessibility,2), "Accessibility")
        loopCountPrintList(shuffleSlice(magics[pureChoice].Mastery,2), "Mastery")
    }
    function findDual(){
        let dual = shuffleSlice(typeArray,2)
        let primary = dual[0]
        let secondary = dual[1]

        document.getElementById("Magic").innerHTML = ''
        document.getElementById("Source").innerHTML = ''
        document.getElementById("Cost").innerHTML = ''
        document.getElementById("Potencies").innerHTML = ''
        document.getElementById("Accessibility").innerHTML = ''
        document.getElementById("Mastery").innerHTML = ''
        
        document.getElementById("Magic").innerHTML = 'DUAL:'
        loopCountPrintList(dual,"Magic")
        let souAr = []
        souAr.push(searchArray(magics[primary].Source))
        souAr.push(searchArray(magics[secondary].Source))
        loopCountPrintList(souAr, "Source")
        let cosAr = []
        cosAr.push(searchArray(magics[primary].Cost))
        cosAr.push(shuffleSlice(magics[secondary].Cost,2))
        loopCountPrintList(cosAr, "Cost")
        let potAr = []
        potAr.push(searchArray(magics[primary].Potency))
        potAr.push(shuffleSlice(magics[secondary].Potency,2))
        loopCountPrintList(potAr, "Potencies")
        let accAr = []
        accAr.push(searchArray(magics[primary].Accessibility))
        accAr.push(shuffleSlice(magics[secondary].Accessibility,2))
        loopCountPrintList(accAr, "Accessibility")
        let masAr = []
        masAr.push(searchArray(magics[primary].Mastery))
        masAr.push(shuffleSlice(magics[secondary].Mastery,2))
        loopCountPrintList(masAr, "Mastery")
    }
    function findTrio(){
        let trio = shuffleSlice(typeArray,3)
        let t1= trio[0]
        let t2= trio[1]
        let t3= trio[2]

        document.getElementById("Magic").innerHTML = ''
        document.getElementById("Source").innerHTML = ''
        document.getElementById("Cost").innerHTML = ''
        document.getElementById("Potencies").innerHTML = ''
        document.getElementById("Accessibility").innerHTML = ''
        document.getElementById("Mastery").innerHTML = ''
        
        document.getElementById("Magic").innerHTML = 'TRIO:'
        loopCountPrintList(trio,"Magic")
        let souAr = []
        souAr.push(searchArray(magics[t1].Source))
        souAr.push(searchArray(magics[t2].Source))
        souAr.push(searchArray(magics[t3].Source))
        loopCountPrintList(souAr, "Source")
        let cosAr = []
        cosAr.push(searchArray(magics[t1].Cost))
        cosAr.push(searchArray(magics[t2].Cost))
        cosAr.push(searchArray(magics[t3].Cost))
        loopCountPrintList(cosAr, "Cost")
        let potAr = []
        potAr.push(searchArray(magics[t1].Potency))
        potAr.push(searchArray(magics[t2].Potency))
        potAr.push(searchArray(magics[t3].Potency))
        loopCountPrintList(potAr, "Potencies")
        let accAr = []
        accAr.push(searchArray(magics[t1].Accessibility))
        accAr.push(searchArray(magics[t2].Accessibility))
        accAr.push(searchArray(magics[t3].Accessibility))
        loopCountPrintList(accAr, "Accessibility")
        let masAr = []
        masAr.push(searchArray(magics[t1].Mastery))
        masAr.push(searchArray(magics[t2].Mastery))
        masAr.push(searchArray(magics[t3].Mastery))
        loopCountPrintList(masAr, "Mastery")
    }
    function findComplex(){
        let c1 = shuffleSlice(typeArray,1)
        let c2 = shuffleSlice(typeArray,1)
        let c3 = shuffleSlice(typeArray,1)
        let c4 = shuffleSlice(typeArray,1)
        let complexAr = [c1,c2,c3,c4]

        document.getElementById("Magic").innerHTML = ''
        document.getElementById("Source").innerHTML = ''
        document.getElementById("Cost").innerHTML = ''
        document.getElementById("Potencies").innerHTML = ''
        document.getElementById("Accessibility").innerHTML = ''
        document.getElementById("Mastery").innerHTML = ''
        
        document.getElementById("Magic").innerHTML = 'COMPLEX:'
        loopCountPrintList(complexAr,"Magic")
        let souAr = []
        souAr.push(searchArray(magics[c1].Source))
        souAr.push(searchArray(magics[c2].Source))
        souAr.push(searchArray(magics[c3].Source))
        souAr.push(searchArray(magics[c4].Source))
        let cosAr = []
        loopCountPrintList(souAr, "Source")
        cosAr.push(searchArray(magics[c1].Cost))
        cosAr.push(searchArray(magics[c2].Cost))
        cosAr.push(searchArray(magics[c3].Cost))
        cosAr.push(searchArray(magics[c4].Cost))
        loopCountPrintList(cosAr, "Cost")
        let potAr = []
        potAr.push(searchArray(magics[c1].Potency))
        potAr.push(searchArray(magics[c2].Potency))
        potAr.push(searchArray(magics[c3].Potency))
        potAr.push(searchArray(magics[c4].Potency))
        loopCountPrintList(potAr, "Potencies")
        let accAr = []
        accAr.push(searchArray(magics[c1].Accessibility))
        accAr.push(searchArray(magics[c2].Accessibility))
        accAr.push(searchArray(magics[c3].Accessibility))
        accAr.push(searchArray(magics[c4].Accessibility))
        loopCountPrintList(accAr, "Accessibility")
        let masAr = []
        masAr.push(searchArray(magics[c1].Mastery))
        masAr.push(searchArray(magics[c2].Mastery))
        masAr.push(searchArray(magics[c3].Mastery))
        masAr.push(searchArray(magics[c4].Mastery))
        loopCountPrintList(masAr, "Mastery")
    }
    let a = rollDice(100)
    if(a >75){
        findPure()
    } else if (a > 50) {
        findDual()
    } else if (a > 25) {
        findTrio()
    } else {
        findComplex()
    }
    };
