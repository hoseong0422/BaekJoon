N = int(input())
data = list(map(int, input().split()))
prime_cnt = 0

for i in data:
    cnt = 0
    if (i == 1):    
        continue
    for j in range(2 , i):
        if (i % j == 0):
            cnt += 1
    if (cnt == 0):
        prime_cnt += 1

print(prime_cnt)