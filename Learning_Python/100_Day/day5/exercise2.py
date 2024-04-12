# Make program that calculate the highest number on list
# not allowed use max min function

# Input a list of student scores
student_scores = input("Input all your student score : ").split()
highest_score = 0 

for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
     
    if student_scores[n] > highest_score:
        highest_score = student_scores[n]
    
print(f"The highest score in class : {highest_score}")