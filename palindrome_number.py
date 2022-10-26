number = input("Enter a Number: ")

if len(number) % 2 == 0:
    index = 0
    counter = 0

    while index < len(number) / 2:
        if number[index] == number[len(number) - index - 1]:
            counter += 1

        index += 1

    if counter == len(number) / 2:
        print("It is a palindrome number")

    else:
        print("It is not a palindrome number")

# else:
#     index = 0
#     counter = 0
#
#     while index < len(number) // 2:
#         if number[index] == number[len(number) - index - 1]:
#             counter += 1
#
#         index += 1
#
#     if counter == len(number) // 2:
#         print("It is a palindrome number")
#
#     else:
#         print("It is not a palindrome number")
