before = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
after =  ['N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']
answer = ''
data = input()
for i in range(len(data)):
    if data[i] == ' ':
        answer += data[i]
    elif data[i].isdigit() == True:
        answer += data[i]
    elif data[i] == data[i].upper():
        answer += after[before.index(data[i])]
    elif data[i] == data[i].lower():
        answer += after[before.index(data[i].upper())].lower()

print(answer)