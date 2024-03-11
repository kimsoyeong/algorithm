N, M = map(int, input().split())

arr = list(map(int, input().split()))

max_sum = -1
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            tmp = arr[i] + arr[j] + arr[k]
            if max_sum < tmp <= M:
                max_sum = tmp

print(max_sum)