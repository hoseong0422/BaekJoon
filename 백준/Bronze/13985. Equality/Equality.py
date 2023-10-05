data = list(map(str, input().split(' ')))

if int(data[0]) + int(data[2]) == int(data[-1]):
    print('YES')
else:
    print('NO')