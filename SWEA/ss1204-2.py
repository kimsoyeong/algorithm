from collections import Counter

T = int(input())

for test_case in range(1, T + 1):
    tc_n = int(input())

    counter = Counter(list(map(int, input().split())))
    print(f"#{tc_n} {counter.most_common(1)[0][0]}")

