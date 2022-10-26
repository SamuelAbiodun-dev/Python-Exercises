age_str = input("Enter your age: ")
age = int(age_str)
maximum_heart_rate = 220 - age
target_heart_rate = maximum_heart_rate * 0.85
heart_rate_range = 85 / 100

print(f"Your age is: {age_str}")
print(f"Maximum heart rate is: {maximum_heart_rate}")
print(f"Your heart rate range is: {heart_rate_range}" + "%")
