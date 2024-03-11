T = 10  # int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())  # 건물의 수
    # 각 건물의 높이
    buildings = list(map(int, input().strip().split()))

    answer = 0
    for i in range(2, len(buildings) - 2):
        bd = buildings[i]

        tmp = -1
        if buildings[i - 1] < bd and buildings[i - 2] < bd \
                and buildings[i + 1] < bd and buildings[i + 2] < bd:  # 조망권 확보 확인
            tmp = max(buildings[i - 1], buildings[i - 2], buildings[i + 1], buildings[i + 2])
        if tmp != -1 and tmp < bd:
            answer += bd - tmp

    print(f"#{test_case} {answer}")

# 문제의 예제
# 14
# 0 0 3 5 2 4 9 0 6 4 0 6 0 0
