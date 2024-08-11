R1, S = map(int,input().split())

R2 = (2 * S) - R1

if -1000 <= R1 <= 1000 and -1000 <= S <= 1000:
    print(R2)

else :
    print("입력값을 확인하세요")

