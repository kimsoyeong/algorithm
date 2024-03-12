N = int(input())

arr = [[0] * 1001 for _ in range(1001)]

# [3] 입력 속도 개선
for n in range(1, N + 1):
    sj, si, w, h = map(int, input().split())

    for i in range(si, si + h):
        arr[i][sj: sj + w] = [n] * w  # 좌항이 list이므로 우항도 list로 줘야 한다!

# [1], [2]의 입력 부분
# for n in range(1, N + 1):
#     sj, si, w, h = map(int, input().split())
#
#     for i in range(si, si + h):
#         for j in range(sj, sj + w):
#             arr[i][j] = n

# [1]: 색종이 개수별로 전체 arr 순회 -> 부분 정답: 시간 초과
#      (배열이 크기때문에 N * 1001 * 1001번 순회하면 오래걸림)
# for n in range(1, N + 1):
#     cnt = 0
#     for lst in arr:
#         cnt += lst.count(n)
#     print(cnt)

# [2]: 빈도수 체크 (1001 * 1001번만 순회) -> 부분 정답: 시간 초과
cnt = [0] * (N + 1)
for row in arr:
    for c in row:
        cnt[c] += 1

print(*cnt[1:], sep='\n')
