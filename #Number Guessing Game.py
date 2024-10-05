#Number Guessing Game

import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("Please type a number larger than 0 next time")
    else:
        pass
else:
    print("Please type a number next time")
    pass
    
r = random.randrange(0, top_of_range)
print(r)

