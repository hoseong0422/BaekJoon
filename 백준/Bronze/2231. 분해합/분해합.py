N = int(input())

i = 1
while True:
    if i + sum([int(i) for i in str(i)]) == N:
        print(i)
        break
    elif i >= N:
        print(0)
        break
    else:
        i += 1