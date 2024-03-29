T = int(input())


def bfs(s, e):
    v = [0] * (N + 1)
    q = [s]

    while q:
        c = q.pop(0)

        # 정답 처리!
        if c == e:
            return v[c]

        for ne, nw in lst[c]:
            if 0 <= ne <= N:
                if v[ne] == 0 or v[ne] > v[c] + nw:
                    v[ne] = v[c] + nw
                    q.append(ne)

    return -1


for test_case in range(1, T + 1):
    N, E = map(int, input().split())  # 마지막 연결지점 번호, 도로 개수

    lst = [[] for _ in range(N + 1)]
    for _ in range(E):
        s, e, w = map(int, input().split())  # 구간: 시작, 끝, 거리
        lst[s].append((e, w))

    print(f"#{test_case} {bfs(0, N)}")