N = int(input())
data = input()
if data.count('A') > data.count('B'):
    print('A')
elif data.count('B') > data.count('A'):
    print('B')
else:
    print('Tie')