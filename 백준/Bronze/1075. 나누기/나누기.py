N = int(input())
F = int(input())
N = N // 100 * 100
i = 0
answer = ''

while True:
    if N % F == 0:
        answer = i
    else:
        i += 1
        N += 1

    if answer != '':
        if len(str(answer)) == 1:
            print(f'0{answer}')

        else:
            print(answer)
        break