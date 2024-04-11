def dfs(n, ci, cj, sm, smc):
    global mx

    if smc > C:  # 가지치기: 종료
        return

    if n == M:  # 정답처리
        mx = max(mx, sm)
        return

    dfs(n + 1, ci, cj, sm + (arr[ci][cj + n] ** 2), smc + arr[ci][cj + n])  # 포함O
    dfs(n + 1, ci, cj, sm, smc)  # 포함X


T = int(input())

for test_case in range(1, T + 1):
    N, M, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = mx = sm1 = 0
    for si in range(N):
        for sj in range(N - M + 1):
            mx = 0
            dfs(0, si, sj, 0, 0)  # 일꾼 1
            sm1 = mx
            for di in range(si, N):
                for dj in range(sj + M if di == si else 0, N - M + 1):
                    mx = 0
                    dfs(0,di, dj, 0, 0)  # 가능한 일꾼 2
                    ans = max(ans, sm1 + mx)

    print(f"#{test_case} {ans}")
