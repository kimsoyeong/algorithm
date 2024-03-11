T = 10  # int(input())

for test_case in range(1, T + 1):
    N = int(input())

    arr = []
    for _ in range(100):
        arr.append(list(map(int, input().strip().split())))

    row_max = 0
    col_max = 0
    d1_sum = 0
    d2_sum = 0

    for i in range(100):
        row_max = max(row_max, sum(arr[i]))
        col_max = max(col_max, sum([col[i] for col in arr]))
        d1_sum += arr[i][i]
        d2_sum += arr[i][99 - i]

    print(f"#{N}", max(row_max, col_max, d1_sum, d2_sum))
