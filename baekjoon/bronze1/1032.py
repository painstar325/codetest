# https://www.acmicpc.net/problem/1032

import sys
input = sys.stdin.readline

def find_another_char(item):
    stan = item[0]
    for c in item:
        if c != stan:
            return "?"
    return stan

N = int(input())
filenames = [input() for _ in range(N)]

result = ""
for item in zip(*filenames):
    result += find_another_char(item)

print(result)