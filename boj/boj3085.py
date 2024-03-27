N = int(input())

arr = [list(input()) for _ in range(N)]


def count():
    ans = cnt = 1
    for i in range(N):
        cnt = 1

        # 세로 방향 검사
        for j in range(1, N):
            if arr[j][i] == arr[j - 1][i]:
                cnt += 1
                ans = max(cnt, ans)
            else:
                cnt = 1

        # 가로 방향 검사
        cnt = 1
        for j in range(1, N):
            if arr[i][j] == arr[i][j - 1]:
                cnt += 1
                ans = max(cnt, ans)
            else:
                cnt = 1

    return ans


mx = 1
for i in range(N):  # 마지막 행은 왜 검사를 안 하지? 오른쪽 검사 해야 하지 않나?
    for j in range(N):  # 마지막 열도 아래쪽 검사 해야함
        curr = arr[i][j]

        # 오른쪽 교환
        if j + 1 < N and arr[i][j] != arr[i][j + 1]:
            # swap
            arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]
            # 가장 긴 연속 찾기
            mx = max(mx, count())
            # 다시 swap
            arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]

        # 아래쪽 교환
        if i + 1 < N and arr[i][j] != arr[i + 1][j]:
            # swap
            arr[i][j], arr[i + 1][j] = arr[i + 1][j], arr[i][j]
            # 가장 긴 연속 찾기
            mx = max(mx, count())
            # 다시 swap
            arr[i][j], arr[i + 1][j] = arr[i + 1][j], arr[i][j]

print(mx)
