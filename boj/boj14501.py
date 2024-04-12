def dfs(i, time, sm):
    global ans
    if i == N + 1:  # 퇴사 날
        if time > 0:
            return
        ans = max(ans, sm)
        return

    if time <= 0:
        dfs(i + 1, T[i] - 1, sm + P[i])

    dfs(i + 1, time - 1, sm)


N = int(input())
T = [0] * (N + 1)
P = [0] * (N + 1)

for i in range(1, N + 1):
    T[i], P[i] = map(int, input().split())

ans = 0
dfs(1, 0, 0)

print(ans)