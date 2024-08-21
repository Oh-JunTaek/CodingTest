K, N, M = map(int, input().split())

required_amount = K * N  # 필요한 총 금액
shortfall = required_amount - M  # 부족한 금액 계산

if shortfall > 0:
    print(shortfall)  # 부족한 금액 출력
else:
    print(0)  # 부족하지 않으면 0 출력
