# 리스트를 받아둔다.
x_coord = []
y_coord = []

# x,y 입력값을 받는다 
for i in range(3):
    x, y = map(int,input().split())
    x_coord.append(x)
    y_coord.append(y)
    

# x값에서 1개만 있는 것을 찾는다
for x in x_coord:
    if x_coord.count(x) == 1:
        last_x = x
    
# y값에서 1개만 있는 것을 찾는다
for y in y_coord:
    if y_coord.count(y) == 1:
        last_y = y

print(last_x , last_y)