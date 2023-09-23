answer = 0
arithmetic = ''
while True:
    data = input()
    if data == '=':
        break
    if data.isdigit():
        if arithmetic == '':
            answer += int(data)
        elif arithmetic == '+':
            answer += int(data)
        elif arithmetic == '-':
            answer -= int(data)
        elif arithmetic == '*':
            answer *= int(data)
        elif arithmetic == '/':
            answer //= int(data)    
    else:
        arithmetic = data
print(answer)