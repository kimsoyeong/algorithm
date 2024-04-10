T = int(input())


def dfs(n, sm, cnt):
    global ans  # 전역 변수 선언

    # 가지치기: 가장 마지막에 고민.. 가장 위에서 처리
    if sm > K:  # 이미 초과.. (이 문제는 음수가 없으므로)
        return

    # 종료 조건 (n(index)에 관련)
    if n == 12:  # 끝까지 왔을 때
        # 정답 처리
        if sm == K and N == cnt:  # cnt: 사용한 숫자의 개수
            # 정답
            ans += 1
        return

    # 사용(포함) O
    dfs(n + 1, sm + lst[n], cnt + 1)

    # 사용(포함) X
    dfs(n + 1, sm, cnt)


for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    lst = [n for n in range(1, 13)]

    ans = 0
    dfs(0, 0, 0)
    print(f"#{test_case} {ans}")