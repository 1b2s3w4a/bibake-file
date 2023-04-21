print("hello")
print("welcome to my game ")
player1 = input("do you want to play? ")
if player1 != "yes":
    quit()

print("so let's play the game ")
score=0

question1=input("what is the name of india prime minister? ")

if question1 != "narendra modi":
    print("incorrect")
    score +=1
question2=input("what is the biggest cricket league in the world? ")
if question2 != "ipl":
    print("incorrect")
    score +=1

question3 = input ("what is the full form of ee? ")
if question3 != "electrical enginnering":
    print("incorrect")
    score +=1
print("thank you for your particpation","and your scor is",score)

ii
