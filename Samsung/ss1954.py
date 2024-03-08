T = int(input())

for test_case in range(1, T + 1):
    N = int(input())

    arr = [[0] * N for _ in range(N)]
    arr[0][0] = 1  # first element

    # direction
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    dr = 0

    i = 0
    j = 0
    cnt = 2
    while cnt <= N * N:
        # next indices
        ni = i + di[dr]
        nj = j + dj[dr]

        if (0 <= ni < N) and (0 <= nj < N) \
                and (arr[ni][nj] == 0):
            i, j = ni, nj
            arr[i][j] = cnt
            cnt += 1
        else:  # change direction
            dr = (dr + 1) % 4

    print(f"#{test_case}")

    for a in arr:
        for c in a:
            print(c, end=" ")
        print()
