# https://www.acmicpc.net/problem/2439

import sys
input = sys.stdin.readline

num = int(input())

for y in range(num):
    for x in reversed(range(num)):
        if x <= y:
            print('*', end='')
        else:
            print(' ', end='')
    print()