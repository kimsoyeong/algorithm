T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int, input().strip().split())

    nums = list(map(int, input().strip().split()))

    sub_sum = max_sum = min_sum = sum(nums[0: M])
    for i in range(M, N):
        sub_sum = sub_sum + nums[i] - nums[i - M]
        max_sum = max(max_sum, sub_sum)
        min_sum = min(min_sum, sub_sum)

    print(f"#{test_case} {max_sum - min_sum}")
