
answer = -1

lst = [0] * 10

for _ in range(10):
    tmp = int(input())
    lst[_] = tmp + (lst[_ - 1] if _ > 0 else 0)

    if abs(100 - lst[_]) <= abs(100 - answer):
        answer = lst[_]

    if answer >= 100:
        break

print(answer)