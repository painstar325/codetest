# https://www.acmicpc.net/problem/1181

from collections import deque

import sys
input = sys.stdin.readline

N = int(input())

q = deque([val + 1 for val in range(N)])
print_arr = []
while(len(q) > 1):
    print_arr.append(str(q.popleft()))
    temp = q.popleft()
    q.append(temp)
else:
    print_arr.append(str(q.popleft()))

print(" ".join(print_arr))