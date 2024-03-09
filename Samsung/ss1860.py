T = int(input())

for test_case in range(1, T+1):
    N, M, K = map(int, input().strip().split())

    guests = sorted(list(map(int, input().strip().split())))

    if guests[0] == 0 or guests[0] < M:
        print(f"#{test_case}", "Impossible")
        continue

    possible = True
    b_num = 0
    gi = 0
    for b in range(M, guests[-1] + 1, 1):
        if b % M == 0:
            b_num += K

        if guests[gi] == b:
            if b_num > 0:
                b_num -= 1
                gi += 1
            else:
                possible = False
                break

    print(f"#{test_case}", "Possible" if possible else "Impossible")