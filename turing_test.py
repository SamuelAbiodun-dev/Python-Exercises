if __name__ == '__main__':
    print("  --------------------------------")
    print("|                                 |")
    print(" WELCOME TO SAM TURING TEST CENTRE")
    print("|                                 |")
    print("  -------------------------------")
    print("We presume you have an issue to be attended to")
    print("Please, what's your problem? ")
    user_input = input("--> ")
    print("Have you had this problem before (yes or no)?")
    user_input3 = input("--> ").lower()
    while user_input3 != "yes" and user_input3 != "no":
        print("****Invalid response****")
        user_input3 = input("Have you had this problem before (yes or no)?")
    if user_input3 == "yes":
        print("Well, you have it again.")
        print("  --------------------------------")
        print("|                                 |")
        print("     THANKS FOR THE PATRONAGE       ")
        print("|                                 |")
        print("  -------------------------------")
    elif user_input3 == "no":
        print("Well, you have it now.")
        print("  --------------------------------")
        print("|                                 |")
        print("     THANKS FOR THE PATRONAGE       ")
        print("|                                 |")
        print("  -------------------------------")


