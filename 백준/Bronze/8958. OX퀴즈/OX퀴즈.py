T = int(input())

for i in range (T):
    test = input()
    score = 0
    consecutive_O = 0

    for char in test:
        if char == 'O':
            consecutive_O += 1
            score += consecutive_O
        else:
            consecutive_O = 0

    print(score)