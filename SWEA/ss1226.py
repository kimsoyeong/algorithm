T = 10


def bfs(S):
    visited = [[0] * 16 for _ in range(16)]
    visited[S[0]][S[1]] = 1
    queue = [S]

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    while queue:
        ci, cj = queue.pop(0)

        # 여기서 정답 처리!!
        if arr[ci][cj] == 3:
            return 1

        for i, j in zip(di, dj):
            ni, nj = ci + i, cj + j
            if 0 <= ni < 16 and 0 <= nj < 16:  # 범위 내
                if arr[ni][nj] != 1 and visited[ni][nj] == 0:  # 벽 제외, 미방문 통로만
                    queue.append((ni, nj))
                    visited[ni][nj] = 1  # 방문 처리

    return 0


for test_case in range(1, T + 1):
    N = int(input())

    arr = []
    S = (0, 0)  # (i, j)
    for i in range(16):
        arr.append(list(map(int, input())))

        if 2 in arr[i]:
            S = (i, arr[i].index(2))

    print(f"#{test_case} {bfs(S)}")
