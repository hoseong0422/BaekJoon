colors = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
value = ""
for i in range(3):
    if i == 2:
        print(int(value) * (10 ** colors.index(input())))
    else:
        value += str(colors.index(input()))