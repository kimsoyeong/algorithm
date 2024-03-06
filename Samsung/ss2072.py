T = int(input())

for test_case in range(1, T+1):
    sum = 0
    for n in list(map(int, input().split())):
         if n%2 != 0: sum += n

    print(f"#{test_case} {sum}")