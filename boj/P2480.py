A, B, C = map(int, input().split())

# 같은 눈 3개: 10000 + (같은 눈) * 1000
# 같은 눈 2개: 1000 + (같은 눈) * 100
# 모두 다른 눈: (가장 큰 눈) * 100

if A == B == C:
    print(10000 + A * 1000)
elif A == B or A == C:
    print(1000 + A * 100)
elif B == C:
    print(1000 + B * 100)
else:
    print(max(max(A, B), C) * 100)
