def dfs(j, sm, smc):
    global si, sj, ans

    if smc == C and sm < ans:
        return

    if smc > C:  # 가지치기: 종료
        return

    if j == sj + M:  # 정답처리
        if smc <= C:  # 없어도 되는 조건이지만, 있을 때 실행 시간이 더 짧음
            ans = max(ans, sm)
        return

    dfs(j + 1, sm + (arr[si][j] ** 2), smc + arr[si][j])  # 포함O
    dfs(j + 1, sm, smc)  # 포함X


T = int(input())

for test_case in range(1, T + 1):
    N, M, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    v = [[0] * N for _ in range(N)]

    for si in range(N):
        for sj in range(N - M + 1):
            ans = 0
            dfs(sj, 0, 0)
            v[si][sj] = ans

    answer = 0
    for i in range(N):
        for j in range(N - M + 1):
            mx = 0
            for di in range(i, N):
                for dj in range(j + M if di == i else 0, N):
                    mx = max(v[di][dj], mx)
            answer = max(answer, v[i][j] + mx)

    print(f"#{test_case} {answer}")
