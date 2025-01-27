import random
left= int(input("Enter starting number: "))
right= int(input("Enter ending number: "))
number = random.randrange(left,right)
while(True):
    guess=int(input("Enter your guess"))
    if(guess<number):
        print("Too low try again")
        continue
    elif(guess>number):
        print("Too high try again")
        continue 
    else:
        print("Correct Guess!!")
        break
    
