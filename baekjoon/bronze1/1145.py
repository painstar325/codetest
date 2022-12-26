# https://www.acmicpc.net/problem/1145
from itertools import combinations
from math import gcd
import sys
input = sys.stdin.readline
nums = list(map(int, input().split()))
combis = combinations(nums, 3)
result = 10000000000
for num1, num2, num3 in combis:
    temp = (num1 * num2) // gcd(num1, num2)
    temp = (temp * num3) // gcd(temp, num3)
    if result > temp:
        result = temp

print(result)