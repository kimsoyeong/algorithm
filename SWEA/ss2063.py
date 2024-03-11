N = int(input())
scores = sorted(list(map(int, input().split())))
print(scores[len(scores)//2])