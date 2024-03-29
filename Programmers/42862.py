def solution(n, lost, reserve):
    answer = 0  # 체육 수업을 들을 수 있는 학생의 최대값

    lst = [1] * (n + 1)
    for e in lost:
        lst[e] -= 1
    for e in reserve:
        lst[e] += 1

    for i in range(1, n + 1):
        if lst[i] == 2:
            if i > 1 and lst[i - 1] == 0:
                lst[i] -= 1
                lst[i - 1] += 1
            elif i < n and lst[i + 1] == 0:
                lst[i] -= 1
                lst[i + 1] += 1

    for e in lst[1:]:
        if e >= 1:
            answer += 1

    return answer


print(solution(5, [2, 4], [1, 3, 5]))
print(solution(5, [2, 4], [3]))
print(solution(3, [3], [1]))
