N = int(input())
for i in range(N):
    data = input().split(' ')
    if len(data) != 1:
        data = data[::-1]
    print(f"Case #{i+1}: " + ' '.join(data))