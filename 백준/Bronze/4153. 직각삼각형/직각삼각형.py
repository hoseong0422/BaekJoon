while True:
    data = list(map(int, input().split()))
    data.sort()
    a = data[0]
    b = data[1]
    c = data[2]
    if a == 0 and b == 0 and c == 0:
        break
    else:
        if a*a + b*b == c*c:
            print('right')
        else:
            print('wrong')