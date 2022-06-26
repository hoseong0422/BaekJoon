cnt = int(input())
for i in range(cnt):
    data = list(input().split(" "))
    N = int(data[0])
    text = str(data[1])

    for t in text:
        print(t * N, end="")
    print("")