N = int(input())

while True:
    if 1 <= N <= 9:
        break

for i in range (1, 10):
    result = N * i
    print(f"{N} * {i} = {result}")