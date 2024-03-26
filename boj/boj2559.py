N, K = map(int, input().split())  # 날짜 수, 연속적 날짜 수

lst = list(map(int, input().split()))

# 1. 시간 초과
# ans = sum(lst[0:K])
# for i in range(1, N):
#     ans = max(ans, sum(lst[i: i+K]))
#
# print(ans)

ans = sum(lst[0:K])
tmp = ans
for i in range(1, N - K + 1):
    tmp = tmp - lst[i - 1] + lst[i + K - 1]
    ans = max(ans, tmp)

print(ans)
