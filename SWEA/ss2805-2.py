T = int(input())

for test_case in range(1, T+1):
    N = int(input())

    arr = []
    for _ in range(N):
        arr.append([int(a) for a in input().strip()])

    ans = 0
    M = N // 2
    s = e = M  # start, end
    for i in range(N):
        for j in range(s, e+1):
            ans += arr[i][j]

        if i < M:
            s -= 1
            e += 1
        else:
            s += 1
            e -= 1

    print(f"#{test_case} {ans}")