import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

print ("Welcome to the secret auction, name your price!")
auction_list = []
highest_bid = 0
highest_bidder = ""

while True:
    name = (input("What is your name? "))
    price = int(input("Name your price! "))
    bid = {"name" : name, "price" : price}

    auction_list.append(bid)

    stop_decision = (input("Are there any more person, type yes or no ")).lower()
    if stop_decision == "no":
        break
    elif stop_decision == "yes":
        clear_screen()

for bid in auction_list: 
    if bid["price"] > highest_bid:
        highest_bid = bid["price"]
        highest_bidder = bid["name"]

print(f"The winner is {highest_bidder} with a price of {highest_bid}")
