A = list(map(int, input().split()))
B = list(map(int, input().split()))

bj = A[0] * B[1] + B[0] * A[1]
bm = A[1] * B[1]

def get_gcd(A, B):
    while B:
        A, B = B, A % B
    return A


while True:
    gcd = get_gcd(bj, bm)
    
    if gcd == 1:
        break
    bj //= gcd
    bm //= gcd

print(bj, bm, sep=' ')