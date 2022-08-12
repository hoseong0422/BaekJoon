data = input()
target = input()
N = len(data)
count = 0
index = 0
for i in range(N):
    if index > i:
        continue
    if data[i:len(target)+i] == target:
        count += 1
        index = i + len(target)
        
print(count)