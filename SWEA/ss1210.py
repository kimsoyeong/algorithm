T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())

    num = 100

    data = []

    for i in range(num):
        data.append(list(map(int, input().strip().split())))\

    # 2의 위치
    ci = num - 1
    cj = data[ci].index(2)

    while ci > 0:
        data[ci][cj] = 0

        if cj > 0 and data[ci][cj - 1] == 1:
            cj -= 1
        elif cj < num - 1 and data[ci][cj + 1] == 1:
            cj += 1
        else:
            ci -= 1

    print(f"#{N}", cj)