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

    ans = 0
    mem = [[0] * N for _ in range(N)]
    # 각 위치의 가능한 최대값을 한 번 저장
    # 동일한 위치에서 dfs 호출로 인한 중복 연산을 방지.
    for i in range(N):
        for j in range(N - M + 1):
            mx = 0
            dfs(0, i, j, 0, 0)
            mem[i][j] = mx

    for i1 in range(N):
        for j1 in range(N - M + 1):
            for i2 in range(i1, N):
                for j2 in range(j1 + M if i1 == i2 else 0, N - M + 1):
                    ans = max(ans, mem[i1][j1] + mem[i2][j2])

    print(f"#{test_case} {ans}")
