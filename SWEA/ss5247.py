T = int(input())

# [3] lib 사용할 수 없는 경우, "큐"를 직접 만든다.
# 선형 큐: q = [0] * 1000000
# index: wr = rd = 0
# enq: q[wr] = d (큐에 넣을 숫자), wr += 1
# deq: d = q[rd], rd += 1


# [2] 제공 lib 사용 -> 더 빠를 수 있음
# list가 deque보다 느림
from collections import deque


def bfs(S, E):
    v = [0] * 1000001
    v[S] = 1

    q = deque()
    q.append(S)

    while q:
        c = q.popleft()

        # 정답 처리
        if c == E:
            return v[c] - 1

        for t in ((c + 1), (c - 1), (c * 2), (c - 10)):
            if (0 < t < 1000001) and v[t] == 0:
                q.append(t)
                v[t] = v[c] + 1

    # 만들 수 없는 숫자 (이 경우는 불가능하지만. 일단 처리)
    return -1


for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    ans = bfs(N, M)

    print(f"#{test_case} {ans}")

# [1] 7/10 시간 초과 발생
# def bfs(S, E):
#     v = [0] * 1000001
#     q = [S]
#     v[S] = 1
#
#     while q:
#         c = q.pop(0)
#
#         # 정답 처리
#         if c == E:
#             return v[c] - 1
#
#         for t in ((c + 1), (c - 1), (c * 2), (c - 10)):
#             if (0 < t < 1000001) and v[t] == 0:
#                 q.append(t)
#                 v[t] = v[c] + 1
#
#     # 만들 수 없는 숫자 (이 경우는 불가능하지만. 일단 처리)
#     return -1
#
#
# for test_case in range(1, T + 1):
#     N, M = map(int, input().split())
#
#     ans = bfs(N, M)
#
#     print(f"#{test_case} {ans}")
