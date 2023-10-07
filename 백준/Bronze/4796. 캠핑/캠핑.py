cnt = 0
while True:
    L, P, V = map(int, input().split())
    cnt += 1
    if L == P == V == 0:
        break
    full_day = (V // P * L)
    if (V % P) <= L:
        extra_day = (V % P)
    else:
        extra_day = L
    print(f"Case {cnt}: {full_day + extra_day}")