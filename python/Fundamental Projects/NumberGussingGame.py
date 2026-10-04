import random

secret_number=random.randint(1,100)
attempt=1
attempts=5
while True:
    print(f"You have only {attempts} attempts")
    value=int(input("Enter your value:"))
    if attempts<1:
        print("Sorry you have lost the game")
        print("Try again next time")
        print("Good Luck Bye!")
        break
    else:
        if value<=0 or value>=101:
            print("Your value must be positive or Your value must be less than 101")
        elif value==secret_number:
            print("------Congratulations------")
            print("You Won the Game!")
            break
        elif value>secret_number:
            print("Attempt: ",attempt)
            print("Your value is: ",value)
            attempt+=1
            print("Your value must be low")
        else:
            print("Attempt: ", attempt)
            print("Your value is: ",value)
            print("Your value must be high")
            attempt+=1
        attempts-=1



















