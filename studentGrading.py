# Loyola, Reylene Grace A.
# IT3C
# WEEK 5 - Programming Problem 3 using nested if else statements:
# (Student Grading System using NUMBERED INDEX)

studentScore = float(input("Enter the student's score: "))
studentAttendance = float(input("Enter the student's attendance: "))

if studentScore >= 0 and studentAttendance >= 0:
    if 0 <= studentScore <= 100 and 0 <= studentAttendance <= 100:
        if studentAttendance < 75:
            print("Student Grade is {0}.".format("Failed"))
        else:
            if studentScore >= 90:
                print("Student Grade is {0}".format("A"))
            elif 80 <= studentScore <= 89:
                print("Student Grade is {0}".format("B"))
            elif 70 <= studentScore <= 79:
                print("Student Grade is {0}".format("C"))
            elif 60 <= studentScore <= 69:
                print("Student Grade is {0}".format("D"))
            elif studentScore < 60:
                print("Student Grade is {0}. ".format("Failed"))
    else:
        print("Invalid input: Must be between 0 and 100.")
else:
    print("Invalid input: Please enter non-negative numbers.")
