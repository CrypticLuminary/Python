import random
from blacljack_art import logo

def calculate(cards):
    total = sum(cards)
    if total > 21:
        total -=10
    return total

def calculateblackjack(computer,drawn):
 
    computer_cards = calculate(computer)
    drawn_ccards = calculate(drawn)

    if computer_cards > 21:
        print("You Win")

    elif drawn_ccards > 21:
        print("You Lose")

    elif drawn_ccards > computer_cards and drawn_ccards < 21 :
        print("You Win")

    elif computer_cards > drawn_ccards and computer_cards < 21:
        print("You Lose")


def blackJack():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    Drawn = []
    computer = []
    c = random.sample(cards,2)
    d = random.sample(cards,2)
    computer.extend(c)
    Drawn.extend(d)
    print(f"Computer Card is {computer[0:1]}")
    print(f"Your Card is {Drawn}")
    a = input("Do You Want To Draw A Card (Yes/No):: ")
    while True:
        if a.lower() == "yes": 
            c = random.choice(cards)
            b = random.choice(cards)  
            computer.append(c)
            Drawn.append(b)  
            print(f"Your drawn card is {b}. Current Drawn list: {Drawn}")
        elif a.lower() == "no": 
            print(f'Computer Cards is {computer}')
            print(f"Final Drawn list: {Drawn}")
            break
        else:
            print("Invalid input! Please enter 'Yes' or 'No'.")
        a = input("Do You Want To Draw A Card (Yes/No):: ")  
    calculateblackjack(computer=computer,drawn=Drawn)


print(logo)
blackJack()
