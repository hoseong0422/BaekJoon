N = int(input())
data = list(map(int, input().split()))

order = [i for i in range(1, N + 1)]

answer = 0

for i in range(N):
    if order[i] != data[i]:
        answer += 1

print(answer)