#제곱수
#2=제곱
#3=아님
#4=제곱수
#5=아님
#6=아님
#7=아님
#8=아님
#9=맞음
#10=아님
# import math

# import sys

# def check_not_square(num):
#     for square in square_numbers:
#         if num % square == 0:
#             return False
#     return True

# input = sys.stdin.readline
# min, max = map(int, input().split())

# square_numbers = [n for n in range(2, int((max)/2)) if int(math.sqrt(n)) == math.sqrt(n)]
# count = 0
# for num in range(min, max+1):
#     #제곱수 확인
#     # if num > 1 and int(math.sqrt(num)) == math.sqrt(num):
#     #     square_numbers.append(num)
#     if check_not_square(num):
#         count += 1

# print(count)






# import math

# import sys

# def check_not_square(num):
#     for square in square_numbers:
#         if num % square == 0:
#             return False
#     return True

# input = sys.stdin.readline
# # min, max = 5, 100
# # min, max = 3, 12
# min, max = 1, 1000000
# # min, max = map(int, input().split())
# square_numbers = [n for n in range(2, max) if int(math.sqrt(n)) == math.sqrt(n)]
# count = 0
# for num in range(min, max+1):
#     #제곱수 확인
#     # if num > 1 and int(math.sqrt(num)) == math.sqrt(num):
#     #     square_numbers.append(num)
#     if check_not_square(num):
#         count += 1

# print(count)

import math

import sys

input = sys.stdin.readline
min, max = 1000000000000, 1000000000000 + 1000000
check_array = [ True ] * (max - min + 1)

idx = 2

while idx * idx <= max:
    
    start = min + (int(idx * idx - int(min % (idx * idx))) if int(min % (idx * idx)) != 0 else int(min % (idx * idx)))
    while start <= max:
        if check_array[start - min]:
            check_array[start - min] = False
        start += int(idx * idx)
    idx += 1

print(check_array.count(True))