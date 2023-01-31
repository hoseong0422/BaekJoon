N = int(input())
for _ in range(N):
    p = int(input())
    
    max_price = 0
    max_index = 0
    players = []
    for i in range(p):
        data = list(map(str, input().split()))
        if int(data[0]) > max_price:
            max_price = int(data[0])
            max_index = i
        players.append(data)
    print(players[max_index][1])