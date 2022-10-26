import random


class GuessingGame:
    def __init__(self):
        self.LOWEST = 1
        self.HIGHEST = 100

    def rand_number(self):
        return random.randint(self.LOWEST, self.HIGHEST)

    def start(self):

        rand_number = self.rand_number()

        print(
            f"Guess the randomly generated number from {self.LOWEST} to {self.HIGHEST}")

        chances = 0
        while True:
            user_num = int(input("Enter the guessed number: "))
            if user_num == rand_number:
                print(
                    f"-> Hurray! You got it in {chances + 1} step{'s' if chances > 1 else ''}!")
                break
            elif user_num < rand_number:
                print("-> Your number is less than the random number")
            else:
                print("-> Your number is greater than the random number")
            chances += 1


if __name__ == '__main__':

    game = GuessingGame()
    game.start()
