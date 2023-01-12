# https://www.acmicpc.net/problem/2238

import sys

input = sys.stdin.readline

interest_rate_dict = {1: 1.05, 3: 1.2, 5: 1.35}


def invest(score, max_year, now_year, new_year):
    if max_year < now_year + new_year:
        return score
    result = int(score * (interest_rate_dict[new_year]))
    return max(
        invest(result, max_year, now_year + new_year, 1),
        invest(result, max_year, now_year + new_year, 3),
        invest(result, max_year, now_year + new_year, 5),
    )


H, Y = map(int, input().split())

print(max(invest(H, Y, 0, 1), invest(H, Y, 0, 3), invest(H, Y, 0, 5)))
