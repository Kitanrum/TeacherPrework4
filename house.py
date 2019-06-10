import into

KOL = False
box = False
clock = False

fPocket = ""
tWhorl = ""


def houseStart():
    
    print("\n Your name is Picky Pocket, a 13-year old thief who was orphaned and has grown-up in Lowborn Town with the Kind Old Lady raising you to become the little pickpocket you are." +"\n You are sitting on your bed in the small loft of the Kind Old Lady's House." +"\n There is a NEWSPAPER ARTICLE dated March 14th 17XX." + "\n There is also a small STACK OF BOOKS resting on a shelf to the right." + "\n You hear the KIND OLD LADY calling your name.")
    
    choice = input("What will you interact with? ")
    if choice == "NEWSPAPER ARTICLE":
        print("\n The clipping is old and yellow. The headline reads 'NOTORIOUS ROGUE VANISHES'." +"\n The image shows the wanted poster created by the Babylon Corporation of the illustrious Cut Lass, a pirate turned thief that had plagued the Babylon Corporation for years." + "\n She was so cool!!")
    elif choice == "STACK OF BOOKS":
        print("\n On top of the stack is a leather bound notebook, work and tattered." + "\n It was given to you by the Kind Old Lady." + "\n It's where you write down your inner most aspirations and all of your accomplishments, like the time you managed to steal a whole jar of candy from Tasty's Treats over in the Garden Variety Center Plaza." +"\n You should really do that again; It was fun AND delicious")
    elif choice == "KIND OLD LADY":
        print("You shout back that you'll be right there." + "\n At the foot of your bed is a chest. In it are your boots, your backpack, a SMALL METAL BOX, and a glowing ALARM CLOCK. You should TAKE EVERYTHING.")
        roomChoice = input("What will you interact with?")
        
        if(roomChoice == "SMALL METAL BOX"):
            print("You carefully pick up the small metal box and make sure the latches are all in place." + "\n This is Fakey Pocket, a compact automaton built for you by the Old Tinkerer." + "\n It looksl ike you, if you were made of metal and soulless. You use it to confuse the authorities so that you can get away if you're in trouble." + "\n And it knows how to get back home so you don't have to worry about losing it!"+ "\n So helpful that Fakey Pocket.")
            
            box = True
            
        elif(roomChoice == "ALARM CLOCK"):
            print(" You are mesmerized by the cool, blue glow of the face of the clock. It was made by the Old Tinkerer." + "\n When you throw it at or near the authorities it slows down time around them to give you extra time to get away." + "\n You thought only Babylon Corporation scientists could get their hands on such tech." + "\n Guess the Old Tinkerer has more connections than you thought." + "\n Oh, it's called the Time Whorl.")
            
            clock = True
        elif(roomChoice == "TAKE EVERYTHING" or box == True and clock == True):
            if(box == True and clock == False):
                print("\n You put on your boots then place Fakey Pocket along with the weird clock in your backpack. You hop down to the floor from your loft and go to the kitchen where the Kind Old Lady is.")
                
                fPocket = "FAKEY POCKET"
                tWhorl = "WEIRD CLOCK"
            elif(box == False and clock == True):
                print("\n You put on your boots then place the metal box along with the Time Whorl in your backpack. You hop down to the floor from your loft and go to the kitchen where the Kind Old Lady is.")
                
                fPocket = "METAL BOX"
                tWhorl = "TIME WHORL"
            elif(box == True and clock == True):
                print("\n You put on your boots thrn place Fakey Pocket along with the Time Whorl in your backpack. You hop down to the floor from your loft and go to the kitchen where the Kind Old Lady is.")
                
                fPocket = "FAKEY POCKET"
                tWhorl = "TIME WHORL"
            else:
                print("\n You put on your boots then place the metal box along with the weird clock in your backpack. You hop down to the floor from your loft and go to the kitchen where the Kind Old Lady is.")
                
                fPocket = "METAL BOX"
                tWhorl = "WEIRD CLOCK"
                into.kitchen = True
        else:
            print("\n You need to be more specific. Don't forget to CAPITALIZE!")
    else:
        print("\n You need to be more specific. Don't forget to CAPITALIZE!")
    
