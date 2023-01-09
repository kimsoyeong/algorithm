students = set()

for s in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
               16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]:
    students.add(s)

for i in range(0, 28):
    students.remove(int(input()))

for s in sorted(list(students)):
    print(s)