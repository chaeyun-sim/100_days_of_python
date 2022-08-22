student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

# 78 65 89 86 55 91 64 89

max_result = 0
highest_score = student_scores[0]
for score in student_scores:
  if score > highest_score:
    highest_score = score
# print(largest_number)
print(f"The highest score in the class is: {highest_score} ") 

min_result = 0
lowest_score = student_scores[0]
for score in student_scores:
  if score < lowest_score:
    lowest_score = score
# print(smallest_number)
print(f"The lowest score in the class is: {lowest_score}")