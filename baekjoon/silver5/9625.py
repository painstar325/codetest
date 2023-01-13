# https://www.acmicpc.net/problem/9625
from collections import deque
import sys

input = sys.stdin.readline

K = int(input())

a = 1
b = 0

for _ in range(K):
    temp = a
    a = b
    b = temp + b

print(a, b)
