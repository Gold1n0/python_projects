print("Welcome to treasure island!")
print("Your mission is to find the treasure! ")


print("You're at a crossroad! Where do you want to go? ")
road_choice = input("Type 'left' or 'right' ")

if road_choice == "left":
    print("You stumble upon a fire and got caught up! You died!")
elif road_choice == "right":
    print("The passage is safe! You see a big lake in the horizon what do you do?")
    
    swim_choice = input("Swim across or wait for a boat, type swim or wait ")

    if swim_choice == "swim":
        print("You ran out of stamina and drowned, you died!")
    elif swim_choice == "wait": 
        print("You waited for a boat and was granted safe passage you survived!")

        house_choice = input("you stumbled upon a house which door do you choose? Type red, blue, green ")

        if house_choice == "red":
            print("You fell down a hole and died!")
        elif house_choice == "blue":
            print("You were ambushed by bandits and died!")
        elif house_choice == "green": 
            print("You have found the treasure! Great job!")
else: 
    print("That's not how you start the adventure!")
