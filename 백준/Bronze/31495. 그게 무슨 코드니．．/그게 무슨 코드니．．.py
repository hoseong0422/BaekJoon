data = input()


if data[0] != '"' or data[-1] != '"' or data.count('"') % 2 == 1 or len(data.replace('"', '')) == 0:
    print("CE")
else:
    print(data.replace('"', ''))
