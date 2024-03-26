K, S, N = input().split()  # 킹 위치, 돌 위치, 움직이는 횟수
N = int(N)


def toPos(st):
    return int(st[1]), ord(st[0]) - 65 + 1


def toAB(i, j):
    return f"{chr(j + 64)}{i}"


ki, kj = toPos(K)
si, sj = toPos(S)

dct = {'R': (0, 1), 'L': (0, -1), 'B': (-1, 0), 'T': (1, 0),
       'RT': (1, 1), 'LT': (1, -1), 'RB': (-1, 1), 'LB': (-1, -1)}
for _ in range(N):
    di, dj = dct[input()]
    ni, nj = ki + di, kj + dj

    if 1 <= ni <= 8 and 1 <= nj <= 8:  # 범위 내
        if (ni, nj) == (si, sj):  # 이동할 위치에 돌이 있는 경우
            ei, ej = si + di, sj + dj  # 돌이 이동할 위치
            if 1 <= ei <= 8 and 1 <= ej <= 8:  # 돌 이동 가능 여부
                si, sj = ei, ej  # 돌 이동
                ki, kj = ni, nj  # 킹 이동
        else:
            ki, kj = ni, nj  # 킹 이동

print(toAB(ki, kj), toAB(si, sj), sep='\n')
