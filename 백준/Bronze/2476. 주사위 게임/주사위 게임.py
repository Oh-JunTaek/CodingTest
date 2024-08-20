N = int(input())  # 참가자 수 입력
max_prize = 0  # 최대 상금을 저장할 변수 초기화

for i in range(N):
    A, B, C = map(int, input().split())
    
    if A == B == C:
        prize = 10000 + (A * 1000)
    elif A == B or A == C:
        prize = 1000 + (A * 100)
    elif B == C:
        prize = 1000 + (B * 100)
    else:
        prize = max(A, B, C) * 100
    
    if prize > max_prize:
        max_prize = prize

print(max_prize)
