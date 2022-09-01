data = (input())
lst = []
for i in data:
    lst.append(int(i))
lst.sort(reverse=True)
print(''.join(str(s) for s in lst))