N = int(input())

for i in range(N):
    data = input().split()
    for j in range(len(data)):
        if len(data[j]) == 4:
            data[j] = '*' * 4

    

    if i != N - 1:
        print(' '.join(data) + '\n')
    else:
        print(' '.join(data))
