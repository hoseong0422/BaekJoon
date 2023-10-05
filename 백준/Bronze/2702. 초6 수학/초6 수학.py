def get_gcd(A, B):
    while B:
        A, B = B, A % B
    return A

def get_lcm(A, B):
    gcd = get_gcd(A, B)
    return A * B // gcd, gcd

N = int(input())

for _ in range(N):
    A, B = map(int, input().split())
    lcm, gcd = get_lcm(A, B)
    print(lcm, gcd, sep=' ')