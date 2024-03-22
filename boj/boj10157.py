C, R = map(int, input().split())
K = int(input())

if K > C * R:
    print(0)
else:
    lst = [[0] * C for _ in range(R)]
    for i in range(R):
        lst[i][0] = i + 1

    i, j = R - 1, 0
    limit_i = R - 1
    limit_j = C - 1

    n = R + 1
    direction = 1
    while n <= K:

        for _ in range(2):
            cnt = limit_i if direction % 2 == 0 else limit_j
            for _ in range(cnt):
                if direction % 4 == 2:  # down
                    i -= 1
                elif direction % 4 == 1:  # right
                    j += 1
                elif direction % 4 == 3:  # left
                    j -= 1
                elif direction % 4 == 0:  # up
                    i += 1

                lst[i][j] = n
                n += 1

            direction += 1

        limit_i -= 1
        limit_j -= 1

    for i in range(R):
        if K in lst[i]:
            j = lst[i].index(K)
            break

    print(j + 1, i + 1)
