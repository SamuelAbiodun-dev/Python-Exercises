import math

if __name__ == '__main__':
    no_Of_complete_eggs = 28
    eggs_per_box = 6

    no_of_boxes = math.ceil(no_Of_complete_eggs / eggs_per_box)
    print(f"The number of boxes that can occupy {no_Of_complete_eggs} eggs is = {no_of_boxes}")

    if no_Of_complete_eggs % eggs_per_box == 0:
        eggs_in_last_box = eggs_per_box

    else:
        eggs_in_last_box = no_Of_complete_eggs % eggs_per_box
        print(f"The number of eggs in the last box is = {eggs_in_last_box}")

    eggsNeeded = eggs_per_box - eggs_in_last_box
    print(f"The number of eggs needed to fill up the last box is = {eggsNeeded}")
