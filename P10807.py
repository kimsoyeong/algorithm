N = int(input())
lst = list(map(int, input().split()))
v = int(input())

answer = 0
for l in lst:
    if l == v:
        answer += 1

print(answer)