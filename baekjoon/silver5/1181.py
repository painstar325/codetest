# https://www.acmicpc.net/problem/1181

import sys
input = sys.stdin.readline

N = int(input())
str_arr = [input().replace("\n", "") for _ in range(N)]
str_dict = {}
for s in str_arr:
    if len(s) not in str_dict:
        str_dict[len(s)] = []
    str_dict[len(s)].append(s)
new = dict()
for key, array in sorted(str_dict.items()):
    for item in sorted(list(set(array))):
        print(item)