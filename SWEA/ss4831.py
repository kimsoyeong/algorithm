T = int(input())

for test_case in range(1, T+1):
    K, N, M = map(int, input().strip().split())

    bus_stops = [0] * (N + 1)
    bus_stops[0] = 1
    for i in map(int, input().strip().split()):
        bus_stops[i] += 1

    i = 0
    n_charge = 0

    flag = True
    while i + K + 1 <= N and flag:
        sub_stops = bus_stops[i: i + K + 1]

        charge = i
        # print(K, len(sub_stops), sub_stops)
        for si in range(1, len(sub_stops)):
            if sub_stops[si] != 0:
                charge = i + si

        if i != charge:
            i = charge
            # print(charge)
            n_charge += 1
        else:
            flag = False

    if flag:
        print(f"#{test_case}", n_charge)
    else:
        print(f"#{test_case} 0")
