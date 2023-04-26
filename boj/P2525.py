H, M = map(int, input().split())
time = int(input())

M += time
if M >= 60:
    u = M / 60
    M %= 60
    H += u

H %= 24
print(int(H), M)
