N = int(input())

halli_galli = {}

for _ in range(N):
    data = input().split()
    fruit = data[0]
    n = int(data[1])
    if fruit not in halli_galli:
        halli_galli[fruit] = n
    else:
        halli_galli[fruit] += n

if 5 in halli_galli.values():
    print("YES")
else:
    print("NO")
