while True:
    data = input()
    if data == 'EOI':
        break
    if 'nemo' in data.lower():
        print('Found')
    else:
        print('Missing')