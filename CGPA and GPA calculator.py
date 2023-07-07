print("Welcome to your CGPA calculator\n")

name = input("What is your name?: ")
# Dictionary containing the Grades and their values
GRADES = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
    "E": 1,
    "F": 0
}

# Their values will be added once calculated 
cummultative_unit = 0
total_grade_point = 0

def calculate_gpa(course_grades):
    # The 'global' calls for the initial values which is zero and then stores their calculated values 
    global cummultative_unit
    global total_grade_point
    for grading in course_grades:
        # The grading[1] is the credit unit 
        cummultative_unit += grading[1]
        # The GRADES[grading[0]] is the course grades value * the credit unit which will give us the Quality point(total_grade_point) 
        total_grade_point += GRADES[grading[0]] * grading[1]
    # The gpa is gotten from dividing the Quality point with the total credit unit    
    GPA = round(total_grade_point / cummultative_unit, 2)
    if GPA <= 2.9:
        print(f"\n{name} You are on pass")
    elif GPA <= 3.4:
        print(f"\n{name} You are on third class")
    elif GPA <= 3.9:
        print(f"\n{name} You are on second class lower")
    elif GPA <= 4.4:
        print(f"\n{name} Your are on second class upper")
    elif GPA <= 5.0:
        print(f"\n{name} You are a first class student")
    print(f"Your GPA for the semester is {GPA} /5.0.")

def calculate_cgpa(course_grades):  # The name courses_grades is not used in our calculations but written for formular generation sake 
    global cummultative_unit
    global total_grade_point
    for grading in course_grades:
        cummultative_unit += grading[1]
        total_grade_point += GRADES[grading[0]] * grading[1]
    CGPA = round(total_grade_point / cummultative_unit, 2)
    if CGPA <= 2.9:
        print(f"\n{name} You are on pass")
    elif CGPA <= 3.4:
        print(f"\n{name} You are on third class")
    elif CGPA <= 3.9:
        print(f"\n{name} You are on second class lower")
    elif CGPA <= 4.4:
        print(f"\n{name} Your are on second class upper")
    elif CGPA <= 5.0:
        print(f"\n{name} You are a first class student")
    print(f"Your CGPA for the year is {CGPA} /5.0.")



choice = ["year", "semester"]    
while True:
    num_of_calc = input(f"\nHello {name} Do you want to calculate your CGPA for a year or for a semester?: ").lower()
    if num_of_calc not in choice:
        print("Please select either year or semester!")
        continue

    # For CGPA calculation for an entire year
    if num_of_calc == "year":
        grades = ["A", "B", "C", "D", "E", "F"]
        course_grades = []
        try:
            course_no = int(input("How many gradable course did you offer in a year?: "))

            i = 0
            # This will keep running until i >= course_no
            while i < course_no:
                try:
                    grade_unit_list = []
                    course_grade = input("%d. Enter grade for each course offered (A, B, C, D, E, or F): " %(i + 1))   # The %(i + 1) helps to indicate the number of items that has been listed
                    if course_grade not in grades:
                        print("Invalid input.")
                        continue
                    grade_unit_list.append(course_grade)

                    course_unit = int(input("%d. Enter course unit: " % (i + 1)))

                    grade_unit_list.append(course_unit)

                    grade_unit_list_tuple = tuple(grade_unit_list)
                    
                    course_grades.append(grade_unit_list_tuple)
                    # After each loop 1 will be added to i so as to continue runing till the course_no value is reached
                    i += 1
                except ValueError:
                    print("Invalid input!")
                    continue
        except ValueError:
            print("Invalid input!")
        calculate_cgpa(course_grades)
        break

    # For GPA of a semester
    elif num_of_calc == "semester":
        grades = ["A", "B", "C", "D", "E", "F"]
        course_grades = []
        try:
            course_no = int(input("How many gradable course did you offer?: "))

            i = 0
            while i < course_no:
                try:
                    grade_unit_list = []
                    course_grade = input("\n%d. Enter grade (A, B, C, D, E, or F): " %(i + 1))

                    if course_grade not in grades:
                        print("Invalid input.")
                        continue
                    grade_unit_list.append(course_grade)

                    course_unit = int(input("%d. Enter course unit: " % (i + 1)))

                    grade_unit_list.append(course_unit)     # The courese unit will be added to the course_grades in a list(grade_unit_list) like this ['A', 3] if course_grade = A and course_unit = 3

                    grade_unit_list_tuple = tuple(grade_unit_list)  # The tuple is used to store multiple course_grades and course_units in the list(grade_unit_list)
                    
                    course_grades.append(grade_unit_list_tuple)  # The stored tupled grade_unit_list is now stored in course_grades which will be used for our calculations
                    i += 1
                except ValueError:
                    print("Invalid input!")
                    continue
        except ValueError:
            print("Invalid input!")
        calculate_gpa(course_grades)
        break
