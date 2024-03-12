N = int(input())

arr = [[0] * 102 for _ in range(102)]

for _ in range(N):
    A, B = map(int, input().split())

    for i in range(B, B + 10):
        for j in range(A, A + 10):
            arr[i+1][j+1] = 1

# 상, 하, 좌, 우
dys = [1, -1, 0, 0]
dxs = [0, 0, -1, 1]

dulae = 0
for i in range(1, 101):
    for j in range(1, 101):
        if arr[i][j] == 1:
            for dy, dx in zip(dys, dxs):
                if arr[i + dy][j + dx] == 0:
                    dulae += 1

print(dulae)
