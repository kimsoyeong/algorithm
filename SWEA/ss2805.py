T = int(input())

for test_case in range(1, T+1):
    N = int(input())

    arr = []
    for _ in range(N):
        arr.append([int(a) for a in input().strip()])

    s = 0
    d = N // 2
    for i in range(d + 1):
        s += sum(arr[i][d - i: d + i + 1])
    for i in range(d + 1, N):
        s += sum(arr[i][i - d: N - i + d])

    print(f"#{test_case} {s}")