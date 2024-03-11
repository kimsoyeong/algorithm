T = int(input())

for test_case in range(1, T+1):
    N = int(input())

    arr = []
    for _ in range(N):
        arr.append(list(input().split()))

    ans = [[] for _ in range(N)]
    idx = 0
    for j in range(N):
        row = ''
        for i in range(N-1, -1, -1):
            row += arr[i][j]
        ans[idx].append(row)
        idx += 1

    idx = 0
    for i in range(N-1, -1, -1):
        row = ''
        for j in range(N-1, -1, -1):
            row += arr[i][j]
        ans[idx].append(row)
        idx += 1

    idx = 0
    for j in range(N-1, -1, -1):
        row = ''
        for i in range(N):
            row += arr[i][j]
        ans[idx].append(row)
        idx += 1

    print(f"#{test_case}")
    for a in ans:
        print(*a)