T = int(input())

for test_case in range(1, T+1):
    N = int(input())  # 버스 노선 수

    cnts = [0] * 5001  # 배열의 개수가 주어졌을 때는 바로 사용하자!
    for _ in range(N):
        A, B = map(int, input().strip().split())
        for i in range(A, B + 1):
            cnts[i] += 1

    P = int(input())

    stops = [0] * P
    for i in range(P):
        stops[i] = cnts[int(input().strip())]

    print(f"#{test_case}", *stops)
