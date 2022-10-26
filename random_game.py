import random

# random.seed(4)
numbers = (random.randint(1, 100))
counter = 0
while counter < 4:
    random_number = int(input("Guess a number between 1 and 100: \n"))
    if random_number == numbers:
        print(f"You guessed {numbers}, You guessed right!")
    elif random_number < numbers:
        print("Too low!")
    elif random_number > numbers:
        print("Too high")
    counter += 1








