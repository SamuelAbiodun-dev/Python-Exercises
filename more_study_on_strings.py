str_one = "Hello cohort thirteen"
greetings = str_one[:12:1]
print(greetings)
split_str_one = str_one.split(" ")
print(split_str_one)
if "cohort" in str_one:
    print(str_one[5:12:])
str_two = str_one[:8] + "z" + str_one[9:]
print(str_two)

