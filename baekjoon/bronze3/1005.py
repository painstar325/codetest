# https://www.acmicpc.net/problem/1005

from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    build_times = [0] + list(map(int, input().split()))
    ms_temp = build_times.copy()
    connect = {}
    in_degree_dict = {}
    
    for _ in range(K):
        pre, next = map(int, input().split())
        if pre not in connect:
            connect[pre] = []
        connect[pre].append(next)
        if next not in in_degree_dict:
            in_degree_dict[next] = 0
        if pre not in in_degree_dict:
            in_degree_dict[pre] = 0
        in_degree_dict[next] += 1
        
    last = int(input())
    

    # first = dict((count, node) for node, count in in_degree_dict.items()).get(0)
    # print(first)

    q = deque()
    # q.append(first)

    for key, value in in_degree_dict.items():
        if value == 0:
            q.append(key)
            ms_temp[key] = build_times[key]


    while(len(q)):
        node = q.popleft()
        if node not in connect:
            continue
        for next in connect[node]:
            ms_temp[next] = max(ms_temp[next], ms_temp[node] + build_times[next])
            in_degree_dict[next] -= 1
            if in_degree_dict[next] == 0:
                q.append(next)

    print(ms_temp[last])