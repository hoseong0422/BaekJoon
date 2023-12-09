def solution(myStr):
    answer = []
    temp = ''
    for i in myStr:
        if i not in ('abc'):
            temp += i
        else:
            if temp != '':
                answer.append(temp)
                temp = ''
    if temp != '':
        answer.append(temp)

    if len(answer) == 0:
        answer.append('EMPTY')
    return answer