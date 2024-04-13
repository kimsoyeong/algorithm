from collections import deque

dy, dx = [1, -1, 0, 0], [0, 0, -1, 1]

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    atoms = deque()
    for _ in range(N):
        # [0]: x(j) [1]: y(i) [2]: d [3]: K
        x, y, d, k = map(int, input().split())
        atoms.append([x * 2, y * 2, d, k])  # .5초 등에 충돌하는 경우를 고려해서 2배해줌

    ans = 0  # 정답: 방출 에너지

    while len(atoms) >= 2:  # 살아남은 원자가 2개 이상 존재할 때만 충돌가능. 혼자 있는 데 충돌할리가 있나.
        n = len(atoms)

        # [1] 새로운 좌표 계산: 1칸 이동
        for i in range(n):
            atoms[i][0] += dx[atoms[i][2]]  # nx
            atoms[i][1] += dy[atoms[i][2]]  # ny

        # [2] 충돌 후보 찾기: key를 좌표로 한 딕셔너리 사용
        crash = {}
        for a in atoms:
            if (a[0], a[1]) in crash:
                crash[(a[0], a[1])].append(a)
            else:
                crash[(a[0], a[1])] = [a]

        # [3] atoms 배열 재정의
        atoms = []  # 초기화
        for key in crash:
            if len(crash[key]) >= 2:  # 여러 개 -> 충돌!
                for a in crash[key]:
                    ans += a[3]  # 원자의 에너지 값 K
            else:
                a = crash[key][0]
                if -2000 <= a[0] <= 2000 and -2000 <= a[1] <= 2000:  # 좌표 범위 확인
                    atoms.append(a)

    print(f"#{test_case} {ans}")
