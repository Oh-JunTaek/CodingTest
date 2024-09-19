T = int(input())

A = 300
B = 60
C = 10

if T % 10 != 0:
    print(-1)
else:
    count_A = T // A
    T %= A

    count_B = T // B
    T %= B

    count_C = T // C

    print(count_A, count_B, count_C)