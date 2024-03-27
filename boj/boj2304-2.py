N = int(input())  # 기둥의 개수

lst = [0] * 1001
mx_i = mx = 0
for _ in range(N):
    L, H = map(int, input().split())
    # L위치에 H 기록
    lst[L] = H

    # [1] mx_i 구하기
    if mx < H:  # 더 높은 경우
        mx_i, mx = L, H

# [2] 왼쪽부터 처리 (mx_i 포함)
ans = mx = 0
for i in range(mx_i + 1):
    mx = max(mx, lst[i])
    ans += mx

# [3] 오른쪽부터 처리
mx = 0
for i in range(1000, mx_i, -1):
    mx = max(mx, lst[i])
    ans += mx

print(ans)