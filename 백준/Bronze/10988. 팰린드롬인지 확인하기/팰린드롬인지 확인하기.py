data = input()
lst = []
for i in data:
    lst.append(i)
lst = lst[::-1]
lst = ''.join(lst)
if lst == data:
    print(1)
else:
    print(0)