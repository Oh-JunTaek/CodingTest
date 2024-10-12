import math

# N을 입력받음
N = int(input())

# 소인수분해 결과 출력
def prime_factorization(N):
    # 2부터 sqrt(N)까지 나누기
    for i in range(2, int(math.sqrt(N)) + 1):
        while N % i == 0:  # i로 나누어 떨어지면 계속 나눔
            print(i)
            N //= i  # N을 i로 나눈 값으로 업데이트
    # 마지막으로 남은 수가 1보다 크다면 그것도 소수이므로 출력
    if N > 1:
        print(N)

if N > 1:  # N이 1이 아닌 경우에만 소인수분해를 수행
    prime_factorization(N)
