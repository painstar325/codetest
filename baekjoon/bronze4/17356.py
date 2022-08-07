# https://www.acmicpc.net/problem/17356

import sys
input = sys.stdin.readline

Wook, jae = map(int, input().split())
# jae = int(input())

M = (jae - Wook) / 400
print(1 / (1 + (10 ** M)))