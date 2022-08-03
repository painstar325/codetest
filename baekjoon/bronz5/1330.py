import sys
input = sys.stdin.readline
# a, b = map(int, input().split())
a, b = 70, 6
if a > b:
    print('>')
elif a < b:
    print('<')
else:
    print('==')
    