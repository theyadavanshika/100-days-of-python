student_score = [150, 120, 139, 190, 198, 170, 20, 38, 199, 112, 167, 189, 191]

total_exam_score = sum(student_score)
print(total_exam_score)

sum = 0
for score in student_score:
    sum = sum + score

print(sum)

max_of_score = max(student_score)
print(max_of_score)

max_score = 0
for score in student_score:
    if score > max_score:
        max_score = score
print(max_score)