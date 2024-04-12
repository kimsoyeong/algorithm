# 1. 백트래킹
def dfs(n, sm):
    global ans
    # [1] 종료 조건: 가능한 n을 종료에 관련된 것으로 정의!
    if n >= N + 1:
        ans = max(ans, sm)
        return

    # [2] 하부 호출: 화살표 개수만큼 호출
    if n + T[n] <= N + 1:  # 상담하는 경우 (퇴사일 전에 상담 완료 가능한 경우만)
        dfs(n + T[n], sm + P[n])
    dfs(n + 1, sm)  # 상담하지 않는 경우


N = int(input())
T = [0] * (N + 1)
P = [0] * (N + 1)
for i in range(1, N + 1):
    T[i], P[i] = map(int, input().split())

ans = 0
dfs(1, 0)
print(ans)

# 2. DP
