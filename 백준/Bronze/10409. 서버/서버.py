N, T = map(int, input().split())
total = 0
cnt = 0
jobs = list(map(int, input().split()))
if sum(jobs) <= T:
    print(len(jobs))
else:
    for job in jobs:
        if total + job <= T:
            total += job
            cnt += 1
        else:
            print(cnt)
            break