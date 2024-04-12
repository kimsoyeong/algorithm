n = int(input())

dp = [0] * (n + 1)
dp[0] = 1
dp[1] = 1

for i in range(2, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2] * 2
    # dp[i - 1]: 2x1 타일 더 추가되는 경우의 수
    # 1) dp[i - 2]: 1x2 타일 추가되는 경우의 수
    # 2) dp[i - 2]: 2x2 타일 추가되는 경우의 수

print(dp[n] % 10007)