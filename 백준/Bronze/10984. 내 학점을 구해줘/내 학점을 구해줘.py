T = int(input())
for _ in range(T):
    N = int(input())
    grade = 0
    total = 0
    for _ in range(N):
        C, G = map(str, input().split())
        grade += int(C)
        total += int(C) * float(G)
    print(grade, round(total/grade, 1))