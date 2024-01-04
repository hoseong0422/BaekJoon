data = input()
for d in data:
    temp = str(ord(d))
    num = sum([int(i) for i in temp])
    print(d * num)