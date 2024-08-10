A, B = map(int, input().split())

if 0 < A < 10 and 0 < B < 10:
    # 나눗셈을 합니다.
    result = A / B
    # 결과를 소수점 이하 9자리까지 출력합니다.
    print(f"{result:.9f}")
else:
    print("입력값을 확인해 주세요")
