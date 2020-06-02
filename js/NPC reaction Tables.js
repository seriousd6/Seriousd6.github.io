function rollDice(number) {
    result = (Math.floor(Math.random() * number))
    return result;
};

function shiftCheck(word) {
    let chance = rollDice(100)
    switch (word) {
        case word = 'pleased':
            if (chance < 40) {
                return "This NPC will shift to Happy on the next encounter"
            } else {
                return "This NPC will stay Pleased for the next encounter"
            }
            break;
        case word = 'happy':
            if (chance < 20) {
                return "This NPC will shift to Friendly on the next encounter"
            } else {
                return "This NPC will stay Happy for the next encounter"
            }
            break;
        case word = 'disgruntled':
            if (chance < 40) {
                return "This NPC will shift to Unhappy on the next encounter"
            } else {
                return "This NPC will stay Disgruntled for the next encounter"
            }
            break;
        case word = 'unhappy':
            if (chance < 20) {
                return "This NPC will shift to Hostile on the next encounter"
            } else {
                return "This NPC will stay Unhappy for the next encounter"
            }
            break;
        default:
            return "please enter the correct word"
    }
}

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

//Before Everything - non-dependant 
let rumorType = [
    "False (Appears as Specific or Exact)", "Vague", "Mixed", "General", "Specific", "Exact",
]
let IVendetta = [
    "they were wrongfully jailed or persecuted", "of a racial crusade", "they want revenge for theft or deception", "they want revenge for personal death(s)", "they are on a religious crusade (local or part of a Faithquest)", "of political persecution", "their social status was destroyed and/or they were socially exiled",
]
let KBuyingOrSelling = [
    "Cloth - (Raw or Finished)", "Wood - (Raw, Finished, Furniture, Containers, Paper)", "Food - (Random types (air, sea, land) from random culture)", "Beverages -(Brewed (Ales), Distilled (Spirits), Raw (Juice), Dried (Teas) or Water)", "Spice - (Salt, Random spice, Random herb, Il(legal) drugs, or Medicine)", "Minerals - (Raw or Refined or Gems)", "Luxury - (Art, Rare Commodity or Masterwork items/weapons/armor)",
]
let LHomeland = [
    `(Homeland: A place from your world)`,
]

let QMinorEnemy = [
    "a snubbed ex-friend", "a school bully", "a business rival", "a local thug", "a romantic rival", "a spiteful boss or teacher", "a family member",
]
let RMajorEnemy = [
    "a politician or political group", "a powerful rogue/thug/assassin", "a noble's family", "a religious cult, sect, group, or temple", "a powerful mage or cabal", "a mercenary group", "a mysterious NPC",
]
let SHaunted = [
    "spirits locked in battle", "a tortured revenant who must relive its brutal murder", "a benign phantom who provides small comforts and messages", "a crazed banshee", "a spiteful haunt, who appears as dead loved ones and friends", "a playful poltergeist, a childish trickster", "an evil ghost, driven to consume lifeforce in a bid to regain life",
]
let TCursed = [
    "where time moves at a different speed", "where sleep and rest is impossible", "where the weather is extremely hot or cold", "where they experience an overwhelming aura of helplessness and suffering", "where there are plagues of vermin", "where there is constant foul weather", "where a corruption of reality occurs",
]
let VEmergency = [
    "political power is dead or arrested/exiled", "business in trouble", "family friend ill or mad or dead", "hometown has been attacked or enslaved or destroyed", "disease epidemic ", "close relative or spouse has done something terrible", "all resources or income has been stolen or destroyed",
]
let WWarning = [
    "a powerful enemy coming for you", "an enemy plotting against you", "how the government is investigating you", "a friend or lover or spouse lying to you", "a co-worker or business partner is stealing from you", "a rival spreading terrible lies and rumors", "an avatar coming",
]
let XSocialEvents = [
    "An invitation to an upcoming event (party, play, etc..) given by a mysterious stranger. ", "A local revival of (insert deity) followers is nearby, and drawing crowds", "A challenge has been issued by the (local ruler), calling for Feats of (insert ability)", "The (guild-house) is permitting new members to join, decided by a contest", "A circus has come to town. Rumors are they are taking on workers", "A fancy dress party for the (local ruler) has drawn all the wealthy in the area", "The marriage/birth/death/divorce/something else of (local ruler) or (ruler's family/spouse)",
]
let YPoliticalEvents = [
    "opposition gaining control through a coup", "downshift in the support of financial backers has driven prices way up", "noble accused of a terrible crime", "marriage between noble houses has been announced, while rumors of treachery persist", "shift in the government's stance on taxes has been taken badly by the populace", "rumor of corruption, and evidence of murder and treachery is begin sought", "powerful figure that has been killed, exiled, or worse",
]
let ZReligiousEvents = [
    "an avatar issuing sanctions", "open warfare against temple enemies is now public knowledge", "a new edict/sanction being announced and the resultant radical shift in the local population's mood", "an expedition to the Heathen Lands has been announced", "temple leaders declaring a peace agreement and a Summit of Faith is announced.", "an artifact or holy relic has been found/destroyed and a Call to the Faithful has gone out", "an avatar appears and denounces the faithless/blesses the faithful and punishes/rewards with a bane/boon",
]
let AAFaithTouched = [
    "dreams of the lives of those who gave their lives in sacrifice for the Faith", "all skills relating to the practice of the faith are more easily accomplished. +1", "hallucinations of the landscape of the deity's Plane haunt the waking mind", "those not of the Faith will be psionically attacked by the environment, driving them out", "animal servants of the deity roam the grounds here, protecting from heathen intruders", "all divine spells are cast here as if the caster was 1 level higher.", "manifestation of an Avatar. Its mood depends on the PCs interaction",
]
let BBWeaveTouched = [
    "a living mask of a Jester can be found here, hidden, but waiting. The parasite sleeps.", "all skills relating to the practice of the arcane mysteries are more easily accomplished. +1", "time and space are on vacation here. Non-causality is a possibility. Dimensionally weird.", "all arcane objects are recharged here, but can only be used once per item per location", "astral and ethereal creatures are feeding from this bountiful font. They are hostile", "all arcane spells are cast here as if the caster were 1 level higher", "wild magic regularly spawns here, bathing the area with random level spells and duration",
]
let CCMysteryCult = [
        "that is trying to return/exile/free/enslave/destroy/rebirth a minor/major deity", "that is collecting objects to trade to a deity for power", "are thralls under a larger power, acquiring resources, knowledge, manpower for a larger plan", "of disaffected people angry at inequality. They have resorted to violence and rhetoric", "of animal worshipers, devoted to returning humanity to a more primal lifestyle", "of outsiders stealing/killing/trading/enslaving/helping the local populace", "of wealthy cannibals and defilers, seeking only pleasure for themselves",
    ]
    //C
