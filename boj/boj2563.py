N = int(input())

arr = [[0] * 100 for _ in range(100)]

for _ in range(N):
    A, B = map(int, input().split())

    for i in range(B, B + 10):
        for j in range(A, A + 10):
            arr[i][j] = 1

    sum_blk = 0
    for row in arr:
        sum_blk += row.count(1)

print(sum_blk)