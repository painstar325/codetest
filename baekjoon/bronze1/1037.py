# https://www.acmicpc.net/problem/1037

import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
numbers.sort()


if N > 1:
    print(numbers[0] * numbers[len(numbers) - 1])
else:
    print(numbers[0] * numbers[0])



