uni = ['Soongsil', 'Korea', 'Hanyang']
data = list(map(int, input().split()))
if sum(data) < 100:
    print(uni[data.index(min(data))])
else:
    print('OK')