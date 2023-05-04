def solution(code):
    mode = 0
    answer = ''
    for i in range(len(code)):
        if mode == 0:
            if code[i] == '1':
                mode = 1
                continue
            elif code[i] != '1' and i % 2 == 0:
                answer += code[i]
        else:
            if code[i] == '1':
                mode = 0
                continue
            elif code[i] != '1' and i % 2 != 0:
                answer += code[i]
    if len(answer) == 0:
        answer = 'EMPTY'
    return answer