function findArtifact() {
    let chance = rollDice(100)
    if (chance < 95) {
        return "an artifact"
    } else {
        return "a piece of a legendary set of artifacts"
    }
}

function findMisc() {
    let misc = [
        "piece of jewelry", "chest", "map", "bucket", "lantern", "jar"
    ]
    return `a legendary ${ searchArray(misc) }`
}

function findArmor() {
    let chance = rollDice(100)
    if (chance < 90) {
        return "a single piece of legendary armor"
    } else {
        return "one part of a legendary set of armor"
    }
}

function findWeapon() {
    let chance = rollDice(100)
    if (chance < 70) {
        return "a common missle or melee weapon"
    } else if (chance < 95) {
        return "a uncommon missle or melee weapon"
    } else {
        return "a rare missle or melee weapon"
    }
}

function findArtPiece() {
    let artArray = [
        "rod", "staff", "wand", "sceptre", "crown", "gemstone"
    ]
    return `a ${ searchArray(artArray) } of high value or untold power`
}

function findCulturalArtifact() {
    let culturalArtifacts = [
        "a statue", "a painting", "an instrument", "some sheet music", "an article of clothing",
    ]
    return `${ searchArray(culturalArtifacts) }, which is a cultural artifact of great respect`
}

function findWeird() {
    let chance = rollDice(100)
    if (chance < 75) {
        return "a mysteriously preserved body part of great power"
    } else {
        return "a mysteriously preserved organ of great power"
    }
}
let CIteminformation = [
    `${ findArtifact() }`, `${ findMisc() }`, `${ findArmor() }`, `${ findWeapon() }`, `${ findArtPiece() }`, `${ findCulturalArtifact() }`, `${ findWeird() }`,
]

function informationSearch() {
    let chance = rollDice(100)
    if (chance < 33) {
        return "They are searching for information about " + searchArray(APersonalInformation)
    } else if (chance < 67) {
        return "They are searching for information about " + searchArray(BLocalInformation)
    } else {
        return "They are searching for information about " + searchArray(CIteminformation)
    }
}

