def remove(lst, n):
    for l in lst:
        if n in l:
            l[l.index(n)] = 0
            break


def is_bingo(lst):
    cnt = 0  # 선 개수

    # 가로
    for l in lst:
        for e in l:
            if e != 0:
                break
        else:
            cnt += 1
    # 세로
    for j in range(5):
        tmp = [l[j] for l in lst]
        for t in tmp:
            if t != 0:
                break
        else:
            cnt += 1

    # 대각선 \
    tmp = []
    for idx in range(5):
        if lst[idx][idx] != 0:
            break
    else:
        cnt += 1

    # 대각선 /
    for idx in range(5):
        if lst[4 - idx][idx] != 0:
            break
    else:
        cnt += 1

    return True if cnt >= 3 else False


def run(lst):
    for i in range(5):
        call = list(map(int, input().split()))
        for j in range(5):
            remove(me, call[j])
            if (i * 5 + j) >= 4 and is_bingo(me):
                print(i * 5 + j + 1)
                return


me = [list(map(int, input().split())) for _ in range(5)]
run(me)