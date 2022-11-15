def solution(order):
    answer = 0
    data = ['3', '6', '9']
    for i in str(order):
        if i in data:
            answer += 1
    return answer