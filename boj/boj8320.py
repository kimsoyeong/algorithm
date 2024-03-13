n = int(input())

sum = n
for i in range(2, n):
    sub = 0
    for j in range(i, n // i + 1):
        sub += 1
    if sub == 0:
        break
    sum += sub
print(sum)