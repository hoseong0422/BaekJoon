N, M = map(int, input().split())
data = [0 for i in range(N)]
for _ in range(M):
    i, j, k = map(int, input().split())
    for b in range(i-1,j):
        data[b] = k
print(*data, sep=' ')