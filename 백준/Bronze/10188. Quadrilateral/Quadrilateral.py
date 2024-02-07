N = int(input())

for i in range(N):
    a, b = map(int, input().split())

    for _ in range(b):
        print('X' * a)
    
    if i < N -1:
        print(' ')