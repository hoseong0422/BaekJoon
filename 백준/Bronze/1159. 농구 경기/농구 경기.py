from collections import defaultdict

N = int(input())
players = defaultdict(int)

for _ in range(N):
    player = input()
    players[player[0]] += 1

keys = sorted([k for k, v in players.items() if v >= 5])

if keys:
    print(''.join(keys))
else:
    print('PREDAJA')
