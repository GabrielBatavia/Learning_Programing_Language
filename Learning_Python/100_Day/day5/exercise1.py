# program that caculates avarange studeng height from list

# Input a pyrhon list of student heights
student_heights = input("Input all your student height : ").split()

total_height = 0
total_height = int(total_height)

number_of_students = 0
number_of_students = int(number_of_students)

averages_height = 0
averages_height = int(averages_height)

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
    total_height += student_heights[n]
    number_of_students += 1
    averages_height += student_heights[n]

averages_height /= number_of_students

print(f"total height : {total_height}")
print(f"number of students : {number_of_students}")
print(f"Average height : {averages_height}")
