def solution(a, d, included):
    answer = 0
    num = 0
    for i in range(len(included)):
        if i == 0 :
            num += a
        else:
            num += d
        if included[i] == True:
            answer += num
    return answer