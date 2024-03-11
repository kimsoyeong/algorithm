T = 10  # int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())

    data = []

    for i in range(100):
        data.append(list(map(int, input().strip().split())))

    answer = -1
    min_distance = 100 * 100
    for j in range(100):
        if data[99][j] == 0:
            continue

        ci = 99
        distance = dr = 0
        cj = j

        while ci > 0:
            distance += 1

            # 좌/우로 방향전환하면, 막다른 길이 나올때까지 그 방향으로 직진해야함. 다시 돌아가면 안 됨
            if dr == 0:  # 수직으로 이동중임
                ci -= 1
                # 다음에 좌/우 방향전환할 수 있을때, 그 다음 순환에서 방향전환되도록 dir을 설정해줌.
                if cj > 0 and data[ci][cj - 1] == 1:
                    dr = -1
                elif cj < 99 and data[ci][cj + 1] == 1:
                    dr = 1
            else:
                cj += dr
                if cj + dr > 99 or data[ci][cj + dr] == 0:  # 막다른 길에서, 수직으로 이동하도록
                    dr = 0

        if distance <= min_distance:
            answer = cj
            min_distance = distance

    print(f"#{N}", answer)