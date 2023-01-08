# https://www.acmicpc.net/problem/10826

import sys

input = sys.stdin.readline

N = int(input())

if N == 0:
    print(0)
elif N == 1:
    print(1)
else:
    result = 0
    fn = 0
    fn2 = 1

    for idx in range(1, N):
        result = fn + fn2
        fn = fn2
        fn2 = result

    print(result)
