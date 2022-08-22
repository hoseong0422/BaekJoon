N = int(input())
time = []

for _ in range(N):
    start, end = map(int, input().split())
    time.append([start, end])
time = sorted(time, key=lambda x : (x[1], x[0]))

last = 0
count = 0

for i, j in time:
    if i >= last:
        count += 1
        last = j
print(count)