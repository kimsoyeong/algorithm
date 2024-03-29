T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())  # dump 횟수
    boxes = list(map(int, input().strip().split()))

    for _ in range(N):
        # dump
        boxes[boxes.index(min(boxes))] += 1
        boxes[boxes.index(max(boxes))] -= 1

    print(f"#{test_case} {max(boxes) - min(boxes)}")