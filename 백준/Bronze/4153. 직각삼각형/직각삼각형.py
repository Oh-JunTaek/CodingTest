# 직각삼각형

result = []

while True:
    a, b, c = map(int,input().split())
    if a == 0 and b == 0 and c == 0:
        break

    a, b, c = sorted([a, b, c]
                    )
    if a**2 + b**2 == c**2:
        result.append("right")
    else:
        result.append("wrong")
    # elif a != 0 or b!= 0 or c!= 0:
    #     result.append("wrong")

for res in result:
    print(res)