def bfs(si, sj, L):
    v = [[100] * M for _ in range(N)]
    v[si][sj] = 1
    q = [(si, sj)]

    d = {1: ((-1, 0), (1, 0), (0, -1), (0, 1)),
         2: ((-1, 0), (1, 0)),
         3: ((0, -1), (0, 1)),
         4: ((-1, 0), (0, 1)),
         5: ((1, 0), (0, 1)),
         6: ((1, 0), (0, -1)),
         7: ((-1, 0), (0, -1))}

    cnt = 1

    while q:
        ci, cj = q.pop(0)

        if v[ci][cj] == L:
            return cnt

        for di, dj in d[arr[ci][cj]]:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < M:
                # 현재 위치와 다음 위치가 연결되어 있는 지 확인
                if (di == -1 and arr[ni][nj] in [1, 2, 5, 6]) \
                        or (di == 1 and arr[ni][nj] in [1, 2, 4, 7]) \
                        or (dj == -1 and arr[ni][nj] in [1, 3, 4, 5]) \
                        or (dj == 1 and arr[ni][nj] in [1, 3, 6, 7]):
                    if v[ni][nj] > v[ci][cj] + 1:
                        cnt += 1
                        v[ni][nj] = v[ci][cj] + 1
                        q.append((ni, nj))

    return cnt


T = int(input())

for test_case in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]

    print(f"#{test_case} {bfs(R, C, L)}")