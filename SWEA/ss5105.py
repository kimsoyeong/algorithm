T = int(input())


def bfs(S, E, arr):
    visited = [[0] * N for _ in range(N)]
    queue = [S]

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    while queue:
        ci, cj = queue.pop(0)

        # 정답 처리 여기서!
        if ci == E[0] and cj == E[1]:
            return visited[ci][cj] - 1

        for i, j in zip(di, dj):
            ni, nj = ci + i, cj + j
            if 0 <= ni < N and 0 <= nj < N:
                if not visited[ni][nj] and arr[ni][nj] != '1':
                    queue.append((ni, nj))
                    visited[ni][nj] = visited[ci][cj] + 1

    return 0


for test_case in range(1, T + 1):
    N = int(input())

    arr = []

    S = E = (0, 0)  # (i, j)
    for i in range(N):
        arr.append(list(input()))

        if '2' in arr[i]:
            S = (i, arr[i].index('2'))
        if '3' in arr[i]:
            E = (i, arr[i].index('3'))

    print(f"#{test_case} {bfs(S, E, arr)}")
