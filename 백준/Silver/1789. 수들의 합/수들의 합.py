S = int(input())
some_n = 0
n = 0

for i in range (1 , S + 1):
    some_n += i
    if some_n > S:
        break
    n += 1

print(n)