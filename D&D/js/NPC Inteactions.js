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

/*==================================================================================*/
/*-----------------------------Page Scripts Below-----------------------------------*/
/*==================================================================================*/

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
        `A father is lecturing his child about having warned them about the sharp rocks and slick footing as the child is wiping away tears with a bloody gash on their leg as the dad wraps the leg in bandages.`, `A small cluster of merchants are leaving their office and undoing their coats and ties as they step out into the hot air of the day.`, `The local dockmaster cheerily walks by holding a fishing set and tackle.`, `The herbalist tends to their small garden taking deep breaths of every crop therein before and after trimming.`, `A nobleman attempting but failing to nonchalantly exit the home of a prostitute. He quickly tries to hide his face from anyone making eye contact with him. Smells of liquor and cheap perfume.`, `Two boys walking down the street. One steps in a pile of dog poop. The other boy laughs at his misfortune before stepping into a much larger pile of horse poop a few steps later. The first boy quickly turns from scowling to laughing hysterically at the second boy.`, `A cat licking the ear of a dog that is lying outside the door to a shop.`, `A goat standing inside a small pen. A puppy wiggles under the fence and begins nursing from the goat’s teat.`, `A very lovable dog approaches your party wanting to be petted. Roughly tries to sniff the crotch of each member before urinating on anyone with any elvish heritage.`, `A little girl playing with her dollies acting out an argument she apparently heard between her parents.`, `An old woman approaches your party who opens her coat and offers to sell various items of “fine, expensive jewelry”. All items are either made from wood, string and garbage or are completely imaginary. She spits on the party when they refuse to consider her wares.`,
    ]
    printFrom(sceneArray, 3,"Scene")
    printFrom(sceneArray2, 2,"Scene")
};
function cat(){
    
    let size = [
        "skin and bones",
        "little scrawny",
        "pretty average in size",
        "little long and lanky",
        "fat",
        "chonky",
        "small and dainty",
        "muscular and toned",
        "gracefully slender",
        "stout and sturdy",
        "petite and delicate",
        "big-bellied",
        "brawny and imposing",
        "sleek and athletic",
        "rounded and plump",
        "long and lean",
        "compact and stocky",
        "majestically large",
        "tiny and compact",
        "slim and elegant",
        "hefty and robust",
        "lean and wiry",
        "well-proportioned",
        "svelte and trim",
        "delicately petite"
    ]
    let color= [
        "solid white",
        "solid black",
        "solid grey",
        "grey and black spotted tabby",
        "orange and black spotted tabby",
        "grey and black striped tabby",
        "orange and white striped tabby",
        "grey and black blotched tabby",
        "black and white bicolor",
        "white and orange bicolor",
        "calico",
        "blue",
        "cream",
        "chocolate",
        "cinnamon",
        "fawn",
        "seal point",
        "chocolate point",
        "lilac point",
        "blue point",
        "red point",
        "cream point",
        "tortoiseshell",
        "smoke",
        "silver tabby",
        "golden tabby",
        "red and white bicolor",
        "silver and white bicolor",
        "chocolate and white bicolor",
        "blue and white bicolor",
        "tortoiseshell and white bicolor",
        "sable",
        "flame point",
        "tortie point",
        "lynx point",
        "marbled",
        "spotted",
        "ticked",
        "brindle",
        "caliby (calico tabby)",
        "van pattern",
        "mink pattern",
        "pointed pattern",
        "tuxedo pattern",
        "harlequin pattern",
        "rosetted pattern",
        "merle pattern",
        "agouti pattern",
        "painted pattern"
    ];
    let eyes = [
        "yellow eyes",
        "golden brown eyes",
        "copper brown eyes",
        "dull green eyes",
        "bright green eyes",
        "brilliant gold eyes",
        "copper eyes",
        "bright blue eyes",
        "pale blue eyes",
        "bluish grey eyes",
        "one blue eye and one golden brown eye",
        "one blue eye and one copper brown eye",
        "amber eyes",
        "hazel eyes",
        "vibrant violet eyes",
        "deep purple eyes",
        "emerald green eyes",
        "jade green eyes",
        "sapphire blue eyes",
        "turquoise eyes",
        "ice blue eyes",
        "smoky grey eyes",
        "steel grey eyes",
        "teal eyes",
        "heterochromia (two different colored eyes)",
        "silver eyes",
        "ruby red eyes",
        "pearl white eyes",
        "fiery orange eyes",
        "citrine yellow eyes",
        "sunset orange eyes",
        "peridot green eyes",
        "amethyst purple eyes",
        "topaz brown eyes",
        "onyx black eyes",
        "aqua blue eyes",
        "glimmering gold-flecked eyes",
        "moonlit silver-flecked eyes",
        "iridescent opal eyes",
        "midnight blue eyes",
        "rose pink eyes",
        "peacock blue eyes",
        "mystic grey eyes",
        "glistening aquamarine eyes",
    ]
    let bredTo = [
        "to hunt mice in granaries",
        "to hunt mice in urban dwellings",
        "to hunt rats aboard ships",
        "to hunt rats and mice in barns",
        "to hunt birds on rooftops",
        "to hunt snakes and lizards",
        "to sit on laps",
        "for no particular reason; its ancestors were semi-feral village cats",
        "for no particular reason; its ancestors were semi-feral city cats",
        "for no reason at all; its ancestors were wild animals",
        "to serve as familiars for magic users",
        "to guard temples and sacred places",
        "to assist in fishing by catching fish at the water's edge",
        "to provide companionship to lonely individuals",
        "to warn of approaching danger with their keen senses",
        "to entertain and perform tricks in circuses or traveling shows",
        "to aid in pest control for farmers or merchants",
        "to be revered and worshipped as divine beings in certain cultures",
        "to guide lost souls to the afterlife, according to folklore",
        "to protect homes and properties from malevolent spirits",
        "to accompany and protect children on their adventures",
        "to carry messages between different groups or communities",
        "to bring good luck and prosperity to their owners",
        "to act as guardians of sacred knowledge and ancient artifacts",
        "to be the companions of wise sages and hermits in secluded places",
        "to participate in traditional festivals and ceremonies",
        "to share a deep bond with a specific human or family for generations",
        "to roam ancient ruins and decipher forgotten hieroglyphics",
        "to assist in magical alchemy by identifying potent ingredients",
        "to weave enchanting melodies with their purring for soothing effects"
    ]
    let favFood = [
        "warm milk",
        "mice",
        "baby mice",
        "songbirds",
        "pigeon",
        "chicken",
        "sardines",
        "tuna",
        "salmon",
        "bacon",
        "cooked turkey",
        "trout",
        "shrimp",
        "tasty fish treats",
        "steamed salmon",
        "chewy beef",
        "crunchy tuna kibbles",
        "duck",
        "quail eggs",
        "lobster",
        "grilled chicken",
        "calamari",
        "anchovies",
        "sushi",
        "scrambled eggs",
        "canned tuna in water",
        "roast duck",
        "roasted lamb",
        "buttered prawns",
        "shredded cheese",
        "oysters",
        "smoked salmon",
        "crab meat",
        "baked mackerel",
        "honey-glazed ham",
        "meat-flavored gravy",
        "grilled steak",
        "pork chops",
        "chicken liver",
        "smoked herring",
        "salmon mousse",
        "shrimp cocktail",
        "tuna tartare"
    ]
    let markings =[
        "white or black toes on one foot",
        "extremely long whiskers",
        "a white or black tipped tail",
        "no tail",
        "a broken tail",
        "a scarred ear",
        "a patch of missing fur",
        "a pink nose",
        "a black nose",
        "a pink and black nose",
        "heterochromia (two different colored eyes)",
        "an extra toe (polydactyl)",
        "tufted ears",
        "a distinctive birthmark",
        "a natural bobtail (naturally short tail)",
        "a split nose (bifid nose)",
        "large, expressive eyes",
        "different colored fur patches (calico or tortoiseshell)",
        "a distinctive spot or stripe pattern",
        "oversized or unusually small ears",
        "webbed paws",
        "a curled tail",
        "extra fluffy fur",
        "one ear that stands upright and one that folds down",
        "distinctive facial markings",
        "brightly colored fur in certain areas",
        "glowing eyes (in the dark or under specific conditions)",
        "an unusually deep or high-pitched meow",
        "long, elegant whiskers that sweep gracefully",
        "a unique pattern resembling a heart or star on its fur",
        "a tail with a unique curl or kink",
        "tufts of fur between the toes (snowshoe feet)",
        "a sleek, shiny coat that reflects light",
        "a distinctive stripe running down the back",
        `a "M" shape on the forehead (M-shaped tabby marking)`,
        `a well-defined "eyeliner" pattern around the eyes`,
        "brightly colored eyes that change with emotions",
        "a tufted tail tip",
        "a unique and endearing vocalization",
        "extra long hind legs for jumping great distances",
        "a small, heart-shaped nose pad",   
        "a feathery tail",
        "a faint bioluminescent glow on the fur",
        "fur that changes color with the weather or surroundings",
        "a tiny crown-shaped marking on the head",
        "a 'spectacle' marking around the eyes",
        "a pattern that resembles constellations on the fur",
        "feathery tufts on the ears",
        "a tail that resembles a fluffy plume",
        "a faint, sweet scent that is naturally emitted from its fur",
        "a unique ability to mimic certain sounds or words",
        "a small, hidden pouch on the belly",
        "distinctive paw pads that resemble little heart shapes"
    ]
    let habits = [
        "a habit of hiding whenever it first meets someone",
        "a habit of begging for food",
        "a mistrustful demeanor, even toward people it knows well",
        "a playful demeanor, always chasing its tail",
        "a curious demeanor, always sneaking up and pouncing on things",
        "a noisy yowl when it is sad",
        "a cute little meow when it is content",
        "a habit of purring and rubbing against your leg",
        "a habit of hissing at any who approach it",
        "a friendly demeanor, provided you have food",
        "a habit of bringing gifts (e.g., small toys or prey) as presents",
        "a nocturnal habit, being most active during the night",
        "a habit of kneading with its paws when it is relaxed or happy",
        "a habit of stealing shiny objects and hoarding them in a secret spot",
        "a grooming ritual where it meticulously cleans itself several times a day",
        "a talkative nature, always meowing to communicate with its owner",
        "a habit of waking up its owner at the same time every morning",
        "a fascination with water and a habit of playing with it",
        "a tendency to follow its owner around the house like a shadow",
        "a habit of perching on high places to observe its surroundings",
        `a playful habit of "hunting" and "catching" toys or insects`,
        "a habit of stretching itself in the sun to bask in the warmth",
        "a habit of bringing comfort to its owner by cuddling close",
        "a habit of curling up in tight spaces for naps",
        "a fondness for sitting on paper or laptop keyboards",
        "a mischievous habit of knocking items off tables or shelves",
        "a habit of pawing at doors to be let in or out of rooms",
        "a ritual of sharpening its claws on specific scratching posts",
        "a habit of following a daily routine, such as mealtime or playtime",
        `a habit of "talking" to birds or other animals through windows`,
        `a habit of seeking attention by headbutting or "booping" its owner`,
        "a cautious habit of exploring new environments slowly and carefully",
        "a habit of rolling onto its back to expose its belly for rubs",
        "a habit of chasing its tail or shadow when bored",
        "a content habit of purring loudly when it finds a comfortable spot",
        "a curious habit of inspecting anything new in its environment",
        "a habit of grooming and snuggling with other pets in the household",
        `a habit of "patrolling" its territory to ensure everything is in order`,
        `a habit of "supervising" its owner's activities from a nearby perch`,
        `a tendency to "head bump" its owner as a sign of affection`,
        "an inquisitive habit of investigating every new visitor to the home",
        "a habit of playfully swatting at moving shadows on the wall",
        "a habit of chirping or chattering at birds outside the window",
        "a habit of kneading and suckling on soft blankets or clothing",
        "a fondness for climbing to high places and surveying its domain",
        "a habit of sleeping in unusual or amusing positions",
        `a habit of "making biscuits" with its paws when content`,
        "an acrobatic habit of leaping and flipping in mid-air during playtime",
        "a tendency to groom and clean the fur of other pets or companions",
        "a habit of burying its food, even if it's indoors and no other animals are present",
        "a habit of following a strict grooming routine, especially before meals",
        "an aloof habit of observing from a distance before engaging in social interactions",
        "a habit of flicking its tail when excited or intrigued by something",
        `a habit of "talking back" when scolded or told to do something it doesn't want`,
        "a penchant for sitting on books, or any other object that demands attention"  
    ]
    let talent = [
        "scratching",
        "hissing",
        "purring",
        "climbing trees",
        "climbing walls",
        "catching mice",
        "catching fish",
        "catching birds",
        "avoiding you",
        "ignoring you",
        "napping in the most unusual positions",
        "finding the coziest spots to sleep",
        "leaping great distances to catch toys or insects",
        "gracefully walking on narrow ledges or fences",
        "balancing objects on its head while walking",
        "sneaking up on unsuspecting prey or companions",
        `showing affection with head butts or gentle "boops"`,
        "fetching small toys like a dog",
        "performing tricks like sitting or rolling over on command",
        "impressively high jumps to reach elevated places",
        "wiggling into tight spaces to explore or hide",
        "sneaking into rooms or cupboards it's not supposed to enter",
        "stealthily observing from a hidden vantage point",
        "swatting at moving reflections or shadows on the wall",
        `making cute and irresistible "puppy eyes" to get what it wants`,
        "flicking its tail to communicate its mood or intentions",
        "gracefully gliding through the air while descending from heights",
        "finding the warmest and sunniest spots for basking",
        "imitating bird calls or other animal sounds",
        "unraveling or unrolling balls of yarn or threads",
        "opening latched doors or cabinets with its paws",
        "finding the shortest routes to favorite destinations",
        `playfully engaging in "hide and seek" with its owner`,
        `gently patting or "petting" its human companion`,
        "rolling over and exposing its belly for belly rubs",
        "chasing its tail for amusement or to relieve boredom",
        "navigating obstacle courses with agility and ease",
        "sneaking up on its own reflection and getting startled",
        "using its paws to dig and bury items in a pretend cache",
        "standing on hind legs to reach higher objects or treats",
        `using its paw to swipe at toys or objects to "bat" them around`,
        `bringing back "gifts" like leaves, sticks, or small toys for its owner`,
        "expressing a wide range of vocalizations to communicate its needs",
        "displaying a regal or majestic posture when perched up high",
        "using its claws to open packages or tear through paper",
        "playing with water by dipping its paws into a water bowl or faucet",
        "observing and mimicking the movements of birds or insects",
        "adjusting its body to fit perfectly into any cozy container or box",
        "sitting on top of tall objects to oversee the room",
    ]
    let quirks = [
        "always attracts magical butterflies around them",
        "has enchanted eyes that change color based on emotions",
        "has whiskers that tingle in the presence of magic",
        "casts tiny sparks when walking on magical runes",
        "always finds the comfiest spot in any room",
        "can understand and respond to ancient languages",
        "can purr a soothing melody that eases tensions",
        "leaves glowing pawprints on surfaces touched",
        "floats a few inches above the ground when relaxed",
        "creates small gusts of wind with tail flicks",
        "has a mystical bond with celestial bodies and phases",
        "has enchanted fur that sparkles under moonlight",
        "can see through illusions and illusions fail on them",
        "is able to navigate complex magical mazes effortlessly",
        "has a special ability to detect hidden enchanted objects",
        "summons playful spectral companions to dance around",
        "brings good fortune when they sleep on treasure chests",
        "can communicate with spirits of ancient forests",
        "whispers ancient prophecies to their masters in their sleep",
        "can dispel minor enchantments with a curious touch",
        "creates mesmerizing patterns with tail swishes",
        "can see into the ethereal plane and reacts playfully",
        "can temporarily mimic other creatures' calls",
        "carries a mysterious charm that glows when danger approaches",
        "has an enchanted collar that changes color with their mood",
        "has a shadow that takes on a unique, playful shape",
        "attracts magical creatures like pixies and fairies",
        "has the ability to dispel dark spirits with a stare",
        "casts a faint, soothing glow in dark places",
        "possesses the ability to purify tainted water",
        "carries an ancient amulet that grants protection",
        "can reflect moonlight to guide lost travelers",
        "leaves a trail of mystical symbols when walking",
        "draws energy from mystical ley lines in the earth",
        "has the uncanny ability to predict natural disasters",
        "sneezes glitter that brings moments of joy",
        "summons ephemeral flowers to bloom in their presence",
        "flicks their tail to cast sparks that light candles",
        "has a magical aura that protects from dark enchantments",
        "has enchanted ears that detect magical frequencies",
        "creates shimmering illusions during playful antics",
        "leaves behind tiny stars in their fur when they groom",
        "knows secret passages and shortcuts through enchanted forests",
        "can shift between their physical form and a ghostly one",
        "has a shimmering, iridescent coat that changes colors in the sunlight",
        "summons gentle rainbows in their wake during sunny days",
        "has an empathic connection with enchanted forests and plants",
        "creates a soothing resonance that calms magical storms with their purring",
        "can communicate with enchanted creatures through a series of gestures",
        "has dreams that are portals to fantastical realms when they sleep",
        "leaves tiny, glowing pawprints in the snow during winter nights",
        "carries a small satchel of enchanted herbs to aid healing",
        "has the power to dispel dark illusions by simply looking into their eyes",
        "is a master at finding hidden portals between worlds",
        "can share visions of forgotten tales through eye contact",
        "emits a trail of enchanted sparks when in battle",
        "has a mystic bond with the spirits of the elements",
        "reveals hidden messages in ancient runes",
        "can detect and purify cursed objects with a touch",
        "summons playful, ephemeral phantoms during moonlit dances",
        "carries an enchanted locket containing a lost memory",
        "seems to know the desires and wishes of those around them",
        "is blessed with the ability to dispel fear and bring courage to others",
        "summons a protective, glowing aura in times of danger",
        "brings a sense of tranquility to any chaotic environment",
        "has meows that hold the power to mend rifts between beings",
        "possesses a special affinity for locating enchanted artifacts",
        "can move silently and leave no trace of their passage",
        "has the gift of foresight through mystical visions",
        "disperses enchanted dust with a flick of their tail",
        "can read the energies of magical ley lines in the earth",
        "seems to be guided by unseen spirits in their adventures",
        "dispels curses and brings blessings",
        "has a magical satchel that holds unlimited space inside",
        "conjures tiny, glowing orbs to light their way in darkness",
        "they leave behind ethereal footprints in the sand",
        "possesses the ability to calm raging elemental spirits",
        "summon enchanted pawprints that reveal hidden treasure caches",
        "carries an enchanted bell that chimes softly in the presence of danger",
        "summons fleeting visions of forgotten histories in ancient ruins",
        "brings harmony and understanding between magical beings",
        "can decipher the ancient script of long-lost civilizations",
        "knows the secret language of enchanted plants and trees",
        "can mend small magical anomalies with a touch of their nose",
        "leaves behind a trail of enchanted flowers wherever they roam",
        "possesses a magical compass that guides them to mystical places",
    ]
    document.getElementById("Cat").innerHTML =  `You see a ${searchArray(size)} cat with ${searchArray(color)} coloration, ${searchArray(eyes)} and ${searchArray(markings)}. The cat was bred to ${searchArray(bredTo)}, enjoys ${searchArray(favFood)}, typically has ${searchArray(habits)} and is especially talented at ${searchArray(talent)}.${variableEvent([` Rumor has it that this cat ${searchArray(quirks)}.`])}`
};
function randomHostAndHook() {
    //HOST AND PLOT COUPON ---------------------------------------------------------- 

    function returnHost() {
        let hostArray = [
            'A large family of gnomes. They are quite welcoming to guests, and serve dishes upon dishes of rich, steaming food at their meals, often accompanied by the father and the older sons singing.', 'A young tiefling loner who’s willing to share his small, spartan flat. A starving-artist type (well, not quite starving, he does pretty well) who specializes in portraits. He doesn’t bother the guests if they don’t bother him. Keeps his work depicting who he remembers as his mother (an Erinyes) in a safe in his room.', 
            'A soft-spoken Half-orc librarian and his wife, an Elvish herbalist. She isn’t as welcoming as him, but is alright with guests as long as they stay out of the workshop. They both do some of the cooking, so the meals are…unique.', "A Kobold matriarch. While her children have all moved out, their children are dropped off at Grandma’s house quite frequently, and she teaches them all she knows. She also runs a small shrine to Bahamut in the cellar.", "A hot-headed, wealthy heiress and her more rational lady-in-waiting.", "The prince of a corroding noble line, of late taken to dressing in black, composing gloomy poems, and brooding on the battlements of his manor.", "A dwarvish professor with a magnificent walrus mustache, as well as his warm, old-fashioned wife (a dressmaker) and their daughter, who’s visiting for a month or so from her apprenticeship.", "The quiet Mother of a hostel run by the temple of the god of the poor. The tragedy and despair of many of her visitors has rubbed off on her a little. The food is outstanding.", "A not-quite-right young man with ambitions to become a psychologist. Asks far too many personal questions, then goes off on rants about what he thinks shaped his guests to the people they are today. Total quack psychologist, doesn’t know what he’s saying at all.", "An Eladrin who’s spending a few centuries ‘indulging in kindness’. There’s a too-good-to-be-true air to the stay. Breakfast in bed, indoor training arena, a small dungeon built underneath the manor and stocked with inexpensive monsters, a wizard’s study, everything they could possibly want. And the host is always smiling.",
            "A jovial Goliath with an Australian accent who spends most of his time wrestling with various dangerous forms of wildlife. Owns a large merchant company, spends most of his time doing push-ups or lifting weights or wrestling yetis.", "A shriveled, wrinkled, hobbling old Bullywug whose sentences are out of order, and seems to speak in riddles. He wears a slightly threadbare robe and carries a walking stick.", "A stern Halfing dance instructor. She’s quite sprightly, humming waltz tunes as she works. She corrects people’s postures out of force of habit.", "An old Dragonborn mercenary who frequently lapses into a thousand-yard-stare. While not tormented by nightmares, he’s a good-humored guy with quite a few tips on adventuring.", "A water genasi weaver whose skill isn’t quite unmatched, but it’s up there. Naturally, the curtains and carpets of his house are expertly made and quite flamboyant.", "A cackling, bitter old woman. Actually a Green Hag, and her curse is the reason the couple next door (whom she finds insufferable) have been trying for a child for years without success. Serves stew or porridge for every meal from a huge, battered-looking black cauldron.", "A hard-as-nails half-elf rancher. Owns stables upon stables of pure-bred racing horses. Despises city-slickers.", 
            "An old Minotaur noble. He wears huge suits, custom-made for him, and has a staff of Animated Objects who sing, dance, and make dinner.", "A slightly suspicious young woman. Knows far too much about weapons, disappears for long periods of time, and locks the basement door very heavily. She’s an assassin for a local gang of racketeers, and will skip town if she’s found out.", "An Animated Armor that speaks like the Discworld golems (That Is, She Talks Like This) and moves very jerkily. She (well, it’s built for a female humanoid) used to work for an evil artificer before a band of adventurers gave her full free will. Knows a thing or sixty-four about dungeoneering, and considers herself indebted to all adventurers.", "A goblin horse-jockey who loves nothing more than the thrill of a race. Talks a mile a minute, usually boasting about his races, and his house is full of trophies that he polishes devoutly.", "A human card-sharp who won his entire house in a game of Triple Ogres. He’s married to the shrewd but not very welcoming owner of a local tavern. She brings home the latest gossip each night.", "A kobold artificer who’s trying to turn his species’ natural affinity for mechanisms to the good. Owns all sorts of fascinating contraptions, like an automatic pencil-sharpener or a tiny construct that writes down any good ideas he has mid-conversation.", "A merry old smuggler, although he’s put his pirating days behind him aside from the odd chorus of Dead Man’s Chest. His house is adorned with model ships and sketches of exotic shores. Drinks strong home-brewed grog.", 
            "The town doctor. There’s something odd about her of late. She stays up past midnight, tends to skip meals, and always seems to be tearing up some piece of paper and tossing it in the trash. (She’s smitten with the blacksmith’s apprentice, but can’t bring herself to tell him.)", "A rough-and-ready frontier-dwelling female Dwarf, who lives in a quaint cottage. She’s older than most of the village, and knows all the skills of the hinterlands: medicine, hunting, cooking, the lot.", "An old man who can’t seem to look you in the eye. He has one craft, and one craft only: he’s a knife maker. Assassins from every syndicate, court or gang come to him for their daggers. Even the odd Drow comes in the dead of the night to buy an honest-to-Lolth Master Work dagger.", "A scheming duke who tries to see if the party thinks his power-plays would work without hinting too obviously at his massive ambitions.", "A satyr couple who are, well, typical satyrs. They love wine, music, food, the usual revel stuff. Enjoy having guests, of course, but can’t stand ‘sticks in the mud’, ‘killjoys’ or ‘introverts’.", "A female Drow who left the Underdark because she’s claustrophobic. Polite, in a regal sort of way. Her house doesn’t have hallways so much as long, broad halls, with bookcases or coffee tables or armchairs.", 
            "A newer vampire who is having a little bit of an identity crisis. He gets the ‘nocturnal’ part, yes, he gets that, but isn’t the whole ‘domination’ thing a little unethical? and similar conversation. Keeps forgetting that garlic tastes disgusting to him now.", "The best Dwarvish pastry-chef that has ever walked the earth. And she knows it. Quite boastful.", "The keeper of a local shrine to the fire god. He’ll just sit by the fireplace, staring into it for hours on end. Has a very large and overly friendly golden retriever.", "The local ‘crazy cat lady’. An Air Genasi whose hair is always blowing in a gentle breeze. This confuses her cats to no end. She has forty-three of them, and one Mimic who enjoys it’s current lifestyle and has decided to stay shaped like a cat.", "A Tabaxi game-warden. His wolfhound isn’t part wolf, it’s part Displacer Beast, which means people often think he has two dogs. Pleasant but fairly quiet.", "A grizzled old human war veteran. Wears an eyepatch. Has a suit of plate-armor stained with horrific, otherworldly humors in his front hall. Retired after ridding his ancestral estate of some kind of great beast he refuses to describe.", "A gnomish scientist who studies modrons. He’s utterly fascinated by them, and can go on for hours with horrifically dull facts and factoids about them. His house is littered with mounted modrons, dissected modrons, everything modron-related you could imagine.", 
            "A time-wizard who messes with his personal time for kicks. Making himself twelve years old, being in four places at once. He thinks it’s a riot. His house is full of books of temporal magic, or at least it was, twelve minutes before you try to open one of them. Opening one book makes them all vanish to the past. It’s his security system.", "A noble Knight Lord who lives in a small castle and commands an order of chivalrous Knights. A former adventurer.", "A wise Grand Wizard who lives in a magic tower and commands a guild of powerful Wizards. A former adventurer.", "A clever Spymaster who lives in a heavily-secured manor and commands a guild of Spies. A former adventurer.", "A pious High Priest of Light who lives in a modest house attached to a glorious Temple. A former adventurer.", "A homely man with balding white hair, a small beard and eyeglasses. Meets with friends often, talking for hours in the cellar. Are they…acting? Playing some sort of dice-game? It’s not quite clear. Says he hails from the realm of Greyhawk.", 
            "An elvish professor of languages who, despite having fought in several wars, is a honorable, straight-laced, old-fashioned gentleman. He’s writing a rather long book. Apparently it’s about halflings and some kind of Ring?", "A razor-witted Dwarvish comedian who does standup at local taverns, dishing out the side-clutchers and knee-slappers galore. Willing to share a few jokes with the party, too. His ‘why did the cockatrice cross the road?’ always gets ’em.", "A Bugbear leg-breaker for the local mob is trying way too hard to be polite and gracious. His apartment’s nice, of course, but he seems to think that the entire party are some sort of sting operation.", "A former Underdark delver, this calm but dispassionate female Tiefling is married to a far more bubbly and cheery Wood Elf. They bicker regularly about what ‘acceptable decorations’ are, stuffed Troglodyte heads or singing roses.", "A brawny whiskey-maker who meets over a nice, old keg with rogues and grave-robbers every night, it seems. His house is above his tavern.", 
            "An Eladrin woodcarver who has recently taken up trying to enchant things. She’s terribly confident it’ll work out eventually, but for now you’ll have to put up with wooden busts that hurl abuse or curse words and cutlery that work together to spell out rather rude slang.", "A Halfling balloonist with a terrible case of wanderlust. Half of his things haven’t been unpacked yet, half of them are already ready to go.", "A master wizard who crafts Golems. Has some shady deals with dungeon overlords, but is still a good man. Might cut the Evil Overlords off from his business if approached; he’s a man of principles, just needs a push of sorts to get him to stand his ground for them.", "An Aasimar teamster who’s moving into the song business. He’s got quite the voice, and a few songs already written: All Shook Up, 500 Miles, and he’s working on a few more.", 
            "A slightly edgy Tiefling who wants to be both friendly and intimidating. Budding metalhead. His apartment is nearly plastered with band posters and song lyrics.", "A genteel, aristocratic Red Dragon who lives in an enormous castle.", "A curious young man enamored by the sea. Despite his youth, his hair is receding. He never seems to blink, either. His house is full of weird idols and jewelry of ancient civilizations.", "A charlatan ‘wizard’ who’s really just a chemist. Tries to keep her lab hidden. Nearly has a breakdown if she’s confronted about her fraud.", "A Goliath strongman of the local circus. His quarters are rather large, because he’s rather large. They’re right next to the acrobats’ and the lion tamer’s.", 
            "A vain elvish wizard who spends most of her time in front of her magic mirror, and the rest of it complaining about upload schedules and dislike mobs and ad revenue.", "A dwarvish butcher. His wife is an author. Both of his daughters are in preschool. He himself is vegetarian, but does eat fish. Spends his evenings playing pool in the cellar with his friends, or going on walks with his daughters.", "A professional court-jester of the local duke or lord. Not as cheery off the job; gripes to anyone who’ll listen about his poor wages and difficult job. His house is a small cottage within the bailey of the castle.", "A tight-lipped priest who seems to have a shrine to every god in his tiny house. The hallways are crammed with altars and icons, and the whole place smells like incense 24/7.", "An unintentionally insufferable Aasimar ballerina. Lets the guests have the run of the kitchen; she’s too busy practicing for her next performance in the studio downstairs.", "A young bachelor Mountain Dwarf, who’s bitter about getting turned down by the local army or militia. He’s drinking a little more than is good for him.", 
            "A gnomish jeweler, his wife and three children. They have a pretty large townhouse. The husband is a little busy with an important order: a new crown for an anonymous nobleman.", "A halfling priest of various gods of knowledge and nature. He’s a part-time biologist, running a few experiments in the lab in his basement. He’d love to meet a Druid or Ranger with more hands-on experience than himself.", "A Fey who lives in a checkers-themed tower. May kick the guests out if they mention chess or use chess analogies. Most of the food is circular (pie, pancakes, etc.), the tablecloths and bedsheets all have checkered patterns. Writes long letters to a bitter rival.", "A Fey who lives in a chess-themed tower. Gets rather testy if people mention checkers. The staff are construct automatons that only move like particular chess pieces. Complains about a completely irrational rival who sends him storms of nonsense letters every day.", "A professional human trick-shot-archer. She goes on tour with the circus now and then. Her favorite one is nailing a playing card out of someone’s hand from one hundred paces.", 
            "A stout Dwarf who’s a master cook. He puts his heart and soul into every slab of beef, taking hours just to prepare them for barbecuing. Doesn’t spend much time with the guests.", "A human former doctor (she’s still got the beak-mask hung up on the wall in an airtight case, and she warns the party that it’s quite contaminated) who retired after fighting some sort of otherworldly entity beneath her ancestral estate. Recently took up horse-riding.", "A human comedian whose jokes tend to be at his own expense. Unmarried but pretty well-off, for a comedian. He tends to leave in the evening and come back close to midnight after his show.", "An eladrin priest of Tymora. Closer to his fey ancestry than most Eladrin. He’s scheming with a local gang to spring some of their hooligans from prison- after all, the whims of chance are unpredictable, or so he’ll say if the party threatens to inform the authorities. Then he will try and bribe them.", "A calm Oriental-looking man who works as a janitor during the day. His apartment isn’t exactly barren, but it’s certainly unextravagant. He’s teaching a local child the various martial arts he mastered in his time as a Monk.", "A simple Halfling herb-farmer. She has a small plot of land behind her house, where she grows things like spices and vegetables. Patient, because as she says, you can’t hurry peppers. Spends most of her time reading novels.", 
            "A dragonborn tale-weaver. No, not an author, she’s quite firm. A tale-weaver, the kind that don’t get written down so much as passed along. Though she doesn’t exactly have it in writing, she’s very familiar with the wording and themes that make a riveting tale.", "A solemn, gods-fearing Dwarvish carpenter. They call him the Pious Benchmaker, which baffles him. His wife is of somewhat better cheer, but tolerates no nonsense in her house. The furniture is first-rate. You could hit it with a battle-hammer and it wouldn’t dent.", "An Aasimar mattress-maker. Laments his own misfortune: his mattresses are so good, he either sleeps on them and can’t get himself out of bed, or he sleeps on a couch or armchair and doesn’t sleep well. It’s a DC X Strength save to get off his guest-beds (the best ones, for he’s quite hospitable), where X is 10 plus the number of days since the sleeper has been in a normal bed instead of a bedroll or cot.", "A slightly unhinged half-orc scholar. He’s studying all sorts of bizarre phenomena at once, and keeps a wall covered in notes, sketches, and pieces of twine connecting them. The statistical anomalies of coin flips, the way the planet is tilted, all those sorts of things. Frequently becomes so engrossed in his studies he forgets to eat.", 
            "A ratcatcher who is quite ferocious in his task. He’s got mousetraps all over the place, and hundreds of rat skulls nailed to his wall. Grim, adamant, and talks at length about what utter vermin rodents are.", "A friendly, jocular doppelganger illusionist and it’s tame mimic pets. The house appears to have a large staff of servants and much finely-made furniture…", "A gnomish Expert Clown. He doesn’t just study mere tossing and tumbling, mind you. He studies the psychology of clowning. What makes a pie to the face so funny? Or what is the thrill-inducing factor of juggling eggs? He can tell you. He can tell you for several hours.", "A human stone-carver and his teenage son. The son’s a little worried about his father, as the latter seems to be losing interest in the craft. Their house is full of half-finished works.", "A high elf mask-maker. It’s a delicate craft, she’ll tell you. Fey come to call every so often, picking up their masks but also staying to chat with her a bit. So do some actors. And one or two assassins.", 
            "A scruffy human gravedigger. He isn’t exactly a philosopher, but tends to make incisive remarks about mortality and time. Doesn’t like elves, because they don’t give him business.", "An old man with a bald head and gleaming eyes. If asked, he only gives his profession as ‘chemist’, and spends a lot of time in his lab. He’s less harmless than he seems; he’s the master poison-brewer for a local assassin’s guild. If he’s found out, he calls in his allies on whoever discovered his true identity.", "A young couple of a Tiefling and an Aasimar. Their ancestors didn’t like the marriage much, and it couldn’t exactly get officiated by a priest (but the local marriage law did allow for a Fey to do the job). They’re getting along fine.", "A pious couple who are gravely concerned about their young daughter. She claims to see ‘shadowy people’ in the cellar, and apparently brought the family dog back to life. They’re both nearly nervous wrecks, and priests of every Good god have been coming and going all week to try and exorcise the child.", "A white-haired old man and his shrill wife, both the village healers, although the Mr. recently got fired by the prince whose father he used to work for.", "A playwright who is outraged at his rivals trying to spread the rumor that his work was ghostwritten for him. Insists on reading off sonnets and scenes to the guests to prove that he’s genuine.", "A grizzled, scarred town guard. He’s only in during the day, usually asleep, and spends the nights walking the streets and smoking very particular cheap cigars. Moody but not hostile.", 
            "A ‘professional quest-giver’ who pampers the heroes with everything he can. He’s in kahoots with a local dungeon-lord, and gets a share of the armor, weapons and loot of the heroes killed in the dungeon he directs them towards. He’ll take to the hills if he’s found out.", "A young priestess of a god of the wilds. Her house is on the very outskirts of town, and has a terrible case of rats, which she doesn’t mind as long as they don’t bother the guests. Rats that do bother the guests get speared. She doesn’t take nonsense, but has some sense of humor.", "A Kenku minstrel who rents a room above the tavern he performs in. It’s covered in posters from his ‘glory-days’- although a keen eye (DC 15 Investigation) will note that they’re actually other bards’ posters, with the minstrel’s name altered into them.", "An apprentice baker and his wife, a schoolteacher. Their house was a cheap deal, and is a little run-down but still serviceable. Gets a little drafty, though.", "A Kobold who claims to be an architect and interior designer. Actually, she’s a dungeon planner who designs catacombs, lairs and castles galore. Highly sought-after by evil overlords, and frantically tries to direct them away while the guests are there. If she’s found out, she’ll flee to the safety of one of her closer creations.", "A Swordsmith who has been at it for years. He keeps a display case of splintered, shattered or blunted swords recovered from various dungeons and battlefields, each with the tale of a fallen hero attached to it.", "A halfling gourmand with an affinity for candies. He’s a longstanding foe of witches who use his creations, or mockeries thereof, to lure children into their cook-pots.", "A Dwarvish family of four- father, mother, son, daughter -who are rather new in town. Hospitable, but the house is still full of moving crates. The father is a lumberjack, the mother is a stay-at-home parent.", "The High Priest of a local shrine of the god of travelers and messengers. He’s an unmatched source of information, references and road maps, and will greet anybody with a smile so long as they return the favor.", "An old Elvish couple. The husband spends most of his time golfing or whittling, the wife is busy giving advice to her newly-married daughter. They live in a nice old house, although there’s a ghost in the attic. Don’t worry, it’s very polite during the day, and it can’t leave the attic."
        ]
        return searchArray(hostArray)
    };

    function findPlot() {
        let hostPlotArray = [
            [ //ZERO THE PERSON'S ROLE
                'a barkeep.', 'a warrior', 'a merchant', 'an agent', 'a criminal', 'a performer', 'a noble', 'a bureaucrat', 'a member of the clergy', 'an artist', 'a craftsman', 'a magic user'
            ],
            [ //ONE THEIR LOCATION
                'in an unknown location - they are hard to pin down, always on the move', `in a ${searchArray(['nearby', 'far away']) + " " + searchArray(['village', 'city', 'castle', 'stronghold'])}`, 'that passes through here occasionally, might want to ask around', "that frequents the area, keep and eye out and you're bound to bump into them", 'that lives right nearby', 'that lives just a few villages away', `quite a distance from here in a remote location, you'll need your map marked`, "who is basically unreachable. Let their people know, they'll find you"
            ],
            [ //TWO THEIR FEELINGS TOWARDS YOU
                "I hate [PC],and I wont give [[PC]/the party] the time of day, unless they pay up front (5gp/minute)", "Why would I help [PC], unless of course [PC] is offering something in return?", "I am willing to help [PC], but they'd need to persuade me", "Will do anything [PC] asks, no explanations or renumerations needed", "I hate [PC's] guts", "I never really liked [PC]", "We did try to kill each other that one time…", "I do not remember [PC] in the slightest", "I tolerate [PC], they'll get no special treatment", "I could lend a hand maybe I guess, but what's their name again?", "We are amicable but not necessarily amenable", "Sure, for the right (high) price in gold", "Yes, but first they'd need to help me do a thing that’s… a little dark", "Yes, but they'd need to help me get this thing first", "Yes, but they'd need to help me resolve a personal issue first", "Yes, but they'd need to cover some expenses", "Yes, but they'd have to join my guild", "Wish I could help, but it’s impossible now because magical restrictions", "Wish I could help, but it’s impossible now because social issues", "Yes, but they'd need to help me resolve a personal issue after", "I would do anything for [PC], but I won’t do that", "Any time, but they'd owe me one", "I would do anything for [PC]"
            ],
            [ //THREE RELATIONSHIP
                'are your rival', 'are an acquantance', 'are an old friend', 'are your old teacher', 'are a fellow student', 'are a family friend', 'are a childhood friend', 'are a family member', 'are an admirer of your work', 'are your secret admirer (stalker?)', 'are a work associate of yours'
            ],
            [ //FOUR ASSISTANCE
                "has done something similar long ago", "has done it once under duress", "has experience getting the right things for it", "has practiced this before, and can totally help", "is very smart, and can puzzle out stuff like this all the time", "knows the right people to ask about it", "knows where to find out more about it", "knows some ancient lore about it", "has some related magic for it", "has  authority to get help for it"
            ],
            [ //FIVE POSSIBLE TWIST
                'NPC really doesn’t like someone else in the party', 'NPC really likes someone in party too much', 'NPC Might tell your enemies', 'NPC Is actually not helpful', 'An adversary learns about you and your location and acts upon it', 'A local mob threatens the NPC to not help [PC]/ Party', "Another NPC you know needs your help, urgently", "You are mistaken for someone else, who's in big trouble", "The NPC severly insults and taunts one of your party members.", "The NPC gets a crush on [PC] or on one of the party"
            ],
        ]

        function findAssistance() {
            return "If you tell your host about a current challenge you'll learn about someone who " + searchArray(hostPlotArray[4]) + "."
        };

        function findRoleAndLocation() {
            return " They are currently " + searchArray(hostPlotArray[0]) + " " + searchArray(hostPlotArray[1]) +"."
        };

        function findRelationship() {
            return " Rumor has it that they " + searchArray(hostPlotArray[3]) + "."
        };

        function findFeelings() {
            return ` Also, you'll probably be hearing something like ` + '"' + searchArray(hostPlotArray[2]) + '" if you end up trying to contact them for help.'
        };

        function findSetback() {
            return searchArray(hostPlotArray[5]) + '.'
        }

        let setbacknumber = Math.floor(Math.random() * 100);
        if (setbacknumber > 85) {
            return findAssistance() + findRoleAndLocation() + findRelationship() + findFeelings() + ' Unfortunately, ' + findSetback(); +"."
        } else {
            return findAssistance() + findRoleAndLocation() + findRelationship() + findFeelings() 
        }
    };

    document.getElementById("Host").innerHTML = returnHost() + " " + findPlot();
    //console.log(returnHost() + findPlot())    
};
function npcBuilder() {
    function findRace() {
        var races = {
            "Common": { 'human': undefined, },
            'Uncommon': { 'dwarf': undefined, 'high-elf': undefined, 'wood-elf': undefined, 'gnome': undefined, 'half-elf': undefined, 'halfling': undefined, },
            'Rare': { 'dragonborn': undefined, 'tiefling': undefined, 'genasi': undefined, 'aasimar': undefined, 'half-orc': undefined, 'tabaxi': undefined, 'drow': undefined, },
            "Very Rare": { 'kalashtar': undefined, 'shifter': undefined, 'warforged': undefined, 'simic hybrid': undefined, 'changeling': undefined, 'goliath': undefined, 'gith': undefined, 'yuan-ti': undefined, 'tortle': undefined, 'aarakocra': undefined, 'orc': undefined, },
            'Ultimate Rare': { 'bugbear': undefined, 'firbolg': undefined, 'goblin': undefined, 'hobgoblin': undefined, 'kenku': undefined, 'kobold': undefined, 'triton': undefined, 'lizardfolk': undefined, 'vedalken': undefined, 'verdan': undefined, 'locathah': undefined, 'grung': undefined, 'centaur': undefined, 'loxodon': undefined, 'minotaur': undefined, },
        };
        let chance = rollDice(100)
        if (chance > 98) {
            return searchArray(Object.keys(races["Ultimate Rare"]));
        } else if (chance > 95) {
            return searchArray(Object.keys(races["Very Rare"]));
        } else if (chance > 80) {
            return searchArray(Object.keys(races["Rare"]));
        } else if (chance > 50) {
            return searchArray(Object.keys(races["Uncommon"]));
        } else {
            return searchArray(Object.keys(races["Common"]));
        }
        //document.getElementById("Race").innerHTML = characterRace
    };
    let gender = [
        `${searchArray([`A young ${findRace()} ${searchArray(['boy', 'girl', 'man', 'woman'])}`, `An old ${findRace()} ${searchArray(['man', 'woman'])}`, `${searchArray([`A young ${searchArray(['boy', 'girl', 'man', 'woman'])}`, `An old ${searchArray(['man', 'woman'])}`])}`, `${searchArray([`A young ${findRace()}`, `An old ${findRace()}`])}` ])}`
    ]
    
    let uniqueFeature = []

    return `${searchArray(gender)} walks up to you and`
};
function wisdom() {
    let wisdom = [
        `You will not be punished for your anger; you will be punished by your anger.`, `In the end, it’s not the years in your life that count. It’s the life in your years.`, `Truth is truth. How you deal with it is up to you.`, `Hero’s are no braver than an ordinary man, but he is brave five minutes longer.`, `Add life to your days, not days to your life. Life is either a daring adventure or nothing. It is not death most people are afraid of. It is getting to the end of life, only to realize, that you never truly lived. Some beautiful paths cannot be discovered without getting lost.`, `Yesterday is history, tomorrow is a mystery, today is a gift of God, which is why we call it the present.`, `We don't get to decide what weighs on our souls, but it is our responsibility nonetheless`, 
        `"We don't make peace with our friends" in the context of "making peace with your enemies is of course difficult and unpleasant, that's why they're your enemies"`, `Speaker (someone the party is going to for answers) pouring tea into a full cup. Tea goes everywhere.`, `PC asks why they are pouring tea into the full cup.`, `Like the full cup you come to me full of yourself. You must be empty if you are to be filled with wisdom.`, `When you learn to balance a tack hammer on your head, you will learn to head off your enemies with a balanced attack`, `“There is more to life than what you're living. You take a chance and face the wind. An open road and a road that's hidden. A brand new life around the bend. “`, `“You take the good, you take the bad, you take them both and there you have The facts of life.”`, `“Now, the world don’t move to the beat of just one drum What might be right for you, may not be right for some.”`, `Inaction in the face of evil can be as damning as the act of evil itself.`, `Choosing to take no action is still a choice. Taking no action is still an action.`, 
        `Is there really honor and glory in war? Look in the eyes of the widows and orphans, listen to cries of the wounded and the silence of the fallen, and stand within the worn-torn battlefields. You'll find your answer.`, `When deciding between the devil you know and the devil you do not know, remember that, in the end, they are both still devils.`, `Four strands of rope, kept separately, can be snapped with ease. Four strands of rope, twined together, are stronger than the sum of their parts. Strength lies not in numbers, but in unity, in cooperation.`, `There is nothing wrong with being proud of yourself, but always remember that too much pride can be blinding.`, `Always keep an eye on your pawns, even the ones you've already sacrificed. Off the board doesn't necessarily mean out of the game.`, `Even a mouse can be ferocious when cornered.`, `The past is written in stone, the present in clay, and the future in sand.`, `You are only bound to your destiny if you believe yourself bound to it. Only when you realize that it is you who controls your destiny can you well and truly be free.`, `Better a swift death at the blades of tyrants, than a slow one under their heel.`, 
        `If you believe you know everything, then you truly know nothing at all.`, `Steel rusts, flesh weakens, but will is unbreakable.`, `If you think you're prepared for any eventuality, I can promise you'll be caught by surprise quite frequently.`, `Before binding yourself to someone through oaths of honor and loyalty, be sure to ask yourself if they even deserve such honor or loyalty.`, `There is no honor or glory in war, just victory or defeat.`, `Until beasts have scribes of their own, tales of the hunt shall always venerate the hunter.`, `The first step towards true wisdom is acknowledging that everything you know pales in comparison to everything you do not. The second is accepting that, no matter how long you study, you can never know everything. The third step is to keep learning regardless.`, `What is the path to true enlightenment? I'm afraid I cannot tell you. Everyone must forge their own path.`, `What is the meaning of life? The meaning of life is to live.`, `There is no shame in accepting charity when it is offered, or in asking for help when it is needed.`, `To er is human, to forgive is divine... but never pay full price for late pizza.`, 
        `Speaker (someone the party is going to for answers) pouring tea into a full cup. Tea goes everywhere.`, `PC asks why they are pouring tea into the full cup.`, `Like the full cup you come to me full of yourself. You must be empty if you are to be filled with wisdom.`, `"The same hammer that breaks glass forges steel"`, `"Leave tomorrow's problems to tomorrow's you"`, `"Dont try to have sex with dragons"`, `"Sometimes you have to walk in the dark to appreciate the light"`, `"Nobody's perfect. You just have to live and work it again and again until you get it right"`, `"If the world ended tomorrow, would you rest in peace knowing your actions today?`, `“There is more to life than what you're living. You take a chance and face the wind. An open road and a road that's hidden. A brand new life around the bend. “`, `“You take the good, you take the bad, you take them both and there you have The facts of life.”`, `“Now, the world don’t move to the beat of just one drum What might be right for you, may not be right for some.”`, 
        `There is a fine line between being brave and being stupid. Make sure you are on the correct side of this line.`, `You must wait for the silt to settle, before the water can be clear.`, `Only a fool leaves this world with a bag full of healing potions.`, `A road of gold is both loud and slippery.`, `Assassin/LE: "The world is cruel, unkind, and deceitful. A wise man will use that against his enemy."`, `Hermit: "The man who thinks himself wise is foolish. The man who thinks himself foolish is wise. The man who thinks too little is dead. The man who thinks too much loses everything he fights for."`, `A bowl is most useful when it is empty.`, `Live. Laugh. Love.`, `Calm waters run deep`, `You can bring a horse to water, but you can not make it drink`, `A copper saved is a copper earned`, `Liquor before beer and you are in the clear, Beer before liquor and you are never sicker....I think.`, 
        `Nothing is written in stone, but a dirt path. If you roll your wagon the same way for too long, it will become the only path you can take`, `Sleep is good.`, `People in glass houses should rarely throw bears.`, `Kindness rewards kindness just as anger punishes anger.`, `Life is a journey and death is the destination. Where you go and what you do with your journey, how you enjoy it, is up to you.`, `When in danger, it can be a good idea to pray, but never forget to run, too.`, `Patience brews the best tea.`, `We should strive to make things better than ourselves.`, `Let me tell you what I wish I’d known when I was young and dreamed of glory: You have no control who lives, who dies, who tells your story.`, 
        `Life is story: it’s best to have one worth reading.`, `Every person is a thread in the tapestry of mortal history.`, `I may die but my requiem plays on, the consequences of my life echoing into the void of history.`, `There can be no friendship without confidence, and no confidence without integrity.`, `Integrity without knowledge is weak and useless, and knowledge without integrity is dangerous and dreadful.`, `There is no wisdom in useless and hopeless sorrow; but there is something in it so like virtue, that he who is wholly without it cannot be loved.`, `It is more from carelessness about truth than from intentional lying, that there is so much falsehood in the world.`, `Every man naturally persuades himself that he can keep his resolutions, nor is he convinced of his imbecility but by length of time and frequency of experiment.`, `It is always observable that silence propagates itself, and that the longer talk has been suspended, the more difficult it is to find any thing to say.`, `Beware the fury of the patient man.`, `We first make our habits, and then our habits make us.`, `Happiness is the perpetual possession of the well decieved.`, `There can only be one wisdom. For if it were possible that there be several wisdoms, then these would have to be from one. Namely, unity is prior to all plurality. All we know of the truth is that the absolute truth, such as it is, is beyond our reach.`, `We don't get to decide what weighs on our souls, but it is our responsibility nonetheless`, `"When there are no foes to slay, there might be a cake to cut."`, `"Sometimes the simple solution IS the solution"`, `"Sonny, I have forgotten more things than you have ever bothered to learn"`, `Remember to add the pasta when the water is boiling. And don't forget to salt it too.`, `Barbarian and a wizard get into a fight about who’s smarter.`, `Barbarian says “you thing you’re so smart because you read your fancy books, but your so dumb you don’t even realize you just stepped in dog shit”`, `Wizard “what when? The dm didn’t tell me”`, `Dm “you’d have to check to know for sure”`, `The wizard raises his foot to check the bottom and the barbarian shoves him over.`, `“See, told you I was smarter”`, `Take the long road, strangers. The long road will set you free`, `Always waver, but never bend`, `Even monkeys fall from tree`, `Often it is the journey that is important not the destination.`,
        `The truth remains the truth, an untruth remains an untruth, no matter how many people believe otherwise.`, `Oh you don't have to be wise to play a wise old mountain man. You only have to be cryptic.`, `Do not disturb your foe while he is making a mistake.`, `Bravery is not to feel no fear, bravery is to be afraid, but still act despite it.`, `When the storm winds blow fiercely the tree that bends breaks`, `When the storm winds blow fiercely the tree that doesn’t bend breaks`, `If you don't take time to enjoy life, what was the point?`, `If you try, you might fail. If you do not try, you have already failed.`, `One, who does not question, is easily lead astray.`, `Good intentions may lead one down the wrong path. However, without good intentions one is already on the wrong path.`, `Stop dreading failure. Learn from it.`, `The truth doesn't care what anyone believes.`, `Titles and praise do not make one great. The path to greatness lies in what you do.`, `When life gives you lemons, make lemonade`, `You see.. marriage is like a rattlesnake. You can have the head of a rattlesnake with its sharp teeth and curious tongue, and the tail of a rattlesnake with its mesmerizing rattle. But only together do you have a whole rattlesnake. Apart, you're just a hollow object and a screaming mess.`, `If you take that cart... you get there.`, `A wise man is but a normal person who is very vocal about the clear lack of common sense nowadays.`, `“Prodigious size alone does not dissuade the sharpened blade”`, `“A strict regimen is paramount, if one is to master the brutal arithmetic of combat”`, `“Every creature has a weakness. The wise hero trains for what they will face.`, `“A little hope, however desperate, is never without worth.”`, `“Failure tests the the mettle of heart, brain, and body.`, `You will endure loss, and learn from it.”`, 
        `“Ignorance of your enemy and of yourself will invariably lead to defeat”`, `“Overconfidence is a slow and insidious killer.”`, `The Zhuangzi is a great source of sayings that sound mysterious and wise.`, `“Now gaining is timely, but losing is what follows. Take comfort in timeliness, and settle into what follows, then grief will not be able to disturb you”`, `“The cosmos burdens me with physical form, toils me through life, eases me through old age, and rests me in death. What makes my life good is what makes my dying good also”`, `“A large tree must have had little worth to grow so vast”`, `"It is important to draw wisdom from many different places, or else it becomes rigid and stale."`, `"Are you so busy fighting that you do not realize your own ship has set sail?"`, `"In the darkest times, hope is something you give yourself. It is the meaning of inner strength"`, `"Destiny is a funny thing. You never know how things are going to work out."`, `"This tea is something more than hot leaf juice!"`, 
        `What is the most important step a man can take? Always the next one.`, `"Get a beach house. It gives you somewhere to go."`, `"Rather than to aim to be something, just be."`, `"Remember that this moment will also pass. Good or bad, everything is temporary"`, `Those who don't love never live. Those who do love never die.`, `Use soap every now and then.`, `Death is inevitable, but Life is a journey to death so make it count`, `Even you're in the right tunnel, the ooze will still eat you if you just sit there.`, `You only get one chance to screw things up forever, so don't be afraid to take it.`, `Saying something that sounds wise and actually being wise are two entirely different matters. Make sure you aim to be wise, unlike me.`, `Knowing your right from your left is irrelevant when the enemy stands straight in front of you.`, `Being able to do the right thing doesn't matter so much as knowing to not to the wrong thing.`, `Regularly wash behind your ears. It will help you to hear the world a little differently.`, `You are what you are. Once you know what you are, what others are doesn’t matter.`, 
        `"It's an old hat, just a different coat"`, `[HimurasanX] "Funny thing about strength, the stronger you are the less you have to fight."`, `"First over the wall is an idiot, the second, is an idiot. The third, seeing what happened to the first two, is who you need watch out for."`, `You already have what you're looking for.`, `The more you run from the past, the quicker you’ll be burning through your future.`, `Life isn’t set in stone, but it is set in a muddy road. The more you drag your cart through the same rut, the harder it’s gonna be to get it out.`, `“A dead thing can go with the stream, but only a living thing can go against it.”`, `"What a person intends means all to them, and little to others. What a person says means little to them, and all to others."`, `"To seek wisdom from a single being is, in itself, an act of the unwise. Open your mind, and you will find yourself garnering more wisdom from the journey home then I may ever teach you."`, 
        `"All things in moderation. Including, of course, moderation."`, `"In your profession, you must not fear death. Fear leads to inhibitions, lack of action, and hesitation - all fully capable of causing your death, and others alongside it, when action is needed. You will fear it, it is natural to do so. Yet you must ignore that instinct, and act without hesitation."`, `"The early bird may get the worm, but it is the second mouse that gets the cheese."`, `"Life very rarely molds itself well to universal wisdom. Take all advice with this in mind. Including this advice, of course."`, `In response to the party failing in a major way: “You tried to (insert major defeat). You mostly failed. This is life. The longer you live, the more you fail. Failure is the mark of a life well lived. In turn, the only way to live without failure is to be of no use to anyone. Trust me, I've practiced”`, `Only two kinds of people claim to feel no fear: liars and madmen.`, `"We can forget happy things. We can probably forget sad things too. People have the power to forget."`, `"An upper jaw filled with joy, and a lower jaw filled with sorrow. Life has a habit of grinding these two together. It is our job to relish it."`, `Fight like you are dying, live like you are fighting`, 
        `"The question is not whether you will love, hurt, dream, and die. It is who you will love, why you will hurt, when you will dream, and how you will die." -Oathbringer by Brandon Sanderson`, `I would love to see where this goes, but just like you I'm not the wisest person you'll come across`, `Don’t wait around for someone to make you happy, if you want to be happy, then be happy.`, `You will be forgotten in the shade of your achievements.`, `There's no situation so bad, that you can't make it worse. - Chris Hadfield (maybe)`, `Mastery of the self is the only mastery that matters.`, `There is no civility, only politics.(Palpatine)`, `A war without civility is a massacre. (Treys Renata)`, `One who is never without one’s weapon will always find oneself using it.`, `A little ritual goes a long way.`, `Mistakes should be rested on the heart not the soul.`, `All is Human that suffers from the human condition.`, `To live is to devour others.`, `Everything is Food for something else.`, `Not everything needs to be Okay at the same time.`, `Love is a rich man's gold.`, 
        `Live for the little things. Die for the big things.`, `To do for someone, something that they can do for themselves, is a form of theft.`, `Nature is where birds fly about uncooked.`, `Among the most courageous must be counted the first to eat an oyster.`, `It is not through violence but compassion that the virtue of a civilization is proved.`, `When one categorizes people according to their great love before all else, all other categories quickly dissolve.`, `Life is a fatal sexually transmitted disease.`, `Almost all absurdity of conduct arises from the imitation of those whom we cannot resemble.`, `No man is much pleased with a companion, who does not increase, in some respect, his fondness for himself.`, `Men more frequently require to be reminded than informed.`, `Avarice is generally the last passion of those lives of which the first part has been squandered in pleasure, and the second devoted to ambition.`, `Every man is rich or poor according to the proportion between his desires and his enjoyments; any enlargement of wishes is therefore equally destructive to happiness with the diminution of possession, and he that teaches another to long for what he never shall obtain is no less an enemy to his quiet than if he had robbed him of part of his patrimony.`, 
        `He is no wise man that will quit a certainty for an uncertainty.`, `Hope is necessary in every condition. The miseries of poverty, of sickness, or captivity, would, without this comfort, be insupportable; nor does it appear that the happiest lot of terrestrial existence can set us above the want of this general blessing; or that life, when the gifts of nature and of fortune are accumulated upon it, would not still be wretched, were it not elevated and delighted by the expectation of some new possession, of some enjoyment yet behind, by which the wish shall at last be satisfied, and the heart filled up to its utmost extent.`, `Pleasure is very seldom found where it is sought. Our brightest blazes of gladness are commonly kindled by unexpected sparks. The flowers which scatter their odours from time to time in the paths of life, grow up without culture from seeds scattered by chance. Nothing is more hopeless than a scheme of merriment.`, `Merriment is always the effect of a sudden impression. The jest which is expected is already destroyed.`, `It is seldom that we find either men or places such as we expect them. ... Yet it is necessary to hope, though hope should always be deluded, for hope itself is happiness, and its frustrations, however frequent, are yet less dreadful than its extinction.`, `Nothing will ever be attempted, if all possible objections must be first overcome.`, `Example is always more efficacious than precept.`, 
        `If one wishes to avoid all criticism, one must simply say nothing, do nothing, and be nothing.`, `"You're the one who has to die when its time for you to die, so live your life the way you want to."`, `"Holding a grudge is drinking poison and praying for your enemy to die. Of course, I knew a paladin whose prayers set their sword afire and raised the dead...."`, `"The gods ask us to be faithful to them at all times because of how hard it is to believe in yourself in the hard times. Faith in miracles is good practice for facing down dragons."`, `mortal beings are the instrument by which the universe cares.” I just like the quote`, `Violence is the last refuge of the incompetent. Those whom the gods would destroy first they make proud!`, `I'm not a wise man. I'm not even a wise guy. But I am wise enough to know I can be wiser still.`, `Forgiveness is difficult. The pain of hatred, even more so.`, `There is nothing to be gained from following the well-worn path. Though blazing your own trail comes with risks, it also comes with rewards.`, `One is not a fool for believing a lie, nor for knowing the truth; only for believing one knows.`, `Bravery is not the absence of fear. Bravery is being scared and saddling up anyway.`, `When in doubt, go slow.`, `When in doubt, go slow. Unless there's an owlbear chasing you, in which case you run fast.`, `Let it be.`, `A fool would become wise if he would persist in his foolishness.`, `For there is no form or substance that does not have its roots in the TOWER, which is under assault from the EGO, that terrible enemy called I.`,
    ]

    let output =  npcBuilder() + ' says, "' + searchArray(wisdom)+`"`
    document.getElementById("Wisdom").innerHTML = output
};
function omens() {
    let omens = [
        `Beware of the blinding red light. If you see this light, you must flee. It will only bring you death!`, `You will find the answer to a long, mysterious riddle in your family bloodline buried between two oak trees, west of the village you grew up in.`, `A path of death lies in your wake.`, `Greed is a poor man’s compass, and I see gold and riches in your future.`, `A single wolf is slaughtered by many enemies that surround it. Let this be a warning sign of danger that is preventable by the pack.`, `The truth will come from a child’s toy. The lie will come from a weapon.`, `You must drink of the poison well and eat of the spoiled pantry.`, `Follow the flight of birds, never in winter, always returning.`, `A song contains a wish. Only the name will answer.`, `The mother has disguised herself. Her babe is lost and will not return. She will nurse no other.`, `The gears turn long after the machine has been broken. He who built it cannot mend it. He who holds it cannot carry it. He who finds it cannot speak it.`, `Gaze through the cracked window, and only then will you see clearly.`, `Beware the men with gills. Speak not to the sea or the southern wind.`, `Beware the snake’s venom, not its bite.`, `Travel five days with the silver star at your heels, then cross the raging river. There you will come to realize your true self.`, `The light will be in the shadowest darkness.`, `Not all the frogs are in the pond, beware of them.`, `One for the fire, two for the clouds, and three for the knights.`, `Don’t trust the song of the birds.`, `Cloak in the water. The man is crying. Let the leaf falls and everything will be fine.`, `For one wish to make, it’ll be more wish to crumble.`, `In the high plain there’s a dark moon. Don’t follow the light.`, `When the dawn will come at the birthday of the mother, rats and snakes will devour all hopes.`, `Near the montains, there is a grey falcon. Look at the eyes, and you’ll die. Look at the tail, and you’ll be rich.`,
        `Don’t move when the night song come, or you’ll gain something you don’t want, and lost something you wanted to keep.`, `Today was possibly the most important day of your life! Congrat.. oh… you missed it… tsk tsk tsk… What a shame… A do-over, then! Tomorrow you will wake up and it will be today. Make sure you return or that decree will stay. k, Bye!`, `Do not trust your thoughts. They will hinder your victory.`,
        `A figment in blue will cross your path tomorrow. You will know it when you see the sign. You must turn around 4 times and speak the following words: And through the drifts the snowy clifts Did send a dismal sheen: Nor shapes of men nor beasts we ken The ice was all between.`, `If you believe in telekinesis, raise my hand. The fortune teller then proceeds to raise their hand.`, `When you are done, the spirit haunting will pass over you.`, `A dragon will give you a jewel. Beware the generous miser.`, `The path less traveled is paved in gold.`, `Find the woman who gives birds their song.`, `Beware, young mouse, for the lion is thorned.`, `${searchArray(['Do', 'do not'])} cross the Mountain!`, `${rollDice(10)+2} Stars Mark the Path!`, `The Moon Shines Brightest to Those in Her Favor.`, `Speak Not The Name Unspoken; They Listen, Always.`, `Beware, for the Great Gyre is Nigh; The Slouching Beast Will Soon Arrive!`,
        `Swords Shall Pierce Thine Heart; Pin Thy Love Lest It Be Lost.`, `Three Crones Shall Visit Thee and Thier Lights Shall Reveal the Truth of What Thou Doth Seek!`, `Keep a Candle Burning; Lest The Dark Take Even Your Fears Away.`, `Build Not Houses of White Stone.`, `Three Coins Must Ye Pay; Three Prices Dear, Secrets Thrice Revealed, ‘ere The Light of Day.`, `Gold, Silver, Copper; Never in the Opposite Order!`, `Spill Forth a Dram for the Lost; Make Merry in the Name of Those Who Pay the Highest Price!`, `You Must Seek the Leaf that Grows Not On Any Tree!`, `Jump the Broom; Dance above the Blades!`, `Sphinx of Black Quartz, Judge Thy Vow.`, `Seek the Egg of Stone; Face the Dragon!`, `Your nights will grow colder still, to match the heat of growing fires.`, `Trust the twin with no siblings, but abhor the lone child.`, `The face of the one you seek is thus- a busker at dawn; a composer at noon; a patron at dusk; a maestro under the stars.`, `Your money, here, have it back. The fortune you’ve asked me to read, never shall I speak of it in this life or any hereafter.`, `A wilting lineage droops to shadowy lows. What the rotten fruit begets chokes out the tree of its birth.`,
        `Beware! Blessings from above may actually be curses from below!`, `A helping hand will come from an unlikely place. Trust it at your own peril.`, `When the leaves fall from the trees so too shall the stars fall from the sky.`, `The wisest men envy the grave.`, `The poison of the moon lies only once.`, `There be dragons in ye head. Make sure to feed them.`, `The treasure you are looking for is in the fruit.`, `Poorly-dresed skanks like you will die alone. Naked, and alone. (Works best in an arctic setting, or not.)`, `Never bring upon yourself the wrath of the chicken. You may think this a metaphor, but it is not. Their beaks are sharp like my toes.`, `Your hands will taste of orange in the near future.`, `That which you hold most dear will turn against you and lead you to ruin`, `Your actions have had unintended and unforeseeable consequences, and have placed into action the final piece of that which now approaches you. You are the harbinger of your own death`, `The thoughts you have had but not put into action are leading you down a path to your own undoing`, `The fall of slow rain upon the barren field will lead you to the house which shelters your destiny`, `Steel your heart for darkness ahead. Your betrayal has already happened though you do not yet know it.`, `Seek ye the good behind the bad and beware the bad behind the good.`, `Never lick a horse in the mouth, they bite.`,
        `A Fall is Coming; Winter Just Round the Bend; Enjoy Spring; Summer Shall Bring An End!`, `Let Not Cold Enter Your Heart, For Then Only Love Can Drive It Out!`, `The black sky will shield you from your enemies. Travel by night.`, `The rope with which you climb may also hang you if you are not careful.`, `You will be an old man/woman by the time your quest is complete.`, `Fools will take great heed of your words. Use this to your advantage.`, `A shrewd and very attractive fortune teller has put a curse on you. I will remove it for an additional sum.`, `Trust not the travelers numbering odd.`, `Take something old, give something new, doubt something red, trust something blue.`, `Left at the stream, at the face look right, crawl through the dark, and you will find the light!`, `Salt thy wounds, relish the sting, sweet is the knave, and bold is the king.`, `Thrice will call the raven, heed its warn lest the fourth cry your dirge.`,
        `Between silver and gold, choose evil’s bane. Between fire and chill, the lady’s kiss.`, `The shadow of the dragon is an omen, but coming of the wolf is the sign.`, `Begrudge not the thieving monkey, lest you take its place in the tiger’s jaws.`, `Lay not your head in the barn animals’ bed, for the headsman soon calls.`, `A copper for the maid, a silver to the beggar, and a gold for a lonely tune, may the vault of riches open to you.`, `Someone you remember, someone you forget, someone with a favor, another with a threat.`, `Poor fortune for ye, unless you confess your guilt to the willow tree.`, `Your luck is a shame until you trade with your mate who has one of the same.`, `A fortune most cold if you do as you’re told.`, `Torch and candle, wax and wick, in the hall of fire, move right quick!`, `Look for the priestess, she will bring salvation.`, `An ancient empire will rise from the waves along with ancient secrets.`, `Only when the lovers are reunited can the curse be broken.`, `As the hermit emerges from hiding, darkness shall soon emerge as well.`, `Watch for a nobleman in red, for he is a devil in disguise.`,
    ]
    let nightmares = []
    
    let freakArray = [
        'their eyes turn black with red swirls', 'they move in jittery, unsettling, motions', 'they speak with multiple dissonant voices', 'you hear many whispers as they speak', 'you get a chill as they begin to speak'
    ]

    let output = npcBuilder() + ` ${searchArray(freakArray)}, and they say "`+ searchArray(omens)+`"`
    document.getElementById("Omen").innerHTML = output
};
function rumor(){
    function single(){
        let singleSubject =[
            [
                "local", 'regional', 'village', 'well-known'
            ],
            [
                `authority`, "magic user", "hero", "noble", "vagrant", "visitor", "criminal", "citizen", 
            ]
        ]
        return searchArray(singleSubject[0]) + " " + searchArray(singleSubject[1])
    }
    function plural() {
        let pluralSubject =[
            [
                "local", 'regional', 'village', 'well-known', "notable", 'well-to-do'
            ],
            [
                `authorities`, "magic users", "heroes", "nobles", "vagrants", "visitors", "criminals", "citizens", 
            ]
        ]
        return "group of " + searchArray(pluralSubject[0]) + " " + searchArray(pluralSubject[1])
    }
    let method = [ 
        `a ${searchArray(['magical', 'nonmagical'])} animal`,
        `${searchArray(['a weapon','a heavy object','their bare hands',`poison ${searchArray(['in their food','on their clothes','in the air'])}`,`deprivation through ${searchArray(['starvation','exposure','dehydration'])} and ${searchArray(['imprisonment', 'restrained and cast out'])}`,`a ${searchArray(['spell', 'magical curse', 'magical item'])}`])}`, 
        `a ${searchArray(['fall', 'fire', 'drowning', 'robbery gone wrong', 'mundane object trapped to be deadly'])}, framed as an accident`,
    ]
    let motive= [  
        "money", "romantic differences", "a percieved slight", "religious reasons", `${searchArray(['magical', 'social'])} compulsion`, "property", "some secret", "a case of mistaken identity, and now they are trying to cover it up",
    ]
    let startArray = [
        "Did you hear ", "Rumor has it "
    ]  
    let complication = [
        "Also, the victim(s) were related to the killer(s).", `It seems to have been done at the behest of a ${searchArray([plural(), single()])}.`, 
    ]
    let verb = [
        'killed'
    ]

    let storyTemplate = [
        searchArray(startArray) + "a "+ single() + " " + searchArray(verb) + " a "+ single() + `. I heard they used ${searchArray(method)}, and it was all done because of ${searchArray(motive)}.`+ ` ${variableEvent(complication)}`,
        searchArray(startArray) +"a "+ plural()+ " " + searchArray(verb) + " a "+ single() + `. I heard they used ${searchArray(method)}, and it was all done because of ${searchArray(motive)}.`+ ` ${variableEvent(complication)}`,
        searchArray(startArray) +"a "+ plural() + " " + searchArray(verb) + " a "+ plural() + `. I heard they used ${searchArray(method)}, and it was all done because of ${searchArray(motive)}.`+ ` ${variableEvent(complication)}`,
        searchArray(startArray) +"a "+ single() + " " + searchArray(verb) + " a "+ plural() + `. I heard they used ${searchArray(method)}, and it was all done because of ${searchArray(motive)}.`+ ` ${variableEvent(complication)}`,
    ]

    let output = npcBuilder() + ` says nervously, "` + searchArray(storyTemplate) + `"`
    document.getElementById("Rumor").innerHTML = output
};
function prophecy(){
    let beginning = [
        "when the Rite of Annihilation is performed during a total planetary alignment.", "if the majority of living souls on the planet pray for it.", "when human civilization achieves the goal for which it was originally designed by entities beyond comprehension: concentrating platinum into an easily harvested form.", "with the first and final casting of the spell Power Word: End.", "when the angels of justice finally manage to argue past their deadlock with the angels of mercy for the destruction of the world.", "when an emperor unites all the kingdoms of the world under one crown and decrees it.", "when the old gods are unchained from their chthonian prison.", "when the Gloaming Horn is blown with enough force to topple castle walls.", "if the four ur-temples at the corners of the earth are desecrated.", "under conditions lost to mortal knowledge.", "if ever the gods’ supply of spilled blood and sacrifices wavers.", "when the last elf fades from the world.", "when the fruit of the Tree of Anti-Life is fed to a would-be messiah.", "in order to censor the spread of an ultimate cosmic secret.", "when an act so vile is committed that the universe rejects itself.", "when one of the thirty-six truly righteous people in the world is made to believe that they are what they are despite their deep humility.", "at the time predetermined at the world’s creation. Manipulating the golden Doomsday Clock might accelerate or delay this inevitable date.", "when the three pieces of the End-Bringer’s Blade are reunited.", "when the seal at the bottom of the Tomb of Worlds is broken.", "when the Questing Beast is caught and killed by an unworthy knight."
    ]
    let proponents = [
        "a militant secret society of skeptics who believe it to be necessary to reveal the illusory nature of the world.", "a disgraced order of paladins who believe this will save the world from an oncoming eon of evil and degeneration.", "a coterie of wizards who seek to usurp the gods by becoming the creators of a new universe.", "a genie bound to the wish of a misanthrope.", "an ultraterrestrial para-deity trapped within the world in a cycle of reincarnation in wretched mortal forms.", "an ultranationalist faction confident that they can preserve their own lands as a habitable sliver while the rest of the world is wiped away.", "an uncanny intelligent machine from the future, seeking to prevent its own abominable construction.", "the demiurge, architect of falsehood, who wishes to shape a new material reality to entrap more luminous souls.", "a fanatical popular movement based on a peculiar interpretation of scripture, wherein the apocalypse will result in a utopia.", "an infamous company of veteran mercenaries who desire an end to all conflict.", "a dryad-like creature bound to ferns instead of trees, who wants to deny the world usurped from them to the seeded and the flowered.", "a ghost who would rather see the world destroyed than move further from their treasured past.", "a union of overworked zeitgeists who want the turning of the ages stopped for an unmeasurable non-eon.", "a beloved, preternaturally-talented composer who desires the apocalypse as the coda to their greatest symphony yet.", "an immortal alchemist who has become terminally bored with everything.", "a nihilist social club.", "a possessing curse bound to kill all the descendants of someone who betrayed its creator tens of thousands of years ago. Most people are now descended from that someone.", "a necromancer who will establish a kingdom of the dead from the bones of the old world.", "invaders from a parallel timeline of secondary possibilities, seeking to supplant their primaries.", "a vengeance-crazed fallen hero who thinks it is the only way to destroy the phylactery of their nemesis, a geolich.",
    ]
    let sign = [
        "artists finding no inspiration for pleasant work, but an abundance of it for the harsh and hideous.", "sterility across all kinds of animals.", "the earth welling blood when dug or ploughed.", "all birdsong becoming the same threnody.", "the moon appearing as a glaring bloodshot eye.", "the living dreaming of the dead mourning for them.", "livestock being born as insatiable meat-eaters.", "an autumn without end.", "idols and icons spontaneously weeping black ichor.", "misrule in all kingdoms.", "colour dimming and darkness deepening.", "the rebuilding of the True Sanctum, which will be the sole, hotly contested place untouched by the apocalypse.", "fresh corpses rising to dig their own graves.", "oracles and soothsayers all screaming at once before falling dead.", "the birth of prodigal infants able to speak and walk from the moment of their first breath.", "an endless storm of locusts scouring the land back and forth.", "ploughs spontaneously reforging themselves into swords.", "cities being overrun with wilderness and feral creatures.", "the appearance of a comet like a bloody pennant.", "a sickening miasma sweeping through the lowlands.",
    ]
    let doom = [
        "giants will rise from the sea and trample cities and mountains to dust.", "the stars will rain down, burning away the forests and the seas.", "the barrier between worlds will wear thin and tear, merging a corner of the multiverse into a mind-bending mosaic.", "light will fade from the heavens and all the world will become the larder of monsters swarming up from its shadow.", "an army of hollowed men will be raised, wielding weapons yet unseen to scourge the earth clean.", "the moon will crack as if an egg and release unclean radiance that transmutes all things exposed to it.", "a slow and steady plague of petrification will sweep the globe. Refugees from stone nations will hack up sand from bloody lungs, all triumphs lost to Ozymandian crumbling.", "complexity will flatten until only an infinite featureless plane exists. Higher thought will be one of the first things to go.", "things will begin to decay while still living, the only way to stave it off for a time being to devour another living thing.", "the world will be swallowed by a tempest. The land will be drowned by sky-high waves and vapourized beneath volleys of lightning.", "all water will become bitter and undrinkable, the soil will lose its goodness, and the glare of the sun will intensify until everywhere is a bleached desert.", "all people will become utterly atomized and alienated from each other, irrevocably separated into personal realities that can only contact each other through horrific violence.", "a veil will be lifted, and everything up until that point will seem to have been very silly. People will laugh themselves to death, or not bother with anything further until it all falls apart.", "every pantheon’s Götterdämmerung will kick off at once.", "the perfect cancer will metastasize, an immortal disease that assimilates all life within it.", "the meek shall inherit the earth, and the strong shall devour the meek’s reward.", "fire will spread from the world’s core, and ice from its poles. Everything will be destroyed in their collision.", "sense and causality will dissolve as if all the world were a dream.", "sorcerous ability will appear at random in people, in frequency and potency never before seen. Their magically-backed whims will tear reality asunder.", "the tools and machines of humanity will sprout new forms and complexities at an accelerating rate, coating first the planet and then the sun, ushering in the obsolescence of mere meat.",
    ]
    let aftermath = [
    "the continuity of time itself will break and turn upon itself.", "all will decline, crumbling over eons into the void.", "the few survivors will shed their lowly flesh and ascend.", "the world will return to primal innocence, as it was in the beginning.", "the lands of the living and the lands of the dead will switch their places, and ghostly throngs will feel their pulse quicken once again.", "the cosmos will reset to the day before it kicked off, with everyone retaining fractured memories of it.", "hyperdimensional vulture-analogues will pick over the wreckage.", "the planet will explode and fill the cosmos with its shards of new kinds of being.", "the dregs of the world left over will drain down to become a new layer of the Abyss.", "there will only be goblins left.", "a circle of skalds will attempt to save some part of the world by singing its stories into other realities.", "the world will be quarantined by the proper authorities to prevent its spread.", "the world’s countless ghosts and sundered futures will merge and be extruded into other worlds as destrudinous psychic sludge.", "most of the world will be reborn through random fluctuations in thermodynamic equilibrium many eons hence.", "the luckiest survivors will sail on celestial winds into the new world born from the old’s ashes.", "the dead world will be raised as a necrokosmos by an arch-necromancer in another universe.", "a new ecosystem with new peoples will emerge, adapted to the changed reality.", "the most interesting survivors will be put in an ultraterrestrial zoo.", "the world and its ending will repeat, diminished and degraded each time, as though remembered by a senile god.", "explorers will come from unreached elsewhere and marvel at what once was.",
    ]

    let voice = [
        'booming, otherwoldly voice', 'small and trepidacious voice', 'hateful and angry voice', 'sad and hopeless voice', 'joyful and unsettling voice'
    ]

    let output =  npcBuilder() + ` in a ${searchArray(voice)}, they say,` + `"Doom is coming, you'll see it ${searchArray(beginning)} Beware ${searchArray(proponents)} Keep watch for ${searchArray(sign)} This will be the end, ${searchArray(doom)} And for those who survive, ${searchArray(aftermath)}"`
    document.getElementById("Prophecy").innerHTML = output
};


