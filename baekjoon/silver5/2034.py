# https://www.acmicpc.net/problem/2034

import sys
input = sys.stdin.readline

def calc_idx(src, next, max):
    next = next - max if next > max else next
    if next > max:
        next = next - max
    elif next < -max:
        next = max + next

    if src + next < 0:
        return max + src + next
    elif src + next >= max:
        return src - max + next
    else:
        return src + next

N = int(input())

sheet = [int(input()) for _ in range(N)]

stan = ["A","","B","C","","D","","E","F","","G",""]

result = []

for start_idx in range(len(stan)):
    if stan[start_idx] == "":
        continue
    start = stan[start_idx]
    sheet_idx = start_idx
    for idx in sheet:
        sheet_idx = calc_idx(sheet_idx, idx, len(stan))
        if stan[sheet_idx] == "":
            break
    else:
        result.append([stan[start_idx], stan[sheet_idx]])

for r in result:
    print(r[0], r[1])