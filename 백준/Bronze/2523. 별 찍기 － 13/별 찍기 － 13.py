N = int(input())
for i in range(1,N+1):
    print((i) * '*')
for i in reversed(range(N)):
    if i == 0:
        break
    print(i * '*')