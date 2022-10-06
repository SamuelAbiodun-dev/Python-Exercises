if __name__ == '__main__':
    grade_str = input("Enter your grade here: ")
    grade = int(grade_str)

    if 90 <= grade <= 100:
        print(f"""
        ***
        Congratulations! Your grade of {grade_str} earns you an A in this course""")
    elif 90 > grade or grade > 100:
        print(f"Sorry! You do not have an A with {grade_str}!")
