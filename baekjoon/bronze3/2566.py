# https://www.acmicpc.net/problem/2566

import sys
input = sys.stdin.readline

max_x, max_y = 1, 1
max_value = 0

for i in range(9):
    arr = list(map(int, input().split()))
    for j, value in enumerate(arr):
        if max_value < value:
            max_value = value
            max_x = i + 1
            max_y = j + 1

print(max_value)
print(max_x, max_y)