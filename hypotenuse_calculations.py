import math


def hypotenuse():
    print("Welcome to Hypotenuse Calculations!")
    user_side1 = float(input("Enter the value of the opposite side of the R.A.T: "))
    user_side2 = float(input("Enter the value of the adjacent side of the R.A.T: "))
    result = float(math.sqrt(math.pow(user_side2, 2) + math.pow(user_side1, 2)))
    print(f"The third and largest side of the R.A.T is: {result:}")
    return result


if __name__ == '__main__':
    hypotenuse()
