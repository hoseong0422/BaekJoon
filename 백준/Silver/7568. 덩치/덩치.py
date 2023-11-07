N = int(input())

data = []
answer = []

for i in range(N):
    a, b = map(int, input().split())
    data.append((a, b))

for i in range(N):
    cnt = 0
    for j in range(N):
        if data[i][0] < data[j][0] and data[i][1] < data[j][1]:
            cnt += 1
    answer.append(cnt + 1)

for ans in answer:
    print(ans, end=' ')