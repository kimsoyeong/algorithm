N, K = map(int, input().split())

q = [x for x in range(1, N + 1)]
print("<", end="")

idx = 0
while q:
    idx = (idx + (K - 1)) % len(q)

    print(q[idx], end="")
    if len(q) > 1:
        print(', ', end="")
    del q[idx]

print(">")
