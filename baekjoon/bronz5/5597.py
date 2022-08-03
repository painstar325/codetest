import sys
input = sys.stdin.readline

students = set([
    9,30,6,12,10,20,21,11,7,5,28,4,18,29,17,19,27,13,16,26,14,23,22,15,3,1,24,25
])

students_all = set([student + 1 for student in range(30)])

result = list(students_all - students)

print(min(result))
print(max(result))
