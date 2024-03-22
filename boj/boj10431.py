P = int(input())

for _ in range(P):
    tmp = list(map(int, input().split()))

    T = tmp[0]
    heights = tmp[1:]

    step = 0

    for i in range(1, 20):
        for j in range(i):
            if heights[j] > heights[i]:
                step += 1

    print(T, step)
