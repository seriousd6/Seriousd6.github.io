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



function plotBuilder(){
    /*Introduction*/
       let plot = [
       'The PCs are seeking shelter from the elements or some other threat, and come across a place to hole up. They find that they have stumbled across something dangerous, secret, or supernatural, and must then deal with it in order to enjoy a little rest.',
       'Some bad guys have arrived and done some bad guy things. The PCs were none the wiser. The bad guys have now made good their escape, and the PCs have caught wind of it in time to chase them down before they make it back to their lair, their home nation, behind enemy lines, etc.',
       "Usually through trickery (but sometimes by digging into the PCs' past), an antagonist has something to hold over the heads of the PCs and make them jump. This could be any kind of threat from physical to social, but it depends on the villain having something - even if it's information - that others don't have. Now, he is pulling the strings of the PCs, telling them to do things they don't want to. The PCs must end the cycle of blackmail, deprive the villain of his edge, and keep him temporarily satisfied while doing it.",
       `Mission objective: enter the dangerous place, and retrieve the vital dingus or valuable person. Overcome the area's defenses to do so.`,
       'The PCs must secure a target for the good guys. There are bad guys there that prefer not to be secured. The fundamental tactical scenario.',
       'There is a place where bad things live. The PCs must make it safe for nice people, systematically clearing it of danger.',
       "The PCs are treasure-hunters, who have caught wind of a treasure-laden ruin. They go to explore it, and must deal with its supernatural denizens to win the treasure and get out alive.",
       'The PCs are stranded in a strange place and they must survive by finding food and shelter, and then worry about getting back home.',
       "A crime or atrocity has been committed, the PCs must solve it. They must interview witnesses (and prevent them from being killed), gather clues (and prevent them from being stolen or ruined). They must then assemble proof to deliver to the authorities, or serve as personal ministers of justice.",
       'The PCs have a valuable object or person, which needs to be taken to a safe place or to its rightful owner, etc. They must undertake a dangerous journey in which one or more factions (and chance and misfortune) try to deprive them of the thing in their care.',
       'The PCs are placed in charge of a large operation (a trading company, a feudal barony, the CIA). Despite a lack of experience in such things, they must make it work and thrive.',
       "A person (church group, nation, galaxy) is in a hazardous situation they can't survive without rescue.The PCs are on the job. In some scenarios, the hook is as simple as a distant yell or crackly distress signal.",
       "The PCs, while traveling or exploring, come across a hornet's nest of bad guys, preparing for Big Badness. They must either find some way to get word to the good guys, or sneak in and disable the place themselves, or a combination of both.",
       "Within a defined area, something important and valuable exists. The PCs (or their employers) want it, but so do one or more other groups. The ones that get it will be the ones that can outthink and outrace the others, deal best with the natives of the area, and learn the most about their target. Each competing group has its own agenda and resources.",
       "The PCs are minding their own business when they are attacked or threatened. They don't know why. They must solve the mystery of their attacker's motives, and in the meantime fend off more attacks. They must put two and two together to deal with the problem.",
       "The PCs are a diplomatic vanguard, trying to open up (or shore up) either political or trade relations with a strange culture. All they have to do is manage for a day or so among the strange customs without offending anybody . . . and what information they have is both incomplete and dangerously misleading.",
       "The PCs are working surveillance - spying on a person, gathering information on a beast in the wild, scouting a new sector. Regardless of the scale, the primary conflict (at least at the start) is the rule that they are only to watch, listen and learn. They are not to make contact or let themselves be known.",
       "Someone is gone: they've run away, gotten lost, or simply haven't called home in a while. Somebody misses them or needs them returned. The PCs are called in to find them and bring them back.",
       "One or more of the PCs wakes up with no memory of the recent past, and now they find themselves in some kind of trouble they don't understand. The PCs must find the reason for the memory lapse, and solve any problems they uncover in the meantime.",
       "Something both bad and inexplicable is happening (racial tension is being fired up in town, all the power is out, the beer supply is drained, it's snowing in July, Voyager still has fans, hordes of aliens are eating all the cheese), and a lot of people are very troubled by it. The PCs must track the phenomenon to its source, and stop it.",
       "The PCs are assigned to guard a single vital spot (anything from a mountain pass to a solar system) from impending or possible attack. They must plan their defensive strategy, set up watches, set traps, and so on, and then deal with the enemy when it arrives.",
       "The PCs are minding their own business and find themselves transported to a strange place. They must figure out where they are, why they are there and how to escape.",
       "A villain or organization is getting ready to do something bad, and the PCs have received a tip-off of some sort. They must investigate to find out more about the caper, and then act to prevent it.",
       "Somebody has tinkered with Things Man Ought Not, or opened a portal to the Mean People Dimension, cracked a wall at the state prison, or summoned an ancient Babylonian god into a penthouse. Before the PCs can even think of confronting the source of the trouble, they must deal with the waves of trouble already released by it: monsters, old foes out for vengeance, curious aliens who think cars/citizens/McDonald's hamburgers resemble food, and so forth.",
       "Somebody needs a dingus (to fulfill a prophecy, heal the monarch, prevent a war, cure a disease, or what have you). The PCs must find a dingus. Often an old dingus, a mysterious dingus, and a powerful dingus. The PCs must learn more about it to track it down, and then deal with taking it from wherever it is.",
       "A town, castle, starship, outpost, or other civilized construct is lying in ruins. Very recently, it was just dandy. The PCs must enter the ruins, explore them, and find out what happened.",
       `The PCs must travel through a hazardous area, and get through without being killed, robbed, humiliated, debased, diseased, or educated by whatever is there. The troubles they encounter are rarely personal in nature - the place itself is the "villain" of the adventure.`,
       "The PCs are on a hunting expedition, to capture or kill an elusive and prized creature. They must deal with its environment, its own ability to evade them, and possibly its ability to fight them.",
       'The PCs are participants in a race, contest, tournament, scavenger hunt or other voluntary bit of sport. They must win.',
       'The PCs are imprisoned, and must engineer an escape, overcoming any guards, automatic measures, and geographic isolation their prison imposes on them.',
       'The PCs are on board a populated conveyance (East Indiaman, Cruise Ship, Ferry, Sleeper Starship), when it is hijacked. The PCs must take action while the normals sit and twiddle.',
       "A bad guy (or a group of them, or multiple parties) is kicking up a ruckus, upsetting the neighbors, poisoning the reservoirs, or otherwise causing trouble. The PCs have to go where the trouble is, locate the bad guys, and stop the party.",
       "The PCs are explorers, and their goal is to enter an unknown territory and scope it out. Naturally, the job isn't just going to be surveying and drawing sketches of local fauna, something is there, something fascinating and threatening.",
       `Any of the basic plots in this list can be re-engineered with the PCs on the outside of it. Either the PCs are accompanying other characters in the midst of such a plot (often being called on to defend the plot from the outside, as it were), or they are minding their own business when the others involved in the plot show up, and must pick sides or simply resist. For instance, with Any Old Port In The Storm, the PCs could already be enjoying (or native to) the shelter when a strange group arrives. If the "the PCs are unwelcome" variant is employed, then perhaps the PCs will be the only voice of reason to still the religious fervor, racial prejudice, anti-monster sentiment, or whatever else is the source of conflict. The PCs find themselves on the receiving end of the adventure. Take any of the plots here and reverse them, placing the PCs in the position where NPCs (often the villain, fugitive, et cetera) normally are`,
       ]
   /*Development*/
       let devs= [
       ['The shelter contains the cause of the threat the PCs were trying to avoid.', `The shelter houses a ${'Hidden Base'}.`, 'The PCs must not only struggle for shelter, they must struggle to survive.', 'The place is a legitimate shelter of some kind, but the PCs are not welcome, and must win hearts or minds to earn their bed for the night.'],
       [ 'The bad guys escaped by stealing a conveyance that the PCs know better than they do.', 'The bad guys duck down a metaphorical (or literal) side-road, trying to hide or blend into an environment (often one hostile to the PCs).', `If the bad guys cross the adventure's "finish line" (cross the county line, make the warp jump, etc.) there's no way to pursue them beyond it.`, ],
       [ 'The adventure hook involves the PCs doing the villain a good turn, which allows him to take advantage of them (very cynical!).', 'To succeed, the PCs must contact other folks that are also being used.', "The PCs aren't the victims at all, but somebody they care about/are charged to protect, is.", ],
       [ 'The goal is not to extract a thing, but to destroy a thing or interfere with a process (kill the force-screen generator, assassinate the evil king, stop the spell from being cast, wreck the invasion plans, close the portal).', 'The goal has moved.', 'The goal is information, which must be broadcast or otherwise released from the area as soon as it is found.', 'The job must be done without alerting anyone.', "The PCs don't know the place is dangerous.", 'The PCs must replace the thing with another thing.', ],
       [ "The PCs must assemble and/or train a force to do the job with them.", "The PCs are working with flawed intelligence and the target zone isn't as described.", "The PCs must coordinate their own efforts with an ally group (possibly putting aside rivalries to do so).", "The target zone includes a population of innocent people, fragile goods, or some other precious thing that mustn't be harmed in the crossfire.", ],
       [ "The bad things can't be beaten with direct conflict.", 'The PCs must learn more about the inhabitants to solve the problem.', "The Haunted House; The Alien Infestation; The Wild Forest.", ],
       [ "The treasure itself is something dangerous.", `The treasure isn't in a ruin, but in a wilderness or even hidden somewhere "civilized."`, "The treasure is someone else's rightful property.", "The treasure turns out to have a will of its own.", ],
       [ "The PCs must survive only for a short period of time, until help arrives, the ship and/or radio is repaired, or some such thing", `in "repair" scenarios, sometimes the PCs must discover some fact about the local environment that will make such repairs possible.` ],
       [ "The PCs are working to clear an innocent already accused (possibly themselves).", "The PCs must work alongside a special investigator or are otherwise saddled with an unwanted ally.", 'Midway through the adventure, the PCs are "taken off the case" - their invitation/authority to pursue the matter is closed (often the result of political maneuvering by an antagonist).', 'The climax is a courtroom scene or other arena of judgment.', "The scale is highly variable for this type of adventure, from a small-town murder to a planetwide pollution scandal.", ],
       [ 'The thing or person is troublesome, and tries to escape or sidetrack the PCs.', "The destination has been destroyed or suborned by the enemy, and the PCs must take upon themselves the job that either the destination or their charge was meant to do when it got there.", 'The person is attempting a political defection.', "Safe arrival at the destination doesn't end the story; the PCs must then bargain with their charge as their token (exchanging money for a hostage, for instance).", 'The PCs must protect the target without the target knowing about it.', ],
       [ 'The PCs are brought in because something big is about to happen, and the Old Guard wants a chance to escape.', 'The peasants, neighbors, employees, et cetera resent the PCs, because their method of inheritance looks outwardly bad and everybody loved the old boss. ', ],
       [ 'The victim(s) is (are) a hostage, or under siege from enemy forces, and the PCs must deal with the captors or break the siege.', 'There is a danger that any rescue attempts will strand the rescuers in the same soup as the rescuees, compounding the problem.', "The rescuees aren't people, but animals, robots, or something else.", `The "victim" doesn't realize that he needs rescuing; he thinks he's doing something reasonable and/or safe.`, "The threat isn't villain-oriented at all; it's a natural disaster, nuclear meltdown, or disease outbreak.", "The rescuees can't leave ; something immobile and vital must be tended to or dealt with at the adventure location.", 'The PCs begin as part of the rescuees, and must escape and gather forces or resources to bring back and proceed as above.', ],
       ['The PCs must figure out how to use local resources in order to defend themselves or have a chance against the inhabitants.'],
       [ 'The natives require the competing factions to gather before them as pals to state their cases.', 'The valuable thing was en route somewhere when its conveyance or courier wrecked or vanished.' ],
       [ "The PCs have something that the bad guys want - but they don't necessarily realize it.", "The bad guys are out for revenge for a dead compatriot from a previous adventure.", "The bad guys have mistaken the PCs for somebody else.", ],
       ["The PCs were chosen by somebody who knew they weren't prepared for it - an NPC trying to sabotage the works (pinning this villain might be necessary to avert disaster)."],
       ["The target gets itself in trouble and the PCs must decide whether to break the no-contact rule in order to mount a rescue.","The target is about to commit a heinous crime; will the PCs interfere or obey orders?"],
       [ "The target has been kidnapped (possibly to specifically lure the PCs).", "The target is dangerous and escaped from a facility designed to protect the public.", "The target is valuable and escaped from a place designed to keep him safe, cozy, and conveniently handy.", "The target has a reason for leaving that the PCs will sympathize with.", "The target has stumbled across another adventure (either as protagonist or victim), which the PCs must then undertake themselves.", `The missing "person" is an entire expedition or pilgrimage of some kind.`, `The target isn't a runaway or missing/lost - they're just someone that the PCs have been hired to track down (possibly under false pretenses).`, ],
       [ `The forgetful PCs voluntarily suppressed or erased the memories, and they find themselves undoing their own work.`, `The entire party is temporarily amnesiac.`, `The PCs drank too much alcohol last night, and now have a massive hangover.`, ],
       [ `The PCs are somehow unwittingly responsible for the whole thing.`, `What seems to be a problem of one nature (technological, personal, biological, chemical, magical, political, etc) is actually a problem of an alternate one.`, ],
       [ `The intelligence the PCs was given turns out to be faulty, but acting on the new information could result in greater danger - but so could not acting on it, and the PCs must choose or create a compromise.`, `The PCs learn that the enemy has good and sympathetic reason for wanting to destroy the protected spot.`, ],
       [ `They were brought there specifically to help someone in trouble.`, `They were brought there by accident, as a by-product of something strange and secret. Some of the PCs' enemies were transported along with them (or separately), and now they have a new battleground, and innocents to convince which guys are the good guys.`, ],
       [ `The initial tip-off was a red herring meant to distract the PCs from the actual caper.`, `There are two simultaneous Bad Things on the way, and no apparent way to prevent both of them - how to choose?`, ],
       [ `The PCs can't simply take the released badness to the mat; they have to collect it and shove it back into the source before it the adventure can really end.`, `The PCs are drawn in to the source and must solve problems on the other side before returning to this one.`, `A secret book, code, or other rare element is necessary to plug the breach (maybe just the fellow who opened it).`, `A close cousin to this plot is the basic "somebody has traveled into the past and messed with our reality" story.`, ],
       [ `The dingus is incomplete when found (one of the most irritating and un-fun plot twists in the universe).`, `Somebody already owns it (or recently stole it, sometimes with legitimate claim or cause).`, `The dingus is information, or an idea, or a substance, not a specific dingus.`, `The PCs must "go undercover" or otherwise infiltrate a group or society, gaining the dingus by guile or stealth.`, ],
       [ `Whatever ruined the ruins (including mean people, weird radiation, monsters, a new race, ghosts) is still a threat; the PCs must save the day.`, `The inhabitants destroyed themselves.`, `The "ruins" are a derelict ship or spaceship, recently discovered.`, `The "ruin" is a ghost town, stumbled across as the PCs travel - but the map says the town is alive and well.`, `Alternatively, a town recently destroyed by some monster or cataclysm suddenly reappears completely unharmed, and the PCs must discover the mystery of its resurrection, possibly re-destroying it in the process.`, ],
       [ `The place isn't dangerous at all, and the various "dangers" are actually attempts to communicate with the party by some agent or another.`,],
       [ `The creature is immune to their devices and weapons.`, `There are other people actively protecting the creature.`, `The creature's lair allows the PCs to stumble onto another adventure.`, ],
       [ `The other contestants are less honest, and the PCs must overcome their attempts to win dishonestly.`, `The PCs are competing for a deeper purpose than victory, such as to keep another contestant safe, or spy on one, or just to get into the place where the event goes down.`, `The PCs don't wish to win; they just wish to prevent the villain from winning.`, `The event is a deliberate test of the PCs abilities (for entry into an organization, for example).`, `The event becomes more deadly than it's supposed to.`, ],
       [ `Something has happened in the outside world and the prison security has fallen lax because of it.`, `The PCs have been hired to "test" the prison - they aren't normal inmates.`, `Other prisoners decide to blow the whistle for spite or revenge.`, `The PCs are undercover to spy on a prisoner, but are then mistaken for real inmates and kept incarcerated.`, `The PCs must escape on a tight schedule to get to another adventure outside the walls.`, ],
       [ `The "hijackers" are government agents pulling a complicated caper, forcing the PCs to choose sides.`, `The hijackers don't realize there is a secondary danger that must be dealt with, and any attempt to convince them is viewed as a trick.`, `The normals are unhelpful or even hostile to the PCs because they think the PCs are just making matters worse.`, ],
       [ `The PCs must not harm the perpetrator(s); they must be bagged alive and well.`, `The bad guys have prepared something dangerous and hidden as "insurance" if they are captured.`, `The "bad guy" is a monster or dangerous animal (or an intelligent creature that everybody thinks is a monster or animal).`, `The "bad guy" is a respected public figure, superior officer, or someone else abusing their authority, and the PCs might meet hostility from normally-helpful quarters who don't accept that the bad guy is bad.`, `A balance of power perpetuates the trouble, and the PCs must choose sides to tip the balance and fix things.`, `The "trouble" is diplomatic or political, and the PCs must make peace, not war.`, ],
       [ `Either the place itself is threatening (in which case the PCs must both play National Geographic and simultaneously try to escape with their skin, sanity, and credit rating) or the place itself is very valuable and wonderful, and something else there is keen on making sure the PCs don't let anyone else know.`, `Other potential conflicts involve damage to the PCs' conveyance or communication equipment, in which case this becomes Don't Eat the Purple Ones. (see above)`, ],
       [ `Instead of hunting, they must be hunted.`, `Instead of fixing, they must avoid getting "fixed" themselves (ow).`, `Alternately, leave a classic plot intact but turn the twists upside down, making them twistier (or refreshingly un twisty).`, ],
       [ `The PCs must work alongside an NPC or organization they'd rather not pal around with (those who are normally rivals or villains, or just a snooty expert sent along to "help" them, etc).`, `The victims are really villains and the villains are really victims.`, `The PCs meet others who can help them, but won't unless the PCs agree to help them with their own causes.`, `The villain is somebody the PCs know personally, even respect or love (or someone they fall for, mid-story).`, `The PCs must succeed without violence, or with special discretion.`, `The PCs must succeed without access to powers, equipment, or other resources they're used to having.`, `The villain is a recurring foil.`, `Another group comparable to the PCs has already failed to succeed, and their bodies/equipment/etc provide clues to help the PCs do better.`, `There are innocents nearby that the PCs must keep safe while dealing with the adventure.`, `The adventure begins suddenly and without warning or buildup; the PCs are tossed into the fire of action in scene one.`, `The PCs must pretend to be someone else, or pretend to be themselves but with very different allegiances, values or tastes.`, `The PCs can't do everything and must choose: which evil to thwart? Which innocents to rescue? Which value or ideal to uphold?`, `The PCs must make a personal sacrifice or others will suffer.`, `The PCs aren't asked to solve the problem, just to render aid against a backdrop of larger trouble: get in a shipment of supplies, sneak out a patient that needs medical help, or so on.`, `One of the PCs is (or is presumed to be) a lost heir, fulfillment of a prophecy, a volcano god, or some other savior and/or patsy, which is why the PCs must do whatever the adventure is about.`, `There is another group of PC-like characters "competing" on the same adventure, possibly with very different goals for the outcome.`, ],
       ]
   
   /*Twist/ Divergence/ False appearance*//*Resolution*/
       let randNum = Math.floor(Math.random()*plot.length)
       let linkedDev = Math.floor(Math.random()*devs[randNum].length) 
       console.log(plot[randNum])
       console.log(devs[randNum][linkedDev])
   }
