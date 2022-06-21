N = int(input())

for n in range(N):
    data = list(map(int, input().split(" ")))
    num = data[0]
    data = data[1:]

    average = sum(data) / num

    cnt = 0
    for score in data:
        if score > average:
            cnt += 1
    avr = cnt / num * 100
    print("{:.3f}%".format(avr))