N, M = map(int, input().split())

answer = 0
for _ in range(N):
    data = input()
    if data.count('O') >= M // 2 + 1:
        answer += 1

print(answer)