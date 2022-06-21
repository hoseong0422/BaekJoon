N = int(input())

for n in range(N):
    data = list(input().split("X"))
    score = 0

    for d in data:
        for s in range(len(d)):
            score += (s+1)
    print(score)