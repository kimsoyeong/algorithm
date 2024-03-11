T = int(input())

for test_case in range(1, T + 1):
    N = int(input())

    arr = []
    for _ in range(N):
        arr.append([s for s in input().strip()])

    print(f"#{test_case}", end=" ")
    flag = False
    for i in range(0, N):
        for j in range(0, N):

            if arr[i][j] == 'o':
                if j+4 < N and '.' not in arr[i][j: j+5]:
                    print("YES")
                    flag = True
                    break
                if i+4 < N and '.' not in [a[j] for a in arr[i: i+5]]:
                    print("YES")
                    flag = True
                    break
                if i + 4 < N and j + 4 < N and '.' not in [arr[i+d][j+d] for d in range(5)]:
                    print("YES")
                    flag = True
                    break
                if i+4 < N and j-4 >= 0 and '.' not in [arr[i+d][j-d] for d in range(5)]:
                    print("YES")
                    flag = True
                    break
        if flag:
            break
    else:
        print("NO")
