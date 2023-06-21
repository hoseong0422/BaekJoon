N = int(input())

for _ in range(N):
    name = input()
    data = name.lower()
    
    if data.count('g') > data.count('b'):
        print(f'{name} is GOOD')
    elif data.count('g') < data.count('b'):
        print(f'{name} is A BADDY')
    else:
        print(f'{name} is NEUTRAL')