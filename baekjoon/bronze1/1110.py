# https://www.acmicpc.net/problem/1110

import sys
input = sys.stdin.readline

N = int(input())

new_N = N
count = 0
while(True):
    count += 1
    sum = 0
    for num in str(new_N):
        sum += int(num)
    new_N = (new_N % 10 * 10) + (sum if sum < 10 else sum % 10)
    if N == new_N:
        print(count)
        break
    


