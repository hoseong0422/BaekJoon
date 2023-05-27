def solution(strArr):
    answer = []
    for i in range(len(strArr)):
        i += 1
        if i % 2 == 0:
            answer.append(strArr[i-1].upper())
        else:
            answer.append(strArr[i-1].lower())
    return answer