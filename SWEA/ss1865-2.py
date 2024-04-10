def dfs(n, bits):  # DFS with Memoization
    if n == N: return 1  # 종료 조건

    if mem[bits] == 0:  # 미방문 상태; 계산된 적 없음  -> 계산 & 저장
        mx = 0
        for j in range(N):
            if bits & (1 << j) == 0:
                mx = max(mx, dfs(n + 1, bits + (1 << j)) * P[n][j] / 100)  # 내 밑에서 계산된 최대값 * 내 확률
        mem[bits] = mx  # 최댓값 저장

    return mem[bits]  # 최댓값 반환


T = int(input())

for test_case in range(1, T + 1):
    N = int(input())

    P = [list(map(int, input().split())) for _ in range(N)]
    mem = [0] * (2 ** N)

    ans = dfs(0, 0) * 100  # 결과를 %로 변환하기 위헤 100 곱함
    print(f"#{test_case} {ans:.6f}")
