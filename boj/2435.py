N, K = map(int, input().split())

temperature = [0] * N

ns = list(map(int, input().split()))
temperature[0] = ns[0]
for i in range(1, N):
    temperature[i] = ns[i] + temperature[i-1]

answer = -float('inf')
for i in range(K - 1, N):   
    if i - K >= 0:
        answer = max(answer, temperature[i] - temperature[i - K])
    else:
        answer = max(answer, temperature[i])

print(answer)