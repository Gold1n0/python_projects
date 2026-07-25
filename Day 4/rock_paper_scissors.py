import random

player_choice = input("Pick your weapon, type 0 for rock, type 1 for paper, type 2 for scissors ")
if player_choice == "0":
    print ("Player chose rock")
elif player_choice == "1":
    print ("Player chose paper")
elif player_choice == "2": 
    print ("Player chose scissors")


weapon_list = ["rock", "paper", "scissors"]
weapon = random.choice(weapon_list)
print (f"Delear Chose : {weapon}")

if player_choice == "0" and weapon == "rock":
    print("It's a Draw")
elif player_choice == "0" and weapon == "paper": 
    print("You Lose")
elif player_choice == "0" and weapon == "scissors": 
    print("You Win")

if player_choice == "1" and weapon == "rock":
    print("You Win")
elif player_choice == "1" and weapon == "paper": 
    print("It's a Draw")
elif player_choice == "1" and weapon == "scissors": 
    print("You Lose")

if player_choice == "2" and weapon == "rock":
    print("You Lose")
elif player_choice == "2" and weapon == "paper": 
    print("You Win")
elif player_choice == "2" and weapon == "scissors": 
    print("It's a Draw")
