import math

if __name__ == '__main__':
    side1_opp = float(input("Enter the size of the opposite side: "))
    side2_adj = float(input("Enter the size of the adjacent side: "))
    hypotenuse = math.sqrt(math.pow(side1_opp, 2) + math.pow(side2_adj, 2))
    print(f"The hypotenuse side is: {hypotenuse}")
