N = int(input())

for _ in range(N):
    answer = 0
    p, s = map(str, input().split())
    answer += p.count(s)
    for i in (p.split(s)):
        if i != '':
            answer += len(i)
    print(answer)