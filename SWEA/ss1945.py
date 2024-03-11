T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())

    up = [0] * 5
    for i, div in enumerate([2, 3, 5, 7, 11]):
        while N % div == 0:
            up[i] += 1
            N //= div
    # a, b, c, d, e = 0, 0, 0, 0, 0
    # while N % 2 == 0:
    #     a += 1
    #     N //= 2
    #
    # while N % 3 == 0:
    #     b += 1
    #     N //= 3
    #
    # while N % 5 == 0:
    #     c += 1
    #     N //= 5
    #
    # while N % 7 == 0:
    #     d += 1
    #     N //= 7
    #
    # while N % 11 == 0:
    #     e += 1
    #     N //= 11

    # print(f"#{test_case} {up[0]} {up[1]} {up[2]} {up[3]} {up[4]}")
    print(f"#{test_case}", *up)