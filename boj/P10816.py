import sys

input = sys.stdin.readline

N = int(input())  # card number
cards = list(map(int, input().split()))  # Cards
cards.sort()

dic = {}

for c in cards:
    if c in dic:
        dic[c] += 1
    else:
        dic[c] = 1

M = int(input())
nums = list(map(int, input().split()))

for n in nums:
    s = 0
    e = N - 1
    if n not in dic:
        print(0, end=" ")
    else:
        while s <= e:
            mid = (s + e) // 2

            if cards[mid] == n:
                break
            if cards[mid] > n:
                e = mid - 1
            else:
                s = mid + 1

        print(dic[n], end=" ")
