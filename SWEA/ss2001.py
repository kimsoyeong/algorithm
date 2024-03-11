T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    cords = []
    for _ in range(N):
        cords.append(list(map(int, input().split())))

    max_sum = 0
    for i in range(N - (M - 1)):
        for j in range(N - (M - 1)):
            print(f"cords[{i}:{i+M}][{j}:{j+M}]")
            s = sum([sum(x[j:j+M]) for x in cords[i:i+M]])
            if s > max_sum:
                max_sum = s

    print(f"#{test_case} {max_sum}")
