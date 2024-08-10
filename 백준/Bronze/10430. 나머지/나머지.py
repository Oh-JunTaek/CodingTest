A, B, C = map(int, input().split())

if 2 <= A <= 10000 and 2 <= B <= 10000 and 2 <= C <= 10000:
    sum_01 = (A + B) % C
    sum_02 = ((A % C) + (B % C)) % C
    sum_03 = (A * B) % C
    sum_04 = ((A % C) * (B % C)) % C
    
    print(sum_01)
    print(sum_02)
    print(sum_03)
    print(sum_04)
else:
    print("입력 값을 확인해주세요")
