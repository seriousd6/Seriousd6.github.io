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

function toWordsLc(s) {
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

function toWordsUc(s) {
    var th = ['', 'thousand', 'million', 'billion', 'trillion'];
    var dg = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine'];
    var tn = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen'];
    var tw = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety'];


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
    location.reload();
};

function printArray(array) {
    for (i = 0; i < array.length; i++) {
        console.log(array[i])
    }
}

function printFrom(array, number, id) {
    let list = shuffle(array).slice(0, number)
    list.forEach(function(item) {
        var li = document.createElement("li");
        var text = document.createTextNode(item);
        li.appendChild(text);
        document.getElementById(id).appendChild(li);
    });
};

function orderedPrint(array, number, id) {
    let list = array.slice(0, number)
    list.forEach(function(item) {
        var li = document.createElement("li");
        var text = document.createTextNode(item);
        li.appendChild(text);
        document.getElementById(id).appendChild(li);
    });
};

function loopCountStoreList(array) {
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
    return count(x);
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

function modify(number) {
    return Math.floor(number * (.85 + Math.random() * .4))
};

function shuffleSlice(array, number) {
    return shuffle(array).slice(0, number)

}

/*________________________________________________________________________________________*/

function plotBuilder(){
    /*Introduction*/
    let plot = 
    [
        [
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
        ],
        [
        "Quest (Act 1: forcing action 'what is the problem?', Act 2: building towards the goal, Act 3: revelation of the solution to the problem)",
        "Adventure (First movement: Abrupt leaving of home/ routine and the core purpose of the hero, Second movement: relevant choices being made along the journey, Third movement: fulfillment of the promises made during the first two movements)",
        "Pursuit (First movement: Identify of the two players, one chases and one is chased, and the why for the chase and the starting event, Second Movement: Chase -- twist, turns, reversals, Third movement: resolving the chase, either escape or capture)",
        "Rescue (Act 1: Separation - protagonist identified, antagonist identified, victim identified and the motivation for rescue is clear. Act 2: Pursuit and surprises. Act 3: Confrontation between protagonist and antagonist.)",
        "Escape (Act 1: Imprisonment. Act 2: planning, failed escape attempt, Act 3: the successful escape)",
        "Revenge (First movement: the crime, start the scene late and get out early, Second movement: the planning and building towards revenge, Third movement: confrontation)",
        "The Riddle/ Mystery (Two element structure (general/ metaphorical, specific/paradoxical, clues and references. Act 1: Exploring the general/ metaphrical aspects, Act 2: Exploring the particulars, Act 3: Solving the riddle",
        "Rivalry (Protagonist vs antagonist on roughly equal footing in a tug of war, an immovable object meets an irresistable force struggling for power over the other)",
        "Underdog (Unmached strengths between protagoinst and antagonist. Act 1: Antagonists have the upperhand, protagonist is disempowered. Act 2: protagonist empowered and ready to stand toe to toe with the antagonist but fails in establishing their hold. Act 3: The rising power of the antagonist and the final victory)",
        "Temptation (First movement: temptation established and the protagonist succumbs to it, Second movement: undergoing effects based on the decision, denial and finding a way out of punishments to follow. Third movement: rise and resolution of the internal conflicts, the crisis has been forced.)",
        "Metamorphasis (Act 1: the curse is introduced and the antagonist has felt the affects of it. Act 2: the relationship between the metamorph and the antagonist. Act 3: terms of release from the curse and resolution)",
        "Transformation (Act 1: An incident that changes the protagonist's life, Act 2: The full transfomative effects are seen, Act 3: the incident that defines the results of the transformation)",
        "Maturation (Coming of age, Act 1: 'before' and a catalytic event Act 2: rejecting the demands of the event, Act 3: developing newfound maturity and the verificaiton of this new maturity.)",
        "Love (Act 1: Lovers found, Act 2: Lovers split, Act 3: Lovers Reunited)",
        "Sacrifice (Act 1: Identifying ideals, Act 2: moral dillema with no easy solution forcing a hard choice, Act 3: making the choice and the cost of the sacrifice)",
        "Discovery (Act 1: the catalyst to a journey, start the scene late and get out early, Act 2: meaningful internal crisis, Act 3: resolution of the crisis)",
        "Wretched Excess (Act 1: life as normal, a catalyst Act 2: loss of control towards some obsession, Act 3: crisis point and the result )",
        "Ascension and Descension (Positive or a negative reactions under stress. Act 1: identifying the main character and the circumstances they start in, Act 2: moral stresses and the decisions that are propelling the character into their new self, Act 3: culmination of character and events)",
        ]
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

    let chance = rollDice(100)
    if (chance < 50){
        let randNum = Math.floor(Math.random()*plot.length)
        let linkedDev = ""
        if (devs[randNum].length > 2){
            linkedDev = searchArray(devs[randNum]) 
        } else if (devs[randNum]) {
            linkedDev = searchArray(devs[34]) 
        } else {
            let combArray = devs[randNum].concat(devs[34])
            linkedDev = searchArray(combArray) 
        }
        console.log(plot[0][randNum])
        console.log(linkedDev)
    } else {
        console.log(searchArray(plot[1]))
        console.log(searchArray(devs[34]))
    }  
}
plotBuilder()
