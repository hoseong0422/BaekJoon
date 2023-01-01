data = list(map(int, input().split()))

asc = [i for i in range(1, 9)]
desc = asc[:]
desc.sort(reverse=True)

if data == asc:
    print('ascending')
elif data == desc:
    print('descending')
else:
    print('mixed')