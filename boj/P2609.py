A, B = map(int, input().split())

x = A
y = B
while x % y != 0:
    r = x % y
    x = y
    y = r

print(y)
print(int(A*B/y))