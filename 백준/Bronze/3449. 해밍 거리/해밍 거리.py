N = int(input())
for _ in range(N):
    a = int(input(), 2)
    b = int(input(), 2)
    xor_result = a ^ b
    
    distance = bin(xor_result).count('1')
    print(f"Hamming distance is {distance}.")