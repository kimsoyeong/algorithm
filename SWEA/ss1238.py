T = 2


def bfs(S):
    visited = [0] * 101
    visited[S] = 1
    queue = [S]

    ans = S  # 반환할 노드 번호
    while queue:
        c = queue.pop(0)

        # [2 sol] 여기서 정답 처리!!
        if (visited[ans] < visited[c]) \
                or (visited[ans] == visited[c] and ans < c):
            # 더 늦게 연락 받거나
            # 동시에 연락 받는 데, 번호 더 큼
            ans = c

        for nxt in arr[c]:
            if not visited[nxt]:
                visited[nxt] = visited[c] + 1
                queue.append(nxt)

    # [1 sol]
    # mx = 1
    # mxs = []
    # for i in range(1, 101):
    #     if visited[i] > mx:
    #         mx = visited[i]
    #         mxs = [i]
    #     elif visited[i] == mx:
    #         mxs.append(i)
    #
    # ans = max(mxs)

    return ans


for test_case in range(1, T + 1):
    N, S = map(int, input().split())

    arr = [[] for _ in range(101)]

    tmp = list(map(int, input().split()))
    for i in range(0, len(tmp) - 1, 2):
        arr[tmp[i]].append(tmp[i + 1])  # 단방향 그래프

    print(f"#{test_case} {bfs(S)}")
