# import string
#
# s = "my name is alexander samuel"
# # replace(" ", "") can be used to replace a string assigned to the variable and not the variable itself
# print(s.upper())
# print(s.lower())
# print(s.capitalize())
# print(s.title())
# print(s.swapcase())
# print(s.casefold())
# print(s.count("you"))
# print(s.count("a"))
# print(s.count("a", 3, 5))
# print(s.find("m"))
# print(s.find("m", 1, 10))
# # print(s.index('"m', 1, 7))
# print(s.rindex("is"))
# print(s.rfind("a"))
# print(s.find("a", s.find("a") + 1))
# print(s.startswith("his name"))
# print(s.endswith("samuel"))
#
# # is alphanumeric
# # is ascii
# # decimal is a number range between 0-9
# print("abc123".isalnum())
# print(s.isalpha())
# # print(isdecimal())
# print("if".isidentifier())
# print(string.digits)
# print(string.ascii_uppercase)
# print(string.ascii_lowercase)
# print(string.ascii_letters)
# print(s.replace(" ", "$"))
# print(s.replace(" ", "$", 2))
#
# hello = "hello"
# print(hello.ljust(20, "*"))
#
# print(hello.rjust(20, "*"))
# print(hello.center(20, "*"))
#
# for i in range(1, 21, 2):
#     s = "*" * i
#     print(s.center(20))
# # print(s.translate(*))
# # Translate
#
# a = "100010110".replace("1", "2").replace("0", "1").replace("2", "0")
# print(a)
#
# binary = "100010101100"
# b = binary.translate(str.maketrans("01", "10"))
# print(b)
import string
word = input("Enter a word with small letters: ")
word2 = input("Enter a word with capital letters: ")
key = int(input("Enter the key to code with small letters: "))
key2 = int(input("Enter the key to code with capital letters: "))
abc = string.ascii_lowercase
ABC = string.ascii_uppercase
inverse2 = ABC[key2:] + ABC[:key2]
inverse = abc[key:] + abc[:key]
# print(word.translate(str.maketrans(abc+ABC, inverse+inverse2)))
print(word.translate(str.maketrans(inverse, abc)))
print(word2.translate(str.maketrans(inverse2, ABC)))
# print(word.translate(str.maketrans(ABC, inverse2)))
# vdpxho
# VDPXHO