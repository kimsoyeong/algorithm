T = int(input())

for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())

    arr = [[[]] * N for _ in range(N)]  # 미생물군집: 미생물 수, 이동방향
    positions = []  # 미생물군집 위치 (i, j)
    for _ in range(K):
        i, j, n, d = map(int, input().split())
        positions.append((i, j))
        arr[i][j] = [(n, d)]

    dirs = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]

    for time in range(M):
        new_cmd = []
        for (i, j) in positions:
            n, d = arr[i][j][0]
            ni, nj = i + dirs[d][0], j + dirs[d][1]

            # 약품 셀 도착
            if ni == 0 or ni == N - 1 or nj == 0 or nj == N - 1:
                n = n // 2  # 미생물 수 타노스 당함
                # 이동 방향 전환
                if d == 1:
                    d = 2
                elif d == 2:
                    d = 1
                elif d == 3:
                    d = 4
                else:
                    d = 3

            # 새로운 위치로 이동
            arr[i][j].pop(0)  # 기존 위치에서 제거
            if len(arr[ni][nj]) > 0:  # 이동하려는 위치에 다른 군집 이미 있는 경우
                arr[ni][nj] += [(n, d)]  # 추가
            else:
                arr[ni][nj] = [(n, d)]

            # update cmd
            new_cmd.append((ni, nj))

        t = set(new_cmd)
        for (i, j) in t:
            if len(arr[i][j]) > 1:
                ans_n = ans_d = mx = 0
                for (tmp_n, tmp_d) in arr[i][j]:  # dc[k]:
                    ans_n += tmp_n
                    if mx < tmp_n:
                        mx = tmp_n
                        ans_d = tmp_d
                arr[i][j] = [(ans_n, ans_d)]

        positions = list(t)

    ans = 0
    for (i, j) in positions:
        ans += arr[i][j][0][0]

    print(f"#{test_case} {ans}")
