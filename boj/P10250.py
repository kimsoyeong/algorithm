T = int(input())

for i in range(T):
    H, W, N = map(int, input().split())

    Y = N % H # 층수
    X = (N // H + 1) # 호

    if Y == 0:
        Y = H
        X -= 1
    print(Y * 100 + X)