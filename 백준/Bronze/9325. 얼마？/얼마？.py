N = int(input())
for _ in range(N):
    P = int(input())
    T = int(input())
    for _ in range(T):
        q, p = map(int, input().split())
        P += q * p
    print(P)