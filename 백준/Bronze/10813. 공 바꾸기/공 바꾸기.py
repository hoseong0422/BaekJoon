N, M = map(int, input().split())
buckets = [i for i in range(1, N+1)]
for _ in range(M):
    i, j = map(int, input().split())
    if i == j:
        continue
    else:
        temp = buckets[i-1]
        buckets[i-1] = buckets[j-1]
        buckets[j-1] = temp
print(*buckets, sep=' ')