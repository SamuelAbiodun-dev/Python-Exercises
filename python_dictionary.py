#
# Employee = {"Name": "Samuel Abiodun",
#             "Age": 29,
#             "Salary": 500000,
#             "Company": "PUNCH"}
# print(type(Employee))
# print("printing Employee data:")
# print(Employee)
#
# Dict = {}
# print("Employee Dictionary: ")
# print(Dict)
# Dict = dict({1: 'Java',
#              2: 'T',
#              3: 'Point'})
# print(Dict)
#
# # Accessing dictionary values:
# Employee = {"Name": "Samuel Abiodun",
#             "Age": 29,
#             "Salary": 600000,
#             "Company": "PUNCH"}
# print(type(Employee))
# print("Printing Employee data:")
# print("Name: %s" % Employee["Name"])
# print("Age: %d" % Employee["Age"])
# print("Salary: %d" % Employee["Salary"])
# print("Company: %s" % Employee["Company"])
#
# Dict = {}
# print("Empty Dictionary: ")
# print(Dict)
#
# Dict = {"name": "cohort_13", "age": 93, "gender": ["male", "female", "others"]}
# print(Dict["name"])
# print(Dict.values())
# print(Dict.items())
# Dict['age'] = 200
# print(Dict)
# Dict["family"] = 3
# print(Dict)
# Dict["family"] = [3, 7]
# print(Dict)
# Dict.pop("age")
# print(Dict)
# Dict["age"] = 3
# print(Dict)
# Dict.popitem()
# print(Dict)
# # del Dict deletes the dictionary
# # Dict.clear() clears the dictionary but leaves the dictionary empty
# # How to use for loop with dictionary
#
# Dict2 = {}
# print(Dict2)
#
# Dict2[0] = "Peter"
# Dict2[2] = "Joseph"
# Dict2[3] = "Ricky"
#
# print(Dict2)
# Dict = {}
# print(Dict)
# Dict["name"] = "c_13"
# Dict['number'] = 100
# Dict["colour"] = "Green_Blue"
# Dict["gender"] = ["male", "female", "others"]
# for i in Dict:
#     print(i)
# for i in Dict:
#     print(Dict[i])
#
# for i in enumerate(Dict):
#     print(i), Dict[i]
# for i, k in enumerate(Dict):
#     print("{}) {}: {}".format(i, k, Dict[k]))
# for i in Dict.values():
#     print(i)
#
# copy_cat = Dict.copy()
# print(copy_cat)
#
# copy_cat_2 = dict(Dict)
# print(copy_cat_2)
#
# c_13_family = {
#     "family_one": {
#         "name": "sam_family",
#         "number": 2
#     },
#     "family_two": {
#         "name": "ade_family",
#         "number": 2
#     },
#     "family_three": {
#         "name": "Kayode_Mommy_K",
#         "number": 5
#     },
#     "family_four": {
#         "name": "CTO_Hanky_Panky",
#         "number": 4
#     },
#     "family_five": {
#         "name": "Ernest_Smile",
#         "number": 3
#     }
#
# }
# print(c_13_family)
# found_family = c_13_family.get("family_four")
#
# semicolon = {
#     "cohort_13": {"Raheem", "Martins"},
#     "cohort_14": {"Moyin", "Bayo"}
# }
# maa = ("Oppa", "Li mee Hun", "Hii", "Say Hii")
# dict_ = semicolon.fromkeys(maa)
# dict_["Oppa"] = "Jude Family"
# dict_["Hii"] = "Mathias Family"
# dict_["Say Hii"] = "Youth Pastor Family"
# print(dict_)

first_pick = {
    "key_1": "Jude hates python",
    "key_2": {
        "name": "paragon",
        "age": "4 months",
        "Loan amount": "4 million naira",
        "size": 38,
        "weight": 3.9
    },
    "key_3": 500,
    "key_4": [50, 10, 5.9, "Hate python"],
    "key_5": "fantastic"
}
for i in first_pick.values():
        # val2 = first_pick["key_2"]["size"]
    # print(val2)
