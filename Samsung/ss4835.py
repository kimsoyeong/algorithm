T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int, input().strip().split())

    nums = list(map(int, input().strip().split()))

    max_sum = sum(nums[0: M])
    min_sum = sum(nums[0: M])
    for i in range(1, N - (M - 1)):
        max_sum = max(max_sum, sum(nums[i: i + M]))
        min_sum = min(min_sum, sum(nums[i: i + M]))

    print(f"#{test_case} {max_sum - min_sum}")
