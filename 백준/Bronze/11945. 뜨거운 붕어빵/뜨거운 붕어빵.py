N, M = map(int, input().split())

data = [str(input()) for i in range(N)]

for i in data:
    print(i[::-1])