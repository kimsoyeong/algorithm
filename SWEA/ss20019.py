T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    st = input()

    N = len(st)
    for i in range(N // 2):
        j = N - i - 1

        if st[i] != st[j]:
            print(f"#{test_case} NO")
            break
    else:
        t1 = st[:N//2]
        t2 = st[N//2 + 1 if N % 2 == 1 else N // 2:]
        for i in range(len(t1)):
            j = len(t1) - i - 1

            if st[i] != st[j]:
                print(f"#{test_case} NO")
                break
        else:
            for i in range(len(t2)):
                j = len(t2) - i - 1

                if st[i] != st[j]:
                    print(f"#{test_case} NO")
                    break
            else:
                print(f"#{test_case} YES")