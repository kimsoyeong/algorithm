def dfs(n, tower_height, cnt):
    """
    :param n: H index
    :param tower_height: 현재까지 탑의 높이
    :param cnt: 탑을 이루는 점원의 수
    """
    global ans

    if n == N:
        if tower_height >= B:
            ans = min(ans, tower_height- B)
        return

    dfs(n + 1, tower_height + H[n], cnt + 1)
    dfs(n + 1, tower_height, cnt)


T = int(input())
for test_case in range(1, T + 1):
    N, B = map(int, input().split())

    H = list(map(int, input().split()))

    ans = 10000 * N
    dfs(0, 0, 0)

    print(f"#{test_case} {ans}")