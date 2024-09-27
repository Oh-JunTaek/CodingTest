N, M = map(int, input().split())
max_sum = 0

while True:
    cards = list(map(int, input().split()))
    if len(cards) == N:
        break
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            card_sum = cards[i] + cards[j] + cards[k]
            if card_sum <= M:
                max_sum = max(max_sum, card_sum)

print(max_sum)