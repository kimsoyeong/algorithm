T = int(input())

q = []
for _ in range(T):
    str = input()
    q = []
    flag = True
    for s in str:
        if s == "(":
            q.append(s)
        elif s == ")":
            if len(q) == 0:
                flag = False
                break
            q.pop()
    if not flag or len(q) > 0:
        print("NO")
    else:
        print("YES")