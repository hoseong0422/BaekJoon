N = int(input())
data = list(map(int, input().split()))

guest = []
cnt = 0
for g in data:
    if g not in guest:
        guest.append(g)
    else:
        cnt += 1
print(cnt)