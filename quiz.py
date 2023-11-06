print("Welcome to the Quiz!")
playing = input("Do you want to play? ")
if playing.lower()!= "yes":
    quit()
score=0

print("Okay! Let's Play :)")

ans=input("What does CPU stand for ?" )
if ans.lower()=="central processing unit":
    print("Correct Answer")
    score+=1
else:
    print("Incorrect!")

ans=input("What is the latest intel processor? " )
if ans.lower()=="i11":
    print("Correct Answer")
    score+=1
else:
    print("Incorrect!")

ans=input("What is the name of the open source chrome browser? " )
if ans.lower()=="chromium":
    print("Correct Answer")
    score+=1
else:
    print("Incorrect!")

ans=input("What does GPU stand for? " )
if ans.lower()=="graphics processing unit":
    print("Correct Answer")
    score+=1
else:
    print("Incorrect!")

print("You got " + str(score) +" questions corerct out of 4")
