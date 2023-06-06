def solution(n):
    answer = []
    for i in range(n):
        temp = []
        for j in range(n):
            if j == i:
                temp.append(1)
            else:
                temp.append(0)
        answer.append(temp)
    return answer