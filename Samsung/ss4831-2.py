T = int(input())

for test_case in range(1, T+1):
    K, N, M = map(int, input().strip().split())

    arr = [0] + list(map(int, input().strip().split())) + [N]

    start = 0
    ans = 0
    for i in range(len(arr)):
        if arr[i] - arr[i - 1] > K:  # 충전소가 멀어서 충전 불가
            ans = 0
            break
        if arr[i] - start > K:  # start에서 현재 i번째 충전소까지 이동이 불가능한 경우
            ans += 1
            start = arr[i-1]  # 이전 충전소에서 충전하게 한다.

    print(f"#{test_case} {ans}")

