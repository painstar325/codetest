n = int(input())

for x in range(n):
    for y in range(x + 1):
        print('*', end='')
    print()  