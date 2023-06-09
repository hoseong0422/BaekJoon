def solution(myString):
    answer = []
    cnt = 0
    for i in range(len(myString)):
        if i == len(myString) - 1:
            if myString[i] == 'x':
                answer.append(cnt)
                cnt = 0
                answer.append(cnt)
                return answer
            else:
                cnt += 1
                answer.append(cnt)
                return answer
        elif myString[i] == 'x':
            answer.append(cnt)
            cnt = 0
        else:
            cnt += 1