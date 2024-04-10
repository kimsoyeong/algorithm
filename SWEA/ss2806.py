def dfs(n):
    """
    :param n: 행 index
    """
    global ans

    if n == N:
        ans += 1
        return

    for j in range(N):
        # 열, 대각선 검사
        if vcol[j] == 0:
            if v2[n + j] == 0 and v3[n - j + N] == 0:
                vcol[j] = 1
                v2[n + j] = 1
                v3[n - j + N] = 1
                # v3[n - j] = 1  # 어차피 음수 index가 없기때문에, 이렇게도 가능
                dfs(n + 1)  # 다음 행 진행
                vcol[j] = 0
                v3[n - j + N] = 0
                # v2[n + j] = 0
                v3[n - j] = 0


T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    vcol = [0] * N
    v2 = [0] * (N * 2)  # 오른쪽 위로 향하는 대각선
    v3 = [0] * (N * 2)  # 왼쪽 위로 향하는 대각선

    ans = 0
    dfs(0)

    print(f"#{test_case} {ans}")
