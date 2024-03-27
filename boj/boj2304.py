N = int(input())

lst = sorted([list(map(int, input().split())) for i in range(N)], key=lambda x: x[0])

# 최대 높이 인덱스 찾기
max_idx = 0
max_ = lst[0][1]
for l in range(1, N):
    if max_ < lst[l][1]:
        max_ = lst[l][1]
        max_idx = l

arr = [0] * N
arr[max_idx] = max_

# 0 ~ max_index
for i in range(max_idx):
    if arr[i] > 0:
        continue

    num = lst[i][1]
    for j in range(i + 1, max_idx + 1):
        if num < lst[j][1]:
            num = lst[j][1]
            break

    for k in range(i, j):
        arr[k] = lst[i][1]

# max_idx ~ N
for i in range(max_idx + 1, N):
    num = lst[i][1]
    for j in range(i - 1, max_idx - 1, -1):
        if num < lst[j][1]:
            num = lst[j][1]
            break
    for k in range(j + 1, i + 1):
        arr[k] = lst[i][1]

# 다각형 면적 계산
cnt = arr[max_idx]
for i in range(max_idx):
    cnt += arr[i] * (lst[i + 1][0] - lst[i][0])

for i in range(max_idx + 1, N):
    cnt += arr[i] * (lst[i][0] - lst[i - 1][0])


print(cnt)