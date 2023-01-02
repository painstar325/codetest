# https://www.acmicpc.net/problem/1475

import sys
input = sys.stdin.readline

N = list(input().strip())

num_dict = {}
for num in N:
    if num not in num_dict:
        num_dict[num] = 0
    num_dict[num] += 1

result = 0
for key, val in num_dict.items():
    if result < val and key not in ['6', '9']:
        result = val
#6, 9계산
temp = int((num_dict.get('6', 0) + num_dict.get('9', 0)) / 2) + ((num_dict.get('6', 0) + num_dict.get('9', 0)) % 2)
if result < temp:
    result = temp

print(result)