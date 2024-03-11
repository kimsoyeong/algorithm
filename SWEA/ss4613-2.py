T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]  # diff: 그냥 string으로 풀이 진행

    mx = 0
    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            cnt = 0
            # diff: list slicing없이 for문으로 순회
            for s in range(i + 1):
                cnt += arr[s].count('W')  # diff: Counter 대신 list자체의 count 함수를 사용
            for s in range(i + 1, j + 1):
                cnt += arr[s].count('B')
            for s in range(j + 1, N):
                cnt += arr[s].count('R')
            mx = max(mx, cnt)

    print(f"#{test_case} {N * M - mx}")