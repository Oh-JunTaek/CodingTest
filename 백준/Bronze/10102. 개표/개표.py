V = int(input())

while True:
    vote = list(input())
    if len(vote) == V:
        break
        
count_A = vote.count('A')
count_B = vote.count('B')

if count_A > count_B:
    print("A")
elif count_A < count_B:
    print("B")
else:
    print("Tie")