from string import ascii_lowercase

alphabet_list = list(ascii_lowercase)
alphabet_list

while True:
    data = input()
    if data == '*':
        break
    if len(set(data.replace(' ', ''))) == len(alphabet_list):
        print('Y')
    else:
        print('N')