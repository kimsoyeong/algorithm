from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

deq = deque()

for _ in range(n):
    s = input().split()

    if "push_back" == s[0]:
        deq.append(s[1])
    elif "push_front" in s:
        deq.appendleft(s[1])
    elif "pop_front" == s[0]:
        if len(deq) == 0:
            print(-1)
        else:
            print(deq.popleft())
    elif "pop_back" == s[0]:
        if len(deq) == 0:
            print(-1)
        else:
            print(deq.pop())
    elif "front" == s[0]:
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[0])
    elif "back" == s[0]:
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[-1])
    elif "size" == s[0]:
        print(len(deq))
    elif "empty" == s[0]:
        if len(deq) == 0:
            print(1)
        else:
            print(0)
