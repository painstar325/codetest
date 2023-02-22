# https://www.acmicpc.net/problem/1021

import sys

input = sys.stdin.readline


def findstep(num, q, start, step):
    end = start + (len(q) + 1 if step > 0 else -len(q) - 1)
    count = 0
    for idx in range(start, end, step):
        if num == q[idx % len(q)]:
            break
        count += 1
    return count


N, M = map(int, input().split())

nums = list(map(int, input().split()))

q = [i for i in range(1, N + 1)]

head = 0
count = 0
for num in nums:
    step1 = findstep(num, q, head, 1)
    step2 = findstep(num, q, head, -1)

    if step1 < step2:
        count += step1
        head = (len(q) + head + step1) % len(q)
    else:
        count += step2
        head = (len(q) + head - step2) % len(q)
    del q[head]

print(count)
