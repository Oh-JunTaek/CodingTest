T = int(input())

for i in range(T):
    A, B = map(int,input().split())
   
    if 0 < A < 10 and 0 < B < 10:
        C = A + B
        print (f"Case #{i+1}: {A} + {B} = {C}")
    else :
        print("입력 값을 확인하세요.")