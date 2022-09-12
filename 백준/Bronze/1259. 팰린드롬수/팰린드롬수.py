while True:

    data = str(input())

    if data == '0':
        break
    elif data == data[::-1]:
        print('yes')
    else:
        print('no')