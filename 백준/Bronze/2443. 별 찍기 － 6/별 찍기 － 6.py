N = int(input())

for i, j in zip(reversed(range(1, N+1)), range(N)):
    print(' ' * j + '*' * (2 * i -1))
