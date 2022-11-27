def solution(s):
    datas = s.split(" ")
    answer = []
    for data in datas:
        if data == 'Z':
            answer.pop()
        else:
            answer.append(int(data))
    return sum(answer)