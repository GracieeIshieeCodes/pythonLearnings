# Loyola, Reylene Grace A.
# IT3C
# WEEK 5

mathGrade = float(input("Enter your grade in Math: "))
peGrade = float(input("Enter your grade in PE: "))
nstpGrade = float(input("Enter your grade in NSTP: "))
englishGrade = float(input("Enter your grade in English: "))

totalGrades = mathGrade + peGrade + nstpGrade + englishGrade

averageGrade = totalGrades / 4

print("Your grade in {0}, {1}, {2}, and {3} is {4}".format("Math", "PE", "NSTP", "English", averageGrade))