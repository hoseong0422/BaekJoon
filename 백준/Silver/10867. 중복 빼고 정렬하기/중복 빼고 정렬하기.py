N = int(input())
data = list(map(int, input().split()))

data = sorted(set(data))
data = list(data)
print(*data, sep=' ')