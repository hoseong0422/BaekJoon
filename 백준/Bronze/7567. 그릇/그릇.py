d = input()
h = 0
for i in range(len(d)):
    if i == 0:
        h += 10
    elif d[i] == d[i-1]:
        h += 5
    else:
        h += 10
print(h)