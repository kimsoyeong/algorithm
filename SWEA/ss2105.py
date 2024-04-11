directions = [(1, 1), (1, -1), (-1, -1), (-1, 1)]


def dfs(i, j, cnt, tour, d):
    """
    :param i: arr i좌표
    :param j: arr j좌표
    :param cnt: 현재 방문 카페의 수 (디저트 중복X)
    :param tour: 방문한 카페들의 디저트 종류 배열 (중복X)
    :param d: 투어 이동 방향
    """
    global ans

    # 가지치기: 투어(사각형)의 반을 돌았는데(전체 방문 카페 수는 현재 cnt의 2배가 됨), 이미 정답보다 작은 경우
    if d == 2 and cnt * 2 <= ans:
        return

    if d > 3:  # 종료조건 (무조건 종료)
        return

    if d == 3 and i == si and j == sj:  # 정답 처리: 마지막 방향 and 시작점 도착
        ans = max(ans, cnt)
        return

    for idx, (di, dj) in enumerate(directions[d: d + 2]):
        ni, nj = i + di, j + dj
        if 0 <= ni < N and 0 <= nj < N:
            if (arr[ni][nj] not in tour) or (ni == si and nj == sj):
                dfs(ni, nj, cnt + 1, tour + [arr[ni][nj]], d + idx)


T = int(input())

for test_case in range(1, T + 1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]
    # visited 배열 사용 X: 어차피 방향 전환하면서, 시작점 외에 중복 방문은 불가능하다.
    ans = 0

    for i in range(N):  # 실제 필요 범위는 N - 2 전까지 => 시간이 더 오래 걸려서 그냥 N으로 둠
        for j in range(1, N - 1):
            si = i
            sj = j
            dfs(i, j, 0, [arr[i][j]], 0)
            # dfs(i, j, 0, [], 0)  # tour를 빈 배열로 넘겨주면, for문 안에서 ni == si and nj == sj 조건이 필요없어지나 실제 실행 시간은 더 오래걸렸다.

    if ans <= 1: ans = -1
    print(f"#{test_case} {ans}")
