unit_dict = {
    'kg' : 2.2046,
    'l' : 0.2642,
    'lb' : 0.4536,
    'g' : 3.7854
}

N = int(input())
for _ in range(N):
    v, u = map(str, input().split())
    if u == 'kg':
        converted_v = round(float(v) * unit_dict[u], 4)
        print(f'{converted_v:.4f} lb')
    elif u == 'lb':
        converted_v = round(float(v) * unit_dict[u], 4)
        print(f'{converted_v:.4f} kg')
    elif u == 'l':
        converted_v = round(float(v) * unit_dict[u], 4)
        print(f'{converted_v:.4f} g')
    elif u == 'g':
        converted_v = round(float(v) * unit_dict[u], 4)
        print(f'{converted_v:.4f} l')