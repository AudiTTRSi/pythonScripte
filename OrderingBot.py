########################
#
#  Ordering bot
# Author : Rok Kepa aka AudiTTRSi
# Version 1.0
#
########################


#####################
# Intro and greetings
#####################
import time
print("Welcome to our new coffe shop!")
time.sleep(2)
print("If you would like to order write Order, if you would like to se menu type Menu")
customer_input =str(input("Order or Menu ? \n" ))

if (customer_input == "order" or customer_input == "Order"):
    #here comes ordering magic
elif (customer_input=="Menu" or customer_input=="menu"):
    #thingy about Menu

else:
    print("hmm...")
    time.sleep(2)
    print("You didnt choose any of the options you got for ordering or showing you a menu, so here comes random quote:")
    time.sleep(2)
    print("Setting goals is the first step in turning the invisible into the visible. - Tony Robbins")
