T = int(input())

results = []

for _ in range(T):
    N = int(input())

    max_L = -1
    S_most = ""
    
    for _ in range(N):
        S, L = input().split() # S는 문자열 L은숫자를 공백으로 입력받는 방법?
        L = int(L)
    
        if L > max_L:
            max_L = L
            S_most = S

    results.append(S_most)
        
for result in results:
    print(result)