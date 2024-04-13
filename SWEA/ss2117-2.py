T = int(input())

cost = [(k*k + (k-1)*(k-1)) for k in range(40)]  # 가능한 운영비용 미리 계산

for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0

    # [1] home 배열 생성: 집 좌표 모아보기
    home = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:  # 집이면,
                home.append((i, j))

    # [2] 모든 좌표 순회하면서, dist(누적) 배열 만들고, cnt
    for si in range(N):
        for sj in range(N):
            dist = [0] * 40
            # 현재 좌표(si, sj)와 home에 속한 좌표(hi, hj)의 거리를 계산.
            # dist[k]: (si, sj)에서 k만큼 떨어진(거리가 k인) 집의 수.
            # 단, 같은 좌표 = 1
            for hi, hj in home:
                t = abs(si - hi) + abs(sj - hj) + 1  # 유클리드 거리 + 1
                dist[t] += 1

            house = 0  #
            for k in range(1, 40):
                house += dist[k]  # 거리 k까지 속해있는 집의 수 누적.
                if cost[k] <= house * M:  # 운영비용 <= 수익
                    ans = max(ans, house)  # 정답 갱신

    print(f"#{test_case} {ans}")