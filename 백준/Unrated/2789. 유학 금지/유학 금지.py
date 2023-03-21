a = input()
b = 'CAMBRIDGE'
lst_a = [i for i in a]
for i in a:
    if i in b:
        lst_a.remove(i)
print(''.join(lst_a))