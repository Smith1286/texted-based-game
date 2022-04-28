# Setup
yes_no = ["yes", "no"]
directions = ["left", "right", "forward", "backward"]
 
# Introduction
name = input("Dio: What is your name, adventurer?\n")
print("Dio: Greetings, " + name + ". Let us go on a adventure!")
print("You find yourself on the edge of a dark forest.")
print("Can you find your way through?\n")
 
# Start of game
response = ""
while response not in yes_no:
    response = input("Would you like to step into the forest?\nyes/no\n")
    if response == "yes":
        print("You head into the forest. You hear crows cawwing in the distance.\n")
    elif response == "no":
        print("You are not ready for this quest. Goodbye, " + name + ".")
        quit()
    else: 
        print("I didn't understand that.\n")
 
# Next part of game
response = ""
while response not in directions:
    print("To your left, you see a cave.")
    print("To your right, there is more forest.")

    response = input("What direction do you move?\nleft/right\n")
    if response == "left":
        print("")
        print("You enter the dark cave and look around there is two ways to go.")
        print("Left or right")
        print("")
    elif response == "right":
        print("")
        print("You head deeper into the forest.\n")
        print("It get's dark out you get lost in the forest")
        print("Thanks for playing " + name + ".")
        quit()
    else:
        print("I didn't understand that.\n")
        
response = ""
while response not in directions:
    print("")
    print("To your left, you see a dark narrow path.")
    print("To your right, there is a lit up path.")
    
    response = input("What direction do you move?\nleft/right\n")
    if response == "left":
        print("")
        print("You get lost and the cave.")
        print("Thanks for playing " + name + ".")
        quit()
    elif response == "right":
        print("")
        print("You head into the lit up path and you reach a locked chest, you open it.")
    else:
        print("")
        print("I didn't understand that.\n")

response = ""
while response not in directions:
    print("")
    print("You open the chest you get a strange golden arrow.")
    print("You then continue out the cave and reach a crossroad to the left is a bush and to the right is a town.")
    
    response = input("What direction do you move?\nleft/right\n")  
    if response == "left":
        print("")
        print("You head into a bush")
        print("On the other side of the bush is a cliff and you fall.")
        print("Thanks for playing " + name + ".")
        quit()
    elif response == "right":
        print("")
        print("You head into town")
        print("you meet a man wearing a jacket and hat he stops and talk with you and says don't go into the town.")
    else:
        print("")
        print("I didn't understand that.\n")
