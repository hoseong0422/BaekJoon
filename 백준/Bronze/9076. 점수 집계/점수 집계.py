N = int(input())

for _ in range(N):
    data = list(map(int, input().split()))
    data.remove(max(data))
    data.remove(min(data))

    if max(data) - min(data) >= 4:
        print("KIN")
    else:
        print(sum(data))