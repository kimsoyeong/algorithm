T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    price = list(map(int, input().split()))

    # pocket = 0
    money = 0

    max_price = price[-1]
    for i in range(N-2, -1, -1):
        if max_price > price[i]:
            money += max_price - price[i]  # 사고 팔고
        else:
            max_price = price[i]  # 새로운 매매가

    # for i in range(N):
    #     if (i < len(price) - 1) and \
    #             (max(price[i:]) > price[i]):  생
    # max함수 사용 시, 7개 test case만 통과하고 Runtime error 발생
    # 아마도, memory 초과 또는 실행시간 초과
    #         # buy one
    #         money -= price[i]
    #         pocket += 1
    #     else:
    #         # sell all in pocket
    #         money += price[i] * pocket
    #         pocket = 0

    print(f"#{test_case} {money}")
