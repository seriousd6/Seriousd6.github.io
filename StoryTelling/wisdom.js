//Chance and array manipulation methods
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

/*==================================================================================*/
/*-----------------------------Page Scripts Below-----------------------------------*/
/*==================================================================================*/


function wisdom(){
    document.getElementById("Wisdom").innerHTML = ""
    let quoteArray = [
        `We are all apprentices in a craft where no one ever becomes a master. ~Ernest Hemingway`,
        `Write. Just do it. Then again. Then some more. And more. Do not wait for inspiration; if you do enough of it often enough, inspiration will eventually come. ~Nancy Kress`,
        `The first draft is just you telling yourself the story. ~Terry Pratchett`,
        `Almost all good writing begins with terrible first efforts. You need to start somewhere. ~Anne Lamott`,
        `Writing is the only thing that, when I do it, I don’t feel I should be doing something else. ~Gloria Steinem`,
        `Writing is a form of therapy; sometimes I wonder how all those who do not write, compose or paint can manage to escape the madness, melancholia, the panic fear which is inherent in a human situation. ~Graham Greene`,
        `I do not over-intellectualise the production process. I try to keep it simple: Tell the damned story. ~Tom Clancy`,
        `You don’t start out writing good stuff. You start out writing crap and thinking it’s good stuff, and then gradually you get better at it. ~Octavia E. Butler`,
        `Start writing, no matter what. The water does not flow until the faucet is turned on. ~Louis L’Amour`,
        `You learn to write by writing. ~William Zinsser`,
        `Everybody walks past a thousand story ideas every day. The good writers are the ones who see five or six of them. Most people don’t see any. ~Orson Scott Card`,
        `Protect the time and space in which you write. Keep everybody away from it, even the people who are most important to you. ~Zadie Smith`,
        `A word after a word after a word is power. ~Margaret Atwood`,
        `You get ideas from daydreaming. You get ideas from being bored. You get ideas all the time. The only difference between writers and other people is we notice when we’re doing it. ~Neil Gaiman`,
        `Writing a novel is like building a wall brick by brick; only amateurs believe in inspiration. ~Frank Yerby`,
        `Doing it all the time, whether or not we are in the mood, gives us ownership of our writing ability. It takes it out of the realm of conjuring where we stand on the rock of isolation, begging the winds for inspiration, and it makes it something as do-able as picking up a hammer and pounding a nail. Writing may be an art, but it is certainly a craft. It is a simple and workable thing that can be as steady and reliable as a chore. ~Julia Cameron`,
        `I can shake off everything as I write; my sorrows disappear, my courage is reborn. ~Anne Frank`,
        `When asked, ‘How do you write?’ I invariably answer, ‘one word at a time’. ~Stephen King`,
        `A professional writer is an amateur who didn’t quit. ~Richard Bach`,
        `Stop trying to write sentences and start trying to write stories. ~James Patterson`,
        `One thing that helps is to give myself permission to write badly. I tell myself that I’m going to do my five or 10 pages no matter what, and that I can always tear them up the following morning if I want. I’ll have lost nothing—writing and tearing up five pages would leave me no further behind than if I took the day off. ~Lawrence Block`,
        `I write to discover what I know. ~Flannery O’Connor`,
        `Exercise the writing muscle every day, even if it is only a letter, notes, a title list, a character sketch, a journal entry. Writers are like dancers, like athletes. Without that exercise, the muscles seize up. ~Jane Yolen`,
        `It’s none of their business that you have to learn to write. Let them think you were born that way. ~Ernest Hemingway`,
        `What I really wanted was every kind of life, and the writer’s life seemed the most inclusive. ~Susan Sontag`,
        `Life can’t defeat a writer who is in love with writing, for life itself is a writer’s lover until death. ~Edna Ferber`,
        `Just write every day of your life. Read intensely. Then see what happens. Most of my friends who are put on that diet have very pleasant careers. ~Ray Bradbury`,
        `Fiction can be more real to the reader than reality itself because fiction is the essence of life. ~James N. Frey`,
        `If there’s a book that you want to read, but it hasn’t been written yet, then you must write it. ~Toni Morrison`,
        `Let me live, love, and say it well in good sentences. ~Sylvia Plath`,
        `You should write because you love the shape of stories and sentences and the creation of different words on a page. Writing comes from reading, and reading is the finest teacher of how to write. ~Annie Proulx`,
        `You can make anything by writing. ~C.S. Lewis`,
        `Don’t try to figure out what other people want to hear from you; figure out what you have to say. It’s the one and only thing you have to offer. ~Barbara Kingsolver`,
        `Read like a butterfly, write like a bee. ~Philip Pullman`,
        `A person is a fool to become a writer. His only compensation is absolute freedom. He has no master except his own soul, and that, I am sure, is why he does it. ~Roald Dahl`,
        `Get it down. Take chances. It may be bad, but it’s the only way you can do anything really good. ~William Faulkner`,
        `Write what should not be forgotten. ~Isabel Allende`,
        `It seems to me that what writers are supposed to do is use their imaginations. Imagination is one of the most important things we have. ~Susanna Clarke`,
        `Writing is its own reward. ~Henry Miller`,
        `The most important thing in writing is to have written. I can always fix a bad page. I can’t fix a blank one. ~Nora Roberts`,
        `You don’t write because you want to say something, you write because you have something to say. ~F. Scott Fitzgerald`,
        `Probably the most important thing I’ve learned is that if I don’t make the time to do the writing, the writing won’t get done. ~Judy Reeves`,
        `I don’t wait for moods. You accomplish nothing if you do that. Your mind must know it has got to get down to work. ~Pearl S. Buck`,
        `When I’m writing I know I’m doing the thing I was born to do. ~Anne Sexton`,
        `If you’re going to try, go all the way. Otherwise, don’t even start. This could mean losing girlfriends, wives, relatives and maybe even your mind. It could mean not eating for three or four days. It could mean freezing on a park bench. It could mean jail. It could mean derision. It could mean mockery–isolation. Isolation is the gift. All the others are a test of your endurance, of how much you really want to do it. And, you’ll do it, despite rejection and the worst odds. And it will be better than anything else you can imagine. If you’re going to try, go all the way. There is no other feeling like that. You will be alone with the gods, and the nights will flame with fire. You will ride life straight to perfect laughter. It’s the only good fight there is. ~Charles Bukowski`,
        `All glory comes from daring to begin. ~Ruskin Bond`,
        `Write what disturbs you, what you fear, what you have not been willing to speak about. Be willing to be split open. ~Natalie Goldberg`,
        `There are three rules for writing a novel. Unfortunately, no one knows what they are. ~W. Somerset Maugham`,
        `Great is the art of beginning, but greater is the art of ending.  ~Henry Wadsworth Longfellow`,
        `Love the writing, love the writing, love the writing… the rest will follow. ~Jane Yolen`,
        `The ability of writers to imagine what is not the self, to familiarize the strange and mystify the familiar, is the test of their power. ~Toni MorrisonToni Morrison Quote`,
        `Fill your paper with the breathings of your heart. ~William Wordsworth`,
        `The writer is an explorer. Every step is an advance into a new land. ~Ralph Waldo Emerson`,
        `I write entirely to find out what I’m thinking, what I’m looking at, what I see, and what it means. What I want and what I fear. ~Joan Didion`,
        `They who dream by day are cognizant of many things which escape those who dream by night. ~Edgar Allan Poe`,
        `The art of writing is the art of discovering what you believe. ~Gustav Flaubert`,
        `I know nothing in the world that has as much power as a word. Sometimes I write one, and look at it, until it shines. ~Emily Dickinson`,
        `That’s what you’re looking for as a writer when you’re working. You’re looking for your own freedom. ~Philip Roth`,
        `Imagination is the beginning of creation. You imagine what you desire, you will what you imagine and at last you create what you will. ~George Bernard Shaw`,
        `Creativity is a combination of discipline and childlike spirit. ~Robert Greene`,
        `Writing is the painting of the voice. ~Voltaire`,
        `It’s the possibility of having a dream come true that makes life interesting. ~Paulo Coelho`,
        `I have fallen in love with the imagination. And if you fall in love with the imagination, you understand that it is a free spirit. It will go anywhere and it can do anything. ~Alice Walker`,
        `Any writer worth his salt writes to please himself… it’s a self-exploratory operation that is endless. ~Harper Lee`,
        `If you have built castles in the air, your work need not be lost; that is where they should be. Now put foundations under them. ~Henry David Thoreau`,
        `There are significant moments in everyone’s day that can make literature. That’s what you ought to write about. ~Raymond Carver`,
        `Keep asking questions because people will always want to know the answer. Open with a question and don’t answer it until the end. ~Lee Child`,
        `But when people say, did you always want to be a writer? I have to say no! I always was a write. ~Ursula K. Le Guin`,
        `You can’t use up creativity. The more you use, the more you have. ~Maya Angelou`,
        `If I waited for perfection, I would never write a word. ~Margaret Atwood`,
        `You should write stories because you love the shape of stories and sentences and the creation of different words on a page. ~Annie Proulx`,
        `I write only because there is a voice within me that will not be stilled. ~Sylvia Plath`,
        `If you do not hear music in your words, you have put too much thought into your writing and not enough heart. ~Terry Brooks`,
        `If you are in difficulties with a book, try the element of surprise: attack it at an hour when it isn’t expecting it. ~H.G. Wells`,
        `Words are sacred. They deserve respect. If you get the right ones, in the right order, you can nudge the world a little. ~Tom Stoppard`,
        `The secret of it all is to write… without waiting for a fit time or place. ~Walt Whitman`,
        `No one else sees the world the way you do, so no one else can tell the stories that you have to tell. ~Charles de Lint`,
        `Successful writing is one part inspiration and two parts sheer stubbornness. ~Gillian Flynn`,
        `I write books because I have always been fascinated by stories and language, and because I love thinking about what makes people tick. ~Lois LowryLois Lowry Quote`,
        `As a writer, you should not judge. You should understand. ~Ernest Hemingway`,
        `If you don’t see the book you want on the shelf, write it. ~Beverly Cleary`,
        `When all else fails, write what your heart tells you. You can’t depend on your eyes, when your imagination is out of focus. Mark Twain`,
        `Stories are light. Light is precious in a world so dark. Begin at the beginning. Make some light. ~Kate DiCamillo`,
        `A writer is a writer not because she writes well and easily, because she has amazing talent, because everything she does is golden. In my view a writer is a writer because even when there is no hope, even when nothing you do shows any sign of promise, you keep writing anyway. ~Junot Diaz`,
        `The first draft is you just telling yourself the story. ~Terry Pratchett`,
        `Write a page a day. Only 300 words and in a year you have written a novel. ~Stephen King`,
        `The secret of getting ahead is getting started. ~Agatha Christie`,
        `The job of the novelist is to invent: to embroider, to color, to embellish, to make things up. ~Donna Tart`,
        `Writing is an act of faith, not a grammar trick. ~E.B. White`,
        `Good stories are not written. They are rewritten. ~Phyllis Whitney`,
        `The first draft is a skeleton. Just bare bones. The rest of the story comes later with revising. ~Judy Bloom`,
        `When you are describing a shape, or sound, or tint, don’t state the matter plainly, but put it in a hint. And learn to look at all things with a sort of mental squint. ~Lewis Carroll`,
        `You may not write well every day, but you can always edit a bad page. You can’t edit a blank page. ~Jodi Picoult`,
        `Perfection is finally attained not when there is no longer anything to add, but when there is no longer anything to take away. ~Antoine de Saint-Exupery`,
        `The secret to editing your work is simple: You need to become its reader instead of its writer. ~Zadie Smith`,
        `I’m writing a first draft and reminding myself that I’m simply shoveling sand into a box so that later I can build castles. ~Shannon Hale`,
        `Don’t labor over a little cameo work in which every word is to be perfect. Technique holds a reader from sentence to sentence, but only content will stay in his mind. ~Joyce Carol Oates`,
        `If you fall in love with the vision and not your words, the rewriting will become easier. ~Nora DeLoach`,
        `Be willing and unafraid to write badly, because often the bad stuff clears the way for good, or forms a base on which to build something better. ~Jennifer Egan`,
        `Plot is no more than footprints left in the snow after your characters have run by on their way to incredible destinations. ~Ray Bradbury`
    ]
document.getElementById("Wisdom").innerHTML = searchArray(quoteArray)
//console.log(searchArray(template))
}

