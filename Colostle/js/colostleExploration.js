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
        
        "A powerful artifact known as the Rookheart, which grants the ability to control Rooks' emotions, has been stolen from a sacred temple. The stolen artifact is believed to be hidden in a city known for its underground market of rare and forbidden items. You are chosen as a member of a covert group tasked with retrieving the Rookheart and restoring it to its rightful place. To infiltrate the underground city, you assume a new identity and navigate a web of deceit, dark alleys, and shadowy figures. Along the way, you form unlikely alliances and must decide whether to use the Rookheart's power for good or prevent its misuse by dangerous individuals.",
      
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
            'exploration':3,
            'combat':4,
            'description':
                `The Armed quite literally have an arm from a Rook connected to them via a complex ritual, attuning its intention to them. The Armed are proficient in melee combat and are highly capableadventurers. They are warriors. An Armed adventurer could have any type of arm; a blade, a hand, a cannon, a strange machine the user doesn’t yet understand. If the arm has a hand or the ability to hold items, it can be used to carry an additional weapon if you have one.`,
            'extended description': 
                `The process of bonding with a Rook Arm is known as ‘The Grafting’. Depending on the person’s constitution, the size and weight of the Rook arm, and those who are carrying out the ritual, this process can vary from simple and painless to lengthy and painful. Because of this, Arm users tend to be battle-hardened and tough, chosen to wield an Arm because they are strong enough. Despite the immense toughness of the Armed, wielding an Arm can still take a great toll on them. Sometimes it can hurt because of its weight, or when it lifts something heavy, it tugs against the user’s body. Other times there is a mental weight, a stress in the mind when coercing it to follow command. Arm users can have any number of arms attached to them, limited only by the physical and mental weight they can bear and the size and complexity of the arms they have. Arms come in all shapes and sizes. Some are like human arms with joints and multi-fingered hands; these tend to be the easiest to wield as they challenge the mind in the same way that a human arm does. But some arms are strange or very different; like coiling segmented plates that flow like a snake, or spidery multi-jointed arrangements that split and separate. Some arms can be big and bulky enough to lift the user off the ground or carry incredibly heavy weights. Others allow users to do fine detailed work that they could never normally do with their human hands. Some Arm users claim to see messages or hallucinations, believed to be the memories of the Rook the arm came from. A complex meditation ritual involving exotic herbs and roots can allow an Arm user to see these memories more clearly and try to understand the Rooks and their purposes better. The images are always hazy and vague but there is a very real sense of a semblance of sentience even though it is generally thought that they are just machines and only Rooklings have sentience.`,
            'trait prompts': ['Are you a hunter who felled their first Rook and wish to wear the arm as a trophy?', 'Does your village or clan fit Rook arms to their children to equip them for the harsh life of living in the Colostle?', 'Did you lose a limb of your own in a battle when young and have the Rook limb fitted as a replacement?', 'Is the Rook arm a family heirloom passed down your family line when the previous owner falls in battle? Are you the latest to claim it, or is there something you must do first before you are worthy?', 'Is your Arm a question of status? Do others in your tribe have larger, more ornate Arms, and is it important to your character to compete or not?', 'Are you the first in your family/clan/village to wield an Arm?']
        },

        'Followed':{
            'exploration':5,
            'combat':3,
            'description':
                `The Followed have a small Rook companion, like a pet or familiar that follows them and their commands. These ‘Rooklings’ are found in the cores of larger Rooks - as yet it is not known why. They display a base level of sentience akin to that of a dog or a cat and can form deep and personal bonds with their human companions. The Followed are excellent rangers, pathfinders and navigators.`,
            'extended description':
                `The Followed are usually very capable explorers, proficient in tracking, survival and navigation, and combined with their Rookling companions (who often have a sense of direction and knowledge about the world) they are more equipped than most to navigate the lands of the Colostle. Rooklings can vary in size from very small (the size of a kitten) to the size of a person. A Rookling will have the body and magic characteristics of the large Rook it was harvested from. To create your first Rookling, head to the ‘Creating your Opponent - Rooks’ section in the combat rules to either choose the body and magic characteristics, or draw cards to create them randomly. No two Rooklings look alike, just like the Rooks they come from, and many of them can be very strange shapes. The only consistent characteristic across them all is that they are made of stone, and seem to feature castle elements but on a much smaller scale; such as doors, windows, crenellations, tiny balconies, drawbridges, and sometimes even tiny gardens in miniature courtyards jutting out of the sides of their bodies. Fighting with Rooklings involves fighting in a partnership with your companion. Your character will have a weapon in their hands, but when you do an UNARMED or MAGIC attack this might be a moment where you command your Rookling to fight, or use its magic! Maybe it has ice powers, or the ability to roll into a ball and smash into its opponents. Maybe it can climb inside an enemy Rook and do damage from within, or maybe it can throw you high into the air to bring a weapon attack down on an enemy; the only limit is your imagination! When fighting with your Rookling companion, think about what it is about your partnership that makes you skilled Rook hunters. Maybe you even have some special moves that you can do together due to a convenient combination of specialities!`,
            'trait prompts': ['Does your village or clan hate the Rooks, and did you have to keep your bond with a Rookling secret?',
            'Is your Rookling the core of a Rook that killed someone close to your character?',
            'Is your bond with your Rookling a reluctant one; does it follow, but you wish it didn’t? ',
            'Does your Rookling have something special about it? A strange crest or a hand that looks like a key?',
            'Think about your Rooklings shape, abilities and how it would fight in combat. With these things considered it will make it easier to come up with strategies in battle!']
        },

        'Helmed':{
            'exploration':2,
            'combat':5,
            'description':
                `The Helmed harvest a piece of strange machinery from the very core of a Rook and, using rituals and a real working understanding of the crystal patterns and stones, they are able to create a Helm that can be worn and operated, granting them the magical abilities of the Rook it was harvested from.`,
            'extended description':
                `The Helmed are the closest to wizards or alchemists in the world of Colostle. Understanding the magical properties of Rooks and how to harness them is partly a pursuit of arcane knowledge and also one of logic and crystal-engineering, like magical circuitry. Any human-made devices that use Rookstones, like lanterns or refrigeration chambers, are made by the Helmed, or someone who would be a great candidate for a Helm. This knack for Rook alchemy is rare and even if it manifests in someone, there is then the added challenge of defeating a Rook to obtain the part or parts usable to create a Helm. However, once done, unlike the Arm which requires attunement and a great toll on the body, the use of a Helm is purely operative, there is no attunement required. It is, however, complex and a deep understanding is required. The Helmeds skills are the most sought after in society. Manipulating and understanding the magical ‘technology’ of the Rooks allows people luxuries beyond the reach of human technology. This can mean one of two things for the Helmed, they are either venerated, or enslaved, depending on the nature of the person who comes across them. Others still consider the Helmed to be Rook sympathizers or ‘witches’. They are thought to be brainwashed with a Rooks thoughts infecting and affecting their own, as such they are often driven out of smaller settlements and distrusted in larger ones. Some religious zealots consider the use of the Rookstone magic to be heresy; consorting with the monsters that threaten everyday life for people. These people consider the Helmed to be the very worst heretics.`,
            'trait prompts': [
                'Has your character always had an understanding of Rooks since they were young? And if so, how did they first discover that?',
                'Does your character respect the Rooks, or simply see them as a source for scrap to tinker with?',
                'Is your character more comfortable in their workshop, dissecting and assembling, and is therefore reluctant to head out on a grand quest or journey?',
                'Is your character surrounded by brave warrior Armed or strategic ranger Followed, and feeling a need to prove their worth in their village or clan?',
                'Is your character driven to understand the mechanisms and technology of the Rooks and the Colostle as a whole?']
        },

        'Mounted':{
            'exploration':5,
            'combat':2,
            'description':
                `The Mounted ride an adapted mechanism taken from Rook parts, as a vehicle or mount to allow them easier traversal across the land and sea of the Colostle. Typically this involves taking a part of the Rook responsible for it’s locomotion and disconnecting it from the main body, and turning it into something that can be operated with crude controls, mechanisms and levers. The Mounted’s mounts can vary from horse-like creatures to boats and even bikes.`,
            'extended description':
                `Like the Helmed, the Mounted are gifted Rooksmiths, with a basic understanding of their functionality. But unlike the Helmed who have an understanding of the magical circuitry and therefore magical abilities of a Rook, the Mounted have a mechanical one. The Mounted are nomads and scavengers, constantly on the hunt for felled or ancient decaying Rooks and harvesting parts for their own mount. Partly to upgrade, and partly to just keep it going, as mounts require constant maintenance, like off-road vehicles. A Mounted’s mount is their heart and their life. Like looking after a bike or a beloved car, it is everything, it is their freedom. When you defeat a Rook or come across a husk out in the wilds, your character can take parts to upgrade or add to the functionality of your mount. This functions as a story opportunity for your character. Perhaps you took damage in your last battle and you take pieces from a fallen Rook to repair it. Maybe where once there were wheels, you attach legs in their place. Individual parts of Rooks seem to function on their own. If you remove a spinning wheel from the core of a Rook it will continue to spin on it’s own. If you take a leg mechanism; it will still have power despite being disconnected. This means any part that isn’t completely smashed to splinters can be made useful to a Mounted. Mounted are capable of battling Rooks and do so using the Mount’s built in Weapons (for example a cannon or a battering ram). In COMBAT, if you draw a WEAPON attack you can use your Mount’s weapon or one that your character carries in their hands. The Mounted have a low starting COMBAT score but as you explore more you will find ways to increase that score. Don’t see this as a limitation. Instead, it is a storytelling opportunity to have your character go on an adventure of growth.`,
            'trait prompts': [
                'Do you come from a village of Mounted, with buildings and encampments made of mechanical parts of Rooks? Being Mounted is in your blood?',
                'Come up with what your mount looks like and what Weapon it has on board to help defend you on your adventures.',
                'Perhaps your nomadic tribe is running out of Rook parts, your lands no longer as fertile for living and fallen Rooks as before. Maybe you must travel further afield to find new lands, rich in broken mechanical parts to scavenge. ',
                'Maybe your father is famous in the tribe for his mechanical adeptness and warrior’s spirit. You live in his shadow, keen to prove you have what it takes to carry on the family name.',
                'One day when scavenging a Rook husk you come across a part unlike any seen before. It could change how your mount functions dramatically. What would the others think if they saw it though, would they try to take it from you?']
        },

        'Allied':{
            'exploration':5,
            'combat':4,
            'description':
                `The Allied adventure out as a team but as Colostle is a solo RPG you as a player gain the ability to control two characters in the place of one. You can choose whether to play as both or just play as one and treat the other as a sort of non-playable companion. Its entirely up to you. This class is intended as a way to add more storytelling into your game for the more creatively ambitious, with a way to add character, dialogue,
                and developing relationships to your adventures.`,
            'extended description':
                `Some adventurers don’t start with the advantages of the other classes such as a powerful arm, a magical helm, a dedicated follower or a vehicle to ride and as such look to each other for the support to head out and explore the Roomlands. Allied start without a power-up like the other classes but gain the advantage of having another person who is by their side through thick and thin. Typically, Allied teams have a strong bond that leads them to want to do everything together, although there is nothing to say that this bond may be tested or even broken by what is yet to come. On their adventures, Allied characters may win arms, helms, Rooklings or mounts from their various battles or encounters and can equip them  to either character leading to an Allied being able to have a sort of multi-class effect. Most Roomlanders are solo creatures but by virtue of having two adventures so tightly bonded to each other, its possible to have one functioning as the melee fighter with an arm and one acting as support with a helm, for example. The combinations are endless.`,
            'trait prompts': [
                `Are your two characters bonded by blood (i.e. brother and sister) and in which case, do you have other siblings? Why are you leaving your family behind?`,
                `Are your two characters in a relationship that is not blood, perhaps a romantic one or a close friendship? Did you grow up in the same location or have you met out in the Roomlands?`,
                `Are your two characters thrust together in some way, perhaps unwillingly or by some sort of ritual? As a result, do they perhaps not get along but are forced to co-operate due to their goals or mission? Perhaps their relationship could change over time as they are forced to work together to survive, and maybe the reason for why they were brought together in the first place will become clear over time?`
            ]
        },

        'Bastion':{
            'exploration':2,
            'combat':4,
            'description':
                `The Bastions are a very recent and surprising discovery for the adventurers of the Colostle and as such they are not a common sight and are often viewed with fear or distrust. Bastions are the only person-sized stone/Rook constructs in the Colostle with most Rooks being much larger than a person and most Rooklings being smaller. Most notably, Bastions can speak and seem to be alive and sentient in the same way as people.`,
            'extended description':
                `Bastions originate from inside Colossal Rooks, the largest Rooks of all. Colossal Rooks are also incredibly rare. The general consensus is that thousands of years ago, there were more Colossal Rooks but now they are thought to be mostly extinct, with perhaps a few still roaming somewhere out there in the Roomlands. The Great City of Parapette was once a Colossal Rook, and it’s thought the fate of other Colossal Rooks are similar to Parapette’s, now husks containing cities or ancient dungeon corridors. Bastions are the ‘immune system’ of Colossal Rooks, defending the massive interior labyrinths of Colossal Rooks bodies from attacks by invaders. The Bastions of a Colossal Rook take on the characteristics of the Colossal Rook they live within, even down to looking like smaller, human sized versions of their colossal counterpart. They are a relatively new discovery for the people of the Colostle and due to looking exactly like the monsters that terrorise the homes and lands of Roomlanders, Bastions are not typically treated with much respect or kindness. Bastions are however capable of all the same feelings and emotions as a person, so they all have the same potential as any human Roomlander.`,
            'trait prompts': [
                `Does your character come from a place friendly to Bastions where they were accepted? Or are they living in a place where they are constantly abused and attacked just for who they are?`,
                `Does your Bastion want to trek out to find others of its kind and perhaps the Colossal Rook body they originated from, as they can’t remember their past?`,
                `Does your Bastion character come from a colony of other Bastions who have made their own colony or village to survive away from humans? And in which case what is that life like and why would they want to leave?`
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


    //TBA Jobs
 
/*****GENERAL*****/
    //Supplements:
    function pickClass(){
        return searchArray(Object.keys(characterClass))
    }
    let items = [
        "one valuable treasure",
        "a cache of supplies",
        "a critical piece of information",
        "a cache of materials to create a potion to heal one wound",
        "a mysterious key",
        "a salvagable vehicle",
        "a working vehicle",
        "a tame animal",
        "a potion",
        "an interesting machine part",
        "a revealing map",
        "a new weapon",
        "an intricate artifact",
        "an intricate idol",
        "two valuable treasures",
        "a rare and powerful artifact of unknown origin, said to hold immense magical capabilities.",
        "a set of ancient and enchanted armor, rumored to have been worn by a legendary hero of the Colostle.",
        "a legendary tome of spells and incantations, granting access to formidable arcane knowledge.",
        "a map detailing the secret passages and hidden chambers of the Colostle, invaluable for any explorer.",
        "a crystalline shard imbued with divine energy, capable of bestowing blessings or curses upon the wielder.",
        "a rare and precious gemstone, believed to be a fragment of a celestial body from beyond the Colostle.",
        "a collection of enchanted scrolls, each containing unique spells that can alter the fabric of reality.",
        "a vial of celestial water, said to grant visions of the future and glimpses into distant realms.",
        "an ancient and powerful artifact, capable of bending time and space within the Colostle's confines.",
        "a pair of mystical gauntlets, empowering the wearer with enhanced strength and magical abilities.",
        "a legendary weapon of immense power, rumored to have been forged by the gods themselves.",
        "a rare and exotic creature, kept as a companion by the most esteemed explorers of the Colostle.",
        "a set of ethereal wings, enabling the wearer to soar through the vast chambers of the Colostle.",
        "a relic of forgotten technology, possessing advanced capabilities far beyond current understanding.",
        "a collection of ancient coins or currency, once used in trade within the Colostle's bustling markets.",
        "a unique and powerful artifact that can manipulate the Colostle's architecture and structures.",
        "a puzzle box of intricate design, said to contain hidden knowledge or valuable treasures.",
        "a vial of mysterious and potent elixir, bestowing temporary enhancements to the drinker's abilities.",
        "a piece of celestial crystal, believed to have fallen from the heavens, radiating celestial energy.",
        "a legendary cloak or mantle, granting the wearer invisibility or the ability to phase through objects.",
        "a music box that plays a hauntingly beautiful melody, capable of soothing or enchanting those who listen.",
        "an ancient and sentient weapon, capable of communicating with its wielder and granting advice in battle.",
        "a set of enchanted runes or sigils, each holding a specific magical effect or power.",
        "a rare and exquisite piece of artwork or sculpture, believed to have been crafted by a master artist.",
        "a collection of rare and exotic spices, sought after by culinary connoisseurs within the Colostle.",
        "a mysterious crystal ball or scrying orb, allowing the user to glimpse distant places and events.",
        "a rare and magical gemstone, capable of absorbing and harnessing elemental energies.",
        "a piece of celestial technology, capable of manipulating gravity or other natural forces.",
        "a hidden room or chamber within the Colostle, filled with long-forgotten treasures and artifacts.",
        "an enchanted and ever-burning torch, providing an eternal source of light in the darkest corners of the Colostle.",
        "a rare and ancient piece of music or sheet music, believed to have the power to influence emotions and behavior.",
        "a legendary and sentient weapon, bonded with the soul of a fallen hero, seeking redemption through the wielder.",
        "a set of rare and enchanted armor, granting the wearer resistance to magical attacks and spells.",
        "a piece of celestial technology, believed to have the power to open portals to other dimensions.",
        "a rare and powerful gemstone, believed to grant visions of the past and future.",
        "one valuable treasure",
        "a cache of supplies",
        "a critical piece of information",
        "a cache of materials to create a potion to heal one wound",
        "a salvagable vehicle",
        "a working vehicle",
        "a tame animal",
        "a potion",
        "an interesting machine part",
        "a revealing map",
        "a new weapon",
        "an intricate artifact",
        "an intricate idol",
        "two valuable treasures",
        "a mystical and ever-burning lantern, illuminating the way through the darkest depths of the Colostle.",
        "an intricate and enigmatic puzzle, said to hold the secret to unlocking the Colostle's greatest mysteries.",
        "a rare and exotic creature, rumored to be the guardian of a hidden treasure or sacred artifact.",
        "a celestial artifact of mysterious origin, believed to hold the power to alter reality itself.",
        "an ancient and powerful relic, granting the wielder dominion over a specific element or force of nature.",
        "a set of celestial gloves or gauntlets, imbued with the power of the stars and capable of channeling cosmic energy.",
        "a unique and mystical mirror, capable of revealing hidden truths and illusions within the Colostle.",
        "a legendary and sentient weapon, capable of adapting its form and abilities to suit the wielder's needs.",
        "a rare and enchanted crystal, capable of storing and harnessing vast amounts of magical energy.",
        "a celestial staff or rod, believed to have once been wielded by a celestial being of great power.",
        "a collection of rare and exotic gems, prized by collectors and gemologists within the Colostle.",
        "an ancient and mysterious relic, rumored to have the power to awaken dormant Rooks to life.",
        "a set of celestial bracers or armlets, bestowing the wearer with enhanced magical prowess and protection.",
        "a rare and enchanted mirror, capable of reflecting the true nature and intentions of those who gaze upon it.",
        "a rare and ancient piece of artwork or sculpture, believed to be a representation of a long-forgotten deity.",
        "a set of enchanted and ever-sharp daggers or throwing knives, sought after by skilled assassins within the Colostle.",
        "an ancient and powerful artifact, capable of manipulating the flow of time within a localized area.",
        "a rare and exotic creature, believed to possess the ability to communicate with the Colostle's ancient spirits.",
        "a celestial artifact of immense power, believed to have once belonged to a long-lost celestial deity.",
        "a legendary and sentient weapon, said to have once been wielded by a celestial hero in a cosmic battle.",
        "a set of mystical and enchanted robes or garments, imbued with the power of the stars.",
        "a piece of celestial technology, believed to have the power to bend reality and create illusions.",
        "a rare and powerful relic, capable of harnessing the energy of the Colostle's celestial core.",
        "a set of ancient and enchanted gloves or gauntlets, said to grant the wearer the power of the Colostle's ancient spirits.",
        "a celestial artifact of mysterious and unknown purpose, sought after by scholars and collectors alike.",
        "a rare and exotic creature, believed to possess the ability to communicate with the Colostle's ancient spirits.",
        "an ancient and powerful relic, said to have once been forged by a celestial blacksmith in the heart of a dying star.",
        "a set of celestial bracers or armlets, imbued with the power of the cosmos and capable of channeling celestial energy.",
        "a legendary and sentient weapon, said to have once been wielded by a deity in a cosmic battle.",
        "a rare and enchanted crystal, capable of storing and harnessing vast amounts of magical energy.",
        "a celestial staff or rod, believed to be a conduit for cosmic energy and the power of the stars.",
        "a unique and enigmatic artifact, capable of granting the power of flight and levitation.",
        "a rare and powerful gemstone, believed to be a fragment of a long-lost celestial body.",
        "one valuable treasure",
        "a cache of supplies",
        "a critical piece of information",
        "a cache of materials to create a potion to heal one wound",
        "a mysterious key",
        "a salvagable vehicle",
        "a working vehicle",
        "a tame animal",
        "a potion",
        "an interesting machine part",
        "a revealing map",
        "a new weapon",
        "an intricate artifact",
        "an intricate idol",
        "two valuable treasures",
        "a set of celestial boots or shoes, granting the wearer the ability to traverse great distances in a single step.",
        "a mystical and ever-burning lantern, said to have been blessed by a celestial guardian.",
        "an ancient and mysterious relic, rumored to have the power to reveal the Colostle's greatest secrets.",
        "a rare and enchanted mirror, capable of reflecting the true nature of those who gaze upon it.",
        "an intricate and powerful artifact, said to have once been used by a legendary hero in battle.",
        "a set of celestial gloves or gauntlets, imbued with the power of the cosmos and capable of channeling celestial energy.",
        "a legendary and sentient weapon, possessing the knowledge and memories of its previous wielders.",
        "a rare and exquisite piece of jewelry, believed to have once adorned the crown of a long-lost king or queen.",
        "an ancient and powerful mask, said to grant the wearer the power to communicate with the Colostle's ancient spirits.",
        "a set of celestial wings, said to have been gifted by a celestial being as a reward for acts of heroism.",
        "a unique and enigmatic puzzle, believed to hold the key to unlocking the Colostle's greatest mysteries.",
        "a rare and exotic creature, said to possess the power to heal and cure ailments.",
        "a celestial artifact of immense power, capable of altering the fabric of reality.",
        "a legendary and sentient weapon, believed to be imbued with the essence of a long-lost civilization.",
        "a rare and powerful relic, capable of controlling and manipulating the elements within the Colostle.",
        "a set of ancient and enchanted boots or shoes, said to grant the wearer the ability to walk on air.",
        "a celestial artifact of mysterious origin, rumored to have the power to alter fate and destiny.",
        "a rare and enchanted crystal ball, capable of revealing glimpses of the past and future.",
        "a set of ethereal wings, said to have been crafted by celestial artisans and granted to a chosen few.",
        "a unique and powerful relic, capable of purifying or corrupting the Colostle's celestial core.",
        "a rare and ancient piece of artwork or sculpture, believed to be a depiction of a celestial being.",
        "a set of enchanted and ever-sharp swords or blades, sought after by skilled warriors within the Colostle.",
        "an ancient and powerful artifact, capable of manipulating the flow of time within the Colostle.",
        "a rare and exotic creature, said to possess the ability to communicate with the Colostle's ancient spirits.",
        "a celestial artifact of immense power, believed to have once belonged to a long-lost celestial deity.",
        "a legendary and sentient weapon, said to have once been wielded by a celestial hero in a cosmic battle.",
        "a set of mystical and enchanted robes or garments, imbued with the power of the stars.",
        "a piece of celestial technology, believed to have the power to bend reality and create illusions.",
        "a rare and powerful relic, capable of harnessing the energy of the Colostle's celestial core.",
        "one valuable treasure",
        "a cache of supplies",
        "a critical piece of information",
        "a cache of materials to create a potion to heal one wound",
        "a mysterious key",
        "a salvagable vehicle",
        "a working vehicle",
        "a tame animal",
        "a potion",
        "an interesting machine part",
        "a revealing map",
        "a new weapon",
        "an intricate artifact",
        "an intricate idol",
        "two valuable treasures",
        "a set of ancient and enchanted gloves or gauntlets, said to grant the wearer the power of the Colostle's ancient spirits.",
        "a celestial artifact of mysterious and unknown purpose, sought after by scholars and collectors alike.",
        "a rare and exotic creature, believed to possess the ability to communicate with the Colostle's ancient spirits.",
        "an ancient and powerful relic, said to have once been forged by a celestial blacksmith in the heart of a dying star.",
        "a set of celestial bracers or armlets, imbued with the power of the cosmos and capable of channeling celestial energy.",
        "a legendary and sentient weapon, said to have once been wielded by a deity in a cosmic battle.",
        "a rare and enchanted crystal, capable of storing and harnessing vast amounts of magical energy.",
        "a celestial staff or rod, believed to be a conduit for cosmic energy and the power of the stars.",
        "a unique and enigmatic artifact, capable of granting the power of flight and levitation.",
        "a rare and powerful gemstone, believed to be a fragment of a long-lost celestial body.",
        "a set of celestial boots or shoes, granting the wearer the ability to traverse great distances in a single step.",
        "a mystical and ever-burning lantern, said to have been blessed by a celestial guardian.",
        "an ancient and mysterious relic, rumored to have the power to reveal the Colostle's greatest secrets.",
        "a rare and enchanted mirror, capable of reflecting the true nature of those who gaze upon it.",
        "an intricate and powerful artifact, said to have once been used by a legendary hero in battle.",
        "a set of celestial gloves or gauntlets, imbued with the power of the cosmos and capable of channeling celestial energy.",
        "a legendary and sentient weapon, possessing the knowledge and memories of its previous wielders.",
        "a rare and exquisite piece of jewelry, believed to have once adorned the crown of a long-lost king or queen.",
        "an ancient and powerful mask, said to grant the wearer the power to communicate with the Colostle's ancient spirits.",
        "a set of celestial wings, said to have been gifted by a celestial being as a reward for acts of heroism.",
        "a unique and enigmatic puzzle, believed to hold the key to unlocking the Colostle's greatest mysteries.",
        "a rare and exotic creature, said to possess the power to heal and cure ailments.",
        "a celestial artifact of immense power, capable of altering the fabric of reality.",
        "one valuable treasure",
        "a cache of supplies",
        "a critical piece of information",
        "a cache of materials to create a potion to heal one wound",
        "a mysterious key",
        "a salvagable vehicle",
        "a working vehicle",
        "a tame animal",
        "a potion",
        "an interesting machine part",
        "a revealing map",
        "a new weapon",
        "an intricate artifact",
        "an intricate idol",
        "two valuable treasures"
    ]
    let situations = [
        'you meet a friend.',
        'a storm rolls in.',
        'something falls from the `ceiling`.',
        'you fall.',
        'a loud noise can be heard.',
        'a strange feeling comes over you.',
        'the sun sets or rises.',
        'a fire breaks out.',
        'something breaks.',
        'your way is blocked.',
        'you are surrounded.',
        'hunger sets in.',
        'you create or repair something.',
        'a powerful earthquake shakes the ground beneath you, causing nearby rooks to awaken from their slumber.',
        'a celestial event bathes the landscape in an otherworldly glow, awakening ancient rooks from their dormant state.',
        'you stumble upon an ancient and forgotten rook nest, guarded fiercely by stone guardians.',
        'a mischievous rook construct steals a valuable item from you, tauntingly evading your pursuit.',
        'a group of rook constructs are engaged in an ominous and ancient ritual, their stone bodies pulsing with energy.',
        'an enigmatic rook construct with glowing markings approaches you, seemingly seeking to confront intruders.',
        'a legendary rook construct, rumored to possess the power of foresight, blocks your path and issues a warning.',
        'you encounter a lost and damaged rook construct, sparking a debate between your companions on whether to help or avoid it.',
        'a band of rook hunters is spotted nearby, equipped with powerful machinery to dismantle the stone constructs.',
        'a traveling merchant offers to sell you a map leading to a hidden rook sanctuary, warning of the danger ahead.',
        'you find a peculiar stone with ancient rook markings that temporarily grants you limited control over nearby constructs.',
        'a reclusive rook sage living in the wilderness claims to have a secret method to temporarily appease rook constructs.',
        'a rival group of adventurers competes with you to collect valuable and rare rook crystals for a grand prize.',
        'a rook guardian challenges you to a trial of wit and strength to prove your worthiness in the rook-controlled territory.',
        'a benevolent rook construct allows you to pass unharmed after you solve a complex puzzle.',
        'you create or repair something.',
        'you encounter a rook of illusions, capable of creating mesmerizing and bewildering stone mirages.',
        'a legendary rook relic is rumored to be hidden in a treacherous cave, protected by deadly traps.',
        'you uncover an ancient rook artifact that temporarily grants you resistance to the constructs’ attacks.',
        'a powerful rook guardian with the ability to manipulate stone and earth offers to guide you through a dangerous terrain.',
        'you come across an enigmatic rook hermit who challenges you to solve a riddle in exchange for safe passage.',
        'a village is under attack by rogue rook constructs controlled by a malevolent sorcerer seeking to destroy human settlements.',
        'you uncover a secret ritual that allows temporary transformation into a rook-like creature to blend in with the constructs.',
        `a legendary rook elder offers to share ancient knowledge of the constructs' origins and weaknesses.`,
        'you encounter a peculiar rook with the ability to foresee danger, offering cryptic warnings.',
        'a group of children from a nearby village claims to have witnessed rook constructs displaying mysterious behavior.',
        'a reclusive rook engineer invites you to witness their mesmerizing and elaborate mechanical performance.',
        'you discover a hidden sanctuary where rooks are revered as symbols of danger and power.',
        'a sacred ceremony is being held by a group of indigenous people to appease the rook constructs and prevent their attacks.',
        'a peculiar rook relic reveals visions of an ancient civilization that controlled the stone constructs.',
        'you stumble upon a gathering of rook constructs exhibiting extraordinary and unexplained phenomena.',
        'you create or repair something.',
        'a mischievous rook construct takes an interest in your belongings, playfully taunting you as it keeps its distance.',
        'a mysterious rook guardian challenges you to an elemental trial to test your resilience against the constructs.',
        'you witness an awe-inspiring aerial dance performed by a group of synchronized rook constructs at dusk.',
        'a rook with the power of empathy seeks your assistance in resolving a dispute among the constructs.',
        'you find yourself in a sacred rook territory where humans are forbidden to tread without permission.',
        'a legendary rook sage imparts ancient knowledge and techniques to temporarily evade the constructs.',
        'you create or repair something.',
      ];

    let foundMachinery = [
        "The machinery can amplify a person's magical abilities, allowing them to cast spells far more potent than their usual capabilities.",
        "When activated, the machinery emits a powerful, mesmerizing light that can temporarily blind or confuse enemies.",
        "The machinery can manipulate nearby stone constructs, causing them to move or even temporarily come to life to aid the wielder.",
        "When activated, the machinery emits a harmonious melody that soothes and pacifies any hostile stone constructs in the vicinity.",
        "The machinery can create a temporary force field, providing protection against magical attacks and physical harm.",
        "When powered on, the machinery allows the user to communicate telepathically with nearby stone constructs.",
        "The machinery has the ability to temporarily turn the wielder invisible, allowing for stealthy reconnaissance or escape.",
        "When activated, the machinery alters the user's voice, allowing them to mimic the sounds of different creatures or even other individuals.",
        "The machinery has the ability to manipulate nearby magnetic fields, allowing the wielder to control nearby metallic objects.",
        "When activated, the machinery creates a pocket of altered time, slowing down or speeding up events in a localized area.",
        "The machinery can summon a temporary sandstorm or whirlwind, causing chaos and confusion among opponents.",
        "When powered on, the machinery releases a burst of energy that temporarily disrupts magical spells and enchantments in the area.",
        "The machinery can create lifelike illusions, confusing enemies and leading them astray.",
        "When activated, the machinery grants the wielder the ability to temporarily control and animate nearby vegetation, creating living barriers or attacking opponents.",
        "The machinery can generate temporary elemental barriers, protecting against fire, ice, or other elemental attacks.",
        "When powered on, the machinery creates an invisible tether between the wielder and nearby stone constructs, allowing for remote control.",
        "The machinery can temporarily transform the wielder into a stone-like being, granting enhanced strength and durability.",
        "When activated, the machinery creates a field of silence, nullifying all sound within its radius and making the area eerily quiet.",
        "The machinery can create temporary portals, allowing the wielder to traverse great distances instantly.",
        "When powered on, the machinery generates a temporary gravity-defying field, allowing the wielder to walk on walls or ceilings.",
        "The machinery can create a burst of vibrant colors and patterns, temporarily mesmerizing and captivating onlookers.",
        "When activated, the machinery emits a wave of healing energy, rejuvenating and revitalizing the wielder and nearby allies.",
        "The machinery can project holographic images, creating complex illusions to deceive or entertain.",
        "When powered on, the machinery creates a zone of heightened agility, allowing the wielder to move with incredible speed and reflexes.",
        "The machinery can generate a temporary weather phenomenon, summoning rain, hail, or lightning at the wielder's command.",
        "When activated, the machinery creates a powerful gust of wind, capable of pushing back opponents or lifting objects into the air.",
        "The machinery can create a localized earthquake, shaking the ground and causing chaos among enemies in its range.",
        "When powered on, the machinery creates an aura of calmness and serenity, pacifying aggressive creatures and promoting peaceful interactions.",
        "The machinery can temporarily manipulate the density of the air, allowing the wielder to create zones of extreme pressure or vacuum.",
        "When activated, the machinery creates an illusionary duplicate of the wielder, confusing enemies and providing a decoy for tactical advantage.",
        "The machinery can temporarily enhance the wielder's senses, granting heightened vision, hearing, or smell.",
        "When powered on, the machinery creates a barrier of light that repels dark and shadowy creatures.",
        "The machinery can temporarily merge with nearby stone constructs, granting the wielder enhanced control over their movements and abilities.",
        "When activated, the machinery projects a protective dome, shielding the wielder and allies from external magical influences.",
        "The machinery can create a temporal distortion, allowing the wielder to briefly glimpse possible future events.",
        "When powered on, the machinery emits a pulse of energy that temporarily disrupts technological devices and mechanisms.",
        "The machinery can generate a temporary blinding flash of light, disorienting foes and giving the wielder an advantage in combat.",
        "When activated, the machinery creates an energy-absorbing barrier, neutralizing incoming magical attacks.",
        "The machinery can temporarily transform the wielder into a spectral form, granting intangibility and ethereal movement.",
        "When powered on, the machinery releases a burst of healing energy, mending wounds and rejuvenating the wielder and companions.",
        "The machinery can project a psychic shield, protecting the wielder's mind from mental intrusion or manipulation.",
        "When activated, the machinery creates a zone of heightened intelligence and insight, enhancing the wielder's problem-solving abilities.",
        "The machinery can generate a temporary distortion in space, causing objects or foes to shrink or expand.",
        "When powered on, the machinery creates a time-loop effect, allowing the wielder to redo a short period of time.",
        "The machinery can temporarily imbue the wielder's weapons or attacks with elemental energy, enhancing their potency.",
        "When activated, the machinery creates a barrier that dampens or nullifies the effects of magic within its vicinity.",
        "The machinery can generate a temporary ethereal bridge, allowing the wielder to traverse gaps or chasms.",
        "When powered on, the machinery emits a pulsating energy field that repels hostile magical creatures.",
        "The machinery can temporarily create a cloak of shadows, concealing the wielder from sight and granting enhanced stealth.",
        "When activated, the machinery creates a burst of energy that disrupts time perception, making foes slow or sluggish.",
        "The machinery can generate a temporary sphere of tranquility, calming aggressive or agitated beings within its range.",
        "When powered on, the machinery creates a magnetic surge, attracting or repelling metallic objects and foes.",
        "The machinery can temporarily project a psychic blast, overwhelming the minds of nearby adversaries.",
        "When activated, the machinery creates an illusion of the wielder's choice, fooling enemies or creating diversions.",
        "The machinery can generate a temporary energy barrier, absorbing and redirecting incoming magical attacks.",
        "When powered on, the machinery creates a zone of pure darkness, obscuring vision and granting the wielder night vision.",
        "The machinery can temporarily bestow the wielder with the ability to communicate with and understand stone constructs.",
        "When activated, the machinery creates a zone of heightened strength, allowing the wielder to lift heavy objects with ease.",
        "The machinery can generate a temporary telekinetic field, allowing the wielder to move objects with the power of their mind.",
        "When powered on, the machinery emits a wave of inspiration, enhancing the artistic or creative abilities of nearby individuals.",
        "The machinery can temporarily create a reflective barrier, bouncing back magical attacks at their source.",
        "When activated, the machinery creates a zone of accelerated healing, aiding in the recovery of injuries for those within its radius.",
        "The machinery can generate a temporary burst of sonic waves, disorienting and stunning opponents.",
        "When powered on, the machinery creates an energy net that immobilizes or restricts the movement of nearby foes.",
        "The machinery can temporarily create a zone of electrical disruption, interfering with magical or technological devices.",
        "When activated, the machinery creates a protective shield that grants immunity to specific elemental attacks.",
        "The machinery can generate a temporary zone of time distortion, aging or de-aging objects or beings within its range.",
        "When powered on, the machinery emits a pulse of energy that disrupts the flow of magic in the area, rendering spells less effective.",
        "The machinery can temporarily grant the wielder the ability to levitate or fly through the air.",
        "When activated, the machinery creates an energy vortex, drawing in and trapping nearby opponents.",
        "The machinery can generate a temporary seismic shockwave, causing the ground to tremble and destabilize foes.",
        "When powered on, the machinery emits a wave of tranquility, calming and soothing aggressive or agitated creatures.",
        "The machinery can temporarily alter the ambient temperature, creating areas of intense cold or heat.",
        "When activated, the machinery creates a zone of heightened intuition, granting the wielder enhanced instincts and foresight.",
        "The machinery can generate a temporary wave of telepathic interference, disrupting mental communication in its vicinity.",
        "When powered on, the machinery emits a pulse of energy that temporarily enhances the physical attributes of nearby allies.",
        "The machinery can temporarily create a zone of heightened charisma, influencing the thoughts and emotions of those nearby.",
        "When activated, the machinery creates a barrier of energy that repels physical projectiles and attacks.",
        "The machinery can generate a temporary zone of gravitation manipulation, altering the weight or movement of objects or beings within its range."
    ]

    //Exploration    
    let generalEvents = [
        [
            `${searchArray(['An armed','An unarmed'])} stranger in unusual robes with a castle symbol on them. Perhaps ${searchArray(['he','she'])} has clues about the nature of the Colostle, but these strangers are often unwilling to even be found, let alone be spoken to. You’ve heard tell of them before - a cult maybe? People don’t talk about them kindly; strangers with strange practices... but they definitely know something. If you fight them, create a human opponent in your COMBAT phase.`,
            `An Animal to hunt for food. This animal is ${searchArray(['easy prey','dangerous'])} The animals in the wilds are strange and unfamiliar; weird combinations of animals you might know, a boar with scales, or a fowl with 2 sets of wings. Adventuring is hungry work, you should make time to eat.`,
            `CALLING - You come across ${searchArray(['a friendly','an unfriendly'])} ${searchArray(['man','woman','boy','girl'])}  who is key to your CALLING. Maybe they have a clue about what you’re looking for, or they block your way to learning more...`,
            `${searchArray(['A trustworthy','An untrustworthy'])} ${searchArray(['man','woman','boy','girl'])} you meet asks you to find something for them. Maybe they have lost something, or they are too afraid to get it. They will reward you with a ${searchArray(items)} if you do this for them. Use the other cards drawn in this EXPLORATION phase to inform where you might need to go. If you fight them, create a human opponent in your COMBAT phase.`,
            `A dead body of a ${searchArray(['man','woman','boy','girl'])}. Who are they? What are they wearing? ${searchArray([`Things seem safe, and if the body is searched you find a ${searchArray(items)}`,`Something seems off, and if you stick around too long, ${searchArray(situations)}`])}`,
            `Another adventurer like yourself, they seem ${searchArray(['friendly','unfriendly'])}, and are garbed in Rook Armour and seem to be a ${pickClass()}. But what do they want? Are they here to help you take down a Rook? If so what do they want in return? Or are their intentions darker? If you fight them, create a human opponent in your COMBAT phase.`,
            `A screech from the sky, the beat of heavy wings... gargoyles. You thought they were just stories you were told as a child. Apparently not! It grabs you by the shoulders and starts to carry you upward. ${searchArray(['It takes you to a whole new area.','It takes you up to its nest in the rafters of the ceiling. There is no fighting a Gargoyle...'])}`,
            `You come across a small settlement, maybe a farming village, the buildings are all wooden and skins, like most small settlements. ${searchArray([`${searchArray(items)} can be found here.`, `While you are here, ${searchArray(situations)}`])}`,
            `A massive skeleton. ‘It looks humanoid. But it can’t be, can it?’ ${searchArray('Getting closer you can see that it is safe',`${searchArray([`You go unnoticed despite finding out it is a bandit camp.`,'You get close enough to see it is bandit camp, just when you realize that, you are captured.'])} It’s a camp of people. At least, they look like people; they walk on 2 legs and carry tools in 2 arms, but they’re not.... human. Who are they? What do they want?`)}`,
            `You found ${searchArray(items)}!`,
            `You found A Medium Rook!`,
            `You found A Massive Rook!`,
            "An unusual phenomenon occurs, causing strange lights and sounds. It might be a natural occurrence, but you can't shake the feeling that it's something more.",
            "A mysterious inscription carved into a stone pillar, wall, or the floor. It seems to hint at hidden secrets or a path to untold knowledge.",
            `A group of nomadic traders passing through the area. They offer to trade their exotic wares, some of which might have unique properties or magical abilities.`,
            "A natural spring with water that glows faintly in the dark. Drinking from it seems to invigorate and heal your wounds.",
            `An ancient statue or monument with engravings depicting events from the distant past. Perhaps deciphering these engravings could reveal lost history or clues about the Colostle.`,
            `A portal shimmering with magical energy. It could lead to a different room within the Colostle, presenting an opportunity to explore new territories.`,
            "A group of adventurers embarking on their own quest. You can join forces, exchange information, or compete for resources.",
            "A strange phenomenon occurs, where gravity seems to shift, causing objects and people to float momentarily.",
            "An abandoned campsite with signs that someone left in a hurry. Investigating further might lead to discovering what scared them off.",
            `A pack of ${searchArray(['friendly','aggressive'])} rooklings. These young Rooks might playfully interact with you or pose a threat if provoked.`,
            "A peculiar tree with glowing fruit that seems to grant enhanced abilities when consumed.",
            "A group of Rooks engaged in a mysterious ritual. Observing their behavior might offer insight into their nature and purpose.",
            "A trapped room that closes in on you, forcing you to solve a mechanical puzzle to escape.",
            "An underground passage or tunnel leading to unknown depths within the Colostle.",
            `A spectral figure that seems to be a guardian spirit of the Colostle. Interacting with it could lead to guidance or protection.`,
            "A collection of ancient books or scrolls containing forgotten knowledge about the Colostle and its origins.",
            `You found ${searchArray(items)}!`,
            `You found A Medium Rook!`,
            `You found A Massive Rook!`,    
            "A mesmerizing painting or mural that seems to come alive with motion and sound, telling a story or providing clues to hidden secrets.",
            "A group of pilgrims on a spiritual journey, seeking enlightenment within the vast confines of the Colostle.",
            "A secret gathering of rebels or dissidents plotting to challenge the ruling power within the Colostle.",
            "A rare and exotic plant or flower with magical properties, sought after by alchemists and potion-makers.",
            "A seemingly infinite library filled with countless books, each holding a piece of lost or forbidden knowledge.",
            "A stone construct hidden among the surroundings, motionless and seemingly harmless until provoked.",
            "An enigmatic hermit living in seclusion within the Colostle, possessing wisdom and knowledge beyond their years.",
            "A series of interconnected waterways or underground rivers that lead to unexplored regions of the Colostle.",
            "A haunting melody emanating from an old, rusted music box or instrument, said to have the power to alter one's fate.",
            "A gathering of ethereal spirits, whispering cryptic messages and prophecies to those who dare to listen.",
            "An ancient battlefield, frozen in time, where the echoes of past conflicts can still be felt.",
            "A mysterious gate or portal that requires a specific key or magical item to unlock its secrets.",
            "A celestial event, such as a rare alignment of stars or a meteor shower, believed to hold significance in the Colostle's history and future.",
            "A vibrant and bustling marketplace, attracting traders from all corners of the Colostle, offering unique goods and services.",
            "A hidden sanctuary or shrine dedicated to an enigmatic deity or entity, drawing pilgrims seeking blessings or answers.",
            "A remote cave containing a dormant Rook that has become a haven for curious explorers and thrill-seekers.",
            "An underground cavern filled with luminescent crystals that emit a soft glow, creating a mesmerizing spectacle.",
            "A forgotten theater or performance hall, where echoes of long-lost performances can still be heard and felt.",
            "A vast and ancient library, said to hold the collective knowledge of every civilization that ever resided in the Colostle.",
            "A hidden chamber filled with intricate mechanical devices, left behind by an enigmatic inventor from ages past.",
            `You found ${searchArray(items)}!`,
            `You found A Medium Rook!`,
            `You found A Massive Rook!`,   
        ],
        [
            `A large treasure. Maybe a chest or a valuable golden object, perched atop an altar, ${searchArray(['it seems completely untouched','there is evidence of attempted raids'])}. Whatever it is, it fills you with hope for your adventure. Add 1 point to either your EXPLORATION or COMBAT scores and come up with a unique item for your inventory.`,
            `A door. No ordinary door - a door between Rooms in the Colostle; it’s impossible, huge beyond imagining, disappearing upward into the sky. If you hadn’t seen it from a distance, you’d have thought it was just another wall. ${searchArray(['The door is ruined, you may be able to slip through a gap',`it is ${searchArray(['intact but unlocked, so you might have to find a mechanism to open it', 'intact and locked, so you might have to find a mechanism to unlock it, and then open it.'])}`])}`,
            `${searchArray(['An intact','A ruined'])} staircase leading to another floor in the Colostle. Massive - and a quest in itself to climb - it vanishes into mist and clouds. Each step is the height of a small house - who could have possibly built this? If this is not the first staircase you have come across, you can consult the BATTLEMENTS module to take you to the Colostle Rooftops. If it is the first staircase you have found, it takes you to another floor of the Colostle.`,
            `Ruins, ${searchArray(['somewhat intact','mostly rubble'])}, of a people you’ve never heard of. The unfamiliar inscriptions and architecture suggest these people lived a very long time ago. While you are here, ${searchArray(situations)}`,
            `A great, strange mechanism that seems to operate something in the Colostle. Pipes, gearwheels and levers; it seems oversized but you think you can operate it. ${searchArray(['It seems functional','It seems damaged,  maybe you need to find something to repair it?'])}`,
            `A trap! ${searchArray(['You avoid it!','You are caught in it!'])} Maybe a hunters trap, or a pit, or some old machinery. What do you do now?`,
            `A cave entrance. A darkness beckons beyond. Could it lead to deeper parts of the Colostle itself? ${searchArray(['It is flat and easily navigable.','It looks deep and hard to climb into.'])}`,
            `The sea. A huge expanse of water stretches out before you ${searchArray([', serene and welcoming',', stormy and tempestuous'])}. You stand on a rocky coast, or a beach, looking out. The water stretches to the horizon but beyond it you can see the tell-tale columns and ceiling supports of the Colostle; it’s all still within a room. If you don’t want to use the expansion module, consider this a coastal region of cliffs and beaches. Otherwise, consult the OCEANS module to explore the SEA!`,
            `CALLING - You come across a place that is key to your CALLING. ${searchArray(['You find a building with a clue in it!','You find one of the locations you were looking for on your quest!'])}`,
            `You come across ${searchArray(['a thriving city; here you see motorised vehicles and mechanisms seemingly on every corner, and best of all, shops, culture, and hunters; a place of commerce, trade and meeting!','an abandoned city. It was either destroyed or the people left, all that remains is the overgrown bones of a once large community and the rook corpses used to defend it.'])}`,
            `You found ${searchArray(items)}!`,
            `You found A Medium Rook!`,
            `You found A Massive Rook!`,
            "A mysterious altar with strange symbols and markings, hinting at a forgotten civilization or deity.",
            "A hidden chamber behind a false wall, concealing valuable artifacts or knowledge.",
            "A large mechanical device that can be activated with the right combination of levers and switches.",
            "A deep chasm or abyss that seems to descend endlessly into the depths of the Colostle.",
            "A hidden cache of ancient weapons or powerful relics left behind by legendary heroes.",
            "A mystical portal that leads to a different dimension or plane of existence.",
            "An ancient observatory with telescopes and celestial charts, offering insights into the Colostle's cosmic mysteries.",
            "A forgotten laboratory filled with alchemical experiments and strange concoctions.",
            "A sentient, talking statue that imparts cryptic riddles or valuable knowledge to those who listen.",
            "A network of underground tunnels and catacombs, believed to hold the secrets of the Colostle's past.",
            `You found ${searchArray(items)}!`,
            `You found A Medium Rook!`,
            `You found A Massive Rook!`,
            "A beautiful garden with vibrant and exotic flora, seemingly thriving in the confined space of the Colostle.",
            "An otherworldly phenomenon, such as floating islands or levitating structures, defying the laws of gravity.",
            "A mysterious mist that shrouds the area, concealing hidden passages and secrets within the Colostle.",
            "A natural hot spring with healing properties, providing a moment of relaxation and rejuvenation for weary adventurers.",
            "A lush forest growing within the confines of a large chamber, teeming with magical creatures and ancient spirits.",
            "A breathtaking waterfall cascading from the Colostle's walls into a crystal-clear pool below.",
            "A magnificent sculpture or statue, seemingly sculpted by a master artist, radiating an aura of power and mystery.",
            "A colorful and enchanting display of bioluminescent plants, illuminating the darkness of the Colostle with an ethereal glow.",
            "A serene and tranquil lake, mirroring the grandeur of the Colostle's architecture, inviting contemplation and introspection.",
            "A massive chandelier or intricate light fixture, suspended from the ceiling, providing an enchanting display of light and shadows.",
            "An underground river or stream, winding through the Colostle's chambers, with its source and destination shrouded in mystery.",
            "A grand hall with ancient paintings and tapestries, depicting the history and legends of the Colostle.",
            `You found ${searchArray(items)}!`,
            `You found A Medium Rook!`,
            `You found A Massive Rook!`,
            "An awe-inspiring astronomical event, such as a meteor shower or comet passing through the Colostle's celestial chambers.",
            "A room filled with crystalline formations that emit a soft and harmonious hum, creating an otherworldly ambience.",
            "A surreal and dreamlike landscape, where the laws of physics seem to bend and reality is distorted.",
            "A captivating performance, whether musical or theatrical, by a group of talented entertainers within the Colostle.",
            "A celestial balcony or observation point, offering a breathtaking view of the stars and galaxies beyond the Colostle.",
            "A mysterious phenomenon that alters the perception of time, making moments feel like hours or hours feel like moments.",
            "A hidden glade or grove, where nature thrives despite the artificial confines of the Colostle.",
            "An intricate and elaborate maze or labyrinth, challenging adventurers to find their way through its twisting passages.",
            "A magical light show, caused by the interplay of reflective surfaces and ethereal energy within the Colostle.",
            "An area covered in phosphorescent fungi, casting an eerie and enchanting glow in the darkness.",
            "An ancient observatory with telescopes and celestial charts, offering insights into the Colostle's cosmic mysteries.",
            "A forgotten laboratory filled with alchemical experiments and strange concoctions.",
            "A sentient, talking statue that imparts cryptic riddles or valuable knowledge to those who listen.",
            "A network of underground tunnels and catacombs, believed to hold the secrets of the Colostle's past.",
            `You found ${searchArray(items)}!`,
            `You found A Medium Rook!`,
            `You found A Massive Rook!`,
        ]
    ]
    function generalExploration(){
        if (rollDice(100) > 50){
            return searchArray(generalEvents[0])
        } else {
            return searchArray(generalEvents[1])
        }
    }

/*****OCEAN*****/
    //Supplements
    let weather = [
        `SUNSHINE - Add one to your EXPLORATION or COMBAT score.`,
        `STRONG WINDS - a good wind takes your boat where you want to go, quickly.`,
        `FOG - Visibility is reduced to 2 feet in front of you. It is unnervingly quiet.`,
        `HEAVY RAIN - No shelter, it pelts against your skin. You’ll just have to sail on.`,
        `CALM - no winds, baking heat. You will be stuck in the middle of the sea with no way to move for 24 hours.`,
        `CROSSWIND - You are blown off course and are lost at sea for 24 hours.`,
        `SNOW - Small flakes settle on your boat, this is going to get cold...`,
        `WATERSPOUT - A column of water twirling with wind, it's heading toward you!`,
        `STORM - Your boat is tossed by huge waves and heavy winds.`,
        `LIGHTNING - Forks of lightning light up the sky, the sea churns with malice.`,
        `ICE - The ocean freezes instantly around your boat. You are stuck for 24 hours.`,
        `TSUNAMI - A huge wave looms above your boat. Can you ride it out or will it smash your boat to pieces?`,
        `MAELSTROM - your boat is damaged and you wake up stranded on a new island. Return to base book Encounter tables for your next EXPLORATION Phase.`
    ]
    //Exploration
    let oceanEvents = [
                `A single castle tower sticks up out of the water, waves splashing around where it connects with the sea.${searchArray(['It seems uninhabited.','You hear voices from deep within.'])} There is a doorway that is accessible from the height of the sea, and when you look down into the interior you are stunned to see that it goes deep down into an underwater complex, completely airtight from the sea around it. WEATHER: ${searchArray(weather)}.`,
                `Another seagoing adventurer in their own vessel. ${searchArray(['They seem friendly.','They seem unfriendly.'])} WEATHER: ${searchArray(weather)}`,
                `Shipwreck. You pull up alongside the ${searchArray([`mostly intact vessel and find ${searchArray(items)} and ${searchArray(items)}`,`the completeley wrecked vessel and find ${searchArray(items)} floating among the debris`])}`,
                `An island with the tell-tale crenellations of a castle around its perimeter. Could it be that you are seeing just the very top of a huge Rook below the waves? ${searchArray(['The rook is dead.',`the rook's traps are still active!`])}`,
                `A huge seagoing creature is swimming just below the surface. Maybe its leading you somewhere, maybe you could hunt it for food? ${searchArray(['It swims past your vessel with no issue.','It hits your vessel as it passes!'])} WEATHER: ${searchArray(weather)}`,
                `Sea cave, large enough for your vessel to enter. It’s huge, cavernous within, like an underground river leading from one cavern to the next. ${searchArray([`It is inhabited and the ${searchArray(['friendly','unfriendly'])} creatures you meet are not human`, `It is uninhabited and you find ${searchArray(items)}`])}`,
                `A pirate ship! The pirates lasso your ship and bring you aboard. This is not a time to fight - you must sneak out and escape the pirate ship! Tell your story of how you navigate the halls and decks of the pirate ship and ${searchArray([`how you find the treasure`,`how you find the weapon`])} that you take back with you.`,
                `Shallow waters and underwater ruins. If the weather is good, you could drop anchor and swim down to investigate...${searchArray(['Finding rook parts','finding treasure'])} should you be able to venture into the deeps.`,
                `A small island. ${generalExploration()}. That is all there is to find here, return to the SEA to continue. WEATHER: ${searchArray(weather)}`,
                `A coastline. If you decide to disembark here then return to the base rulebook for ongoing EXPLORATION phases. WEATHER: ${searchArray(weather)}`,
                `You found an island with ${searchArray(items)}!`,
                `You found A Medium Rook!`,
                `You found A Massive Rook!`,
                `A massive whirlpool is forming in the distance. You must navigate your vessel carefully to avoid being pulled into its deadly grasp. WEATHER: ${searchArray(weather)}`,
                `A group of friendly sea creatures are playfully swimming alongside your vessel. Interacting with them might bring good fortune. WEATHER: ${searchArray(weather)}`,
                `An eerie silence falls over the ocean. No waves, no wind - it feels unsettling. You can't shake the feeling that something is watching you. WEATHER: ${searchArray(weather)}`,
                `An abandoned sea fortress stands on a small island. Exploring it might yield valuable information or items. WEATHER: ${searchArray(weather)}`,
                `A sudden dense fog surrounds your vessel, making navigation challenging and disorienting. WEATHER: ${searchArray(weather)}`,
                `A ghost ship emerges from the mist, its tattered sails billowing in the wind. Beware, for it is said to bring bad luck to those who encounter it. WEATHER: ${searchArray(weather)}`,
                `A mysterious underwater cave system with bioluminescent plants illuminating the way. WEATHER: ${searchArray(weather)}`,
                `A floating marketplace where merchants from different realms gather to trade exotic goods. WEATHER: ${searchArray(weather)}`,
                `A massive coral reef teeming with colorful marine life. Exploring it could lead to valuable discoveries. WEATHER: ${searchArray(weather)}`,
                `A deep-sea trench, its depths shrouded in darkness and mystery. You might find ancient artifacts or encounter dangerous creatures. WEATHER: ${searchArray(weather)}`,
                `A pod of majestic sea creatures, like giant turtles or whales, swimming alongside your vessel. Observing them can be a humbling experience. WEATHER: ${searchArray(weather)}`,
                `An underwater geyser erupts, propelling your vessel high into the air. You must quickly regain control before crashing back into the sea. WEATHER: ${searchArray(weather)}`,
                `A distant island with a towering lighthouse, its light sweeping the ocean surface. It could lead you to safety or guide you toward danger. WEATHER: ${searchArray(weather)}`,
                `A massive floating tree or cluster of seaweed that can be explored for valuable treasures. WEATHER: ${searchArray(weather)}`,
                `You found an island with ${searchArray(items)}!`,
                `You found A Medium Rook!`,
                `You found A Massive Rook!`,
                `A mysterious glowing light emanates from beneath the water's surface. Investigating it might lead to an ancient artifact or valuable treasure. WEATHER: ${searchArray(weather)}`,
                `A seaquake rocks your vessel, causing damage and throwing off your navigation. You must make repairs before continuing. WEATHER: ${searchArray(weather)}`,
                `A massive tentacled creature emerges from the depths, its presence sending shivers down your spine. Do you flee or attempt to confront it? WEATHER: ${searchArray(weather)}`,
                `A group of friendly merfolk rise out of the water, offering to trade rare underwater materials for some of your supplies. WEATHER: ${searchArray(weather)}`,
                `A sea shanty can be heard in the distance, sung by haunting voices. Following the song might lead you to a hidden island or a mysterious event. WEATHER: ${searchArray(weather)}`,
                `An underwater volcanic eruption creates a temporary island of molten rock and magma. It could be a unique opportunity to find rare materials or powerful relics. WEATHER: ${searchArray(weather)}`,
                `A vast whirlpool pulls your vessel toward its center. Escaping its grasp requires skillful navigation and a bit of luck. WEATHER: ${searchArray(weather)}`,
                `A colossal shadow passes beneath your vessel - the silhouette of a massive sea creature that dwarfs even the Sea Rooks. It disappears into the depths, leaving you in awe. WEATHER: ${searchArray(weather)}`,
                `A hidden cove with bioluminescent algae lighting up the area. Exploring it might reveal ancient carvings or forgotten knowledge. WEATHER: ${searchArray(weather)}`,
                `A strange magnetic anomaly interferes with your compass, making navigation challenging. You must rely on other means to find your way. WEATHER: ${searchArray(weather)}`,
                `A small floating island of debris and wreckage provides a chance to salvage useful materials. WEATHER: ${searchArray(weather)}`,
                `An ancient underwater temple rises from the depths, its submerged halls filled with relics and mysteries of a long-lost civilization. WEATHER: ${searchArray(weather)}`,
                `A gathering of massive manta rays gliding gracefully through the water. Observing them can be a mesmerizing experience. WEATHER: ${searchArray(weather)}`,
                `A haunting melody drifts on the ocean breeze, tempting sailors to follow its enchanting tune. The source could be a siren or something else entirely. WEATHER: ${searchArray(weather)}`,
                `A massive school of glowing fish creates a dazzling display of underwater lights. Collecting some of them might have magical effects. WEATHER: ${searchArray(weather)}`,
                `An eerie silence falls over the ocean, broken only by the distant sounds of mysterious calls. The cause of this silence might be something lurking below. WEATHER: ${searchArray(weather)}`,
                `A submerged wreck of an ancient airship, now resting on the ocean floor. Exploring it might lead to advanced technology or forgotten knowledge. WEATHER: ${searchArray(weather)}`,
                `A ghost ship sailing the seas, manned by the spirits of its crew. Boarding it could reveal tales of lost treasure or a curse that must be broken. WEATHER: ${searchArray(weather)}`,
                `A colossal whirlpool that connects the ocean to another dimension. Venturing into it might lead to strange and otherworldly encounters. WEATHER: ${searchArray(weather)}`,
                `An underwater cave system, rumored to hold the entrance to the fabled Abyssal Labyrinth. WEATHER: ${searchArray(weather)}`,
                `A mirage-like illusion of a utopian island, promising rest and respite from your adventures. Be wary of its enchanting allure. WEATHER: ${searchArray(weather)}`,
                `You found an island with ${searchArray(items)}!`,
                `You found A Medium Rook!`,
                `You found A Massive Rook!`
    ]
    function oceanExploration(){
        return searchArray(oceanEvents)
    }

/*****CITY*****/
    //Supplements
    let rooklings = [
        "A spidery rookling with 6 legs, scuttling around with remarkable speed.",
        "A ball-shaped rookling that rolls playfully, often chasing after its human companion.",
        "A telescopic rookling that extends and retracts its body like a curious observer.",
        "A rookling with a large glowing eye, capable of seeing in the darkest of places.",
        "A speedy wheeled rookling, zooming through the terrain with great agility.",
        "A friendly and loving rookling, always eager to nuzzle and show affection.",
        "A rookling with powerful spring-like legs, capable of impressive acrobatics.",
        "A rookling that walks on 4 legs like a loyal and steadfast companion.",
        "A rookling that splits into 3 parts, each maintaining its own distinct personality.",
        "A mean-looking rookling bristling with blades, ready to defend its human companion.",
        "A rookling that magically floats in the air beside you, defying gravity with grace.",
        "A rookling with a mysterious door in its front, leading to a hidden compartment.",
        "A rookling that emits garbled speech from time to time, attempting to communicate.",
        "A miniature version of the rook, complete with stone armor and powerful elemental abilities.",
        "A graceful and agile rookling with wings, capable of gliding through the air.",
        "A rookling with a crystalline body that refracts light, creating beautiful rainbow patterns.",
        "An inquisitive rookling that loves to solve puzzles and find hidden secrets.",
        "A musical rookling that emits enchanting melodies from the crystals on its back.",
        "A rookling with a luminescent glow, providing a gentle and comforting light in the dark.",
        "A mischievous rookling that loves to play harmless pranks on its human companions.",
        "A rookling with an ancient script etched on its surface, capable of translating forgotten languages.",
        "A rookling with an affinity for earth and nature, able to control plants and summon vines.",
        "A rookling with the ability to manipulate water, creating small cascades and miniature waterfalls.",
        "A rookling with a keen sense of danger, warning its human companion of nearby threats.",
        "A rookling with the gift of mimicry, capable of imitating sounds and voices it hears.",
        "A rookling with a tiny yet potent flame that can ignite small objects.",
        "A rookling that can temporarily grow in size to assist its human companion in combat.",
        "A rookling with a powerful magnetic field, attracting and repelling metallic objects.",
        "A rookling with a set of retractable claws, perfect for climbing and exploration.",
        "A rookling with a soft and furry exterior, providing warmth and comfort to its human companion.",
        "A rookling with a set of glowing runes on its back, each holding unique magical properties.",
        "A rookling with the ability to create illusions, helping its human companion in stealth missions.",
        "A rookling with a mesmerizing dance, capable of captivating other creatures with its movements.",
        "A rookling with the power to communicate telepathically, forming a strong mental bond with its human companion.",
        "A rookling with the gift of foresight, offering glimpses of future events to its human companion.",
        "A rookling with a set of tiny wings, allowing it to levitate and glide for short distances.",
        "A rookling with the ability to produce a calming aura, pacifying aggressive creatures in its vicinityand soothing its human companion in times of stress and danger.",
        "A rookling with an intricate set of gears and cogs, capable of fixing mechanical devices.",
        "A rookling with a unique pattern of bioluminescent markings, glowing in various colors.",
        "A rookling with an insatiable curiosity, often leading its human companion to unexpected discoveries.",
        "A rookling with the gift of invisibility, becoming transparent to aid in stealthy missions.",
        "A rookling with a magnetic personality, attracting small metal objects from its surroundings.",
        "A rookling with the power to manipulate sand and earth, creating miniature landscapes.",
        "A rookling with a shell-like protective covering, retracting into it when threatened.",
        "A rookling with the ability to emit an ear-piercing sonic scream, stunning foes in combat.",
        "A rookling with a hypnotic gaze, capable of entrancing creatures it locks eyes with.",
        "A rookling with the power to generate a force field, shielding its human companion from harm.",
        "A rookling with an array of colorful feathers, capable of changing its appearance to blend into different environments.",
        "A rookling with a trail of small floating orbs, each illuminating its path.",
        "A rookling with the ability to produce a healing aura, aiding in the recovery of wounds and injuries.",
        "A rookling with the gift of telekinesis, capable of moving objects with its mind.",
        "A rookling with a set of venomous spines, deterring potential threats from getting too close.",
        "A rookling with the power of cryomancy, able to freeze water and create ice constructs.",
        "A rookling with the ability to project holographic images, creating distractions or illusions.",
        "A rookling with a unique gemstone embedded in its body, granting it special elemental powers.",
        "A rookling with the gift of empathy, able to sense and understand the emotions of those around it.",
        "A rookling with a pair of retractable antennae, capable of detecting hidden dangers or treasures.",
        "A rookling with the power to control lightning, unleashing electrifying attacks in battle.",
        "A rookling with a chameleon-like ability to blend seamlessly into its surroundings.",
        "A rookling with the gift of telepathy, capable of communicating with other creatures mentally.",
        "A rookling with a whirlwind-like movement, able to create powerful gusts of wind.",
        "A rookling with the ability to manipulate time for short bursts, enabling brief glimpses into the past or future.",
        "A rookling with a series of glowing orbs encircling its body, granting it enhanced senses and awareness.",
        "A rookling with a set of retractable fins, capable of swimming swiftly through water.",
        "A rookling with the power of pyrokinesis, able to create and control fire with precision.",
        "A rookling with a collection of tiny mirrors on its surface, reflecting light and creating dazzling displays.",
        "A rookling with the gift of teleporation, able to instantly transport itself and its companion to different locations.",
        "A rookling with the power to manipulate gravity, altering the weight and movement of objects.",
        "A rookling with a soothing aura, capable of calming aggressive creatures and reducing tension in its vicinity.",
        "A rookling with a unique color-shifting ability, changing its appearance to match its emotions.",
        "A rookling with the gift of levitation, able to float gently above the ground.",
        "A rookling with the ability to generate a protective force field, shielding its companion from harm.",
        "A rookling with a set of bioluminescent patterns that form beautiful glowing designs on its surface.",
        "A rookling with the power of terramancy, capable of manipulating earth and stone.",
        "A rookling with a set of extendable tentacles, useful for reaching and grabbing objects from a distance.",
        "A rookling with the gift of healing, able to mend wounds and cure ailments with its touch.",
        "A rookling with a series of holographic projectors, capable of creating decoys and illusions.",
        "A rookling with the ability to generate protective barriers, shielding its companion from attacks.",
        "A rookling with a collection of tiny crystal shards on its body, refracting light in stunning patterns.",
        "A rookling with the power of aquamancy, capable of controlling water and summoning water-based attacks.",
        "A rookling with a unique camouflage ability, blending seamlessly into its surroundings for stealthy maneuvers.",
        "A rookling with the gift of precognition, able to see glimpses of future events in its dreams.",
        "A rookling with a set of retractable wings, allowing it to fly short distances.",
        "A rookling with the power of telepathy, able to communicate with its companion through thoughts and emotions.",
        "A rookling with a gentle aura, capable of soothing aggressive creatures and calming turbulent waters.",
        "A rookling with an intricate pattern of glowing tattoos, each holding unique magical properties.",
        "A rookling with the gift of agility, able to perform acrobatic feats and nimble movements.",
        "A rookling with a set of extendable vines, useful for reaching and grasping objects from afar.",
        "A rookling with the ability to generate electric charges, useful for powering devices and lighting dark spaces.",
        "A rookling with a collection of mesmerizing patterns on its body, capable of entrancing onlookers.",
        "A rookling with the power to generate protective shields, guarding its companion from harm.",
        "A rookling with a set of glowing crystal horns, each emitting a different harmonious note.",
        "A rookling with the gift of teleportation, able to transport itself and its companion to distant locations.",
        "A rookling with a calming presence, capable of pacifying aggressive creatures and alleviating fear.",
        "A rookling with a unique ability to generate heat, keeping its companion warm in cold environments.",
        "A rookling with a set of luminescent patterns on its body, glowing in various colors.",
        "A rookling with the power of aerokinesis, able to control air and create gusts of wind.",
        "A rookling with a keen intellect, able to understand and solve complex puzzles.",
        "A rookling with the gift of invisibility, capable of blending into its surroundings to avoid detection.",
        "A rookling with a series of rotating gears and mechanisms, capable of fixing broken devices.",
        "A rookling with a set of retractable fins, useful for swimming and navigating underwater.",
        "A rookling with the power of geomancy, able to shape and manipulate the terrain to its advantage.",
        "A rookling with a collection of tiny sparkling gems on its body, reflecting light in dazzling displays.",
        "A rookling with the gift of mind-reading, able to understand the thoughts and emotions of those around it.",
        "A rookling with a soothing aura, capable of calming aggressive creatures and reducing tension in its vicinity."
      ];

    let cityBasics ={
        'staples': {
            'Hunters Guild':
                `You can decide to accept quests and head out to complete the requirements, or you can turn it down and ask for another. This is as simple as going through the process again and seeing what you get a second time. Consider using the quests you DON’T take on as more aspects to your story. Other things are happening out in the world and maybe they can tie in to your character’s overall adventure.`,
            'Tavern' : 
                `Colostle operates on a bartering system of commerce, you can trade any item you have found on your travels for a night’s stay at the Tavern. This stay will grant your player +1 to either your COMBAT or EXPLORATION scores. You can only do this ONCE per visit to the city. You will have to spend at least one EXPLORATION phase outside of the city before being able to use the Tavern again. The Tavern is also a great place to meet people and talk to strangers, and hear rumours and ask about any jobs that are needed. Once per visit to the Tavern you can ask a stranger for a quest and use the Quest Generation system from the Hunter’s Guild section to create one. Then when complete you will need to return to the Tavern for your reward.`,
            'Merchant':
                `The Merchant is an interesting character found in their shop in the city streets. For a variety of different prices (see each item) all manner of strange devices, weapons and supplies can be purchased. Some of them are single use - others are pieces of equipment you can equip, Currently Selling :
                ${shuffleSlice(merchant,1+rollDice(4))}
                `,
            'Housing District':
                `The Housing District is where the populace of the city live and is a great place for your story to develop if you need to meet a contact, stay with family or friends, or get some information. The district mostly consists of Rook husks piled on top of one another to create something akin to an apartment block. Makeshift ladders and crude stairways clamber over lower houses to reach upper ones and here-and-there old Rook arms form bridges and washing lines. Between the houses; wandering the various walkways and corridors are vendors selling food door-to-door, mysterious cultists going about their shady business trying to recruit new members, and the residents themselves, gossiping or visiting friends. It is a vibrant place and where your character will need to go if they are looking for someone. All manner of people live in the Housing Districts of cities; entertainers, brewers, retired heroes, seamstresses, tailors, huge families, hermits squirrelled away from the outside world, and soldiers for the army of the city. The Housing District is a great place for anything to happen in your story that involves meeting new or old characters and advancing your adventure with information and rumour!`
            },
        'amenities' : {
            'Palace Grounds' :
                `This city has a palace, and a ruler as well. This is likely a place of sumptuous architecture built out of only the most ornate Rook husks, at a high point in the city  looking over everyone else. It is doubtful that a wanderer such as yourself would simply be allowed in but perhaps your story has given your character a reason to speak to the ruler? An offering would certainly help - maybe you have picked up a treasure on your adventure?`,
            'Lapidarist' :
                `A Rookstone specialist; someone who can work these ancient magical stones and magically upgrade your equipment, for a price of course. FOR 1 TREASURE - they can add an additional magical ability (Ice, Rumble or Electric) to your helm. FOR 2 TREASURES - they can add a magical ability to an Arm, Rookling or Mount. FOR 3 TREASURES - they will share with you a Rookstone from their private collection. One that isn’t Ice, Rumble or Electric; but a new one-of-a-kind magical power. You can come up with what this power is and how your character can use it.`,
            'Rooksmith' :
                `Toiling away in their Mount Garages; Rooksmiths work on the mechanical parts of Rooks and convert them into vehicles or mounts to be ridden upon. FOR 3 TREASURES - they will build a custom mount for your character. It could be seaworthy, or landworthy and will feature some form of WEAPON based attack ability which you can choose (such as cannon, crossbow, battering ram etc.) See MOUNTED class info for fighting with MOUNT weapons.`,
            'Cartographer': 
                `A wise and bookish individual dedicated to the difficult art of mapping the lands around the city. Cartographers rely on information from Rook Hunters as they cannot go out and collect it themselves. THEY WILL PAY 2 TREASURES for a map of a new area. Take a quest from the Hunter’s Guild. Draw a map of your adventure marking anything discovered from your EXPLORATION phases whilst on the quest. Return it to the Cartographer for your reward.`,
            'Weapon Smith':
                `A tough person covered in oil and rumble powder working in a hot and smoky forge. They take Rook weapons and adapt and upgrade them for hunters. FOR 1 TREASURE - they can upgrade your current weapon. Add 1 to your COMBAT score. FOR 2 TREASURES - they can give you a whole new weapon. This is yours to come up with; perhaps a great hammer or a long Rookspear? Add 1 to your COMBAT score.`,
            'Arms Dealer': 
                `They stand behind their counter; a great number of small arms coming out of their back like a stone spider. The Arms dealer can find a new arm for you and help you with the ritual of attunement. FOR 2 TREASURES - they can provide you with a whole new arm. This can be whatever you imagine - perhaps it is coiled like a snake, or huge and thick like a tree trunk; able to lift a boulder with ease?`,
            'Rookling Creche':
                `Rookling Crèches appear in most cities in the Colostle as a great place for Hunters to pickup their first Rookling companion for a quest. Or for those who live within the city to secure some cheap labour for their business or family home. As a player you can trade any Rooklings you have adopted on your journey here for a chance at a different type using the table below. Or you can buy a Rookling for 2 TREASURES. Either way you must let the cards decide which you receive - its always a gamble with Rooklings!`,
            'Gourmet District':
                `The centre of food production in the city; a bustling place of restaurants, food markets and spice bazaars. Here, hunters who have caught wild beasts out in the lands surrounding the city can find a great price for their prize - and also get a great meal while they’re bargaining. THEY WILL PAY 1 TREASURE for a wild beast caught by a hunter. FOR 1 TREASURE - enjoy a meal from one of the many restaurants and add 1 to your EXPLORATION score.`,
            'House for sale':
                `Living in a city does not come cheap. For 20 TREASURES you can buy a house in a city that has this option available. This is advisable to do if the city you have discovered has a lot of useful amenities. Owning a house grants you plenty of story options for your character but it also grants your character 2 major boons:
                HEALING - once per stay in the city you can heal your character fully back up to their starting EXPLORATION and COMBAT scores. Narratively this involves your character staying in the city for a WEEK.
                FAST TRAVEL - As a resident you gain access to the city’s Caravan service which allows your character the ability to fast travel back from any Hunter’s Guild quests. This means your character won’t have to spend the EXPLORATION phases to journey back after a quest and instead can travel for a single day in the caravan. You cannot use the Caravan to head out to a quest though - only to return home.`  
            }
    }
    let merchant = [
        `GLIDER - Neat unfolding glider structure stored on your character’s back that allows you to glide from heights. PRICE: 3 Treasures`,
        `WEATHERSTONE - A mysterious stone that summons (${searchArray(weather)}). it will always generate. Can be used once per EXPLORATION phase. PRICE - Any 5 items`,
        `TURTLE SHELL ARMOUR - Stone Rook Armour in the shape of a turtle shell. Will block one wound of damage each COMBAT phase. PRICE - 5 Treasures`,
        `TRIPWIRE LAUNCHER - A crossbow-like device that launches 2 pins with a chain between them. When aimed correctly this can trip up a Rook. PRICE - 4 items`,
        `ROOK GAUNTLETS - Huge stone Rook hands that fit over your hands and allow you to punch with the power of a Rook. PRICE - Any 1 item`,
        `EXTENDING POLE - Telescopic pole made from Rook parts. Allows you to vault upward and also attack from a distance PRICE - Any 3 items`,
        `ELECTRIC SWORD - A Rook great sword imbued with Electric magic. PRICE - 1 Treasure`,
        "FLAME-RESISTANT CLOAK - A special cloak woven from Rook fibers that grants protection against fire and intense heat. PRICE - 2 Treasures",
        "WIND CHARM - A small charm imbued with wind magic. When activated, it grants a burst of speed for a short duration. PRICE - 2 items",
        "EARTHEN AMULET - A powerful amulet that allows the wearer to summon temporary earth constructs for various purposes. PRICE - 3 Treasures",
        "AETHER GOGGLES - A pair of goggles that grant the ability to see through solid objects, revealing hidden passages and treasures. PRICE - 4 items",
        "CRYSTALINE POTION - A potion crafted from Rook crystals that temporarily enhances the drinker's strength and agility. PRICE - 1 Treasure",
        "AQUA BOOTS - Special boots made from Rook materials that allow the wearer to walk on water surfaces. PRICE - 3 items",
        "SILENT WHISTLE - A magical whistle that, when blown, temporarily silences all sound within its vicinity, aiding in stealthy approaches. PRICE - 2 items",
        "SHADOW CLOAK - A cloak that grants the wearer the ability to blend into the shadows and become nearly invisible in dimly lit areas. PRICE - 4 Treasures",
        "EMBERSTONE - A rare and precious stone that radiates warmth and can provide a source of heat in cold environments. PRICE - 2 Treasures",
        "AEGIS SHIELD - A shield made from Rook parts that can repel magical attacks and provide additional defense in combat. PRICE - 3 Treasures",
        "SPECTRAL LANTERN - A lantern that emits a ghostly glow, revealing hidden spirits and entities invisible to the naked eye. PRICE - 2 items",
        "AETHERIC BAND - A magical band worn on the arm that grants the ability to manipulate aether, allowing the user to create temporary barriers and force fields. PRICE - 5 Treasures",
        "STARDUST VIAL - A vial filled with stardust, which can be sprinkled to reveal hidden magical symbols and messages. PRICE - 1 Treasure",
        "CLOCKWORK AMULET - An amulet with intricate clockwork mechanisms that can slow down or speed up time for short periods. PRICE - 4 Treasures",
        "SHIMMERING EARRINGS - Earrings adorned with Rook crystals that grant the ability to understand and speak any language. PRICE - 3 items",
        "FROSTBITE ARROWHEADS - Special arrowheads made from Rook materials that freeze targets upon impact. PRICE - 2 items",
        "ARCANE PENDANT - A pendant imbued with ancient arcane energy, granting the wearer limited control over elements. PRICE - 5 Treasures",
        "SUNSTONE LENS - A lens made from a sunstone that amplifies sunlight and can be used to create powerful solar attacks. PRICE - 3 Treasures",
        "AETHERIC RESONATOR - A handheld device that can emit a sonic frequency capable of shattering obstacles and barriers. PRICE - 4 items",
        "EMBERBLADE - A sword forged with Rook materials and enchanted with fire magic, capable of igniting foes in combat. PRICE - 2 Treasures",
        "DIVINE MEDALLION - A medallion that provides protection against dark and unholy forces, granting resistance to necromantic spells. PRICE - 5 Treasures",
        "SHADOWSTEP BOOTS - Boots that allow the wearer to teleport short distances in the blink of an eye. PRICE - 3 items",
        "STORMKEEPER STAFF - A staff made from Rook parts that can summon and control thunderstorms. PRICE - 4 Treasures",
        "ETHEREAL TOME - A book filled with ancient knowledge and spells, granting access to powerful arcane abilities. PRICE - 5 Treasures",
        "CELESTIAL ORB - A crystal orb that reveals hidden constellations and can predict celestial events. PRICE - 3 Treasures",
        "SOULSTONE AMULET - An amulet that stores the souls of defeated enemies, allowing the player to harness their abilities. PRICE - 4 Treasures",
        "BLAZING GLOVES - Gloves imbued with fire magic, allowing the player to throw fiery projectiles at enemies. PRICE - 2 items",
        "PHASEWALKER PENDANT - A pendant that grants the ability to pass through solid objects for a short period. PRICE - 5 Treasures",
        "MIND READER'S EYE - A special eye patch that enables the wearer to read the thoughts of others. PRICE - 3 items",
        "SHAPESHIFTER'S RING - A ring that allows the wearer to transform into different creatures or objects. PRICE - 4 Treasures",
        "FROSTBANE CRYSTAL - A crystal that emits a freezing aura, encasing enemies in ice. PRICE - 2 Treasures",
        "TWILIGHT CAPE - A cloak that grants invisibility in low light conditions and shadowy environments. PRICE - 3 items",
        "STARFORGE HAMMER - A hammer capable of channeling starlight to forge powerful magical weapons. PRICE - 4 Treasures",
        "ETHERWEAVE ARMOR - Armor woven from ethereal threads that grants increased agility and mobility. PRICE - 5 Treasures",
        "TIMEKEEPER'S HOURGLASS - An hourglass that allows the user to manipulate time for brief moments. PRICE - 3 items",
        "ENCHANTER'S QUILL - A quill that can imbue written words with magical properties and effects. PRICE - 2 items",
        "FLIGHT OF THE PHOENIX - A feather that grants the ability to fly for a limited time, like the mythical phoenix. PRICE - 4 Treasures",
        "CRIMSON HEARTSTONE - A heart-shaped stone that grants the ability to control and manipulate blood. PRICE - 2 Treasures",
        "SHIELD OF THE ANCIENTS - A legendary shield that provides immunity to certain magical attacks. PRICE - 4 Treasures",
        "DREAMWALKER'S SANDALS - Sandals that allow the wearer to enter the dreams of others. PRICE - 2 items",
        "ASTRAL COMPASS - A compass that guides the player to hidden celestial treasures and locations. PRICE - 5 Treasures",
        "SPARKBENDER GLOVES - Gloves that can control and direct lightning for offensive and defensive purposes. PRICE - 3 items"
      ]

    let huntersGuild = [
        [/*Location*/
            "in a deep dark forest",
            "on an island in the middle of a lake",
            "high in some rocky mountains",
            "in a Rook graveyard",
            "deep in a strange cave",
            "in the misty gloomy swamplands",
            "at the doorway to another room",
            "in the abandoned ruins of an ancient people",
            "on the huge staircase leading up into the clouds",
            "within the labyrinthine catacombs beneath the city",
            "at the edge of a treacherous volcanic crater",
            "within the ancient and overgrown Rook Temple",
            "amidst the shifting sands of the desert dunes",
            "in the heart of a dense and enchanted forest",
            "at the summit of a towering floating island",
            "inside the mechanical clockwork city",
            "in the treacherous maze of ice caves",
            "on a series of small floating islands in the sky",
            "within the deep chasms of the underground caverns",
            "in the eerie glow of a bioluminescent underground lake",
            "at the border of the ethereal realm and the physical world",
            "inside the ruins of an ancient Rook city",
            "at the mouth of a long-forgotten underground river",
            "within the mysterious and ever-shifting Mirror Marsh",
            "on the outskirts of a bustling coastal town",
            "in the enchanted glade hidden deep within the forest",
            "at the entrance of an otherworldly dimensional rift",
            "on the treacherous cliffs overlooking the sea",
            "within the ruins of a once-mighty Rook fortress",
            "amidst the colorful and psychedelic Dream Gardens",
            "in the pitch-black depths of a subterranean abyss",
            "at the heart of a massive Rook-infested labyrinth",
            "within the ancient and decaying Rook Hive",
            "on the floating islands of the Aetherial Skylands",
            "at the boundary between the elemental planes",
            "inside the long-abandoned Rook Observatory",
            "amidst the floating icebergs of the Frozen Wastes",
            "in the magical glen guarded by ancient Rook sentinels",
            "within the cursed and ever-shifting Whispering Woods",
            "at the ancient Rook Stargate, an interdimensional portal",
            "on the outskirts of the mystical and ethereal Celestial City",
            "within the underground crystal caves, glowing with magic",
            "amidst the ruins of a sunken Rook city, beneath the ocean",
            "at the heart of the fiery volcanic caldera",
            "within the eerie and ghostly Rook Catacombs",
            "on the floating islands of the Sky Archipelago",
            "at the sacred Rook Shrine, hidden high in the mountains",
            "within the vast and labyrinthine Rook Library",
            "in the shadowy depths of the forbidden Rook Sanctuary",
            "amidst the twisted and otherworldly Rook Wonderland",
            "at the entrance of the legendary and elusive Rookgate",
            "within the mysterious and enchanting Rook Garden of Dreams",
            "on the shifting sands of the ancient Rook Colosseum",
            "at the haunted and decrepit Rook Manor",
            "within the lost Rook Temple of the Four Elements",
            "at the heart of the enchanted and ever-changing Whispering Forest"
        ],
        [/*Twist*/
        `The Rook is picking on travellers and attacking their mounts and then eating them.`,
        `The Rook is flying somehow, circling a tower and dropping boulders on anyone who gets close.`,
        `Inside a huge ancient Rook husk, a medium-sized Rook is holed up sending hordes of Rooklings out to steal resources and bring them back.`,
        `A massive spider-like Rook is terrorising local towns and villages.`,
        `A wheeled Rook is churning up farmland of a local village.`,
        `A Rook has made its nest in a village and has forced all the residents out.`,
        `A Rook has planted itself in a river and blocks the flow of water.`,
        `A Rook underground is causing earthquakes with its rumble magic.`,
        `At the top of a volcano, a massive Rook is awakening and threatens to make the volcano erupt.`,
        `A mischievous spectral Rookling haunts a town.`,
        `A town built on the back of a huge once-dormant Rook. But the Rook has awoken and is slowly on the move...`,
        `People have reported a voice coming from within a massive dormant Rook...`,
        `A whole village is dreaming of the same Rook, but none of them have seen it... yet.`,
        `A faction of Rook worshippers, believing the Rook to be divine, opposes the Guild's attempts to remove it from the region.`,
        `A group of treasure hunters believes that the Rook's interior hides an ancient cache of magical artifacts and is determined to explore it.`,
        `The Rook suddenly exhibits strange behavior, such as moving erratically or emitting ethereal lights, baffling both the Guild and locals.`,
        `A powerful sorcerer, seeking to harness the Rook's energy, attempts to bind the construct to their will, posing a significant threat.`,
        `The Rook's movements are being controlled remotely by an unknown individual using advanced magical technology.`,
        `An enigmatic figure known as the "Rook Tamer" claims to have the ability to communicate with and control the Rook, leading to intrigue and suspicion.`,
        `The Rook begins emitting an unsettling, otherworldly hum that affects the mental well-being of nearby inhabitants.`,
        `A long-lost scroll containing ancient knowledge about the Rooks' origins and weaknesses resurfaces, drawing the attention of various factions.`,
        `The Guild discovers that the Rook's true purpose is not to cause harm, but to protect an ancient relic buried deep within its body.`,
        `An artist attempts to paint an elaborate mural on the Rook's surface, but their work seems to influence the Rook's behavior in mysterious ways.`,
        `A reclusive engineer claims to have devised a way to deactivate the Rook without destroying it, sparking a heated debate on the best course of action.`,
        `The Rook shows signs of sentience, as if it is trying to convey a message to the Guild or the nearby populace.`,
        `A legendary architect, fascinated by the Rook's design, sets out to study its construction methods to build even grander structures.`,
        `The Rook Hunters Guild is approached by a secret society that believes the Rooks hold the key to unlocking ancient knowledge and secrets.`,
        `A peculiar phenomenon causes the Rook to duplicate itself, leading to confusion and difficulty in identifying the real one.`,
        `A group of scholars insists that the Rook contains inscriptions with clues to a lost civilization's history, leading to an academic expedition.`,
        `The Rook's presence inadvertently attracts a congregation of worshippers, convinced it embodies a mythical creature from ancient legends.`,
        `A skilled musician discovers that certain musical notes have a soothing effect on the Rook, sparking debates on how to use this knowledge.`,
        `The Rook's body begins to emit powerful magical energy, drawing the attention of practitioners seeking to harness it for their purposes.`,
        `A sect of druids claims that the Rook is part of a larger network of sentient stone constructs, forming a natural defense system for the land.`,
        `The Rook Hunters Guild uncovers evidence suggesting that a hostile neighboring kingdom seeks to control the Rook for military advantage.`,
        `A traveling carnival sets up camp on the Rook's back, using its impressive height and space as a unique venue for their performances.`,
        `The Rook's movements appear to align with the positions of celestial bodies, hinting at a cosmic connection that baffles astronomers.`,
        `A master locksmith believes that the Rook guards a hidden vault filled with untold riches and offers their expertise to unlock it peacefully.`,
        `A peculiar enchantment placed on the Rook causes it to emit a mesmerizing glow, attracting curious onlookers from all over.`,
        `A renowned philosopher theorizes that the Rook embodies the essence of stoicism and seeks to study it as a philosophical symbol.`,
        `A legendary blacksmith endeavors to forge a weapon capable of defeating the Rook, but doing so requires rare materials and skilled craftsmen.`,
        `A mysterious illness begins affecting those who spend too much time in the Rook's vicinity, prompting investigations into its cause and cure.`,
        `The Rook begins emanating a powerful magnetic field, disrupting navigational devices and posing risks to air and sea travel.`,
        `An eccentric inventor constructs a massive, mechanical replica of the Rook to study its behavior and movements for engineering purposes.`,
        `A hidden sect of monks reveres the Rook as a symbol of balance and harmony and opposes any attempts to disturb its peace.`,
        `An ambitious noble aims to harness the Rook's strategic value by constructing a fortress atop it, leading to tension with the Guild.`,
        `A seer claims that the Rook's presence is tied to a series of prophetic visions, and deciphering them may unlock its true purpose.`,
        `The Rook's shadow mysteriously takes on a life of its own, leading to unnerving encounters and folklore surrounding its doppelganger.`,
        `A peculiar form of magical crystals is found within the Rook's core, prompting both scientific and arcane investigations into their properties.`,
        `The Rook is discovered to contain intricate clockwork mechanisms, suggesting it might be a relic from a highly advanced ancient civilization.`,
        `An oracle believes that the Rook serves as a conduit between the mortal realm and the spirit world, potentially granting visions of the afterlife.`,
        `A group of illusionists uses the Rook as a canvas for their grandiose magical projections, creating awe-inspiring displays.`,
        `The Rook's exterior begins to change color and texture, signifying a deeper magical transformation with unknown implications.`,
        `The Guild receives a mysterious map that supposedly leads to the secret chamber where the Rook's creator hid their most precious inventions.`,
        `A rare cosmic event, the "Rook's Comet," coincides with the construct's awakening, sparking rumors of an otherworldly connection.`,
        `The Rook's presence somehow affects the growth of nearby flora, leading botanists to study its potential effects on agriculture and medicine.`,
        `An elusive group of geomancers believes that the Rook holds the key to unlocking ley line energy, and they seek to tap into its power source.`,
        `A group of rebels sees the Rook as a symbol of oppression and aims to topple it to spark a revolution against the ruling monarchy.`,
        `The Rook suddenly goes dormant, prompting scholars to investigate the cause and potential consequences for the region's stability.`,
        `A renowned bard composes a mesmerizing symphony inspired by the Rook's appearance, captivating all who listen to its enchanting melody.`,
        `An ancient prophecy foretells that the Rook's awakening heralds the rise of a new king, igniting a power struggle within the realm.`,
        `The Rook's massive form attracts a rare species of magical creatures, and preserving their habitat becomes a top priority for conservationists.`,
        `A hidden chamber within the Rook's interior contains elaborate mechanisms that might unlock a portal to a pocket dimension.`,
        `A talented sculptor offers to craft an ornate, lifelike statue of the Rook to serve as a symbol of peace and unity in the region.`,
        `The Rook is unexpectedly discovered to contain traces of ancient knowledge, drawing the interest of scholars and historians from afar.`,
        `A peculiar "Rook Whisperer" emerges, claiming to have the ability to communicate with the construct through a unique form of magic.`,
        `An order of architects considers the Rook's design as an architectural masterpiece and seeks to document its structural elements.`,
        `The Rook suddenly exhibits signs of advanced intelligence, as if it is trying to communicate its thoughts and emotions.`,
        `A wandering artificer believes that the Rook's design holds the key to constructing golems of unimaginable power.`,
        `A traveling circus seeks to incorporate the Rook into their performances, but doing so safely presents significant challenges.`,
        `An ancient, weathered map indicates that the Rook might be part of a network of similar constructs scattered throughout the land.`,
        `The Rook's position atop a powerful ley line makes it a focal point for arcane practitioners seeking to tap into its energy.`,
        `A group of alchemists proposes using a concoction to temporarily shrink the Rook, allowing for in-depth study of its intricate carvings.`,
        `A young squire becomes convinced that the Rook contains the spirit of a legendary knight and is determined to communicate with it.`,
        `An eccentric scholar hypothesizes that the Rook is actually a remnant of a long-lost civilization from another plane of existence.`,
        `The Rook begins emitting a peculiar frequency that only certain individuals can hear, leading to speculations about its purpose.`,
        `A secretive cult reveres the Rook as an avatar of an ancient deity and seeks to protect it at all costs.`,
        `The Rook's presence influences the local climate, leading to mysterious weather patterns that affect agriculture and trade.`,
        `A renowned chef aims to create a culinary masterpiece using ingredients harvested from within the Rook's interior, attracting food enthusiasts.`,
        `A skilled engineer designs a colossal, mobile fortress modeled after the Rook and seeks Guild assistance in testing its functionality.`,
        `A curious researcher discovers a hidden chamber within the Rook that contains advanced astronomical instruments.`,
        `A peculiar phenomenon causes the Rook to emit harmonious musical tones, attracting traveling musicians to perform on its surface.`,
        `The Rook appears to resonate with the emotional state of nearby individuals, leading to experiments in emotional manipulation.`,
        `A guild of illusionists sets out to create an awe-inspiring light show that transforms the Rook into a breathtaking spectacle.`,
        `An enigmatic hermit, living atop the Rook's spire, offers cryptic advice to passersby, hinting at hidden truths about the construct.`,
        `The Rook becomes the subject of a controversial art installation, sparking debates about the boundaries of artistic expression.`,
        `A group of ambitious scholars seeks to decipher the complex carvings on the Rook's surface, believing they hold ancient secrets.`,
        `The Rook's shadow mysteriously moves independently, hinting at a connection to a parallel plane of existence.`,
        `A reclusive mage believes that the Rook's design serves as a conduit for gathering raw magical energy from the environment.`,
        `The Guild receives a cryptic message claiming that the Rook's awakening is the first step in an ancient prophecy's fulfillment.`,
        `An architect proposes an audacious plan to construct a network of bridges and structures connecting various Rooks throughout the land.`,
        `A legendary blacksmith believes that the Rook's core houses a powerful artifact capable of transforming mundane materials into gold.`,
        `The Rook's surface mysteriously changes to display intricate patterns and symbols that shift with the phases of the moon.`,
        `A group of spiritualists insists that the Rook embodies the soul of an ancient ancestor and is deserving of veneration.`,
        `A skilled inventor develops a flying machine, intending to explore the Rook from above and study its intricate mechanisms.`,
        `An ancient tome discovered in a forgotten library contains detailed descriptions of similar constructs to the Rook from distant lands.`,
        `The Rook appears to be a focal point for unusual celestial events, leading astronomers to study its potential astronomical significance.`,
        `A peculiar artifact found within the Rook's interior suggests a connection to an ancient civilization predating recorded history.`,
        `A gifted artisan endeavors to create lifelike, animated replicas of the Rook using enchanted sculptures.`,
        `A renowned bard composes a series of epic poems recounting the Rook's history and influence on the realm.`,
        `The Rook mysteriously moves during the night, leading to legends of a "sleepwalking construct" that wanders the land.`,
        `An ethereal, ghostly presence begins to manifest near the Rook, leading to rumors of a restless spirit haunting the construct.`,
        `A rare astronomical alignment causes the Rook's surface to reflect star patterns with astonishing precision.`,
        `The Guild is approached by a faction of pacifists who seek to mediate with the Rook and find a nonviolent resolution to the issue.`,
        `A talented sculptor offers to craft a magnificent, life-size statue of the Rook to commemorate its significance to the region.`,
        `An ancient prophecy claims that the Rook's awakening signals the end of an era and the dawn of a new age of enlightenment.`,
        `The Rook's intricate carvings begin to emit a soft glow, attracting curious onlookers from miles around.`,
        `An unscrupulous merchant attempts to capitalize on the Rook's presence by selling counterfeit relics supposedly found within its body.`,
        `A group of geomancers believes that the Rook's alignment with ley lines holds the key to predicting future natural disasters.`,
        `The Rook's awakening coincides with the emergence of a powerful mage claiming to be its creator, seeking recognition for their work.`,
        `An art historian sets out to decipher the symbolism and hidden meanings behind the Rook's intricate carvings.`,
        `A peculiar form of magic, unique to the Rook, begins to affect the surrounding flora and fauna, creating a mesmerizing natural spectacle.`,
        `A legendary alchemist speculates that the Rook's core contains the secret to eternal life, sparking a race to unlock its mysteries.`,
        `The Rook's interior is discovered to contain a complex maze of chambers and corridors, suggesting it might serve as a labyrinthine prison.`,
        `An ancient tale speaks of a hidden treasure guarded within the Rook's depths, drawing treasure hunters from far and wide.`,
        `The Rook begins emanating a soothing aura that has a calming effect on nearby wildlife, prompting nature enthusiasts to study it.`,
        `An ambitious engineer proposes a plan to retrofit the Rook with advanced mechanisms, transforming it into a formidable war machine.`,
        `The Guild receives a mysterious riddle that supposedly reveals a clue to understanding the Rook's true purpose and origin.`,
        `A peculiar mineral found within the Rook's body exhibits unique magical properties, sparking interest among alchemists and enchanters.`,
        `The Rook's presence inexplicably affects the behavior of local wildlife, leading druids to study its impact on the ecosystem.`,
        `A renowned scholar believes that the Rook holds the key to deciphering a forgotten language, potentially unlocking ancient knowledge.`,
        `A group of mystical healers claim that the Rook's energy has therapeutic properties and seek permission to conduct healing ceremonies nearby.`,
        `The Rook's awakening coincides with a rare celestial event, prompting astrologers to speculate about its cosmic significance.`,
        `An enigmatic figure known as the "Rook Guardian" appears, claiming to have the ability to communicate with and protect the construct.`,
        `A group of illusionists sets out to create a grand magical illusion that makes the Rook appear as a different creature altogether.`,
        `The Rook's presence mysteriously attracts metal objects from miles around, creating a peculiar magnetic phenomenon.`,
        `An eccentric scholar hypothesizes that the Rook is actually a portal to another realm, prompting investigations into its true nature.`,
        `A legendary philosopher once wrote about the Rook as a symbol of stoic strength and resilience, inspiring a new philosophical movement.`,
        `The Rook's surface displays a mesmerizing light show during the night, attracting astronomers and stargazers to observe it.`,
        `An order of monks believes that the Rook is a test sent by their deity to evaluate the realm's moral virtues.`,
        `The Rook's construction materials are discovered to possess unique magical properties, attracting various factions seeking to harness them.`,
        `An ambitious architect aims to build an elaborate observation deck atop the Rook's spire, offering unparalleled views of the realm.`,
        `The Rook begins emanating a faint hum that seems to resonate with the vibrations of the earth, intriguing geologists and seismologists.`,
        `A legendary cartographer seeks to create a detailed map of the Rook's intricate carvings, transforming them into an artistic masterpiece.`,
        `The Rook's awakening coincides with a rare astronomical event known as the "Rook Eclipse," attracting stargazers from all over.`,
        `A peculiar artist sets out to paint an enormous, ever-changing mural on the Rook's surface, depicting scenes from history and myth.`,
        `The Rook's presence influences the weather patterns, leading meteorologists to study its potential impact on the region's climate.`,
        `An ancient chronicle mentions that the Rook once housed an oracle who could predict the realm's future, leading to a search for prophecies.`,
        `A group of enthusiastic children believes that the Rook is a guardian of hidden treasure, sparking a playful treasure hunt.`,
        `The Rook begins emitting peculiar, harmonious sounds that seem to respond to specific frequencies played nearby, fascinating musicians.`,
        `An order of knights seeks to honor the Rook as a symbol of strength and chivalry, vowing to protect it from potential threats.`,
        `The Rook's awakening coincides with a unique planetary alignment, inspiring astrologers to study its astrological significance.`,
        `A peculiar form of magical flora begins to grow on the Rook's surface, leading botanists to study its potential properties.`,
        `A legendary cartographer aims to create a highly detailed map of the Rook's interior chambers and tunnels, exploring its labyrinthine depths.`,
        `The Rook's awakening coincides with a rare astronomical event known as the "Rook Comet," leading astronomers to observe its trajectory.`,
        `A master calligrapher offers to inscribe the Rook's intricate carvings with ancient script, preserving its history for generations to come.`,
        `A reclusive sage believes that the Rook's design represents a complex mathematical equation, leading to new discoveries in geometry.`,
        `The Rook's presence affects the flow of magical energy in the region, intriguing practitioners of the arcane arts.`,
        `An art exhibition centered around the Rook's significance inspires various artists to create diverse artworks in its honor.`,
        `A renowned geographer seeks to create a comprehensive map of the Rook's location and its impact on the surrounding geography.`,
        `The Rook's awakening coincides with a rare astronomical event known as the "Rook Equinox," attracting scholars and astronomers.`,
        `An enterprising entrepreneur proposes constructing a floating marketplace atop the Rook, turning it into a bustling commercial hub.`,
        `A group of researchers discovers that the Rook's design incorporates principles of sacred geometry, leading to philosophical discussions.`,
        `The Rook's surface mysteriously reflects the phases of the moon, prompting speculation about its connection to lunar cycles.`,
        `A group of treasure hunters claims that the Rook's core contains a cache of ancient artifacts and sets out to uncover its secrets.`,
        `The Rook begins emitting soft, haunting melodies, sparking rumors of an ethereal musician hidden within its structure.`,
        `A renowned sculptor offers to carve intricate symbols of peace and unity onto the Rook's surface, turning it into a beacon of harmony.`,
        `An ancient prophecy speaks of a time when the Rook will awaken and reveal a secret that will reshape the realm's destiny.`,
        `The Rook's intricate carvings appear to form a map that leads to a hidden location of immense importance, prompting a treasure hunt.`,
        `A group of spiritualists seeks to commune with the Rook's spirit, aiming to understand its true purpose and nature.`,
        `The Rook's surface displays ancient runes that reputedly hold the key to unlocking forgotten magic, drawing mystics from afar.`,
        `A talented sculptor endeavors to carve lifelike statues of legendary figures into the Rook's body, creating a monument to history.`,
        `An enigmatic architect believes that the Rook's design conceals a complex mechanism that can unlock new technological advancements.`,
        `The Rook's awakening coincides with a rare astronomical event known as the "Rook Meteor Shower," drawing enthusiasts to witness it.`,
        `A mysterious figure known as the "Rook Watcher" appears, claiming to have insights into the construct's true purpose and meaning.`,
        `A unique form of magical crystals is discovered within the Rook's interior, sparking research into their potential applications.`,
        `The Rook's presence mysteriously affects the growth patterns of nearby plants, leading botanists to study its potential impact on agriculture.`,
        `An ancient manuscript speaks of a legendary knight whose spirit resides within the Rook, guiding it to protect the realm.`,
        `A gifted musician composes a mesmerizing symphony that aims to convey the emotions and history embodied by the Rook's imposing presence.`,
        `The Rook's awakening coincides with a rare astronomical event known as the "Rook Nova," attracting astronomers to study its luminosity.`,
        `An order of scholars seeks to decode the Rook's carvings, believing they contain profound philosophical teachings.`,
        `The Rook's surface displays a mesmerizing light show during the night, attracting curious onlookers and stargazers.`
        ],
    ]

    let cityName = [
        'Battlement Crossing', 'Tapestrian Stronghold', 'Chalice Chambers', 'Guardstone Outpost', 'Pillared Vestibule', 'Hall of Mirrors', `Dungeon's End`, 'Balustrade Bastion', 'Hearthstone Hall', 'Watchtower Nexus', 'Throneguard Citadel', 'Great Hallway Haven', 'Portcullis Plaza', 'Banquet Balcony', 'Chamber Archway', 'Tower Turrets', 'Chalice Courtyard', 'Vaulted Vestry', 'Armored Atrium', 'Rampart Sanctuary', 'Thronegate', 'Citadel Halls', 'Chandelier Keep', 'Tapestria', 'Moatstone', 'Armory Hall', 'Towering Hearth', 'Grand Gallery', 'Vaultspire', 'Chambercross', 'Rampart Haven', 'Tapestry Towers', 'Courtyard Keep', 'Dungeonbridge', 'Banquethall', 'Courtwarden', `King's Cloister`, 'Foyerhelm', 'Drawbridge Hall', 'Ballistower Bastion', 'Serpentine Stronghold', 'Crowned Chambers', 'Wardenstone Outpost', 'Pillared Peristyle', 'Throne Room Theatre', 'Tower Watch', 'Gauntlet Gallery', 'Portico Plaza', 'Parapet Pavilion', 'Fortress Foyer', 'Galleried Guardhouse', 'Rampart Overlook', 'Gargoyle Bastion', 'Hearthwood Hall', 'Watchful Nexus', 'Courtly Citadel', 'Ballroom Haven', 'Chambergate', 'Tapestry Terrace', 'Citadel Keep', 'Thronecrest Citadel', 'Crenellated Cloister', 'Grand Ramparts', 'Tapestried Tower', 'Armory Archway', 'Vaulted Vestibule', 'Banquet Bastion', 'Hearthstone Hallway', 'Great Hall Gate', 'Watchtower Ward', 'Pillared Parapet', 'Towering Terrace', 'Chalice Chambers', 'Citadel Courtyard', 'Galleria Gateway', 'Rampart Rise', 'Tapestry Terrace', 'Guarded Gallery', 'Bastille Bridge', `Dungeon's Doorway`, 'Portcullis Path', 'Moatstone Manor', 'Towering Throne', 'Vaulted Veranda', 'Armored Arcade', 'Watchful Way', 'Balustrade Ballroom', 'Courtyard Citadel', 'Hearthstone Hideaway', 'Throneguard Terrace', 'Rampart Retreat', 'Chalice Cloister', 'Grand Gallery', 'Tapestria Towers', 'Citadel Commons', 'Galleried Gatehouse', 'Portico Promenade', 'Great Hall Haven', 'Watchtower Walk', 'Pillared Plaza', 'Doorhaven', 'Rookridge', 'Portcullis City', 'Rookgate', 'Doorkeep', 
        'Rookborough', 'Gatestone', 'Rookport', 'Lockwood', 'Rookshire', 'Threshold City', 'Rookwatch', 'Iron Door Citadel', 'Rookfall', 'Lockhaven', 'Gatewood', 'Rookreach', 'Doorberg', 'Rookstead', 'Iron Gate Township', 'Rookcrest', 'Portal City', 'Rookspire', 'Lockshire', 'Gatehaven', 'Rookstone', 'Portalburg', 'Rookshire', 'Doortown', 'Rookgate City', 'Iron Key Village', 'Rookcross', 'Portalwood', 'Doorstead', 'Lockridge', 'Rookway', 'Keyhold City', 'Rookwatch', 'Portalkeep', 'Lockport', 'Rooksville', 'Keygate', 'Doorberg', 'Lockcrest', 'Rookbridge', 'Keystone City', 'Doortown', 'Stonewall', 'Granite City', 'Marbleton', 'Sandstone Springs', 'Limestone Ridge', 'Quartzburg', 'Slateville', 'Boulder Heights', 'Cobblestone Cove', 'Jasper Junction', 'Amethystville', 'Feldspar Falls', 'Agateville', 'Onyx Haven', 'Gypsum Glen', 'Flintwood', 'Basalt Bay', 'Shaleton', 'Pumice Pines', 'Obsidian Outpost', 'Gemstone Gorge', 'Ruby Rapids', 'Topaz Terrace', 'Gneiss Glade', 'Crystal Creek', 'Mica Meadows', 'Slate Springs', 'Lapis Lazuli Lake', 'Siltstone Shores', 'Sandstone Strand', 'Marble Meadows', 'Chertville', 'Garnet Grove', 'Serpentine City', 'Soapstone Summit', 'Jasper Junction', 'Schistville', 'Petrified Park', 'Peridot Pass', 'Dolomite Dale', 'Rhyolite Ridge', 'Quartz Quarry', 'Travertine Town', 'Limestone Lake', 'Granite Glen', 'Slate Stream', 'Agate Arch', 'Shale Shore', 'Chert Coast', 'Gypsum Gulf', 'Jasper Jetty', 'Schist Spire', 'Serpentine Strand', 'Soapstone Sound', 'Rhyolite Reach', 'Travertine Trail', 'Obsidian Oasis', 'Peridot Pinnacle', 'Mica Mesa', 'Diorite Dell', 'Sandstone Slope', 'Granite Gardens', 'Limestone Lowlands', 'Onyx Overlook', 'Gneiss Grotto', 'Siltstone Steppes', 'Chert Chasm', 'Dolomite Divide', 'Amethyst Abyss', 'Rhyolite Ravine', 'Shale Sinkhole', 'Quartz Quarry', 'Lapis Lazuli Lagoon', 'Jasper Jungle', 'Soapstone Springs', 'Slate Sanctuary', 'Garnet Gully', 'Pumice Plateau', 'Sandstone Spires', 'Marble Mountain', 'Agate Ascent', 'Gneiss Grove', 'Basalt Bluff', 'Onyx Outlook', 'Chert Cliffs', 'Obsidian Overhang', 'Mica Mesa', 'Travertine Terrace', 'Slate Summit', 'Limestone Lake', 'Jasper Junction', 'Garnet Glade', 'Shale Shores', 'Sandstone Strand', 'Serpentine Sound', 'Rhyolite Reach', 'Quartz Quarry', 'Peridot Pass', 'Gypsum Gulf', 'Agate Arch', 'Aquafortress', 'Castlemere', 'Waterholm', 'Citadel Bay', 'Cascadon', 'Moatmere', 'Aquedale', 'Tidekeep', 'Castlehaven', 
        'Waterford', 'Wavefort', 'Portcove', 'Merestone', 'Castlemere', 'Aquamaris', 'Watercrest', 'Tidegate', 'Castlebay', 'Aquabridge', 'Riverhold', 'Castleport', 'Floodmoat', 'Waterglade', 'Castlebrook', 'Aquashade', 'Streamkeep', 'Castlebayou', 'Fountainreach', 'Waterfall', 'Castlewave', 'Aquasurge', 'Lakefort', 'Watershield', 'Castleflow', 'Tidemarsh', 'Aquaspring', 'Harborcastle', 'Waterstone', 'Castleisle', 'Riverwatch', 'Aquashore', 'Oceanfort', 'Castlehaven', 'Torrentkeep', 'Waterford', 'Castlecreek', 'Lakehold', 'Wateredge', 'Castlehaven', 'Baykeep', 'Snowcrest', 'Frostcastle', 'Icehaven', 'Winterfort', 'Glacialdale', 'Snowkeep', 'Icemere', 'Frostholm', 'Winterport', 'Snowridge', 'Icegate', 'Frostreach', 'Wintermoat', 'Snowstone', 'Iceshield', 'Glacierock', 'Winterhaven', 'Snowbrook', 'Frosthaven', 'Icecove', 'Winterfall', 'Snowbourne', 'Frostwatch', 'Icemoor', 'Wintercrest', 'Snowglen', 'Frostwood', 'Icefort', 'Winterbrook', 'Snowward', 'Frostisle', 'Winterhelm', 'Snowshield', 'Frostkeep', 'Iceshore', 'Winterport', 'Snowpeak', 'Frostberg', 'Icespire', 'Winterglade', 'Frostgate', 'Winterreach', 'Snowhaven', 'Frostmoor', 'Icemont', 'Winterwatch', 'Snowholm', 'Frostfield', 'Icereach', 'Winterstone', 'Hearthside', 'Bedrock', 'Mantlehaven', 'Foyerfield', 'Gallery Glen', 'Loftwick', 'Chambercross', 'Tapestry Terrace', 'Rugwood', 'Pillared Passage', 'Chandelier Court', 'Hallspring', 'Parlorhaven', 'Windowshire', 'Banisterberg', 'Cellardale', 'Balcony Bay', 'Vaultspire', 'Corbelled Cove', 'Kitchenbrook', 'Courtyardstead', 'Hallberg', 'Stairwellwood', 'Mantleside', 'Skylighton', 'Loungestead', 'Fireplace Fields', 'Vestibulewood', 'Archwayburg', 'Studybrook', 'Armorywood', 'Ceilingstead', 'Alcoveburg', 'Dresserham', 'Rugdale', 'Balustrade Bay', 'Hearthfield', 'Courtyardwick', 'Chandelierstead', 'Mantlewood', 'Galleryshore', 'Skylightberg', 'Hallwick', 'Windowshire', 'Banisterham', 'Loungestead', 'Cellardale', 'Kitchenbrook', 'Stairwellwood',
    ]
    function buildCity(){
        let size = 4 + rollDice(9)
        let cityContents = [
            `Hunter's guild : You can decide to accept quests and head out to complete the requirements, or you can turn it down and ask for another. This is as simple as going through the process again and seeing what you get a second time. Consider using the quests you DON’T take on as more aspects to your story. Other things are happening out in the world and maybe they can tie in to your character’s overall adventure.`,
            `Tavern :  In Colostle, you can trade any item for a night's stay, granting +1 to either COMBAT or EXPLORATION scores. This can be done once per city visit and requires at least one EXPLORATION phase outside the city before using the Tavern again. It's an excellent place to meet people, hear rumors, and get quests using the Quest Generation system from the Hunter's Guild. Return to the Tavern for your reward after completing a quest.`,
            `Merchant : The Merchant is an interesting character found in their shop in the city streets. For a variety of different prices (see each item) all manner of strange devices, weapons and supplies can be purchased. Some of them are single use - others are pieces of equipment you can equip. Currently selling: ${shuffleSlicePrint(merchant,1+rollDice(4))}`,
            `Housing District : a bustling residential area with stacked Rook husks, vendors, cultists, and other diverse inhabitants. Characters can meet contacts, gather information, and advance their adventure here. Anything can happen in this vibrant neighborhood.`
            ] 
        for (i=size-4;i>0;i--){
            let a = searchArray(Object.keys(cityBasics.amenities))
            cityContents.push(a + ' : ' + Object.values(cityBasics.amenities[a]))
        }
        loopPrintList(cityContents, "cityOutput")
        console.log(cityContents)
        
    }
    function guildQuest(){
        let distance = 2 + rollDice(3) 
        let reward = 2 + rollDice(1)
        return `${searchArray(huntersGuild[1])} It can be found ${searchArray(huntersGuild[0])}, ${distance} phases away. We will give you ${reward} treasures if you solve this problem.`
    }
    function rookling(){
        return searchArray(rooklings)
    }




/*****BATTLEMENTS*****/
    //Supplements
    let exposureEvents = [
        `TREASURE FALL - A stone capsule falls from the sky, triggered by your movement. Nothing attacks you, but the capsule contains a TREASURE within it. It goes into your inventory - you may be able to trade it later on in your adventure.`,
        `ASTROLITHIC ROOK CHASE - An Astrolithic Rook falls, but something about it seems wrong; it falls onto a distant rooftop, gets up, and turns in your direction. You see its eyes flash - it’s hunting you! Describe how you run away and hide from it (using other prompts from this EXPLORATION phase), or turn to fight! Create your opponent`,
        `EERIE SILENCE - Nothing happens. Maybe you got away with it this time.`,
        `ASTROLITHIC WRECKFALL - draw another card to see if you are hit by debris from the falling wreck of a downed Astrolithic Rook. ${searchArray(['You are hit and take 1 WOUND','You are not hit by the wreckfall!'])}`,
        `METEOR SHOWER - Tonnes of burning debris falls from the sky, perhaps once a Rook, but now just fiery balls of death. You’re caught out with nowhere to take cover, take one WOUND.`,
        `ASTROLITHIC ROOK APPEARS - create your opponent and then fight!`,
        `FLOCK OF ASTROLITHIC ROOKLINGS - A flock of smaller and nimble Astrolithic Rooklings descend from the sky, surrounding you with their fiery presence. Describe how you evade their attacks or engage in combat.`,

    
    ]
    //Exploration
    let battlementEvents = [
            `You come across a camp of nomads squatting in a large sturdy outbuilding on the edge of a rooftop. They have clearly been here for years, surviving a meagre frightened existence. Resting with them will heal one WOUND. ${searchArray(['Your actions cause you to be EXPOSED!','You manage to avoid unwanted danger'])}`,
            `A barren prairie plain stretches off as far as the eye can see. This must be the flat roof of a ROOM below. There is little cover out here. ${searchArray(['Your actions cause you to be EXPOSED!','You manage to avoid unwanted danger'])}`,
            `A battlement edge. Looking down you can see the hodge-podge labyrinth of other roofs below; some flat, some slanted, with towers and crenellations jutting up between. Moving on will mean climbing down to another rooftop. ${searchArray(['Your actions cause you to be EXPOSED!','You manage to avoid unwanted danger'])}`,
            `A strange, small outbuilding that looks like a small castle tower, perched atop the roof you were traversing. Looking inside you find ${searchArray([`${searchArray(items)}!`,' another person, wounded and cowering in fear.'])} ${searchArray(['Your actions cause you to be EXPOSED!','You manage to avoid unwanted danger.'])}`,
            `A crashed ruin of an Astrolithic Rook. This one has huge rectangular wings of panelled blue glass, all cracked and smashed. You might be able to find Helm, Arm or Mounted materials, but there is no Rookling inside. ${searchArray(['Your actions cause you to be EXPOSED!','You manage to avoid unwanted danger.'])}`,
            `A rooftop forest, perfect cover from the Astrolithics! Many trees, gathered together in a tight-knit group, force their gnarled roots up out of the stony brickwork that is the Colostle’s rooftop. It is quiet and calm here, no wind, maybe animals to hunt? ${searchArray(['Your actions cause you to be EXPOSED!','You manage to avoid unwanted danger.'])}`,
            `Ice wastes. This rooftop must house a cold Room below, as this whole rooftop is tundra. Arctic winds and ice - it is cold and the wind is piercing. ${searchArray(['Your actions cause you to be EXPOSED!','You manage to avoid unwanted danger.'])}`,
            `You see a lone nomad sprinting in fear, and then you look beyond them and see an Astrolithic Rook speeding along, a few feet above the ground. Do you help? ${searchArray(['Your actions cause you to be EXPOSED!','You manage to avoid unwanted danger.'])}`,
            `A hole in the roof. Looking down through it, you are faced first-hand with how dizzyingly high up you are. Through the wispy clouds you can see land masses and oceans below you like a patchwork blanket, miles away. Maybe you can climb through this hole and down to the Rafters of that Room? ${searchArray(['Your actions cause you to be EXPOSED!','You manage to avoid unwanted danger.'])}}`,
            `Another adventurer like yourself. They are friendly and tough and they agree to team up with you. If you are facing an Astrolithic Rook this turn they will assist you and reduce the Rook’s COMBAT score by 1. In your battle, describe how the other adventurer assists you. If you don’t meet a Rook this phase, the adventurer will heal one of your wounds and then you can decide if you continue to travel together or go your separate ways. ${searchArray(['Your actions cause you to be EXPOSED!','You manage to avoid unwanted danger.'])}`,
            `A way back down. Maybe a staircase or climbable wall. If you choose to return to a Room below, return to the general exploration section for Encounters therein.`,
            'Your actions cause you to be EXPOSED!',
            'Your actions cause you to be doubly EXPOSED!',
            `ABANDONED HIDEOUT - You stumble upon an abandoned hideout on the rooftops. The place seems to have been used by previous adventurers. Investigate the hideout to find useful items or clues to further your quest. ${searchArray(['Your actions cause you to be EXPOSED!','You manage to avoid unwanted danger.'])}`,
            `MIST-ENSHROUDED TREASURE - In the distance, you spot a gleaming object surrounded by thick mist. It looks like a valuable treasure. Decide whether to approach it, risking exposure to the Astrolithic Rooks, or play it safe and stay hidden. ${searchArray(['Your actions cause you to be EXPOSED!','You manage to avoid unwanted danger.'])}`,
            `LIGHT OF GUIDANCE - A mysterious light appears before you, leading the way to safety and revealing hidden paths across the Battlements. Follow the light's guidance to gain an advantage in your exploration.`,
            `SHADOW OF FEAR - The constant threat of the Astrolithic Rooks begins to take a toll on your nerves. ${searchArray(['Your actions cause you to be EXPOSED!','You manage to avoid unwanted danger.'])}`,
            `ASTROLITHIC RAY - A burst of searing energy shoots down from the sky, leaving scorch marks on the rooftops. Decide whether to take cover or risk exposure to find out what caused the blast. ${searchArray(['Your actions cause you to be EXPOSED!','You manage to avoid unwanted danger.'])}`,
            `REMNANTS OF A HERO - You come across the remains of a fallen hero who ventured into the Battlements before you. Search the area for any useful items they left behind or pay your respects to their memory.${searchArray(['Your actions cause you to be EXPOSED!','You manage to avoid unwanted danger.'])}`,
            `RIFT IN THE SKY - The sky above you tears open, revealing a shimmering portal to an unknown realm. Decide whether to investigate the mysterious rift or avoid it altogether. ${searchArray(['Your actions cause you to be EXPOSED!','You manage to avoid unwanted danger.'])}`,
            `ASTROLITHIC NEST - You stumble upon a nesting ground for Astrolithic Rooks. The ground trembles as they take flight, making you vulnerable to their attacks. Describe how you deal with the nesting Rooks. ${searchArray(['Your actions cause you to be EXPOSED!','You manage to avoid unwanted danger.'])}`,
            `GLIMMER OF HOPE - A faint glimmer of hope emerges amidst the gloomy rooftops. You spot a potential escape route to the lower rooms of the Colostle. Decide whether to risk the journey or continue exploring the Battlements. ${searchArray(['Your actions cause you to be EXPOSED!','You manage to avoid unwanted danger.'])}`,
            `SOLAR FLARE - A burst of intense light engulfs the area, temporarily blinding you and attracting the attention of Astrolithic Rooks. Draw another card to see if you can find cover before they arrive. ${searchArray(['Your actions cause you to be EXPOSED!','You manage to avoid unwanted danger.'])}`,
            `SILVER-LINED CLOUDS - The clouds above part for a moment, revealing a breathtaking view of the stars. The sight fills you with wonder and momentarily distracts you from the dangers around you. ${searchArray(['Your actions cause you to be EXPOSED!','You manage to avoid unwanted danger.'])}`,
            `UNEXPECTED ALLY - You encounter another traveler on the Battlements, a fellow Hunter seeking a way back down to the rooms. Decide whether to join forces or remain cautious and continue your journey alone. ${searchArray(['Your actions cause you to be EXPOSED!','You manage to avoid unwanted danger.'])}`,
            `CRUMBLING TOWER - The ground shakes as a nearby tower begins to collapse. Decide whether to seek shelter or risk crossing the unstable terrain for potential rewards. ${searchArray(['Your actions cause you to be EXPOSED!','You manage to avoid unwanted danger.'])}`,
            `ANCIENT MARKINGS - Strange markings etched into the rooftops catch your eye. They seem to be a part of an ancient script. Investigate the markings to decipher their meaning or press on with your exploration. ${searchArray(['Your actions cause you to be EXPOSED!','You manage to avoid unwanted danger.'])}`,
            `DIMENSIONAL ANOMALY - A mysterious distortion in space appears before you. It looks like a gateway to another dimension. Decide whether to investigate the anomaly or avoid meddling with unknown forces. ${searchArray(['Your actions cause you to be EXPOSED!','You manage to avoid unwanted danger.'])}`,
            `STARLIT GEM - You find a radiant gemstone glowing softly among the ruins. Its ethereal light could aid you in your journey. Decide whether to keep it with you or leave it behind to avoid drawing attention. ${searchArray(['Your actions cause you to be EXPOSED!','You manage to avoid unwanted danger.'])}`,
            `A way back down. Maybe a staircase or climbable wall. If you choose to return to a Room below, return to the general exploration section for Encounters therein. ${searchArray(['Your actions cause you to be EXPOSED!','You manage to avoid unwanted danger.'])}`,
            'Your actions cause you to be EXPOSED!',
            'Your actions cause you to be doubly EXPOSED!',
            `ASTROLITHIC STORM - The sky crackles with intense energy, and bolts of astral lightning strike down relentlessly. Draw another card to see if you can navigate safely through the storm. ${searchArray(['Your actions cause you to be EXPOSED!','You manage to avoid unwanted danger.'])}`,
            `FORGOTTEN ARTIFACT - A peculiar artifact lies hidden among the debris. Its purpose remains a mystery, but it might hold valuable information or powers. Decide whether to investigate or leave it undisturbed. ${searchArray(['Your actions cause you to be EXPOSED!','You manage to avoid unwanted danger.'])}`,
            `MIRROR LAKE - A large pool of water reflects the starry sky above. Gazing into the mirror-like surface reveals glimpses of the past and the future. Decide whether to risk exposing yourself to the visions or press on with your mission. ${searchArray(['Your actions cause you to be EXPOSED!','You manage to avoid unwanted danger.'])}`,
            `ILLUSIONARY PATHWAY - You encounter a surreal and winding pathway that seems to shift and change before your eyes. Draw another card to see if you can navigate through the illusion safely. ${searchArray(['Your actions cause you to be EXPOSED!','You manage to avoid unwanted danger.'])}`,
            `ECHOING WHISPERS - Eerie whispers fill the air, seemingly emanating from the very rooftops. The voices carry cryptic messages and warnings. Decide whether to follow their guidance or ignore the haunting whispers. ${searchArray(['Your actions cause you to be EXPOSED!','You manage to avoid unwanted danger.'])}`,
            `SHIMMERING PORTAL - You stumble upon a shimmering portal that seems to lead to another part of the Battlements or perhaps another realm altogether. Decide whether to take the risk and step through or avoid the unknown gateway. ${searchArray(['Your actions cause you to be EXPOSED!','You manage to avoid unwanted danger.'])}`,
            `DUST STORM - A sudden dust storm engulfs the area, limiting visibility and making it challenging to find cover. Draw another card to see if you can navigate safely through the storm. ${searchArray(['Your actions cause you to be EXPOSED!','You manage to avoid unwanted danger.'])}`,
            `GHOSTLY SPECTERS - Ghostly apparitions appear before you, haunting the Battlements with their mournful presence. Decide whether to investigate the spirits or avoid their gaze. ${searchArray(['Your actions cause you to be EXPOSED!','You manage to avoid unwanted danger.'])}`,
            `FRACTURED REALITY - Reality itself seems to bend and twist, creating rifts and strange phenomena. Draw another card to see how you react to the altered environment. ${searchArray(['Your actions cause you to be EXPOSED!','You manage to avoid unwanted danger.'])}`,
            `ASTROLITHIC STRAY - A lost and confused Astrolithic Rook stumbles upon your location. It doesn't appear hostile but is unpredictable. Describe how you handle the encounter. ${searchArray(['Your actions cause you to be EXPOSED!','You manage to avoid unwanted danger.'])}`,
            `SOUND OF WAR - Distant sounds of battle echo across the rooftops. Draw another card to see if you investigate the source of the conflict or decide to steer clear of the danger. ${searchArray(['Your actions cause you to be EXPOSED!','You manage to avoid unwanted danger.'])}`,
            `COSMIC PHENOMENON - The night sky erupts with a stunning cosmic display, with celestial lights and colors dancing above. The sight mesmerizes you, momentarily forgetting the peril around you. ${searchArray(['Your actions cause you to be EXPOSED!','You manage to avoid unwanted danger.'])}`,
            `CRYPTIC SYMBOLS - Mysterious symbols appear etched on the rooftops, forming a trail leading to an unknown destination. Decide whether to follow the symbols or continue your exploration independently. ${searchArray(['Your actions cause you to be EXPOSED!','You manage to avoid unwanted danger.'])}`,
            `ABANDONED CAMP - You stumble upon an abandoned campsite, complete with scattered belongings and remnants of a past traveler. Investigate the campsite to uncover clues or avoid the area to remain undetected. ${searchArray(['Your actions cause you to be EXPOSED!','You manage to avoid unwanted danger.'])}`

    ]
 
    