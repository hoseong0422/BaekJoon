def solution(ingredient):
    answer = 0
    data = []

    for i in ingredient:
        data.append(i)
        if len(data) >= 4:
            if data[-1] == 1 and data[-2] == 3 and data[-3] == 2 and data[-4] == 1:
                data.pop()
                data.pop()
                data.pop()
                data.pop()
                answer+=1

    return answer