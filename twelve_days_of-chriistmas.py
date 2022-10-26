def display12():
    print("""
    Twelve drummers drumming
    Eleven pipers piping
    Ten lords are leaping
    Nine ladies dancing
    Eight maids are milking
    Seven swamps are swimming
    Six geese are laying
    Five golden rings!
    Four calling birds
    Three fresh hens
    Two turtle doves and
    A partridge in a pear tree""")


def display11():
    print("""
    Eleven pipers piping
    Ten lords are leaping
    Nine ladies dancing
    Eight maids are milking
    Seven swamps are swimming
    Six geese are laying
    Five golden rings!
    Four calling birds
    Three fresh hens
    Two turtle doves and
    A partridge in a pear tree""")


def display10():
    print("""
    Ten lords are leaping
    Nine ladies dancing
    Eight maids are milking
    Seven swamps are swimming
    Six geese are laying
    Five golden rings!
    Four calling birds
    Three fresh hens
    Two turtle doves and
    A partridge in a pear tree""")


def display9():
    print("""
    Nine ladies dancing
    Eight maids are milking
    Seven swamps are swimming
    Six geese are laying
    Five golden rings!
    Four calling birds
    Three fresh hens
    Two turtle doves and
    A partridge in a pear tree""")


def display8():
    print("""
    Eight maids are milking
    Seven swamps are swimming
    Six geese are laying
    Five golden rings!
    Four calling birds
    Three fresh hens
    Two turtle doves and
    A partridge in a pear tree""")


def display7():
    print("""
    Seven swamps are swimming
    Six geese are laying
    Five golden rings!
    Four calling birds
    Three fresh hens
    Two turtle doves and
    A partridge in a pear tree""")


def display6():
    print("""
    Six geese are laying
    Five golden rings!
    Four calling birds
    Three fresh hens
    Two turtle doves and
    A partridge in a pear tree""")


def display5():
    print("""
    Five golden rings!
    Four calling birds
    Three fresh hens
    Two turtle doves and
    A partridge in a pear tree""")


def display4():
    print("""
    Four calling birds
    Three fresh hens
    Two turtle doves and
    A partridge in a pear tree""")


def display3():
    print("""
    Three fresh hens
    Two turtle doves and
    A partridge in a pear tree""")


def display2():
    print("""
    Two turtle doves and
    A partridge in a pear tree""")


def display1():
    print("""
    partridge in a pear tree""")


if __name__ == '__main__':
    day = int(input("Enter a day of Christmas (1-12), to display a song!: "))
    if day == 1:
        print(f"On the ", day,"st" "day of Christmas, my true love said to me,")
    if day == 2:
        print(f"On the ", day,"nd day of Christmas, my true love said to me,")
    if day == 3:
        print(f"On the ", day,"rd day of Christmas, my true love said to me,")
    if day != 1 and day != 2 and day != 3 and day <= 12:
        print(f"On the ", day,"th day of Christmas, my true love said to me,")

    if day > 12:
        print("Invalid input!")
    match day:
        case 12: display12()
        case 11: display11()
        case 10: display10()
        case 9: display9()
        case 8: display8()
        case 7: display7()
        case 6: display6()
        case 5: display5()
        case 4: display4()
        case 3: display3()
        case 2: display2()
        case 1: display1()


