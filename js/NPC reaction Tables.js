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

function searchArray(array) {
    let shuffled = shuffle(array)
    return shuffled[Math.floor(Math.random() * shuffled.length)];
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
};

// convert numbers to word form
function toWords(s) {
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
//Reload Page
function reload() {
    location.reload()
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



/*############################Page Scripts#########################################*/
function scene() {
    document.getElementById("Scene").innerHTML = ""

    function person(number) {
        let generic = ["man", "boy", "girl", "woman"]
        let any = [`${searchArray(["young","old"])} man`, `${searchArray(["young","baby"])} boy`, `${searchArray(["young","baby"])} girl`, `${searchArray(["young","old"])} woman`]
        let withagency = [`a${searchArray([" young","n old"])} man`, `a${searchArray([" young",""])} boy`, `a${searchArray([" young",""])} girl`, `a${searchArray([" young","n old"])} woman`]
        let plural = [`young ${searchArray(["men","men and women","men, women and children","women"])}`, `varying aged ${searchArray(["men","men and women","men, women and children","women"])}`, `old ${searchArray(["men","men and women","women"])}`, `boys and girls`, `boys`, `girls`]
        let audience = [`a ${searchArray(generic)}`, `a small group of ${searchArray(plural)}`, `a large group of ${searchArray(plural)}`]
        let professional = [`${searchArray([" young","n old"])} man`, `${searchArray([" young","n old"])} woman`]
        if (number === 0) {
            return searchArray(generic)
        } else if (number === 1) {
            return searchArray(any)
        } else if (number === 2) {
            return searchArray(withagency)
        } else if (number === 3) {
            return searchArray(audience)
        } else if (number === 4) {
            return searchArray(plural)
        } else if (number === 5) {
            return searchArray(professional)
        }
    };
    let sceneArray = [
            `You see a few kids playing ${searchArray(["by climbing trees and houses and jumping down to scare people","with a pet","wall-ball","with a ball", "with some small figurines","tag","hide and go seek","freeze tag","hunter and prey"])}`,
            `You see a kid, sitting on a wall ${searchArray(["stargazing","counting the clouds","muttering to themselves",`looking ${searchArray(["longingly","lazily","pitifully", "desperately","anxiously"])} at ${searchArray(["another kid","the local bakery","over the horizon","the graveyard","the treeline"])}`,])}`,
            `You see a ${searchArray(["troubled","bored"])} ${person(0)} who ${searchArray(["can't decide what to do","seems to be daydreaming about someone",])}`,
            `You see a ${person(0)} in the process of ${searchArray(["stealing something", "pickpocketing someone","mugging someone"])}`,
            `You see ${searchArray([ "two boys", "two girls", "a boy and a girl", `a${searchArray([" young","n old"])} man and a${searchArray([" young","n old"])} woman`, `two old ${searchArray(["men","women"])}`])} ${searchArray(["complaining loudly","in a fistfight","playing chess","bickering back and forth",`making a deal`, `doing some scientific experiments`, `having a silent conversation`, `learning magic`, `playfully fighting`, `fishing`, `hiding from the rain`, `being nagged by ${person(2)}`])}`,
            `You see a group of ${person(4)} building ${searchArray(["a house","a boat","a wagon","a cart","some furniture"])}`,
            `You see a ${person(0)} casting a spell`,
            `You see a ${searchArray(["celebratory parade","funeral procession"])} for a ${searchArray(["well-loved","widely hated"])} ${person(1)}`,
            `You see ${person(2)} ${searchArray(["demonstrating a lack of control","demonstrating confident ignorance","showing absentmindeness","using unessicarily fancy words to impress people","unknowingly misuing words and phrases of speech", "avoiding eye contact","behaving foolishly"])}`,
            `You see ${person(3)} ${searchArray(["speaking with","discussing current events with","in a heated argument with","listening to",])} a${searchArray([" shabby-looking", " wise-looking"," surprisingly young-looking"," dirty-looking"," ancient-looking"," shifty-looking","n unassuming-looking","awe-inspiring","oddly attractive","wild-eyed"])} ${searchArray(["cleric","preist","sage","mage","paladin"])}`,
            `You see ${searchArray([person(2),person(3)])} ${searchArray(["stargazing","preparing for an exorcism","working with plants and gathering some",`saving someone from ${searchArray(["a wld animal attack","drowining in the river", "a monster attack",])}`,"trying to stop a fistfight","cheering on a fistfight","sifting through the destruction of a recent bandit attack","watching a group of bandits terrorizing their home","taking measurements of the land for some project","trying to combat nature",`${searchArray(["trying to calm a drunk man","loading things onto a cart","lifting and hauling heavy boxes","pushing a broken cart"])}`,"chasing someone","playing friendly games","in mass hysteria","performing a religious ceremony","preparing to hunt ghosts","preparing for a hunt","foraging","negotiating with some guards","arguing with some guards","selling holy amulets","clearing plants","cutting down trees","selling something","selling useless things","eating a meal","writing a letter", "writing letters","writing stories","writing poetry", "composing songs", "searching for a thief","painting","whittling","washing clothes","singing", "listening to a musician", "digging a large hole (excavating)"])}`,
            `You see ${person(2)} ${searchArray([`stuck ${searchArray(["under a dead horse", "under a broken wagon","under a fallen tree","in quicksand"])} calling for help`,"dishing out orders to others","quilting a blanket","sewing some clothes","using unfair weights in trades","in the process of forging something","wandering aimlessly",`${searchArray(["loading things onto a cart","lifting and hauling heavy boxes","pushing a broken cart"])}`,"chasing someone","panicing","seemingly in a hurry","performing a religious ritual","running from something, or someone",`bathing in the ${searchArray(["river","lake","ocean",])}`,"grooming themselves","offering to tell your fortune for the exclusive price of 1 gold","on their way to file papers with the local authority","performing some calculations with their finger in the air","sleeping on a bench","taking a nap in the grass","making a poor attempt to smuggle something past the guards",`hiding something (probably to smuggle it) in their ${searchArray(["horse's saddlebags","pack","wagon","bag of holding",])}`, `demonstrating an invention to ${person(3)}`, "begging for coins",`struggling with an illness`, `drying clothes`, `reeling from a spell effect`, `drunkenly wandering`, `acting very afraid of something`, `skinning an animal`, `translating signs/carvings`, `reading news`, `sending a mail pigeon`, `preparing meat`, `guarding someone, or something`, `doing artisan work`, `cooking`, `under a mental magic effect`, `hitchhiking`, `bluffing/denying something`, `speaking with shady people`, `mourning`, `performing a quest`, `following someone`, `gardening`, `gathering simple resourses (herbs, dyes etc.)`, `searching for a lost item`, `waiting for delivery`, `meditating`, `creating some alchemical concotion ( a cure for something)`, `parting with someone`, `counting coins`, `drawing schematics`, `preparing a potion`, `on a road to somewhere`, `sculpting`,])}`,
            `You see ${person(2)} that looks quite peculiar`,
            `You see a small group of ${person(4)} celebrating ${searchArray(["a reanimation ceremony","an initation ceremony","a birthday","the opening of a shrine", "a local holiday","something that involves a lot of drinking",])} `,
            `You see a small group of ${person(4)} having a ${searchArray(["nostalgiс","heated","lazy"])} ${searchArray(["argument","discussion","debate",])} about ${searchArray(["other races", "a local gossip","supernatural phenomena","their ancestors","the way things used to be","the other sex","current events", "the current ruler","politics",])}`,
            `You see a small group of ${person(4)} ${searchArray(["gathering to see a(n)", "currently attending/watching a(n)","leaving a recently ended"])} ${searchArray(["court proceeding","play","sports event","ressurection ritual","circus", "odd transport caravan", "public execution", "quarentine announcement","decree from the ruler","arrest", "magic (sleight of hand) show","the visiting of the local lord", "auction", "odd local competition or activity",])}`,
            `You come upon an area that ${searchArray(["should have people, and has evidence of people recently present, but there is nobody here","has a manned checkpoint made by local authorities","has a manned checkpoint made by a group impersonating local authorities",])}`, 
            `You see a ${person(0)} ${searchArray(["tithing to a local temple","damaging soem property","walking into the entrance of a mine","playing a ball game using mostly their feet with a few other players","admiring themselves in a reflection","sharing food with a young kid","gathering food", "looking at the horizon","faking the ability to do something","eavesdropping on a nearby conversation","warming themselves by a fire","praying","singing a hymn", "peeing in a bush on the side of the road"])}`,
            `You see a ${person(5)} ${searchArray(["collecting taxes","asking for donations for a local cause", "about to start a duel with another person","and their significant other getting married","proposing marriage to their significant other","collecting trash on a cart", "feeding a child", "flirting with another person", "healing someones wounds","taunting someone",`providing an inspirational message to ${person(3)}`, `teaching a lesson to ${person(3)}`, `loudly haggling with a ${searchArray(["craftsman","merchant","butcher","carriage-driver"])}`,"working in a manufacturing plant","learning from a teacher","tying somebody up","walking a drunk home","signing a contract","controlling a machine that they built","placing animal traps","selling illegal merchandise","setting up some explosives","on a pilgrimage", "changing clothes", "training some fighters", "mumbling under their breath","training some kids"])}`,
            `You see a small group of ${person(4)} ${searchArray([`up to some debaucherous antics`, `gambling on some games`, `preparing for something`, `telling stories to one another`, `training the local fighter regiment`, `trying to solve a local cattle theft`, `in a hideout/ambush spot`, `calming down a posessed person`, `engaged in a mass fistfight`, `doing a controlled burn of an area of forest`, `extinguishing a fire`, `searching for someone`, `doing a family activity`, `dancing together`, `advertising a product or service`, `fixing a broken ${searchArray(["house","cart","roof","wheel"])}`, `waiting for some adventurers to show up`, `smoking on a break`, `plowing a field`,])}`,
        ]
    let sceneArray2 = [
        `A child is throwing a tantrum in the street. One of their parents is standing nearby, pretending not to notice.`, `A patron is arguing with a shopkeeper over the price of an item that the shop doesn't sell.`, `A man is dancing in front of a group of elderly women. As he dances, the women will toss coins into his hat. Occasionally, one of the women will scoff and take some coins back.`, `Two Nobles are arguing the finer points of cockroach racing.`, `Neighbors are having a heated discussion about a noisy dog.`, `Graham the Hobo is performing an acrobatic pole dance.`, `Town guards are going door to door handing out flyers detailing changes to refuse disposal ordinances.`, `Three chickens are walking down the street stacked on top of each other.`, `A group of children are chasing a man with wooden swords. They are all laughing and shouting.`, `A wizard is seated across the table from an unnaturally large toad. The wizard is frantically flipping through several books.`, `A farmer is arguing with their cow. It seems the cow is unwilling to go where the farmer wants her to.`, `Drunken sailors are singing loudly from a tarven while the bar bouncer looks a them.`, `A town crier announces a gathering of the local religious group.`, `An unmarried couple walks hand in hand. Some passersby look at them and giggle.`, `A group of dock workers are team lifting a loaded wagon to reattach a broken wheel`, `A woman occasionally checking a small paper as she window shops`, `A young boy is selling newspapers on the corner. They aren’t selling well`, `Two horse-drawn carts slowly maneuver past each other as their drivers argue`, `A small circle of people are gathered around a pair of men locked in a serious match of arm wrestling`, `A small child runs through a gathering of pigeons`, `A goose steals a gardener's trowel and is chased for their audacity.`, `Graham the Hobo stands off to the side of the town square holding an old parchment aloft with the words, "Need Money for Ale. Why lie?"`, `A small cadre of druids are working on the community garden, cracking jokes and taking their time. It could be a class on growing but you aren't sure from this distance.`, 
        `A blacksmith loudly scolding his apprentice for a minor mistake.`, `A very pregnant mother shopping while her son, tied to her by her apron-strings, stomps in every mud-puddle he can reach. The mother doesn't seem to notice how muddy the son has gotten her dress.`, `A tired looking prostitute on the walk outside the brothel smoking a pipe with a very bored expression on her face.`, `A loaded haywain blocking traffic outside an inn's stables, the old driver is arguing with city watch, "I ain't movin till the innkeep's boys unload my wagon. He paid me for this load, he's gettin it!"`, `A down-on-the-heels entertainer sitting in the corner of the inn, muttering to himself as he attempts to compose a ballad. From the snippets the players can hear, the composition is not going well.`, `An obviously drunk person in the stockade playing rhyming games with a group of kids gathered around his penitent post.`, `While her father speaks with a street merchant, a little girl no more than three years of age saunters over to hug a dog that's taller than her. The towering dog allows it, even resting its head on her shoulder.`, 
        `Two children have taken a ball from a third, who looks to be on the verge of tears. A nearby horse whinnies as the older kids toss the ball back and forth, distracting one of the bullies at exactly the right moment to cause him to be pelted in the face. The younger kid snatches back their ball, sticks out their tongue, and runs away.`, `A young, overdressed nobleman is attempting to woo a lady. He steps in something unpleasant, and the trailing pair of chaperoning attendants struggle to contain their laughter.`, `Graham the Hobo seems to have decided that now would be an excellent time for a bath in a nearby fountain.`, `A small group of friars is administering short blessings and distributing loaves of bread to a queue of downtrodden families and street urchins.`, `An elderly couple quietly sits on a bench holding hands. Two old, feral cats are sitting together on their haunches at the other end of the bench. The old man and his coincidentally corresponding cat sneeze at the exact same time. Neither couple seems to pay any attention to the other.`, `Someone farts, nobody is that bothered`, `Plump teenage girl and her spindly younger brother are setting up fried chicken stand in the town square. There's a big wicker cage of doomed chickens softly clucking.`, `A fella sitting back in a chair, feet up on a table/what-have-you quietly humming a song to himself.`, `A group of ${rollDice(15)+2} men unloading a wagon.`, `A cat stalking a butterfly.`, `Two small boys climbing a tree.`, `A maid beating a rug.`, `A farmer plowing a field.`, `A horse throwing/losing his horseshoe.`, `A teenager chasing his/her/their dog, its leash trailing behind the dog.`, `A man proposing to a woman (or vice versa).`, `A person painting the side of his house/store.`, `A person cleaning the street (perhaps a punishment for a minor infraction of the law).`, 
        `A cleric on a soapbox preaching.`, `A flock of birds clustered around a bakery.`, `Local town councilman is putting up posters and shaking hands in the town square, reminding people of the upcoming election.`, `Two maintenance men lead a horse and cart with tar and cobblestones to repair potholes in the main streets of town.`, `There's a commotion at the local barbershop as a aging noblewoman with "the vapors" demands the barber to urgently soothe her stomach demons by reading her humors and applying leeches.`, `Brenda pushes her cart of home grown vegetables through the street toward the farmers market, muttering on about every perceived slight and insult she's received over the years from awful Farmer Mills, the man who has a wheat flour and baked goods cart.`, `A rat drags a piece of bread larger than it is along the street and into the sewer drain.`, `Two girls play hopscotch, one is called by her mother to come home. The other one frowns and eventually wanders off home.`, `Farmer Mills and Farmer Hewson argue about irrigation and water rights as the spring rains have been few and far between.`, `Graham the Hobo has set up a three card monte table outside a pub with a deck of cards that looks like he found in a ditch. "Try your luck" he shouts.`, `Graham the Hobo feeds a malnourished stray dog a small piece of bread from the loaf he is eating`, `Graham the Hobo sees a woman unknowingly drop a piece of fine jewelry, then returns it to her`, `A fisherman is digging up and collecting worms`, `A gnome tinkers with a toy dragon as a child watches in fascination.`, 
        `A group of children play as make-believe adventurers.`, `A noble buys a caged bird.`, `You notice a child picking the loose portions of a brick from a wall.`, `A well-dressed man with the voice of an auctioneer is selling a miracle cure for diseases no one’s heard of.`, `A young man taking the long way around the block/square or doubling back to peek in a window. He is nervous but doesn't seem to be doing anything wrong. He is sweet on a food vendor who works selling fried dumplings/ falafel and tries to find an opportunity to talk to her`, `A young man stop in the street and watch a particularly nice horse go by. He appears to be grocer or general store kind of assistant. His shirt is used but clean and his duties take him inside and outside a shop dusting carpets. If you watch for half an hour he lingers and studies a horse that has been tethered nearby. It's a nicer horse than most people see and you guess he knows how to judge good horseflesh by how he sizes them up.`, `There is a man on stilts, whitewashing the outside of a house. He rolls his eyes and is curt with everyone who makes a joke about "how's the weather up there?". He mutters to himself that this is more efficient than a ladder. He openly yells and tells off a group of three kids who clearly are working towards a plan to mess with his stilts.`, `A young woman briefly stops to smell the fresh bread as she walks past the bakery.`, 
        `A man leaves a large building and pauses for a moment. He pats his pockets, sighs in disappointment, then goes back into the building to grab whatever he had forgotten.`, `Two men load a cart outside of a home while a nobleman speaks to the homes crying owner reviewing a piece of parchment.`, `Another child is throwing a tantrum in the street, crying about not wanting to go inside.`, `A couple is arguing outside a tavern.`, `A woman stands by the water, washing clothes.`, `A group of three men teasing each other over a dice game.`, `An older fruit salesman demonstrates to a curious onlooker how to use a mallet to crush grapes in a small vat.`, `Two children arguing over a toy, and their mother hanging her clothespins, oblivious.`, `A couple in deep discussion about whether or not to spend their savings on a new property or to continue saving.`, `Two children playing a game of marbles. They are about seven years old. One has a ring of blue, red, and yellow marbles. The other has a ring of green, blue, and purple.`, `Two children playing on top of a hay wagon. They appear to be twin brothers about five years old.`, 
        `Two ducks with ducklings following them. You are confused why they're here in the village, but their wet footprints likely lead back to a small pond nearby.`, `Two ducks are in a pen with their latest batch of babies. One of the villagers say that they are "mill" ducks and how it's such a pity they have been cross breeding them for centuries to attain a perfect egg-laying machine.`, `A small brown hare drinking from a stream. It is quite a ways away from the rest of a batch of rabbits that are gathering near the feet of two hunters. The brown hare also seems to lack the distinctive black ears and white nose of the others.`, `A small fence surrounds a nearly empty plot of land. This plot of land apparently is where the town gallows currently sit. The current hanging dummy, a simple wooden figure of a man, stands with a sign that reads "Thievery."`, `A local town boy is selling a box of potentially enchanted cookies`, `Shopkeeper and his employee brother are splitting up the profits. “Four for me, one for you. Four for me, one for you.” “That’s not fair! I work twice as hard as you.” “Oh really?! But I take all the risk! Alright then. FIVE for me, one for you.”`, `Graham the Hobo deftly stops a child from wandering into the path of a moving wagon`, `A man is talking to a woman. They aren't doing anything important, but a passing man in a hat smiles at them.`, `A child is missing his two front teeth.`, `A little girl leading around a goat with a string.`, `The village blacksmith and his neighbor are talking with each other over the fence that separates their two houses.`, 
        `You see a thatched roof house near the edge of town. A female halfling walks out of the front door and stands on the porch. She turns and says something to someone inside, then turns and shuts the door.`, `A young man is practicing archery by himself.`, `You hear a scream, and as you glance up, it turns out to be someone's shriek of happy recognition as a woman sees an old friend they haven't seen in a while.`, `An old man, with two days of beard stubble and stains on his shirt, stands on a street corner scratching the top of his butt crack and watching people walk by.`, `Three people have stopped hanging linens and are arguing about the lyrics to a well known song. Two of the trio insist that the last person is singing the lyrics wrong. The song is about adding to the parts of a tree and repeating previous verses: 'The branch was on the limb, the limb was on the tree, the tree was on the stump, the stump was in the hole...' (In real life it's the song 'Rattlin Bog' if you don't want to make your own lyrics)`, `The two are correct. There's regional variance on certain words, but the third person is just getting the order of the tree wrong.`, `Interestingly, surrounding townsfolk not in the trio begin singing after a few minutes of the trio arguing over the lyrics.`, `Three girls are jumping rope and are learning a new trick`, `A farmhand or shepard/ranch hand is juggling. She's not passing the hat or anything, she is bored, standing next to a wagon. To a trained eye she is self-taught, and can do columns, cascade, and reverse cascade. Her older sister sits in the wagon, minding the horse pulling it. The wagon sits outside a post-station. The wagon has shovel and pickaxe heads and bundles of appropriately sized wooden staves in the back of it.`, `A small group of people have placed a mug on a bench and are attempting to throw rocks into it from increasingly longer distances.`, 
        `A father is lecturing his child about having warned them about the sharp rocks and slick footing as the child is whiping away tears with a bloody gash on their leg as the dad wraps the leg in bandages.`, `A small cluster of merchants are leaving their office and undoing their coats and ties as they step out into the hot air of the day.`, `The local dockmaster cheerily walks by holding a fishing set and tackle.`, `The herbalist tends to their small garden taking deep breaths of every crop therein before and after trimming.`, `A nobleman attempting but failing to nonchalantly exit the home of a prostitute. He quickly tries to hide his face from anyone making eye contact with him. Smells of liquor and cheap perfume.`, `Two boys walking down the street. One steps in a pile of dog poop. The other boy laughs at his misfortune before stepping into a much larger pile of horse poop a few steps later. The first boy quickly turns from scowling to laughing hysterically at the second boy.`, `A cat licking the ear of a dog that is lying outside the door to a shop.`, `A goat standing inside a small pen. A puppy wiggles under the fence and begins nursing from the goat’s teat.`, `A very lovable dog approaches your party wanting to be petted. Roughly tries to sniff the crotch of each member before urinating on anyone with any elvish heritage.`, `A little girl playing with her dollies acting out an argument she apparently heard between her parents.`, `An old woman approaches your party who opens her coat and offers to sell various items of “fine, expensive jewelry”. All items are either made from wood, string and garbage or are completely imaginary. She spits on the party when they refuse to consider her wares.`,
    ]
    printFrom(sceneArray, 3,"Scene")
    printFrom(sceneArray2, 2,"Scene")
};

//Before Everything - non-dependant 
let rumorType = ["False (Appears as Specific or Exact)", "Vague", "Mixed", "General", "Specific", "Exact", ]
let IVendetta = ["they were wrongfully jailed or persecuted", "of a racial crusade", "they want revenge for theft or deception", "they want revenge for personal death(s)", "they are on a religious crusade (local or part of a Faithquest)", "of political persecution", "their social status was destroyed and/or they were socially exiled", ]
let KBuyingOrSelling = ["Cloth - (Raw or Finished)", "Wood - (Raw, Finished, Furniture, Containers, Paper)", "Food - (Random types (air, sea, land) from random culture)", "Beverages -(Brewed (Ales), Distilled (Spirits), Raw (Juice), Dried (Teas) or Water)", "Spice - (Salt, Random spice, Random herb, Il(legal) drugs, or Medicine)", "Minerals - (Raw or Refined or Gems)", "Luxury - (Art, Rare Commodity or Masterwork items/weapons/armor)", ]
let LHomeland = [`(Homeland: A place from your world)`, ]
let QMinorEnemy = ["a snubbed ex-friend", "a school bully", "a business rival", "a local thug", "a romantic rival", "a spiteful boss or teacher", "a family member", ]
let RMajorEnemy = ["a politician or political group", "a powerful rogue/thug/assassin", "a noble's family", "a religious cult, sect, group, or temple", "a powerful mage or cabal", "a mercenary group", "a mysterious NPC", ]
let SHaunted = ["spirits locked in battle", "a tortured revenant who must relive its brutal murder", "a benign phantom who provides small comforts and messages", "a crazed banshee", "a spiteful haunt, who appears as dead loved ones and friends", "a playful poltergeist, a childish trickster", "an evil ghost, driven to consume lifeforce in a bid to regain life", ]
let TCursed = ["where time moves at a different speed", "where sleep and rest is impossible", "where the weather is extremely hot or cold", "where they experience an overwhelming aura of helplessness and suffering", "where there are plagues of vermin", "where there is constant foul weather", "where a corruption of reality occurs", ]
let VEmergency = ["political power is dead or arrested/exiled", "business in trouble", "family friend ill or mad or dead", "hometown has been attacked or enslaved or destroyed", "disease epidemic ", "close relative or spouse has done something terrible", "all resources or income has been stolen or destroyed", ]
let WWarning = ["a powerful enemy coming for you", "an enemy plotting against you", "how the government is investigating you", "a friend or lover or spouse lying to you", "a co-worker or business partner is stealing from you", "a rival spreading terrible lies and rumors", "an avatar coming", ]
let XSocialEvents = ["An invitation to an upcoming event (party, play, etc..) given by a mysterious stranger. ", "A local revival of (insert deity) followers is nearby, and drawing crowds", "A challenge has been issued by the (local ruler), calling for Feats of (insert ability)", "The (guild-house) is permitting new members to join, decided by a contest", "A circus has come to town. Rumors are they are taking on workers", "A fancy dress party for the (local ruler) has drawn all the wealthy in the area", "The marriage/birth/death/divorce/something else of (local ruler) or (ruler's family/spouse)", ]
let YPoliticalEvents = ["opposition gaining control through a coup", "downshift in the support of financial backers has driven prices way up", "noble accused of a terrible crime", "marriage between noble houses has been announced, while rumors of treachery persist", "shift in the government's stance on taxes has been taken badly by the populace", "rumor of corruption, and evidence of murder and treachery is begin sought", "powerful figure that has been killed, exiled, or worse", ]
let ZReligiousEvents = ["an avatar issuing sanctions", "open warfare against temple enemies is now public knowledge", "a new edict/sanction being announced and the resultant radical shift in the local population's mood", "an expedition to the Heathen Lands has been announced", "temple leaders declaring a peace agreement and a Summit of Faith is announced.", "an artifact or holy relic has been found/destroyed and a Call to the Faithful has gone out", "an avatar appears and denounces the faithless/blesses the faithful and punishes/rewards with a bane/boon", ]
let AAFaithTouched = ["dreams of the lives of those who gave their lives in sacrifice for the Faith", "all skills relating to the practice of the faith are more easily accomplished. +1", "hallucinations of the landscape of the deity's Plane haunt the waking mind", "those not of the Faith will be psionically attacked by the environment, driving them out", "animal servants of the deity roam the grounds here, protecting from heathen intruders", "all divine spells are cast here as if the caster was 1 level higher.", "manifestation of an Avatar. Its mood depends on the PCs interaction", ]
let BBWeaveTouched = ["a living mask of a Jester can be found here, hidden, but waiting. The parasite sleeps.", "all skills relating to the practice of the arcane mysteries are more easily accomplished. +1", "time and space are on vacation here. Non-causality is a possibility. Dimensionally weird.", "all arcane objects are recharged here, but can only be used once per item per location", "astral and ethereal creatures are feeding from this bountiful font. They are hostile", "all arcane spells are cast here as if the caster were 1 level higher", "wild magic regularly spawns here, bathing the area with random level spells and duration", ]
let CCMysteryCult = ["that is trying to return/exile/free/enslave/destroy/rebirth a minor/major deity", "that is collecting objects to trade to a deity for power", "are thralls under a larger power, acquiring resources, knowledge, manpower for a larger plan", "of disaffected people angry at inequality. They have resorted to violence and rhetoric", "of animal worshipers, devoted to returning humanity to a more primal lifestyle", "of outsiders stealing/killing/trading/enslaving/helping the local populace", "of wealthy cannibals and defilers, seeking only pleasure for themselves", ]
    //C

    function findArtifact() {
    let chance = rollDice(100)
    if (chance < 95) {
        return "an artifact"
    } else {
        return "a piece of a legendary set of artifacts"
    }
};

function findMisc() {
    let misc = [
        "piece of jewelry", "chest", "map", "bucket", "lantern", "jar"
    ]
    return `a legendary ${ searchArray(misc) }`
};

function findArmor() {
    let chance = rollDice(100)
    if (chance < 90) {
        return "a single piece of legendary armor"
    } else {
        return "one part of a legendary set of armor"
    }
};

function findWeapon() {
    let chance = rollDice(100)
    if (chance < 70) {
        return "a common missle or melee weapon"
    } else if (chance < 95) {
        return "a uncommon missle or melee weapon"
    } else {
        return "a rare missle or melee weapon"
    }
};

function findArtPiece() {
    let artArray = [
        "rod", "staff", "wand", "sceptre", "crown", "gemstone"
    ]
    return `a ${ searchArray(artArray) } of high value or untold power`
};

function findCulturalArtifact() {
    let culturalArtifacts = [
        "a statue", "a painting", "an instrument", "some sheet music", "an article of clothing",
    ]
    return `${ searchArray(culturalArtifacts) }, which is a cultural artifact of great respect`
};

function findWeird() {
    let chance = rollDice(100)
    if (chance < 75) {
        return "a mysteriously preserved body part of great power"
    } else {
        return "a mysteriously preserved organ of great power"
    }
};

let CIteminformation = [`${ findArtifact() }`, `${ findMisc() }`, `${ findArmor() }`, `${ findWeapon() }`, `${ findArtPiece() }`, `${ findCulturalArtifact() }`, `${ findWeird() }`, ]

function informationSearch() {
    let chance = rollDice(100)
    if (chance < 33) {
        return "They are searching for information about " + searchArray(APersonalInformation)
    } else if (chance < 67) {
        return "They are searching for information about " + searchArray(BLocalInformation)
    } else {
        return "They are searching for information about " + searchArray(CIteminformation)
    }
};

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
};
//needs to be after C
let UTreasure = ["a set of potions", "a bag of gems", "some weapons or armor", "a stash of coins", "a few wands, rods, and staves", "a few pieces of clothing", `${searchArray(CIteminformation)}`, ]
let NMajorQuest = ["awaken a sleeping NPC", `recover or destroy an ${searchArray(CIteminformation)}`, "aid or slay an NPC", "slay a monster", "liberate or enslave an NPC", "discover a lost foreign land", "save or destroy the world", ]
let MMinorQuest = ["commune with an avatar", "map a location", "deliver a message", `recover a special ${searchArray(UTreasure)}`, "deliver a package", "destroy a minor monster/cleanse a tainted area", "rediscover a local forgotten place", ]
let HMajorBoon = [`divine intervention that grants ${searchArray(UTreasure)}`, `true Knowledge of the location of ${searchArray(UTreasure)} is obtained `, `a large amount of monetary wealth`, `(+1) for an existing skill or knowledge, or a new skill is obtained`, ` hot to improve a personal relationship to 100%`, `a major property being awarded or an improvement to a major property is granted`, `a specific rumor for ${searchArray(CIteminformation)}`, ]

//after non dependent
function enemyChooser() {
    let chance = rollDice(100)
    if (chance < 50) {
        return searchArray(QMinorEnemy)
    } else {
        return searchArray(RMajorEnemy)
    }
};

function questFinder() {
    let chance = rollDice(100)
    if (chance < 50) {
        return searchArray(MMinorQuest)
    } else {
        return searchArray(NMajorQuest)
    }
};
let JOnTheRun = ['they committed political crime', 'they escaped from detention for a crime', 'they committed minor crime of theft, fraud or assualt', 'they committed major crime of theft, murder or rape (or this can be substituted with anarchy)', 'they committed religious crime', `they got tangled up with a myystery cult ${searchArray(CCMysteryCult)}`, 'unjustly accused', ]
let DFaction = [`a mystery cult ${searchArray(CCMysteryCult)}`, `a group of slavers or brutal overlords`, `a group of religious warriors or clerics`, `a group of law and justice officers or warriors`, `a group of corrupt mercenaries or rogues`, `a merchant collective or guild`, `a cabal of mages`, ]

//after enemyChooser
function friendOrEnemy() {
    let chance = rollDice(100)
    if (chance < 50) {
        return "a friend"
    } else {
        return enemyChooser()
    }
};
let GMinorBoon = [`an enemy, ${enemyChooser()}, being temporarily thwarted`, `a minor magic item`, `a small amount of money or resources`, `a magicked gemstone (use 0-level or Cantrip effect, 1/day, as level 1 caster)`, `a minor property or an improvement to a minor property`, `a personal relationship established with potential ally or social status increases with ally`, `for one day, all activities to be easier. +1`, ]
let FMajorBane = [`bad luck (random penalties[disadvantage] to random die rolls) for 1 month or 10 combats`, `an outbreak of a large plague or pestilence`, `a large loss of monetary wealth`, `many items of value have being lost or destroyed`, `many buildings and/or the land being damaged`, `many people being killed`, `the PC or Party attracting the negative attention of ${enemyChooser()}`, ]
let EMinorBane = ['a disease or pestilence', 'buildings being destroyed', `the PC or Party enemy, ${enemyChooser()} to now actively oppose them`, 'the loss of items of value', `a curse, ${searchArray(TCursed)}, being activated`, 'people being injured', `the PC or Party being haunted by ${searchArray(SHaunted)}`, ]
let BLocalInformation = [`tells of something in the area that could cause ${searchArray(GMinorBoon)}.`, `tells of ${ searchArray(VEmergency) }`, `passes along knowledge of a ${ searchArray(XSocialEvents) }`, `gives information about a threat from an ememy, ${ enemyChooser() }`, `passes along information of a ${ searchArray(YPoliticalEvents) }`, `gives information about ${ searchArray(ZReligiousEvents) }`, `tells of ${ searchArray(FMajorBane) }`, ]
let APersonalInformation = [`a secret that leads to ${searchArray(HMajorBoon)}`, `a family emergency caused by ${searchArray(VEmergency)}`, `a ${searchArray(rumorType) } rumor about the PC as told by ${ friendOrEnemy() }`, `a suspicion held by the PC or the Party`, `a small warning regarding ${searchArray(WWarning)}`, `something the PC or Party has been investigating`, `- no, gives a severe warning about ${searchArray(WWarning)}`, ]

function faithOrWeave() {
    let chance = rollDice(100)
    if (chance < 50) {
        return "This place is Faithtouched - " + searchArray(AAFaithTouched)
    } else {
        return "This place is Weavetouched - " + searchArray(BBWeaveTouched)
    }
};

function hauntedOrCursed() {
    let chance = rollDice(100)
    if (chance < 50) {
        return "This place is haunted by " + searchArray(SHaunted) + "."
    } else {
        return "This place has a cursed reality " + searchArray(TCursed) + "."
    }
};

let monsters = ['aarakocra', 'aboleth', 'angels', 'animated object', 'animated weapon', 'ankheg', 'azer', 'banshee', 'basilisk', 'behir', 'beholder', 'blight', 'bugbear', 'bulette', 'bullywug', 'cambion', 'carrion crawler', 'centaur', 'chimera', 'chuul', 'cloaker', 'cockatrice', 'couatl', 'crawling claw', 'cyclops', 'darkmantle', 'death knight', 'demilich', 'demon', 'devil', 'dinosaur', 'displacer beast', 'doppleganger', 'dracolich', 'shadow dragon', 'dragon', 'dragon turtle', 'drider', 'dryad', 'duergar', 'elemental', 'empyrean', 'ettercap', 'ettin', 'faerie dragon', 'flameskull', 'flumph', 'fomorian', 'fungi', 'galeb duhr', 'gargoyle', 'genie', 'ghost', 'giant', 'gibbering mouther', 'gith', 'gnoll', 'goblin', 'golem', 'gorgon', 'grell', 'grick', 'griffon', 'grimlock', 'hag', 'half dragon', 'harpy', 'hell hound', 'helmed horror', 'hippogriph', 'hobgoblin', 'homunculus', 'hook horror', 'hydra', 'intellect devourer', 'invisible stalker', 'jakalwere', 'kenku', 'kobold', 'kraken', 'kuo-toa', 'lamia', 'lich', 'lizardfolk', 'lycanthrope', 'magmin', 'manticore', 'medusa', 'mephits', 'merfolk', 'merrow', 'mimic', 'mind flayer', 'minotaur', 'modron', 'mummie', 'myconid', 'naga', 'nightmare', 'nothic', 'ogre', 'oni', 'ooze', 'orc', 'otyugh', 'owlbear', 'pegasus', 'peryton', 'piercer', 'pixie', 'psuedodragon', 'purple worm', 'quaggoth', 'rakshasa', 'remorhazes', 'revenant', 'rox', 'roper', 'rust monster', 'sahuagin', 'salamanders', 'satyr', 'scarecrow', 'shadow', 'shambling mound', 'shield guardian', 'skeleton', 'slaadi', 'specter', 'sphinx', 'sprite', 'stirge', 'succubus', 'incubus', 'terrasque', 'thri-kreen', 'treant', 'troglodyte', 'troll', 'umber hulk', 'unicorn', 'vampires', 'water weird', 'wight', `will-o'-wisp`, 'wraith', 'wyvern', 'xorn', 'yeti', 'yuan-ti', 'yugoloth', 'zombie', 'ape', 'awakened tree', 'awakened shrub', 'axe beak', 'baboon', 'badger', 'bat', 'black bear', 'blink dog', 'blood hawk', 'boar', 'brown bear', 'camel', 'cat', 'constrictor snake', 'crab', 'crocodile', 'death dog', 'deep', 'dire wolf', 'draft horse', 'eagle', 'elephant', 'elk', 'flying snake', 'frog', 'giant ape', 'giant badger', 'giant bat', 'giant boar', 'giant centipede', 'giant constrictor snale', 'giant crab', 'giant crocodile', 'giant eagle', 'giant elk', 'giant fire beetle', 'giant frog', 'giant goat', 'giant hyena', 'giant lizard', 'giant octopus', 'giant owl', 'giant poisonous snake', 'giant rat', 'giant scorpion', 'giant sea horse', 'giant shark', 'giant spider', 'giant toad', 'giant vulture', 'giant wasp', 'giant weasel', 'giant wolf spider', 'goat', 'hawk', 'hunter shark', 'hyena', 'jackal', 'killer whale', 'lion', 'lizard', 'mammoth', 'mastiff', 'mule', 'octopus', 'owl', 'panther', 'phase spider', 'poisonous snake', 'polar bear', 'pony', 'quipper', 'rat', 'raven', 'reef shark', 'rhinoceros', 'riding horse', 'saber-toother tiger', 'scorpion', 'sea horse', 'spider', 'bat swarm', 'insect swarm', 'poisonous snake swarm', 'quipper swarm', 'rat swarm', 'raven swarm', 'tiger', 'vulture', 'warhorse', 'weasel', 'winter wolf', 'wolf', 'worg', ]
let monsterEncounter = ["a flock of aarakocra", "an ankheg", "some bugbears", "a behir", "a sinkhole", "a traveling NPC", "a bulette", "a centaur", "a chimera", "a cockatrice", "a couatl", "a sealed entrance to the UnderDark", "an abandoned hunter's cabin", "a displacer Beast", "some dryad", "an earth elemental", "an ettin", "a faerie dragon", "weather phenomenon/disaster", `a ${searchArray(monsters)} and dead handlers`, "army patrol from (nearby military encampment suitable to your world.)", "a galeb duhr", "a gargoyle", "Hill Giants", "a gibbering mouther", "gnolls", "a large cavern system", "an abandoned cave", "a malignity of Goblins", "ghouls", "a hippogriff", "hobgoblins", "a hydra", "a deactivated colossus", "an evil cleric and minions performing ritual", "a jackalwere", "a manticore", "ogres", "orcs", "owlbears", "an unpowered standing circle of stones", `an old battlefield full of ${searchArray(monsters)} skeletons`, "a rust monster", "some satyr", "stirges", "treants", "trolls", "a cycle gate", "an abandoned fort/tower/temple", "a wyvern", ]
let npcReactionToQuestioning = [`Hostile, now a nemesis. This interaction results in ${searchArray(FMajorBane)}. Also this NPC Will pursue PC until dead.`, `Unhappy, this interaction results in ${searchArray(EMinorBane)}. ${shiftCheck('unhappy')}`, `Disgruntled. The NPC gives false information. ${shiftCheck('disgruntled')}.`, `Tells you about ${searchArray(APersonalInformation)}, or ${searchArray(BLocalInformation)}, as requested `, `They are pleased. They share a ${searchArray(rumorType)} Rumour. ${shiftCheck('pleased')}`, `Happy. Rewards PC or Party with ${searchArray(GMinorBoon)}. ${shiftCheck('happy')}`, `Friendly, now an ally. Gives information about ${ searchArray(HMajorBoon) }. Will protect PC until dead.`, ]

function hostile() {
    document.getElementById("Reaction").innerHTML = npcReactionToQuestioning[0]

};

function unhappy() {
    document.getElementById("Reaction").innerHTML = npcReactionToQuestioning[1]
};

function disgruntled() {
    document.getElementById("Reaction").innerHTML = npcReactionToQuestioning[2]
};

function neutral() {
    document.getElementById("Reaction").innerHTML = npcReactionToQuestioning[3]
};

function pleased() {
    document.getElementById("Reaction").innerHTML = npcReactionToQuestioning[4]
};

function happy() {
    document.getElementById("Reaction").innerHTML = npcReactionToQuestioning[5]
};

function friendly() {
    document.getElementById("Reaction").innerHTML = npcReactionToQuestioning[6]
};

function reaClear() {
    document.getElementById("Reaction").innerHTML = ""
};

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
};

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
};

function reload() {
    location.reload()
};