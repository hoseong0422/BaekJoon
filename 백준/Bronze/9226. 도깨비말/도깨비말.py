check = ['a', 'e', 'i', 'o', 'u']

while True:
    data = input()
    if data == '#':
        break
    while True:
        for i in data:
            if 'a' not in data and 'e' not in data and 'i' not in data and 'o' not in data and 'u' not in data:
                answer = data + 'ay'
                print(answer)
                break

            if i not in check:
                data = data[1:]+data[0]
            else:
                answer = data + 'ay'
                print(answer)
                break
        break