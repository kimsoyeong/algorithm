def dfs(n, sm):
    global mx, mn
    if n == N:
        mx = max(mx, sm)
        mn = min(mn, sm)
        return

    for o in range(4):
        if op[o] > 0:
            if o == 0:
                tmp = sm + lst[n]
            elif o == 1:
                tmp = sm - lst[n]
            elif o == 2:
                tmp = sm * lst[n]
            elif o == 3:
                tmp = int(sm / lst[n])

            op[o] -= 1
            dfs(n + 1, tmp)
            op[o] += 1


T = int(input())

for test_case in range(1, T + 1):
    N = int(input())

    op = list(map(int, input().split()))
    lst = list(map(int, input().split()))

    mx = -100000000
    mn = 100000000
    dfs(1, lst[0])

    print(f"#{test_case} {mx - mn}")
