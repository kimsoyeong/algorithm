def dfs(n, sm):
    global ans

    # 가지치기
    if sm >= ans:
        return

    # 종료 조건
    if n > 12:
        # 정답 처리
        ans = min(ans, sm)
        return

    for p, d in zip([day, mon, mon3, year], [1, 1, 3, 12]):
        new_ = 0
        if p == day:
            new_ = p * lst[n]
        else:
            new_ = p

        dfs(n + d, sm + new_)


T = int(input())

for test_case in range(1, T + 1):
    day, mon, mon3, year = map(int, input().split())
    lst = [0] + list(map(int, input().split()))

    ans = 3000 * 12
    dfs(1, 0)  # 1월부터 시작
    print(f"#{test_case} {ans}")
