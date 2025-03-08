from art import logo



def clear_screen():
    print("\033[H\033[J", end="")
max_bid = 0
Bidders = {}
clear_screen()
print(logo)
print("\n"*5)
bidders = input("Enter your name: ")
bid = int(input("Enter your bid: $"))
ask = input("Are there any other bidders? Type 'yes' or 'no' ")
Bidders[bidders] = bid
while ask == "yes":   
    clear_screen()
    print(logo)
    print("\n"*5)
    bidders = input("Enter your name: ")
    bid = int(input("Enter your bid: $"))
    Bidders[bidders] = bid
    ask = input("Are there any other bidders? Type 'yes' or 'no': ")

for key in Bidders:
    if Bidders[key] > max_bid:
        max_bid = Bidders[key]
        winner = key
clear_screen()
print("\n"*5)
print(logo)
print(f"The winner is {winner} with a bid of ${max_bid}")
print("\n"*5)