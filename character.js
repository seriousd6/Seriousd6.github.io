function buildChar() {
    //RACE GENERATOR-----------------------------------------------------------------------------
    //Race & Features Array
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
    var raceFeatures = {
            'Human': [],
            'Dwarf': [],
            'Elf': [],
            'Gnome': [],
            'Half-elf': [],
            'Halfling': [],
            'Dragonborn': [],
            'Tiefling': [],
            'Genasi': [],
            'Aasimar': [],
            'Half-Orc': [],
            'Tabaxi': [],
            'Warforged': [],
        }
        //Probability and Weighting
    function raceReturn() {
        var randNum = Math.floor(Math.random() * 100);
        if (randNum > 98) {
            var uRare = races[4];
            var uRareIndex = Math.floor(Math.random() * uRare.length);
            var uRareRace = uRare[uRareIndex];
            return uRareRace;
        } else if (randNum > 95) {
            var vRare = races[3];
            var vRareIndex = Math.floor(Math.random() * vRare.length);
            var vRareRace = vRare[vRareIndex];
            return vRareRace;
        } else if (randNum > 80) {
            var rare = races[2];
            var rareIndex = Math.floor(Math.random() * rare.length);
            var rareRace = rare[rareIndex];
            return rareRace;
        } else if (randNum > 50) {
            var unCom = races[1];
            var unComIndex = Math.floor(Math.random() * unCom.length);
            var unComRace = unCom[unComIndex];
            return unComRace;
        } else {
            var com = races[0];
            var comIndex = Math.floor(Math.random() * com.length);
            var comRace = com[comIndex];
            return comRace;
        }
    };

    function printRace() {
        console.log("----Race----:\n " + raceReturn() + "\n");
    };
    printRace();

    // CLASS GENERATOR----------------------------------------------------------------------------
    //Class Array
    let classes = [
            [
                'Bard', 'Cleric', 'Fighter', 'Paladin', 'Ranger', 'Rogue',
            ],
            [
                'Barbarian', 'Druid', 'Monk', 'Nomad',
            ],
            [
                'Sorcerer', 'Warlock', 'Wizard', 'Artificer', 'Summoner',
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
            'squatter', 'Urchin', 'Vagabond'
        ],

    };
    //Pick a profession
    function findProf() {
        var fieldSearch = Object.keys(professions);
        var whatField = Math.floor(Math.random() * fieldSearch.length);
        var getFieldName = fieldSearch[whatField];
        var getSubFields = professions[getFieldName]
        var whatSubField = Math.floor(Math.random() * getSubFields.length)
        var npcProf = getSubFields[whatSubField];
        return npcProf + ", Subfield of " + getFieldName;
    };
    //Pick a class or profession
    function classReturn() {
        var randNum = Math.floor(Math.random() * 100);
        if (randNum > 98) {
            var cuRare = classes[3];
            var cuRareIndex = Math.floor(Math.random() * cuRare.length);
            var cuRareClass = cuRare[cuRareIndex];
            return cuRareClass;
        } else if (randNum > 95) {
            var cvRare = classes[2];
            var cvRareIndex = Math.floor(Math.random() * cvRare.length);
            var cvRareClass = cvRare[cvRareIndex];
            return cvRareClass;
        } else if (randNum > 85) {
            var cRare = classes[1];
            var cRareIndex = Math.floor(Math.random() * cRare.length);
            var cRareClass = cRare[cRareIndex];
            return cRareClass;
        } else if (randNum > 65) {
            var cCom = classes[0];
            var cComIndex = Math.floor(Math.random() * cCom.length);
            var cComClass = cCom[cComIndex];
            return cComClass;
        } else {
            return findProf();
        };
    }

    function printClass() {
        console.log("----Class----:\n " + classReturn() + "\n");
    }
    printClass();
    //PERSONALITY GENERATOR----------------------------------------------------------------------
    var personality = [];

    var goals

    var fears


    //CATCHPHRASE and QUIRK GENERATOR-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -
    var catchPhrase = [
        "What happens happened and will happen again!", "I’d buy that for a gold…", "Yadda yadda yadda", "You know what they say…",
        "I hate the Underdark. It’s too dark.", "Don’t feed the owlbears!", "By my Great Aunt Myrra’s beard!",
        "I once knew a goblin who talked like you, I didn’t know him for long if you get what I mean.",
        "Do you think this belly is just for show?!", "You know what they say, half elves are just the mules of the humanoids.",
        "I could drink the lake dry if I ever felt like It!", "You’ve got some nerve, looking at me and all.",
        "My father is a Lord, do you know what that means? It means that I am more important than you.", "Tiamat did nothing wrong.", "Bababooy, Bababooy, his head went kablooy.",
        "As it was foretold…", "So it has come to this?", "I’m a PASS-A-FIST. Here, catch! (Punch random PC)", "If something is nonlethal then you aren’t trying hard enough.",
        "I wish we were better strangers.", "I have declared war on the Moon! For too long it has hung unmonitored and unsuspected in the sky. It has gained an enormous tactical advantage!",
        "May the bridges I burn light the way.", "May your knives drink deeply. (A farewell to fellow soldiers)", "If you’re gonna be dumb you gotta be tough!",
        "(When forced to do something that seems obviously stupid and pointless.) Oh good, another windmill to tilt at.", "Dishonor on you. Dishonor on your family. Dishonor on your COW!",
        "You look better in RED! (Said after inflicting damage.)", "May madness and disease visit you often. (Say it kindly!)", "When all you have is a hammer. Everything else becomes the nail.",
        "You’re up against the wall, and I am the fucking wall", "Never let up on your foe. To give them even a moment’s chance to recover was folly.", "Take it up with my lawyer.",
        "That’s the way the meatball bounces!", "…and hey! Stay hydrated.", "Oh Honey don’t do that…", "Water you doing!?", "Peasants.", "I’ll drink you under the table, scrub!",
        "I’ve wrastled [Incredibly doubtful monster name]s tougher than you, boy!", "We huntin’ tonight!", "I had something for this.", "DANGER ZONE!",
        "You can tell that this is magical, because of the way that it is.", "The wheel weaves as the wheel wills.", "Well you can go [insert setting-specific-swear-word] yourself.",
        "Drugs won’t make you happy, but sometimes they help.", "I haven’t seen something this bad since Briarwillow Creek…", "Don’t do anything that your evil mirror twin would do!",
        "That’s rough. [hands you a fresh peach] Maybe this’ll help.", "You wanna die bitch?!", "Whiskers and potash!", "Let me just say…", "Can it burn? Maybe we should just burn it.",
        "[After every order or statement by the players:] Why? Seriously, I wanna know.", "They can’t hurt ya if ya don’t believe in ’em.", "And so the turn tables, are turning.",
        "Looks like the glove is on the other foot.", "Curiousity killed the dog.", "What has 1 thumb and 2 smiles? – 2 headed ogre who just lost his arm.", "By Markovia’s thighbone!",
        "What in the Holy Light of the Morninglord is going on here?!", "Better in than out, I say.", "Where I come from we have a saying [Insert half of a proverb here].",
        "Bang a gong, let’s get it on!", "I kick ass for the [insert diety]!", "I think I’m allergic to that.", "Something stinks, and it ain’t my toe fungus.",
        "You know, the best thing about brain damage is you get to keep hearing the same jokes over and over and they never stop being funny. (repeat as often as possible, even in the same conversation)",
        "This is your burn notice.", "Never a lucky day…", "A balance must always be paid.", "This, too, is the will of the gods.", "Weapons are for weak men, mercy is for weak women.",
        "Oh, you have swords.", "It has been foreseen.", "You have made your choice.", "All will be revealed…", "In all the nine hells I have never seen something so…", "Redemption is overrated.",
        "My mother always told me to have mercy. Unfortunately, for you I’m a bit of a rebel.", "Let me tell you how this is going to go.", "I was never here.", "Time to feed the worms.",
        "Happiness is like a mimic, deceptive and deadly.", "I hope your next wound is unique.", "What wonderful art I could make with a soul as colorful as yours.", "The stars align in my favor.",
        "Foresight makes life so boring.", "Do you ever wonder what life would be like if you just disappeared?", "And thus the cycle repeats…", "You lie? You die.",
        "Keep your gold close and your dagger closer.", "Insanity is law in a land driven by chaos.", "Yeah, I’m gonna stop you right there.",
    ];

    function findPhrase() {
        var phraseIndex = Math.floor(Math.random() * catchPhrase.length);
        var catPhrase = catchPhrase[phraseIndex];
        return catPhrase;
    };

    function printPhrase() {
        console.log("----Catch Phrase----:\n " + findPhrase() + "\n");
    };
    printPhrase();


    var personalityQuirk = [
        "You’re a vegan, and make sure everyone you meet knows.", "You’re obsessed with personal hygiene.", "You don’t like people you don’t already know. People can still make it into your good graces as you get to know them.",
        "You hate getting wet. So much so, you can’t even remember the last time you bathed.", "You actively avoid words with the letter S, due to a lisp you find embarrassing.", "You scratch your right ear whenever you lie.",
        "You can’t stand green beans/potatoes/rice, to the point where you can’t eat anything that has even touched it on the same plate.", "When someone makes you flustered, you punch their shoulder.",
        "Whenever something surprises you, you get hiccups.", "You start crying after any adrenaline drop (a fight ends, you get startled…). People mistake this for sadness, but it’s just a bodily function.",
        "If you yell more than a few words, your voice gets hoarse. You avoid yelling, therefore people just assume you are always calm and collected.", "You compulsively scratch (roll 1d4): 1. the nape of your neck; 2. your scalp; 3. your lower stomach; 4. your nose.",
        "You bite your fingernails/pick your nose.", "Whenever you cry, you try to catch the tears with your tongue.", "You don’t notice the volume of your voice, often embarrassing your companions in social gatherings.",
        "You always have to one-up people when it comes to (roll 1d4): 1. how powerful you are (physically or magically); 2. your sexual prowess/achievements; 3. how good of a friend you are; 4. how bad you have/had it.",
        "You have a mother/father/sister/brother complex, and always love/hate anyone resembling them.", "You chew with your mouth open.", "You pick between your teeth for leftovers with your fingers, and flick them away.",
        "You insist you’re ambidextrous, although you clearly aren’t. You will go as far as using your off hand to ‘prove’ it, and always make vapid excuses for your shortcomings with it.",
        "You claimed to know [obscure language] once to impress someone, and now hope never to meet someone whom actually speaks it.", "You believe in love at first sight, and practice what you preach! You become instantly enamored with the first attractive person you see in a town.",
        "No matter how savvy you are, you can never tell when (roll 1d4): 1. someone you aren’t into is hitting on you; 2. someone rejects you politely without firmly saying no; 3. someone compliments you to be polite; 4. someone tries to change the subject of off embarrassment rather than dishonesty.",
        "You always “correct” people about the pronunciation of spells and anything related to arcana, always putting the emphasis on the wrong syllable. For example saying “Maygeek mysle” instead of magic missile.",
        "You try to fit in with other races by trying to uses their terminology and accents as well as believing in the stereotypes given to that race which just makes you come off as condescending and racist.",
        "The more people there are, the more quiet you are.", "You get extremely defensive when someone disagrees with you.", "You panic when you are suddenly put into the spotlight.",
        "You just can’t stop talking about your preferences. You always have to give your opinion, even to strangers.", "You can’t remember people’s faces well.",
        "You don’t have a censor, and always let people know exactly what you think.", "If some says any number lower than 8, your must pass a willpower check or keep counting to 8.", "You are very modest, and must cover everything but your head whenever possible. If someone were to see you without sleeves you would blush. If someone saw you shirtless you would be uncontrollably stuttering, and so on with levels of embarrassment.",
        "If you see a hairy mammal that is not trying to kill you, you are obligated to try to pet it, even if it is an NPC/PC.", "Any race smaller than you, you treat as cute. You talk to it as though it were a small pet or baby, (even goblins).",
        "You get drunk and start talking in a language other than common. Usually it is just gibberish and people who actually speak the language are offended.", "If there is no light or you are unable to see, while you are not sleeping. You pee yourself.",
        "You know 100 dad jokes and always say one if no one is talking or there is an awkward silence.", "You are very bad at eating with utensils. If you use a fork, you must pass a test, (GMs choice) or stab your tounge.",
        "You sneeze whenever someone says your name.", "You forget people’s names. Whenever talking to someone you must pass an int check or say the wrong name. Once you get it right without being reminded you remember the name of that person.",
        "You hate sand, because it’s course and rough and it gets everywhere.", "You’re extremely conscious of proper posture. You’re constantly standing or sitting up straight.",
        "You have a huge smile that never reaches your eyes.", "You’re constantly humming a tune, not always the same one. It’s very soft and most of the time you don’t even know you’re doing it. If asked, you will say the tune is from a particular song, but anyone who makes a DC 15 History check will know it’s not the tune from that song at all",
        "While not knowing much of your deity, you still heavily worship them. You often with confidence misquote from scripture, or make up a quote in your head.", "You don’t feel comfortable unless you’re chewing on something. If you’re not eating there has to be a toothpick, stem of grass, piece of straw or a pipe in your mouth.",
        "You can’t abide having a wrinkle in your socks. If there’s something off about them you can’t concentrate on anything until you’ve taken your boots off and corrected it.",
        "You give nicknames to everyone and everything. How flattering they are depends on how you think of the person or object.", "You refer to yourself in the third person. As if your body were not your own…",
        "Whenever you see a dog you immediately try to pet it. If you are attempting to resist the urge, you must pass a DC 15 Animal Handling check.", "You frequently try to rhyme your sentences. You are very bad at it…",
        "Before asking a question you say “more inquiry needed,” you also end conversations with “conversation over”.", "You absolutely refuse to stay in the second floor of any building for an extended period of time.",
        "You enjoy showing off your prowess with other languages besides common to the point of annoyance to others.", "Art is your passion. You feel compelled to sketch people you meet.",
        "You cannot stand the sound of people snapping their fingers.", "You are very forgetful about past events. You tell the same childhood story several times a day.",
        "You have memorized every holiday of the year, and will do nothing until proper celebration has been made on the days of.",
        "You have lived vicariously through your older siblings/parents. All your interesting tales are things they have done.", "You are illiterate, and will stop at nothing to make sure no one knows this fact.",
        "You cannot pronounce your own name correctly.", "Sometimes mid conversation with someone you space out or pay more attention to what’s going on around you (a bird in the distance or whatever) unless the other people are engaging you, monologues bore you.",
        "You have a tendency to spit on the floor.", "You always reference how your mother would feel about any topic in conversation.", "You never look directly into someone’s eyes, instead gazing slightly to the right or left of their face when speaking to them.",
        "Anytime someone asks a question, you ask for “the magic word”. If they DO ask the question by saying “Please”, you assume they have an ulterior motive.",
        "You know “fun facts” about everything. They are usually wrong.", "You are absolutely sure everyone taller than you is on stilts. You eyeball their legs and sometimes attempt to prove this fact.",
        "When drinking water, you must purify it or filter it in some way. The thought of dirty water makes you ill.", "You absolutely REFUSE to sleep without a trinket of some kind. (a blanket, a stuffed animal, a pillow, etc.)",
        "When you see a child’s toy, you must pass a Wis 10 save or you must play with it. You’re a child at heart and kids always make you smile.", "You believe the world to be flat (or cubed if it happens to actually be flat).",
        "You believe that food must have an excessive amount of spices in it…more than anybody else appreciates. You also insist on cooking.",
        "Your extremities (feet, hands) are always freezing. Either bad circulation, a family curse, or strange genes in the bloodline is the cause.",
        "Every time you sit near a candle, you try your best to put it out with your fingers. You are rarely successful.",
        "You occasionally blink really hard, rub your eyes, and then look around as if it’s the first time seeing everything around you.",
        "You are completely convinced that everyone else has the exact same prejudices as you.",
        "You are on the hunt for a familiar. Every day, you pick a new creature or NPC and follow it/get it to follow you.", "You tend to clinically diagnose other people’s physical and emotional flaws in front of them.",
        "You strongly identify with another species, to the point of trying to pass as them.", "Each night, you have a vivid prophetic dream of your own messy death the next day.",
        "You name all of your actions as you execute them, ranging in volume from a quiet murmur to a earsplitting yell.",
        "You need to look cool at all times. You obsessively map out dramatic entrances, witty one-liners, and elaborate combat moves.",
        "You are embarrassed by the sound of your laugh, and use all your willpower to not let a single giggle escape.",
        "You are needlessly maternal, and will not rest until all of your friends (and some strangers) are well fed and cared for.",
        "You zone out whenever someone takes longer than five seconds to explain something, but pretend to have understood it perfectly.",
        "You spend all of your free time honing your skills at something extremely obscure and probably useless.",
        "You have an overly guilty conscience, and will try to make up for crimes that strangers have committed.",
        "When idle, you make neat stacks of nearby objects, including small animals and other people’s valuables.",
        "You introduce yourself by a slightly different name every time.",
        "Your left hand often wanders without your knowledge.",
        "You often challenge people to drinking contests of your own invention.",
        "You languish under such a labyrinthine series of opinions about the world that each new topic provokes a strong emotional response. [1: Horror. 2: Rage. 3: Grief. 4: Skepticism. 5: Lust. 6: Delight.]",
        "You always speak in hypotheticals.", "You have to stop whatever you are doing and look someone directly in their eyes before you talk to them.",
        "You constantly polish any metal you are holding or have on you.", "You adjust your glasses when you’re nervous.", "You overexaggerate when telling stories of your past deeds.",
    ];

    function findQuirk() {
        var quirkIndex = Math.floor(Math.random() * personalityQuirk.length);
        var npcQuirk = personalityQuirk[quirkIndex];
        return npcQuirk;
    }

    function printQuirk() {
        console.log("----Personality Quirk----:\n" + findQuirk() + "\n");
    }
    printQuirk();


    var physicalQuirk = [
        "A long, glorious beard.Each braid represents another person that has asked him what the braids mean.",
        "The npc has a cleft cut into their nose.",
        "The npc has many tiny tattoos across their face starting from the corner of their mouth to the edge of their eye.",
        "The npc has an extra hand coming out of their right arm the hand is as small as a child’ s and is blackened and seems to be of no use.",
        "The NPC is missing a tooth.",
        "One of the NPC’ s arms is a different tone, length, and has a different shape of hand than the other.",
        "The NPC has been cursed to have a part of their body, (arm, leg, hand, maybe even a tail…) that is of a different race.(ex.A human with the hand of a tabaxi…)",
        "The NPC has many scars and callouses along their forearms, perhaps being formed over many brutal sparring sessions.",
        "The NPC has long, slender fingers, perhaps from living an easy life in the high class or perhaps from living a life scrounging in the streets.",
        "The NPC has well - toned leg muscles.Clearly, they are used to running.",
        "The NPC has bags under their eyes, perpetually unable to sleep a full night.",
        "The NPC has meticulously groomed hair(beard and mustache as well if applicable) and is almost never seen with an out - of - place hair.",
        "The NPC wears an array of gaudy and flamboyant jewellery, supporting itself on a cane embedded with a poorly cut ruby too big to be real.It’ s ears sport a multitude of filigree ear rings, as if to distract from it crooked and yellow teeth.",
        "The npc’ s eyes change color with their mood.",
        "The npc is abnormally tall / short for their race.",
        "The NPC’ s left hand has steel claws that appear to be artificially attached.",
        "The NPC has a very faint tattoo on their forehead that requires a DC 15 Investigation check to make out clearly.The tattoo is enchanted to cast suggestion on someone who successfully investigates the tattoo.The suggestion is“ Stop looking at my forehead.”",
        "If a man, the NPC has a surprisingly large butt / hips.",
        "NPC has no hair.",
        "NPC has a mohawk.",
        "NPC has a beard with beads in it.",
        "NPC has half of their hair blonde, and has one blonde eye on the same side.",
        "NPC is carrying a large sack.On the sack are the letters TBD.",
        "NPC doesn’ t have eyebrows, but instead has tattooed eyebrows slightly too high, which gives a look of permanent surprise.",
        "PC is covered in tattoos of the cities they have been to.Each one best representing that city.",
        "NPC has a mouth on their back that says mean stuff about them.This would usually sadden people but this just pushes them to complete their goals more.",
        "NPC has a horn coming out of their forehead that they are very self conscious about. They constantly shave it off if they have time.",
        "NPC has scales on his legs.(If they are a species that usually has scales then their legs are human.)",
        "NPC has no natural teeth left. Luckily for him his enemies had some. His jaw is full of random teeth that are surgically placed in .They may not be fabulous but they sure is scary!",
        "NPC has a magical tattoo that can answer riddles.",
        "NPC is missing his left eye.He constantly forgets which eye is actually gone.",
        "NPC has acid burn scars on both of his hands.",
        "NPC is fascinated by jewelry so much so that they are wearing so much jewelry that it weighs them down.",
        "NPC has a scar around their neck.",
        "NPC has orange eyes that glow when near heroic people.",
        "NPC has white eyes that glow when near neutral good to lawful good holy symbols.",
        "NPC has red eyes that glow when near blood.",
        "NPC has green eyes that glow when near poison.",
        "NPC is extremely muscular but lazy in actions.",
        "NPC has bright yellow hair that glows in the dark.",
        "NPC has the tail of a rat.",
        "NPC is blinded in daylight but can see perfectly in the dark.",
        "NPC was given a curse by a witch when he was a child and now has a finger on his right arm that points in the direction of the closest person that wants to kill him.",
        "NPC has a extremely chapped lips.",
        "NPC has a tattoo of a map leading to an X.Doesn’ t remember when it got there or why it’ s there.",
        "NPC has a mechanical limb that they cannot fully control. It does the motion for whatever he is thinking even if it’ s socially wrong.",
        "NPC has a horrid burn mark running down from their left elbow to their hand.",
        "The NPC is missing his / her left arm, and doesn’ t seem quite used to functioning without it.",
        "The NPC has a jewel implanted in the place of a lost eye.",
        "The NPC has a distracting mole.",
        "The NPC has one long fingernail, presumably left unfiled for strumming an instrument.",
        "The NPC has a violet bruise on the bone of their cheek.",
        "The NPC has acne scars pockmarked across their face.",
        "The NPC has a snaggletooth long enough to be a fang.",
        "The NPC has one leg severely deformed, they carry themselves around on double crutches.",
        "The NPC has a pair of thick spectacles that don’ t fit.",
        "The NPC has thick, greasy dreadlocks from years of improper washing.",
        "The NPC has one eye swollen over from a recent fight.",
        "The NPC’ s mouth is permanently crooked, giving them a cocky smirk even in serious moments.",
        "The NPC has not cut or groomed his / her hair since he / she was defeated by his / her rival 8 years ago.",
        "Scars… Everywhere.",
        "The NPC has a beard that is visibly fake.",
        "The NPC has an eye on the palm of his / her right hand that he / she tries to hide with a fingerless glove.",
        "NPC has one blue eye and one brown.",
        "NPC’ s face has splotches the color of red wine.",
        "NPC has a sparse beard, like underarm hair.",
        "NPC has bushy eyebrows that waggle when they talk.",
        "The NPC has no nose.He has one big hole where the nose was supposed to be.",
        "NPC walks with a significant limp requiring a cane to help them walk.",
        "NPC has a very muscular upper body, but their legs look very underdeveloped.",
        "Male NPC talks with a define lisp and tends be be flamboyant with arm gestures.",
        "NPC has 6 fingers.",
        "NPC is androgynous.Very difficult to glean gender.",
        "NPC has a Hunchback and disfigured face with extra growths.",
        "NPC has whats left of a hand still attached.It looks like it was crushed and was never amputated.",
        "NPC has abnormally large forearms and / or calves.",
        "The NPC is wearing an obvious wig.",
        "The NPCs left eye has three pupils.",
        "The NPC constantly smells of rosemary and brimstone.",
        "The NPC has a long pointy nose that curls and wiggles according the NPC’ s emotions.",
        "A holy symbol is branded onto the NPC’ s right hand.",
        "The NPC’ s teeth are made out of various rare metals.",
        "Exotic runes are carved on the NPC’ s forearm.",
        "NPC’ s hands are stained multiple colors.",
        "NPC has a forked tongue.",
        "NPC has piercings all over their body.Bars and rings cover them.",
        "NPC is blind / deaf.",
        "NPC has ashen skin and no hair.",
        "NPC has sharpened teeth and loves to smile.",
        "NPC is unusually hairy, having thick hair on almost all visible skin apart from around eyes and palms.",
        ",NPC always wears bright, vibrant clothing.",
        "NPC constantly twitches.They can’ t stay still.",
        "The skin on the NPC’ s left forearm is transparent.",
        "There are small mushrooms on the back of the NPC’ s neck.",
        "The NPC has small woodland critters in their hair.",
        "The NPC uses overly - exagerated movements for everything.",
        "The NPC is slowly rotting away.",
        "The NPC has incredibly beautiful features.One of the most beautiful people you’ ve ever seen!",
    ];

    function findPhysQuirk() {
        var physQuirkIndex = Math.floor(Math.random() * physicalQuirk.length);
        var physQuirk = physicalQuirk[physQuirkIndex];
        return physQuirk;
    };

    function printPhysQuirk() {
        console.log("----Physical Quirk----:\n " + findPhysQuirk() + "\n");
    }
    printPhysQuirk();


    //SONG, DISCUSSION  GENERATOR-------------------------------------------------------------------
    var discussionTopics = [
        'Love', 'Battle (before the events of the campaign)', 'Hardship', 'A personal triumph', 'Friendship', 'Family', 'Faith or religion', 'Survival', 'Good', 'Evil', 'Politics',
        'A formative event in life', 'Your personal philosophy', 'Your culture', 'A culture you have experienced unlike your own', 'One of your hobbies', 'Your passion',
        'Recent events (your opinion on it, how it affected you, etc.)', 'Something funny', 'Your greatest rival', 'Something you admire/dislike about another party member',
        'Something you’ve stolen (or seen somebody steal)', 'A controversial opinion', 'What you would change about the world', 'Your education', 'Your childhood', 'The scariest moment of your life',
        'Science and technology', 'A regret or mistake', 'A foolish childhood dream', 'Heartbreak', 'A painful memory', 'Something you like about yourself', 'Something you dislike about yourself',
        'Revenge', 'A favorite tale of a hero of old', 'An encounter with nature', 'Your place in the world', 'Something you still can’t explain', 'A night you barely remember', 'An internal struggle',
        'The best meal you’ve eaten', 'The weirdest meal you’ve eaten', 'Celebration', 'Music', 'Art', 'An item you own', 'Deception', 'Betrayal', 'Ingenuity', 'Losing something important',
        'Doing the right thing', 'Doing the wrong thing', 'Being accused of something you didn’t do', 'Seeing something you shouldn’t have', 'Money', 'An interaction with a stranger', 'A monster',
        'The worst person you’ve ever known', 'Someone you idolize', 'A pet peeve', 'A sexual encounter (or simply a romantic one, if the player is uncomfortable by this)', 'Drugs', 'Anger',
        'Someone you miss', 'Something you will never do again', 'A hidden talent/skill', 'Beauty', 'A good conversation you once had', 'Justice', 'Failure', 'Magic', 'Being in over your head',
        'Teamwork', 'Jealousy', 'Prejudice', 'A realization you had about yourself', 'Something you’ve realized since the start of this campaign', 'A long journey', 'Everything going wrong',
        'The best day of your life', 'The worst day of your life', 'Trying too hard', 'A pet you once had (or someone else’s)', 'An irrational fear', 'A lie you’ve told', 'Rebellion', 'Trust',
        'What you miss most from back home', 'Fashion/clothing', 'A game', 'Your hope for the future', 'If you could go back in time', 'Your thoughts on children', 'Feeling powerful', 'Feeling helpless',
        'Abandonment', 'Finding something or someone you had lost', 'The greatest prank you ever pulled/witnessed', 'Feeling like the universe (i.e. the DM) is out to get you',
    ]

    function findDisctopic() {
        var topicIndex = Math.floor(Math.random() * discussionTopics.length);
        var discTopic = discussionTopics[topicIndex];
        return discTopic;
    }

    function printDiscTopic() {
        console.log("----Discussion Topic----:\n " + findDisctopic() + "\n");
    }
    printDiscTopic();

    var bardSongs = [
        "'Snuffed The Magic Dragon’ – A song about slaying a dragon that has terrorized the countryside. This song has a part two called ‘Stuffing The Magic Dragon’ in which the party has the dragon stuffed and brought to their castle.",
        "‘The Deep One’s Sea Shanty’ – To anyone who can’t speak Aquan this sound sounds like an upbeat sea shanty sung in another language. To those who do speak Aquan it tells the story of ‘The One who causes the waves’ and how he fought the gods themselves to reclaim the sea as his own.",
        "‘Lycan Virgin’ – Famous wenching song punctuated by wolf howls. Werewolves struggle to resist joining in during these parts, as does anyone else who has had a few…",
        "‘Crossbow’ – A song about a Ranger who rides into town to collect a bounty, alive or dead, against the Barbarian Reckless Redd. ‘No one dared to ask his business, no one dared to make a slip, ‘cus the Ranger there among them had a crossbow at his hip.’",
        "‘The Wizard and the Wren’ – A children’s song about a wizard who built a wooden town taller than any in the land that was undone by a wren who needed twigs to build its nest.",
        "‘The Crown on the Head and the Crown on the Heart’ – An epic poem describing a king who was usurped and his journey of growth on his return to the throne.",
        "‘Ashkeeper’ – A slow and somber dwarven chant about the history of one of their oldest and deepest fortresses.",
        "‘Our Son Arsen’s Arsine Arson and Parson Carson’s Incarceration Assertion’ – This bar song is known for being a dangerous tongue twister, and requires a DC 20 perform or linguistics check to sing without a serious mouth injury. Failing the check results in being unable to sing or speak for 1d6 hours.",
        "‘My Shortest Love’ – a song about the love between an elf and a halfling (hence “shortest”).",
        "‘The Seven Dwarves’ – song about how seven dwarves help to rescue a human maiden poisoned by a female wizard.",
        "‘Blasphemy Song’ – a rhyming song where every verse is an insult to a god. It is usual sung at a speedy pace. Worshipers say any bard who sings the song will face divine retribution, but for most bards, this wasn’t their last song.",
        "‘The Seven Screw-ups That Saved the World’ – A song about an adventuring party in which the members kept dying but still managed to stop the apocalypse. Each verse is how they helped the party, and how they died is in the chorus: ‘There were Seven Screw-ups in the party in all, One sang with the banshee in the hall and then there were Six Screw-ups in the party in all’ Popularly altered to sing the praises of other unfortunate adventuring groups.",
        "‘Rocking Chair’ – A calm ballad about an old elven lady remembering the times when she was young and fierce.",
        "‘Cold Blows the Wind’ – The love ballad of a budding necromancer and the lover she lost to the sea.",
        "‘Letters in the Sky’ – A tragic tale about a prince exiled to the sun and a princess exiled to the moon, and how they can only express their love for each other by arranging the stars into messages. Usually, it ends with the performer gazing skyward on the final chorus.",
        "‘Pahoot’ – A children’s song (best played on the flute or piccolo) that parents roll their eyes at while their children giggle. It features verses about the exploits of Pahoot, the flatulent goblin, who somehow always gets the last laugh whenever he’s ostracized for his odor.",
        "‘Where You’ve Been’ – A song about a ranger who searches for his lost love, using his tracking skills, but he’s delayed by his memories of the locations he visits. At the end of the song, he finds his love waiting for him.",
        "‘Behind Blue Scales’ – song by a blue dragonborn who wants to break free from chromatic influence.",
        "‘What’s In A Bottle Of Elfish Wine’ – A popular song among taverns owners and their patrons. This fast paced song is widely known and adapted by everyone who sings it.",
        "‘The Night Groomer’ – a tragic story about a night time barber who was killed by a customer that transformed into a werewolf.",
        "‘The Lonely Golem’ – A song about a statue coming to life and starting a quest to find friends, forgetting that its job was to protect an ancient weapon built to destroy nations." <
        "‘The Shortening of Meradian Finn’ – A Dwarven drinking song with thirty-eight official verses (and countless unofficial ones), the song recounts the punishment meted out against an Elven noble who stole from a Dwarven treasury. The chorus ends with a rousing slamming of glasses and a ‘in the end, he never did again!’ It is considered poor taste by many elves, which helps account in part for its popularity." <
        "‘The Bawdy Body of Biddy Badee’ – A raucous account of an old woman accidentally restored to youth and beauty. The song makes liberal use of alliteration and plays on words: ‘her newly charmed charms were enchanting enchantment; passing by barracks led to guardsman advancement…’",
        "‘The Cruel Changeling’ – A mournful ballad of a wandering bard falling for a woman at a fair, only to discover that she is wearing another’s face.",
        "‘And All for a Turnip’ – A song best sung as a round. It tells the story of a hungry halfling and his incredible exploits finding a snack.",
        "‘I Eldalië Nairii (sometimes translated as The People Mourn)’ – An Elven Dirge describing the loss of Cyrindes Flestivel, a beautiful and kind mage, to a spreading plague, along with many of her people. A melancholy ode to loss, some have taken it as a representation of the Elves’ sense of mourning for the loss of their brighter world.",
        "‘I Eldalië Snuiiiiii (The last word is used to sound like snoring or deep breathing)’ – A parody of the Elven Dirge ‘I Eldalië Nairii’, the song is of unknown source; it tells of an Elven bard singing the dirge, while the listeners fall asleep from boredom. A sure way to insult the singer of such a dirge, it is best sung with as much false pomposity as possible.",
        "‘But the Gnome Was Never Seen’ – A children’s song, used to remind Gnomish youths about the importance of caution and care.",
        "‘Adam the Easygoing’ – A relaxed song telling the tale of the titular Adam, a large, pudgy human paladin with an odd knack for befriending those he defeated in combat.",
        "‘I Write the Spells’ – A catchy if somewhat easily grating little song of unknown origin. If sung, it makes certain wizards go absolutely berserk.",
        "‘Nyarna Nwalcamun’ – The Saga of the Hero Grefedd and his journey to destroy the sentient cursed sword Nwalcamun. Traditionally, the climactic final battle scene is punctuated by the beat of a hammer on an anvil, representing Grefedd’s smashing of Nwalcamun while under attack by a drow army.",
        "‘The Green Eyes of Mallistari’ – The wooing song of a human woodsman for a half-elven maiden ‘met in a shady glade.’ The song is notable for a memorable bridge, often used when teaching the lute.",
        "‘Ga-Grosh For-Thaash’ – A song adapted from an Orcish marching anthem, useful for learning the rudiments of Orcish.",
        "‘The Oysters of Miss Marchelle’ – A sea shanty, recounting the joys of stopping in port at an establishment called ‘Harbor Belle.’ The song declares that ‘no sailor can resist the delight of the oysters of Miss Marchelle.’ The shanty, unlike many such songs, is not clearly innuendo, although it certainly may be (and many sailors sing it as such).",
        "‘Arnash Quadmatter’ – A song mocking the quintessential absent-minded wizard, referring to the foibles caused by having ‘his nose in a book, a book, a book…’",
        "‘The Missing Child’ – A mournful Elven song about a mother looking for her lost child, eventually going mad with grief and drowning herself, only to rise again as a banshee." <
        "‘Grandma Got Eaten By An Owlbear’ – A Popular song in winter months reminding people that they shouldent allow their elderly ex adventuring grandmother to attempt to wrestle monstrosities.",
        "‘You Can Just Call Me The Gnome’ – A fast-paced, silly song telling the increasing exploits of Hamish McTamish, a fictional gnome adventurer. Each time the chorus is sung, Hamish’s name is lengthened with more titles (the last chorus includes as many silly titles as the singer can think of and can sing in a single breath) followed by ‘but you can just call me the Gnome!’ Although believed to be human in origin, gnomes love the song, and an informal competition has sprung up as to the longest final chorus. The current record belongs to Sprigvill Gaudynack, who (via both her own talent and magical augmentation) kept the last chorus going for three and a half minutes.",
        "‘Callaud’s Pre-funeral Dance’ – A sprightly instrumental air for country dances. If played with a performance check DC 18 or higher, it functions like ‘Otto’s Irresistible Dance’ for anyone not in combat or threatened (i.e. it will make listening townsfolk break out into dance, but not if you are in the midst of robbing their homes).",
        "‘Long, Gone Galangal’ – A love story told through Gamelan music about an adventurous Chef seeking a rare root in the forest. Instead of finding it, they find the love of their life. The song is quite long, requires a large number of musicians to play properly, and has a happy ending.",
        "‘Untranslateable Orcish Proverb’ – A morality tale operatically told through Carved Masks, Huge Percussion Instruments (Taiko style Drumming), Slapstick Pantomime, and Throat Singing techniques. A classic of High Orcish culture, now practically lost to time and the collapse of High-Orcish society. The choregraphy is quite energetic.",
        "‘Great-Grandmother Will Enjoy Eating Your Flesh An Orchestral Eladrin Morality Tale from the Far Fey Realms’ – A bold hero cheats and fails to respect the ancestral Mother-spirit. The mother spirit holds the hero to his deal and devours him for his crimes. The tale is told non-verbally, through colorful illusion and intepretive dance.",
        "‘My Lord, Come-a-Leaping’ – A bawdy Halfling tale about a Randy Prince who is turned into Frog when he comes on too strong to a powerful and beautiful Halfling Sorceress, and discovers he likes being a Frog more than a Ruler.",
        "‘The Farmer’s Corn’ – A bawdy tale about a comely farmer’s daughter who mishears something someone said, and spreads gossip around the village.",
        "‘The Three Spinners’ – A children’s Tale retold through a tongue twisting call and response song. It is about three unmarried magical Farm-women who challenge that they can out-spin (thread) better than anyone. They challenge a devil, who curses one with a swollen foot, one with an infected finger, and one with an infected lip. The woman with the infected lip’s line is supposed to be sung while holding one’s tongue. In the end, the women win, the devil is defeated, and each one wins more gold than they know what to do with.",
        "‘The Town with No Name’ – ‘I came across a pokey town. Not much going on and curtains all down. I came across a smokey tavern. Not much going on in that pokey town.’ A slow sad song about a old woman that lost her way and found a town not on any maps they brought and only too late discovered it to be a ghost town. (Actual ghost town not just one that was abandoned).",
        "‘Beware A Human Bard’ – A pseudo-cautionary song about the lascivious characteristics of human bards; the song begins with an Elvish mother warning her daughter, and proceeds through all the more common races into more and more ridiculous warnings (‘Mama Golem warns that he’ll say he likes your rocks, but what he’s really thinking of…’)",
        "‘The Fall of the Sun’ – A mournful Aarakocra ballad, said to have been written by the first to travel from the Elemental Plane of Air and see a sunset.",
        "‘The Cheese Song’ – ‘Cheese Cheese Cheese Cheese Cheese Cheese Cheese Cheese Cheese Cheese’ A song used by Kenku bards who create melodies out of the different voices and accents they have heard the word in the songs they sing.",
        "‘Glida’s Wedding’ – A traditional halfling travel song, describing the setup for a halfling wedding, ‘held in the shadow of the wagons on a Summer Sunday.’",
        "‘The Flute & Lute’ – A ‘dueling instruments’ style song featuring the eponymous instruments. While some bards have added words to the lute portion, it is usually simply instrumental.",
        "‘Bear Bride’ – A song about a human maid, enchanted by a fair traveler into leaving her home, who meets a sad end when she discovers the traveler is a dangerous druid. Likely originating in legends warning of associating with strangers.",
        "‘Rocks Fall’ – A cautionary song about travelers who did not heed the warnings of the gods and met a sudden and tragic end in an avalanche.",
        "‘Green Fields, Grey Fields (The Old Woman and Young Girl)’ – A song about an old woman walking with her great-granddaughter. The song is both nostalgic and melancholy.",
        "‘The Solemn Judge’ – A song about an irascible old magistrate, his beautiful daughter, and the blacksmith’s son who falls for her. The last verse tells of the judge marrying the happy couple.",
        "‘Fleshy Pinklings’ – An Orcish Festival song, championing the power of the Orcish races and declaring their superiority over the rest of the world, and their destiny as conquerors.",
        "‘Cloth in the Street’ – A protest song, originally written in Malthcumband, calling for weavers to rise up against an unjust leader. Banned in many evil-aligned areas, the song calls for the people to rise up and take back the city. Ironically, one of the governments to ban the song is the tyrannical Communal Autocracy of Malthcumband, formed by many of the same weavers the song was first written for.",
        "‘The Colors Of Death’ – A colorful tale of how an adventuring party was brutally murdered by all the chromatic dragons at once.",
        "‘Well Well Well’ – A song relating how several people did mischief and subsequently fell into a hole in the ground. The chorus starts with: ‘Well Well Well, look who fell here!’.",
        "‘To The Death’ – A marching song about a young soldier who plans on dying bravely to defend their homeland, and asks their leader to write a letter home for them to their one true love. It was quite popular long ago, but is now considered cloying and outdated.",
        "‘Ale for the Victorious’ – A popular drinking song sung by soldiers while off-duty.",
        "‘To My Lover’s Lover’s Love’ – A downer of a song, this tear-jerker is a letter dictated, postmortem, by a forlorn lover telling all the sordid and dirty deeds of their former lover, now in the arms of another.",
        "‘Sir Dalloway the Duelist’ – A song from a hundred years ago, poking fun at nobles and fragile honor. It was once considered unlawful to sing it in polite company, but it is now a popular folk ballad that is quite catchy.",
        "‘Rhetting the Flax’ – A work song about how many bales of flax a young and ambitious villager promises to grow, harvest, prepare, spin, weave, and sell, so they can have enough fabric and gold for a huge wedding, if only their lover would return their affection. The song is a thinly veiled sexual innuendo.",
        "‘The Horrible Haggis of Hampstead Heath’ – A rhyming cumulative song about a mimic that swallows an farmer’s old, rotten haggis, gains magical powers, and then goes on a rampage. It devours an entire town, where every occupant, their occupation, their children, and the name of their family pets are listed. At first no-one stops it because they are too self-centered. In the end, the town’s guards and even the mayor are devoured. The song has a happy ending as the unlikely hero lets themselves get devoured and then slices open the mimic from the inside, releasing everybody safe and sound. The best bards are able to keep the crowd going for an entire hour, and then recite in reverse order the entire population of the village.",
        "‘Ogre-Melon Crawl’ – A catchy ditty which is a comedic precautionary tale about walking and not riding a horse if you have been drinking Ogre-Melon wine.",
        "‘Two Hundred and Seventeen Heartbeats’ – a controversial Elven composition. The singer takes a breath, then measures their pulse in silence for the duration that the title implies, while the audience is meant to slowly embrace the many natural sounds taking place during that time as a song of their own. It has been hailed by some musicians as a deep, thoughtful reflection on natural sounds, but criticized by others as a bad joke.",
        "‘Dwavers Wumblerubs’ – A halfling nonsense song, meant to sound like, but not actually be, Dwarvish. Sung with mock solemnity.",
        "‘Slashworthy’ – A sea shanty about a cutlass that never went dull, until the captain of the ship used it to shave his back.",
        "‘The Old Dun Cow’ – The dedicated patrons of a tavern take refuge in the cellar while the building burns down around them, and take advantage of the taverner’s stores while waiting to be rescued.",
        "‘The Hollowed One’ – A tale about a man who gave his mind, will, and voice to be able to house a disgraced god to protect his people. Any who hear it are inclined to feel a deep lament for this person.",
        "‘The Snarl’ – A frightening song about gnoll attacks, with reference to the sounds they make beforehand. Sure to give a frisson to listeners.",
        "‘Duplicitous Dannalor’ – A song about a half-elf man who is having simultaneous affairs with an elven woman and a human woman.",
        "‘Dreaming of an Inn’ – A ballad of an adventurer in the wilderness, missing civilization and bemoaning the uncouth surroundings and travelling companions.",
        "‘Gandavous Thunke’ – Oh, Gandavous Thunke was a dangerous drunk with chaos instilled in his soul, And when faced with sellswords, or rampaging Orc Hordes, Or an angry cantankerous Troll, Old Gandy would growl and fix them with a scowl and unleash the magic inside, Calling forth lightning, or- equally frightening- A fireball, leaving them fried. Now, though it seems tragic, the use of the magic has had an effect on his hue; So if you’re foolhardy and meet him at a party, you can call him Old Gandy the Blue.",
        "‘This Moment of Magic’ – A love song about a wizard’s apprentice falling for his classmate as they cooperate in the creation of a summoning circle. ‘Though I open a gate to the Plane of Air, and float through unending skies, I would never find night that was dark as your hair, nor a view as blue as your eyes.’",
        "‘Robin Redbreast’ – A song about a bird hopping through the forest. Although unknown by many, including some of its singers, there is a second message contained in thieves’ cant within the song, describing the guard patterns of the Royal Summer Palace of Keann.",
        "‘The Future Journey’ – A Dwarven song about the afterlife ‘dug down below.’",
        "‘Tenting on the Old Campground’ – a ballad of a soldier honoring and remembering those they’ve lost and wishing for an end of the war they are fighting.",
        "‘My Hedgehog Son’ – A catchy, nonsense, drinking song about a magical, talking hedgehog that gets adopted by a childless farmer, the hedgehog rides a rooster like a knight on a horse, and makes the farmer rich. The song is filled with tongue twisters. Bards occasionally challenge each other to invent and repeat new verses, each more difficult and hilarious than the last, while taking a drink after every flubbed line.",
        "‘The Silken Meadow’ – Who knew ancient Eladrin epic poetry turned thousand year old ballad could be so raunchy?",
        "‘Llolth’s Lullaby’ – An adventuring bard somewhere made it all the way down to the underdark, and heard one or two of the teaching songs sung by the Creche Matrons who give young Drow infants the education they need to survive the rigors of life; the song is in a deep dialect of undercommon that is almost never spoken anymore, but it is filled with all sorts of ‘Learning Magic’, mnemonics, and cultural references that makes it a sort of memetic hazard (you NEVER forget the words if sung by a powerful enough teacher), but the effect is less so when you don’t understand the language. That adventurous bard made it back to the surface, but not understanding the dialect of the deep, transposed the lullaby into a few other chords and added an improvisational lick of their own. That was a thousand years ago, and people have been humming and playing the tune up here ever since then, 50 generations later.",
        "‘Health Potion #9’ – A song about a long-suffering herbalist companion to a luckless knight and the scrapes the two of them get into. In the end, they end happily- the knight marries a guard captain who arrests him, while the herbalist falls for a local fortune teller.",
        "‘Ghouls in the Graveyard’ – A song about running through a graveyard seeking to avoid the attack of undead.",
        "‘A Red Ribbon’ – A murder-ballad. A lover is given a red ribbon, the lover cheats while wearing the ribbon. The lover is strangled with said ribbon. The song is sung from the perspective of the lover wearing the red ribbon and ends abruptly, mid verse.",
        "‘She’s Won the Crusade’ – A song about the exploits of a halfling bard, celebrating her exploits in the Great Crusade of Nevis with increasingly impossible descriptions of her victories.",
        "‘Last breath’ – A song about the recent death of a loved one, party member, and loss, the song goes through the 5 stages of grief as well.",
        "‘Hurry Up and Die’ – A song about a necromancer seeking a zombie companion, but surrounded only by living creatures.",
        "‘Run Through The Jungle’ – A saga of adventurers who managed to successfully get through the Haunted Temple of Khymann’roe and obtain the Crystal of Nor’Vesh without ever entering combat- simply by running away.",
        "‘No Rest For The Wicked’ – This song tells the tale of Caela of the Mammoth, a paladin of vengeance from a barbarian tribe, on her quest to hunt down the travelers who robbed and killed her father.",
        "‘The Stew’ – a Farcical portrayal of an foolish adventurer getting news that their loved one has decided that they are probably dead and has moved on. The distraught adventurer falls in love with the attractive savage, promising they’d ‘Jump in the Stew for You’. It has become a popular saying amongst foolish young lovers.",
        "‘There Is No Mountain’ – A chant developed in the monastery of Gar-Yin. The chant is used to focus the speaker away from the material realm, and declares the non-existence of the mountain, valley, and river visible from the monastery’s meditation area.",
        "‘The Scornful Beauty’ – A human traveler falls for a Dwarven gemsmith’s daughter, but she rebuffs his advances. The song calls on her to turn her head and consider his suit.",
        "‘Dihen-Nin (Forgive Me)’ – A mournful plea by an Elven soldier to his fallen comrades, begging their forgiveness for his survival ‘when your songs have been ended.’",
        "‘Captain Hennion’s Wife’ – A decidedly ribald army song about the wife of a commanding officer; it is common to adapt a verse to be about the wife (or daughter) of a current army leader. Singing this song can be a good way to end up in the stocks; nevertheless, it is very popular in camp.",
        "‘And Another Tree Falls’ – A mournful tale of a dryad, trying unsuccessfully to protect her grove from the incursion of a growing human city. This song is abnormally famous for starting bar fights, especially if there are urban and wild elements in the tavern.",
        "‘Clotted Soil’ – A recounting of the betrayal of King Bhoulthekk Bramfisted and his army by the Elven nation of Alv’dirae when the Dwarven army stood to defend Alv’dirae’s borders from attacks by the Ghowldresh Empire. One of the often-quoted verses from the saga includes the line ‘And may I trust a broken axe before an elf again.’",
        "‘The Old Fisherman’ – A shanty about a mysterious old Dwarven fisherman, encountered in the middle of the ocean on a little skiff. According to legend, if the fisherman is disturbed by a ship and not treated with respect, he kills every guilty soul on the ship with his gaff and leaves them hanging from the yardarms like a fish market.",
        "‘Simon McGurk’ – A shanty about a brilliant but lazy pirate. ‘Oh Simon McGurk, scared stiff of work, sailing all over the sea…’",
        "‘Greed’s Foul End’ – A movement from a morality play featuring a single musician and a vocalist. The piece is about the dangers of greed and the benefits of charity. Poignant, but difficult to pull off; often a touchstone work for performers of an ecclesiastical bent.",
    ];

    function findFaveSong() {
        var songIndex = Math.floor(Math.random() * bardSongs.length);
        var faveSong = bardSongs[songIndex];
        return faveSong;
    }

    function printSong() {
        console.log("----Favorite Song----:\n " + findFaveSong() + "\n");
    }
    printSong();
}