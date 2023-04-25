max_score = 0
a, b, c = map(int, input().split())
N = int(input())
for _ in range(N):
    scores = []
    for _ in range(3):
        p1, p2, p3 = map(int, input().split())
        score = (a * p1) + (b * p2) + (c * p3)
        scores.append(score)
    if sum(scores) > max_score:
        max_score = sum(scores)
print(max_score)