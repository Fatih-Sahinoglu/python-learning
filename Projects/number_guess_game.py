import random

number=random.randint(1,100)
turn=1
while True:
    print()
    guess=int(input("Enter your guess [1,100]: "))
    
    if guess<1 or guess>100:
        print()
        print("Please enter a number among [1,100]")
        
        turn+=1
        continue
    else:
        if guess<number:
            print()
            print(f"Number is greater than {guess}")
            turn+=1
        elif guess>number:
            print()
            print(f"Number is less than {guess}")
            turn+=1
        else:
            print()
            print("Congraulations!! You guessed",number,"in",turn,"turns")
            print()
            break