T = int(input())


def bfs(si, sj):
    # v = [[0] * N for _ in range(N)]
    v[si][sj] = 1
    queue = [(si, sj)]
    ans = [arr[si][sj]]

    while queue:
        ci, cj = queue.pop(0)

        # 4방향 범위 내, 미방문, "나(current)와 1 차이"
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = ci + di, cj + dj
            if N > ni >= 0 and 0 <= nj < N:
                if v[ni][nj] == 0 and abs(arr[ci][cj] - arr[ni][nj]) == 1:
                    queue.append((ni, nj))
                    v[ni][nj] = 1
                    ans.append(arr[ni][nj])

    return min(ans), len(ans)


for test_case in range(1, T + 1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]
    v = [[0] * N for _ in range(N)]

    num = N * N
    cnt = 0
    for i in range(N):
        for j in range(N):
            if v[i][j] == 0:  # 방문안 한 숫자
                tmn, tcnt = bfs(i, j)
                if tcnt > cnt or (tcnt == cnt and num > tmn):
                    # 방 개수 더 많음 or 개수 똑같고 방 번호 작음
                    cnt = tcnt
                    num = tmn

    print(f"#{test_case} {num} {cnt}")

# Runtime error
# def bfs(si, sj):
#     visited = [[0] * N for _ in range(N)]
#     visited[si][sj] = 1
#     queue = [(si, sj)]
#     ans = 1
#
#     while queue:
#         ci, cj = queue.pop(0)
#
#         # 여기서 정답 처리!!
#         ans = max(ans, visited[ci][cj])
#
#         for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
#             ni, nj = ci + di, cj + dj
#             if 0 <= ni < N and 0 <= nj < N:
#                 if visited[ni][nj] == 0 and arr[ni][nj] - arr[ci][cj] == 1:
#                     visited[ni][nj] = visited[ci][cj] + 1
#                     queue.append((ni, nj))
#
#     return ans
#
#
# for test_case in range(1, T + 1):
#     N = int(input())
#
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     mx = 0
#     mx_room = -1
#     for i in range(N):
#         for j in range(N):
#             # arr[i][j]: room number
#             tmp = bfs(i, j)  # 개수
#
#             if tmp > mx:
#                 mx = tmp
#                 mx_room = arr[i][j]
#
#     print(f"#{test_case} {mx_room} {mx}")
