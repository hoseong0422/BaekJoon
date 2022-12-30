N = 5
data = []
for _ in range(N):
    num = int(input())
    if num < 40:
        data.append(40)
    else:
        data.append(num)
        
print(sum(data) // N)