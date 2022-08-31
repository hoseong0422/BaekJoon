N = int(input())

for i in range(N):
    print(((i+1) * '*') + (' ' * ((N - (i + 1)) * 2)) + ((i+1)*'*'))
for i in reversed(range(N)):
    print(('*' * (i)) + (' ' * ((N-i) * 2)) + ('*' * (i)))