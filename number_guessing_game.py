import random

print ("Welcome to Gold's Number Guesser! \n")
print ("Guess the number from a 1 to 100 \n")


difficulty = input("Choose your difficulty - Easy, Medium, or Hard: ").lower()

if difficulty == "easy":
    lives = 10
elif difficulty == "medium":
    lives = 7
elif difficulty == "hard":
    lives = 5
else:
    print("Invalid choice, defaulting to Easy.")
    lives = 10

number_list = list(range(1,101))
number_to_guess = random.choice(number_list)
user_guess = int (input ("Guess the number! "))

while lives > 0:
    if number_to_guess == user_guess:
        print ("That's the correct number you win!")
        break

    elif user_guess < number_to_guess:
        print ("The number is too low!")
        lives -= 1 
        print (f"You have {lives} lives remaining")
        if lives < 1: 
            print ("You're out of lives! Game Over!")
            break
        user_guess = int (input ("Guess the number! "))

    elif user_guess > number_to_guess:
        print ("The number is too high!")
        lives -= 1 
        print (f"You have {lives} lives remaining")
        if lives < 1: 
            print ("You're out of lives! Game Over!")
            break
        user_guess = int (input ("Guess the number! "))