T = int(input())
results = []

for _ in range(T):
    vps = input()
    count = 0

    is_vaild = True

    for char in vps:
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1

        if count < 0 :
            is_vaild = False
            break

    if is_vaild and count == 0:
        results.append("YES")
    else:
        results.append("NO")
            
for result in results:
    print(result)