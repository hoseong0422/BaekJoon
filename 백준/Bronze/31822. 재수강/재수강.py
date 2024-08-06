code = input()
N = int(input())
answer = 0
for _ in range(N):
    if code[:5] == input()[:5]:
        answer += 1
print(answer)