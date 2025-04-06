print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

Question = input("A magnet would most likely attract which of the following? " \
"A: Metal B: Plastic C: Wood D: The wrong man ")
if Question.lower() == "a":
    print("Correct!")
    score +=1
else: 
    print("Incorrect!")

Question = input("Where did Scotch whisky originate? " \
"A: Ireland B: Wales C: The United States D: Scotland ")
if Question.lower() == "d":
    print("Correct!")
    score +=1
else: 
    print("Incorrect!")

Question = input("In fancy hotels, it is traditional for what tantalizing treat to be left on your pillow?" \
"A: Pretzel B: An apple C: A mint D: A photo of wolf blitzer  ")
if Question.lower() == "c":
    print("Correct!")
    score +=1

else: 
    print("Incorrect!")

Question = input("In the United States, what is traditionally the proper way to adress a judge?" \
"A: Your hloiness B: Your honor C: Your eminence D: You da man! ")
if Question.lower() == "b":
    print("Correct!")
    score +=1

else: 
    print("Incorrect!")

Question = input("The popular children's song 'it is raining, pouring' mentions an 'old man' doing what? " \
"A: Snoring B: Laughing C: Cooking D: Yelling at squirrels")
if Question.lower() == "a":
    print("Correct!")
    score +=1

else: 
    print("Incorrect!")

print("You got " + str (score) + "true out of 5 question")
print("And your score is " + str(score/5*100) + "%.")