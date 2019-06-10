import house

intro = False
kitchen = False
street = False
mansion = False
breakf = False

sneakUse = False
fakeUse = False
timeUse = False
hideUse = False

def main():
    print("Welcome to Picky Pocket's Quest For Greatness." + "\n\t This is a text adventure! Make sure to type commands to progress the story." + "\n\t Items you can interact, locations you can visit, and action you can take with will be CAPITALIZED." + "\n\t Enjoy!"+ "\n \n======================")
    
    house.houseStart()
    
    if kitchen == true:
        print("Kitchen Scene")
        kitchen = False
    if street == true:
        print("Street Scene")
        street = False


main()