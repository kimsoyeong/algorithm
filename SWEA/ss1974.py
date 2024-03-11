T = int(input())

for test_case in range(1, T + 1):
    arr = []
    for _ in range(9):
        arr.append(list(map(int, input().split())))

    flag = True
    for i in range(0, 9, 3):
        j = i
        for d in range(3):
            if len(set(arr[i + d][0:9])) != 9:
                flag = False
                break
            if len(set([a[j + d] for a in arr[0:9]])) != 9:
                flag = False
                break

        if not flag: break
        if len(set([d for a in arr[i:i + 3] for d in a[j:j + 3]])) != 9:
            flag = False
            break
    if flag:
        print(f"#{test_case} 1")
    else:
        print(f"#{test_case} 0")
