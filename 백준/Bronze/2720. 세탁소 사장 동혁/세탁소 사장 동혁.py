T = int(input())
for _ in range(T):
    Q, D, N, P = 0, 0, 0, 0
    exchange = int(input())
    while True:
        if exchange == 0:
            print(f'{Q} {D} {N} {P}')
            break
        if exchange >= 25:
            Q += exchange // 25
            exchange = exchange % 25
            continue
        elif exchange >= 10:
            D += exchange // 10
            exchange = exchange % 10
            continue
        elif exchange >= 5:
            N += exchange // 5
            exchange = exchange % 5
            continue
        elif exchange >= 1:
            P += exchange // 1
            exchange = exchange % 1
            continue