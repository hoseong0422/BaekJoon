scales = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
row = 0
while True:
    data = input()

    if data == '***':
        break
    
    if row % 2 == 0:
        scale = data.split(' ')
        row += 1
    else:
        move = int(data)
        
        answer = []
        for s in scale:
            if s not in scales:
                if s[-1] == 'b':
                    s = alpha[alpha.index(s[0]) - 1] + '#'
                else:
                    s = alpha[alpha.index(s[0]) + 1]
                
            if scales.index(s) + move <= 11 and scales.index(s) + move >= 0:
                answer.append(scales[scales.index(s) + move])
            elif scales.index(s) + move > 11:
                answer.append(scales[((scales.index(s) + move) % 11) - 1])
            elif scales.index(s) + move < 0:
                answer.append(scales[scales.index(s) + move])
                
        print(*answer, sep=' ')
        row += 1