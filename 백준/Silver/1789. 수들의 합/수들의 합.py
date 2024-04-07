N = int(input())

S = 0
for i in range(1, N+1):

    S += i
    if S == N:
        print(i)
        break
    elif S > N:
        print(i - 1)
        break
