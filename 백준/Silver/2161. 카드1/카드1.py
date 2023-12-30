N = int(input())
cards = [i for i in range(1, N+1)]
floor = []

for i in range(N):
    if len(cards) == 1:
        floor.append(cards[0])
        break
    floor.append(cards[0])
    cards = cards[1:]
    cards = cards[1:] + [cards[0]]

print(*floor, sep=' ')