arr = []

for i in range(9):
    arr.append(int(input()))

total = sum(arr)

f = False


def solution():
    for i in range(8):
        for j in range(i + 1, 9):
            if total - arr[i] - arr[j] == 100:
                a = arr[i]
                b = arr[j]
                return a, b


a, b = solution()

for e in sorted(arr):
    if e != a and e != b:
        print(e)
