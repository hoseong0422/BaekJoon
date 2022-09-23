M = int(input())
N = int(input())
prime_num = []

for i in range(M, N+1):
    cnt = 0
    for j in range(2, i+1):
        if i % j == 0:
            cnt += 1
    if cnt == 1:
        prime_num.append(i)

if len(prime_num) > 0:
    prime_num.sort()
    print(sum(prime_num), prime_num[0], sep='\n')
else:
    print(-1)