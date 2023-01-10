# https://www.acmicpc.net/problem/2238

import sys

input = sys.stdin.readline

N = int(input())

cnt = 0
result = -1
while True:
    coin5 = (N // 5) + cnt
    coin2 = (N - (coin5 * 5)) // 2
    mod2 = (N - (coin5 * 5)) % 2
    if coin5 <= 0 and mod2 == 1:
        result = -1
        break
    elif coin5 >= 0 and mod2 == 0:
        result = coin5 + coin2
        break
    cnt -= 1

print(result)