plotBuilder()



/*

"Silver ewer",
"Carved bone statuette",
"Small gold bracelet",
"Cloth-of-gold vestments",
"Black velvet mask stitched with silver thread",
"Copper chalice with silver filigree",
"Pair of engraved bone dice",
"Small mirror set in a painted wooden frame",
"Embroidered silk handkerchief",
"Gold locket with a painted portrait inside"
"Gold ring set with bloodstones",
"Carved ivory statuette",
"Large gold bracelet",
"Silver necklace with a gemstone pendant",
"Bronze crown",
"Silk robe with gold embroidery",
"Large well-made tapestry",
"Brass mug with jade inlay",
"Box of turquoise animal figurines",
"Gold bird cage with electrum filigree"
"Silver chalice set with moonstones",
"Silver-plated steel longsword with jet set in hilt",
"Carved harp of exotic wood with ivory inlay and zircon gems",
"Small gold idol",
"Gold dragon comb set with red garnets as eyes",
"Bottle stopper cork embossed with gold leaf and set with amethysts",
"Ceremonial electrum dagger with a black pearl in the pommel",
"Silver and gold brooch",
"Obsidian statuette with gold fittings and inlay",
"Painted gold war mask"
"Fine gold chain set with a fire opal",
"Old masterpiece painting",
"Embroidered silk and velvet mantle set with numerous moonstones",
"Platinum bracelet set with a sapphire",
"Embroidered glove set with jewel chips",
"Jeweled anklet",
"Gold music box",
"Gold circlet set with four aquamarines",
"Eye patch with a mock eye set in blue sapphire and moonstone",
"A necklace string of small pink pearls"
"Jeweled gold crown",
"Jeweled platinum ring",
"Small gold statuette set with rubies",
"Gold cup set with emeralds",
"Gold jewelry box with platinum filigree",
"Painted gold child's sarcophagus",
"Jade game board with solid gold playing pieces",
"Bejeweled ivory drinking horn with gold filigree"

`An adventuring party setting off from a village for their first adventure. Goblins can be seen peering out of some bushes.`,
`group of ${searchArray(['adventurers', `${searchArray(subject[1])}`])}` 
`${searchArray(['setting off from', 'heading towards', 'in the midst of'])} a ${searchArray(['campsite','village','city','battefield','cave','portal','wasteland'])}`,
`A handsome painting of a local lord or other noble, signed “To my dearest friend ______.”`,
`A cat with wings sitting on a hill licking its paws.`,
`A treent patting a blushing dryad on the head.`,
`A charismatic devil in a suit, sipping wine from a goblet while sitting on a fine chair that itself sits stop a massive pile of gold and jewels.`,
`A ruined city in the middle of a desert. A giant broken crystal hovers above the tallest tower.`,
`${searchArray(['ruined city', 'mountain', 'metropolis'])} ${searchArray(["in the middle of the"])}`,
`A nearly nude female dragonborn, draped in silks and eating grapes on a sofa.`,
`A jeweled sword stuck in a common stone.`,
`A beholder in a top hat whose eyes follow you. But each time you look, it's a different eye.`,
`A man with a flute and a naked female of every other race.`,
`A gnome standing proudly in front of some unidentifiable machine. Perhaps it flies?`,
`The danse macabre: several skeletons, some in rags and some bedecked in finery, dance together. It is a reminder that after death, all bodies, regardless of status, are the same to a necromancer.`,
`A troll intimidating a traveler on his bridge.`,
`A red-faced drunken giant.`,
`A still-life of potions and alchemical supplies.`,
`A solemn saint with a halo of actual enchanted flames.`,
`An archer posing with a dead peryton.`,
`A hero raising their magical spear to the sky in triumph.`,
`A haggard old crone with a crystal ball. The ball contains the painter's reflection, distorted and upside down.`,
`An artifact in a glowing crystal cage.`,
`The prophesied end of the world.`,
`You. The painting is enchanted to depict the viewer.`,
`A mirror depicting the room it is in, devoid of people. A small plaque on the frame titles it "Vampires"`,
`A formal-looking portrait of a headless woman, holding the decapitated head of a man.`,
`A figure sits writing at a desk, surrounded by stacks of books and parchment.`,
`A bunch of poorly-rendered stick figures and...is that a house? And it might be on fire? The only clear thing about this painting is that it was likely done by a child.`,
`Geometric forms that overlap and intertwine, into which you can sort of apply some level of anthropomorphization. That might be a set of eyes, and that might be a mouth, after all.`,
`A coronation scene, with a woman being crowned amidst a court of noble onlookers.`,
`A scientific-looking rendering of a local animal/plant, annotated with biological observations.`,
`An underwater shipwreck, surrounded by murky water and ethereal forms.`,
`An evening sky lit by the aurora.`,
`A bridge spanning a wide river, still in mid-construction.`,
`A formal-looking portrait of a pig and an anteater.`,
`Starry Night with a Nautiloid in the sky`,
`An painting from a remote country. It depicts a magnificent walled city, with a golem in the background that towers over it. The golem bears the symbol of a foreign deity on its chest, representing the god’s role as a guardian of the city.`,
`A golem of Hextor burning a village of elves. Drow army can be seen below helping the Golen -Circa 32 year of present day.`,
`A mated pair of displacer beasts trying to scare off an invading owlbear from their recent kill.`,
`A nature conservationist caring for and trying to nurse a winter wolf back to health.`,
`A day in the life of dwarf miners plying their craft.`,
`A wizard and apprentice(s) discussing magical lore or performing a magical case study.`,
`A portrait of adventuring friends before setting out for the first time.`,
`A portrait of adventuring friends as kids in their neighborhood or perhaps at a fair.`,
`A portrait of adventuring friends surrounded by many/some of their accumulated wealth and accomplishments before one or more of them moved away and/or were killed.`,
`A family portrait of some noble family.`,
`A family portrait of a wealthy merchant's family.`,
`large caravan (entering, leaving) a city.`,
`Ships docket at a large port city.`,
`A portrait of a busy market street with lots of people buying and selling goods.`,
`A brave knight battling a horrible monster. Both are being controlled by puppet strings.`,
`A portrait of an adventuring group that looks like a (younger, older) version of the PCs.`,
`A woman and a bear standing beside one another, they each have matching multi colored eyes.`,
`A pantion of L-G and L-N deities arguing in a court room.`,
`63.he deity of wisdom lecturing the hungover deity of festivities`,
`A ancient red dragon battling a ancient white dragon.`,
`A wizard being taunted by his lich-like reflection in a mirror.`,
`A nobleman singing a pact with a grinning succubus`,
`A druidic protection ritual performed in a beautiful forest by charming but animal-like people. They have e.g. antlers or wings.`,
`A religious picture about the fight between the good and the evil.`,
`A portrait of a long dead ancestor, with telltale signs of something demonic about them.`,
`A large ship battling a kraken in the middle of a raging storm.`,
`A group of skeletons in a dungeon, peeking around a corner that some unsuspecting adventurers are approaching, planning an ambush.`,
`An idealized painting of famous Wizards at a library discussing principles of magic (Think School of Athens)`,
`A historical gathering of clerics/cultists promoting their faith in a courtyard.`,
`A portrait of a long dead ancestor, with telltale signs of something demonic about them.`,
`large ship battling a kraken in the middle of a raging storm.`,
`Dead nature ( don't know the translation, those training paintings everyone does first to test styles.`,
`Graphite sketches of an ancient, now outdated, dwarven war machine.`,
`A collection of paintings of forest scenes with a red hooded girl and a werewolf:`,
`1st the girl is on the foreground, giving the perspective of natural movement. The creature is on the background, lurking, with vicious intent.`,
`2nd the girl forces through a narrow rock formation giving the impression she will be ambushed at any time.`,
`3rd represents a flung of the werewolf leaping towards the child`,
`4th a darker scene sets a circle of red hooded people facing the werewolf over a stone alter in the forest. It is faintly visible from some angles the form of three greenish tentacles surrounding the altar, and a gaping maw with nightmarish properties.`,
`Satyr peeps through trees and watches the dryads bathe joyesly.`,
`he market of meerkhat, a sensorial confounding painting of a desert based market, with vibrant colours, hundreds of depicted heads ( as in shoppers and sellers) all almost running over each other, and what looks like a parade on a higher road in the background. The looker of the painting makes a DC 13 Wisdom saving throw to resist an urge to go shopping ( either the gift shop at the museum or going to the closest market and going on a spree ).`,
`A group of gnomes or halflings tiptoeing around a sleeping dragon and their hoard`,
`A large army of dark knights being driven away by angels, their awesomely armored leader holding an evil looking great sword being struck in the chest by a spear of light.`,
`A portrait of a striking military leader's top half. Not shown is the bottom half, where the leader is wearing very silly underwear and women's shoes.`,
`A necromancer animating skeletons like puppets to play instruments. One of them is playing a trumpet.`,
`A grand feast being held in a cramped tavern room.`,
`A group of six werewolves playing poker.`,
`A sad dwarf with his ear cut off.`,
`A banshee screaming on a bridge.`,
`A group of gnomes or halflings tiptoeing around a sleeping dragon and their hoard`,
`A pack of gnolls battling a town militia`,
`The Ascension of a cleric into a saint or celestial`,
`A warlock being contacted and accepting a pact with their patron (whichever kind)`,
`A noble knight breaking a liches phylactery`,
`A large army of dark knights being driven away by angels, their awesomely armored leader holding an evil looking great sword being struck in the chest by a spear of light`,
`A trio of giant humanoids carving out mountains from the earth, as a god watches over them.`,
`A Yuan-Ti Pureblood crown found at the site of an unearthed ruin.`,
`Leather gloves, with 4 slots on the knuckles for jewels; to the side, one of the jewels, cracked and faded with color. Rumored to hold the power to cast any magic spell once if all four gems can be seated (one set per glove).`,
`Tools thought to be the earliest concepts for modern Dwarven forging. Among the menagerie is a small anvil, shaped like a Dwarven head, probably used for working with gold.`,
`A painting, on magical parchment, displays an epic magical encounter between former wizards of the realm. This painting's details of the spells are all magically flowing across the parchment, giving the painting the feel that the spells are being cast at the viewer!`,
`A single solitary rune stone found within the core of an ancient tree, recently felled due to some evil force. The rune written on the stone reads "growth".`,
`A green tinged chest-plate, which is a remnant of a ancient society of Dwarven druids.`,
`An ancient cave painting from the early days of the world which depicts a creature of colossal size. Archaeologists have theorized that this might be one of the first artistic depictions of the legendary Tarrasque.`,
`The perfectly preserved corpse of a mindflayer.`,
`The tooth of a Kraken.`,
`A silk dress spun by the spiders of the Feywild.`,
`A sculpture depicting a hypothetical gate to the Nine Hells. It’s been rumored that if the doors on it were opened it would capture and drag those unwary souls to meet eternal damnation. Such rumors are naturally considered unfounded in the greater scientific community but as a precaution the doors are chained shut.`,
`A full suit of armor once worn by a legendary hero.`,
`A collection of old Elven vases, if broken or shattered they unleash a wave of liquid; water, lava, gold, or acid.`,
`A bunch of carved rocks that float of their own violation. They in fact are just levitating via magnetism but the museum curator believes they are magical.`,
`A mummy, in all it's golden regalia on a throne. Must have a sleep spell cast on it or it rises and generally acts like an old forgetful man bothering people.`,
`The very large skull of an unknown creature. It has six eye sockets and dagger sized teeth.`,
`A large rock covered with runes. Otherwise ordinary but a group of cultists have gathered outside the museum chanting 'release our master' ever since the rock arrived.`,
`An obsidian Idol, which scholars believe depicts an ancient Lizardfolk god, whose name is now forgotten.`,
`The perfectly preserved Mask of a Merregon, retrieved from an abandoned Cult site.`,
`A rare example of Derro Art, A statue made of granite, seemingly twisted into curious shapes with magic. Its meaning is subject for speculation .`,
`The Book of Ur: A mysterious manuscript written in an unknown language nobody has been able to decipher in 50 years. Somehow, the book is immune to spells, such as Comprehend Languages. (Either the only source about an ancient secret society or just gibberish).`,
`A dagger carved out of a large opal. Believed to have been used in ceremonies by early tribes in Kara-Tur.`,
`A ceremonial bronze helmet from a Uthgard burial mound. The Uthgard are not happy about that.`,
`The remains of an early gnomish automaton.`,
`A cube made up off interlocking smaller cubelets. It was used as a mental exercise by an ancient group of monks and philosophers.`,
`The ruins of Modron that was severely damaged and shut down during The Great Modron March. If it where to deactivate, it would return to the preset path of that specific march.`,
`A handful of glowing dust-like material from an unknown plane, and is said to be highly poisonous and able to warp flesh. The dying man who brought the strange material spoke only of a place called "Trinity".`,
`An ancient Dwarven rune carving which depicts an ancient disaster. On loan from the clan which carved it until other depictions of the disaster are unearthed and used instead.`,
`A map of a magical moving island.`,
`A large painting of a badly disguised Kobold wizard riding a dragon and throwing lightning bolts.`,
`A small pouch of black sand, rumored to cause any cut the sand touches to infect and cause rot.`,
`An ever-full wine skin, known to never be consumed no matter how much you take from it.`,
`A very old map of an unknown land. You've never seen a map quite like it. It shows an island, or a continent, surrounded by water. But that's only the beginning. Everything is out of proportion: Dots indicate major cities, but these cities are larger than life, each the size of our own Kingdom! And this island is much smaller than our own land!`,
`A single gauntlet, similar to the combat gauntlets of a knight, but with an attachment that allows it to be affixed to the arm.`,
`A small pocketwatch with the power to slow down time for a brief moment, just long enough to get away with something.`,
`A blood-stained journal page, with a poem that speaks of an ancient terror rising.`,
`An onyx and diamond jeweled broach, known to give the user access to the memories of its previous owners for a few moments.`,
`A small ornate music box, covered in demonic faces. When wound it plays a dark and thudding tune that puts those who hear it in a state of hypnosis.`,
`A silver whistle, rumored to summon the beast that was used to make the whistle.`,
`A small wooden box containing several intricate puzzles, each one fitting into another like a puzzle within a puzzle.`,
`A glass bottle containing the glowing essence of lightning.`,
`A glossy obsidian stone, with an eyehole carved in it for looking into a different dimension.`,
`A small, ornate hourglass, holding back the sands of time.`,
`A pipe shaped like a demon's head, with a unique kind of bowl that cools hot tabacs into a pleasant fruit flavor.`,
`A very old and dusty tome, containing the story of a warrior from an age long forgotten.`,
`A golden ring with an embedded ruby that forms the image of a roaring dragon.`,
`A small ornate container of face paint, traditionally used for festivals where the user paints their face to look like the fearsome undead.`,
`A notebook with complex mathematical formulas covering every page.`,
`An album containing several family portraits spanning multiple generations.`
*/