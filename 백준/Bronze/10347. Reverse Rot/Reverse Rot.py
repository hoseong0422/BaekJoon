target = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'

while True:
    answer = ''
    data = input().split()
    N = data[0]
    if N == '0':
        break
    temp = data[1]
    temp = temp[::-1]
    for i in range(len(temp)):
        if target.index(temp[i]) + int(N) < len(target):
            answer += target[target.index(temp[i]) + int(N)]
        else:
            answer += target[(target.index(temp[i]) + int(N)) % len(target)]
    print(answer)