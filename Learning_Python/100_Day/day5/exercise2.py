# Make program that calculate the highest number on list

# Input a list of student scores
student_scores = input().split()

for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
    
highest_score = 0 