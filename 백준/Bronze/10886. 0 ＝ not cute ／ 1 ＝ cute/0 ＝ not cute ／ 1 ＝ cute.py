N = int(input())
list_a = []
list_b = []

for i in range (N):
    someone = int(input())
    if someone == 1:
        list_a.append(1)
    else:
        list_b.append(0)

if list_a.count(1) > list_b.count(0):
    print("Junhee is cute!")

else :
    print("Junhee is not cute!")   