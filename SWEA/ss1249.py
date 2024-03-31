T = int(input())

from collections import deque

INF = 10000


def bfs(si, sj):
    v = [[INF] * N for _ in range(N)]
    q = deque()
    q.append((si, sj))

    v[si][sj] = arr[si][sj]

    while q:
        ci, cj = q.popleft()

        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N \
                    and v[ni][nj] > v[ci][cj] + arr[ni][nj]:
                v[ni][nj] = v[ci][cj] + arr[ni][nj]
                q.append((ni, nj))

    return v[N - 1][N - 1]


for test_case in range(1, T + 1):
    N = int(input())

    arr = [list(map(int, input())) for _ in range(N)]

    print(f"#{test_case} {bfs(0, 0)}")
