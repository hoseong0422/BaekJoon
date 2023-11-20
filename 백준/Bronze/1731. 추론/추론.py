N = int(input())

data = [int(input()) for i in range(N)]

if data[1] - data[0] == data[2] - data[1]:
    db = data[1] - data[0]
    print(data[-1] + db)
elif data[1] // data[0] == data[2] // data[1]:
    dc = data[1] // data[0]
    print(data[-1] * dc)