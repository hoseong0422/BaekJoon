data = input()
if 'AND' in data:
    if 'true' in data and 'false' not in data:
        print('true')
    else:
        print('false')
else:
    if 'true' in data:
        print('true')
    else:
        print('false')