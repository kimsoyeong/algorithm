N = int(input())


def count(lst):
    cnt = ans = 1  # 연속적으로 같은 색의 사탕 수
    for i in range(1, len(lst)):
        if lst[i] == lst[i-1]: # 이전과 같은 지 확인
            cnt += 1  # 같으면 +1
            ans = max(ans, cnt)  # 가장 긴 연속 사탕 수 갱신
        else:  # 다르면, 0
            cnt = 1

    return ans


def solve(arr):
    # 행 방향으로만 확인하는 함수
    mx = 0

    for i in range(N - 1):  # 현재 행, 다음 행 검사하니까, 마지막행은 순회 안해도 됨
        for j in range(N):  # 마지막열도 아래쪽 검사해야 함
            # 오른쪽 교환
            if j + 1 < N:
                arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]
                mx = max(mx, count(arr[i]))
                arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]  # 원래대로

            # 아래쪽 교환:
            if i + 1 < N:
                arr[i][j], arr[i + 1][j] = arr[i + 1][j], arr[i][j]
                mx = max(mx, count(arr[i]))
                mx = max(mx, count(arr[i + 1]))
                arr[i][j], arr[i + 1][j] = arr[i + 1][j], arr[i][j]  # 원래대로

    return mx


arr = [list(input()) for _ in range(N)]
arr_t = list(map(list, zip(*arr)))  # transpose
ans = max(solve(arr), solve(arr_t))

print(ans)