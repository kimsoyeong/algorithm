P = int(input())

for _ in range(P):
    tmp = list(map(int, input().split()))

    T = tmp[0]
    heights = tmp[1:]

    step = 0

    N = len(heights)

    for i in range(1, N):
        curr = heights[i]

        cnt = 0
        for j in range(i - 1, -1, -1):
            if heights[j] > curr:
                cnt += 1

        step += cnt

    print(T, step)
