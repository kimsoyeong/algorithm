T = int(input())

from collections import deque


def bfs(si, sj):
    v = [[0] * N for _ in range(N)]
    v[si][sj] = 0
    q = deque()
    q.append((si, sj))

    while q:
        ci, cj = q.popleft()

        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # 상하좌우 4방향
            ni, nj = ci + di, cj + dj

            if 0 <= ni < N and 0 <= nj < N:  # 범위 내
                # 방문한 적이 없거나
                # (방문 했었는데) 더 적은 연료가 소모되는 길로 가거나
                if v[ni][nj] == 0\
                        or v[ni][nj] > v[ci][cj] + 1 + max(arr[ni][nj] - arr[ci][cj], 0):  # 낮은 곳으로 이동할 땐 연료 X
                    q.append((ni, nj))
                    v[ni][nj] = v[ci][cj] + 1 + max(arr[ni][nj] - arr[ci][cj], 0)

    return v[N - 1][N - 1]


for test_case in range(1, T + 1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    print(f"#{test_case} {bfs(0, 0)}")
