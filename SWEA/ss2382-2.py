di, dj = [0, -1, 1, 0, 0], [0, 0, 0, -1, 1]
tbl = [0, 2, 1, 4, 3]  # 방향 전환용


T = int(input())

for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(K)]

    for _ in range(M):
        # [1] 1칸 이동처리, 경계면 //2, 방향반대
        for i in range(len(arr)):
            # [0]: i, [1]: j, [2]: n, [3]: dr
            arr[i][0] = arr[i][0] + di[arr[i][3]]
            arr[i][1] = arr[i][1] + dj[arr[i][3]]
            if arr[i][0] == 0 or arr[i][0] == N - 1 or arr[i][1] == 0 or arr[i][1] == N - 1:
                arr[i][2] //= 2
                arr[i][3] = tbl[arr[i][3]]

        # [2] 좌표기준([0][1]) 정렬, 서브 조건으로 개수([2]) 정렬 (내림차순)
        arr.sort(key=lambda x: (x[0], x[1], x[2]), reverse=True)

        # [3] 같은 좌표 합치기
        i = 1
        while i < len(arr):
            # 위와 비교
            if arr[i - 1][0:2] == arr[i][0:2]:  # i,j => [0],[1] 좌표 같으면
                arr[i - 1][2] += arr[i][2]  # (1) n([3]) 합치기
                arr.pop(i)  # (2) 나를 arr에서 pop
            else:
                i += 1

    ans = 0
    # 정답처리: n의 합
    for lst in arr:
        ans += lst[2]

    print(f"#{test_case} {ans}")

