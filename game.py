########################
#
#  Text based adventure
# Author : Rok Kepa aka AudiTTRSi
# Version 1.0
#
########################


#####################
# Intro and greetings
#####################
import time
print("Welcome to the text base adventure game ")
time.sleep(2)
username = input("What is your name? \n")
user_inventory = []
time.sleep(2)
print("Helloo" ,str(username))
print("Throug this game you will face different challenges, riddles, puzzles that will bring you to the end of game")
print("Are you ready to take a dive in this adventure?")
stranger_meet=False
user_start = str(input("Yes or No \n" ))
if (user_start == "Yes" or user_start== "yes"):
    print("at the start you were take to Island far far in Pacific Ocean")
    time.sleep(2)
    print("It looks like you were dropped in the middle of the island")
    time.sleep(2)
    print("You can head towards North, South, East or West")
    time.sleep(2)
    print("Go north and you will come to the village,")
    time.sleep(2)
    print("go east and you will come to dark Forest,")
    time.sleep(2)
    print("to the west you will find cave entry,")
    time.sleep(2)
    print("go to the south you will find small pound,")
    time.sleep(2)
    print("go to north and you will get to the valley.")
    time.sleep(2)
    print("Where would you like to go? ")
    user_direction =  str(input("What direction do you choose? \n"))
    time.sleep(2)
######
#
# North dirrection
#
######

    if(user_direction == "North"):

        print("After half and hour walk you are in the middle of small valley.")
        time.sleep(2)
        print("Suddenly you hear someone walking towards you.")
        time.sleep(2)
        print("Looks like a stranger in dark coat")
        time.sleep(2)
        print("What you will you do? Greet the stranger or Hide?")
        stranger_first_interaction = str(input("Greet or Hide? \n"))

        ######
        #
        # decision about interaction with stranger
        #
        ######

        if(stranger_first_interaction == "Greet" or stranger_first_interaction == "greet"):
            stranger_meet = True
            print("You have decided to greet the stranger you call him and stranger notices you and starts approaching")
            time.sleep(2)
            print("When he is almost at you stranges takes of his hat and smiles and greets you with smile on the face")
            time.sleep(2)
            print("You are not from this island, says stranger")
            time.sleep(2)
            print("In dark forest you might find some supplies that you might need to explore the caves,\nin the pound on the south you can find fish to eat\nLocals are talking about ")
######
#
# South dirrection
#
######
    elif(user_direction =="South"):
        print("You have choose" ,user_direction)
        time.sleep(2)
        print("After a few minutes you come to small pond surrounded by few trees. Where you can sit in shadow or try to catch the fish")
        time.sleep(2)
        print("What will you do?")
        user_decision_south = str(input("Will you sit down or go fishing?\n"))
        if (user_decision_south == "Sit down"):
            print("You sit down in the shadow of the old tree closest to the pound.")
            time.sleep(2)
            print("In the pound you can see the fish")
            time.sleep(2)
            print("Will you try to catch fish or sit in shadow?")
            user_decision_south2 = str(input("Go fishing or sit?"))
            if(user_decision_south2 == "Go fishing"):
                time.sleep(2)
                print("You will need to make some kind of fishing equipment, maybe you can try looking around for materials.")
######
#
# East dirrection
#
######
    elif(user_direction =="East"):
        print("You have choose" ,user_direction)
        time.sleep(2)
        print("From starting point you soon come to the edge of forest. You enter with caution")
######
#
# West dirrection
#
######
    elif(user_direction == "West"):
        print("You have choose" ,user_direction)

    else:
        print("Please enter correct direction")
elif (user_start=="No" or user_start=="no"):
    print("Ok, maybe you will decide to go on adventure next time \nIf you would like to go let me know.")
else:
    print("You didn't answer my questions")
