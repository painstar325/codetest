#https://www.acmicpc.net/problem/1270

import sys

input = sys.stdin.readline

N = int(input())
results = []
for i in range(N):
    army = list(map(str, input().strip().split()))
    team = army[0]
    del army[0]
    
    army_len = len(army)
    
    army_dict = {}
    for num in army:
        if num not in army_dict:
            army_dict[num] = 1
        else:
            army_dict[num] += 1
    
    for key, value in list(sorted(army_dict.items(), key=lambda item: item[1], reverse=True)):
        if value + value > army_len:
            results.append(key)
        else:
            results.append("SYJKGW")
            
        break
    
    
for result in results:
    print(result)