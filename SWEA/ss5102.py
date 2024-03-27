T = int(input())


def bfs(S, E):
    queue = [S]
    visited = [0] * (V + 1)
    visited[S] = 1  # 방문 표시: 거리

    while queue:
        c = queue.pop(0)

        # 이 부분에서 정답 처리!
        if c == E:
            return visited[E] - 1  # 첫번째 노드에서 이미 거리를 1로 줬기 때문에 - 1 값 반환

        for nxt in lst[c]:  # 연결된 노드
            if not visited[nxt]:  # 미방문
                queue.append(nxt)
                visited[nxt] = visited[c] + 1  # 지나온 거리를 넣어줌

    return 0  # 못 찾은 경우


for test_case in range(1, T + 1):
    V, E = map(int, input().split())

    lst = [[] for _ in range(V + 1)]

    for i in range(E):
        v1, v2 = map(int, input().split())  # 간선 정보: v1 -> v2 & v2 -> v1
        lst[v1].append(v2)
        lst[v2].append(v1)

    S, G = map(int, input().split())
    ans = bfs(S, G)

    print(f"#{test_case} {ans}")