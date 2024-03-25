H, W = map(int, input().split())

answer = [[0] * W for _ in range(H)]
clouds = [input() for _ in range(H)]

for i in range(H):
    cnt = -1  # 'c' 만나지 못하면 계속 -1로 기록됨
    for j in range(W):
        if clouds[i][j] == 'c':  # 구름을 만나면 0으로 초기화
            cnt = 0
        else:  # .을 만나면,
            if cnt >= 0:  # 이전에 구름이 있었다면, 1 증가
                cnt += 1
            answer[i][j] = cnt  # 증가한 값(구름) 또는 -1(구름X)가 기록됨

for ans in answer:
    print(*ans)
