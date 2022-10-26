import random


class GuessGame:
    def __init__(self):
        self.Smallest = 1
        self.Biggest = 100

    def random_no(self):
        return random.randint(self.Smallest, self.Biggest)

    def start(self):

        rand_number = self.random_no()

        print(
            f"Guess the randomly generated number from range {self.Smallest} to {self.Biggest}")

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

    game = GuessGame()
    game.start()
