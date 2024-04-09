def dfs(n, sm, cnt):
    global ans

    if cnt == N:
        ans = min(ans, sm + e[n - 1][0])
        return

    for s in range(2, N + 1):
        if visited[s] == 0:
            visited[s] = 1
            dfs(s, sm + e[n - 1][s - 1], cnt + 1)
            visited[s] = 0


T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    e = [list(map(int, input().split())) for _ in range(N)]

    visited = [0] * (N + 1)

    ans = 1000 * N
    dfs(1, 0, 1)

    print(f"#{test_case} {ans}")
