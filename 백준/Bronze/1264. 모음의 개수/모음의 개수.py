while True:
    data = input()
    if data == '#':
        break
    cnt = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in data:
        if i.lower() in vowels:
            cnt += 1
    print(cnt)