N = int(input())
data = list(map(int, input().split()))
cnt = 0
            
for i in data:
    if i == N:
        cnt += 1
print(cnt)