while True:
    N = int(input())
    if N == -1:
        break
    yak = []
    for i in range(1, N):
        if N % i == 0:
            yak.append(i)

    if N == sum(yak):
        answer = ' + '.join([str(i) for i in yak])
        print(f'{N} = {answer}')
    else:
        print(f'{N} is NOT perfect.')