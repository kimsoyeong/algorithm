directions = [(1, 1), (1, -1), (-1, -1), (-1, 1)]


def dfs(i, j, cnt, tour, d):
    global si, sj, ans

    if d >= 3:
        if i == si and j == sj:
            ans = max(ans, cnt)
            return

    for idx, (di, dj) in enumerate(directions[d: d + 2]):
        ni, nj = i + di, j + dj
        if 0 <= ni < N and 0 <= nj < N:
            if (v[ni][nj] == 0 and arr[ni][nj] not in tour) or (ni == si and nj == sj):
                v[ni][nj] = 1
                dfs(ni, nj, cnt + 1, tour + [arr[ni][nj]], d + idx)
                v[ni][nj] = 0


T = int(input())

for test_case in range(1, T + 1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]
    v = [[0] * N for _ in range(N)]
    ans = 0

    for i in range(N):
        for j in range(1, N - 1):
            si = i
            sj = j
            dfs(i, j, 0, [arr[i][j]], 0)

    if ans <= 1: ans = -1
    print(f"#{test_case} {ans}")
