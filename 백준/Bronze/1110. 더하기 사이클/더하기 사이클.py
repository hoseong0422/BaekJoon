N = int(input())
cnt = 0
init_N = N

while True:
    if N >= 10:
        A = N // 10
        B = N % 10
    elif N < 10:
        A = 10
        B = N
    
    sum = A + B
    cnt += 1
    N = (B * 10) + (sum % 10)

    if N == init_N:
        print(cnt)
        break
    else:
        continue