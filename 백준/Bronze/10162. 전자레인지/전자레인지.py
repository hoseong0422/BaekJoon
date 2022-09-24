A, B, C = 300, 60, 10

N = int(input())
if N % C != 0:
    print(-1)
else:
    A_cnt = N // A
    B_cnt = (N % A) // B
    C_cnt = ((N % A) % B) // C

    print(A_cnt, B_cnt, C_cnt)