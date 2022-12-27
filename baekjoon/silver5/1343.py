# https://www.acmicpc.net/problem/1343

import sys
input = sys.stdin.readline

def replace_word():
    polyA = "AAAA"
    polyB = "BB"

    words = input().strip().split(".")
    result = []
    for word in words:
        cnt = 0
        if len(word) % 2 != 0:
            return "-1"
        new_word = ""
        while(cnt < len(word)):
            if len(word[cnt:]) >= 4:
                new_word += polyA
                cnt += 4
            else:
                new_word += polyB
                cnt += 2
            
        result.append(new_word)
    return ".".join(result)

print(replace_word())


