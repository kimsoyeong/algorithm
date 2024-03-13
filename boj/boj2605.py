N = int(input())  # 학생 수

# 학생들 원래 순서
students = [i for i in range(1, N+1)]

# 학생 들이 뽑은 번호
cards = list(map(int, input().strip().split()))

for i in range(1, N):
    tmp = students[i]
    students[i - cards[i] + 1: i + 1] = students[i - cards[i]: i]
    students[i - cards[i]] = tmp

print(*students)