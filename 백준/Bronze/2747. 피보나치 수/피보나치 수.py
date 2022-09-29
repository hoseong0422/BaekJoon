N = int(input()) + 1
fib = [0 for _ in range(N)]
for i in range(N):
    if i == 0:
        fib[i] = 0
    elif i == 1:
        fib[i] = 1
    else:
        fib[i] = fib[i-2] + fib[i-1]
print(fib[-1])