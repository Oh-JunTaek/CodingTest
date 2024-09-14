n = int(input())

q1 = []
q2 = []
q3 = []
q4 = []
AXIS = []

for i in range(n):
    x, y = map(int, input().split())
    
    if x > 0 and y > 0:
        q1.append(1)  # 1사분면
    elif x < 0 and y > 0:
        q2.append(1)  # 2사분면
    elif x < 0 and y < 0:
        q3.append(1)  # 3사분면
    elif x > 0 and y < 0:
        q4.append(1)  # 4사분면
    else:
        AXIS.append(1)  # 축에 있는 경우

print(f"Q1: {len(q1)}")
print(f"Q2: {len(q2)}")
print(f"Q3: {len(q3)}")
print(f"Q4: {len(q4)}")
print(f"AXIS: {len(AXIS)}")
