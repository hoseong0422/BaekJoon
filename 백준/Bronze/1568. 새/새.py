N = int(input())
cnt = 0
while N > 0:
    for i in range(1, N+1):
        if N >= i:
            cnt += 1
            N -= i
        else:
            break
print(cnt)