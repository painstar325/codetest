import sys
input = sys.stdin.readline
# a, b = map(int, input().split())
a, b = -2, 5
a, b = 5, 6
a, b = -2131231, 2131232
if a < 0 and b < 0:
    print(abs(min(a, b) - max(a, b)))
else:
    print((abs(a) + abs(b)) if a < 0 or b < 0 else max(a, b) - min(a, b))