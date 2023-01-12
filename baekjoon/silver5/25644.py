# https://www.acmicpc.net/problem/25644

import sys

input = sys.stdin.readline

N = int(input())
days = list(map(int, input().split()))

day_tuples = [(val, i) for i, val in enumerate(days)]
day_tuples.sort()

max_idx = len(days) - 1

pre_max_idx = -1

score = 0
for max_idx in reversed(range(len(days))):
    if pre_max_idx >= day_tuples[max_idx][1]:
        continue
    for min_idx in range(pre_max_idx + 1, day_tuples[max_idx][1] + 1):
        if day_tuples[max_idx][0] - days[min_idx] > score:
            score = day_tuples[max_idx][0] - days[min_idx]
    pre_max_idx = day_tuples[max_idx][1]
    if pre_max_idx == len(days) - 1:
        break

print(score)
