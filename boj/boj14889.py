def dfs(n, steam, lteam):
    global ans

    # 가지치기
    if ans == 0:
        return

    # 가지치기
    # if len(steam) > M or len(lteam) > M:
    #     return

    # 정답처리
    if n == N:
        if len(steam) == len(lteam):
            # 시너지 계산
            ss = ls = 0
            for i in range(M):
                for j in range(M):
                    si, sj = steam[i], steam[j]
                    li, lj = lteam[i], lteam[j]
                    ss += S[si][sj]
                    ls += S[li][lj]
            ans = min(ans, abs(ss - ls))
        return

    dfs(n + 1, steam + [n], lteam)  # 스타트팀으로
    dfs(n + 1, steam, lteam + [n])  # 링크팀으로


N = int(input())
M = N // 2
S = [list(map(int, input().split())) for _ in range(N)]

ans = 100 * M * M
dfs(0, [], [])

print(ans)
