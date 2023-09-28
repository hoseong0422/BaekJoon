data = list(map(int, input().split()))

sorted_data = sorted(data)
while True:
    if data == sorted_data:
        break
    for i in range(1, len(data)):
        if data[i-1] > data[i]:
            temp_num = data[i]
            data[i] = data[i-1]
            data[i-1] = temp_num
            print(*data, sep=' ')