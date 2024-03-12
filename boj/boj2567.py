N = int(input())

arr = [[0] * 102 for _ in range(102)]

for _ in range(N):
    A, B = map(int, input().split())

    for i in range(B, B + 10):
        for j in range(A, A + 10):
            arr[i + 1][j + 1] = 1

dulae = 0

# 행 방향 순회
for i in range(1, 101):
    for j in range(1, 102):
        # (j) 왼쪽 값(j - 1)과 비교하므로, 100번째 입력의 오른쪽 가장자리를 확인하려면 101번 index까지 확인해야 한다.
        if arr[i][j] != arr[i][j - 1]:
            dulae += 1

# 3rd solution: Transpose 후 행 방향 순회
arr = list(zip(*arr))  # 전치행렬: 수정 필요시 list(map(list, zip(*arr)))
for i in range(1, 101):
    for j in range(1, 102):
        if arr[i][j] != arr[i][j - 1]:
            dulae += 1

# 2nd solution: 열 방향 순회
# for j in range(1, 101):
#     for i in range(1, 102):
#         # (i) 위쪽 값(i - 1)과 비교하므로, 100번째 입력의 위쪽 가장자리를 확인하려면 101번 index까지 확인해야 한다.
#         if arr[i][j] != arr[i - 1][j]:
#             dulae += 1

# 1st solution: 전체 순회
# # 상, 하, 좌, 우
# dys = [1, -1, 0, 0]
# dxs = [0, 0, -1, 1]
#
# for i in range(1, 101):
#     for j in range(1, 101):
#         if arr[i][j] == 1:
#             for dy, dx in zip(dys, dxs):
#                 if arr[i + dy][j + dx] == 0:
#                     dulae += 1

print(dulae)
