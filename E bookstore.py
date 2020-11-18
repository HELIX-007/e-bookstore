# Title 
print('         *********************************')
print('          Hello,Welcome to AMA ebookstore')
print('         *********************************')
print('please select your desired genres\nscifi,horror,mystery,novel,selfhelp')

#Genre and Books available 
scifi=['The Martian,','Frankenstein,','I,Robot,','Ready Player One,','The Time Machine,'] 
horror=['The Shining,','Haunting Of Hill House,','The Silence of the Lambs,','The Exorcist,','American Psycho,']
mystery=['Sharp Objects,','Double Cross,','Angels and Demons,','Battle Ground,','The Da Vinci Code,']
novel=['To Kill a Mockingbird,','The Great Gatsby,','Pride and prejudice,','The Lord Of The Rings,','War and Peace,']
selfhelp=['Think and grow rich,','The subtle art of not giving a fuck,','The power of habit,','12 rules for life,','the 48 laws of power,']
genre=[scifi,horror,mystery,novel,selfhelp]
Genre=['scifi','horror','mystery','novel','selfhelp']


#Genre input
g=input('type your desired genre : ')
for i in Genre:
    if i == g:
        a=Genre.index(i)
        print(*genre[a])

#book description and price
def book_details():
    global Genre
    global b
    global a
    if b == "The Martian,":
        print("""                  ********About the story********
Six days ago, astronaut Mark Watney became one of the first people to walk on Mars.
Now, he’s sure he’ll be the first person to die there.
After a dust storm nearly kills him and forces his crew to evacuate while thinking him dead,
Mark finds himself stranded and completely alone with no way to even signal Earth that he’s alive—and even if he could get word out,
his supplies would be gone long before a rescue could arrive.
Chances are, though, he won’t have time to starve to death.
The damaged machinery, unforgiving environment,
or plain-old “human error” are much more likely to kill him first.But Mark isn’t ready to give up yet.
Drawing on his ingenuity, his engineering skills — and a relentless,
dogged refusal to quit — he steadfastly confronts one seemingly insurmountable obstacle after the next.
Will his resourcefulness be enough to overcome the impossible odds against him?""")
        print("\nAUTHOR - ANDY WEIR" )
        print("\nPAPER BACK - Rs 500")
        
        
    elif b == "Frankenstein,":
        print("""                  ********About the story********
Victor Frankenstein, a Swiss student of natural science creates an artificial man from pieces of corpses and brings his creature to life.
Though it initially seeks affection, the monster inspires loathing in everyone who meets it.
Lonely and miserable, the monster turns upon its creator, who eventually loses his life.""")
        print("\nAUTHOR - MARY SHELLY" )
        print("\nPAPER BACK - Rs 300")
        
        
    elif b == "I,Robot,":
        print("""                  ********About the story********
A collection of nine short stories that imagines the development of “positronic” (humanlike),
with a form of artificial intelligence) robots and wrestles with the moral implications of the technology. """)
        print("\nAUTHOR -  ISAAC ASIMOV" )
        print("\nPAPER BACK - Rs 310")
       
        
    elif b == "Ready Player One,":
        print("""                  ********About the story********
IN THE YEAR 2044, reality is an ugly place.
The only time teenage Wade Watts really feels alive is when he's jacked into the virtual utopia known as the OASIS.
Wade's devoted his life to studying the puzzles hidden within this world's digital confines,
puzzles that are based on their creator's obsession with the pop culture of decades past and that promise massive power and fortune to whoever can unlock them.
But when Wade stumbles upon the first clue, he finds himself beset by players willing to kill to take this ultimate prize.
The race is on, and if Wade's going to survive, he'll have to win—and confront the real world he's always been so desperate to escape.""")
        print("\nAUTHOR -  ERNEST CLINE" )
        print("\nPAPER BACK - Rs 470")
        
        
    elif b == "The Time Machine,":
        print("""                  ********About the story********
A Victorian scientist, claims that he has invented a device that enables him to travel through time,
and has visited the future, arriving in the year 802,701 in what had once been London.
""")
        print("\nAUTHOR - H.G.WELLS" )
        print("\nPAPER BACK - Rs 150")
        
        
    elif b == "The Shining,":
        print("""                  ********About the story********
Jack Torrance's new job at the Overlook Hotel is the perfect chance for a fresh start.
As the off-season caretaker at the atmospheric old hotel,
he'll have plenty of time to spend reconnecting with his family and working on his writing.
But as the harsh winter weather sets in, the idyllic location feels ever more remote...and more sinister.
And the only one to notice the strange and terrible forces gathering around the Overlook is Danny Torrance, a uniquely gifted five-year-old.""")
        print("\nAUTHOR - STEPHEN KING" )
        print("\nPAPER BACK - Rs 300")
        
        
    elif b == "Haunting Of Hill House,":
        print("""                  ********About the story********
Four seekers who arrive at a notoriously unfriendly pile called Hill House:
Dr. Montague, an occult scholar looking for solid evidence of a "haunting";
Theodora, the lighthearted assistant;
Eleanor, a friendless, fragile young woman well acquainted with poltergeists;
and Luke, the future heir of Hill House.
At first, their stay seems destined to be merely a spooky encounter with inexplicable phenomena.
But Hill House is gathering its powers—and soon it will choose one of them to make its own.""")
        print("\nAUTHOR - SHIRLEY JACKSON" )
        print("\nPAPER BACK - Rs 290")
        
        
    elif b == "The Silence of the Lambs,":
        print("""                  ********About the story********
A young FBI trainee. An evil genius locked away for unspeakable crimes.
A plunge into the darkest chambers of a psychopath's mind--in the deadly search for a serial killer.""")
        print("\nAUTHOR - THOMAS HARRIS" )
        print("\nPAPER BACK - Rs 350")
        
        
    elif b == "The Exorcist,":
        print("""                  ********About the story********
The terror begins unobtrusively. Noises in the attic.
In the child's room, an odd smell, the displacement of furniture, an icy chill.
At first, easy explanations are offered.
Then frightening changes begin to appear in eleven-year-old Regan.
Medical tests fail to shed any light on her symptoms, but it is as if a different personality has invaded her body.
Father Damien Karras, a Jesuit priest, is called in.
Is it possible that a demonic presence has possessed the child? Exorcism seems to be the only answer...""")
        print("\nAUTHOR - WILLIAM PETER BLATTY" )
        print("\nPAPER BACK - Rs 940")
        
        
    elif b == "American Psycho,":
        print("""                  ********About the story********
Patrick Bateman is twenty-six and he works on Wall Street, he is handsome, sophisticated, charming and intelligent. He is also a psychopath.
Taking us to head-on collision with America's greatest dream—and its worst nightmare—American Psycho is bleak, bitter, black comedy about a world
we all recognise but do not wish to confront.""")
        print("\nAUTHOR - BRET EASTON ELLIS" )
        print("\nPAPER BACK - Rs 470")
       
        
    elif b == "Sharp Objects":
        print("""                  ********About the story********
Fresh from a brief stay at a psych hospital,
reporter Camille Preaker faces a troubling assignment: she must return to her tiny hometown to cover the unsolved murder of a preteen girl and the disappearance of another.
For years, Camille has hardly spoken to her neurotic, hypochondriac mother or to the half-sister she barely knows: a beautiful thirteen-year-old with an eerie grip on the town.
Now, installed in her old bedroom in her family's Victorian mansion, Camille finds herself identifying with the young victims—a bit too strongly.
Dogged by her own demons, she must unravel the psychological puzzle of her own past if she wants to get the story—and survive this homecoming.""")
        print("\nAUTHOR - GILLIAN FLYNN" )
        print("\nPAPER BACK - Rs 480")
        
        
    elif b == "Double Cross,":
        print("""                  ********About the story********
Just when Alex thought his life was calming down into a routine of patients and therapy sessions, he finds himself back in the game--this time to catch a criminal mastermind like no other.
A spate of elaborate murders in Washington D.C. have the whole East Coast on edge.
They are like nothing Alex Cross and his new girlfriend, Detective Brianna Stone, have ever seen.
With each murder, the case becomes increasingly complex.
There's only one thing Alex knows: the killer adores an audience.
As victims are made into gruesome spectacles citywide, inducing a media hysteria, it becomes clear to Alex that the man he's after is a genius of terror--and he's after fame.
The killer has the whole city by its strings--and he'll stop at nothing to become the most terrifying star that Washington D.C. has ever seen""")
        print("\nAUTHOR - JAMES PATTERSON" )
        print("\nPAPER BACK - Rs 890")
        
        
    elif b == "Angels and Demons,":
        print("""                  ********About the story********
World-renowned Harvard symbologist Robert Langdon is summoned to a Swiss research facility to analyze a cryptic symbol seared into the chest of a murdered physicist.
What he discovers is unimaginable: a deadly vendetta against the Catholic Church by a centuries-old underground organization -- the Illuminati.
In a desperate race to save the Vatican from a powerful time bomb, Langdon joins forces in Rome with the beautiful and mysterious scientist Vittoria Vetra.
Together they embark on a frantic hunt through sealed crypts, dangerous catacombs, and deserted cathedrals,
and into the depths of the most secretive vault on earth...the long-forgotten Illuminati lair.""")
        print("\nAUTHOR - DAN BROWN" )
        print("\nPAPER BACK - Rs 250")
       
        
    elif b == "Battle Ground,":
        print("""                  ********About the story********
THINGS ARE ABOUT TO GET SERIOUS FOR HARRY DRESDEN, CHICAGO’S ONLY PROFESSIONAL WIZARD, in the next entry in the #1 New York Times bestselling Dresden Files.
Harry has faced terrible odds before.
He has a long history of fighting enemies above his weight class.
The Red Court of vampires.The fallen angels of the Order of the Blackened Denarius. The Outsiders.
But this time it’s different. A being more powerful and dangerous on an order of magnitude beyond what the world has seen in a millennium is coming.
And she’s bringing an army. The Last Titan has declared war on the city of Chicago, and has come to subjugate humanity, obliterating any who stand in her way.
Harry’s mission is simple but impossible: Save the city by killing a Titan. And the attempt will change Harry’s life, Chicago, and the mortal world forever.""")
        print("\nAUTHOR - JIM BUTCHER" )
        print("\nPAPER BACK - Rs 1300")
        
        
    elif b == "The Da Vinci Code,":
        print("""                  ********About the story********
While in Paris, Harvard symbologist Robert Langdon is awakened by a phone call in the dead of the night.
The elderly curator of the Louvre has been murdered inside the museum, his body covered in baffling symbols.
As Langdon and gifted French cryptologist Sophie Neveu sort through the bizarre riddles,
they are stunned to discover a trail of clues hidden in the works of Leonardo da Vinci—clues visible for all to see and yet ingeniously disguised by the painter.
Even more startling, the late curator was involved in the Priory of Sion—a secret society,
whose members included Sir Isaac Newton, Victor Hugo, and Da Vinci—and he guarded a breathtaking historical secret.
Unless Langdon and Neveu can decipher the labyrinthine puzzle—while avoiding the faceless adversary who shadows their every move—the explosive,
ancient truth will be lost forever.""")
        print("\nAUTHOR - DAN BROWN" )
        print("\nPAPER BACK - Rs 400")
       
        
    elif b == "To Kill a Mockingbird,":
        print("""                  ********About the story********
"Shoot all the bluejays you want, if you can hit 'em, but remember it's a sin to kill a mockingbird."

A lawyer's advice to his children as he defends the real mockingbird of Harper Lee's classic novel—a black man charged with the rape of a white girl.
Through the young eyes of Scout and Jem Finch,Harper Lee explores with rich humor and unswerving honesty the irrationality of adult attitudes toward race and class
in the Deep South of the 1930s.The conscience of a town steeped in prejudice, violence, and hypocrisy is pricked by the stamina and quiet heroism
of one man's struggle for justice—but the weight of history will only tolerate so much.""")
        print("\nAUTHOR - HARPER LEE" )
        print("\nPAPER BACK - Rs 500")
        
        
    elif b == "The Great Gatsby,":
        print("""                  ********About the story********
The tragic story of Jay Gatsby, a self-made millionaire, and his pursuit of Daisy Buchanan, a wealthy young woman whom he loved in his youth.""")
        print("\nAUTHOR - F. SCOTT FITZGERALD" )
        print("\nPAPER BACK - Rs 150")
       
        
    elif b == "Pride and prejudice,":
        print("""                  ********About the story********
A classic of English literature, written with incisive wit and superb character delineation, it centres on the turbulent relationship
between Elizabeth Bennet, the daughter of a country gentleman, and Fitzwilliam Darcy, a rich aristocratic landowner.""")
        print("\nAUTHOR - JANE AUSTEN" )
        print("\nPAPER BACK - Rs 150")
        
        
    elif b == "The Lord Of The Rings,":
        print("""                  ********About the story********
One Ring to rule them all, One Ring to find them, One Ring to bring them all and in the darkness bind them

In ancient times the Rings of Power were crafted by the Elven-smiths, and Sauron, the Dark Lord, forged the One Ring, filling it with his own power
so that he could rule all others.But the One Ring was taken from him, and though he sought it throughout Middle-earth, it remained lost to him.
After many ages it fell by chance into the hands of the hobbit Bilbo Baggins.

From Sauron's fastness in the Dark Tower of Mordor, his power spread far and wide.
Sauron gathered all the Great Rings to him, but always he searched for the One Ring that would complete his dominion.

When Bilbo reached his eleventy-first birthday he disappeared, bequeathing to his young cousin Frodo
the Ruling Ring and a perilous quest: to journey across Middle-earth, deep into the shadow of the Dark Lord, and destroy the Ring
by casting it into the Cracks of Doom.

The Lord of the Rings tells of the great quest undertaken by Frodo and the Fellowship of the Ring: Gandalf the Wizard; the hobbits Merry,
Pippin, and Sam; Gimli the Dwarf; Legolas the Elf; Boromir of Gondor; and a tall, mysterious stranger called Strider.""")
        print("\nAUTHOR - J.R.R. TOLKIEN" )
        print("\nPAPER BACK - Rs 700")
        
        
    elif b == "War and Peace,":
        print("""                  ********About the story********
War and Peace is an affirmation of life itself, `a complete picture', as a contemporary reviewer put it
of everything in which people find their happiness and greatness, their grief and humiliation'.War and Peace begins in the Russian city of St. Petersburg in 1805,
as fear of Napoleon's ongoing war making begins to set in.
Andrey Bolkonsky and Nikolay Rostov go to the Austrian front under General Kutuzov, to engage with Napoleon's troops.""")
        print("\nAUTHOR - LEO TOLSTOY" )
        print("\nPAPER BACK - Rs 350")
        
        
    elif b == "Think and grow rich,":
        print("""                  ********About the story********
Think and Grow Rich, based on the author’s famed Law of Success,
represents the distilled wisdom of distinguished men of great wealth and achievement. 

Andrew Carnegie’s magic formula for success was the direct inspiration for this book.
Carnegie demonstrated its soundness when his coaching brought fortunes
to those young men to whom he had disclosed his secret.""")
        print("\nAUTHOR - NAPOLEON HILL" )
        print("\nPAPER BACK - Rs 910")
        
        
    elif b == "The subtle art of not giving a fuck,":
        print("""                  ********About the story********
“Not everybody can be extraordinary—there are winners and losers in society, and some of it is not fair or your fault.”
Manson advises us to get to know our limitations and accept them—this, he says, is the real source of empowerment.
Once we embrace our fears, faults, and uncertainties—once we stop running from and avoiding, and start confronting painful truths—we can begin
to find the courage and confidence we desperately seek.
“In life, we have a limited amount of fucks to give. So you must choose your fucks wisely.”
Manson brings a much-needed grab-you-by-the-shoulders-and-look-you-in-the-eyes moment of real-talk, filled with entertaining stories and profane, ruthless humor""")
        print("\nAUTHOR - MARK MANSON" )
        print("\nPAPER BACK - Rs 300")
        
        
    elif b == "The power of habit,":
        print("""                  ********About the story********
A young woman walks into a laboratory. Over the past two years, she has transformed almost every aspect of her life.
She has quit smoking, run a marathon, and been promoted at work. The patterns inside her brain, neurologists discover, have fundamentally changed.

Marketers at Procter & Gamble study videos of people making their beds.
They are desperately trying to figure out how to sell a new product called Febreze, on track to be one of the biggest flops in company history.
Suddenly, one of them detects a nearly imperceptible pattern—and with a slight shift in advertising, Febreze goes on to earn a billion dollars a year.

An untested CEO takes over one of the largest companies in America.
His first order of business is attacking a single pattern among his employees—how they approach worker safety—and soon the firm,
Alcoa, becomes the top performer in the Dow Jones.

What do all these people have in common?
They achieved success by focusing on the patterns that shape every aspect of our lives.""")
        print("\nAUTHOR - CHARLES DUHIGG" )
        print("\nPAPER BACK - Rs 250")
        
        
    elif b == "12 rules for life,":
        print("""                  ********About the story********
What does everyone in the modern world need to know?
Renowned psychologist Jordan B. Peterson's answer to this most difficult of questions
uniquely combines the hard-won truths of ancient tradition with the stunning revelations of cutting-edge scientific research.""")
        print("\nAUTHOR - JORDAN PETERSON" )
        print("\nPAPER BACK - Rs 410")
        
        
    elif b == "the 48 laws of power,":
        print("""                  ********About the story********
This amoral, cunning, ruthless, and instructive book synthesizes the philosophies of Machiavelli,
Sun Tzu, and Carl Von Clausewitz with the historical legacies of statesmen, warriors, seducers, and con men throughout the ages""")
        print("\nAUTHOR - ROBERT GREENE" )
        print("\nPAPER BACK - Rs 460")
        
        
    else:
        print("Invalid input")
    
    
 
    
