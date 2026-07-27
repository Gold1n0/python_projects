import random
score = 0
game_state = True

animal_weights = {
    "mouse": 0.02,
    "hamster": 0.15,
    "hedgehog": 0.9,
    "rabbit": 2,
    "cat": 4.5,
    "small dog": 10,
    "raccoon": 12,
    "penguin": 25,
    "wolf": 40,
    "goat": 60,
    "human": 70,
    "kangaroo": 85,
    "deer": 90,
    "pig": 120,
    "gorilla": 160,
    "lion": 190,
    "tiger": 220,
    "grizzly bear": 300,
    "polar bear": 450,
    "moose": 500,
    "horse": 550,
    "giraffe": 800,
    "bison": 900,
    "hippopotamus": 1500,
    "white rhino": 2300,
    "elephant seal": 3000,
    "african elephant": 6000,
    "sperm whale": 41000,
    "humpback whale": 30000,
    "blue whale": 150000,
}


def get_random_animal(animal_dict):
    animal = random.choice(list(animal_dict.keys()))
    weight = animal_dict[animal]
    return animal, weight

while game_state == True:
    animal1, weight1 = get_random_animal(animal_weights)
    animal2, weight2 = get_random_animal(animal_weights)

    while animal2 == animal1:
        animal2, weight2 = get_random_animal(animal_weights)

    print ("Choose between the two animals!")

    print (animal1)
    print (animal2)

    answer = input ("Choose between the two animals, which one is heavier? ").lower()

    if weight1 > weight2 and answer == animal1:
        print("Correct! you gained 1 point")
        score += 1
    elif weight2 > weight1 and answer == animal2:
        print("Correct! you gained 1 point")
        score += 1
    else:
        print(f"Wrong! {animal1} was {weight1}kg and {animal2} was {weight2}kg, Game Over!")
        game_state = False

    print(f"Your score is now: {score}")

    keep_playing = input("Play again? y/n ").lower()

    if keep_playing == "n":
        print (f"Sad to see you go! your final score was: {score}")
