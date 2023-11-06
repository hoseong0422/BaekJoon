N = int(input())

names = list(map(str, input().split()))
name_dict = {}

for name in names:
    name_dict[name] = 0

for _ in range(N):
    picked = list(map(str, input().split()))
    
    for p in picked:
        name_dict[p] += 1

lst_names = list(name_dict.items())
lst_names.sort(key = lambda x :(-x[1], x[0]))

for name in lst_names:
    print(name[0], name[1], sep=' ')