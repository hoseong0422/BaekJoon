T = int(input())
for _ in range(T):
    data = list(map(str, input().split()))
    num = float(data[0])
    math_exp = data[1:]
    for e in math_exp:
        if e == '@':
            num *= 3
        elif e == '%':
            num += 5
        else:
            num -= 7
    print("{:.2f}".format(num))