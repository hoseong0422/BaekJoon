while True:
    data = input()

    if data == '#':
        break

    parity = data[-1]
    answer = data[:-1]
    bitcnt = answer.count('1')

    if parity == 'e':
        if bitcnt % 2 == 0:
            answer += '0'
        else:
            answer += '1'
    else:
        if bitcnt % 2 == 0:
            answer += '1'
        else:
            answer += '0'
    print(answer)