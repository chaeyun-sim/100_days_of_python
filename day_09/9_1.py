student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}

for k, v in student_scores.items():
  if v > 90:
    student_grades['Outstanding'] = k
  elif v > 80:
    student_grades['Exceeds Expectations'] = k
  elif v > 70:
    student_grades['Acceptable'] = k
  elif v <= 70:
    student_grades['Fail'] = k

# teaches'

# for student in student_scores:
#   score = student_scores[student]
#   if score > 90:
#     student_grades[student] = "Outstanding"
#   elif score > 90:
#     student_grades[student] = "Exceeds Expectations"
#   elif score > 90:
#     student_grades[student] = "Acceptable"
#   else:
#     student_grades[student] = "Fail"


print(student_grades)