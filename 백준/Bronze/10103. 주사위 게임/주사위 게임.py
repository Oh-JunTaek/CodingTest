n = int(input())

if not( 1<= n <= 15):
    print("입력 값을 확인해 주세요")
    exit()
score_a = 100
score_b = 100

for i in range(n):
    A , B = map(int,input().split())

    if not ( 1 <= A <= 6 and 1 <= B <= 6):
        print("입력 값을 확인해 주세요")
        exit()
    if A > B: 
        score_b -= A
    elif A < B :
        score_a -= B

print (f"{score_a}")
print (f"{score_b}")