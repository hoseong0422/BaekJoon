import sys

N = int(sys.stdin.readline())
data = []

for _ in range(N):
    data.append(sys.stdin.readline().split())

data.sort(key = lambda x : (int(x[0]), int(x[1])))

for d in data:
    print(d[0], d[1], sep=' ')