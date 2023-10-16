data = input()

answer = ''
for i in data:
    if i in ['E', 'I']:
        if i == 'E':
            answer += 'I'
        else:
            answer += 'E'
    elif i in ['S', 'N']:
        if i == 'S':
            answer += 'N'
        else:
            answer += 'S'
    elif i in ['T', 'F']:
        if i == 'T':
            answer += 'F'
        else:
            answer += 'T'
    else:
        if i == 'J':
            answer += 'P'
        else:
            answer += 'J'
print(answer)