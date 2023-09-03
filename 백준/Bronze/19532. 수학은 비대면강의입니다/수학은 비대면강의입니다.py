a, b, c, d, e, f = map(int, input().split())

for i in range(0, 1000):
    for j in range(0 , 1000):
        if a * i + b * j == c and d * i + e * j == f:
            print(i, j, sep=' ')
            break
        elif a * -i + b * j == c and d * -i + e * j == f:
            print(-i, j, sep=' ')
            break
        elif a * i + b * -j == c and d * i + e * -j == f:
            print(i, -j, sep=' ')
            break
        elif a * -i + b * -j == c and d * -i + e * -j == f:
            print(-i, -j, sep=' ')
            break