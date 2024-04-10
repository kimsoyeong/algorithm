def dfs(n, sm1, sm2):
    global ans

    if len(sm1) > N / 2:
        return

    if n == N:
        if len(sm1) == N / 2:
            tmp1 = tmp2 = 0
            for i in sm1:
                for j in sm1:
                    tmp1 += S[i][j]
            for i in sm2:
                for j in sm2:
                    tmp2 += S[i][j]

            ans = min(ans, abs(tmp1 - tmp2))
        return

    dfs(n + 1, sm1 + [n], sm2)  # A에 식재료 추가
    dfs(n + 1, sm1, sm2 + [n])  # B에 식재료 추가


T = int(input())

for test_case in range(1, T + 1):
    N = int(input())

    S = [list(map(int, input().split())) for _ in range(N)]

    ans = 20000 * N * N
    dfs(0, [], [])

    print(f"#{test_case} {ans}")
