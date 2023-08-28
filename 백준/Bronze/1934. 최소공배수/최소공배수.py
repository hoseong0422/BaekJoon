def get_gcd(A, B):
    while B:
        A, B = B, A % B
    return A

def get_lcm(A, B):
    return A * B // get_gcd(A, B)

N = int(input())
for _ in range(N):
    A, B = map(int, input().split())

    print(get_lcm(A, B))