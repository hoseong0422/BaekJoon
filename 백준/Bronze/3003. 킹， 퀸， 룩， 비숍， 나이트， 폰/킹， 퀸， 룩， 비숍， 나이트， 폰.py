base = [1, 1, 2, 2, 2, 8]
data = list(map(int, input().split(" ")))
for i in range(len(data)):
    data[i] = base[i] - data[i]
print(str(data)[1:-1].replace(",", ""))