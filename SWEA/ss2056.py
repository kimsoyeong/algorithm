T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    date = input()
    year = int(date[:4])
    month = int(date[4:6])
    day = int(date[6:])

    if ((month in [1, 3, 5, 7, 8, 10, 12] and 0 < day < 32)
            or (month in [4, 6, 9, 11] and 0 < day < 31)
            or (month == 2 and 0 < day < 29)):
        print(f"#{test_case}", end=" ")
        print("{:04d}/{:02d}/{:02d}".format(year, month, day, day))
    else:
        print(f"#{test_case} -1")
