N = int(input())
money = 1000 - N
coins = [500, 100, 50, 10, 5, 1]
cnt = 0
for coin in coins:
    cnt += money // coin
    money = money % coin
    if money == 0:
        print(cnt)
        break