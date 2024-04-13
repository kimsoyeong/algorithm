T = int(input())

cost = [(k*k + (k-1)*(k-1)) for k in range(40)]  # 가능한 운영비용 미리 계산

for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    for i in range(N):
        for j in range(N):
            # i, j: 현재 방문 중인 집의 좌표
            k = scale = 1

            while scale < N*2:  # scale이 최대 가능 크기보다 작은 동안
                scale = 2*k - 1  # 마름모의 크기(높이 == 너비)
                house = 0  # 마름모 내 집의 수

                # 마름모 탐색
                e = scale // 2
                for di in range(-e, 1):  # 마름모 위쪽
                    for dj in range(-e - di, e + di + 1):
                        ni, nj = i + di, j + dj
                        if 0 <= ni < N and 0 <= nj < N:  # 좌표 범위
                            if arr[ni][nj] == 1:  # 집이 있으면
                                house += 1
                for di in range(1, e + 1):  # 마름모 아래쪽
                    for dj in range(-e + di, e - di + 1):
                        ni, nj = i + di, j + dj
                        if 0 <= ni < N and 0 <= nj < N:  # 좌표 범위
                            if arr[ni][nj] == 1:  # 집이 있으면
                                house += 1

                # 정답 갱신
                if cost[k] <= M * house:  # 비용 <= 수익
                    ans = max(ans, house)

                # k 갱신
                k += 1

    print(f"#{test_case} {ans}")
