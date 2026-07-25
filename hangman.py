import random

words = [
    "galaxy", "whisper", "canyon", "velvet", "thunder",
    "mirror", "harbor", "cascade", "flicker", "labyrinth",
    "ember", "quartz", "meadow", "silhouette", "voyage",]

lives = 6
random_word = random.choice(words)

blank = ["_"] * len(random_word)

while "_" in blank and lives > 0:
    print (" ".join(blank))
    print(f"Lives remaining: {lives}")
    guess = input("Guess a letter: ").lower()

    if guess in random_word: 
        for i in range(len(random_word)):
            if random_word[i] == guess: 
                blank[i] = guess
    else: 
        lives -= 1
        print ("Wrong guess!")


if lives == 0:
    print(f"You lose! The word was {random_word}")
else: 
    print (f"You Win! The word was: {random_word}")