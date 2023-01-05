# https://www.acmicpc.net/problem/2238

import sys
input = sys.stdin.readline

def find_min_key(src, start):
    min_key = start
    for key, val in src.items():
        if src[min_key] > val or (src[min_key] == val and key < min_key):
            min_key = key
    return min_key

U, N = map(int, input().split())

names = []
prices = []
price_dict = {}
for _ in range(N):
    name, price = map(str, input().strip().split())
    price = int(price)
    if price not in price_dict:
        price_dict[price] = 0
    price_dict[price] += 1
    names.append(name)
    prices.append(price)

min_key = find_min_key(price_dict, prices[0])

min_idx = prices.index(min_key)
print(names[min_idx], prices[min_idx])