T = int(input())

for test_case in range(1, T + 1):
    N = int(input())

    x = -1
    y = 0

    curr = 1
    cords = [[0] * N for _ in range(N)]
    for _ in range(N):
        x += 1
        cords[y][x] = curr
        # print(f"{curr}: [{y}][{x}]")
        curr += 1

    direction = 0
    cnt = N - 1
    while cnt > 0:
        for _ in range(2):
            for _ in range(cnt):
                if direction % 4 == 0:
                    y += 1
                elif direction % 4 == 1:
                    x -= 1
                elif direction % 4 == 2:
                    y -= 1
                else:  # 3
                    x += 1

                cords[y][x] = curr
                # print(f"{curr} - {direction % 4}: [{y}][{x}]")
                curr += 1
            direction += 1
        cnt -= 1

    print(f"#{test_case}")
    for cord in cords:
        for c in cord:
            print(c, end=" ")
        print()
