#choose your own adventure game
name = input("Type your name: ")
print("Welcomr", name, "to this adventure!")
answer = input(
    "You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go?  "
)
if answer.lower() == "left":
    answer = input("You come to a river, you can walk around it or swim across? Type walk to walk around or swim to swim across:  ")
    
    if answer.lower() == "swim": 
        print("You swim across and were eaten by an alligator.")
    elif answer.lower() == "walk":
        print("You walked for many miles, ran out of water and you lost the game. ")
    else:
        print("Not a valid option. You lose.")
elif answer.lower() == "right":
    answer = input("You come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)?")
    
    if answer == "back":
        print("You go back to the main road. Now you can decide to drive into the woods. ")
    elif answer == "cross":
       answer = input("You cross the bridge and meet a stranger. Do you talk to them? ")
       if answer.lower() == "Yes":
           print("Fuck off")
       else:
           print("Get the fuck outta here")
    else:
        print("Not a valid option. You lose.")
            
else:
    print("Not a valid option. You lose.")