def bfs(start):
    queue = [start]
    visited = [0] * (N + 1)
    visited[start] = 1

    while queue:
        c = queue.pop(0)  # 현재 방문 노드
        print(c, end=" ")

        for n in graph[c]:
            if visited[n] == 0: # 미방문 노드
                queue.append(n)
                visited[n] = 1 # or 거리 (visited[c] + 1)

    return # 탐색 종료


def dfs(start, visited):

    c = start
    visited += [c]
    print(c, end=" ")

    for n in graph[c]:
        if n not in visited:
            dfs(n, visited)

    return


# Main
N, M, V = map(int, input().strip().split())

# Build graph
graph = [[] for _ in range(N + 1)]
for i in range(M):
    s, e = map(int, input().strip().split())

    # Bi-directional edge
    graph[s] += [e]
    graph[e] += [s]

graph = [sorted(nodes) for nodes in graph]

# Run search
dfs(V, [V])
print()

bfs(V)
