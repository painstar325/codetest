
#동적계획법을 문제
#메모제이션을 사용하여 중복된 계산을 최소화 하여 알고리즘 수행 시간 단축

N = int(input())

# 실패.. 재귀는 너무 오래 걸림
# def make_1(src):
#     if src == 1:
#         return 0
#     division_3 = 1000000
#     division_2 = 1000000
#     sub_1 = 1000000
#     if src % 3 == 0:
#         division_3 = make_1(src / 3)
#     if src % 2 == 0:
#         division_2 = make_1(src / 2)
#     sub_1 = make_1(src - 1)
#     return min(division_3, division_2, sub_1) + 1

# print(make_1(N))

# memo = [0 for _ in range(N + 1)]
memo = [0] * (N + 1)

for i in range(2, N + 1):
    memo[i] = memo[i - 1] + 1
    if i % 3 == 0 :
        memo[i] = min(memo[i], memo[int(i / 3)] + 1)
    if i % 2 == 0 :
        memo[i] = min(memo[i], memo[int(i / 2)] + 1)
    
print(memo[N])
