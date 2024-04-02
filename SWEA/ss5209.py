def dfs(i, sm):
    global ans

    if sm >= ans:
        return

    if i == N:
        ans = min(ans, sm)
        return

    for j in range(N):
        if v[j] == 0:
            v[j] = 1
            dfs(i + 1, sm + V[i][j])
            v[j] = 0


T = int(input())

for test_case in range(1, T + 1):
    N = int(input())

    V = [list(map(int, input().split())) for i in range(N)]

    v = [0] * N
    ans = 99 * N
    dfs(0, 0)

    print(f"#{test_case} {ans}")
