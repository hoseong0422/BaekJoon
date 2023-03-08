data = [int(input()) for _ in range(9)]

max = data[0]
n = 1
for i in range(1, len(data)):
    if data[i] > max:
        max = data[i]
        n = i + 1

print(max)
print(n)