function deedFinder() {
    let OGoodDeeds = [
        "freed an innocent from imprisonment", "corrected a long-standing error", "helped unfortunates with financial aid", "spread a charitable political message or religious doctrine", "helped local children or relatives to overcome oppression", "healed the sick and comfort the dying", `used ${searchArray(CIteminformation)} to spread goodwill`,
    ]
    let PEvilDeeds = [
        "humiliated and tortured a rival", "extorted someone", "stole from friends or family", "badly beat or kill a rival", "destroyed a business, financially or physically", "agitated society with a harmful political message or religious doctrine", "spread lies and rumors against an individual or group of a shocking nature",
    ]
    let chance = rollDice(100)
    if (chance < 50) {
        return searchArray(OGoodDeeds)
    } else {
        return searchArray(PEvilDeeds)
    }
}
//needs to be after C
let UTreasure = [
    "a set of potions", "a bag of gems", "some weapons or armor", "a stash of coins", "a few wands, rods, and staves", "a few pieces of clothing", `${searchArray(CIteminformation)}`,
]
let NMajorQuest = [
    "awaken a sleeping NPC", `recover or destroy an ${searchArray(CIteminformation)}`, "aid or slay an NPC", "slay a monster", "liberate or enslave an NPC", "discover a lost foreign land", "save or destroy the world",
]
let MMinorQuest = [
    "commune with an avatar", "map a location", "deliver a message", `recover a special ${searchArray(UTreasure)}`, "deliver a package", "destroy a minor monster/cleanse a tainted area", "rediscover a local forgotten place",
]
let HMajorBoon = [
        `divine intervention that grants ${searchArray(UTreasure)}`, `true Knowledge of the location of ${searchArray(UTreasure)} is obtained `, `a large amount of monetary wealth`, `(+1) for an existing skill or knowledge, or a new skill is obtained`, ` hot to improve a personal relationship to 100%`, `a major property being awarded or an improvement to a major property is granted`, `a specific rumor for ${searchArray(CIteminformation)}`,
    ]
    //after non dependent
function enemyChooser() {
    let chance = rollDice(100)
    if (chance < 50) {
        return searchArray(QMinorEnemy)
    } else {
        return searchArray(RMajorEnemy)
    }
}

function questFinder() {
    let chance = rollDice(100)
    if (chance < 50) {
        return searchArray(MMinorQuest)
    } else {
        return searchArray(NMajorQuest)
    }
}
let JOnTheRun = [
    'they committed political crime', 'they escaped from detention for a crime', 'they committed minor crime of theft, fraud or assualt', 'they committed major crime of theft, murder or rape (or this can be substituted with anarchy)', 'they committed religious crime', `they got tangled up with a myystery cult ${searchArray(CCMysteryCult)}`, 'unjustly accused',
]
let DFaction = [
    `a mystery cult ${ searchArray(CCMysteryCult) }`, `a group of slavers or brutal overlords`, `a group of religious warriors or clerics`, `a group of law and justice officers or warriors`, `a group of corrupt mercenaries or rogues`, `a merchant collective or guild`, `a cabal of mages`,
]

//after enemyChooser
function friendOrEnemy() {
    let chance = rollDice(100)
    if (chance < 50) {
        return "a friend"
    } else {
        return enemyChooser()
    }
}
let GMinorBoon = [
    `an enemy, ${enemyChooser()}, being temporarily thwarted`, `a minor magic item`, `a small amount of money or resources`, `a magicked gemstone (use 0-level or Cantrip effect, 1/day, as level 1 caster)`, `a minor property or an improvement to a minor property`, `a personal relationship established with potential ally or social status increases with ally`, `for one day, all activities to be easier. +1`,
]
let FMajorBane = [
    `bad luck (random penalties[disadvantage] to random die rolls) for 1 month or 10 combats`, `an outbreak of a large plague or pestilence`, `a large loss of monetary wealth`, `many items of value have being lost or destroyed`, `many buildings and/or the land being damaged`, `many people being killed`, `the PC or Party attracting the negative attention of ${enemyChooser()}`,
]
let EMinorBane = [
    'a disease or pestilence', 'buildings being destroyed', `the PC or Party enemy, ${enemyChooser()} to now actively oppose them`, 'the loss of items of value', `a curse, ${searchArray(TCursed)}, being activated`, 'people being injured', `the PC or Party being haunted by ${searchArray(SHaunted)}`,
]
let BLocalInformation = [
    `tells of something in the area that could cause ${searchArray(GMinorBoon)}.`, `tells of ${ searchArray(VEmergency) }`, `passes along knowledge of a ${ searchArray(XSocialEvents) }`, `gives information about a threat from an ememy, ${ enemyChooser() }`, `passes along information of a ${ searchArray(YPoliticalEvents) }`, `gives information about ${ searchArray(ZReligiousEvents) }`, `tells of ${ searchArray(FMajorBane) }`,
]
let APersonalInformation = [
    `a secret that leads to ${searchArray(HMajorBoon)}`, `a family emergency caused by ${searchArray(VEmergency)}`, `a ${searchArray(rumorType) } rumor about the PC as told by ${ friendOrEnemy() }`, `a suspicion held by the PC or the Party`, `a small warning regarding ${searchArray(WWarning)}`, `something the PC or Party has been investigating`, `- no, gives a severe warning about ${searchArray(WWarning)}`,
]

function faithOrWeave() {
    let chance = rollDice(100)
    if (chance < 50) {
        return "This place is Faithtouched - " + searchArray(AAFaithTouched)
    } else {
        return "This place is Weavetouched - " + searchArray(BBWeaveTouched)
    }
}

