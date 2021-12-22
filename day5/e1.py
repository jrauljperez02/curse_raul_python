# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

# 🚨 Don't change the code above 👆

#average = (sum(student_heights))/(len(student_heights))
total_grades = 0
for grades in student_heights:
    total_grades = total_grades + grades

number_of_students = 0
for student in student_heights:
    number_of_students += 1

final_average = total_grades / number_of_students
print(f"Average = {final_average}")

#Write your code below this row 👇
