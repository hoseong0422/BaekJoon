N = int(input())
answer = 0
for _ in range(N):
    data = input().split('-')[-1]
    if int(data) <= 90:
        answer += 1
print(answer)