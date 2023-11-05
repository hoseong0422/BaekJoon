low_0 = ['`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=']
low_1 = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '[', ']', '\\']
low_2 = ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';' ,'\'']
low_3 = ['Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '/']

while True:
    try:
        data = input()
        
        answer = ''
        for d in data:
            if d in low_0:
                answer += low_0[low_0.index(d) - 1]
            elif d in low_1:
                answer += low_1[low_1.index(d) - 1]
            elif d in low_2:
                answer += low_2[low_2.index(d) - 1]
            elif d in low_3:
                answer += low_3[low_3.index(d) - 1]
            elif d == ' ':
                answer += ' '

        print(answer)
    
    except EOFError:
        break