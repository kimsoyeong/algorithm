H, W = map(int, input().split())

answer = [[-1]*W for _ in range(H)]
for i in range(H):
    clouds = input()
    for j in range(W):
        if clouds[j] == "c":
            answer[i][j] += 1  # 0

            cnt = 1
            for d in range(j + 1, W):
                if clouds[d] != "c":
                    answer[i][d] += cnt + 1
                    cnt += 1
                else:
                    break

for ans in answer:
    print(*ans)