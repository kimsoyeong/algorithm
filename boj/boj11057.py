n = int(input())

#  1, 2: 뒤쪽에 숫자 추가하는 방식
#  3: 앞쪽에 숫자 추가하는 방식

# 1. 2차원 DP 배열 (111,140KB/ 136ms)
dp = [[0] * 10 for _ in range(n + 1)]
dp[1] = [1] * 10

for i in range(2, n + 1):
    for j in range(10):
        dp[i][j] = sum(dp[i - 1][j:])

print(sum(dp[n][:]) % 10007)

# 2. 1차원 DP 배열 (110,612KB/ 136 ms)
#   - 행 구분없이 계속 덮어쓰는 것
#   - 1번 풀이와 큰 차이는 없음.
dp = [1] * 10

for i in range(2, n + 1):  # N - 1번 처리
    for j in range(10):
        dp[j] = sum(dp[j:])

print(sum(dp) % 10007)


# 3.  앞쪽에 숫자 추가 (109,240KB/ 120 ms)
#    - 2중 for 문 내 매번 호출하던 sum함수가 생략되서 더 빨라짐. (어마어마한 의미는 없음)
dp = [1] * 10

for i in range(n - 1):  #  2 ~ n + 1만큼 순회하는 것과 동일함. 어차피 i를 안 쓰기 때문에 n - 1번 반복하는 것과 동일.
    for j in range(1, 10):
        dp[j] = dp[j] + dp[j - 1]  # dp[j - 1]은 지금까지 합이 누적된 것. 이걸 더하면, j위치도 누적값이 되는 것.

print(sum(dp) % 10007)
