# vowels = ['a', 'e', 'i', 'o', 'u']
# s = "May the force be with you."
# count = 0
# while s:
#     count += s[0] in vowels
#     s = s[1:]
# print(count)


# open_file = open("temp.txt", "a")
# print("duration", file=open_file)
# print("myaeiou", file=open_file)
# print("education", file=open_file)
# print("facetious", file=open_file)

# open_text = open("temp.txt", "r")
#
# find_word = ''
# for word in open_text:
#     for char in word:
#         if char in ['a', 'e', 'i', 'o', 'u']:
#             find_word += char
#
#     if find_word == 'aeiou':
#         print(word, end='')
#
#     find_word = ''

# open_file = open("text.txt", "a")
# print("acceious", file=open_file)
# print("associative", file=open_file)
# print("ufocibeca", file=open_file)
#
# open_file = open("text.txt", "r")
# find_word = ''
# for text in open_file:
#     for char in text:
#         if char in ['a', 'e', 'i', 'o', 'u']:
#             find_word += char
#
#     if find_word == 'aeiou':
#         print(text, end='')
#
#     find_word = ''
#
first_text = open("trial_text.txt", "x")
first_text.write("Hello World")
file_ = open("first_text", "r")
print(file_.read())
file_.close()



