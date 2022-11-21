def solution(quiz):
    answer = []
    for i in quiz:
        a = i.split('=')[0].split(' ')[0]
        b = i.split('=')[0].split(' ')[-1]
        arithmetic = i.split('=')[0].split(' ')[1]
        
        ans = i.split('=')[-1]
        
        if arithmetic == '-':
            if int(a) - int(b) == int(ans):
                answer.append('O')
            else:
                answer.append('X')
        else:
            if int(a) - int(b) == int(ans):
                answer.append('O')
            else:
                answer.append('X')
    return answer

def solution(quiz):
    answer = []
    for i in quiz:
        c= i.split('=')
        for j in range (len(c)):
            if eval(c[0]) == eval(c[1]):
                answer.append('O')
                break
            else:
                answer.append('X')
                break
    return answer

