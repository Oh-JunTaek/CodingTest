A, B = map(int,input().split())

if 1 <= A <= 10000 and 1<= B <= 10000:
    add = A + B
    sub = A - B
    mul = A * B
    div = A // B
    mod = A % B
    print(add)
    print(sub)
    print(mul)
    print(div)
    print(mod)
else :
    print("입력 값을 확인해 주세요.")