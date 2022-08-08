N = int(input())
data = list(map(int, input().split()))
data.sort()
min_list = []
for i in range(len(data)):
    min_list.append(sum(data[i::-1]))
print(sum(min_list))