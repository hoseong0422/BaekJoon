data = list(map(int, input().split()))
data.sort()

if sum(data[:2]) > data[-1]:
    print(sum(data))
else:
    print(sum(data[:2]) * 2 -1)