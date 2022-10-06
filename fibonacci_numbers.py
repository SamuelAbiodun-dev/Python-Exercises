def fib(n):
    if n == 1:
        return 0

    elif n == 2:
        return 1

    else:
        return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    print("Fibonacci Numbers")
    position = int(input("Enter a position: "))
    print(fib(position))
