# https://www.acmicpc.net/problem/1075

import sys
input = sys.stdin.readline

N = int(input())
F = int(input())

new_N = (int(N / 100) * 100)
for tail in range(100):
    if ((new_N + tail) / F).is_integer():
        print(f"{tail:02d}")
        break
