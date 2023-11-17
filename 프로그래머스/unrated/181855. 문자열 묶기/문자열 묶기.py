def solution(strArr):
    answer = 0
    data = [len(i) for i in strArr]
    
    for i in set(data):
        if data.count(i) > answer:
            answer = data.count(i)
    return answer