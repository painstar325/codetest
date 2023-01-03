# https://www.acmicpc.net/problem/1475

import sys
input = sys.stdin.readline

X = list(map(int, list(input().strip())))
cnt = 0
while len(X) > 1:
    cnt += 1
    Y = sum(X)
    X = list(map(int, list(str(Y))))
else:
    Y = sum(X)
print(cnt)
print("YES" if Y % 3 == 0 else "NO")