#book input
b=input("enter the desired book : ")
b+=","
def book_input():
    global Genre 
    global b
    global a
    for i in genre[a]:
        if i == b:
            book_details()
            d=input("Press 1 to add to cart and 2 to go back : ")
            if d == "1":
                print ("Added to cart")
                continue_payment=input("Press 1 to proceed to payment Press 2 to continue shopping : ")
                if continue_payment == "1":
                    print("CONFIRMATION OF ORDER")
                elif continue_payment == "2":
                    g=input('type your desired genre : ')
                    for i in Genre:
                        if i == g:
                            a=Genre.index(i)
                            print(*genre[a])
                    b=input("enter the desired book : ")
                    b+=","
                    book_input()
                
            elif d == "2":
                b=input("Enter the desired book : ")
                book_details()
                d=input("Press 1 to add to cart and 2 to go back : ")
                if d == "1":
                    print ("Added to cart")
                    continue_payment=input("Press 1 to proceed to payment Press 2 to continue shopping : ")
                    if continue_payment == "1":
                        print("CONFIRMATION OF ORDER")
                    elif continue_payment == "2":
                        g=input('type your desired genre : ')
                        for i in Genre:
                            if i == g:
                                a=Genre.index(i)
                                print(*genre[a])
                        b=input("enter the desired book : ")
                        b+=","
                        book_input()
                        
            else:
                print("invalid input")
book_input()



