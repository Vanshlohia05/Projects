#Quizgame
print("quiz")


p = input("do you want to play?. ").strip().lower()

if p.lower() == "yes":
    print("Let's play! ")
else:
    quit()
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central proccessing unit":
    print("Correct!  ")
    score+=1
else:
    print("The answer is incorrect!")
    
answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!  ")
    score+=1
else:
    print("The answer is incorrect!")
    

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!  ")
    score+=1
else:
    print("The answer is incorrect!")
    
answer = input("What does PSU stand for? ")
if answer.lower() == "public service unit":
    print("Correct!  ")
    score+=1
else:
    print("The answer is incorrect!")
    
print(f"You got {score} questions correct")
print(f"You got {(score/4)*100} percentage correct")