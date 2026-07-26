import random
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def adjust_ace (hand, total):
    while total > 21 and 11 in hand:
        hand[hand.index(11)] = 1
        total = sum(hand)
    return total

game_state = False

player = []
dealer = []

welcome = input ("Welcome to Gold's Casino, press Y to play BlackJack, press N to leave! ").lower()

if welcome == "y":
    game_state = True

    player = [random.choice(cards), random.choice(cards)]
    dealer = [random.choice(cards), random.choice(cards)]

    dealer_total = sum(dealer)
    dealer_total = adjust_ace(dealer, dealer_total)
    player_total = sum(player)
    player_total = adjust_ace(player, player_total)

    print("Your hand is " + ", ".join(str(card) for card in player))
    print (f"Dealer hand is {dealer[0]}")

    while game_state == True:
        choice = input("Press Y to hit! or press P to pass! ").lower()

        if choice == "y":
            new_card = random.choice(cards)
            player.append(new_card)
            player_total = sum(player)
            player_total = adjust_ace(player, player_total)
            print(f"You drew a {new_card}. Your hand is now: " + ", ".join(str(card) for card in player))
            print(f"Your total is: {player_total}")

            if player_total > 21:
                print("Bust! You lose!")
                break

        elif choice == "p":
            while dealer_total < 16:
                new_card = random.choice(cards)
                dealer.append(new_card)
                dealer_total = sum(dealer)
                dealer_total = adjust_ace(dealer, dealer_total)
                print(f"Dealer drew a {new_card}. Dealer hand is now: " + ", ".join(str(card) for card in dealer))
                print(f"Dealer total is: {dealer_total}")

            if dealer_total > 21:
                print("Your hand is " + ", ".join(str(card) for card in player))
                print("Dealer hand is " + ", ".join(str(card) for card in dealer))
                print(f"Player total is: {player_total}")
                print(f"Dealer total is: {dealer_total}")
                print("Dealer Bust! You win! ")
                break

            if player_total < dealer_total:
                print("Your hand is " + ", ".join(str(card) for card in player))
                print("Dealer hand is " + ", ".join(str(card) for card in dealer))
                print(f"Player total is: {player_total}")
                print(f"Dealer total is: {dealer_total}")
                print ("Dealer Scores! You Lose!")
                break

            if player_total > dealer_total:
                print("Your hand is " + ", ".join(str(card) for card in player))
                print("Dealer hand is " + ", ".join(str(card) for card in dealer))
                print(f"Player total is: {player_total}")
                print(f"Dealer total is: {dealer_total}")
                print ("Player Scores! You Win!")
                break

            if player_total == dealer_total: 
                print("Your hand is " + ", ".join(str(card) for card in player))
                print("Dealer hand is " + ", ".join(str(card) for card in dealer))
                print(f"Player total is: {player_total}")
                print(f"Dealer total is: {dealer_total}")
                print ("It's a tie! No one wins!")
                break
else: 
    game_state = False