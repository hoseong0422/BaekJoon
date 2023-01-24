N, K = map(int, input().split())
data = list(map(int, input().split()))
data.sort(reverse=True)
print(data[K-1])