line1 = input().split()
n, m = map(int, line1)

student_answers = []
for _ in range(n):
    student_answers.append(input())
    
question_points = list(map(int, input().split()))
total_max_score = 0

for j in range(m):
    counts = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0}
    
    for i in range(n):
        answer = student_answers[i][j]
        counts[answer] += 1
    
    max_students_correct = max(counts.values())
    total_max_score += max_students_correct * question_points[j]
    
print(total_max_score)