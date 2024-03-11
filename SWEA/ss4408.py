T = int(input())

for test_case in range(1, T + 1):
    N = int(input())

    # 복도 배열
    aisle = [0] * 200

    for _ in range(N):
        S, E = map(int, input().split())
        if S > E:
            S, E = E, S  # sort

        # 복도 배열에 사용할 index
        si = (S - 1) // 2
        ei = (E - 1) // 2

        for i in range(si, ei + 1):
            aisle[i] += 1  # 빈도 체크

    print(f"#{test_case}", max(aisle))
