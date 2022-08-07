# https://www.acmicpc.net/problem/10984

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    sum_C, sum_G = 0, 0
    for _ in range(N):
        C, G = map(float, input().split())
        sum_C += C
        sum_G += (C * G)
    print(int(sum_C), round(sum_G / sum_C, 1))
