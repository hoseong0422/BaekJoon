while True:
    data = input()
    if data == '0':
        break

    while True:
        lst = [int(i) for i in data]
        if sum(lst) < 10:
            print(sum(lst))
            break   
        else:
            data = str(sum(lst))