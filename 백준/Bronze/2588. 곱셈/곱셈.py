A = int(input())
B = int(input())

c = B % 10
d = (B // 10) % 10 
e = (B // 100)


if 100 <= A <= 999 and 100<= B <= 999:
    print(A * c)
    print(A * d)
    print(A * e)
    print(A * B)

else :
    print("입력값을 확인하세요")
    