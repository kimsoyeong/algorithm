def dfs2(n, sm, add, sub, mul, div):
    global mx, mn
    if n == N:
        mx = max(mx, sm)
        mn = min(mn, sm)
        return

    if add > 0:
        dfs2(n + 1, sm + A[n], add - 1, sub, mul, div)
    if sub > 0:
        dfs2(n + 1, sm - A[n], add, sub - 1, mul, div)
    if mul > 0:
        dfs2(n + 1, sm * A[n], add, sub, mul - 1, div)
    if div > 0:
        dfs2(n + 1, int(sm / A[n]), add, sub, mul, div - 1)


def dfs(n, sm):
    global mx, mn
    if n == N:
        mx = max(mx, sm)
        mn = min(mn, sm)
        return

    for i in range(4):
        if op[i] > 0:  # 연산자 남아있으면
            tmp = sm
            if i == 0:
                tmp += A[n]
            elif i == 1:
                tmp -= A[n]
            elif i == 2:
                tmp *= A[n]
            else:
                tmp = int(tmp/A[n])

            op[i] -= 1
            dfs(n+1, tmp)
            op[i] += 1


N = int(input())
A = list(map(int, input().split()))

mx = -1000000000
mn = 1000000000

# [1] 내 풀이
op = list(map(int, input().split()))
# op => [0]: + [1]: - [2]: * [3]: /
dfs(1, A[0])

# [2] 문어박사님 풀이
add, sub, mul, div = map(int, input().split())
dfs2(1, A[0], add, sub, mul, div)

print(mx)
print(mn)
