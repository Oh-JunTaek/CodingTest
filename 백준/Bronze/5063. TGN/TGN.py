N = int(input())

ad = []
plus = "do not advertise"
zero = "does not matter"
minus = "advertise"

for i in range(N):
    r, e , c = map(int,input().split())
    if r > e - c:
        ad.append(plus)
    elif r == e - c:
        ad.append(zero)
    else :
        ad.append(minus)

for result in ad:
    print(result)