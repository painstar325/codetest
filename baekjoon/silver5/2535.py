# https://www.acmicpc.net/problem/2535

import sys

input = sys.stdin.readline

N = int(input())

students = {}
for _ in range(N):
    country, student, score = map(int, input().split())
    students[score] = {"country": country, "student": student}

country_cnt = 0
pre_country = -1
cnt = 0
for score, val in sorted(students.items(), reverse=True):
    if pre_country == val["country"] and country_cnt == 2:
        continue
    elif pre_country == val["country"]:
        country_cnt += 1
    else:
        pre_country = val["country"]
        country_cnt = 1
    print(val["country"], val["student"])
    cnt += 1
    if cnt == 3:
        break
