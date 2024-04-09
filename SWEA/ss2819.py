def dfs(i, j, num7, cnt):
    if cnt == 6:
        if num7 not in ans:
            ans.append(num7)
        return

    for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        ni, nj = di + i, dj + j
        if 0 <= ni < 4 and 0 <= nj < 4:
            dfs(ni, nj, num7 + lst[ni][nj], cnt + 1)


T = int(input())

for test_case in range(1, T + 1):
    lst = [list(input().split()) for _ in range(4)]

    ans = []
    for i in range(4):
        for j in range(4):
            dfs(i, j, lst[i][j], 0)

    print(f"#{test_case} {len(ans)}")
