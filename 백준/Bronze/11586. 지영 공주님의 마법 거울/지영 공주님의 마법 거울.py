N = int(input())
data = [input() for i in range(N)]
K = int(input())
if K == 1:
    print(*data, sep='\n')
elif K ==2:
    for d in data:
        print(d[::-1])
elif K ==3:
    for d in data[::-1]:
        print(d)