

number = input("Enter a number: ")

index = 0
while index < len(number):
    print(number[len(number) - 1 - index], end=' ')

    index += 1
