def dfs(n, cnt, battery):
    global ans

    # 가지치기
    if cnt >= ans:
        return

    if n == N:
        ans = min(ans, cnt)
        return

    dfs(n + 1, cnt + 1, M[n] - 1)
    if battery > 0:
        dfs(n + 1, cnt, battery - 1)


T = int(input())

for test_case in range(1, T + 1):
    ip = list(map(int, input().split()))

    N = ip[0]
    M = [0] + ip[1:]

    ans = 100 * N
    dfs(2, 0, M[1] - 1)

    print(f"#{test_case} {ans}")
