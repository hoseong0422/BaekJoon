N = int(input())

for _ in range(N):
    data = input()
    if len(data) >= 6 and len(data) <= 9: 
        print('yes')
    else:
        print('no')