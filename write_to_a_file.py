# open file for writing
# creates file if it does not exist
# overwrites if it exists
# writing a text
# temp_file = open("temp.txt", "w")
# print("first line", file=temp_file)
# print("second line", file=temp_file)
# temp_file.write("Hello World")
# temp_file.close()
# editing the already existing text
# temp_file = open("temp.txt", "a")
# print("first line", file=temp_file)
# print("second line", file=temp_file)
# temp_file.close()

# temp_file = open("Samuel Abiodun", "a")
# print("Samuel Abiodun", file=temp_file)
# print("Samuel A", file=temp_file)
# temp_file.close()

# .strip() is used to get rid of white space

# input_file = open("temp.txt", "r")
# output_file = open("output.txt", "w")
# for line_str in input_file:
#     new_str = " "
#     line_str = line_str.strip()
#     for char in line_str:
#         new_str = char + new_str
#     print(new_str, file=output_file)
#
#     print("Line: {:12s} reversed is: {:s}".format(line_str, new_str))
# input_file.close()
# output_file.close()

text_file = open("text.txt", "w")
input_text = "She has a facetious remark"
print(input_text, file=text_file)
text_file.close()


texts_txt = open("text.txt", "r")
for vow in ['a', 'e', 'i', 'o', 'u']:
    word = vow
    word2 = input_text.count(vow.lower())
    print(f"{word} = {word2}")
text_file.close()

# def get_vowels_in_word(word):
#     """Return vowels in string word--include repeats."""
#     vowel_str = "aeiou"
#     vowels_in_word = ""
#     for char in word:
#         if char in vowel_str:
#             vowels_in_word += char
#     return vowels_in_word
