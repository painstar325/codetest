# https://www.acmicpc.net/problem/1264

import sys
import re
input = sys.stdin.readline

line = input()
while line[0] != '#':
    print(len(re.findall('[a|e|i|o|u]', line.lower())))
    line = input()
