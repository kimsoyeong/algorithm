T = int(input())

for test_case in range(1, T + 1):
    tc_n = int(input())
    n_dict = {}

    for n in list(map(int, input().split())):
        if n not in n_dict.keys():
            n_dict[n] = 1
        else:
            n_dict[n] += 1

    st = sorted(n_dict.items(), key=lambda x: x[1], reverse=True)

    print(f"#{tc_n} {st[0][0]}")
