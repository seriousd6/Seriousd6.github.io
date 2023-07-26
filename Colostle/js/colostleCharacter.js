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
function shuffleSlicePrint(array, number) {
    let a = shuffle(array).slice(0, number)
    return a.join(', ')
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


//Character Creation
    //Calling
    let calling = [
        `There is an army sweeping through the lands around your village. You have heard tales of their unstoppable nature; burning villages in their wake, their men clad in monstrous, spiked black armour. One night they arrive at your village; it is chaos, people screaming, running for their lives, the roofs of your people’s huts and tents ablaze, lighting up the night sky. But most terrifying of all... Rooks, following their general’s commands, their eyes burning with a purple flame. No-one has ever commanded a living Rook before - how is this possible? You survive. Maybe you’re left for dead, maybe you hide. Maybe they took someone you love, maybe you just want revenge... either way, you will need to get to the bottom of the mystery of the Black Army and the Rooks of Purple Flame.`,
        `You have a vision as you sleep one night; far across the lands, in a room that looks nothing like the room your village resides in, is a tower. The tower looks like it might have been a Rook once; thin and impossibly tall with its slender arms by its sides. In your vision you see a weapon in a room at the very top of the tower, waiting, calling for you. Your village has been besieged by Rooks lately, your hunters are stretched thin. Maybe, if you could reach this mythical place, you might be able to save your village?`,
        `It flew overhead, casting a shadow black as night in the middle of the day - the Dragon Rook, the only Rook known to fly. You hear whispers and rumours of a party heading out to hunt it... they say if you can defeat it, you will gain the ability to fly... you can’t let them get to it first.`,
        `Most villages and peoples living in the Colostle have a passive opinion about the Rooks; they are simple wildlife and rarely seen, nothing to be too worried about. But not your village. Your village has hated all Rooks ever since one ploughed right through the centre of your homes, killing loved ones and disappearing into the night. Which is why your secret friendship with a very unusual Rook would not go down well with the villagers if they ever were to discover it. You meet your friend in a nearby forest as often as you can. It doesn’t talk, but it doesn’t attack; it’s not like other Rooks but you don’t know why. One day when you pay it a visit, it is gone from its usual place, and there are signs of a scuffle and a trail leading off into the distance. You have to go find it.`,
        `As a child, your mother used to tell you stories of warriors with diamond skin, morphing weapons of magma and obsidian blades that never dulled. Their powers came from the Fabled Rookstones; ancient one-of-a-kind stones, hundreds of them, made of a different rock, crystal or gem and each holding a unique magical power. It wasn’t true of course; there are only 3 kinds of Rookstones, Ice, Shock and Rumble, and all Rooks have one of these. Everybody knows that. But now, as an adult, you know a little more, you’re a little wiser to the world. And you know that stories like that don’t exist without a grain of truth. What if the legendary Rookstones actually exist?`,
        `A map and a key passed down in your family. The map covers a huge area; you can see multiple rooms - and you’ve never even seen the edges of your Room! 5 locations are marked on it with different coloured glyphs. The locations look like ancient Rook bodies, long since fallen, rotting like ancient temples. The key is ornate and strange, with a Rook symbol carved into its head. It looks like it would fit into a Rook. Maybe those 5 ancient Rook bodies are locked, and only you have the key. But what could possibly be hidden within?`,
        `You are a member of an order of Knights. Knights have one job: They are highly trained and conditioned to take on Rooks and are some of the greatest Rook fighters in all of the Colostle. Your superior in your Order has called you into his office, and he has a mission for you...`,
        "Legend speaks of an ancient prophecy that foretells the rise of a powerful Rook King who will unite all Rooks under his banner and bring either ruin or prosperity to the land. You possess a mysterious mark on your hand, a symbol that matches the one described in the prophecy. Now, people are starting to notice the mark and rumors spread about your connection to the Rook King. Some believe you are the chosen one, destined to fulfill the prophecy, while others fear you as a harbinger of destruction. As the weight of destiny rests upon your shoulders, you must decide whether to embrace your fate or forge your own path.",
        "A group of Rooks, unlike any you've ever seen, have been appearing near ancient ruins. They are larger, more intelligent, and seem to possess an ancient magic. These Rooks are rumored to guard a legendary artifact said to grant immense power to whoever possesses it. Adventurers from all corners of the Colostle have started flocking to the ruins, eager to claim the artifact for themselves. You, too, are drawn to the ruins, but for a different reason. You seek answers about the origins and purpose of these enigmatic Rooks. Unraveling the mystery may lead you to the artifact or reveal a greater threat lurking in the shadows.",
        "In a remote corner of the Colostle, a reclusive Rook whisperer has been studying the creatures for years. This mysterious individual has managed to form a telepathic bond with a powerful Rook called the Mindweaver. The Mindweaver is said to have knowledge beyond mortal comprehension, and the Rook whisperer seeks to use this connection to unravel the ancient secrets hidden within the Rook society. However, the Rook whisperer has disappeared, and the Mindweaver is growing restless, sending out psychic messages to those sensitive enough to receive them. As one of the few people capable of hearing the Mindweaver's call, you embark on a journey to find the missing Rook whisperer and uncover the Mindweaver's secrets before they fall into the wrong hands.",
        "A deadly illness is spreading throughout the Colostle, and the source is suspected to be an ancient curse carried by a rare and elusive Rook species. As the disease claims more lives, healers and scholars are desperate to find a cure. You are among the few who have seen these mysterious Rooks up close, and you possess knowledge that could hold the key to unlocking the cure. However, the Rooks are highly territorial and reclusive, making it perilous to approach them. With time running out, you must navigate treacherous terrain and outsmart dangerous creatures to uncover the secret of the cursed Rooks and save your people from the spreading plague.",
        "You have always been fascinated by Rooks and their mysterious nature. Unlike others who fear or hate these creatures, you have devoted your life to understanding and protecting them. As an expert in Rook behavior, you've noticed a sudden change in their demeanor. They are becoming increasingly aggressive and hostile towards humans, launching unprovoked attacks on villages. You suspect that some external force is influencing the Rooks, causing this unnatural behavior. To stop the escalating conflict between humans and Rooks, you set out on a perilous journey to discover the source of the disturbance and restore harmony between the two species.",
        "For generations, your family has been the guardians of a sacred forest, home to a group of ancient and wise Rooks. These Rooks have acted as protectors of the forest and its inhabitants for centuries, maintaining a delicate balance between nature and civilization. However, a powerful and corrupt entity has emerged, seeking to exploit the forest's resources and disrupt its harmony. With the sacred forest under threat, you must rally the Rooks and other guardians to defend their home and preserve the ancient wisdom held within. Your journey will take you through perilous battles and profound revelations about the true nature of the Colostle.",
        "In the heart of the Colostle lies a hidden sanctuary known as the Rook's Haven. This sanctuary is rumored to contain ancient knowledge and artifacts that could reshape the fate of the entire world. Many have attempted to find the sanctuary, but none have succeeded. With the world on the brink of chaos, you embark on a dangerous quest to uncover the elusive Rook's Haven. Along the way, you encounter powerful foes, unravel long-forgotten secrets, and face the ultimate challenge of proving yourself worthy of the sanctuary's wisdom and power.",
        "You are a gifted Rook tamer with the ability to communicate with these majestic creatures through a unique form of telepathy. Your talents have earned you both admiration and envy from others in the Colostle. When a powerful and enigmatic Rook known as the Celestial Sovereign descends from the skies, heralding an era of unprecedented change, you sense a profound shift in the balance of the world. As tensions rise and conflicts escalate, you must navigate through political intrigue, ancient prophecies, and personal dilemmas to understand the Celestial Sovereign's true intentions. Your choices will determine the fate of the Colostle and its inhabitants.",
        "In the heart of the Colostle lies a mysterious and ever-changing labyrinth known as the Rook's Maze. This intricate structure is said to hold immeasurable treasures and arcane knowledge guarded by elusive Rooks with riddles as their only language. Many have entered the maze seeking its treasures, but none have returned. Fueled by the allure of unimaginable riches and the thirst for ancient wisdom, you venture into the Rook's Maze. As you delve deeper, you must rely on your wits and ingenuity to solve the Rooks' riddles, avoid deadly traps, and confront the enigmatic Maze Guardian, a legendary Rook whose power is said to transcend reality itself.",
        "In a world where Rooks are a symbol of fear and destruction, you are an artist who sees beauty in these creatures' mysterious nature. Through your art, you capture the essence of Rooks, portraying them not as harbingers of doom but as enigmatic beings worthy of admiration. Your artwork gains unexpected popularity, captivating the hearts of people across the Colostle. As your reputation grows, you attract the attention of a reclusive Rook art collector known as the Master of Feathers. This enigmatic figure offers you a chance to see the Rooks as no one else has before, leading you on an artistic journey that will challenge your perception of the world and reveal the hidden depths of the Colostle's ancient connection with these magnificent creatures.",
        "In a world where Rooks are considered soulless monsters, you have always believed there is more to them than meets the eye. Your studies have led you to a forbidden library that houses ancient texts about the true nature of Rooks and their mysterious origins. As you delve deeper into the secrets hidden within the scrolls, you uncover a hidden society of Rooks that possess intelligence, emotions, and even the ability to communicate with humans. Determined to reveal the truth to the world and change the perception of Rooks, you must navigate through a web of deception, face opposition from powerful forces, and forge an unprecedented alliance between humans and Rooks to usher in a new era of understanding and harmony.",
        "Your village has always been plagued by enigmatic curses, and rumors persist that these curses are connected to ancient Rook artifacts scattered across the Colostle. As an aspiring archaeologist, you embark on a perilous journey to uncover the truth behind these artifacts and the mysteries they hold. The path ahead is fraught with danger, and you must navigate through treacherous terrain, decipher cryptic clues, and face the wrath of cursed Rooks guarding their relics. Only by unraveling the ancient secrets can you break the curses that haunt your village and prevent the unleashed power from falling into the wrong hands.",
        "The Colostle is on the brink of an unprecedented celestial event known as the Rook's Eclipse. Once in a thousand years, the stars align to grant one individual a unique and extraordinary ability bestowed by the Rooks themselves. As the Rook's Eclipse approaches, you find yourself at the center of attention, as many believe you to be the chosen one. Each faction seeks to sway you to their cause, promising power, wealth, and glory. With the fate of the Colostle hanging in the balance, you must navigate the intricacies of political intrigue, test the limits of your newfound power, and ultimately make a choice that will shape the destiny of the world forever.",
        "In a remote village, a mysterious Rook Oracle has taken residence. This oracle is said to possess the ability to see glimpses of the future through ancient Rook runes. The villagers seek the oracle's guidance for important decisions, and her visions have been instrumental in averting disasters in the past. However, a powerful group of skeptics is spreading fear and distrust, claiming that the oracle's visions are mere deception. As an impartial seeker of truth, you are determined to investigate the Rook Oracle's powers and uncover the source of her visions. Your journey will take you through treacherous terrains, and you must confront your own doubts and beliefs to reveal the truth behind the enigmatic oracle.",
        "A legendary Rook race known as the Thunderbolts is rumored to be the fastest and most agile among all Rooks. Their swiftness is said to rival lightning, making them formidable allies or adversaries. Many have tried to capture a Thunderbolt to harness its speed, but all have failed. You, however, stumble upon an injured Thunderbolt, and its presence in your village brings both hope and danger. As you nurse the creature back to health, you develop a unique bond, and you realize that the Thunderbolt is the key to saving your village from a calamitous storm approaching the Colostle. To protect the Thunderbolt and harness its speed, you must face Rook poachers, fierce storms, and your own fears.",
        "Rumors of a long-lost Rook sanctuary hidden deep in the heart of the Colostle have surfaced. Said to be a place of immense wisdom and untold knowledge, this sanctuary is believed to contain the secret to unlocking the true potential of Rookstones. As a Rookstone collector and researcher, you have dedicated your life to understanding the mystical properties of these ancient artifacts. With the revelation of the sanctuary's existence, you embark on an expedition to find it, braving treacherous landscapes, cunning traps, and rival collectors who seek to claim the knowledge for themselves. The journey will challenge your expertise and push the boundaries of what you thought was possible with Rookstones.",
        "A forgotten ancient civilization left behind a series of mysterious Rook statues scattered across the Colostle. Each statue is rumored to hold unique powers and guarded secrets. No one has been able to activate the statues' magic until now. You accidentally activate one of the statues, triggering a chain reaction that awakens the others. As the statues' magic stirs, they begin to cause chaos across the lands, granting great powers to some but wreaking havoc in others. Guided by visions and ancient texts, you must decipher the statues' purpose and find a way to harness their magic before they tear the Colostle apart.",
        "For generations, your family has served as the guardians of an ancient library containing the accumulated knowledge of Rooks and their history. As a new guardian, you have taken on the responsibility of preserving this knowledge for future generations. However, a dark cult seeks to destroy the library and erase all records of the Rooks' past. They believe that with the eradication of Rook history, they can reshape the world according to their desires. You must protect the library at all costs and uncover the truth behind the cult's motivations. Your quest will take you on a perilous journey through forgotten realms and forgotten Rook tales, testing your resolve and knowledge as a guardian.",
        "The Colostle is in the midst of a time of turmoil, as wars between different factions escalate. The Rooks, too, have been affected by the conflict, and they are being hunted and exploited for their abilities in the battles. You are a skilled negotiator and peacemaker, known for your ability to communicate with both humans and Rooks. You are approached by a group of Rook leaders who seek your help in mediating a peace treaty between the warring factions. As you delve deeper into the negotiations, you uncover hidden agendas, dark secrets, and an ancient prophecy that could reshape the future of the Colostle. The fate of the entire land now rests in your hands as you strive to bring about harmony between humans and Rooks and put an end to the senseless bloodshed.",
        "The legendary Rook Crown, rumored to grant its wearer the power to command all Rooks, has resurfaced after centuries of being lost. The Crown is said to be hidden within the treacherous Rook's Labyrinth, a place filled with illusions, traps, and ancient guardians. Many have entered the labyrinth, but none have returned. You are determined to find the Crown, not for power, but to keep it out of the wrong hands. Armed with ancient maps and riddles, you set out on an epic quest, joined by a group of unlikely allies. Each step takes you deeper into the heart of the labyrinth, where you must confront your fears, solve intricate puzzles, and prove your worthiness to claim the Rook Crown or ensure it remains hidden forever.",
        `A mysterious plague is affecting Rooks across the Colostle, causing them to lose their natural instincts and attack villages indiscriminately. As an experienced Rook researcher, you suspect foul play, and your investigation leads you to the discovery of an ancient artifact known as the "Rookbane." This powerful relic is said to possess the ability to control Rooks' minds and bend them to its user's will. You must race against time to find the Rookbane before it falls into the wrong hands, while also finding a cure for the afflicted Rooks. Your journey will take you to the darkest corners of the Colostle, where you must confront a shadowy organization that seeks to unleash chaos upon the land.`,
        "A powerful and ancient Rook guardian has awakened from its long slumber. Legends speak of its ability to bring both prosperity and devastation to the land. As the guardian wreaks havoc across the Colostle, various factions seek to harness its power for their own purposes. You, however, believe that the key to subduing the guardian lies in understanding its past and the ancient contract it once had with a forgotten civilization. With the help of ancient texts and the guidance of reclusive Rook scholars, you set out on a quest to uncover the guardian's true nature and restore balance to the land.",
        "A mysterious and elusive Rook species known as the Silverwings has been sighted in the highest peaks of the Colostle. Said to possess unparalleled wisdom and the ability to manipulate time, the Silverwings are sought after by scholars and adventurers alike. You receive a cryptic message from an old friend, a renowned Rook researcher, who claims to have found the location of the Silverwings' hidden sanctuary. Eager to learn their secrets, you set out on a perilous journey to reach the sanctuary, but you soon discover that you are not the only one searching for the elusive Rooks. Dark forces are also on the trail, intent on using the Silverwings' powers for their nefarious purposes. To protect the sanctuary and its ancient knowledge, you must outwit the pursuers and prove yourself worthy of the Silverwings' teachings.",
        "A sacred festival dedicated to the Rooks is held once every century in the heart of the Colostle. This festival is a time of celebration and reverence, where humans and Rooks come together to honor the ancient bond between their two species. As the next festival approaches, you are chosen as the emissary to represent your village and attend the grand event. However, rumors circulate that a radical faction plans to disrupt the festival, believing it to be a sign of weakness in the face of the Rooks. To prevent chaos and protect the fragile alliance between humans and Rooks, you must navigate intricate political intrigues, form alliances, and uncover the true intentions of the radical group.",
        "In a remote corner of the Colostle lies a mysterious and enchanted forest where time flows differently. Legends say that those who enter the forest are granted the gift of communicating with ancient spirits and unraveling the secrets of the past. Drawn by the allure of this mystical place, you venture into the forest, guided by a cryptic map passed down through generations. The forest, however, is full of challenges, illusions, and trials set by the spirits to test your worthiness. As you delve deeper into the forest, you must confront your innermost fears and regrets while seeking wisdom from the ancient spirits. The knowledge you gain could change the course of history in the Colostle.",
        "A curious phenomenon is occurring across the Colostle - Rooks from different regions are vanishing without a trace. As an experienced Rook tracker, you are tasked with investigating the mystery behind these disappearances. Your journey takes you to distant lands, where you encounter unique Rook species and learn about their cultures and customs. Amid your investigation, you uncover a powerful magical artifact capable of opening portals to other dimensions. With each new portal, you find yourself in a different realm, confronting unknown dangers and meeting diverse Rook societies. As you connect the dots between the disappearing Rooks and the portals, you must make choices that will determine the fate of these mysterious creatures and the Colostle itself.",
        "A secretive group of Rook cultists is conducting forbidden experiments, seeking to harness the power of a legendary cosmic event known as the Rook Eclipse. This rare celestial phenomenon occurs once every millennium and is said to bestow incredible abilities upon those who witness it. However, the cultists' reckless experiments are endangering the delicate balance of the Colostle and drawing the attention of malevolent forces from beyond. As a skilled adventurer and Rook expert, you are recruited by an ancient order to infiltrate the cult and put an end to their dangerous activities. In the process, you will uncover ancient prophecies, dark conspiracies, and hidden truths about the Rook Eclipse that will test the limits of your abilities and determination.",
        "A legendary Rook known as the Arbiter has emerged from the depths of the Colostle. It is said that the Arbiter possesses the power to judge the hearts of individuals and mete out justice accordingly. As the Arbiter passes judgment on both humans and Rooks, a great controversy arises. Some see the Arbiter's actions as divine justice, while others believe it is a threat to free will and individuality. When the Arbiter sets its sights on your village, you must confront your past deeds and inner conflicts. Alongside unlikely allies, you embark on a quest to understand the Arbiter's true intentions and discover the path to a more just and harmonious future for the Colostle.",
        "A hidden Rook city rumored to be the birthplace of all Rooks lies deep within an ancient mountain range. The city's existence has been a mystery for centuries, but you receive a map leading to its location from an anonymous sender. The map is said to reveal the way to the city only once every few decades. With the rare opportunity before you, you set out to find the elusive Rook city, encountering treacherous terrains, ancient puzzles, and guardians along the way. However, you soon realize that you are not the only one searching for the city. As rival expeditions converge upon the hidden metropolis, you must race against time to uncover its secrets and safeguard its ancient knowledge from falling into the wrong hands.",
        "A powerful artifact known as the Rookheart, which grants the ability to control Rooks' emotions, has been stolen from a sacred temple. The stolen artifact is believed to be hidden in a city known for its underground market of rare and forbidden items. You are chosen as a member of a covert group tasked with retrieving the Rookheart and restoring it to its rightful place. To infiltrate the underground city, you assume a new identity and navigate a web of deceit, dark alleys, and shadowy figures. Along the way, you form unlikely alliances and must decide whether to use the Rookheart's power for good or prevent its misuse by dangerous individuals.",
        "Rumors spread of a legendary Rook that possesses the power to control time itself. This Time Weaver Rook is said to be able to undo past events, alter the present, and glimpse into the future. As various factions seek to control the Time Weaver Rook's abilities, you find yourself unexpectedly connected to the creature through a mysterious artifact passed down through generations. The artifact grants you glimpses of potential timelines and visions of events that have not yet occurred. With this newfound power, you must navigate a complex web of temporal paradoxes, make difficult decisions that will shape the fate of the Colostle, and ultimately decide whether the manipulation of time is a blessing or a curse.",
        "An enigmatic Rook with the ability to bring inanimate objects to life appears in your village, leaving a trail of animated sculptures and enchanted artifacts in its wake. The Artificer Rook, as it is called, sparks fascination and awe among the villagers, who believe that it may hold the key to unlocking long-lost Rook technologies and ancient art of enchantment. As you delve deeper into the mystery of the Artificer Rook, you uncover a forgotten Rook civilization that once thrived in the Colostle, but vanished mysteriously. To harness the Artificer Rook's powers and preserve its knowledge, you must decipher ancient scripts and confront guardians protecting long-forgotten Rook sanctuaries.",
        "A celestial event known as the Rookfall, where countless Rooks descend from the skies, occurs once in a generation. As the next Rookfall approaches, prophecies foretell that a chosen individual will bond with a celestial Rook and gain access to cosmic powers. You discover that you are marked as the chosen one and must seek out the location of the Rookfall. Along the journey, you encounter various factions vying for control of the celestial Rooks' powers for their own ambitions. To protect the balance of the Colostle, you must form an unbreakable bond with a celestial Rook and thwart those who seek to misuse its otherworldly abilities.",
        "In a forgotten corner of the Colostle lies a hidden realm called the Rookrealm, a magical pocket dimension created by ancient Rook sorcerers. Legends speak of the realm's ability to grant wishes, but also of its treacherous challenges that only the worthy can overcome. Drawn by the allure of fulfilling your deepest desires, you venture into the Rookrealm, guided by the whispers of the ancient Rooks. The realm's illusions and ever-changing landscapes test your resolve and force you to confront your true desires and fears. As you navigate through this enchanting yet perilous realm, you must decide whether to pursue personal ambitions or to seek a greater purpose that will benefit the Colostle as a whole.",
        "A charismatic Rook oracle has been hosting mysterious gatherings in the heart of the Colostle, drawing in individuals from all walks of life. The Oracle Rook is said to possess the gift of prophecy, offering glimpses of potential futures and life-altering advice. Intrigued by the prospect of gaining insight into your own destiny, you attend one of the oracle's gatherings. To your surprise, the oracle addresses you directly, presenting a series of cryptic riddles and visions that hold the keys to unlocking your true potential. As you interpret the oracle's messages, you must confront personal doubts and make pivotal choices that will shape the course of your journey in the Colostle.",
        "A powerful and ancient Rook guardian known as the Soulrender awakens from its millennia-long slumber. Legends speak of the Soulrender's ability to consume and harness the souls of the departed, granting it unparalleled strength. As the guardian embarks on a relentless quest to fulfill its unknown purpose, the Colostle is plunged into chaos and fear. In a twist of fate, you discover that you possess a unique connection to the Soulrender, able to hear its haunting whispers and visions. Driven by a sense of responsibility, you set out to understand the guardian's motives and prevent it from wreaking havoc upon the living and the dead. In your quest to find the truth, you encounter lost spirits, ancient rites, and the ethereal realm that holds the key to the guardian's destiny.",
        "The Colostle is on the brink of a catastrophic event known as the Rookstorm - a massive convergence of powerful Rooks that threatens to unleash chaos and destruction. To prevent this cataclysmic event, you must embark on a quest to locate and awaken the dormant Rook Wardens scattered across the Colostle. These ancient guardians are the only ones capable of calming the Rookstorm and restoring balance to the land. However, finding the reclusive and long-forgotten Rook Wardens proves to be a daunting challenge, as they have withdrawn from the world for centuries. Guided by the whispers of the wind and the clues left by the Rook Wardens' allies of old, you journey into the heart of the Rookstorms and must harness the elemental forces to protect the Colostle from impending doom.",
        "In the heart of the Colostle lies a hidden library known as the Archives of the Rooks. Within its labyrinthine halls lie countless tomes, scrolls, and ancient artifacts containing the accumulated knowledge and history of the Rooks. As a scholar and adventurer, you dream of gaining access to this repository of wisdom. However, the entrance to the Archives remains a well-guarded secret, accessible only through a series of trials and challenges that test your intellect, courage, and wisdom. Alongside a diverse group of seekers, you venture into the depths of the Archives, delving into the mysteries of the Rooks' origins, forgotten civilizations, and the secrets that lie hidden within the dusty shelves. Unraveling the enigmas of the Archives may lead you to profound revelations or unveil ancient malevolence that should have remained forgotten.",
        "A long-forgotten prophecy tells of a cosmic alignment that occurs once every thousand years. During this rare celestial event known as the Rook Eclipse, the barriers between dimensions weaken, and powerful cosmic entities known as the Eclipsers emerge. Legends say that the Eclipsers grant extraordinary abilities to those who can form a bond with them. As the next Rook Eclipse approaches, you find yourself drawn into a journey to locate the elusive Eclipsers and gain their otherworldly powers. However, you are not the only one seeking these cosmic beings, and a dark cult bent on harnessing their powers for nefarious purposes also seeks to control them. In this cosmic race against time, you must uncover the secrets of the Eclipsers and decide whether the temptation of their abilities is worth the risk of unleashing untold cosmic forces upon the Colostle.",
        "A mysterious artifact known as the Rook's Tear has surfaced, said to possess the power to heal any wound or ailment. The Rook's Tear is rumored to be hidden in a sacred sanctuary guarded by a reclusive Rook guardian called the Watchful Sentinel. As the Colostle faces an unprecedented crisis of disease and sickness, healers and seekers from all corners of the land journey to find the sanctuary and claim the Rook's Tear. Drawn by a personal tragedy, you embark on a perilous quest to find the Watchful Sentinel and obtain the artifact's healing powers. Along the way, you encounter other adventurers with their own motivations, and together, you must navigate treacherous landscapes and prove your worth to the sentinel to gain access to the sanctuary.",
        "A peculiar phenomenon known as Rookshifting has been plaguing the Colostle, causing Rooks to transform into unnatural and monstrous forms. The cause of the Rookshifting remains a mystery, and the transformed Rooks pose a threat to both humans and wildlife alike. As a skilled Rookshifter yourself, with the ability to temporarily communicate and soothe the transformed creatures, you are determined to uncover the source of the affliction and find a way to restore the Rooks to their natural states. Your journey takes you to ancient ruins, forgotten caverns, and even a parallel plane where the secrets of Rookshifting are said to reside. Along the way, you encounter resistance from those who fear the transformed Rooks and must confront the ethical dilemmas of wielding your unique ability to alter their fates.",
        "A rogue group of Rook hunters known as the Crimson Talons has risen to power in the Colostle, led by a charismatic and ruthless leader known as the Scarlet Talon. The Crimson Talons' mission is to eradicate Rooks, viewing them as dangerous and unpredictable threats to humanity. As a staunch advocate for peaceful coexistence with Rooks, you join a growing resistance to protect these majestic creatures from extinction. The conflict escalates, and you find yourself entangled in a deadly game of cat and mouse with the Crimson Talons. To save the Rooks and prevent further bloodshed, you must uncover the truth behind the leader's motivations and attempt to bridge the divide between humans and Rooks before it's too late.",
        "A powerful curse known as the Rookbane has been unleashed upon the Colostle, causing Rooks to lose control of their abilities and turning them into chaotic entities. The Rookbane's origin remains shrouded in mystery, and its corruptive influence threatens to consume the entire realm. As the only one immune to the Rookbane's effects, you are deemed the Rookwarden - the guardian tasked with containing and dispelling the curse. Guided by ancient texts and enigmatic visions, you set out on a quest to find the Rookbane's source and confront the malevolent force behind it. Along the way, you must navigate treacherous encounters with corrupted Rooks and seek the aid of powerful mystics and ancient spirits to save the Colostle from the brink of destruction.",
        "In a remote and uncharted territory of the Colostle lies an ethereal realm known as the Rook's Dream. The Rook's Dream is said to be a manifestation of the collective consciousness of all Rooks, a realm where the boundaries of reality and imagination blur. Few have ever witnessed this mystical realm, and those who have speak of its surreal landscapes and enigmatic inhabitants. Drawn by the allure of the unknown, you venture into the Rook's Dream, guided by whispers from a spectral Rook. As you delve deeper into the realm, you uncover echoes of forgotten histories, encounter ethereal challenges, and unlock the secrets of the Rooks' connection to this dreamlike plane. However, navigating the realm's ever-shifting landscapes and deciphering its symbolism may challenge your very perception of reality.",
      ];
      
    //Nature
    let nature = [
        'Happy-go-lucky, extremely optimistic, fun',
        'Impatient, quick-to-anger, grumpy',
        'Brave, by-the-book, serious, no sense of humour',
        'Introspective, quiet, mysterious, person of few words',
        'Larger than life, tells exaggerated stories, roars with laughter',
        'Sly, strategic and always planning',
        'Salt-of-the-earth, common folk, finds it easy to talk with anyone',
        'Calm, composed, unshakable in difficult situations',
        'Eccentric, quirky, often lost in thought about peculiar topics',
        'Charming, smooth-talker, knows how to win people over',
        'Hot-tempered, fierce, fiercely protective of loved ones',
        'Free-spirited, adventurous, always seeking new experiences',
        'Wise, sage-like, imparts valuable life lessons to others',
        'Energetic, restless, always on the move and looking for action',
        'Nurturing, caring, takes care of others as if they were family',
        'Reserved, shy, takes time to open up to new people',
        'Analytical, logical, approaches problems with a rational mindset',
        'Empathetic, compassionate, understands and feels others’ emotions deeply',
        'Witty, sharp-tongued, uses humor to disarm or tease others',
        'Determined, persistent, never gives up in the face of challenges',
        'Adventurous, thrill-seeker, always seeking the next adrenaline rush',
        'Honest, straightforward, values truth and integrity above all else',
        'Curious, inquisitive, always seeking knowledge and understanding',
        'Charismatic, charming, can persuade others with ease',
        'Stoic, stoic, keeps emotions hidden and maintains a composed exterior',
        'Playful, mischievous, enjoys pranks and light-hearted fun',
        'Compassionate, caring, always there to lend a helping hand',
        'Enigmatic, mysterious, others struggle to understand their true motives',
        'Optimistic, sees the silver lining in even the darkest situations',
        'Diligent, hardworking, always gives their best effort in everything they do',
        'Innovative, creative, thinks outside the box to solve problems',
        'Loyal, devoted, fiercely stands by their friends and allies',
        'Resolute, unwavering, sticks to their principles no matter the cost',
        'Chill, laid-back, goes with the flow and doesn’t let things bother them',
        'Independent, self-reliant, prefers to do things on their own',
        'Daring, bold, unafraid to take risks for the greater good',
        'Analytical, keen observer, notices details that others miss',
        'Gentle, kind-hearted, treats others with gentleness and compassion',
        'Confident, self-assured, believes in themselves and their abilities',
        'Mysterious, enigmatic, others can never quite figure them out',
        'Assertive, strong-willed, always takes charge in a crisis',
        'Easygoing, adaptable, able to adjust to any situation with ease',
        'Idealistic, believes in a better world and works to make it a reality',
        'Fierce, fierce, fiercely protective of their loved ones',
        'Eccentric, quirky, marches to the beat of their own drum',
        'Humble, modest, never brags about their accomplishments',
        'Resourceful, inventive, always finds creative solutions to problems',
        'Patient, calm, never rushes into decisions and carefully weighs options',
        'Cheerful, bright, always has a smile on their face',
        'Focused, determined, keeps their eye on the prize',
        'Perceptive, intuitive, can read people and situations with ease',
        'Diplomatic, tactful, skilled at resolving conflicts and finding common ground',
        'Courageous, fearless, unafraid to face danger head-on',
        'Reliable, dependable, always comes through for their friends',
        'Quirky, eccentric, has unique habits and interests',
        'Steadfast, unwavering, remains loyal to their beliefs and values',
        'Thoughtful, considerate, puts others’ needs before their own',
        'Adventurous, thrill-seeker, always seeking excitement and new challenges',
        'Cautious, vigilant, takes calculated risks to avoid unnecessary danger',
        'Witty, clever, has a sharp and quick sense of humor',
        'Empathetic, compassionate, deeply cares about the well-being of others',
        'Daring, audacious, willing to take bold actions to achieve their goals',
        'Adaptable, flexible, can adjust to new situations and environments with ease',
        'Inquisitive, curious, always eager to learn and explore',
        'Optimistic, positive, always looks on the bright side of life',
        'Focused, determined, sets clear goals and works tirelessly to achieve them',    
    ]
    //Class
    const characterClass = {
        'Armed':{
            'exploration':'3',
            'combat':'4',
            'description':
                `The Armed quite literally have an arm from a Rook connected to them via a complex ritual, attuning its intention to them. The Armed are proficient in melee combat and are highly capableadventurers. They are warriors. An Armed adventurer could have any type of arm; a blade, a hand, a cannon, a strange machine the user doesn’t yet understand. If the arm has a hand or the ability to hold items, it can be used to carry an additional weapon if you have one.`,
            'extended description': 
                `The process of bonding with a Rook Arm is known as ‘The Grafting’. Depending on the person’s constitution, the size and weight of the Rook arm, and those who are carrying out the ritual, this process can vary from simple and painless to lengthy and painful. Because of this, Arm users tend to be battle-hardened and tough, chosen to wield an Arm because they are strong enough. Despite the immense toughness of the Armed, wielding an Arm can still take a great toll on them. Sometimes it can hurt because of its weight, or when it lifts something heavy, it tugs against the user’s body. Other times there is a mental weight, a stress in the mind when coercing it to follow command. Arm users can have any number of arms attached to them, limited only by the physical and mental weight they can bear and the size and complexity of the arms they have. Arms come in all shapes and sizes. Some are like human arms with joints and multi-fingered hands; these tend to be the easiest to wield as they challenge the mind in the same way that a human arm does. But some arms are strange or very different; like coiling segmented plates that flow like a snake, or spidery multi-jointed arrangements that split and separate. Some arms can be big and bulky enough to lift the user off the ground or carry incredibly heavy weights. Others allow users to do fine detailed work that they could never normally do with their human hands. Some Arm users claim to see messages or hallucinations, believed to be the memories of the Rook the arm came from. A complex meditation ritual involving exotic herbs and roots can allow an Arm user to see these memories more clearly and try to understand the Rooks and their purposes better. The images are always hazy and vague but there is a very real sense of a semblance of sentience even though it is generally thought that they are just machines and only Rooklings have sentience.`,
            'trait prompts': 
                [
                    'Are you a hunter who felled their first Rook and wish to wear the arm as a trophy?', 
                    'Does your village or clan fit Rook arms to their children to equip them for the harsh life of living in the Colostle?', 
                    'Did you lose a limb of your own in a battle when young and have the Rook limb fitted as a replacement?', 
                    'Is the Rook arm a family heirloom passed down your family line when the previous owner falls in battle? Are you the latest to claim it, or is there something you must do first before you are worthy?', 
                    'Is your Arm a question of status? Do others in your tribe have larger, more ornate Arms, and is it important to your character to compete or not?', 
                    'Are you the first in your family/clan/village to wield an Arm?',
                    'Have you ever encountered a rare and mystical creature in the Colostle that left a profound impact on your life? If so, how did that encounter shape your worldview and goals?',
                    'Were you once a respected member of a different profession or social role before becoming a hunter with a Rook arm? If yes, what circumstances led you to make this drastic change in your life?',
                    'Is there a particular hunter or legendary figure in your village\'s history who inspires you to become the best hunter you can be? How do you carry on their legacy?',
                    'Have you ever formed a close bond with a particular animal companion during your hunts? If so, how did this animal become your trusted ally, and what unique skills do they bring to your adventures?',
                    'How does your hunter persona in the Colostle contrast with your life before you ventured into the wild? How do you balance the two aspects of your identity?',
                    'Have you ever faced a moral dilemma during your hunts, where you had to choose between preserving the balance of nature and achieving your goals as a hunter? How did you resolve such conflicts, and how did they affect you?',
                    'Is there a powerful artifact or ancient relic in the Colostle that you seek to find or protect? What drives you to pursue this item, and what challenges do you anticipate facing in your quest?',
                    'Have you ever been part of a hunting party or adventuring group in the Colostle? What memorable experiences did you share with your companions, and do you still keep in touch with them?',
                    'Is there a unique skill or technique that you developed as a hunter with a Rook arm, setting you apart from other hunters in the Colostle? How did you discover or perfect this skill?',
                    'Have you encountered any hostile factions or individuals during your hunts? How do these conflicts shape your perspective on the Colostle\'s inhabitants, and do you actively seek to resolve or avoid such confrontations?'
                ]
        },

        'Followed':{
            'exploration':'5',
            'combat':'3',
            'description':
                `The Followed have a small Rook companion, like a pet or familiar that follows them and their commands. These ‘Rooklings’ are found in the cores of larger Rooks - as yet it is not known why. They display a base level of sentience akin to that of a dog or a cat and can form deep and personal bonds with their human companions. The Followed are excellent rangers, pathfinders and navigators.`,
            'extended description':
                `The Followed are usually very capable explorers, proficient in tracking, survival and navigation, and combined with their Rookling companions (who often have a sense of direction and knowledge about the world) they are more equipped than most to navigate the lands of the Colostle. Rooklings can vary in size from very small (the size of a kitten) to the size of a person. A Rookling will have the body and magic characteristics of the large Rook it was harvested from. To create your first Rookling, head to the ‘Creating your Opponent - Rooks’ section in the combat rules to either choose the body and magic characteristics, or draw cards to create them randomly. No two Rooklings look alike, just like the Rooks they come from, and many of them can be very strange shapes. The only consistent characteristic across them all is that they are made of stone, and seem to feature castle elements but on a much smaller scale; such as doors, windows, crenellations, tiny balconies, drawbridges, and sometimes even tiny gardens in miniature courtyards jutting out of the sides of their bodies. Fighting with Rooklings involves fighting in a partnership with your companion. Your character will have a weapon in their hands, but when you do an UNARMED or MAGIC attack this might be a moment where you command your Rookling to fight, or use its magic! Maybe it has ice powers, or the ability to roll into a ball and smash into its opponents. Maybe it can climb inside an enemy Rook and do damage from within, or maybe it can throw you high into the air to bring a weapon attack down on an enemy; the only limit is your imagination! When fighting with your Rookling companion, think about what it is about your partnership that makes you skilled Rook hunters. Maybe you even have some special moves that you can do together due to a convenient combination of specialities!`,
            'trait prompts': 
                [
                    'Does your village or clan hate the Rooks, and did you have to keep your bond with a Rookling secret?',
                    'Is your Rookling the core of a Rook that killed someone close to your character?',
                    'Is your bond with your Rookling a reluctant one; does it follow, but you wish it didn’t? ',
                    'Does your Rookling have something special about it? A strange crest or a hand that looks like a key?',
                    'Think about your Rooklings shape, abilities and how it would fight in combat. With these things considered it will make it easier to come up with strategies in battle!',
                    'Has your Rookling ever displayed unexpected abilities or powers, hinting at a deeper mystery behind its origins?',
                    `Is your character's bond with the Rookling viewed positively or negatively by others in your village or community?`,
                    'Has your Rookling ever been in danger, and what sacrifices did your character make to protect it?',
                    'Does your Rookling have a unique name or special significance, and how did your character come up with it?',
                    'Is there a rival or antagonist in the Colostle who seeks to harm or capture your Rookling, and how does your character plan to confront this threat?',
                    'Has your character ever faced a moral dilemma regarding their bond with the Rookling, and how did they resolve it?',
                    'Does your Rookling have any peculiar eating habits or dietary preferences that your character has had to adapt to?',
                    'Has your character ever encountered other individuals who have formed bonds with Rooklings, and what was their relationship like?',
                    'Does your Rookling possess a unique marking or trait that distinguishes it from other Rooklings?',
                    'Is there a prophecy or legend in your village about a chosen one who would form a powerful bond with a Rookling, and could it be related to your character?',
                    'Has your Rookling ever saved your character from a dangerous situation or shown remarkable intelligence or loyalty?',
                    'Is there a specific event or circumstance that led to your character forming a bond with the Rookling? How did this event change your character\'s perspective on the Colostle and its creatures?',
                    'Does your character have a special connection or telepathic link with the Rookling, allowing for non-verbal communication and understanding?',
                    'Has your Rookling ever faced hostility or mistreatment from others, and how did your character react or defend their companion?',
                    'Is there a particular goal or quest that your character and the Rookling share, binding them together in a shared purpose and destiny?'
                ]
        },

        'Helmed':{
            'exploration':'2',
            'combat':'5',
            'description':
                `The Helmed harvest a piece of strange machinery from the very core of a Rook and, using rituals and a real working understanding of the crystal patterns and stones, they are able to create a Helm that can be worn and operated, granting them the magical abilities of the Rook it was harvested from.`,
            'extended description':
                `The Helmed are the closest to wizards or alchemists in the world of Colostle. Understanding the magical properties of Rooks and how to harness them is partly a pursuit of arcane knowledge and also one of logic and crystal-engineering, like magical circuitry. Any human-made devices that use Rookstones, like lanterns or refrigeration chambers, are made by the Helmed, or someone who would be a great candidate for a Helm. This knack for Rook alchemy is rare and even if it manifests in someone, there is then the added challenge of defeating a Rook to obtain the part or parts usable to create a Helm. However, once done, unlike the Arm which requires attunement and a great toll on the body, the use of a Helm is purely operative, there is no attunement required. It is, however, complex and a deep understanding is required. The Helmeds skills are the most sought after in society. Manipulating and understanding the magical ‘technology’ of the Rooks allows people luxuries beyond the reach of human technology. This can mean one of two things for the Helmed, they are either venerated, or enslaved, depending on the nature of the person who comes across them. Others still consider the Helmed to be Rook sympathizers or ‘witches’. They are thought to be brainwashed with a Rooks thoughts infecting and affecting their own, as such they are often driven out of smaller settlements and distrusted in larger ones. Some religious zealots consider the use of the Rookstone magic to be heresy; consorting with the monsters that threaten everyday life for people. These people consider the Helmed to be the very worst heretics.`,
            'trait prompts': 
                [
                    'Has your character always had an understanding of Rooks since they were young? And if so, how did they first discover that?',
                    'Does your character respect the Rooks, or simply see them as a source for scrap to tinker with?',
                    'Is your character more comfortable in their workshop, dissecting and assembling, and is therefore reluctant to head out on a grand quest or journey?',
                    'Is your character surrounded by brave warrior Armed or strategic ranger Followed, and feeling a need to prove their worth in their village or clan?',
                    'Is your character driven to understand the mechanisms and technology of the Rooks and the Colostle as a whole?',
                    'Does your character have a unique understanding of Rook technology, granting them the ability to modify and enhance Rook arms in unconventional ways?',
                    'Has your character ever faced criticism or skepticism from others in their village or community due to their fascination with Rooks and their affinity for machinery?',
                    'Does your character have a collection of rare and ancient Rook parts that they keep as prized possessions or study for knowledge?',
                    'Is your character renowned for their inventive genius and innovation, with other members of their village seeking their guidance in mechanical matters?',
                    'Has your character ever encountered malfunctioning or hostile Rooks in the Colostle, and how did they handle such dangerous situations?',
                    `Is your character driven by a desire to uncover the secrets of the Colostle's ancient technology and harness it for the betterment of their village or civilization?`,
                    'Has your character always had an affinity for tinkering and mechanics, even before they encountered the Rooks?',
                    'Is your character haunted by the memory of a failed experiment or invention that had unintended consequences?',
                    'Does your character have a mentor or role model who was a skilled engineer or inventor, and do they strive to live up to their legacy?',
                    'Is your character known for their exceptional craftsmanship and the unique designs they incorporate into their Rook arms?',
                    'Does your character have a rival or competitor in the field of Rook technology, and how does this rivalry fuel their drive to innovate?',
                    'Has your character ever encountered a mysterious and ancient Rook of unknown origin, and did it leave a lasting impact on their pursuit of knowledge?',
                    'Does your character have a special bond with a particular Rook, and do they consider it more than just a tool or companion?',
                    'Is your character an adventurer at heart, using their Rook arms not only for research but also for thrilling exploration of the Colostle?',
                    'Does your character believe that there is a greater purpose behind the existence of Rooks, and are they determined to uncover the truth?',
                    'Is your character fascinated by the fusion of magic and technology, leading them to experiment with enchanted Rook arm enhancements?'                 
                ]
        },

        'Mounted':{
            'exploration':'5',
            'combat':'2',
            'description':
                `The Mounted ride an adapted mechanism taken from Rook parts, as a vehicle or mount to allow them easier traversal across the land and sea of the Colostle. Typically this involves taking a part of the Rook responsible for it’s locomotion and disconnecting it from the main body, and turning it into something that can be operated with crude controls, mechanisms and levers. The Mounted’s mounts can vary from horse-like creatures to boats and even bikes.`,
            'extended description':
                `Like the Helmed, the Mounted are gifted Rooksmiths, with a basic understanding of their functionality. But unlike the Helmed who have an understanding of the magical circuitry and therefore magical abilities of a Rook, the Mounted have a mechanical one. The Mounted are nomads and scavengers, constantly on the hunt for felled or ancient decaying Rooks and harvesting parts for their own mount. Partly to upgrade, and partly to just keep it going, as mounts require constant maintenance, like off-road vehicles. A Mounted’s mount is their heart and their life. Like looking after a bike or a beloved car, it is everything, it is their freedom. When you defeat a Rook or come across a husk out in the wilds, your character can take parts to upgrade or add to the functionality of your mount. This functions as a story opportunity for your character. Perhaps you took damage in your last battle and you take pieces from a fallen Rook to repair it. Maybe where once there were wheels, you attach legs in their place. Individual parts of Rooks seem to function on their own. If you remove a spinning wheel from the core of a Rook it will continue to spin on it’s own. If you take a leg mechanism; it will still have power despite being disconnected. This means any part that isn’t completely smashed to splinters can be made useful to a Mounted. Mounted are capable of battling Rooks and do so using the Mount’s built in Weapons (for example a cannon or a battering ram). In COMBAT, if you draw a WEAPON attack you can use your Mount’s weapon or one that your character carries in their hands. The Mounted have a low starting COMBAT score but as you explore more you will find ways to increase that score. Don’t see this as a limitation. Instead, it is a storytelling opportunity to have your character go on an adventure of growth.`,
            'trait prompts':
                [
                    'Do you come from a village of Mounted, with buildings and encampments made of mechanical parts of Rooks? Being Mounted is in your blood?',
                    'Come up with what your mount looks like and what Weapon it has on board to help defend you on your adventures.',
                    'Perhaps your nomadic tribe is running out of Rook parts, your lands no longer as fertile for living and fallen Rooks as before. Maybe you must travel further afield to find new lands, rich in broken mechanical parts to scavenge. ',
                    'Maybe your father is famous in the tribe for his mechanical adeptness and warrior’s spirit. You live in his shadow, keen to prove you have what it takes to carry on the family name.',
                    'One day when scavenging a Rook husk you come across a part unlike any seen before. It could change how your mount functions dramatically. What would the others think if they saw it though, would they try to take it from you?',
                    'Has your character ever encountered a hostile faction or group that despises the Mounted, and how do they navigate such conflicts?',
                    'Does your mount have a unique or peculiar quirk that sets it apart from other mounts, and how does this quirk affect your adventures?',
                    'Are you known for your exceptional riding and combat skills among the Mounted, earning you a respected place in the nomadic community?',
                    'Did you once encounter a rare, ancient Rook with extraordinary abilities, and how did that encounter influence your journey as a Mounted?',
                    'Has your character ever faced a moral dilemma when scavenging parts from Rooks that might still have faint traces of life or consciousness?',
                    `Are there ancient legends or myths about Rooks and Mounted that drive your character's sense of purpose and curiosity?`,
                    'Has your mount ever been captured by an enemy faction, leading to a daring rescue mission that strengthened the bond between you and your mount?',
                    'Does your character carry an old, tattered journal passed down from a legendary Rooksmith ancestor, and do they seek to uncover the secrets within its pages?',
                    'Are there secret societies or organizations of Mounted that your character aspires to join, and what challenges must they overcome to prove their worth?',
                    'Does your character have a hidden talent or ability that surprises others in the Mounted community, and how does this skill aid in their adventures?',
                    `Are you part of a tight-knit group of Mounted who travel together, relying on each other's skills and mounts for survival?`,
                    'Did you discover a rare and powerful Rook part during your travels, and now you must decide whether to keep it for your mount or sell it for the betterment of your tribe?',
                    'Has your mount saved your life on multiple occasions, and do you share a unique bond with it that goes beyond the mechanical?',
                    'Are you a collector of Rook artifacts, seeking to gather and preserve the history of these ancient machines?',
                    'Does your character have a rival or competitor among the Mounted, and do they often find themselves in heated races to salvage the best Rook parts?',
                    'Has your mount been passed down through generations in your family, and do you feel a deep responsibility to maintain its legacy?',
                    'Is your character skilled in crafting specialized tools or gadgets for their mount, enhancing its performance and capabilities?',
                    'Do you have a deep respect and understanding of the wilderness, knowing the best locations to scavenge for valuable Rook parts?',
                    'Has your mount ever malfunctioned during a critical moment, putting you and your companions in danger, and how did you manage to overcome the situation?',
                    'Does your character yearn for a legendary Rook part said to grant incredible powers, and are they willing to go to great lengths to find it?'
                ]
        },

        'Allied':{
            'exploration':'5',
            'combat':'4',
            'description':
                `The Allied adventure out as a team but as Colostle is a solo RPG you as a player gain the ability to control two characters in the place of one. You can choose whether to play as both or just play as one and treat the other as a sort of non-playable companion. Its entirely up to you. This class is intended as a way to add more storytelling into your game for the more creatively ambitious, with a way to add character, dialogue,
                and developing relationships to your adventures.`,
            'extended description':
                `Some adventurers don’t start with the advantages of the other classes such as a powerful arm, a magical helm, a dedicated follower or a vehicle to ride and as such look to each other for the support to head out and explore the Roomlands. Allied start without a power-up like the other classes but gain the advantage of having another person who is by their side through thick and thin. Typically, Allied teams have a strong bond that leads them to want to do everything together, although there is nothing to say that this bond may be tested or even broken by what is yet to come. On their adventures, Allied characters may win arms, helms, Rooklings or mounts from their various battles or encounters and can equip them  to either character leading to an Allied being able to have a sort of multi-class effect. Most Roomlanders are solo creatures but by virtue of having two adventures so tightly bonded to each other, its possible to have one functioning as the melee fighter with an arm and one acting as support with a helm, for example. The combinations are endless.`,
            'trait prompts': 
                [
                    `Are your two characters bonded by blood (i.e. brother and sister) and in which case, do you have other siblings? Why are you leaving your family behind?`,
                    `Are your two characters in a relationship that is not blood, perhaps a romantic one or a close friendship? Did you grow up in the same location or have you met out in the Roomlands?`,
                    `Are your two charactrs thrust together in some way, perhaps unwillingly or by some sort of ritual? As a result, do they perhaps not get along but are forced to co-operate due to their goals or mission? Perhaps their relationship could change over time as they are forced to work together to survive, and maybe the reason for why they were brought together in the first place will become clear over time?`,
                    'Do your characters share a common goal or quest that brought them together, and what challenges do they anticipate in achieving their shared objective?',
                    'Are your characters from different backgrounds or cultures, and how do their diverse perspectives enhance their problem-solving abilities?',
                    'Has one of your characters made a significant sacrifice for the other in the past, and how does this act of selflessness impact their current bond?',
                    `Does one character have a secret they've kept from the other, and how might this revelation affect the trust and cooperation between the two?`,
                    'Are your characters complementary in their skills and abilities, each bringing unique strengths to the partnership?',
                    'Has the Allied duo ever encountered other adventurers who underestimate or doubt the power of their bond, and how do they prove their worth to skeptics?',
                    `Do your characters have a signature battle tactic or maneuver that they've perfected through their close collaboration?`,
                    'Are there any legendary tales or rumors of closely bonded Allied pairs that your characters aspire to emulate?',
                    'Has your Allied team ever encountered a situation where they had to choose between their personal goals and the well-being of the other, and how did they resolve the conflict?',
                    'Have your characters ever encountered a formidable adversary or situation that put their bond to the ultimate test?',
                    'Does one character have a specific fear or weakness that the other provides emotional support and encouragement for?',
                    'Are your characters known in the Roomlands as a legendary duo, and how do they feel about their reputation?',
                    'Have your characters ever been separated for an extended period, and how did they cope with the distance?',
                    'Do your characters share a favorite memory or moment from their past adventures that they often reminisce about?',
                    'Has one character ever saved the other from certain doom, creating an unbreakable debt of gratitude?',
                    'Is there a special item or memento that symbolizes the bond between your characters, and what is its significance?',
                    'Do your characters have a unique and unspoken way of communicating during battles or dangerous situations?',
                    'Has your Allied duo ever encountered another group of adventurers with a similar bond, and how did they interact?',
                    'Is there a mentor figure who taught your characters the value of loyalty and partnership?',
                    'Does one character have a personal quest or vendetta that the other is determined to support and see through?',
                    'Have your characters ever disagreed on a critical decision, and how did they resolve the conflict?',
                    'Is there a memorable moment from their shared history that led to the formation of their strong bond?',
                    'Do your characters have a shared dream or aspiration that they hope to fulfill together?',
                    'Has one character ever made a significant sacrifice to protect the other, and how did it shape their future adventures?'
                ]
        },

        'Bastion':{
            'exploration':'2',
            'combat':'4',
            'description':
                `The Bastions are a very recent and surprising discovery for the adventurers of the Colostle and as such they are not a common sight and are often viewed with fear or distrust. Bastions are the only person-sized stone/Rook constructs in the Colostle with most Rooks being much larger than a person and most Rooklings being smaller. Most notably, Bastions can speak and seem to be alive and sentient in the same way as people.`,
            'extended description':
                `Bastions originate from inside Colossal Rooks, the largest Rooks of all. Colossal Rooks are also incredibly rare. The general consensus is that thousands of years ago, there were more Colossal Rooks but now they are thought to be mostly extinct, with perhaps a few still roaming somewhere out there in the Roomlands. The Great City of Parapette was once a Colossal Rook, and it’s thought the fate of other Colossal Rooks are similar to Parapette’s, now husks containing cities or ancient dungeon corridors. Bastions are the ‘immune system’ of Colossal Rooks, defending the massive interior labyrinths of Colossal Rooks bodies from attacks by invaders. The Bastions of a Colossal Rook take on the characteristics of the Colossal Rook they live within, even down to looking like smaller, human sized versions of their colossal counterpart. They are a relatively new discovery for the people of the Colostle and due to looking exactly like the monsters that terrorise the homes and lands of Roomlanders, Bastions are not typically treated with much respect or kindness. Bastions are however capable of all the same feelings and emotions as a person, so they all have the same potential as any human Roomlander.`,
            'trait prompts':
                [
                    `Does your character come from a place friendly to Bastions where they were accepted? Or are they living in a place where they are constantly abused and attacked just for who they are?`,
                    `Does your Bastion want to trek out to find others of its kind and perhaps the Colossal Rook body they originated from, as they can’t remember their past?`,
                    `Does your Bastion character come from a colony of other Bastions who have made their own colony or village to survive away from humans? And in which case what is that life like and why would they want to leave?`,
                    'Does your character come from a lineage of Bastions, with a long history of serving inside Colossal Rooks?',
                    'Has your Bastion ever encountered other creatures similar to themselves, and how did they react to the meeting?',
                    'Does your character possess unique abilities or modifications that set them apart from other Bastions?',
                    'Has your Bastion ever felt conflicted about their role as defenders of Colossal Rooks and questioned their purpose?',
                    'Does your character feel a deep connection to the ancient Colossal Rooks and a desire to uncover the mysteries of their past?',
                    'Is there a specific event or battle in which your Bastion displayed incredible bravery and selflessness?',
                    'Has your character ever ventured into the dangerous, uncharted territories of the Roomlands to find clues about their origin?',
                    'Does your Bastion have any human friends or allies who treat them with respect and understanding?',
                    'Has your character ever experienced a malfunction or glitch in their systems, and how did they cope with it?',
                    'Does your character seek acceptance and friendship from other Roomlanders despite their resemblance to monsters?',
                    'Has your Bastion ever encountered ancient relics or technology from the time when Colossal Rooks were more abundant?',
                    'Does your character have a hidden compartment or ability that surprises and intrigues other adventurers?',
                    'Has your Bastion ever had to make a difficult decision to prioritize the safety of others over their own well-being?',
                    'Does your character keep a journal or record of their adventures and thoughts as they try to understand their purpose?',
                    'Has your Bastion ever encountered an active Colossal Rook, and how did they react to the encounter?',
                    'Does your character have a recurring dream or memory that hints at their forgotten past?',
                    'Has your Bastion ever formed an unlikely alliance with a human or other creature to achieve a common goal?',
                    'Does your character have a favorite location or landmark within the colossal body they once protected?',
                    'Has your Bastion ever encountered hostility from other adventurers who mistake them for a malevolent creature?',
                    'Does your character have a natural talent for leading and protecting others in times of danger?',
                    'Has your Bastion ever come across remnants of other Bastions and wondered about their fate?',
                    'Does your character have a unique way of communicating or expressing emotions without words?',
                    'Has your Bastion ever discovered an ancient artifact that provided clues about the history of Colossal Rooks?',
                    'Does your character have a fascination with the mechanics and inner workings of Colossal Rooks?',
                    'Has your Bastion ever had to confront their own mortality and the uncertainty of their future?'
                  
                ]
        },


    }
    let specialClass = {
        'Within': {
            'exploration':5,
            'combat':6,
            'description':
                `Those that take on the incredibly powerful Astrolithic Rooks and win are experienced, mythic warriors. And their reward is an opportunity to become Within. For with a little careful manipulation it is possible to climb into a defeated Astrolithic Rook and pilot it; like a huge stone suit of armour. However, not only are Astrolithic Rooks incredibly powerful with grand new weaponry never seen in the Rooms below... but they can fly.`,
            'extended description':
                `Easily the most powerful class; ‘Within’ is a status that is earned and is never the start of your character’s journey. Especially considering that the only way to attain a Rooksuit is by making it to the rooftops and slaying an Astrolithic Rook. All ‘Within’ start life as a different class - and when piloting their Rooksuit it acts as a temporary upgrade until they elect to leave it for some reason. While ‘Within’, a player has a few options available to them: Firstly they can fly. They can use this ability to fast travel across the battlements, or reenter the Rooms below and fly across those lands. On top of that the combat stats for a Within are immensely high, making you nearly unstoppable against other Rooks. Being Within means you are not subject to Astrolithic Rook attacks whilst within the Rooksuit. The instant you leave the suit, the Astrolithics may notice you again. You have attacks: (LASER ATTACK The Rook seems to charge some kind of glass or crystal emitter and then suddenly a blast of white heat flashes from the end and hurtles towards your character in a straight line | FLYING ATTACK The Rook swoops out of range of your attacks only to swing around in the air and lash out at you as it flies back. | GRAB ATTACK A stone hand unfolds from a hidden location and grabs you, at the same time, the Rook hurtles into the sky carrying you upward. A fall from this height could really hurt! | ROCKET ATTACK The Rook disconnects a part of itself, perhaps one of its arms or a small turret and it blasts towards you with the same propulsion as the Rook has itself for flight. Your character braces as the stone missile streaks toward you...) piloting an Astrolithic Rook. 
                When writing your Within character think carefully about what this means for your character’s story. It could be considered an end, your warrior/adventurer reaching the zenith of legend; the highest power of all. Or perhaps this power changes your character somewhat; for good or for bad. Or you could continue your journey; now as a near invincible hero and your story could introduce moments of peril by being separated from your Rooksuit or having it stolen from you. The Within is intended as the peak of your potential rewards; a gift to a player so that there is something at the end of the adventure to aspire to. But just imagine how the other characters you have met might react to seeing you in a Rooksuit - or what it might mean for advancing the story of your character’s Calling.`
        }
            
    }
    let nameArray = [//name
        "Nelia", "Thorug", "Berek", "Fen-Reley", "Soriq", "Alis", "Dreya", "Yeleris", "Perelli", "Quen", "Taura", "Reneen", "Mirriq", "Karrik", "Yalena", "Zephron", "Lyssandra", "Graul", "Virel", "Elara", "Tannith", "Vaelen", "Sylna", "Xandar", "Kallara", "Draven", "Evelia", "Zyreth", "Nylar", "Thalia", "Vaelin", "Seraphine", "Drevan", "Aurelia", "Zyrra", "Kaelon", "Sylvana", "Xarius", "Ilyana", "Vaelor", "Kyrin", "Zarina", "Lysander", "Elandra", "Thoren", "Veloria", "Xavren", "Galya", "Kythor", "Zyna", "Alaric", "Elyria", "Syndra", "Valen", "Kyrana", "Zephyr", "Thalara", "Xaelis", "Garen", "Kyra", "Zarael", "Elowen", "Tyrin", "Vasha", "Xandra", "Grenn", "Nylara", "Syrael", "Zeraphina", "Elandor", "Thalion", "Vaelora", "Xyler", "Gwynn", "Kendry", "Zavian", "Lysara", "Erevan", "Thessa", "Vesper", "Xyra", "Haldor", "Nyx", "Syrin", "Zayla", "Iliad", "Elysia", "Tavian", "Vaelis", "Zirel", "Kyrielle", "Rahel", "Dyrin", "Zephyra", "Nairis", "Gwynden", "Eryon", "Taryn", "Zarya", "Kyras", "Graelle", "Thoras", "Zylen", "Haelis", "Kyrilla", "Elinor", "Sylas", "Zandar", "Vespera", "Gaelen", "Elaria", "Thalor", "Zara", "Nylan", "Theska", "Varis", "Zaraea", "Lyndor", "Zirelia", "Erynn", "Gavric", "Zaelia", "Elysar", "Toryn", "Vaelan", "Kyren", "Saelin", "Eldor", "Thalina", "Zeryn", "Xanthe", "Gwenneth", "Elowyn", "Tarys", "Zaelynn"
        ]

    function pickName(){
        loopPrintList([searchArray(nameArray)],"Name")
    }
    function pickClass(){
        let a = searchArray(Object.keys(characterClass))
        let outputArray = []
        outputArray.push(`Class = ${a}`)
        outputArray.push(`Exploration: ${characterClass[a].exploration}`)
        outputArray.push(`Combat: ${characterClass[a].combat}`)
        outputArray.push(`Trait prompts:`)
        let b = shuffleSlice(Object.values(characterClass[a]['trait prompts']),2)
        outputArray.push(b[0])
        outputArray.push(b[1])
        loopPrintList(outputArray,"Class")
        console.log
        loopPrintList([characterClass[a].description],"Description")= `${characterClass[a].description}`
    }
    function pickNature(){
        loopPrintList([searchArray(nature)],"Nature")
    }
    function pickCalling(){
        loopPrintList([searchArray(calling)],"Calling")
    }