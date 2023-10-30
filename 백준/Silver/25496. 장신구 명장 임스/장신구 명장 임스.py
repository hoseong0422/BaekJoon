P, N = map(int, input().split())
accs = list(map(int, input().split()))

accs.sort()

answer = 0
for i in range(N):
    if P < 200:
        answer += 1
        P += accs[i]
    else:
        break
print(answer)