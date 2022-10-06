track_record = []
day = 1
while day <= 7:
    numbers_of_days = int(input(f"Input the number of infected patients for day {day}:"))
    track_record.append(numbers_of_days)
    day = day + 1
print()
print(f"The total number of reported infections for the week is: {(sum(track_record))}")
print(f"The average number of the reported infections is: %.2f" % (sum(track_record) / len(track_record)))
print(f"The smallest number of the reported infections is: {min(track_record)}")
print(f"The largest number of the reported infections is: {max(track_record)}")
