T = int(input())

for test_case in range(1, T+1):
    N = int(input().strip())

    lst = [[0] * (i+1) for i in range(N)]

    print(f"#{test_case}")
    for i in range(N):
        for j in range(i + 1):
            if j == 0 or i == j:
                lst[i][j] = 1
            else:
                lst[i][j] = lst[i-1][j-1] + lst[i-1][j]

            print(lst[i][j], end=" ")
        print()
