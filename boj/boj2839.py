N = int(input())

cnt5 = 0
cnt3 = 0

# cnt5: 5kg 봉지 수; 봉지 수가 최소인 경우는 전부 5kg 봉지로 옮기는 경우
for cnt5 in range(N//5, -1 ,-1):  # 딱 떨어지지 않으면,  # 5kg 봉지 수를 하나 줄인다.
    cnt3 = (N - cnt5 * 5) // 3  # 남은 설탕 kg에서 가능한 3kg 봉지 개수 계산

    if cnt5 * 5 + cnt3 * 3 == N:  # 딱 떨어지는 지 확인
        print(cnt5 + cnt3)
        break
else:
    print(-1)