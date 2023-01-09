N, M = map(int, input().split())
# row, col

A = []

for i in range(N):
    A.append(list(map(int, input().split())))
for i in range(N):
    for idx, j in enumerate(map(int, input().split())):
        A[i][idx] += j

for ai in A:
    print(" ".join(map(str, ai)))

