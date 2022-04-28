# Setup
yes_no = ["yes", "no"]
directions = ["left", "right", "forward", "backward"]
 
# Introduction
name = input("Dio: What is your name, adventurer?\n")
print("----------------------------------------------------------")
print(" ")
print("Dio: Greetings, " + name + ". Let us go on a adventure!")
print(" ")
print("-----------------------------------------------------------")
print("You find yourself on the edge of a dark forest.")
print("Can you find your way through?\n")
 
# Start of game
response = ""
while response not in yes_no:
    response = input("Would you like to step into the forest?\nyes/no\n")
    if response == "yes":
        print("----------------------------------------------------------------")
        print(" ")
        print("You head into the forest. You hear crows cawwing in the distance.\n")
        print("----------------------------------------------------------------")
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
        print("----------------------------------------------------------------")
        print(" ")
        print("You enter the dark cave and look around there is two ways to go.")
        print("Left or right")
        print(" ")
        print("----------------------------------------------------------------")
        print("")
    elif response == "right":
        print("")
        print("You head deeper into the forest.\n")
        print("It get's dark out you get lost in the forest")
        print("Thanks for playing " + name + ".")
        quit()
    else:
        print("I didn't understand that.\n")
# Next part of game
       
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
        print("----------------------------------------------------------------")
        print(" ")
        print("You head into the lit up path and you reach a locked chest and open it and find a golden arrow.")
        print("You head out of the cave and see a town.")
        print(" ")
        print("----------------------------------------------------------------")
    else:
        print("")
        print("I didn't understand that.\n")
# Next part of game

response = ""
while response not in directions:
    print("")
    print("You start heading toward the town and a hooded man is approaching you to the left.")
    print("And to your right you see a bunch of bushes you can run too.")
    
    response = input("What direction do you move?\nleft/right\n")
    if response == "right":
        print("")
        print("You run away from the man and into the bushes and you are met with a cliff on the other side and you fall.")
        print("Thanks for playing " + name + ".")
        quit()
    elif response == "left":
        print("----------------------------------------------------------------")
        print("")
        print("You start heading toward the hooded man and he stops you to ask you something about the golden arrow you found in the chest at the cave. ")
        print("He say that the arrow is a dangerous tool and asks you to throw it off the cliff just near of there.")
        print(" ")
        print("----------------------------------------------------------------")
    else:
        print("")
        print("I didn't understand that.\n")
 # Next part of game