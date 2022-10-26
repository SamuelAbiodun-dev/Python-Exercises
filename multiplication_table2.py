# for number1 in range(1, 13):
#     for number2 in range(1, 21):
#         print(f"%-4d" % (number1 * number2), end='')
#     print()

def multiplication_table(value, stop, operator):
    for counter in range(1, stop + 1):
        match operator:
            case "+":
                print(f"{value} + {counter} = {value + counter}")
            case "-":
                print(f"{value} - {counter} = {value - counter}")
            case "*":
                print(f"{value} * {counter} = {value * counter}")
            case "/":
                print(f"{value} / {counter} = {value / counter}")


if __name__ == '__main__':
    number = int(input("Enter a number: "))
    operator = input("Enter the operator sign: ")
    end = int(input("Enter an end number: "))
    multiplication_table(number, end, operator)
