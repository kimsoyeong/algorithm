T = int(input())

for test_case in range(1, T + 1):
    day, mon, mon3, year = map(int, input().split())
    lst = [0] + list(map(int, input().split()))

    arr = [0] * 13
    for i in range(1, 13):
        # 가능한 4가지 방식
        mn = arr[i-1] + lst[i] * day  # 이전 달까지 비용 + 일일권 비용
        mn = min(mn, arr[i - 1] + mon)  # 월간권 비용 (비교)
        if i >= 3:
            mn = min(mn, arr[i - 3] + mon3)  # 분기권(3달) 비용 (비교)
        if i >= 12:
            mn = min(mn, arr[i - 12] + year) # 연간권 비용 (비교)

        arr[i] = mn  # i번째 달의 최소 비용

    print(f"#{test_case} {mn}")
