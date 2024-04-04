def dfs(n, cnt, battery):
    global ans

    # 가지치기
    if cnt >= ans:
        return

    if n == N:
        ans = min(ans, cnt)
        return

    # 가지치기를 고려하는 경우: 좋은(유망한) 답이 먼저 나오는 방향으로 호출
    # 최소 값을 찾아야하므로, 최대한 교체하지 않는 것이 유망한 답!
    if battery > 0:
        dfs(n + 1, cnt, battery - 1)  # 교체 X
    dfs(n + 1, cnt + 1, M[n] - 1)  # 교체 O


T = int(input())

for test_case in range(1, T + 1):
    ip = list(map(int, input().split()))

    N = ip[0]
    M = [0] + ip[1:]

    ans = 100 * N
    dfs(2, 0, M[1] - 1)

    print(f"#{test_case} {ans}")
