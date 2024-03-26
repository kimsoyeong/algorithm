king, stone, N = input().split()  # 킹 위치, 돌 위치, 움직이는 횟수
N = int(N)

king_i = int(king[1]) - 1
king_j = ord(king[0]) - 65

stone_i = int(stone[1]) - 1
stone_j = ord(stone[0]) - 65

for i in range(N):
    move = input()

    x, y = 0, 0
    if move == "R":
        x += 1
    elif move == "L":
        x -= 1
    elif move == "T":
        y += 1
    elif move == "B":
        y -= 1
    elif move == "RT":
        x += 1
        y += 1
    elif move == "LT":
        x -= 1
        y += 1
    elif move == "RB":
        x += 1
        y -= 1
    elif move == "LB":
        x -= 1
        y -= 1

    tmp_x, tmp_y = king_j + x, king_i + y
    if 0 <= tmp_y < 8 and 0 <= tmp_x < 8:  # 체스판 내
        if tmp_y == stone_i and tmp_x == stone_j:  # 돌과 겹칠 때
            if 0 <= stone_i + y < 8 and 0 <= stone_j + x < 8:
                stone_i += y
                stone_j += x
            else:
                continue
        king_i = tmp_y
        king_j = tmp_x

print(f"{chr(king_j + 65)}{king_i + 1}")
print(f"{chr(stone_j + 65)}{stone_i + 1}")
