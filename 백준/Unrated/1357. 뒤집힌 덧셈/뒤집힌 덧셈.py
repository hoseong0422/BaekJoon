def Rev(x):
    x = str(x)[::-1]
    return int(x)

x, y =map(int, input().split())

print(Rev(Rev(x) + Rev(y)))