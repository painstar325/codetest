import sys
input = sys.stdin.readline
nums = list(map(int, input().split()))

num_sum = 0
for num in nums:
    num_sum += (num ** 2)
print(num_sum % 10)