# https://www.acmicpc.net/problem/2238
from collections import deque
import sys

input = sys.stdin.readline

a_to_i = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
a_to_i_dict = {chr(65 + i): a_to_i[i] for i in range(len(a_to_i))}

a = list(input().strip())
b = list(input().strip())

q = deque()

for woman, man in zip(a, b):
    q.append(a_to_i_dict[woman])
    q.append(a_to_i_dict[man])

while len(q) > 2:
    l = len(q) - 1
    temp = q.popleft()
    for _ in range(l):
        temp2 = q.popleft()
        q.append((temp2 + temp) % 10)
        temp = temp2


print(str(q.popleft()) + str(q.popleft()))
