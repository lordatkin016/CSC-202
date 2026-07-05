print("=" * 45)
print("      PERSONAL POCKET CGPA CALCULATOR")
print("=" * 45)

courses = int(input("Enter Number of Courses: "))

total_points = 0
total_units = 0

for i in range(1, courses + 1):

    print("\nCourse", i)

    unit = int(input("Course Unit: "))
    score = float(input("Score: "))

    # Grade determination using selection statements
    if score >= 70:
        grade = "A"
        point = 5

    elif score >= 60:
        grade = "B"
        point = 4

    elif score >= 50:
        grade = "C"
        point = 3

    elif score >= 45:
        grade = "D"
        point = 2

    elif score >= 40:
        grade = "E"
        point = 1

    else:
        grade = "F"
        point = 0

    quality_point = unit * point

    total_points += quality_point
    total_units += unit

    print("Grade:", grade)
    print("Grade Point:", point)

cgpa = total_points / total_units

print("\n" + "=" * 40)
print("Total Course Units:", total_units)
print("Total Quality Points:", total_points)
print("CGPA =", round(cgpa, 2))

# CGPA Remark
if cgpa >= 4.50:
    print("Class of Degree: First Class")

elif cgpa >= 3.50:
    print("Class of Degree: Second Class Upper")

elif cgpa >= 2.40:
    print("Class of Degree: Second Class Lower")

elif cgpa >= 1.50:
    print("Class of Degree: Third Class")

elif cgpa >= 1.00:
    print("Class of Degree: Pass")

else:
    print("Class of Degree: Fail")

print("=" * 40)
