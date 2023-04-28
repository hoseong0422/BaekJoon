data = [input() for i in range(int(input()))]

data = list(set(data))
data.sort()
data.sort(key=lambda x : len(x))
print(*data, sep='\n')