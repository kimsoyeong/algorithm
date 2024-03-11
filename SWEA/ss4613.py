from collections import Counter
T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    arr = [[a for a in input()] for _ in range(N)]

    ans = N * M
    for i in range(N - 2):
        # i_range = (0, i + 1)
        cw = Counter([d for a in arr[0: i + 1] for d in a])
        w = M * (i + 1) - cw["W"]

        for j in range(i + 1, N - 1):
            # j_range = (i+1, j + 1)
            cb = Counter([d for a in arr[i + 1: j + 1] for d in a])
            b = M * (j - i) - cb["B"]
            # rest_range = (j + 1, N)
            cr = Counter([d for a in arr[j + 1: N] for d in a])
            r = M * (N - j - 1) - cr["R"]

            ans = min(ans, w + b + r)

    print(f"#{test_case} {ans}")
