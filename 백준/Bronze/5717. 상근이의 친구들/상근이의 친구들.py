while True:
    M , F = map(int,input().split())
    if M == 0 and F == 0:
        break

    if 1 <= M <= 5 and 1<= F <= 5:
        sum = M + F
        print(sum)