function hauntedOrCursed() {
    let chance = rollDice(100)
    if (chance < 50) {
        return "This place is haunted by " + searchArray(SHaunted) + "."
    } else {
        return "This place has a cursed reality " + searchArray(TCursed) + "."
    }
}


let monsterEncounter = [
    "a flock aarakocra", "an ankheg", "some bugbears", "a behir", "a sinkhole", "a traveling NPC", "a bulette", "a centaur", "a chimera", "a cockatrice", "a couatl", "a sealed entrance to the UnderDark", "an abandoned hunter's cabin", "a displacer Beast", "some dryad", "an earth elemental", "an ettin", "a faerie dragon", "weather phenomenon/disaster", "a caged monster (reroll) and dead handlers", "army patrol from (nearby military encampment suitable to your world.)", "a galeb duhr", "a gargoyle", "Hill Giants", "a gibbering mouther", "gnolls", "a large cavern system", "an abandoned cave", "a malignity of Goblins", "ghouls", "a hippogriff", "hobgoblins", "a hydra", "a deactivated colossus", "an evil cleric and minions performing ritual", "a jackalwere", "a manticore", "ogres", "orcs", "owlbears", "an unpowered standing circle of stones", "an old battlefield (reroll for monster skeletons)", "a rust monster", "some satyr", "stirges", "treants", "trolls", "a cycle gate", "an abandoned fort/tower/temple", "a wyvern",
]


let npcReactionToQuestioning = [
    `Hostile, now a nemesis. This interaction results in ${searchArray(FMajorBane)}. Also this NPC Will pursue PC until dead.`,
    `Unhappy, this interaction results in ${searchArray(EMinorBane)}. ${shiftCheck('unhappy')}`,
    `Disgruntled. The NPC gives false information. ${shiftCheck('disgruntled')}.`,
    `Tells you about ${searchArray(APersonalInformation)}, or ${searchArray(BLocalInformation)}, as requested `,
    `They are pleased. They share a ${searchArray(rumorType)} Rumour. ${shiftCheck('pleased')}`,
    `Happy. Rewards PC or Party with ${searchArray(GMinorBoon)}. ${shiftCheck('happy')}`,
    `Friendly, now an ally. Gives information about ${ searchArray(HMajorBoon) }. Will protect PC until dead.`,
]

function hostile() {
    document.getElementById("Reaction").innerHTML = npcReactionToQuestioning[0]
}

function unhappy() {
    document.getElementById("Reaction").innerHTML = npcReactionToQuestioning[1]
}

function disgruntled() {
    document.getElementById("Reaction").innerHTML = npcReactionToQuestioning[2]
}

function neutral() {
    document.getElementById("Reaction").innerHTML = npcReactionToQuestioning[3]
}

function pleased() {
    document.getElementById("Reaction").innerHTML = npcReactionToQuestioning[4]
}

function happy() {
    document.getElementById("Reaction").innerHTML = npcReactionToQuestioning[5]
}

function friendly() {
    document.getElementById("Reaction").innerHTML = npcReactionToQuestioning[6]
}

function reaClear() {
    document.getElementById("Reaction").innerHTML = ""
}

let npcMotivation = [
    `On the run because ${searchArray(JOnTheRun)}. They are being pursued by ${enemyChooser()} because they ${deedFinder()}.`,
    `A vendetta against ${enemyChooser()} because ${searchArray(IVendetta)}.`,
    `${informationSearch()}.`,
    `Buying/Selling ${searchArray(KBuyingOrSelling)} at nearby location, then returning home - ${searchArray(LHomeland)}.`,
    `On a local quest to ${searchArray(MMinorQuest)} for the reward of ${searchArray(UTreasure)}.`,
    `Looking to ${questFinder()} in the service of ${searchArray(QMinorEnemy)}.`,
    `Looking to ${searchArray(NMajorQuest)} in the hopes of earning ${searchArray(UTreasure)}.`,
]

function motivation() {
    document.getElementById("Motivation").innerHTML = searchArray(npcMotivation);
}


let areaStatus = [
    `${faithOrWeave()}.`,
    `Home to ${searchArray(DFaction)}. Their alignment is Evil/Neutral.`,
    `You'll find ${searchArray(monsterEncounter)} here, and nearby is ${searchArray(UTreasure)}.`,
    `Benign area of NPC population or is abandoned. No treasure.`,
    `Home to ${searchArray(DFaction)}. Their alignment is Good/Neutral.`,
    `You'll find ${searchArray(monsterEncounter)} here, and nearby is ${searchArray(CIteminformation)}.`,
    `${hauntedOrCursed()}`,
]

function area() {
    document.getElementById("Area Status").innerHTML = searchArray(areaStatus);
}

function reload() {
    location.reload()
}