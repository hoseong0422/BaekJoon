N = int(input())
for _ in range(N):
    even = []
    data = list(map(int, input().split()))
    for d in data:
        if d % 2 == 0:
            even.append(d)
    even.sort()
    print(sum(even), even[0])