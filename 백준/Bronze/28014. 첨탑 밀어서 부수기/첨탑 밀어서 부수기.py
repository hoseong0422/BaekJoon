N = int(input())
data = list(map(int, input().split()))

cnt = 0

for i in range(len(data)):
    if i == 0:
        cnt += 1
    elif data[i] >= data[i-1]:
        cnt += 1
print(cnt)