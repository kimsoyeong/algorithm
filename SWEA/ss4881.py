def dfs(n, sm):
    """
    :param n: 행 번호
    :return:
    """
    global ans
    # 가지 치기
    if sm >= ans:
        return

    # 종료 조건
    if n == N:
        # 정답 처리
        ans = min(sm, ans)
        return

    for j in range(N):
        # 사용 여부 check: 사용안 한 경우만
        if visited[j] == 0:
            visited[j] = 1   # 사용(방문) 표시
            dfs(n + 1, sm + arr[n][j])
            visited[j] = 0  # 다시 초기화 (중요)


T = int(input())

for test_case in range(1, T + 1):
    N = int(input())

    arr = [list(map(int, input().split())) for n in range(N)]
    visited = [0] * N

    ans = N * 10
    dfs(0, 0)
    print(f"#{test_case} {ans}")
