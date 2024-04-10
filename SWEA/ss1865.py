def dfs(n, sm):
    global ans

    if ans >= sm:  # 가지치기: 시간초과 방지
        return

    if n == N:
        ans = max(ans, sm)
        return

    for i in range(N):
        if visited[i] == 0 and P[n][i] > 0:
            visited[i] = 1
            dfs(n + 1, sm * (P[n][i] / 100))
            visited[i] = 0


T = int(input())

for test_case in range(1, T + 1):
    N = int(input())

    P = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N

    ans = 0
    dfs(0, 100)
    print(f"#{test_case} {ans:.6f}")
