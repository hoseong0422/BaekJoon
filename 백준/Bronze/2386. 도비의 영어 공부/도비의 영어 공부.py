while True:
    data = input()
    s = data[0]
    sentence = data[1:]
    sentence = sentence.lower()
    if s == '#':
        break
    print(f'{s} {sentence.count(s)}')