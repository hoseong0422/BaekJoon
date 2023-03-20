N, K = map(int, input().split())
yak = []
for i in range(1, N+1):
    if N % i == 0:
        yak.append(i)

if len(yak) >= K:
    print(yak[K-1])
else:
    print(0)