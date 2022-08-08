N, K = map(int, input().split(" "))
money = []
coins = 0
for i in range(N):
    money.append(int(input()))
for coin in money[::-1]:
    if K >= coin:
        coins += K // coin
        K = K % coin
    else:
        continue
print(coins)