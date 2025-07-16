import random
from numberGuessing_art import logo

def guess():
    print(logo)
    hard_attempt = 5
    easy_attempt = 10
    attempt = 0
    # guess_number = int(input("Enter the no between 1 to 100 :: "))
    computer_number = random.choice(range(1,100))   # random.randint(1,100)
    mode = input("Enter Which Mode You Want To Play (easy/hard) :: ")
    if (mode.lower() == "easy"):
        attempt = easy_attempt
        print(f"You Have {attempt} Remaning")
    elif (mode.lower() == "hard"):
        attempt = hard_attempt
        print(f"You Have {attempt} Remaning")
    else:
        print('Enter Valid Game Mode')
    while(attempt != 0):
        try:
            num = int(input("Guess the number between 1 and 100: "))
            if num < 1 or num > 100:
                print("Please enter a number between 1 and 100.")
                continue
        except ValueError:
            print("Please enter a valid integer.")
            continue
       
        if(num > computer_number):
            print("High")

        elif num < computer_number :
            print("Low")

        else :
            print ("You Win")
            return
        attempt -= 1
        if attempt > 0:
            print(f"You have {attempt} attempts remaining.")
        else:
            print(f"Game over! The number was {computer_number}.")




guess()