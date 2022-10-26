def question_number_2(len1, len2, len3):
    if len1 == len2 == len3:
        print("It is an equilateral triangle!")
    else:
        print("It is not an equilateral triangle!")


if __name__ == '__main__':
    length1 = input("Enter the first length of the triangle:\n")
    length2 = input("Enter the second length of the triangle:\n")
    length3 = input("Enter the third length of the triangle:\n")

    question_number_2(length1, length2, length3)
