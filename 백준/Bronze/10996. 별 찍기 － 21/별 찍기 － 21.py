import math

N =int(input())

for _ in range(N):

    print('* ' * (math.floor(1 + ((N - 1) / 2))))
    print(' *' * (math.ceil((N - 1) / 2)))