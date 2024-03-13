n = int(input())

sum = n
for i in range(2, n):
    sub = n // i + 1 - i

    if sub < 1:
        break
    sum += sub
print(sum)