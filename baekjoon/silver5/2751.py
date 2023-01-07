# https://www.acmicpc.net/problem/2751

import sys

input = sys.stdin.readline

N = int(input())

arr = [int(input()) for _ in range(N)]

arr.sort()

for val in arr:
    print(val)
