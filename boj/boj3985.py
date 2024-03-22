from collections import Counter

L = int(input())  # cake 길이
N = int(input())  # 방청객 수

cakes = [0] * (L + 1)
pred_cnt = -1
pred_i = 0

max_cnt = -1
max_i = 0
for i in range(N):
    P, K = map(int, input().split())

    if K - P + 1 > pred_cnt:
        pred_i = i + 1
        pred_cnt = K - P + 1

    cnt = 0
    for j in range(P, K + 1):
        if cakes[j] == 0:
            cakes[j] = i + 1
            cnt += 1
    if cnt > max_cnt:
        max_cnt = cnt
        max_i = i + 1

print(pred_i)
print(max_i)