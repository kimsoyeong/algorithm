T = 2

def bfs(S):
    visited = [0] * 101
    visited[S] = 1
    queue = [S]

    while queue:
        c = queue.pop(0)

        for nxt in arr[c]:
            if not visited[nxt]:
                visited[nxt] = visited[c] + 1
                queue.append(nxt)

    mx = 1
    mxs = []
    for i in range(1, 101):
        if visited[i] > mx:
            mx = visited[i]
            mxs = [i]
        elif visited[i] == mx:
            mxs.append(i)

    return max(mxs)


for test_case in range(1, T + 1):
    N, S = map(int, input().split())

    arr = [[] for _ in range(101)]

    tmp = list(map(int, input().split()))
    for i in range(0, len(tmp) - 1, 2):
        arr[tmp[i]].append(tmp[i+1])  # 단방향 그래프

    print(f"#{test_case} {bfs(S)}")