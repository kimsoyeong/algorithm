N, L = map(int, input().split())  # 신호등 개수, 도로 길이

lst = []
for _ in range(N):
    D, R, G = map(int, input().split())  # 신호등 위치, 빨간색, 초록색 지속 시간
    lst.append([D, R, G])

wait_time = 0
i = 0
for i in range(N):
    D, R, G = lst[i]

    # 빨간불에 걸리는 지 확인 (%)
    cnt = D + wait_time
    cnt %= (R + G)
    if cnt < R:  # 빨간 불에 걸린다면
        # wait
        wait_time += R - cnt  # 대기시간 추가

print(L + wait_time)  # 이동시간 + 대기시간