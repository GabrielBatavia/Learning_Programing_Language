# program that grades student test results

student_scores = {
    "Gabriel": 91,
    "Shalom": 90,
    "Anak": 89,
    "Clara": 94,
    "Fael": 88,
    "Ington": 85,
    "Cio": 87,
    "Petrus": 70
}

for n in student_scores.keys():
    if student_scores[n] >= 91:
        student_scores[n] = "Outstanding"
    elif student_scores[n] >= 81:
        student_scores[n] = "Exceeds Expectation"
    elif student_scores[n] >=71:
        student_scores[n] = "Acceptable"
    elif student_scores[n] <= 70:
        student_scores[n] = "Fail"
        
print(student_scores)